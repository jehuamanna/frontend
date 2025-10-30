# Performance Optimization Decision Tree

## Quick Decision Flow

```
START: Measure baseline FPS with DevTools
│
├─ FPS >= 60 with smooth interactions?
│  ├─ YES  → You're done! Monitor in production
│  └─ NO   → Continue diagnosis
│
├─ Frame time > 16ms consistently?
│  ├─ YES  → Identify bottleneck
│  └─ NO   → Check for dropped frames
│
├─ How many objects being rendered?
│  ├─ < 100       → Likely not rendering bottleneck
│  ├─ 100-500     → Apply state batching + viewport culling
│  ├─ 500-2000    → Apply viewport culling + culling
│  ├─ 2000-10000  → Apply spatial indexing (Quadtree)
│  └─ > 10000     → Apply Quadtree + dirty rectangles
│
├─ Canvas size?
│  ├─ < 2000x2000   → Standard optimizations sufficient
│  ├─ 2000x5000     → Consider tile-based rendering
│  └─ > 5000x5000   → Tile-based + worker rendering
│
├─ What's the bottleneck?
│  ├─ Memory growth    → Implement layer caching + cleanup
│  ├─ Rendering time   → Implement spatial indexing or tile-based
│  ├─ CPU usage        → Move to workers or reduce object count
│  └─ GPU bandwidth    → Implement dirty rectangles or layer caching
│
└─ Apply optimization → Measure again → Repeat until 60fps achieved
```

## Performance Scenarios & Solutions

### Scenario: Small Canvas, Many Objects (500-2000)

**Symptoms**:
- Frame time: 20-30ms
- FPS drops when zooming out
- Objects off-screen still rendered

**Root Cause**: Rendering invisible objects

**Solution Stack** (in order):
1. Viewport culling (5-10x improvement)
2. Context state batching (2-3x improvement)
3. Transform matrix optimization (already done)

**Implementation Time**: 2-3 hours
**Expected Result**: 60fps maintained

**Code Example**:
```javascript
// Step 1: Implement viewport calculation
calculateViewport() {
  return {
    x: -this.pan.x,
    y: -this.pan.y,
    width: this.canvas.width / this.zoom,
    height: this.canvas.height / this.zoom
  };
}

// Step 2: Filter visible objects
const visibleObjects = this.objects.filter(obj => 
  this.isInViewport(obj.bounds, viewport)
);

// Step 3: Batch by state
const byColor = visibleObjects.reduce((acc, obj) => {
  if (!acc[obj.color]) acc[obj.color] = [];
  acc[obj.color].push(obj);
  return acc;
}, {});

// Step 4: Render batched by color
for (const [color, group] of Object.entries(byColor)) {
  this.ctx.fillStyle = color;
  for (const obj of group) {
    obj.render(this.ctx);
  }
}
```

---

### Scenario: Medium Canvas, Many Objects (2000-5000)

**Symptoms**:
- Frame time: 25-40ms
- Worse at extreme zoom levels
- CPU usage constant regardless of visible area

**Root Cause**: Rendering thousands of invisible objects at extreme zoom

**Solution Stack**:
1. Spatial indexing - Quadtree (15-30x improvement)
2. Viewport culling (5-10x improvement)
3. Dirty rectangle tracking (additional 2-5x)

**Implementation Time**: 4-6 hours
**Expected Result**: 60fps maintained even at extreme zoom

**Decision Point**: 
```
Is Quadtree overhead worth it?
│
├─ YES if:
│  ├─ Object count > 1000
│  ├─ Zoom range wide (10%-6400%)
│  ├─ Scene mostly static
│  └─ Objects scattered across large area
│
└─ NO if:
   ├─ Object count < 500
   ├─ Objects clustered in viewport
   ├─ Frequent dynamic changes
   └─ Performance already good
```

**Implementation Steps**:
1. Build Quadtree on object initialization
2. Rebuild when objects move (debounced)
3. Query viewport, render only visible objects
4. Add dirty rectangle tracking for static objects

---

### Scenario: Large Canvas, Performance Issues

**Symptoms**:
- Canvas size 5000x5000 or larger
- First load takes time
- Memory usage grows
- Smooth interaction despite complexity

**Root Cause**: Rendering entire large canvas every frame

**Solution Stack**:
1. Tile-based rendering (10-50x improvement)
2. Asynchronous tile rendering
3. Progressive tile loading
4. Layer caching for static content

**Implementation Time**: 6-10 hours
**Expected Result**: Smooth panning/zooming at 60fps

**Architecture**:
```
Large Canvas
├─ Divide into 256x256 tiles
├─ Render tiles asynchronously
├─ Cache rendered tiles
├─ Composite visible tiles to main canvas
├─ Update tiles on viewport change
└─ Progressively load new tiles
```

**Tile Size Calculation**:
```javascript
const optimalTileSize = (canvasSize, targetFPS = 60) => {
  // Want to render ~50-100 tiles per frame for smooth updates
  const pixelsPerFrame = 1000000; // Adjust based on device
  const tilesNeeded = 50;
  return Math.sqrt(pixelsPerFrame / tilesNeeded);
};

// Examples:
// Small devices: 128x128 tiles
// Medium devices: 256x256 tiles
// Large monitors: 512x512 tiles
```

---

### Scenario: Complex Rendering Operations

**Symptoms**:
- Main thread blocked during render
- Input lag during heavy operations
- High CPU usage on main thread

**Root Cause**: Heavy rendering blocking user input

**Solution Stack**:
1. Move rendering to Web Workers (2-4x improvement)
2. OffscreenCanvas for background rendering
3. Progressive rendering with priority

**Implementation Time**: 5-8 hours
**Expected Result**: Responsive UI, smooth interaction

**Architecture**:
```javascript
// Main thread
canvas.addEventListener('mousemove', handlePan); // Always responsive

// Worker thread
worker.postMessage({ 
  type: 'render',
  tiles: visibleTiles,
  zoom: this.zoom
});

worker.onmessage = (e) => {
  const bitmap = e.data;
  ctx.drawImage(bitmap, 0, 0); // Composite immediately
};
```

---

### Scenario: Memory Issues

**Symptoms**:
- Memory usage grows over time
- Page becomes unresponsive after extended use
- Garbage collection pauses visible

**Root Cause**: Caches not being invalidated, old objects not freed

**Solution Stack**:
1. Layer cache cleanup strategy
2. Object pooling for frequently created objects
3. WeakMap for automatic cleanup

**Implementation**:
```javascript
class CacheManager {
  constructor(maxSize = 50) {
    this.cache = new Map();
    this.maxSize = maxSize;
    this.lruQueue = [];
  }
  
  set(key, value) {
    if (this.cache.has(key)) {
      this.lruQueue.splice(this.lruQueue.indexOf(key), 1);
    }
    
    this.cache.set(key, value);
    this.lruQueue.push(key);
    
    // Evict least recently used if exceeded
    if (this.cache.size > this.maxSize) {
      const lru = this.lruQueue.shift();
      this.cache.delete(lru);
    }
  }
  
  get(key) {
    if (!this.cache.has(key)) return null;
    
    // Mark as recently used
    this.lruQueue.splice(this.lruQueue.indexOf(key), 1);
    this.lruQueue.push(key);
    
    return this.cache.get(key);
  }
}
```

---

## Performance Optimization Checklist

### Phase 1: Foundation (Must Do)
- [ ] GPU acceleration enabled (context flags)
- [ ] RequestAnimationFrame implemented
- [ ] Transform matrix applied once per frame
- [ ] Context state managed (single save/restore)
- [ ] DevTools baseline FPS measured

**Time**: 0-1 hour
**Performance gain**: 10-50x

### Phase 2: Basic Optimization (Recommended)
- [ ] Viewport culling implemented
- [ ] Context state batching for colors
- [ ] Keyboard shortcuts working
- [ ] Touch/trackpad zoom smooth

**Time**: 2-4 hours
**Performance gain**: 2-10x

### Phase 3: Advanced Optimization (If Needed)
- [ ] Spatial indexing (Quadtree) if 2000+ objects
- [ ] Dirty rectangle tracking if static background
- [ ] Layer caching for non-animated layers
- [ ] Performance profiling dashboard

**Time**: 4-8 hours
**Performance gain**: 5-40x

### Phase 4: Expert Optimization (Advanced)
- [ ] Tile-based rendering for large canvas
- [ ] Worker rendering for complex ops
- [ ] Progressive loading with priority queue
- [ ] Production metrics monitoring

**Time**: 8-16 hours
**Performance gain**: 10-100x

---

## Profiling Before/After

### Before Optimization
```
Frame 1: 45ms (dropped frame)
Frame 2: 42ms (dropped frame)
Frame 3: 18ms (acceptable)
Average: 35ms (28 fps)
P95: 48ms
```

### After Basic Optimization
```
Frame 1: 14ms
Frame 2: 15ms
Frame 3: 15ms
Average: 14.7ms (68 fps)
P95: 16ms
```

### After Advanced Optimization
```
Frame 1: 8ms
Frame 2: 9ms
Frame 3: 8ms
Average: 8.3ms (120 fps, capped at 60fps display)
P95: 10ms
```

---

## Common Pitfalls & Solutions

| Pitfall | Impact | Solution |
|---------|--------|----------|
| Reading pixels in render loop | 100x slowdown | Move getImageData outside render loop |
| Too many save/restore calls | 5x slowdown | Batch transformations |
| Rendering everything always | 10-99x slowdown | Add viewport culling |
| Large cache never cleared | Memory leak | Implement LRU cache eviction |
| Tile size too small | Overhead > benefits | Use 256-512px tiles |
| Tile size too large | Visible loading delay | Use 128-256px tiles |
| Workers for simple operations | Slower due to overhead | Use workers only for complex ops |
| No performance monitoring | Can't identify issues | Add metrics collection |

---

## Decision Matrix: Which Optimization?

```javascript
const selectOptimization = (objectCount, canvasSize, avgFrameTime) => {
  // Automatic optimizations always applied
  
  if (avgFrameTime < 16) return "DONE - Already 60fps";
  
  if (objectCount < 100) {
    return "Profile to identify bottleneck - likely not rendering";
  }
  
  if (objectCount < 500) {
    if (avgFrameTime > 30) return "Apply viewport culling (5-10x)";
    if (avgFrameTime > 20) return "Apply state batching (2-5x)";
  }
  
  if (objectCount < 2000) {
    if (avgFrameTime > 30) return "Apply Quadtree + viewport culling (10-30x)";
    if (avgFrameTime > 20) return "Apply viewport culling (5-10x)";
  }
  
  if (objectCount < 10000) {
    if (avgFrameTime > 40) return "Apply Quadtree + dirty rectangles (20-50x)";
    if (avgFrameTime > 30) return "Apply Quadtree (10-30x)";
  }
  
  if (canvasSize > 5000) {
    if (avgFrameTime > 40) return "Apply tile-based rendering (10-50x)";
    if (avgFrameTime > 30) return "Apply Quadtree + progressive rendering";
  }
  
  return "Apply worker rendering for heavy ops";
};
```

---

## When to Use Each Optimization

### Viewport Culling
**Use when**: 100+ objects or many off-screen
**Skip when**: <50 objects, all visible
**Effort**: 1-2 hours
**Gain**: 5-10x

### Quadtree Spatial Indexing
**Use when**: 1000+ objects or extreme zoom
**Skip when**: < 500 objects, good FPS
**Effort**: 3-4 hours
**Gain**: 10-40x

### Tile-Based Rendering
**Use when**: Canvas 5000x5000+ or static content
**Skip when**: < 2000x2000 canvas
**Effort**: 6-10 hours
**Gain**: 10-100x

### Worker Rendering
**Use when**: Complex rendering per frame blocking UI
**Skip when**: Simple shapes, good performance
**Effort**: 4-6 hours
**Gain**: 2-4x (with overhead)

### Layer Caching
**Use when**: Layers don't change frequently
**Skip when**: Everything animates constantly
**Effort**: 2-3 hours
**Gain**: 10-100x for static layers

### Dirty Rectangle Tracking
**Use when**: Small portion of canvas changes per frame
**Skip when**: Entire canvas redrawn always
**Effort**: 3-5 hours
**Gain**: 5-99x (depends on dirty area %)

---

## Production Monitoring Essentials

```javascript
class ProductionMetrics {
  recordFrameTime(duration) {
    metrics.histogram('canvas.frame_time', duration);
    
    if (duration > 16) {
      metrics.increment('canvas.dropped_frames');
    }
    
    if (duration > 32) {
      metrics.increment('canvas.severe_jank');
      console.warn(`Severe jank: ${duration}ms`);
    }
  }
  
  recordSceneComplexity(objectCount) {
    metrics.gauge('canvas.object_count', objectCount);
  }
  
  recordMemoryUsage() {
    if (performance.memory) {
      metrics.gauge('canvas.memory_used', 
        performance.memory.usedJSHeapSize / 1024 / 1024
      );
    }
  }
}
```

**Alerts to Set**:
- Frame time > 20ms for > 10 seconds
- Memory growth > 50MB in 5 minutes
- Dropped frames > 5 per minute
- CPU usage > 80% on main thread

