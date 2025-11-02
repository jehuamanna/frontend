
## Sandbox Manager

**IFrame Sandbox Implementation**:

```javascript
/**
 * Sandbox Manager
 * Handles creation and management of isolated plugin environments
 */
class SandboxManager {
  constructor(pluginManager) {
    this.pluginManager = pluginManager;
    this.sandboxes = new Map();
    this.nextSandboxId = 0;
  }
  
  /**
   * Create sandbox for plugin
   */
  async createSandbox(descriptor) {
    const sandboxType = descriptor.ui ? 'iframe' : 'worker';
    
    let sandbox;
    if (sandboxType === 'iframe') {
      sandbox = new IFrameSandbox(descriptor, this.pluginManager);
    } else {
      sandbox = new WorkerSandbox(descriptor, this.pluginManager);
    }
    
    await sandbox.create();
    
    this.sandboxes.set(descriptor.id, sandbox);
    
    return sandbox;
  }
  
  /**
   * Destroy sandbox
   */
  async destroySandbox(sandbox) {
    await sandbox.destroy();
    this.sandboxes.delete(sandbox.descriptor.id);
  }
  
  /**
   * Get sandbox by plugin ID
   */
  getSandbox(pluginId) {
    return this.sandboxes.get(pluginId);
  }
  
  /**
   * Destroy all sandboxes
   */
  destroy() {
    for (const sandbox of this.sandboxes.values()) {
      sandbox.destroy();
    }
    this.sandboxes.clear();
  }
}

/**
 * IFrame-based Sandbox (for UI plugins)
 */
class IFrameSandbox {
  constructor(descriptor, pluginManager) {
    this.descriptor = descriptor;
    this.pluginManager = pluginManager;
    this.iframe = null;
    this.window = null;
    this.messageHandlers = new Map();
    this.nextMessageId = 0;
  }
  
  /**
   * Create iframe sandbox
   */
  async create() {
    return new Promise((resolve, reject) => {
      // Create iframe element
      this.iframe = document.createElement('iframe');
      
      // Set sandbox attributes for security
      this.iframe.setAttribute('sandbox', [
        'allow-scripts',
        'allow-same-origin', // Required for postMessage
        ...(this.descriptor.permissions.includes('forms') ? ['allow-forms'] : []),
        ...(this.descriptor.permissions.includes('popups') ? ['allow-popups'] : []),
        ...(this.descriptor.permissions.includes('modals') ? ['allow-modals'] : [])
      ].join(' '));
      
      // Set CSP via meta tag in iframe content
      const csp = this.buildCSP();
      
      // Hide iframe initially
      this.iframe.style.display = 'none';
      this.iframe.style.position = 'absolute';
      this.iframe.style.width = '100%';
      this.iframe.style.height = '100%';
      this.iframe.style.border = 'none';
      
      // Setup message handler
      window.addEventListener('message', (event) => {
        this.handleMessage(event);
      });
      
      // Load complete handler
      this.iframe.onload = () => {
        this.window = this.iframe.contentWindow;
        resolve();
      };
      
      this.iframe.onerror = (error) => {
        reject(new Error(`Failed to create sandbox: ${error}`));
      };
      
      // Append to DOM
      document.body.appendChild(this.iframe);
    });
  }
  
  /**
   * Build Content Security Policy
   */
  buildCSP() {
    const directives = [
      "default-src 'self'",
      "script-src 'self' 'unsafe-eval'", // unsafe-eval needed for dynamic code
      "style-src 'self' 'unsafe-inline'",
      "img-src 'self' data: https:",
      "font-src 'self' data:",
      "connect-src 'self' https:",
      "frame-src 'none'",
      "object-src 'none'"
    ];
    
    return directives.join('; ');
  }
  
  /**
   * Load plugin code into sandbox
   */
  async load(entryPoint) {
    // Inject plugin loader script
    const loaderScript = this.createLoaderScript(entryPoint);
    
    // Write HTML to iframe
    const html = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="UTF-8">
        <meta http-equiv="Content-Security-Policy" content="${this.buildCSP()}">
        <style>
          * { margin: 0; padding: 0; box-sizing: border-box; }
          body { font-family: system-ui, -apple-system, sans-serif; }
        </style>
      </head>
      <body>
        <div id="plugin-root"></div>
        <script>${loaderScript}</script>
      </body>
      </html>
    `;
    
    const doc = this.iframe.contentDocument;
    doc.open();
    doc.write(html);
    doc.close();
    
    // Wait for plugin to initialize
    await this.waitForReady();
  }
  
  /**
   * Create plugin loader script
   */
  createLoaderScript(entryPoint) {
    return `
      (function() {
        // Setup communication bridge
        const bridge = {
          call: function(method, ...args) {
            return new Promise((resolve, reject) => {
              const id = Math.random().toString(36);
              
              const handler = (event) => {
                if (event.data.type === 'response' && event.data.id === id) {
                  window.removeEventListener('message', handler);
                  if (event.data.error) {
                    reject(new Error(event.data.error));
                  } else {
                    resolve(event.data.result);
                  }
                }
              };
              
              window.addEventListener('message', handler);
              
              window.parent.postMessage({
                type: 'call',
                id: id,
                method: method,
                args: args
              }, '*');
            });
          },
          
          emit: function(event, data) {
            window.parent.postMessage({
              type: 'event',
              event: event,
              data: data
            }, '*');
          },
          
          on: function(event, handler) {
            window.addEventListener('message', (e) => {
              if (e.data.type === 'event' && e.data.event === event) {
                handler(e.data.data);
              }
            });
          }
        };
        
        // Expose API to plugin
        window.PluginAPI = bridge;
        
        // Load plugin script
        const script = document.createElement('script');
        script.src = '${entryPoint}';
        script.onerror = () => {
          bridge.emit('error', 'Failed to load plugin script');
        };
        document.head.appendChild(script);
      })();
    `;
  }
  
  /**
   * Wait for plugin to be ready
   */
  waitForReady(timeout = 5000) {
    return new Promise((resolve, reject) => {
      const timeoutId = setTimeout(() => {
        reject(new Error('Plugin initialization timeout'));
      }, timeout);
      
      const handler = (event) => {
        if (event.data.type === 'ready') {
          clearTimeout(timeoutId);
          window.removeEventListener('message', handler);
          resolve();
        }
      };
      
      window.addEventListener('message', handler);
    });
  }
  
  /**
   * Initialize plugin
   */
  async initialize(context) {
    await this.sendMessage('initialize', {
      config: context.config,
      permissions: this.descriptor.permissions
    });
  }
  
  /**
   * Handle messages from plugin
   */
  handleMessage(event) {
    if (event.source !== this.window) {
      return; // Not from our iframe
    }
    
    const { type, id, method, args, event: eventName, data } = event.data;
    
    switch (type) {
      case 'call':
        this.handleAPICall(id, method, args);
        break;
      
      case 'event':
        this.handlePluginEvent(eventName, data);
        break;
      
      case 'response':
        this.handleResponse(id, event.data);
        break;
    }
  }
  
  /**
   * Handle API call from plugin
   */
  async handleAPICall(id, method, args) {
    try {
      // Call through API bridge
      const api = this.pluginManager.apiBridge.createAPI(this.descriptor);
      const result = await api[method](...args);
      
      this.sendResponse(id, result);
    } catch (error) {
      this.sendResponse(id, null, error.message);
    }
  }
  
  /**
   * Handle plugin event
   */
  handlePluginEvent(eventName, data) {
    this.pluginManager.emit(`plugin:${this.descriptor.id}:${eventName}`, data);
  }
  
  /**
   * Handle response to our call
   */
  handleResponse(id, data) {
    const handler = this.messageHandlers.get(id);
    if (handler) {
      this.messageHandlers.delete(id);
      if (data.error) {
        handler.reject(new Error(data.error));
      } else {
        handler.resolve(data.result);
      }
    }
  }
  
  /**
   * Send message to plugin
   */
  sendMessage(method, args) {
    return new Promise((resolve, reject) => {
      const id = (this.nextMessageId++).toString();
      
      this.messageHandlers.set(id, { resolve, reject });
      
      this.window.postMessage({
        type: 'call',
        id: id,
        method: method,
        args: args
      }, '*');
      
      // Timeout after 30 seconds
      setTimeout(() => {
        if (this.messageHandlers.has(id)) {
          this.messageHandlers.delete(id);
          reject(new Error('Message timeout'));
        }
      }, 30000);
    });
  }
  
  /**
   * Send response to plugin
   */
  sendResponse(id, result, error = null) {
    this.window.postMessage({
      type: 'response',
      id: id,
      result: result,
      error: error
    }, '*');
  }
  
  /**
   * Show plugin UI
   */
  show(container) {
    this.iframe.style.display = 'block';
    if (container) {
      container.appendChild(this.iframe);
    }
  }
  
  /**
   * Hide plugin UI
   */
  hide() {
    this.iframe.style.display = 'none';
  }
  
  /**
   * Activate plugin
   */
  async activate() {
    await this.sendMessage('activate', {});
    this.show();
  }
  
  /**
   * Deactivate plugin
   */
  async deactivate() {
    await this.sendMessage('deactivate', {});
    this.hide();
  }
  
  /**
   * Update configuration
   */
  async updateConfig(config) {
    await this.sendMessage('updateConfig', config);
  }
  
  /**
   * Cleanup plugin
   */
  async cleanup() {
    await this.sendMessage('cleanup', {});
  }
  
  /**
   * Destroy sandbox
   */
  destroy() {
    if (this.iframe && this.iframe.parentNode) {
      this.iframe.parentNode.removeChild(this.iframe);
    }
    this.iframe = null;
    this.window = null;
    this.messageHandlers.clear();
  }
}

/**
 * Web Worker-based Sandbox (for background plugins)
 */
class WorkerSandbox {
  constructor(descriptor, pluginManager) {
    this.descriptor = descriptor;
    this.pluginManager = pluginManager;
    this.worker = null;
    this.messageHandlers = new Map();
    this.nextMessageId = 0;
  }
  
  /**
   * Create worker sandbox
   */
  async create() {
    return new Promise((resolve, reject) => {
      try {
        // Create worker with plugin code
        const workerCode = this.createWorkerCode();
        const blob = new Blob([workerCode], { type: 'application/javascript' });
        const url = URL.createObjectURL(blob);
        
        this.worker = new Worker(url);
        
        // Setup message handler
        this.worker.onmessage = (event) => {
          this.handleMessage(event);
        };
        
        this.worker.onerror = (error) => {
          console.error('[WorkerSandbox] Error:', error);
          this.pluginManager.emit(`plugin:${this.descriptor.id}:error`, error);
        };
        
        resolve();
        
      } catch (error) {
        reject(error);
      }
    });
  }
  
  /**
   * Create worker initialization code
   */
  createWorkerCode() {
    return `
      // Worker-side plugin API
      const PluginAPI = {
        call: function(method, ...args) {
          return new Promise((resolve, reject) => {
            const id = Math.random().toString(36);
            
            const handler = (event) => {
              if (event.data.type === 'response' && event.data.id === id) {
                self.removeEventListener('message', handler);
                if (event.data.error) {
                  reject(new Error(event.data.error));
                } else {
                  resolve(event.data.result);
                }
              }
            };
            
            self.addEventListener('message', handler);
            
            self.postMessage({
              type: 'call',
              id: id,
              method: method,
              args: args
            });
          });
        },
        
        emit: function(event, data) {
          self.postMessage({
            type: 'event',
            event: event,
            data: data
          });
        },
        
        on: function(event, handler) {
          self.addEventListener('message', (e) => {
            if (e.data.type === 'event' && e.data.event === event) {
              handler(e.data.data);
            }
          });
        }
      };
      
      // Load plugin
      self.importScripts('${this.descriptor.main}');
    `;
  }
  
  /**
   * Load plugin code
   */
  async load(entryPoint) {
    // Worker already loaded in create()
    await this.waitForReady();
  }
  
  /**
   * Wait for ready signal
   */
  waitForReady(timeout = 5000) {
    return new Promise((resolve, reject) => {
      const timeoutId = setTimeout(() => {
        reject(new Error('Worker initialization timeout'));
      }, timeout);
      
      const handler = (event) => {
        if (event.data.type === 'ready') {
          clearTimeout(timeoutId);
          this.worker.removeEventListener('message', handler);
          resolve();
        }
      };
      
      this.worker.addEventListener('message', handler);
    });
  }
  
  /**
   * Initialize plugin
   */
  async initialize(context) {
    await this.sendMessage('initialize', {
      config: context.config,
      permissions: this.descriptor.permissions
    });
  }
  
  /**
   * Handle messages from worker
   */
  handleMessage(event) {
    const { type, id, method, args, event: eventName, data } = event.data;
    
    switch (type) {
      case 'call':
        this.handleAPICall(id, method, args);
        break;
      
      case 'event':
        this.handlePluginEvent(eventName, data);
        break;
      
      case 'response':
        this.handleResponse(id, event.data);
        break;
    }
  }
  
  /**
   * Handle API call from worker
   */
  async handleAPICall(id, method, args) {
    try {
      const api = this.pluginManager.apiBridge.createAPI(this.descriptor);
      const result = await api[method](...args);
      
      this.sendResponse(id, result);
    } catch (error) {
      this.sendResponse(id, null, error.message);
    }
  }
  
  /**
   * Handle plugin event
   */
  handlePluginEvent(eventName, data) {
    this.pluginManager.emit(`plugin:${this.descriptor.id}:${eventName}`, data);
  }
  
  /**
   * Handle response
   */
  handleResponse(id, data) {
    const handler = this.messageHandlers.get(id);
    if (handler) {
      this.messageHandlers.delete(id);
      if (data.error) {
        handler.reject(new Error(data.error));
      } else {
        handler.resolve(data.result);
      }
    }
  }
  
  /**
   * Send message to worker
   */
  sendMessage(method, args) {
    return new Promise((resolve, reject) => {
      const id = (this.nextMessageId++).toString();
      
      this.messageHandlers.set(id, { resolve, reject });
      
      this.worker.postMessage({
        type: 'call',
        id: id,
        method: method,
        args: args
      });
      
      setTimeout(() => {
        if (this.messageHandlers.has(id)) {
          this.messageHandlers.delete(id);
          reject(new Error('Message timeout'));
        }
      }, 30000);
    });
  }
  
  /**
   * Send response to worker
   */
  sendResponse(id, result, error = null) {
    this.worker.postMessage({
      type: 'response',
      id: id,
      result: result,
      error: error
    });
  }
  
  /**
   * Activate plugin
   */
  async activate() {
    await this.sendMessage('activate', {});
  }
  
  /**
   * Deactivate plugin
   */
  async deactivate() {
    await this.sendMessage('deactivate', {});
  }
  
  /**
   * Update configuration
   */
  async updateConfig(config) {
    await this.sendMessage('updateConfig', config);
  }
  
  /**
   * Cleanup
   */
  async cleanup() {
    await this.sendMessage('cleanup', {});
  }
  
  /**
   * Destroy worker
   */
  destroy() {
    if (this.worker) {
      this.worker.terminate();
      this.worker = null;
    }
    this.messageHandlers.clear();
  }
}
```

## Permission System

**Permission Manager**:

```javascript
/**
 * Permission Manager
 * Handles capability-based security for plugins
 */
class PermissionManager {
  constructor(pluginManager) {
    this.pluginManager = pluginManager;
    
    // Define available permissions
    this.availablePermissions = new Set([
      'storage',
      'storage.local',
      'storage.sync',
      'network',
      'network.fetch',
      'network.websocket',
      'ui',
      'ui.toolbar',
      'ui.sidebar',
      'ui.modal',
      'ui.notification',
      'clipboard',
      'clipboard.read',
      'clipboard.write',
      'file',
      'file.read',
      'file.write',
      'geolocation',
      'camera',
      'microphone',
      'notifications'
    ]);
    
    // Plugin permissions: Map<pluginId, Set<permission>>
    this.grantedPermissions = new Map();
    
    // Permission groups
    this.permissionGroups = {
      'storage': ['storage.local', 'storage.sync'],
      'network': ['network.fetch', 'network.websocket'],
      'ui': ['ui.toolbar', 'ui.sidebar', 'ui.modal', 'ui.notification'],
      'clipboard': ['clipboard.read', 'clipboard.write'],
      'file': ['file.read', 'file.write']
    };
  }
  
  /**
   * Check if plugin has required permissions
   */
  async checkPermissions(descriptor) {
    const requested = descriptor.permissions || [];
    
    // Validate permissions
    for (const permission of requested) {
      if (!this.availablePermissions.has(permission)) {
        throw new Error(`Unknown permission: ${permission}`);
      }
    }
    
    // Check if user needs to grant permissions
    const needsGrant = requested.filter(p => {
      return this.requiresUserConsent(p);
    });
    
    if (needsGrant.length > 0) {
      const granted = await this.requestUserPermissions(descriptor, needsGrant);
      if (!granted) {
        throw new Error('User denied permissions');
      }
    }
    
    // Grant permissions
    this.grantedPermissions.set(descriptor.id, new Set(requested));
    
    return true;
  }
  
  /**
   * Check if permission requires user consent
   */
  requiresUserConsent(permission) {
    const sensitivePermissions = [
      'geolocation',
      'camera',
      'microphone',
      'clipboard.read',
      'file.write',
      'notifications'
    ];
    
    return sensitivePermissions.includes(permission);
  }
  
  /**
   * Request permissions from user
   */
  async requestUserPermissions(descriptor, permissions) {
    return new Promise((resolve) => {
      // Create permission dialog
      const dialog = this.createPermissionDialog(descriptor, permissions);
      
      dialog.onApprove = () => {
        resolve(true);
        dialog.close();
      };
      
      dialog.onDeny = () => {
        resolve(false);
        dialog.close();
      };
      
      dialog.show();
    });
  }
  
  /**
   * Create permission request dialog
   */
  createPermissionDialog(descriptor, permissions) {
    const overlay = document.createElement('div');
    overlay.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0,0,0,0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 10000;
    `;
    
    const dialog = document.createElement('div');
    dialog.style.cssText = `
      background: white;
      padding: 24px;
      border-radius: 8px;
      max-width: 500px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    `;
    
    dialog.innerHTML = `
      <h2 style="margin: 0 0 16px 0;">Permission Request</h2>
      <p><strong>${descriptor.name}</strong> requests the following permissions:</p>
      <ul style="margin: 16px 0;">
        ${permissions.map(p => `<li>${this.getPermissionDescription(p)}</li>`).join('')}
      </ul>
      <div style="display: flex; gap: 8px; justify-content: flex-end;">
        <button id="deny-btn" style="padding: 8px 16px; cursor: pointer;">Deny</button>
        <button id="approve-btn" style="padding: 8px 16px; cursor: pointer; background: #007bff; color: white; border: none; border-radius: 4px;">Approve</button>
      </div>
    `;
    
    overlay.appendChild(dialog);
    document.body.appendChild(overlay);
    
    return {
      show: () => {},
      close: () => {
        document.body.removeChild(overlay);
      },
      onApprove: null,
      onDeny: null,
      element: dialog
    };
  }
  
  /**
   * Get human-readable permission description
   */
  getPermissionDescription(permission) {
    const descriptions = {
      'storage': 'Store data locally',
      'storage.local': 'Store data in local storage',
      'storage.sync': 'Sync data across devices',
      'network': 'Make network requests',
      'network.fetch': 'Fetch data from servers',
      'network.websocket': 'Open websocket connections',
      'ui': 'Modify user interface',
      'ui.toolbar': 'Add toolbar buttons',
      'ui.sidebar': 'Add sidebar panels',
      'ui.modal': 'Show modal dialogs',
      'ui.notification': 'Show notifications',
      'clipboard': 'Access clipboard',
      'clipboard.read': 'Read from clipboard',
      'clipboard.write': 'Write to clipboard',
      'file': 'Access files',
      'file.read': 'Read files',
      'file.write': 'Write files',
      'geolocation': 'Access your location',
      'camera': 'Access camera',
      'microphone': 'Access microphone',
      'notifications': 'Show system notifications'
    };
    
    return descriptions[permission] || permission;
  }
  
  /**
   * Check if plugin has specific permission
   */
  hasPermission(pluginId, permission) {
    const permissions = this.grantedPermissions.get(pluginId);
    if (!permissions) return false;
    
    // Check exact permission
    if (permissions.has(permission)) {
      return true;
    }
    
    // Check parent permission (e.g., 'storage' grants 'storage.local')
    const parts = permission.split('.');
    if (parts.length > 1) {
      const parent = parts[0];
      return permissions.has(parent);
    }
    
    return false;
  }
  
  /**
   * Revoke permission
   */
  revokePermission(pluginId, permission) {
    const permissions = this.grantedPermissions.get(pluginId);
    if (permissions) {
      permissions.delete(permission);
    }
  }
  
  /**
   * Revoke all permissions for plugin
   */
  revokeAllPermissions(pluginId) {
    this.grantedPermissions.delete(pluginId);
  }
  
  /**
   * Get granted permissions for plugin
   */
  getPermissions(pluginId) {
    const permissions = this.grantedPermissions.get(pluginId);
    return permissions ? Array.from(permissions) : [];
  }
}
```


