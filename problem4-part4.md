
## Testing Strategy

**Unit Tests**:

```javascript
/**
 * Test suite for Event Delegation System
 */
describe('EventDelegator', () => {
  let delegator;
  let container;
  
  beforeEach(() => {
    container = document.createElement('div');
    container.innerHTML = `
      <button class="test-btn" data-id="1">Button 1</button>
      <button class="test-btn" data-id="2">Button 2</button>
      <div class="parent">
        <span class="child">Child</span>
      </div>
    `;
    document.body.appendChild(container);
    
    delegator = new EventDelegator(container);
  });
  
  afterEach(() => {
    delegator.destroy();
    document.body.removeChild(container);
  });
  
  describe('Handler Registration', () => {
    it('should register event handler', () => {
      const handler = jest.fn();
      delegator.on('click', '.test-btn', handler);
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(handler).toHaveBeenCalledTimes(1);
    });
    
    it('should return handler ID', () => {
      const id = delegator.on('click', '.test-btn', () => {});
      expect(typeof id).toBe('number');
    });
    
    it('should handle multiple handlers for same event', () => {
      const handler1 = jest.fn();
      const handler2 = jest.fn();
      
      delegator.on('click', '.test-btn', handler1);
      delegator.on('click', '.test-btn', handler2);
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(handler1).toHaveBeenCalledTimes(1);
      expect(handler2).toHaveBeenCalledTimes(1);
    });
  });
  
  describe('Selector Matching', () => {
    it('should match class selectors', () => {
      const handler = jest.fn();
      delegator.on('click', '.test-btn', handler);
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(handler).toHaveBeenCalled();
    });
    
    it('should match ID selectors', () => {
      const el = document.createElement('div');
      el.id = 'unique-id';
      container.appendChild(el);
      
      const handler = jest.fn();
      delegator.on('click', '#unique-id', handler);
      
      el.click();
      expect(handler).toHaveBeenCalled();
    });
    
    it('should match descendant selectors', () => {
      const handler = jest.fn();
      delegator.on('click', '.parent .child', handler);
      
      const child = container.querySelector('.child');
      child.click();
      
      expect(handler).toHaveBeenCalled();
    });
    
    it('should not match non-matching elements', () => {
      const handler = jest.fn();
      delegator.on('click', '.non-existent', handler);
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(handler).not.toHaveBeenCalled();
    });
  });
  
  describe('Event Propagation', () => {
    it('should propagate through ancestors', () => {
      const handlers = {
        child: jest.fn(),
        parent: jest.fn(),
        root: jest.fn()
      };
      
      delegator.on('click', '.child', handlers.child);
      delegator.on('click', '.parent', handlers.parent);
      delegator.on('click', '*', handlers.root);
      
      const child = container.querySelector('.child');
      child.click();
      
      expect(handlers.child).toHaveBeenCalled();
      expect(handlers.parent).toHaveBeenCalled();
      expect(handlers.root).toHaveBeenCalled();
    });
    
    it('should stop propagation', () => {
      const handlers = {
        child: jest.fn((event) => event.stopPropagation()),
        parent: jest.fn()
      };
      
      delegator.on('click', '.child', handlers.child);
      delegator.on('click', '.parent', handlers.parent);
      
      const child = container.querySelector('.child');
      child.click();
      
      expect(handlers.child).toHaveBeenCalled();
      expect(handlers.parent).not.toHaveBeenCalled();
    });
    
    it('should stop immediate propagation', () => {
      const handlers = {
        first: jest.fn((event) => event.stopImmediatePropagation()),
        second: jest.fn()
      };
      
      delegator.on('click', '.test-btn', handlers.first, { priority: 100 });
      delegator.on('click', '.test-btn', handlers.second, { priority: 50 });
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(handlers.first).toHaveBeenCalled();
      expect(handlers.second).not.toHaveBeenCalled();
    });
  });
  
  describe('Handler Priority', () => {
    it('should execute handlers in priority order', () => {
      const order = [];
      
      delegator.on('click', '.test-btn', () => order.push(1), { priority: 1 });
      delegator.on('click', '.test-btn', () => order.push(100), { priority: 100 });
      delegator.on('click', '.test-btn', () => order.push(50), { priority: 50 });
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(order).toEqual([100, 50, 1]);
    });
  });
  
  describe('Handler Removal', () => {
    it('should remove handler by event type and selector', () => {
      const handler = jest.fn();
      delegator.on('click', '.test-btn', handler);
      delegator.off('click', '.test-btn');
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(handler).not.toHaveBeenCalled();
    });
    
    it('should remove handler by namespace', () => {
      const handler = jest.fn();
      delegator.on('click.test', '.test-btn', handler);
      delegator.off('.test');
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(handler).not.toHaveBeenCalled();
    });
    
    it('should remove specific handler', () => {
      const handler1 = jest.fn();
      const handler2 = jest.fn();
      
      delegator.on('click', '.test-btn', handler1);
      delegator.on('click', '.test-btn', handler2);
      delegator.off('click', '.test-btn', handler1);
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(handler1).not.toHaveBeenCalled();
      expect(handler2).toHaveBeenCalled();
    });
  });
  
  describe('Once Option', () => {
    it('should execute handler only once', () => {
      const handler = jest.fn();
      delegator.on('click', '.test-btn', handler, { once: true });
      
      const button = container.querySelector('.test-btn');
      button.click();
      button.click();
      
      expect(handler).toHaveBeenCalledTimes(1);
    });
  });
  
  describe('Conditional Handlers', () => {
    it('should execute handler when condition is true', () => {
      const handler = jest.fn();
      let shouldExecute = true;
      
      delegator.on('click', '.test-btn', handler, {
        condition: () => shouldExecute
      });
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(handler).toHaveBeenCalledTimes(1);
      
      shouldExecute = false;
      button.click();
      
      expect(handler).toHaveBeenCalledTimes(1); // Still 1
    });
  });
  
  describe('Custom Events', () => {
    it('should emit and handle custom events', () => {
      const handler = jest.fn();
      delegator.on('custom:event', document, handler);
      
      delegator.emit('custom:event', document, { data: 'test' });
      
      expect(handler).toHaveBeenCalled();
      expect(handler.mock.calls[0][0].detail).toEqual({ data: 'test' });
    });
  });
  
  describe('Middleware', () => {
    it('should execute middleware before handlers', () => {
      const order = [];
      
      delegator.use(() => order.push('middleware'));
      delegator.on('click', '.test-btn', () => order.push('handler'));
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(order).toEqual(['middleware', 'handler']);
    });
    
    it('should cancel event when middleware returns false', () => {
      const handler = jest.fn();
      
      delegator.use(() => false);
      delegator.on('click', '.test-btn', handler);
      
      const button = container.querySelector('.test-btn');
      button.click();
      
      expect(handler).not.toHaveBeenCalled();
    });
  });
});

/**
 * Integration tests
 */
describe('EventDelegator Integration', () => {
  it('should handle complex UI interactions', () => {
    const app = document.createElement('div');
    app.innerHTML = `
      <div class="todo-app">
        <input class="todo-input" placeholder="Add todo" />
        <button class="add-btn">Add</button>
        <ul class="todo-list"></ul>
      </div>
    `;
    document.body.appendChild(app);
    
    const delegator = new EventDelegator(app);
    const todos = [];
    
    // Add todo
    delegator.on('click', '.add-btn', () => {
      const input = app.querySelector('.todo-input');
      const text = input.value.trim();
      
      if (text) {
        todos.push({ id: Date.now(), text, done: false });
        renderTodos();
        input.value = '';
      }
    });
    
    // Toggle todo
    delegator.on('click', '.todo-item', (event, element) => {
      const id = parseInt(element.dataset.id);
      const todo = todos.find(t => t.id === id);
      if (todo) {
        todo.done = !todo.done;
        renderTodos();
      }
    });
    
    // Delete todo
    delegator.on('click', '.delete-btn', (event, element) => {
      event.stopPropagation();
      const id = parseInt(element.closest('.todo-item').dataset.id);
      const index = todos.findIndex(t => t.id === id);
      if (index !== -1) {
        todos.splice(index, 1);
        renderTodos();
      }
    });
    
    function renderTodos() {
      const list = app.querySelector('.todo-list');
      list.innerHTML = todos.map(todo => `
        <li class="todo-item ${todo.done ? 'done' : ''}" data-id="${todo.id}">
          ${todo.text}
          <button class="delete-btn">×</button>
        </li>
      `).join('');
    }
    
    // Test the interactions
    const input = app.querySelector('.todo-input');
    const addBtn = app.querySelector('.add-btn');
    
    input.value = 'Test todo';
    addBtn.click();
    
    expect(todos.length).toBe(1);
    expect(todos[0].text).toBe('Test todo');
    
    // Clean up
    delegator.destroy();
    document.body.removeChild(app);
  });
});

/**
 * Performance tests
 */
describe('EventDelegator Performance', () => {
  it('should handle thousands of elements efficiently', () => {
    const container = document.createElement('div');
    
    // Create 10,000 elements
    for (let i = 0; i < 10000; i++) {
      const el = document.createElement('button');
      el.className = 'btn';
      el.dataset.id = i;
      container.appendChild(el);
    }
    
    document.body.appendChild(container);
    
    const delegator = new EventDelegator(container);
    const handler = jest.fn();
    
    const start = performance.now();
    delegator.on('click', '.btn', handler);
    const registrationTime = performance.now() - start;
    
    // Registration should be fast
    expect(registrationTime).toBeLessThan(1);
    
    // Click middle element
    const middleBtn = container.children[5000];
    
    const clickStart = performance.now();
    middleBtn.click();
    const clickTime = performance.now() - clickStart;
    
    // Event handling should be fast
    expect(clickTime).toBeLessThan(5);
    expect(handler).toHaveBeenCalled();
    
    // Clean up
    delegator.destroy();
    document.body.removeChild(container);
  });
});
```

## Security Considerations

**Input Validation and Sanitization**:

```javascript
/**
 * Secure event delegation
 */
class SecureEventDelegator extends EventDelegator {
  constructor(rootElement, options = {}) {
    super(rootElement, options);
    
    this.trustedOrigins = options.trustedOrigins || [];
    this.maxHandlerExecutionTime = options.maxHandlerExecutionTime || 5000;
    this.sanitizeEventData = options.sanitizeEventData !== false;
  }
  
  /**
   * Validate selector to prevent injection
   */
  validateSelector(selector) {
    if (!selector || typeof selector !== 'string') {
      return false;
    }
    
    // Block potentially dangerous selectors
    const dangerousPatterns = [
      /<script/i,
      /javascript:/i,
      /on\w+=/i,
      /data:text\/html/i
    ];
    
    for (const pattern of dangerousPatterns) {
      if (pattern.test(selector)) {
        console.error('[Security] Dangerous selector blocked:', selector);
        return false;
      }
    }
    
    // Validate CSS selector syntax
    try {
      document.querySelector(selector);
      return true;
    } catch (error) {
      console.error('[Security] Invalid selector:', selector);
      return false;
    }
  }
  
  /**
   * Override on() with validation
   */
  on(eventType, selector, handler, options = {}) {
    // Validate selector
    if (selector && !this.validateSelector(selector)) {
      throw new Error('Invalid or dangerous selector');
    }
    
    // Wrap handler with security checks
    const secureHandler = this.createSecureHandler(handler);
    
    return super.on(eventType, selector, secureHandler, options);
  }
  
  /**
   * Create secure handler wrapper
   */
  createSecureHandler(handler) {
    return (event, element) => {
      // Check event origin for cross-origin events
      if (event.origin && !this.isTrustedOrigin(event.origin)) {
        console.warn('[Security] Event from untrusted origin blocked:', event.origin);
        return;
      }
      
      // Sanitize event data
      if (this.sanitizeEventData && event.detail) {
        event.detail = this.sanitizeData(event.detail);
      }
      
      // Execute with timeout
      const timeoutId = setTimeout(() => {
        console.error('[Security] Handler execution timeout');
        throw new Error('Handler execution timeout');
      }, this.maxHandlerExecutionTime);
      
      try {
        return handler.call(this, event, element);
      } finally {
        clearTimeout(timeoutId);
      }
    };
  }
  
  /**
   * Check if origin is trusted
   */
  isTrustedOrigin(origin) {
    if (this.trustedOrigins.length === 0) {
      return true; // No restriction
    }
    
    return this.trustedOrigins.includes(origin);
  }
  
  /**
   * Sanitize event data
   */
  sanitizeData(data) {
    if (typeof data !== 'object' || data === null) {
      return data;
    }
    
    const sanitized = {};
    
    for (const [key, value] of Object.entries(data)) {
      // Sanitize strings
      if (typeof value === 'string') {
        sanitized[key] = this.sanitizeString(value);
      }
      // Recursively sanitize objects
      else if (typeof value === 'object' && value !== null) {
        sanitized[key] = this.sanitizeData(value);
      }
      // Keep primitives
      else {
        sanitized[key] = value;
      }
    }
    
    return sanitized;
  }
  
  /**
   * Sanitize string to prevent XSS
   */
  sanitizeString(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }
  
  /**
   * Content Security Policy integration
   */
  enforceCSP() {
    // Check for CSP violations
    window.addEventListener('securitypolicyviolation', (event) => {
      console.error('[CSP] Violation:', {
        blockedURI: event.blockedURI,
        violatedDirective: event.violatedDirective,
        effectiveDirective: event.effectiveDirective
      });
      
      // Emit CSP violation event
      this.emit('csp:violation', document, {
        violation: event
      });
    });
  }
}

/**
 * Rate limiting to prevent DoS
 */
class RateLimitedDelegator extends EventDelegator {
  constructor(rootElement, options = {}) {
    super(rootElement, options);
    
    this.rateLimits = new Map();
    this.defaultLimit = options.defaultLimit || {
      maxEvents: 100,
      window: 1000 // 100 events per second
    };
  }
  
  /**
   * Override handleEvent with rate limiting
   */
  handleEvent(event, target) {
    if (!this.checkRateLimit(event.type)) {
      console.warn('[RateLimit] Event rate limit exceeded:', event.type);
      return;
    }
    
    super.handleEvent(event, target);
  }
  
  /**
   * Check rate limit for event type
   */
  checkRateLimit(eventType) {
    const now = Date.now();
    
    if (!this.rateLimits.has(eventType)) {
      this.rateLimits.set(eventType, {
        events: [],
        limit: this.defaultLimit
      });
    }
    
    const limiter = this.rateLimits.get(eventType);
    
    // Remove old events outside window
    limiter.events = limiter.events.filter(
      time => now - time < limiter.limit.window
    );
    
    // Check if limit exceeded
    if (limiter.events.length >= limiter.limit.maxEvents) {
      return false;
    }
    
    // Record event
    limiter.events.push(now);
    return true;
  }
  
  /**
   * Set custom rate limit for event type
   */
  setRateLimit(eventType, maxEvents, window) {
    const limiter = this.rateLimits.get(eventType) || { events: [] };
    limiter.limit = { maxEvents, window };
    this.rateLimits.set(eventType, limiter);
  }
}
```

## Browser Compatibility and Polyfills

**Cross-browser Support**:

```javascript
/**
 * Polyfills for older browsers
 */
(function() {
  // Element.matches polyfill
  if (!Element.prototype.matches) {
    Element.prototype.matches =
      Element.prototype.matchesSelector ||
      Element.prototype.mozMatchesSelector ||
      Element.prototype.msMatchesSelector ||
      Element.prototype.oMatchesSelector ||
      Element.prototype.webkitMatchesSelector ||
      function(s) {
        const matches = (this.document || this.ownerDocument).querySelectorAll(s);
        let i = matches.length;
        while (--i >= 0 && matches.item(i) !== this) {}
        return i > -1;
      };
  }
  
  // Element.closest polyfill
  if (!Element.prototype.closest) {
    Element.prototype.closest = function(s) {
      let el = this;
      
      do {
        if (Element.prototype.matches.call(el, s)) return el;
        el = el.parentElement || el.parentNode;
      } while (el !== null && el.nodeType === 1);
      
      return null;
    };
  }
  
  // CustomEvent polyfill
  if (typeof window.CustomEvent !== 'function') {
    function CustomEvent(event, params) {
      params = params || { bubbles: false, cancelable: false, detail: null };
      const evt = document.createEvent('CustomEvent');
      evt.initCustomEvent(event, params.bubbles, params.cancelable, params.detail);
      return evt;
    }
    window.CustomEvent = CustomEvent;
  }
  
  // WeakMap polyfill (simplified)
  if (typeof WeakMap === 'undefined') {
    window.WeakMap = (function() {
      const keys = [];
      const values = [];
      
      function WeakMap() {}
      
      WeakMap.prototype = {
        get: function(key) {
          const index = keys.indexOf(key);
          return index !== -1 ? values[index] : undefined;
        },
        
        set: function(key, value) {
          const index = keys.indexOf(key);
          if (index !== -1) {
            values[index] = value;
          } else {
            keys.push(key);
            values.push(value);
          }
        },
        
        has: function(key) {
          return keys.indexOf(key) !== -1;
        },
        
        delete: function(key) {
          const index = keys.indexOf(key);
          if (index !== -1) {
            keys.splice(index, 1);
            values.splice(index, 1);
            return true;
          }
          return false;
        }
      };
      
      return WeakMap;
    })();
  }
})();

/**
 * Browser compatibility layer
 */
class CompatibleEventDelegator extends EventDelegator {
  constructor(rootElement, options = {}) {
    super(rootElement, options);
    
    this.browser = this.detectBrowser();
    this.applyBrowserFixes();
  }
  
  /**
   * Detect browser
   */
  detectBrowser() {
    const ua = navigator.userAgent;
    
    return {
      isIE: /MSIE|Trident/.test(ua),
      isEdge: /Edge/.test(ua),
      isFirefox: /Firefox/.test(ua),
      isSafari: /Safari/.test(ua) && !/Chrome/.test(ua),
      isChrome: /Chrome/.test(ua) && !/Edge/.test(ua)
    };
  }
  
  /**
   * Apply browser-specific fixes
   */
  applyBrowserFixes() {
    if (this.browser.isIE) {
      this.applyIEFixes();
    }
    
    if (this.browser.isSafari) {
      this.applySafariFixes();
    }
  }
  
  /**
   * IE-specific fixes
   */
  applyIEFixes() {
    // IE doesn't support passive event listeners
    this.options.passive = false;
    
    // IE has issues with event.path
    this.buildPropagationPath = (target) => {
      const path = [];
      let current = target;
      
      while (current && current !== document) {
        path.push(current);
        current = current.parentNode;
      }
      
      return path;
    };
  }
  
  /**
   * Safari-specific fixes
   */
  applySafariFixes() {
    // Safari has different event timing
    // Use setTimeout(0) instead of Promise for async operations
  }
}

/**
 * Feature detection
 */
const features = {
  passiveEvents: (() => {
    let passive = false;
    try {
      const opts = Object.defineProperty({}, 'passive', {
        get: () => passive = true
      });
      window.addEventListener('test', null, opts);
      window.removeEventListener('test', null, opts);
    } catch (e) {}
    return passive;
  })(),
  
  customElements: 'customElements' in window,
  shadowDOM: 'attachShadow' in Element.prototype,
  eventPath: 'path' in Event.prototype || 'composedPath' in Event.prototype
};
```


