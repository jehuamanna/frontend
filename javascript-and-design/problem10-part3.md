
## API Bridge

**Host API for Plugins**:

```javascript
/**
 * API Bridge
 * Provides secure API access to plugins
 */
class APIBridge {
  constructor(pluginManager) {
    this.pluginManager = pluginManager;
  }
  
  /**
   * Create API proxy for plugin
   */
  createAPI(descriptor) {
    const api = {
      // Storage API
      storage: this.createStorageAPI(descriptor),
      
      // Network API
      network: this.createNetworkAPI(descriptor),
      
      // UI API
      ui: this.createUIAPI(descriptor),
      
      // Events API
      events: this.createEventsAPI(descriptor),
      
      // Plugins API (inter-plugin communication)
      plugins: this.createPluginsAPI(descriptor),
      
      // Clipboard API
      clipboard: this.createClipboardAPI(descriptor),
      
      // Notifications API
      notifications: this.createNotificationsAPI(descriptor)
    };
    
    // Return proxied API with permission checks
    return this.createSecureProxy(api, descriptor);
  }
  
  /**
   * Create secure proxy with permission checks
   */
  createSecureProxy(api, descriptor) {
    return new Proxy(api, {
      get: (target, prop) => {
        const value = target[prop];
        
        if (typeof value === 'object' && value !== null) {
          return this.createSecureProxy(value, descriptor);
        }
        
        if (typeof value === 'function') {
          return (...args) => {
            // Check permission before calling
            const permission = this.getRequiredPermission(prop);
            if (permission && !this.checkPermission(descriptor.id, permission)) {
              throw new Error(`Permission denied: ${permission}`);
            }
            
            return value.apply(target, args);
          };
        }
        
        return value;
      }
    });
  }
  
  /**
   * Get required permission for API method
   */
  getRequiredPermission(method) {
    const permissions = {
      'storage': 'storage',
      'network': 'network',
      'ui': 'ui',
      'clipboard': 'clipboard',
      'notifications': 'notifications'
    };
    
    return permissions[method];
  }
  
  /**
   * Check if plugin has permission
   */
  checkPermission(pluginId, permission) {
    return this.pluginManager.permissionManager.hasPermission(pluginId, permission);
  }
  
  /**
   * Create Storage API
   */
  createStorageAPI(descriptor) {
    const namespace = descriptor.id;
    
    return {
      get: async (key) => {
        return await this.pluginManager.storage.get(`${namespace}:${key}`);
      },
      
      set: async (key, value) => {
        await this.pluginManager.storage.set(`${namespace}:${key}`, value);
      },
      
      remove: async (key) => {
        await this.pluginManager.storage.remove(`${namespace}:${key}`);
      },
      
      clear: async () => {
        await this.pluginManager.storage.clearNamespace(namespace);
      },
      
      keys: async () => {
        return await this.pluginManager.storage.keys(namespace);
      }
    };
  }
  
  /**
   * Create Network API
   */
  createNetworkAPI(descriptor) {
    return {
      fetch: async (url, options = {}) => {
        // Apply CORS restrictions
        const response = await fetch(url, {
          ...options,
          credentials: 'omit' // Don't send cookies
        });
        
        return {
          ok: response.ok,
          status: response.status,
          statusText: response.statusText,
          headers: Object.fromEntries(response.headers.entries()),
          json: () => response.json(),
          text: () => response.text(),
          blob: () => response.blob()
        };
      },
      
      websocket: (url) => {
        // Return wrapped WebSocket
        const ws = new WebSocket(url);
        return {
          send: (data) => ws.send(data),
          close: () => ws.close(),
          onMessage: (handler) => {
            ws.onmessage = (e) => handler(e.data);
          },
          onError: (handler) => {
            ws.onerror = handler;
          },
          onClose: (handler) => {
            ws.onclose = handler;
          }
        };
      }
    };
  }
  
  /**
   * Create UI API
   */
  createUIAPI(descriptor) {
    return {
      toolbar: {
        addButton: (config) => {
          return this.addToolbarButton(descriptor, config);
        },
        removeButton: (id) => {
          this.removeToolbarButton(descriptor, id);
        }
      },
      
      sidebar: {
        show: (content) => {
          this.showSidebar(descriptor, content);
        },
        hide: () => {
          this.hideSidebar(descriptor);
        }
      },
      
      modal: {
        show: (config) => {
          return this.showModal(descriptor, config);
        },
        hide: () => {
          this.hideModal(descriptor);
        }
      },
      
      notification: {
        show: (message, options) => {
          this.showNotification(descriptor, message, options);
        }
      },
      
      contextMenu: {
        add: (items) => {
          this.addContextMenu(descriptor, items);
        },
        remove: () => {
          this.removeContextMenu(descriptor);
        }
      }
    };
  }
  
  /**
   * Create Events API
   */
  createEventsAPI(descriptor) {
    return {
      on: (event, handler) => {
        window.addEventListener(`plugin:${event}`, (e) => {
          handler(e.detail);
        });
      },
      
      emit: (event, data) => {
        this.pluginManager.emit(`plugin:${descriptor.id}:${event}`, data);
      },
      
      once: (event, handler) => {
        const wrappedHandler = (e) => {
          handler(e.detail);
          window.removeEventListener(`plugin:${event}`, wrappedHandler);
        };
        window.addEventListener(`plugin:${event}`, wrappedHandler);
      }
    };
  }
  
  /**
   * Create Plugins API (inter-plugin communication)
   */
  createPluginsAPI(descriptor) {
    return {
      send: async (targetPluginId, message) => {
        return await this.pluginManager.messageBus.send(
          descriptor.id,
          targetPluginId,
          message
        );
      },
      
      broadcast: (message) => {
        this.pluginManager.messageBus.broadcast(descriptor.id, message);
      },
      
      onMessage: (handler) => {
        this.pluginManager.messageBus.onMessage(descriptor.id, handler);
      },
      
      list: () => {
        return this.pluginManager.getAllPlugins().map(p => ({
          id: p.id,
          name: p.name,
          version: p.version
        }));
      }
    };
  }
  
  /**
   * Create Clipboard API
   */
  createClipboardAPI(descriptor) {
    return {
      read: async () => {
        return await navigator.clipboard.readText();
      },
      
      write: async (text) => {
        await navigator.clipboard.writeText(text);
      }
    };
  }
  
  /**
   * Create Notifications API
   */
  createNotificationsAPI(descriptor) {
    return {
      show: async (title, options = {}) => {
        if (Notification.permission !== 'granted') {
          await Notification.requestPermission();
        }
        
        return new Notification(title, {
          ...options,
          tag: `plugin-${descriptor.id}`
        });
      }
    };
  }
  
  /**
   * Add toolbar button
   */
  addToolbarButton(descriptor, config) {
    const button = document.createElement('button');
    button.textContent = config.label;
    button.className = 'plugin-toolbar-button';
    button.onclick = config.onClick;
    
    const toolbar = document.getElementById('toolbar');
    if (toolbar) {
      toolbar.appendChild(button);
    }
    
    return button;
  }
  
  /**
   * Show sidebar
   */
  showSidebar(descriptor, content) {
    const sidebar = document.getElementById('sidebar');
    if (sidebar) {
      sidebar.innerHTML = content;
      sidebar.style.display = 'block';
    }
  }
  
  /**
   * Show modal
   */
  showModal(descriptor, config) {
    const modal = document.createElement('div');
    modal.className = 'plugin-modal';
    modal.innerHTML = `
      <div class="modal-content">
        <h3>${config.title}</h3>
        <div>${config.content}</div>
        <button onclick="this.closest('.plugin-modal').remove()">Close</button>
      </div>
    `;
    
    document.body.appendChild(modal);
    
    return {
      close: () => modal.remove()
    };
  }
  
  /**
   * Show notification
   */
  showNotification(descriptor, message, options = {}) {
    // Simple notification implementation
    const notification = document.createElement('div');
    notification.className = 'plugin-notification';
    notification.textContent = message;
    notification.style.cssText = `
      position: fixed;
      top: 20px;
      right: 20px;
      padding: 16px;
      background: #333;
      color: white;
      border-radius: 4px;
      z-index: 10000;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
      notification.remove();
    }, options.duration || 3000);
  }
}
```

## Message Bus (Inter-Plugin Communication)

```javascript
/**
 * Message Bus
 * Handles communication between plugins
 */
class MessageBus {
  constructor(pluginManager) {
    this.pluginManager = pluginManager;
    this.channels = new Map();
    this.messageHandlers = new Map();
    this.broadcastChannel = null;
    
    this.setupBroadcastChannel();
  }
  
  /**
   * Setup broadcast channel for multi-tab communication
   */
  setupBroadcastChannel() {
    if ('BroadcastChannel' in window) {
      this.broadcastChannel = new BroadcastChannel('plugin-messages');
      
      this.broadcastChannel.onmessage = (event) => {
        this.handleBroadcastMessage(event.data);
      };
    }
  }
  
  /**
   * Send message from one plugin to another
   */
  async send(fromPluginId, toPluginId, message) {
    // Validate plugins
    const fromPlugin = this.pluginManager.getPlugin(fromPluginId);
    const toPlugin = this.pluginManager.getPlugin(toPluginId);
    
    if (!toPlugin) {
      throw new Error(`Target plugin not found: ${toPluginId}`);
    }
    
    // Create message envelope
    const envelope = {
      from: fromPluginId,
      to: toPluginId,
      message: message,
      timestamp: Date.now(),
      id: this.generateMessageId()
    };
    
    // Send to target plugin
    const handlers = this.messageHandlers.get(toPluginId) || [];
    
    for (const handler of handlers) {
      try {
        await handler(envelope);
      } catch (error) {
        console.error('[MessageBus] Handler error:', error);
      }
    }
    
    return envelope.id;
  }
  
  /**
   * Broadcast message to all plugins
   */
  broadcast(fromPluginId, message) {
    const envelope = {
      from: fromPluginId,
      to: '*',
      message: message,
      timestamp: Date.now(),
      id: this.generateMessageId()
    };
    
    // Send to all active plugins except sender
    for (const [pluginId] of this.pluginManager.activePlugins) {
      if (pluginId !== fromPluginId) {
        const handlers = this.messageHandlers.get(pluginId) || [];
        handlers.forEach(handler => {
          try {
            handler(envelope);
          } catch (error) {
            console.error('[MessageBus] Handler error:', error);
          }
        });
      }
    }
    
    // Broadcast to other tabs
    if (this.broadcastChannel) {
      this.broadcastChannel.postMessage(envelope);
    }
  }
  
  /**
   * Register message handler for plugin
   */
  onMessage(pluginId, handler) {
    if (!this.messageHandlers.has(pluginId)) {
      this.messageHandlers.set(pluginId, []);
    }
    
    this.messageHandlers.get(pluginId).push(handler);
  }
  
  /**
   * Handle broadcast message from other tab
   */
  handleBroadcastMessage(envelope) {
    const targetPlugin = envelope.to;
    
    if (targetPlugin === '*') {
      // Broadcast to all
      for (const [pluginId] of this.pluginManager.activePlugins) {
        const handlers = this.messageHandlers.get(pluginId) || [];
        handlers.forEach(handler => handler(envelope));
      }
    } else {
      // Send to specific plugin
      const handlers = this.messageHandlers.get(targetPlugin) || [];
      handlers.forEach(handler => handler(envelope));
    }
  }
  
  /**
   * Create direct channel between two plugins
   */
  createChannel(plugin1Id, plugin2Id) {
    const channelId = `${plugin1Id}<->${plugin2Id}`;
    
    if (this.channels.has(channelId)) {
      return this.channels.get(channelId);
    }
    
    const channel = new MessageChannel();
    
    this.channels.set(channelId, {
      port1: channel.port1,
      port2: channel.port2
    });
    
    return this.channels.get(channelId);
  }
  
  /**
   * Generate unique message ID
   */
  generateMessageId() {
    return `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  }
  
  /**
   * Destroy message bus
   */
  destroy() {
    if (this.broadcastChannel) {
      this.broadcastChannel.close();
    }
    
    this.channels.clear();
    this.messageHandlers.clear();
  }
}
```

## Dependency Resolution

```javascript
/**
 * Dependency Resolver
 * Manages plugin dependencies and load order
 */
class DependencyResolver {
  constructor(pluginManager) {
    this.pluginManager = pluginManager;
  }
  
  /**
   * Resolve dependencies for plugin
   */
  async resolve(descriptor) {
    const dependencies = descriptor.dependencies || {};
    
    // Build dependency graph
    const graph = this.buildDependencyGraph(descriptor);
    
    // Check for circular dependencies
    if (this.hasCircularDependency(graph, descriptor.id)) {
      throw new Error(`Circular dependency detected for ${descriptor.id}`);
    }
    
    // Get load order
    const loadOrder = this.topologicalSort(graph, descriptor.id);
    
    // Load dependencies in order
    for (const depId of loadOrder) {
      if (depId === descriptor.id) continue;
      
      if (!this.pluginManager.activePlugins.has(depId)) {
        await this.pluginManager.load(depId);
      }
    }
    
    return true;
  }
  
  /**
   * Build dependency graph
   */
  buildDependencyGraph(descriptor) {
    const graph = new Map();
    const visited = new Set();
    
    const visit = (id) => {
      if (visited.has(id)) return;
      visited.add(id);
      
      const plugin = this.pluginManager.registry.get(id);
      if (!plugin) {
        throw new Error(`Dependency not found: ${id}`);
      }
      
      const deps = Object.keys(plugin.dependencies || {});
      graph.set(id, deps);
      
      deps.forEach(depId => visit(depId));
    };
    
    visit(descriptor.id);
    
    return graph;
  }
  
  /**
   * Check for circular dependencies using DFS
   */
  hasCircularDependency(graph, start) {
    const visited = new Set();
    const stack = new Set();
    
    const dfs = (node) => {
      visited.add(node);
      stack.add(node);
      
      const neighbors = graph.get(node) || [];
      
      for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
          if (dfs(neighbor)) return true;
        } else if (stack.has(neighbor)) {
          return true; // Circular dependency found
        }
      }
      
      stack.delete(node);
      return false;
    };
    
    return dfs(start);
  }
  
  /**
   * Topological sort for load order
   */
  topologicalSort(graph, start) {
    const visited = new Set();
    const result = [];
    
    const visit = (node) => {
      if (visited.has(node)) return;
      visited.add(node);
      
      const neighbors = graph.get(node) || [];
      neighbors.forEach(neighbor => visit(neighbor));
      
      result.push(node);
    };
    
    visit(start);
    
    return result;
  }
  
  /**
   * Check version compatibility
   */
  checkVersionCompatibility(required, installed) {
    // Simple semver checking
    const parseVersion = (v) => v.split('.').map(Number);
    
    // Handle version range operators
    if (required.startsWith('^')) {
      // Compatible with minor/patch updates
      const requiredVer = parseVersion(required.slice(1));
      const installedVer = parseVersion(installed);
      
      return installedVer[0] === requiredVer[0] &&
             (installedVer[1] > requiredVer[1] ||
              (installedVer[1] === requiredVer[1] && installedVer[2] >= requiredVer[2]));
    }
    
    if (required.startsWith('>=')) {
      const requiredVer = parseVersion(required.slice(2));
      const installedVer = parseVersion(installed);
      
      for (let i = 0; i < 3; i++) {
        if (installedVer[i] > requiredVer[i]) return true;
        if (installedVer[i] < requiredVer[i]) return false;
      }
      return true;
    }
    
    // Exact match
    return required === installed;
  }
}
```

## Plugin Storage

```javascript
/**
 * Plugin Storage
 * IndexedDB-based storage for plugins
 */
class PluginStorage {
  constructor() {
    this.dbName = 'plugin-storage';
    this.dbVersion = 1;
    this.db = null;
    
    this.init();
  }
  
  /**
   * Initialize IndexedDB
   */
  async init() {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.dbName, this.dbVersion);
      
      request.onerror = () => reject(request.error);
      request.onsuccess = () => {
        this.db = request.result;
        resolve();
      };
      
      request.onupgradeneeded = (event) => {
        const db = event.target.result;
        
        if (!db.objectStoreNames.contains('plugins')) {
          db.createObjectStore('plugins', { keyPath: 'key' });
        }
      };
    });
  }
  
  /**
   * Get value from storage
   */
  async get(key) {
    if (!this.db) await this.init();
    
    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['plugins'], 'readonly');
      const store = transaction.objectStore('plugins');
      const request = store.get(key);
      
      request.onsuccess = () => {
        resolve(request.result?.value);
      };
      request.onerror = () => reject(request.error);
    });
  }
  
  /**
   * Set value in storage
   */
  async set(key, value) {
    if (!this.db) await this.init();
    
    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['plugins'], 'readwrite');
      const store = transaction.objectStore('plugins');
      const request = store.put({ key, value });
      
      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }
  
  /**
   * Remove value from storage
   */
  async remove(key) {
    if (!this.db) await this.init();
    
    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['plugins'], 'readwrite');
      const store = transaction.objectStore('plugins');
      const request = store.delete(key);
      
      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }
  
  /**
   * Get all keys for namespace
   */
  async keys(namespace) {
    if (!this.db) await this.init();
    
    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['plugins'], 'readonly');
      const store = transaction.objectStore('plugins');
      const request = store.getAllKeys();
      
      request.onsuccess = () => {
        const keys = request.result.filter(k => k.startsWith(`${namespace}:`));
        resolve(keys.map(k => k.replace(`${namespace}:`, '')));
      };
      request.onerror = () => reject(request.error);
    });
  }
  
  /**
   * Clear namespace
   */
  async clearNamespace(namespace) {
    const keys = await this.keys(namespace);
    
    for (const key of keys) {
      await this.remove(`${namespace}:${key}`);
    }
  }
  
  /**
   * Create namespaced storage
   */
  createNamespace(namespace) {
    return {
      get: (key) => this.get(`${namespace}:${key}`),
      set: (key, value) => this.set(`${namespace}:${key}`, value),
      remove: (key) => this.remove(`${namespace}:${key}`),
      clear: () => this.clearNamespace(namespace),
      keys: () => this.keys(namespace)
    };
  }
}
```


