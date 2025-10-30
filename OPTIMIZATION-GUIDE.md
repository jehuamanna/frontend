# Performance Optimization Guide - Quick Reference

## Executive Summary

This guide provides a complete framework for optimizing canvas rendering performance. For detailed implementations and explanations, see `PERFORMANCE-OPTIMIZATION-DEEP-DIVE.md`.

## Quick Start: Optimization Checklist

### Automatic Optimizations (Zero Configuration)
- [x] RequestAnimationFrame throttling: 60fps cap
- [x] GPU hardware acceleration via canvas context
- [x] 2D affine transformation matrix applied once per frame
- [x] DPI value cached at initialization
- [x] Context state managed with single save/restore

**Performance gain**: 10-50x automatically

### Manual Optimizations by Scenario

#### Scenario 1: 100-500 Objects
**Apply**: Context state batching + Viewport culling
```javascript
// Sort objects by fill color before rendering
const byColor = objects.reduce((acc, obj) => {
  if (!acc[obj.color]) acc[obj.color] = [];
  acc[obj.color].push(obj);
  return acc;
}, {});

for (const [color, group] of Object.entries(byColor)) {
  ctx.fillStyle = color;
  for (const obj of group) obj.render(ctx);
}
```

**Performance gain**: 2-5x speedup
**Implementation time**: 30 minutes

#### Scenario 2: 500-2000 Objects
**Apply**: Viewport culling + Context state batching
```javascript
// Calculate visible viewport
const viewport = {
  x: -this.pan.x,
  y: -this.pan.y,
  width: width / this.zoom,
  height: height / this.zoom
};

// Only render visible objects
const visible = objects.filter(obj => isInViewport(obj.bounds, viewport));
for (const obj of visible) obj.render(this.ctx);
```

**Performance gain**: 5-10x speedup
**Implementation time**: 1 hour

#### Scenario 3: 2000-10000 Objects
**Apply**: Spatial indexing (Quadtree) + Viewport culling
```javascript
// Query quadtree for visible objects
const visible = quadtree.retrieve(viewport);
for (const obj of visible) obj.render(ctx);
```

**Performance gain**: 10-40x speedup
**Implementation time**: 3-4 hours

#### Scenario 4: Very Large Canvas (10000x10000+)
**Apply**: Tile-based rendering + Layer caching
```javascript
// Render and cache tiles asynchronously
await tileRenderer.renderTiles(viewport, zoom, layers);

// Composite visible tiles
tileRenderer.compositeTiles(viewport);
```

**Performance gain**: 10-100x speedup (for large static content)
**Implementation time**: 6-8 hours

#### Scenario 5: Complex Per-Frame Operations
**Apply**: Web Worker rendering
```javascript
// Offload heavy rendering to workers
const bitmap = await workerRenderer.renderTile(data);
ctx.drawImage(bitmap, x, y);
```

**Performance gain**: 2-4x with multiple workers
**Implementation time**: 4-6 hours

#### Scenario 6: Mostly Static Layers
**Apply**: Layer caching
```javascript
// Cache rendered layers between frames
if (layer.isDirty) {
  layer.updateCache();
}
ctx.drawImage(layer.cache, layer.x, layer.y);
```

**Performance gain**: 10-100x for static layers
**Implementation time**: 2 hours

## Performance Profiling Guide

### Using Chrome DevTools

1. **Open Performance tab** (DevTools -> Performance)
2. **Record for ~5 seconds** while interacting with canvas
3. **Look for**:
   - Frame time (target: < 16ms for 60fps)
   - Long tasks (> 50ms)
   - Dropped frames (visible as red bars)

### Key Metrics to Monitor

```javascript
class PerformanceMonitor {
  recordFrame(duration) {
    if (duration > 16) {
      console.warn(`Dropped frame: ${duration.toFixed(1)}ms`);
    }
    
    // Track metrics
    this.frameTimes.push(duration);
    
    // Report every 60 frames (1 second at 60fps)
    if (this.frameTimes.length % 60 === 0) {
      const avg = this.frameTimes.reduce((a, b) => a + b) / this.frameTimes.length;
      const fps = 1000 / avg;
      console.log(`Average frame time: ${avg.toFixed(1)}ms (${fps.toFixed(0)} fps)`);
    }
  }
}
```

### Common Bottlenecks

| Symptom | Cause | Solution |
|---------|-------|----------|
| Frame time increases with zoom | Off-screen objects rendered | Add viewport culling |
| Smooth pan, jerky zoom | Blocking operations in render | Use RAF, avoid getImageData |
| Constant 60fps, then sudden drops | State management overhead | Batch save/restore calls |
| Poor performance on mobile | GPU acceleration disabled | Check context flags |
| Memory usage grows over time | Layer caches not cleared | Implement cache invalidation |
| Slow when panning | Many objects outside viewport | Implement spatial indexing |

## Implementation Order

### Phase 1: Foundation (Required)
1. GPU acceleration via context flags
2. Transformation matrix applied once
3. RequestAnimationFrame loop
4. Context state management

**Result**: 10-50x baseline speedup

### Phase 2: Light Optimization (Optional, < 1000 objects)
1. Context state batching by color
2. Viewport culling calculation

**Result**: 2-10x additional speedup

### Phase 3: Medium Optimization (1000-5000 objects)
1. Spatial indexing (Quadtree)
2. Advanced viewport culling
3. Dirty rectangle tracking

**Result**: 10-40x additional speedup

### Phase 4: Heavy Optimization (5000+ objects, large canvas)
1. Tile-based rendering
2. Worker rendering
3. Layer caching
4. Aggressive culling

**Result**: 10-100x additional speedup

## Performance Targets by Application Type

### Design Tools (Figma-like)
- Target: 60fps with 5000+ objects
- Optimizations: Quadtree + Viewport culling + Layer caching
- Estimated implementation: 8-10 hours

### Image Editors (Photoshop-like)
- Target: 60fps with 10000x10000 canvas
- Optimizations: Tile-based + Worker rendering + Layer caching
- Estimated implementation: 16-20 hours

### Collaborative Whiteboarding (Miro-like)
- Target: 60fps with 500+ objects, smooth realtime updates
- Optimizations: Viewport culling + State batching
- Estimated implementation: 4-6 hours

### CAD/Architecture Tools
- Target: 60fps with 50000+ objects at extreme zoom
- Optimizations: Quadtree + Spatial indexing + Dirty rectangles
- Estimated implementation: 12-16 hours

## Cost-Benefit Analysis

```
Optimization          | Dev Time | Performance Gain | ROI
─────────────────────────────────────────────────────────
GPU acceleration      | 0h       | 10-50x           | Infinite
Transform matrix      | 0h       | 10-20x           | Infinite
State batching        | 1h       | 2-5x             | Very High
Viewport culling      | 2h       | 5-10x            | Very High
Spatial indexing      | 4h       | 10-40x           | High
Dirty rectangles      | 6h       | 5-99x            | Medium
Tile-based rendering  | 8h       | 10-100x          | Medium
Worker rendering      | 6h       | 2-4x             | Low
Layer caching         | 2h       | 10-100x          | Very High
```

## When to Stop Optimizing

**Stop when**:
1. Frame time consistently < 16ms (60fps)
2. No dropped frames during normal interaction
3. Marginal gains < 5% for next optimization
4. Diminishing returns on effort invested

**Don't optimize**:
1. Code that's not a bottleneck (avoid premature optimization)
2. Features less than 10% of users experience
3. Cases where user doesn't notice the difference

## Testing Performance Changes

```javascript
// A/B test different optimizations
class PerformanceTest {
  async runTest(name, implementation, iterations = 1000) {
    const start = performance.now();
    for (let i = 0; i < iterations; i++) {
      implementation();
    }
    const end = performance.now();
    const avg = (end - start) / iterations;
    console.log(`${name}: ${avg.toFixed(3)}ms per operation`);
    return avg;
  }
}

// Example
const perf = new PerformanceTest();
const time1 = await perf.runTest('Without optimization', () => render());
const time2 = await perf.runTest('With optimization', () => renderOptimized());
console.log(`Speedup: ${(time1 / time2).toFixed(1)}x`);
```

## Production Monitoring

### Key Metrics to Track
- Average frame time
- 95th percentile frame time
- Dropped frames (> 16ms)
- Memory usage
- GPU utilization

### Recommended Monitoring Solution
```javascript
class ProductionMonitor {
  recordMetric(name, value) {
    // Send to analytics service
    analytics.track('canvas_metric', {
      metric: name,
      value: value,
      timestamp: Date.now(),
      userAgent: navigator.userAgent,
      viewport: window.innerWidth + 'x' + window.innerHeight
    });
  }
}
```

---

For detailed implementation guide, see: `PERFORMANCE-OPTIMIZATION-DEEP-DIVE.md`

