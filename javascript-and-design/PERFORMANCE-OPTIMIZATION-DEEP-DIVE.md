# High-Fidelity Canvas Performance Optimization: Deep Dive

## Table of Contents
1. Basic Performance Optimizations
2. Advanced Optimization Opportunities
3. Optimization Decision Matrix
4. Real-world Tuning Strategy

---

## Basic Performance Optimizations

### 1. RequestAnimationFrame Throttling: Capped at 60fps (16ms per frame)

**Why it matters**: Browser repaints happen at screen refresh rate (typically 60Hz). Rendering faster than this wastes CPU/GPU resources and causes tearing.

**How it works**: RAF automatically syncs with browser paint cycle, ensuring one render per frame maximum.

**Implementation**:
```javascript
startRenderLoop() {
  const loop = (timestamp) => {
    this.render(timestamp);
    requestAnimationFrame(loop); // Automatically throttled to 60fps
  };
  requestAnimationFrame(loop);
}
```

**Performance Impact**:
- Reduces unnecessary renders by 95%+ on idle
- Allocates ~16ms per frame for all operations
- One-frame delay in response (imperceptible to users)

**When to use**: Always - it's automatic with RAF

---

### 2. GPU Acceleration: Hardware-accelerated canvas rendering

**Why it matters**: GPU rendering is 10-100x faster than CPU for graphics operations. Modern browsers offload canvas to GPU with the right settings.

**How it works**: Canvas context created with optimal flags for GPU acceleration:
```javascript
this.ctx = this.canvas.getContext('2d', {
  alpha: true,
  antialias: true,
  willReadFrequently: false,  // Key: tells browser we won't read pixels often
  preserveDrawingBuffer: false // Key: don't keep buffer between frames
});
```

**Key flags explained**:
- `willReadFrequently: false`: Enables GPU acceleration by promising no getImageData calls
- `preserveDrawingBuffer: false`: Allows browser to optimize memory without preserving previous frame

**Performance Characteristics**:
- CPU rendering: 1,000-5,000 objects per frame at 60fps
- GPU rendering: 50,000+ objects per frame at 60fps
- Speedup: 10-50x for complex scenes

**Configuration Options**:
```javascript
// For opaque backgrounds (no alpha)
this.ctx = this.canvas.getContext('2d', { alpha: false });

// For high-quality image scaling
ctx.imageSmoothingEnabled = true;
ctx.imageSmoothingQuality = 'high';

// Avoid reading pixels in render loop (kills GPU acceleration)
// GOOD: Read once per interaction
const imageData = ctx.getImageData(0, 0, 100, 100);

// BAD: Reading in render loop
function render() {
  const data = ctx.getImageData(0, 0, canvas.width, canvas.height);
  // GPU acceleration disabled!
}
```

**Trade-offs**:
- GPU memory usage: ~8x canvas size in RGBA format
- For 2000x2000 canvas: 16MB GPU memory
- Automatic CPU fallback if GPU unavailable
- Browser support: Chrome 26+, Firefox 42+, Safari 10+, Edge 12+

---

### 3. DPI Caching: Compute device pixel ratio once

**Why it matters**: Accessing window.devicePixelRatio is synchronous but relatively expensive. Computing it multiple times per frame wastes CPU cycles.

**Current Implementation**:
```javascript
constructor() {
  this.devicePixelRatio = window.devicePixelRatio || 1;
}

setupDPI() {
  const dpr = this.enableRetina ? this.devicePixelRatio : 1;
  // Use cached dpr value
}
```

**Performance Impact**:
- Direct access: ~0.1ms per call (negligible alone)
- Called 1000x per second: 100ms waste!
- Caching eliminates 99% of overhead

**Advanced: Dynamic DPI Change Detection**:
```javascript
setupDPIChangeListener() {
  const observer = new ResizeObserver(() => {
    const newDpr = window.devicePixelRatio;
    if (newDpr !== this.devicePixelRatio) {
      console.log(`DPI changed: ${this.devicePixelRatio}x to ${newDpr}x`);
      this.devicePixelRatio = newDpr;
      this.setupDPI();
    }
  });
  observer.observe(this.container);
}
```

**When DPI Changes Occur**:
- User drags window between monitors (macOS with mixed 1x/2x)
- System DPI scaling changes (Windows)
- Browser zoom is applied to window

---

### 4. Context State Management: Minimize save/restore calls

**Why it matters**: Canvas context state (fill, stroke, transform, etc.) management copies state objects. Save/restore are expensive operations.

**Performance Impact**:
- save() call: ~0.05ms
- restore() call: ~0.05ms
- Total per frame: ~0.1ms
- At 60fps: ~6ms per second waste if not batched

**Current (Optimal) Implementation**:
```javascript
render(timestamp) {
  // Compute transformation ONCE
  this.ctx.save();
  
  // Apply transformation matrix (3 operations only)
  this.ctx.translate(logicalWidth / 2, logicalHeight / 2);
  this.ctx.scale(this.zoom, this.zoom);
  this.ctx.translate(-logicalWidth / 2 + this.pan.x, -logicalHeight / 2 + this.pan.y);
  
  // All objects rendered with same transform
  for (const layer of this.layers) {
    layer.render(this.ctx);
  }
  
  this.ctx.restore();
}
```

**State Batching by Color**:
```javascript
// BAD: Multiple state changes
render() {
  for (const shape of shapes) {
    this.ctx.strokeStyle = shape.strokeStyle;
    this.ctx.fillStyle = shape.fillStyle;
    shape.render(this.ctx);
  }
}

// GOOD: Sort by state, batch renders
render() {
  const byColor = shapes.reduce((acc, shape) => {
    const key = shape.fillStyle + shape.strokeStyle;
    if (!acc[key]) acc[key] = [];
    acc[key].push(shape);
    return acc;
  }, {});
  
  for (const [color, group] of Object.entries(byColor)) {
    this.ctx.fillStyle = color;
    for (const shape of group) {
      shape.render(this.ctx);
    }
  }
}
```

**Performance Gains**:
- Reduced save/restore: 50% less overhead
- State batching: 30-50% speedup for multi-object renders
- Overall frame time: 2-5ms savings

---

### 5. Transformation Matrix: Pre-computed and applied once

**Why it matters**: Computing and applying 2D affine transformation for every object is expensive. Apply once to canvas context for all objects.

**Current (Optimal) Approach**:
```javascript
render(timestamp) {
  // Compute transformation ONCE
  this.ctx.save();
  
  // Apply transformation matrix (3 operations only)
  this.ctx.translate(logicalWidth / 2, logicalHeight / 2);
  this.ctx.scale(this.zoom, this.zoom);
  this.ctx.translate(-logicalWidth / 2 + this.pan.x, -logicalHeight / 2 + this.pan.y);
  
  // All objects rendered with same transform
  for (const layer of this.layers) {
    layer.render(this.ctx);
  }
  
  this.ctx.restore();
}
```

**Why This is Efficient**:
- Canvas handles transformation in GPU
- All draw calls automatically transformed
- No per-object math needed

**Alternative (Bad) Approach**:
```javascript
// BAD: Transform each object individually
for (const shape of shapes) {
  const x = shape.x * this.zoom + this.pan.x;
  const y = shape.y * this.zoom + this.pan.y;
  ctx.drawImage(shape.image, x, y);
}
```

**Why This is Slow**:
- Per-object calculation: O(n) multiplications
- CPU-side math on every frame
- Cache misses on each calculation
- No GPU optimization possible

**Performance Comparison**:
- Single transform: ~0.5ms for 10,000 objects
- Per-object transform: ~5-10ms for 10,000 objects
- Speedup: 10-20x

**Matrix Composition for Complex Transforms**:
```javascript
class TransformationMatrix {
  constructor(a, b, c, d, e, f) {
    this.a = a; this.b = b; this.c = c;
    this.d = d; this.e = e; this.f = f;
  }
  
  // Pre-multiply matrices for complex transforms
  multiply(other) {
    return new TransformationMatrix(
      this.a * other.a + this.c * other.b,
      this.b * other.a + this.d * other.b,
      this.a * other.c + this.c * other.d,
      this.b * other.c + this.d * other.d,
      this.a * other.e + this.c * other.f + this.e,
      this.b * other.e + this.d * other.f + this.f
    );
  }
  
  apply(ctx) {
    ctx.transform(this.a, this.b, this.c, this.d, this.e, this.f);
  }
}
```

---

## Advanced Optimization Opportunities

### 1. Dirty Rectangle Tracking: Only re-render changed regions

**Why implement**: Most frames, only a small portion of canvas changes. Repainting everything wastes GPU bandwidth.

**How it works**: Track which rectangles changed and only redraw those areas.

**Basic Implementation**:
```javascript
class DirtyRectangleTracker {
  constructor() {
    this.dirtyRects = [];
    this.rects = new Map();
  }
  
  markDirty(shapeId, x, y, width, height) {
    this.dirtyRects.push({ x, y, width, height });
    this.rects.set(shapeId, { x, y, width, height });
  }
  
  merge() {
    if (this.dirtyRects.length === 0) return [];
    
    let rects = [...this.dirtyRects];
    let merged = [];
    
    while (rects.length > 0) {
      const rect = rects.pop();
      let found = false;
      
      for (let i = 0; i < rects.length; i++) {
        if (this.overlaps(rect, rects[i])) {
          const mergedRect = this.merge2(rect, rects[i]);
          rects[i] = mergedRect;
          found = true;
          break;
        }
      }
      
      if (!found) merged.push(rect);
    }
    
    return merged;
  }
  
  overlaps(r1, r2) {
    return !(r1.x + r1.width < r2.x || r2.x + r2.width < r1.x ||
             r1.y + r1.height < r2.y || r2.y + r2.height < r1.y);
  }
  
  merge2(r1, r2) {
    const x1 = Math.min(r1.x, r2.x);
    const y1 = Math.min(r1.y, r2.y);
    const x2 = Math.max(r1.x + r1.width, r2.x + r2.width);
    const y2 = Math.max(r1.y + r1.height, r2.y + r2.height);
    return { x: x1, y: y1, width: x2 - x1, height: y2 - y1 };
  }
}
```

**Rendering with Dirty Rects**:
```javascript
render(timestamp) {
  const dirtyRects = this.dirtyRectTracker.merge();
  
  for (const rect of dirtyRects) {
    this.ctx.clearRect(rect.x, rect.y, rect.width, rect.height);
    
    this.ctx.save();
    this.ctx.beginPath();
    this.ctx.rect(rect.x, rect.y, rect.width, rect.height);
    this.ctx.clip();
    
    for (const layer of this.layers) {
      layer.render(this.ctx);
    }
    
    this.ctx.restore();
  }
  
  this.dirtyRectTracker.reset();
}
```

**Performance Gains**:
- 10% canvas dirty: 9x faster
- 5% canvas dirty: 19x faster
- 1% canvas dirty: 99x faster

**Trade-offs**:
- Complexity: Moderate overhead
- Not worth it for: Simple scenes with few objects
- Worth it for: Complex scenes with 1000+ objects
- Breakeven point: ~200 objects per frame

---

### 2. Spatial Indexing: Quadtree for object culling

**Why implement**: At extreme zoom (6400%), most objects are off-screen. Without culling, we render thousands of invisible objects.

**Quadtree Structure**:
```javascript
class Quadtree {
  constructor(bounds, maxObjects = 10, maxLevels = 8, level = 0) {
    this.bounds = bounds;
    this.maxObjects = maxObjects;
    this.maxLevels = maxLevels;
    this.level = level;
    this.objects = [];
    this.nodes = [];
  }
  
  split() {
    const nextLevel = this.level + 1;
    const subWidth = this.bounds.width / 2;
    const subHeight = this.bounds.height / 2;
    const x = this.bounds.x;
    const y = this.bounds.y;
    
    this.nodes[0] = new Quadtree(
      { x, y, width: subWidth, height: subHeight },
      this.maxObjects, this.maxLevels, nextLevel
    );
    this.nodes[1] = new Quadtree(
      { x: x + subWidth, y, width: subWidth, height: subHeight },
      this.maxObjects, this.maxLevels, nextLevel
    );
    this.nodes[2] = new Quadtree(
      { x, y: y + subHeight, width: subWidth, height: subHeight },
      this.maxObjects, this.maxLevels, nextLevel
    );
    this.nodes[3] = new Quadtree(
      { x: x + subWidth, y: y + subHeight, width: subWidth, height: subHeight },
      this.maxObjects, this.maxLevels, nextLevel
    );
  }
  
  getIndex(rect) {
    const midX = this.bounds.x + this.bounds.width / 2;
    const midY = this.bounds.y + this.bounds.height / 2;
    
    const inTop = rect.y < midY && rect.y + rect.height < midY;
    const inBottom = rect.y > midY;
    const inLeft = rect.x < midX && rect.x + rect.width < midX;
    const inRight = rect.x > midX;
    
    if (inTop && inLeft) return 0;
    if (inTop && inRight) return 1;
    if (inBottom && inLeft) return 2;
    if (inBottom && inRight) return 3;
    return -1;
  }
  
  insert(obj) {
    if (this.nodes.length > 0) {
      const index = this.getIndex(obj.bounds);
      if (index !== -1) {
        this.nodes[index].insert(obj);
        return;
      }
    }
    
    this.objects.push(obj);
    
    if (this.objects.length > this.maxObjects && this.level < this.maxLevels) {
      if (this.nodes.length === 0) this.split();
      
      for (let i = this.objects.length - 1; i >= 0; i--) {
        const index = this.getIndex(this.objects[i].bounds);
        if (index !== -1) {
          this.nodes[index].insert(this.objects[i]);
          this.objects.splice(i, 1);
        }
      }
    }
  }
  
  retrieve(viewport, result = []) {
    for (const obj of this.objects) {
      if (this.intersects(obj.bounds, viewport)) {
        result.push(obj);
      }
    }
    
    for (const node of this.nodes) {
      if (this.intersects(node.bounds, viewport)) {
        node.retrieve(viewport, result);
      }
    }
    
    return result;
  }
  
  intersects(rect1, rect2) {
    return !(rect1.x + rect1.width < rect2.x ||
             rect2.x + rect2.width < rect1.x ||
             rect1.y + rect1.height < rect2.y ||
             rect2.y + rect2.height < rect1.y);
  }
}
```

**Usage for Culling**:
```javascript
render(timestamp) {
  const rect = this.canvas.getBoundingClientRect();
  const logicalWidth = rect.width;
  const logicalHeight = rect.height;
  
  const viewport = {
    x: -this.pan.x,
    y: -this.pan.y,
    width: logicalWidth / this.zoom,
    height: logicalHeight / this.zoom
  };
  
  const visibleObjects = this.quadtree.retrieve(viewport);
  
  this.ctx.save();
  for (const obj of visibleObjects) {
    obj.render(this.ctx);
  }
  this.ctx.restore();
}
```

**Performance Characteristics**:
- Without culling (1000 objects, 5% visible): 19 objects rendered, 981 wasted
- With Quadtree: 50 objects queried, ~25 rendered
- Speedup: 10-40x depending on zoom level

**Trade-offs**:
- Build overhead: ~10ms for 10,000 objects
- Query time: O(log n) vs O(n)
- Memory: ~30% additional per object
- Only effective at extreme zoom or massive counts

---

### 3. Tile-Based Rendering: Asynchronous tile rendering

**Why implement**: For very large canvases (10000x10000px+), rendering everything each frame is slow.

**Implementation**:
```javascript
class TileBasedRenderer {
  constructor(tileSize = 256, canvas, ctx) {
    this.tileSize = tileSize;
    this.canvas = canvas;
    this.ctx = ctx;
    this.tiles = new Map();
    this.tilesToRender = [];
  }
  
  getVisibleTiles(viewport, zoom) {
    const tiles = [];
    const startCol = Math.floor(viewport.x / this.tileSize);
    const startRow = Math.floor(viewport.y / this.tileSize);
    const endCol = Math.ceil((viewport.x + viewport.width) / this.tileSize);
    const endRow = Math.ceil((viewport.y + viewport.height) / this.tileSize);
    
    for (let row = startRow; row < endRow; row++) {
      for (let col = startCol; col < endCol; col++) {
        tiles.push({ row, col });
      }
    }
    
    return tiles;
  }
  
  async renderTiles(viewport, zoom, layers) {
    this.tilesToRender = this.getVisibleTiles(viewport, zoom);
    
    // Sort by distance from center
    this.tilesToRender.sort((a, b) => {
      const centerX = viewport.x + viewport.width / 2;
      const centerY = viewport.y + viewport.height / 2;
      const aDist = Math.pow(a.col * this.tileSize - centerX, 2) + 
                    Math.pow(a.row * this.tileSize - centerY, 2);
      const bDist = Math.pow(b.col * this.tileSize - centerX, 2) + 
                    Math.pow(b.row * this.tileSize - centerY, 2);
      return aDist - bDist;
    });
    
    for (const tile of this.tilesToRender) {
      await this.renderTile(tile, zoom, layers);
      
      // Yield to browser every 16ms
      await new Promise(resolve => setTimeout(resolve, 0));
    }
  }
  
  async renderTile(tile, zoom, layers) {
    const key = `${tile.col},${tile.row}`;
    
    if (this.tiles.has(key)) return;
    
    const tileCanvas = document.createElement('canvas');
    tileCanvas.width = this.tileSize;
    tileCanvas.height = this.tileSize;
    const tileCtx = tileCanvas.getContext('2d');
    
    const tileX = tile.col * this.tileSize;
    const tileY = tile.row * this.tileSize;
    
    tileCtx.save();
    tileCtx.translate(-tileX, -tileY);
    
    for (const layer of layers) {
      layer.render(tileCtx, { 
        x: tileX, y: tileY, 
        width: this.tileSize, 
        height: this.tileSize 
      });
    }
    
    tileCtx.restore();
    this.tiles.set(key, tileCanvas);
  }
  
  compositeTiles(viewport) {
    const tiles = this.getVisibleTiles(viewport, 1);
    
    for (const tile of tiles) {
      const key = `${tile.col},${tile.row}`;
      const cachedTile = this.tiles.get(key);
      
      if (cachedTile) {
        const x = tile.col * this.tileSize;
        const y = tile.row * this.tileSize;
        this.ctx.drawImage(cachedTile, x, y);
      }
    }
  }
}
```

**Performance Characteristics**:
- 10000x10000px canvas: Full render ~500ms, tile-based ~50ms per frame
- Memory: Caches only visible tiles, ~5MB for 10000x10000 at 256px tiles
- Latency: Progressive rendering shows partial results quickly

**Trade-offs**:
- Complexity: Significantly more code
- Tile seams: Need anti-aliasing at boundaries
- Cache invalidation: Detect when tiles change
- Best for: Very large static content

---

### 4. Worker Rendering: OffscreenCanvas with Web Workers

**Why implement**: Move heavy rendering to background threads, keep main thread responsive.

**Main Thread**:
```javascript
class WorkerRenderer {
  constructor(numWorkers = 4) {
    this.workers = Array(numWorkers).fill(null).map(() => 
      new Worker('renderer-worker.js')
    );
    this.currentWorker = 0;
    this.pending = new Map();
    this.taskId = 0;
    
    this.workers.forEach(worker => {
      worker.onmessage = (e) => {
        const { id, imageData } = e.data;
        const resolve = this.pending.get(id);
        if (resolve) {
          resolve(imageData);
          this.pending.delete(id);
        }
      };
    });
  }
  
  async renderTile(tileData, layers) {
    const id = this.taskId++;
    const worker = this.workers[this.currentWorker];
    this.currentWorker = (this.currentWorker + 1) % this.workers.length;
    
    return new Promise(resolve => {
      this.pending.set(id, resolve);
      worker.postMessage({
        id,
        tileData,
        layers: layers.map(l => l.serialize())
      });
    });
  }
}
```

**Worker Thread**:
```javascript
self.onmessage = (e) => {
  const { id, tileData, layers } = e.data;
  
  const canvas = new OffscreenCanvas(tileData.width, tileData.height);
  const ctx = canvas.getContext('2d');
  
  for (const layer of layers) {
    renderLayer(ctx, layer);
  }
  
  canvas.convertToBlob().then(blob => {
    createImageBitmap(blob).then(bitmap => {
      self.postMessage({ id, imageData: bitmap });
    });
  });
};
```

**Performance**:
- Main thread: Free to handle input (smooth 60fps)
- Worker threads: Render 4 tiles in parallel
- Complex scenes: 2-4x speedup with 4 workers
- Latency: One frame delay (acceptable)

---

### 5. Layer Caching: Cache rendered layers as images

**Why implement**: If a layer doesn't change, rendering it again wastes GPU time.

**Implementation**:
```javascript
class CachedLayer {
  constructor(layer) {
    this.layer = layer;
    this.cache = null;
    this.isDirty = true;
  }
  
  markDirty() {
    this.isDirty = true;
  }
  
  render(ctx, bounds) {
    if (this.isDirty || !this.cache) {
      this.updateCache(bounds);
      this.isDirty = false;
    }
    
    if (this.cache) {
      ctx.drawImage(this.cache, bounds.x, bounds.y);
    }
  }
  
  updateCache(bounds) {
    const layerCanvas = document.createElement('canvas');
    layerCanvas.width = bounds.width;
    layerCanvas.height = bounds.height;
    const layerCtx = layerCanvas.getContext('2d');
    
    layerCtx.save();
    layerCtx.translate(-bounds.x, -bounds.y);
    this.layer.render(layerCtx);
    layerCtx.restore();
    
    this.cache = layerCanvas;
  }
}
```

**Performance**:
- First frame: Render layer + cache (expensive)
- Subsequent frames: Just drawImage (10-100x faster)
- Best for: Static layers that don't animate
- Memory: Cache size = layer size (~8MB per large layer)

---

### 6. RequestAnimationFrame: Already Optimal

Current implementation is already optimal. RAF automatically throttles to screen refresh rate.

---

### 7. Viewport Culling: Render only visible objects

**Why implement**: Objects outside viewport waste rendering time.

**Implementation**:
```javascript
class ViewportCuller {
  calculateViewport(zoom, pan, width, height) {
    return {
      x: -pan.x,
      y: -pan.y,
      width: width / zoom,
      height: height / zoom
    };
  }
  
  isVisible(bounds, viewport) {
    return !(bounds.x + bounds.width < viewport.x ||
             viewport.x + viewport.width < bounds.x ||
             bounds.y + bounds.height < viewport.y ||
             viewport.y + viewport.height < bounds.y);
  }
  
  cullObjects(objects, viewport) {
    return objects.filter(obj => this.isVisible(obj.bounds, viewport));
  }
}
```

**Usage**:
```javascript
render(timestamp) {
  const viewport = {
    x: -this.pan.x,
    y: -this.pan.y,
    width: logicalWidth / this.zoom,
    height: logicalHeight / this.zoom
  };
  
  const visibleObjects = this.culler.cullObjects(this.objects, viewport);
  
  for (const obj of visibleObjects) {
    obj.render(this.ctx);
  }
}
```

**Performance**:
- Without culling (1000 objects, 10% visible): 10x slowdown
- With culling: 1x speed (only visible rendered)
- Speedup: 10x

---

## Optimization Decision Matrix

```
Optimization          | Complexity | Speedup | Breakeven
─────────────────────────────────────────────────────────────
RAF throttling        | None       | Auto    | Always
GPU acceleration      | Low        | 10-50x  | Always
DPI caching           | None       | Auto    | Always
Context state mgmt    | Low        | 2-5x    | 100+ objects
Transform matrix      | None       | Auto    | Always
─────────────────────────────────────────────────────────────
Dirty rectangles      | High       | 5-99x   | 200+ objects
Spatial indexing      | High       | 10-40x  | 1000+ objects
Tile-based rendering  | Very High  | 10x     | 10000x10000+ canvas
Worker rendering      | Very High  | 2-4x    | Heavy per-frame work
Layer caching         | Medium     | 10-100x | Static layers
Viewport culling      | Medium     | 5-10x   | 500+ objects
```

---

## Real-World Performance Tuning Strategy

### 1. Establish Baseline
```javascript
class PerformanceMonitor {
  constructor() {
    this.measurements = [];
  }
  
  mark(name) {
    performance.mark(name);
  }
  
  measure(name, startMark, endMark) {
    performance.measure(name, startMark, endMark);
    const measure = performance.getEntriesByName(name)[0];
    this.measurements.push({ name, duration: measure.duration });
  }
  
  report() {
    for (const m of this.measurements) {
      console.log(`${m.name}: ${m.duration.toFixed(2)}ms`);
    }
  }
}
```

### 2. Measure Each Component
```javascript
render(timestamp) {
  const perf = this.perfMonitor;
  
  perf.mark('render-start');
  
  perf.mark('update-state-start');
  this.updateState(timestamp);
  perf.measure('update-state', 'update-state-start');
  
  perf.mark('render-layers-start');
  this.renderLayers();
  perf.measure('render-layers', 'render-layers-start');
  
  perf.mark('render-end');
  perf.measure('total-render', 'render-start', 'render-end');
  
  if (timestamp % 60 === 0) {
    perf.report();
  }
}
```

### 3. Apply Optimizations Systematically
1. Always apply: RAF, GPU, transforms, DPI caching
2. Profile with DevTools to find bottlenecks
3. Apply targeted optimization for bottleneck
4. Re-profile to verify improvement
5. Stop at diminishing returns (usually 1-2% gain)

### 4. Production Monitoring
```javascript
class ProductionMetrics {
  recordFrameTime(duration) {
    // Send to analytics
    navigator.sendBeacon('/metrics', JSON.stringify({
      timestamp: Date.now(),
      frameDuration: duration,
      fps: 1000 / duration
    }));
  }
}
```

---

## Summary

The most impactful optimizations are:
1. **GPU acceleration** (automatic): 10-50x speedup
2. **Transformation matrix** (automatic): 10-20x speedup
3. **Viewport culling**: 5-10x speedup for 500+ objects
4. **Spatial indexing**: 10-40x speedup for extreme zoom
5. **Dirty rectangles**: 5-99x speedup (complex scenes)

Start with automatic optimizations, profile, then apply targeted optimizations based on specific bottlenecks.

