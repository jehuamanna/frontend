
## Supporting Data Structures

**LRU Cache for Selector Matching**:

```javascript
/**
 * Least Recently Used (LRU) Cache
 * O(1) get and set operations
 */
class LRUCache {
  constructor(maxSize = 1000) {
    this.maxSize = maxSize;
    this.cache = new Map();
  }
  
  get(key) {
    if (!this.cache.has(key)) {
      return undefined;
    }
    
    // Move to end (most recently used)
    const value = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, value);
    
    return value;
  }
  
  set(key, value) {
    // Remove if exists (will re-add at end)
    if (this.cache.has(key)) {
      this.cache.delete(key);
    }
    
    // Remove oldest if at capacity
    if (this.cache.size >= this.maxSize) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
    
    this.cache.set(key, value);
  }
  
  clear() {
    this.cache.clear();
  }
  
  get size() {
    return this.cache.size;
  }
}
```

**Event Profiler**:

```javascript
/**
 * Performance profiler for event handlers
 */
class EventProfiler {
  constructor() {
    this.events = [];
    this.handlers = new Map();
    this.currentEventId = 0;
  }
  
  startEvent(eventType, target) {
    const id = this.currentEventId++;
    this.events.push({
      id,
      eventType,
      target: this.getElementSelector(target),
      startTime: performance.now(),
      endTime: null,
      handlers: []
    });
    return id;
  }
  
  endEvent(eventId) {
    const event = this.events.find(e => e.id === eventId);
    if (event) {
      event.endTime = performance.now();
      event.duration = event.endTime - event.startTime;
    }
  }
  
  recordHandler(handlerId, duration) {
    if (!this.handlers.has(handlerId)) {
      this.handlers.set(handlerId, {
        callCount: 0,
        totalDuration: 0,
        avgDuration: 0,
        maxDuration: 0
      });
    }
    
    const stats = this.handlers.get(handlerId);
    stats.callCount++;
    stats.totalDuration += duration;
    stats.avgDuration = stats.totalDuration / stats.callCount;
    stats.maxDuration = Math.max(stats.maxDuration, duration);
  }
  
  getStats() {
    return {
      totalEvents: this.events.length,
      avgEventDuration: this.events.length > 0
        ? this.events.reduce((sum, e) => sum + (e.duration || 0), 0) / this.events.length
        : 0,
      handlerStats: Array.from(this.handlers.entries()).map(([id, stats]) => ({
        handlerId: id,
        ...stats
      })),
      slowestHandlers: this.getSlowestHandlers(10)
    };
  }
  
  getSlowestHandlers(limit = 10) {
    return Array.from(this.handlers.entries())
      .map(([id, stats]) => ({ handlerId: id, ...stats }))
      .sort((a, b) => b.avgDuration - a.avgDuration)
      .slice(0, limit);
  }
  
  getElementSelector(element) {
    if (!element) return 'unknown';
    
    let selector = element.tagName.toLowerCase();
    if (element.id) {
      selector += `#${element.id}`;
    }
    if (element.className) {
      selector += `.${element.className.split(' ').join('.')}`;
    }
    
    return selector;
  }
  
  clear() {
    this.events = [];
    this.handlers.clear();
  }
  
  generateReport() {
    const stats = this.getStats();
    
    console.group('Event Delegation Performance Report');
    console.log(`Total Events: ${stats.totalEvents}`);
    console.log(`Avg Event Duration: ${stats.avgEventDuration.toFixed(3)}ms`);
    console.log('\nSlowest Handlers:');
    console.table(stats.slowestHandlers);
    console.groupEnd();
  }
}
```

**Priority Queue for Handler Execution**:

```javascript
/**
 * Priority Queue using binary heap
 * O(log n) insertion, O(1) peek, O(log n) extraction
 */
class PriorityQueue {
  constructor(comparator = (a, b) => a.priority - b.priority) {
    this.heap = [];
    this.comparator = comparator;
  }
  
  push(item) {
    this.heap.push(item);
    this.bubbleUp(this.heap.length - 1);
  }
  
  pop() {
    if (this.isEmpty()) return null;
    
    const result = this.heap[0];
    const last = this.heap.pop();
    
    if (!this.isEmpty()) {
      this.heap[0] = last;
      this.bubbleDown(0);
    }
    
    return result;
  }
  
  peek() {
    return this.isEmpty() ? null : this.heap[0];
  }
  
  isEmpty() {
    return this.heap.length === 0;
  }
  
  bubbleUp(index) {
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      
      if (this.comparator(this.heap[index], this.heap[parentIndex]) >= 0) {
        break;
      }
      
      this.swap(index, parentIndex);
      index = parentIndex;
    }
  }
  
  bubbleDown(index) {
    while (true) {
      const leftChild = 2 * index + 1;
      const rightChild = 2 * index + 2;
      let smallest = index;
      
      if (leftChild < this.heap.length && 
          this.comparator(this.heap[leftChild], this.heap[smallest]) < 0) {
        smallest = leftChild;
      }
      
      if (rightChild < this.heap.length && 
          this.comparator(this.heap[rightChild], this.heap[smallest]) < 0) {
        smallest = rightChild;
      }
      
      if (smallest === index) break;
      
      this.swap(index, smallest);
      index = smallest;
    }
  }
  
  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }
}
```

## Advanced Selector Matching

**CSS Selector Engine with Optimization**:

```javascript
/**
 * Optimized selector matching engine
 */
class SelectorMatcher {
  constructor() {
    // Cache compiled selectors
    this.selectorCache = new Map();
    
    // Simple selector optimization
    this.simpleSelectors = new Set();
  }
  
  /**
   * Match element against selector with optimization
   */
  match(element, selector) {
    if (!selector) return true;
    
    // Fast path for simple selectors
    if (this.isSimpleSelector(selector)) {
      return this.matchSimple(element, selector);
    }
    
    // Use native matches for complex selectors
    try {
      return element.matches(selector);
    } catch (error) {
      console.warn(`Invalid selector: ${selector}`);
      return false;
    }
  }
  
  /**
   * Check if selector is simple (class, id, or tag)
   */
  isSimpleSelector(selector) {
    return /^[#.]?[\w-]+$/.test(selector);
  }
  
  /**
   * Optimized matching for simple selectors
   */
  matchSimple(element, selector) {
    if (selector.startsWith('#')) {
      return element.id === selector.slice(1);
    }
    
    if (selector.startsWith('.')) {
      return element.classList.contains(selector.slice(1));
    }
    
    return element.tagName.toLowerCase() === selector.toLowerCase();
  }
  
  /**
   * Find closest ancestor matching selector
   */
  closest(element, selector, root) {
    let current = element;
    
    while (current && current !== root) {
      if (this.match(current, selector)) {
        return current;
      }
      current = current.parentElement;
    }
    
    return null;
  }
  
  /**
   * Compile selector into optimized matcher
   */
  compile(selector) {
    if (this.selectorCache.has(selector)) {
      return this.selectorCache.get(selector);
    }
    
    const matcher = {
      selector,
      isSimple: this.isSimpleSelector(selector),
      parts: this.parseSelector(selector)
    };
    
    this.selectorCache.set(selector, matcher);
    return matcher;
  }
  
  /**
   * Parse selector into parts
   */
  parseSelector(selector) {
    // Simple parsing for common patterns
    const parts = [];
    
    // Split by combinators
    const tokens = selector.split(/\s*([>+~\s])\s*/);
    
    for (let i = 0; i < tokens.length; i += 2) {
      const part = tokens[i];
      const combinator = tokens[i + 1] || ' ';
      
      if (part) {
        parts.push({ selector: part, combinator });
      }
    }
    
    return parts;
  }
}
```

**Event Context Manager**:

```javascript
/**
 * Manages event context and conditional execution
 */
class EventContext {
  constructor() {
    this.contexts = new WeakMap();
    this.globalState = new Map();
  }
  
  /**
   * Set context data for an element
   */
  setContext(element, key, value) {
    if (!this.contexts.has(element)) {
      this.contexts.set(element, new Map());
    }
    
    this.contexts.get(element).set(key, value);
  }
  
  /**
   * Get context data for an element
   */
  getContext(element, key) {
    const context = this.contexts.get(element);
    if (!context) return undefined;
    
    return context.get(key);
  }
  
  /**
   * Check if element has context
   */
  hasContext(element, key) {
    const context = this.contexts.get(element);
    return context ? context.has(key) : false;
  }
  
  /**
   * Set global state
   */
  setGlobal(key, value) {
    this.globalState.set(key, value);
  }
  
  /**
   * Get global state
   */
  getGlobal(key) {
    return this.globalState.get(key);
  }
  
  /**
   * Create conditional handler
   */
  createConditional(condition) {
    return (event, element) => {
      if (typeof condition === 'function') {
        return condition.call(this, event, element);
      }
      
      if (typeof condition === 'object') {
        return this.evaluateConditionObject(condition, event, element);
      }
      
      return true;
    };
  }
  
  /**
   * Evaluate condition object
   */
  evaluateConditionObject(condition, event, element) {
    // Context-based conditions
    if (condition.context) {
      for (const [key, value] of Object.entries(condition.context)) {
        if (this.getContext(element, key) !== value) {
          return false;
        }
      }
    }
    
    // State-based conditions
    if (condition.state) {
      for (const [key, value] of Object.entries(condition.state)) {
        if (this.getGlobal(key) !== value) {
          return false;
        }
      }
    }
    
    // Attribute-based conditions
    if (condition.attributes) {
      for (const [attr, value] of Object.entries(condition.attributes)) {
        if (element.getAttribute(attr) !== value) {
          return false;
        }
      }
    }
    
    return true;
  }
}
```

## Custom Event System

**Custom Event Emitter**:

```javascript
/**
 * Custom event system for synthetic events
 */
class CustomEventSystem {
  constructor(delegator) {
    this.delegator = delegator;
    this.eventQueue = [];
    this.isProcessing = false;
  }
  
  /**
   * Create and dispatch custom event
   */
  dispatch(eventType, target, detail = {}, options = {}) {
    const event = new CustomEvent(eventType, {
      detail: detail,
      bubbles: options.bubbles !== false,
      cancelable: options.cancelable !== false,
      composed: options.composed || false
    });
    
    // Add to queue for batched processing
    if (options.batch) {
      this.eventQueue.push({ event, target });
      this.scheduleProcessing();
      return event;
    }
    
    // Dispatch immediately
    return this.dispatchEvent(event, target);
  }
  
  /**
   * Dispatch event through delegation system
   */
  dispatchEvent(event, target) {
    // Use delegation system if available
    if (this.delegator) {
      this.delegator.handleEvent(event, target);
    } else {
      target.dispatchEvent(event);
    }
    
    return event;
  }
  
  /**
   * Schedule batched event processing
   */
  scheduleProcessing() {
    if (this.isProcessing) return;
    
    this.isProcessing = true;
    
    requestAnimationFrame(() => {
      this.processQueue();
      this.isProcessing = false;
    });
  }
  
  /**
   * Process queued events
   */
  processQueue() {
    const batch = this.eventQueue.splice(0);
    
    for (const { event, target } of batch) {
      this.dispatchEvent(event, target);
    }
  }
  
  /**
   * Create synthetic event from native event
   */
  createSynthetic(nativeEvent, overrides = {}) {
    const syntheticEvent = {
      type: nativeEvent.type,
      target: nativeEvent.target,
      currentTarget: nativeEvent.currentTarget,
      bubbles: nativeEvent.bubbles,
      cancelable: nativeEvent.cancelable,
      defaultPrevented: nativeEvent.defaultPrevented,
      timeStamp: nativeEvent.timeStamp,
      
      // Mouse events
      clientX: nativeEvent.clientX,
      clientY: nativeEvent.clientY,
      pageX: nativeEvent.pageX,
      pageY: nativeEvent.pageY,
      screenX: nativeEvent.screenX,
      screenY: nativeEvent.screenY,
      
      // Keyboard events
      key: nativeEvent.key,
      code: nativeEvent.code,
      keyCode: nativeEvent.keyCode,
      altKey: nativeEvent.altKey,
      ctrlKey: nativeEvent.ctrlKey,
      metaKey: nativeEvent.metaKey,
      shiftKey: nativeEvent.shiftKey,
      
      // Touch events
      touches: nativeEvent.touches,
      changedTouches: nativeEvent.changedTouches,
      targetTouches: nativeEvent.targetTouches,
      
      // Methods
      preventDefault: () => nativeEvent.preventDefault(),
      stopPropagation: () => nativeEvent.stopPropagation(),
      stopImmediatePropagation: () => nativeEvent.stopImmediatePropagation(),
      
      // Original event
      nativeEvent: nativeEvent,
      
      // Overrides
      ...overrides
    };
    
    return syntheticEvent;
  }
}
```

**Event Composer**:

```javascript
/**
 * Compose multiple event handlers
 */
class EventComposer {
  /**
   * Compose handlers with middleware pattern
   */
  static compose(...handlers) {
    return function composedHandler(event, element) {
      let index = 0;
      
      const next = () => {
        if (index >= handlers.length) return;
        
        const handler = handlers[index++];
        return handler(event, element, next);
      };
      
      return next();
    };
  }
  
  /**
   * Create throttled handler
   */
  static throttle(handler, delay = 100) {
    let lastCall = 0;
    let timeoutId = null;
    
    return function throttledHandler(event, element) {
      const now = Date.now();
      
      if (now - lastCall >= delay) {
        lastCall = now;
        return handler.call(this, event, element);
      }
      
      // Schedule for later
      if (!timeoutId) {
        timeoutId = setTimeout(() => {
          lastCall = Date.now();
          timeoutId = null;
          handler.call(this, event, element);
        }, delay - (now - lastCall));
      }
    };
  }
  
  /**
   * Create debounced handler
   */
  static debounce(handler, delay = 100) {
    let timeoutId = null;
    
    return function debouncedHandler(event, element) {
      clearTimeout(timeoutId);
      
      timeoutId = setTimeout(() => {
        handler.call(this, event, element);
      }, delay);
    };
  }
  
  /**
   * Create handler that only fires once
   */
  static once(handler) {
    let called = false;
    
    return function onceHandler(event, element) {
      if (called) return;
      called = true;
      return handler.call(this, event, element);
    };
  }
  
  /**
   * Create conditional handler
   */
  static when(condition, handler) {
    return function conditionalHandler(event, element) {
      if (condition(event, element)) {
        return handler.call(this, event, element);
      }
    };
  }
  
  /**
   * Create handler with retry logic
   */
  static retry(handler, maxRetries = 3, delay = 1000) {
    return async function retryHandler(event, element) {
      let lastError;
      
      for (let i = 0; i < maxRetries; i++) {
        try {
          return await handler.call(this, event, element);
        } catch (error) {
          lastError = error;
          
          if (i < maxRetries - 1) {
            await new Promise(resolve => setTimeout(resolve, delay));
          }
        }
      }
      
      throw lastError;
    };
  }
}
```

## Error Handling and Edge Cases

**Robust Error Handling**:

```javascript
/**
 * Error handler for event delegation
 */
class EventErrorHandler {
  constructor(delegator) {
    this.delegator = delegator;
    this.errors = [];
    this.maxErrors = 100;
    this.errorListeners = new Set();
  }
  
  /**
   * Handle error in event handler
   */
  handleError(error, context) {
    const errorRecord = {
      error: error,
      message: error.message,
      stack: error.stack,
      context: {
        eventType: context.event?.type,
        target: this.getElementInfo(context.target),
        handlerId: context.descriptor?.id,
        timestamp: Date.now()
      }
    };
    
    this.errors.push(errorRecord);
    
    // Keep only recent errors
    if (this.errors.length > this.maxErrors) {
      this.errors.shift();
    }
    
    // Notify error listeners
    this.notifyErrorListeners(errorRecord);
    
    // Log to console in development
    if (process.env.NODE_ENV === 'development') {
      console.error('[EventDelegator] Handler error:', errorRecord);
    }
    
    // Send to error tracking service
    this.reportToService(errorRecord);
  }
  
  /**
   * Get element information for debugging
   */
  getElementInfo(element) {
    if (!element) return null;
    
    return {
      tagName: element.tagName,
      id: element.id,
      className: element.className,
      selector: this.getElementSelector(element)
    };
  }
  
  /**
   * Get CSS selector for element
   */
  getElementSelector(element) {
    if (!element) return 'unknown';
    
    let selector = element.tagName.toLowerCase();
    
    if (element.id) {
      selector += `#${element.id}`;
    } else if (element.className) {
      const classes = element.className.split(' ').filter(c => c);
      if (classes.length > 0) {
        selector += `.${classes.join('.')}`;
      }
    }
    
    return selector;
  }
  
  /**
   * Add error listener
   */
  onError(listener) {
    this.errorListeners.add(listener);
  }
  
  /**
   * Remove error listener
   */
  offError(listener) {
    this.errorListeners.delete(listener);
  }
  
  /**
   * Notify error listeners
   */
  notifyErrorListeners(errorRecord) {
    for (const listener of this.errorListeners) {
      try {
        listener(errorRecord);
      } catch (error) {
        console.error('[EventDelegator] Error in error listener:', error);
      }
    }
  }
  
  /**
   * Report to error tracking service
   */
  reportToService(errorRecord) {
    // Integration with Sentry, LogRocket, etc.
    if (window.Sentry) {
      window.Sentry.captureException(errorRecord.error, {
        tags: {
          component: 'EventDelegator',
          eventType: errorRecord.context.eventType
        },
        extra: errorRecord.context
      });
    }
  }
  
  /**
   * Get recent errors
   */
  getRecentErrors(limit = 10) {
    return this.errors.slice(-limit);
  }
  
  /**
   * Clear error history
   */
  clearErrors() {
    this.errors = [];
  }
}

/**
 * Handle edge cases
 */

// Edge Case 1: Detached elements
function handleDetachedElements(delegator) {
  const observer = new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      // Clean up handlers for removed nodes
      for (const node of mutation.removedNodes) {
        if (node.nodeType === Node.ELEMENT_NODE) {
          delegator.cleanupElement(node);
        }
      }
    }
  });
  
  observer.observe(delegator.root, {
    childList: true,
    subtree: true
  });
  
  return observer;
}

// Edge Case 2: Shadow DOM
function handleShadowDOM(delegator, shadowRoot) {
  // Create separate delegator for shadow root
  const shadowDelegator = new EventDelegator(shadowRoot, delegator.options);
  
  // Forward events to main delegator if needed
  shadowDelegator.use((context) => {
    if (context.event.composed) {
      delegator.handleEvent(context.event, context.target);
    }
  });
  
  return shadowDelegator;
}

// Edge Case 3: Event retargeting
function retargetEvent(event, newTarget) {
  Object.defineProperty(event, 'target', {
    value: newTarget,
    writable: false,
    configurable: true
  });
}

// Edge Case 4: Circular event prevention
class CircularEventPreventer {
  constructor() {
    this.processing = new WeakSet();
  }
  
  isProcessing(element, eventType) {
    const key = { element, eventType };
    return this.processing.has(key);
  }
  
  markProcessing(element, eventType) {
    const key = { element, eventType };
    this.processing.add(key);
    
    // Clean up after event loop
    setTimeout(() => {
      this.processing.delete(key);
    }, 0);
  }
}
```


