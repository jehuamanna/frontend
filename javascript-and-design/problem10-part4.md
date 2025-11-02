
## Error Handling and Edge Cases

**Robust Error Handling**:

```javascript
/**
 * Error Boundary for Plugins
 */
class PluginErrorBoundary {
  constructor(pluginManager) {
    this.pluginManager = pluginManager;
    this.errors = new Map();
  }
  
  /**
   * Wrap plugin execution with error boundary
   */
  wrap(pluginId, fn) {
    return async (...args) => {
      try {
        return await fn(...args);
      } catch (error) {
        this.handleError(pluginId, error);
        throw error;
      }
    };
  }
  
  /**
   * Handle plugin error
   */
  handleError(pluginId, error) {
    if (!this.errors.has(pluginId)) {
      this.errors.set(pluginId, []);
    }
    
    const errorRecord = {
      error: error,
      message: error.message,
      stack: error.stack,
      timestamp: Date.now()
    };
    
    this.errors.get(pluginId).push(errorRecord);
    
    // Limit error history
    const errors = this.errors.get(pluginId);
    if (errors.length > 50) {
      errors.shift();
    }
    
    // Check if plugin should be disabled
    const recentErrors = errors.filter(e => 
      Date.now() - e.timestamp < 60000 // Last minute
    );
    
    if (recentErrors.length > 10) {
      console.error(`[PluginManager] Too many errors from ${pluginId}, disabling`);
      this.pluginManager.deactivate(pluginId);
    }
    
    // Emit error event
    this.pluginManager.emit('plugin:error', {
      pluginId,
      error: errorRecord
    });
  }
  
  /**
   * Get error history for plugin
   */
  getErrors(pluginId) {
    return this.errors.get(pluginId) || [];
  }
  
  /**
   * Clear errors for plugin
   */
  clearErrors(pluginId) {
    this.errors.delete(pluginId);
  }
}

// Edge Case Handlers

/**
 * Handle plugin crashes
 */
async function handlePluginCrash(pluginManager, pluginId) {
  const context = pluginManager.getPlugin(pluginId);
  if (!context) return;
  
  try {
    // Attempt graceful cleanup
    await context.sandbox.cleanup();
  } catch (error) {
    console.error('[PluginManager] Cleanup failed:', error);
  }
  
  // Force unload
  await pluginManager.unload(pluginId);
  
  // Mark as crashed
  context.descriptor.status = 'crashed';
  context.descriptor.error = new Error('Plugin crashed');
}

/**
 * Handle memory leaks
 */
function detectMemoryLeak(pluginId) {
  if (!performance.memory) return false;
  
  const threshold = 50 * 1024 * 1024; // 50MB
  const used = performance.memory.usedJSHeapSize;
  
  // Simple heuristic: check if memory usage is abnormally high
  return used > threshold;
}

/**
 * Handle infinite loops
 */
function createExecutionTimeout(fn, timeout = 5000) {
  return Promise.race([
    fn(),
    new Promise((_, reject) => 
      setTimeout(() => reject(new Error('Execution timeout')), timeout)
    )
  ]);
}
```

## Accessibility Considerations

**Plugin Accessibility Features**:

```javascript
/**
 * Accessibility support for plugins
 */
class PluginAccessibility {
  constructor(pluginManager) {
    this.pluginManager = pluginManager;
  }
  
  /**
   * Ensure plugin UI is accessible
   */
  validateAccessibility(pluginId) {
    const context = this.pluginManager.getPlugin(pluginId);
    if (!context || !context.sandbox.iframe) return;
    
    const iframe = context.sandbox.iframe;
    const doc = iframe.contentDocument;
    
    // Check for ARIA labels
    const interactiveElements = doc.querySelectorAll('button, a, input, select');
    for (const el of interactiveElements) {
      if (!el.getAttribute('aria-label') && !el.textContent.trim()) {
        console.warn(`[A11y] Interactive element missing label in ${pluginId}`);
      }
    }
    
    // Check color contrast
    // Check keyboard navigation
    // etc.
  }
  
  /**
   * Announce plugin state changes to screen readers
   */
  announce(message) {
    const announcer = document.getElementById('plugin-announcer');
    if (announcer) {
      announcer.textContent = message;
      setTimeout(() => {
        announcer.textContent = '';
      }, 1000);
    }
  }
}
```

## Performance Optimization

**Performance Monitoring**:

```javascript
/**
 * Plugin Performance Monitor
 */
class PluginPerformanceMonitor {
  constructor() {
    this.metrics = new Map();
  }
  
  /**
   * Record plugin load time
   */
  recordLoadTime(pluginId, duration) {
    if (!this.metrics.has(pluginId)) {
      this.metrics.set(pluginId, {
        loadTime: 0,
        messageLatency: [],
        memoryUsage: []
      });
    }
    
    this.metrics.get(pluginId).loadTime = duration;
  }
  
  /**
   * Record message latency
   */
  recordMessageLatency(pluginId, latency) {
    const metrics = this.metrics.get(pluginId);
    if (metrics) {
      metrics.messageLatency.push(latency);
      
      // Keep only recent 100 measurements
      if (metrics.messageLatency.length > 100) {
        metrics.messageLatency.shift();
      }
    }
  }
  
  /**
   * Get performance report
   */
  getReport(pluginId) {
    const metrics = this.metrics.get(pluginId);
    if (!metrics) return null;
    
    const avgLatency = metrics.messageLatency.length > 0
      ? metrics.messageLatency.reduce((a, b) => a + b) / metrics.messageLatency.length
      : 0;
    
    return {
      loadTime: metrics.loadTime,
      avgMessageLatency: avgLatency,
      maxMessageLatency: Math.max(...metrics.messageLatency, 0)
    };
  }
}

/**
 * Lazy loading optimization
 */
class LazyPluginLoader {
  constructor(pluginManager) {
    this.pluginManager = pluginManager;
    this.loadPromises = new Map();
  }
  
  /**
   * Load plugin on demand
   */
  async loadOnDemand(pluginId) {
    // Return existing promise if already loading
    if (this.loadPromises.has(pluginId)) {
      return this.loadPromises.get(pluginId);
    }
    
    const promise = this.pluginManager.load(pluginId);
    this.loadPromises.set(pluginId, promise);
    
    try {
      await promise;
      return true;
    } finally {
      this.loadPromises.delete(pluginId);
    }
  }
  
  /**
   * Preload plugins based on usage patterns
   */
  async preload(pluginIds) {
    // Load in parallel with concurrency limit
    const concurrency = 3;
    const results = [];
    
    for (let i = 0; i < pluginIds.length; i += concurrency) {
      const batch = pluginIds.slice(i, i + concurrency);
      const batchResults = await Promise.allSettled(
        batch.map(id => this.loadOnDemand(id))
      );
      results.push(...batchResults);
    }
    
    return results;
  }
}
```

## Usage Examples

**Example 1: Basic Plugin Development**:

```javascript
// Plugin manifest.json
{
  "id": "hello-world",
  "name": "Hello World Plugin",
  "version": "1.0.0",
  "main": "plugin.js",
  "permissions": ["ui.notification"]
}

// plugin.js - Plugin code
(function() {
  const api = window.PluginAPI;
  
  // Initialize plugin
  api.on('initialize', async (config) => {
    console.log('Plugin initialized with config:', config);
    
    // Add toolbar button
    await api.call('ui.toolbar.addButton', {
      label: 'Hello',
      onClick: async () => {
        await api.call('ui.notification.show', 'Hello from plugin!');
      }
    });
    
    // Signal ready
    api.emit('ready');
  });
  
  // Handle activation
  api.on('activate', () => {
    console.log('Plugin activated');
  });
  
  // Handle deactivation
  api.on('deactivate', () => {
    console.log('Plugin deactivated');
  });
  
  // Cleanup
  api.on('cleanup', () => {
    console.log('Plugin cleanup');
  });
})();
```

**Example 2: Plugin with Storage**:

```javascript
// Plugin with persistent storage
(function() {
  const api = window.PluginAPI;
  let counter = 0;
  
  api.on('initialize', async (config) => {
    // Load saved state
    counter = (await api.call('storage.get', 'counter')) || 0;
    
    // Add UI
    await api.call('ui.toolbar.addButton', {
      label: `Count: ${counter}`,
      onClick: async () => {
        counter++;
        
        // Save state
        await api.call('storage.set', 'counter', counter);
        
        // Update UI
        await api.call('ui.notification.show', `Count: ${counter}`);
      }
    });
    
    api.emit('ready');
  });
})();
```

**Example 3: Inter-Plugin Communication**:

```javascript
// Plugin A: Sender
(function() {
  const api = window.PluginAPI;
  
  api.on('initialize', async () => {
    // Send message to Plugin B
    const response = await api.call('plugins.send', 'plugin-b', {
      action: 'getData',
      params: { id: 123 }
    });
    
    console.log('Response from Plugin B:', response);
    
    api.emit('ready');
  });
})();

// Plugin B: Receiver
(function() {
  const api = window.PluginAPI;
  
  api.on('initialize', async () => {
    // Listen for messages
    await api.call('plugins.onMessage', (message) => {
      console.log('Received message:', message);
      
      if (message.action === 'getData') {
        // Send response
        return { data: 'Hello from Plugin B' };
      }
    });
    
    api.emit('ready');
  });
})();
```

**Example 4: Plugin with Network Access**:

```javascript
// Plugin that fetches data
(function() {
  const api = window.PluginAPI;
  
  api.on('initialize', async (config) => {
    const apiKey = config.apiKey;
    
    await api.call('ui.toolbar.addButton', {
      label: 'Fetch Data',
      onClick: async () => {
        try {
          const response = await api.call('network.fetch', 
            `https://api.example.com/data?key=${apiKey}`
          );
          
          const data = await response.json();
          
          await api.call('ui.modal.show', {
            title: 'Data',
            content: JSON.stringify(data, null, 2)
          });
        } catch (error) {
          await api.call('ui.notification.show', `Error: ${error.message}`);
        }
      }
    });
    
    api.emit('ready');
  });
})();
```

**Example 5: Host Application Setup**:

```javascript
// Initialize plugin system
const pluginManager = new PluginManager({
  pluginDirectory: '/plugins/',
  sandboxMode: 'iframe',
  enableHotReload: true
});

// Register hooks
pluginManager.hook('beforeLoad', async (descriptor) => {
  console.log(`Loading plugin: ${descriptor.name}`);
});

pluginManager.hook('afterLoad', async (descriptor, context) => {
  console.log(`Loaded plugin: ${descriptor.name}`);
});

pluginManager.hook('onError', async (descriptor, error) => {
  console.error(`Plugin error: ${descriptor.name}`, error);
});

// Load specific plugin
async function loadPlugin(pluginId) {
  try {
    await pluginManager.load(pluginId);
    console.log(`Plugin ${pluginId} loaded successfully`);
  } catch (error) {
    console.error(`Failed to load plugin ${pluginId}:`, error);
  }
}

// Load all plugins
async function loadAllPlugins() {
  const plugins = pluginManager.getAllPlugins();
  
  for (const plugin of plugins) {
    if (plugin.status === 'registered') {
      await loadPlugin(plugin.id);
    }
  }
}

// Plugin marketplace UI
function renderPluginMarketplace() {
  const plugins = pluginManager.getAllPlugins();
  
  return plugins.map(plugin => `
    <div class="plugin-card">
      <h3>${plugin.name}</h3>
      <p>${plugin.description}</p>
      <button onclick="installPlugin('${plugin.id}')">
        ${plugin.status === 'active' ? 'Uninstall' : 'Install'}
      </button>
    </div>
  `).join('');
}

// Install/uninstall plugin
async function installPlugin(pluginId) {
  const context = pluginManager.getPlugin(pluginId);
  
  if (context) {
    await pluginManager.unload(pluginId);
  } else {
    await pluginManager.load(pluginId);
  }
  
  // Refresh UI
  renderPluginMarketplace();
}
```

## Testing Strategy

**Unit Tests**:

```javascript
describe('PluginManager', () => {
  let pluginManager;
  
  beforeEach(() => {
    pluginManager = new PluginManager({
      pluginDirectory: '/test-plugins/'
    });
  });
  
  afterEach(() => {
    pluginManager.destroy();
  });
  
  describe('Plugin Registration', () => {
    it('should register a valid plugin', async () => {
      const manifest = {
        id: 'test-plugin',
        name: 'Test Plugin',
        version: '1.0.0',
        main: 'plugin.js'
      };
      
      await pluginManager.register(manifest);
      
      const descriptor = pluginManager.registry.get('test-plugin');
      expect(descriptor).toBeDefined();
      expect(descriptor.name).toBe('Test Plugin');
    });
    
    it('should reject invalid plugin metadata', async () => {
      const invalidManifest = {
        name: 'Test Plugin'
        // Missing required fields
      };
      
      await expect(pluginManager.register(invalidManifest))
        .rejects.toThrow('Invalid plugin metadata');
    });
    
    it('should reject duplicate plugin IDs', async () => {
      const manifest = {
        id: 'test-plugin',
        name: 'Test Plugin',
        version: '1.0.0',
        main: 'plugin.js'
      };
      
      await pluginManager.register(manifest);
      
      await expect(pluginManager.register(manifest))
        .rejects.toThrow('Plugin already registered');
    });
  });
  
  describe('Plugin Loading', () => {
    it('should load a registered plugin', async () => {
      const manifest = {
        id: 'test-plugin',
        name: 'Test Plugin',
        version: '1.0.0',
        main: 'plugin.js',
        permissions: []
      };
      
      await pluginManager.register(manifest);
      await pluginManager.load('test-plugin');
      
      const context = pluginManager.getPlugin('test-plugin');
      expect(context).toBeDefined();
      expect(context.descriptor.status).toBe('active');
    });
    
    it('should resolve dependencies before loading', async () => {
      const depManifest = {
        id: 'dependency',
        name: 'Dependency',
        version: '1.0.0',
        main: 'dep.js'
      };
      
      const pluginManifest = {
        id: 'main-plugin',
        name: 'Main Plugin',
        version: '1.0.0',
        main: 'main.js',
        dependencies: { 'dependency': '^1.0.0' }
      };
      
      await pluginManager.register(depManifest);
      await pluginManager.register(pluginManifest);
      
      await pluginManager.load('main-plugin');
      
      // Dependency should be loaded first
      expect(pluginManager.getPlugin('dependency')).toBeDefined();
      expect(pluginManager.getPlugin('main-plugin')).toBeDefined();
    });
  });
  
  describe('Permission System', () => {
    it('should check permissions before granting API access', async () => {
      const manifest = {
        id: 'test-plugin',
        name: 'Test Plugin',
        version: '1.0.0',
        main: 'plugin.js',
        permissions: ['storage']
      };
      
      await pluginManager.register(manifest);
      await pluginManager.load('test-plugin');
      
      const hasPermission = pluginManager.permissionManager
        .hasPermission('test-plugin', 'storage');
      
      expect(hasPermission).toBe(true);
    });
    
    it('should deny access to unpermitted APIs', async () => {
      const manifest = {
        id: 'test-plugin',
        name: 'Test Plugin',
        version: '1.0.0',
        main: 'plugin.js',
        permissions: []
      };
      
      await pluginManager.register(manifest);
      await pluginManager.load('test-plugin');
      
      const context = pluginManager.getPlugin('test-plugin');
      
      await expect(context.api.storage.get('key'))
        .rejects.toThrow('Permission denied');
    });
  });
  
  describe('Sandbox Isolation', () => {
    it('should create isolated iframe sandbox', async () => {
      const manifest = {
        id: 'ui-plugin',
        name: 'UI Plugin',
        version: '1.0.0',
        main: 'plugin.js',
        ui: 'ui.html'
      };
      
      await pluginManager.register(manifest);
      await pluginManager.load('ui-plugin');
      
      const context = pluginManager.getPlugin('ui-plugin');
      expect(context.sandbox instanceof IFrameSandbox).toBe(true);
      expect(context.sandbox.iframe).toBeDefined();
    });
    
    it('should create worker sandbox for background plugins', async () => {
      const manifest = {
        id: 'worker-plugin',
        name: 'Worker Plugin',
        version: '1.0.0',
        main: 'plugin.js'
        // No UI
      };
      
      await pluginManager.register(manifest);
      await pluginManager.load('worker-plugin');
      
      const context = pluginManager.getPlugin('worker-plugin');
      expect(context.sandbox instanceof WorkerSandbox).toBe(true);
      expect(context.sandbox.worker).toBeDefined();
    });
  });
});
```

## Security Considerations

**Security Best Practices**:

```javascript
/**
 * Security hardening for plugin system
 */
class PluginSecurity {
  /**
   * Sanitize plugin code before loading
   */
  static sanitizeCode(code) {
    // Remove dangerous patterns
    const dangerousPatterns = [
      /eval\s*\(/g,
      /Function\s*\(/g,
      /new\s+Function/g,
      /<script/gi,
      /javascript:/gi,
      /on\w+\s*=/gi
    ];
    
    for (const pattern of dangerousPatterns) {
      if (pattern.test(code)) {
        throw new Error('Potentially dangerous code detected');
      }
    }
    
    return code;
  }
  
  /**
   * Validate API calls
   */
  static validateAPICall(method, args, permissions) {
    // Check if method is allowed
    const allowedMethods = this.getAllowedMethods(permissions);
    
    if (!allowedMethods.includes(method)) {
      throw new Error(`Unauthorized API call: ${method}`);
    }
    
    // Validate arguments
    this.validateArguments(method, args);
    
    return true;
  }
  
  /**
   * Content Security Policy for plugins
   */
  static buildCSP() {
    return {
      'default-src': ["'self'"],
      'script-src': ["'self'"],
      'style-src': ["'self'", "'unsafe-inline'"],
      'img-src': ["'self'", 'data:', 'https:'],
      'connect-src': ["'self'"],
      'frame-src': ["'none'"],
      'object-src': ["'none'"],
      'base-uri': ["'self'"],
      'form-action': ["'self'"]
    };
  }
  
  /**
   * Rate limiting for plugin API calls
   */
  static createRateLimiter(maxCalls = 100, window = 60000) {
    const calls = new Map();
    
    return (pluginId) => {
      const now = Date.now();
      
      if (!calls.has(pluginId)) {
        calls.set(pluginId, []);
      }
      
      const pluginCalls = calls.get(pluginId);
      
      // Remove old calls outside window
      const recentCalls = pluginCalls.filter(time => now - time < window);
      calls.set(pluginId, recentCalls);
      
      if (recentCalls.length >= maxCalls) {
        throw new Error('Rate limit exceeded');
      }
      
      recentCalls.push(now);
      return true;
    };
  }
}
```


