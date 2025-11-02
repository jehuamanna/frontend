# Frontend System Design Problems - Categorized Reference

**Total: 100 Problems organized into 8 categories**

This document categorizes 100 advanced frontend system design problems suitable for Principal/Staff-level engineering interviews.

---

## Category 1: Performance & Optimization (18 problems)

Problems focused on rendering performance, memory efficiency, layout optimization, and achieving 60fps interactions.

### 1. Virtualized Infinite List with Dynamic Heights
Build a memory-efficient list that renders millions of items with variable heights, smooth 60fps scrolling, and O(log n) index lookups using Fenwick trees.

**Topics**: Windowing, ResizeObserver, prefix-sum trees, layout thrashing prevention

### 7. Browser Layout Engine Optimization — Minimize Reflows
Diagnose and fix layout thrashing, achieve 60fps on scroll/resize. Batch DOM operations, use `will-change`, and measure with Performance profiler.

**Topics**: Forced synchronous layout, batching, compositing, paint pipeline

### 17. Tiny Animations Engine with Motion Planning
Animation engine supporting 1000+ simultaneous transitions at 60fps using GPU compositing, RAF scheduling, and object pooling.

**Topics**: requestAnimationFrame, CSS transforms, Web Animations API, interruption semantics

### 19. High-fidelity Pixel-Perfect Zoomable Canvas
Zoomable canvas with billions-of-pixels virtual space, tiled rendering, progressive LOD, and vector object editing.

**Topics**: Canvas/SVG/WebGL tradeoffs, spatial indexing (quadtrees), tile streaming

### 39. High-volume Real-time Charts with Backfill
Render tens of thousands of streaming points per second with pause/backfill, zooming, and downsampling.

**Topics**: WebGL/Canvas, downsampling (LTTB), decimation, time-series buffering

### 62. Client-side Search Index for Rich Content
Full-text search for 100k+ DOM nodes with stemming, stopwords, incremental updates, and highlighting.

**Topics**: Inverted indexes, tokenization, web workers, memory optimization

### 63. Predictive Layout Prefetcher
Predict which elements will enter viewport and precompute layout/styles to reduce jank.

**Topics**: IntersectionObserver, speculative rendering, layout pipeline

### 70. DOM-based Spreadsheet Renderer (Excel clone)
Render 1M+ cells efficiently with frozen rows/columns, scrolling, formulas, and selections.

**Topics**: Virtualization, canvas vs DOM tradeoffs, dependency graphs

### 71. Performance Budget Enforcer in CI
CI tool that blocks builds if bundle size/CLS/LCP exceed budget with auto-generated reports.

**Topics**: CI/CD, Lighthouse API, thresholds, metrics pipelines

### 72. Precise Input Latency Profiler
Measure input-to-paint latency per component and visualize bottlenecks.

**Topics**: PerformanceObserver, event timing API, paint timing, flamecharts

### 80. DOM Layout Stress Simulator
Generate pathological DOM layouts (deep nesting, massive reflows) and measure browser regressions.

**Topics**: Benchmark harnesses, DOM APIs, layout thrash detection

### 81. Incremental Static DOM Rehydration
Rehydrate server-rendered DOM progressively, prioritizing visible elements.

**Topics**: SSR hydration, priority queues, idle tasks, streaming

### 90. Tiny Deterministic Scheduler for Heavy DOM Work
Cooperative scheduler that slices large DOM tasks into micro-jobs while keeping UI responsive.

**Topics**: Task slicing, cooperative scheduling, Jest-friendly determinism

### 93. High-performance DOM Merging for Microfrontends
DOM-merge protocol for independently-deployed microfrontends to coexist without conflicts.

**Topics**: Namespacing, CSS isolation, event containment, lifecycle contracts

### 98. Component-level Performance SLA Enforcement
Monitor component render times in production and trigger fallbacks when exceeding SLAs.

**Topics**: Performance marks/measures, feature-flagged degradation, observability

### 99. Progressive Hydration with Interaction Tracing
Hydrate components in priority order based on actual user interactions from server-rendered markup.

**Topics**: Interaction tracing, priority queue hydration, idle-time scheduling

### 100. Low-latency Image Editing Pipeline in Browser
In-browser editor with nondestructive edits, undo history, and GPU-accelerated filters.

**Topics**: WebGL/OffscreenCanvas, layer compositing, history/delta storage

### 52. Latency-adaptive UI Throttle
Scheduler that adapts UI update frequency based on measured input-to-display latency.

**Topics**: Latency measurement, adaptive algorithms, rAF cadence

---

## Category 2: Accessibility (9 problems)

Problems focused on ARIA, keyboard navigation, screen readers, and inclusive design.

### 2. Accessible, Keyboard-navigable Date Range Picker
Full keyboard navigation (arrows, PgUp/PgDn), ARIA roles, screen reader announcements, localization.

**Topics**: WAI-ARIA, roving tabindex, Intl.DateTimeFormat, focus management

### 11. High-performance Drag & Drop with Accessibility
Drag-drop for thousands of items with keyboard reordering, multi-select, and accessible announcements.

**Topics**: Pointer Events, aria-dropeffect/aria-grabbed, virtualization

### 34. Large-scale Accessibility Audit Automation
Programmatic SPA inspection beyond basic rules (focus order, landmarks, semantics) with prioritized fixes.

**Topics**: aXe rules, programmatic focus analysis, heuristic scoring

### 42. Universal Focus Management for Modal/Drawer System
Manage focus trapping, restore, stacking, nested modals across Shadow DOM and iframes.

**Topics**: Focus management, inert, tabindex, aria-hidden, portal focus

### 45. High-performance Accessibility Tree Sync
Efficiently update accessibility tree for virtualized UI without O(n) updates.

**Topics**: Accessibility tree model, ARIA, batching updates, role mappings

### 51. Composable ARIA Widgets Library (low-level primitives)
Accessible, composable primitives (roving focus, combobox, tree, grid) with tiny runtime.

**Topics**: WAI-ARIA patterns, keyboard models, semantics-first APIs

### 66. Optimized Accessibility Announcer Queue
Live-region announcer that batches and prioritizes screen reader messages.

**Topics**: ARIA live regions, debouncing, priority queues, UX heuristics

### 78. Accessibility-First Rich Chart Component
Accessible chart with full keyboard navigation, screen reader narration, zoom/pan controls.

**Topics**: SVG, ARIA roles for charts, focus rings, screen reader UX

### 92. Accessibility-aware Image Annotation Tool
Image annotation with alt-text suggestions and semantic labels for assistive tech.

**Topics**: Region mapping, alt-text heuristics, accessibility metadata

---

## Category 3: Security (10 problems)

Problems focused on XSS prevention, CSP, sandboxing, authentication, and secure data handling.

### 8. Secure HTML Sanitizer with CSP-aware Output
Sanitize arbitrary HTML to prevent XSS while preserving safe markup. Allowlist tags/attributes, rewrite for CSP.

**Topics**: XSS mitigation, CSP nonces/hashes, DOMParser, URL parsing

### 21. Hierarchical Permission System in Client UI
Client-side permission system with feature flags, role-based UI, remote policy updates.

**Topics**: Capability-based security, policy caches, encryption for sensitive flags

### 32. Cross-origin Embedding & Secure Communication Layer
Safely embed third-party widgets with controlled capabilities and message passing.

**Topics**: iframe sandbox, postMessage origin/security, proxy capabilities

### 46. Inline Code Execution Sandbox for Educational App
Secure in-browser sandbox for running JS/TS snippets with resource/time limits.

**Topics**: iframe sandboxing, WebAssembly isolation, worker timeouts

### 49. End-to-end Encrypted Sync of User Settings
Encrypt user settings before syncing so server never sees plaintext. Key rotation and multi-device sync.

**Topics**: WebCrypto API, key management, conflict resolution, secure backups

### 64. Sandbox for Untrusted Widgets with CSS Isolation
Framework for third-party widgets that can't break global styles or leak information.

**Topics**: Shadow DOM, iframe sandbox, CSS scoping, CSP

### 68. Multi-origin Authentication in SPAs
Frontend auth manager handling multiple origins (iframe-embedded apps) with token refresh and logout sync.

**Topics**: postMessage, SameSite cookies, CORS, OAuth 2.0

### 73. Secure Drag-drop Across Origins
Drag-drop where source/target may be different origins, with no data leaks.

**Topics**: HTML5 drag-drop, DataTransfer security, origin isolation

### 83. Client-only Secure Secret Manager
Client-side secret storage (API keys) with encryption-at-rest and no server exposure.

**Topics**: WebCrypto, localStorage/IndexedDB encryption, key rotation

### 89. Secure WebAuthn Multi-factor Flow
Frontend flow orchestrating password + WebAuthn device registration with fallback.

**Topics**: WebAuthn API, credential management, attestation, UX fallbacks

---

## Category 4: Architecture & Design Patterns (14 problems)

Problems focused on system architecture, component patterns, state management, and code organization.

### 3. DOM Diffing Engine (mini React reconcile)
Diffing/reconciliation engine with keyed list reconciliation, functional components, minimal DOM operations.

**Topics**: Virtual DOM, keyed reconciliation, lifecycle, batched updates

### 4. Event Delegation System & Custom Event Propagation
Custom event system with delegated handlers, CSS-selector matching, namespaces, and priority.

**Topics**: Event propagation, composedPath(), selector matching, MutationObserver

### 10. Pluggable Plugin System for UI Framework
Plugin architecture with registration, lifecycle hooks, fault isolation, and hot-pluggable loading.

**Topics**: Module systems, dynamic import, iframe sandboxing, versioning

### 20. Runtime Type Validation & Prop Contracts
Runtime type-checking for components with shape diffs and minimal, actionable errors.

**Topics**: Structural typing, JSON schema, babel plugin integration

### 27. Deterministic Replay Tool for UI Bugs
Recorder/replayer capturing user events and DOM mutations to reproduce bugs.

**Topics**: Event serialization, MutationObserver, snapshot checkpoints

### 28. Component Graph Hot-reload w/o State Loss
Hot-reload that swaps component implementations while preserving local state and DOM.

**Topics**: Module hot-swapping, stable instance identity, state serialization

### 38. Zero-downtime Frontend Migration Strategy
Rollout system for migrating to new framework incrementally with no downtime and rollback.

**Topics**: Feature flags, routing, module federation, incremental hydration

### 41. Reactive Formulas Engine (spreadsheet-like)
Reactive engine where cells contain formulas, with cycle detection and dependency graph.

**Topics**: Topological sort, incremental recomputation, cycle detection

### 44. Efficient DOM Snapshot & Diff for Time Travel Debugging
Serialized DOM + JS state snapshots for fast time-travel diffs.

**Topics**: Serialization, incremental checkpoints, compression, sanitization

### 65. State-machine Driven UI Workflow Engine
Model complex UI flows (multi-step forms, wizards) as explicit state machines.

**Topics**: Statecharts, persistence, serialization, guard conditions

### 69. Declarative Undo/Redo History for Any Component
Global undo/redo manager where components register atomic actions.

**Topics**: Command pattern, immutability, action logs, snapshots

### 85. Component Error Boundary System
Reusable error boundary system for vanilla JS components with fallbacks.

**Topics**: window.onerror, unhandledrejection, component lifecycle

### 95. Structured Content Editor with Plugin API
Document editor for nested content with plugin system for block types and validation.

**Topics**: Block model, schema validation, plugin lifecycle, collaborative hooks

### 37. Deterministic CSS Cascade Visualizer
Show exact origin, specificity, and cascade order of every computed style.

**Topics**: CSS cascade, specificity, computed style internals, Shadow DOM

---

## Category 5: Browser APIs & Internals (19 problems)

Problems requiring deep knowledge of browser APIs, DOM manipulation, and platform capabilities.

### 5. Diagnosing and Fixing Memory Leaks in a SPA
Find and fix memory leaks using Chrome DevTools, identify detached DOM nodes and listener leaks.

**Topics**: Heap profiler, closures, detached DOM, WeakMap/WeakRef

### 6. ContentEditable Rich-Text Editor: Undo/Redo & Cursor Preservation
Rich text editor with robust undo/redo preserving cursor/selection across DOM changes.

**Topics**: Selection/Range APIs, caret positioning, operational transforms

### 9. Cross-window / WebWorker Shared State with Low-latency Updates
Synchronize state between main thread, iframes, and Web Worker with eventual consistency.

**Topics**: postMessage, BroadcastChannel, SharedArrayBuffer, IndexedDB

### 15. Advanced Input Masking & Validation Library
Input masking for phone numbers, credit cards that preserves cursor and works with IME.

**Topics**: Composition events, Selection API, Unicode normalization

### 22. Browser-native PDF Viewer with Annotations
In-browser PDF viewer with panning, zooming, text selection, and persistent annotations.

**Topics**: PDF.js, coordinate mapping, text layer mapping, storage sync

### 23. Precise Time/Alarm Scheduler in Web (multi-tab)
Scheduling API that fires callbacks at precise times across tabs with leader election.

**Topics**: BroadcastChannel, leader election, Visibility API, timer clamping

### 24. Custom Layout Engine (Constraint-based)
Constraint-based layout engine (like Auto Layout) that solves constraints efficiently.

**Topics**: Cassowary solver, constraint propagation, performance engineering

### 29. Multi-language Right-to-left Layout Engine
UI layout supporting mixed LTR/RTL content with bidi reordering and mirrored icons.

**Topics**: Unicode Bidirectional Algorithm, CSS direction, mirroring

### 33. Declarative Gesture Recognition Library
Gesture recognition for pinch/rotate/complex gestures across touch/mouse/pen.

**Topics**: Pointer Events, gesture state machines, hit testing, passive listeners

### 48. Adaptive Input Pipeline for IME-heavy Languages
Controls behaving correctly across composition sequences (IME) and mobile keyboards.

**Topics**: Composition events, input event ordering, caret handling

### 61. DOM Snapshot Compression for Error Reporting
Capture DOM snapshots on error using structural hashing and compression.

**Topics**: MutationObserver, DOM serialization, compression, privacy filters

### 67. Font Loading & FOUT/FOIT Mitigation
Font loader avoiding flashes of invisible text while balancing layout shifts.

**Topics**: Font Loading API, fallback stacks, layout stability

### 75. Streaming Form Data Validator
Validate form fields in real-time using streaming server responses.

**Topics**: Streams API, async validation, debounce, AbortController

### 82. DOM Virtual Filesystem Explorer
Filesystem tree with millions of files/folders, lazy-load, search/filter, keyboard nav.

**Topics**: Virtualization, async loading, keyboard UX, tree widgets

### 86. Deterministic Cross-browser Rendering Diff Tool
Load page in multiple browsers and highlight pixel/layout diffs with CSS/HTML/JS blame.

**Topics**: Screenshot diffing, CSSOM differences, cross-browser quirks

### 91. Adaptive Layouts for Foldable / Multi-screen Devices
UI components adapting to hinge/fold states and multi-screen layouts.

**Topics**: CSS viewport segments API, window segments, fold-aware UX

### 96. Cross-platform Native-like Tactile Feedback Layer
Abstract haptic & audio feedback layer mapping UI actions to device sensations.

**Topics**: Vibration API, platform capability detection, fallbacks

### 54. Dynamic Accessibility Role Inference Engine
Infer missing semantics for legacy markup and auto-inject ARIA safely.

**Topics**: Heuristics, ML-assisted suggestions, false positives mitigation

### 87. Resource-aware Image CDN Client
Client-side image selection based on DPR, viewport, user motion preference, and quota.

**Topics**: srcset/sizes auto-generation, DPR handling, save-data

---

## Category 6: Data Synchronization & Offline (6 problems)

Problems focused on offline-first architecture, conflict resolution, multi-tab sync, and data persistence.

### 13. Robust Offline-first Sync with Conflict Resolution
Offline-first data layer for todo app with optimistic UI and CRDT-based conflict resolution.

**Topics**: Service Worker, Background Sync, IndexedDB, CRDTs, retries

### 16. Secure File Upload Widget with Chunking & Resume
Large file uploader with chunking, resume support, progress across tabs, client-side hashing.

**Topics**: fetch streaming, Service Worker, BroadcastChannel, tus protocol

### 30. Event Storming Resilience — Backpressure & Sampling
Client-side telemetry pipeline with sampling/backpressure, offline persistence, bounded memory.

**Topics**: Token bucket, batching, IndexedDB, privacy-aware sampling

### 74. DOM-based Collaborative Whiteboard
Collaborative whiteboard with strokes syncing in real time using CRDTs for vector graphics.

**Topics**: Canvas/SVG, WebRTC/WebSocket, CRDT, delta compression

### 77. Deterministic Multi-tab State Sync with Leader Election
Keep app state consistent across tabs, elect leader for expensive operations.

**Topics**: BroadcastChannel, leader election algorithms, storage events

### 79. Multi-stage Progressive Web App Bootstrapping
PWA startup flow: shell → skeleton UI → cached content → live content.

**Topics**: App shell model, hydration, SW caching, skeleton screens

---

## Category 7: Advanced UI Components & Rendering (24 problems)

Problems focused on complex interactive components, rendering techniques, and visual effects.

### 12. Predictive Pre-rendering / Speculative Fetching Layer
Speculative loader that prefetches resources based on user behavior predictions.

**Topics**: link rel=prefetch/preload, navigator.connection, rate-limiting

### 14. Fine-grained CSS-in-JS Engine
CSS-in-JS engine with atomic classes, SSR/hydration, deduplication, minimal runtime.

**Topics**: CSSOM, SSR hydration tokens, specificity, critical CSS

### 18. Large-scale Form Engine with Conditional Logic & Autosave
Form engine rendering from JSON schema with conditional fields and autosave.

**Topics**: JSON Schema, validation, debounce, optimistic UI, IndexedDB

### 25. Progressive Image Loading with Perceptual Metrics
Progressive loading selecting quality based on viewport, network, and saliency.

**Topics**: IntersectionObserver, saliency heuristics, LQIP, responsive images

### 26. Shadow DOM + CSS Isolation Framework
UI component system using Shadow DOM with theme propagation and cross-shadow styling.

**Topics**: Shadow DOM, ::part/::slotted, CSS custom properties

### 31. Fast Diff/Highlight Changes for Code Editor
Diff algorithm for large documents (100k+ lines) with incremental updates.

**Topics**: Myers diff, patience diff, suffix arrays, chunking

### 36. Composable Gesture-driven Canvas Editor
Vector editor composing gestures into commands with undo/redo and precise hit-testing.

**Topics**: Pointer events, transform math, spatial indexing, command pattern

### 40. Privacy-preserving Analytics SDK
Analytics SDK with differential-privacy guarantees and on-device aggregation.

**Topics**: Differential privacy, aggregation, batching, privacy budgets

### 43. Pluggable Theming System with A/Bable Runtime
Runtime theming with CSS variables, on-the-fly switching, and A/B experiment hooks.

**Topics**: CSS custom properties, SSR theme hydration, feature flags

### 50. Composable Animation Keyframe Compiler
Compiler taking motion specs and outputting performant CSS/Web Animations API usage.

**Topics**: Web Animations API, easing curves, GPU properties

### 53. Universal Input Abstraction for Game-like UIs
Input layer standardizing mouse/keyboard/touch/gamepad/VR with mapping and rebinding.

**Topics**: Gamepad API, pointer capture, input event normalization

### 55. Composable Streaming Parser for Large HTML Documents
Streaming HTML parser progressively rendering huge streams without full DOM materialization.

**Topics**: Streaming parsing, incremental rendering, backpressure

### 56. Predictive Form Autofill with Privacy Controls
Smart autofill predicting form intent, handling conditional fields, respecting privacy.

**Topics**: Heuristics, privacy-by-default, input heuristics, secure storage

### 58. High-throughput Clipboard Manager for Complex Data
Clipboard manager supporting multiple formats, incremental paste previews, security.

**Topics**: Clipboard API, MIME types, paste sanitization, async clipboard

### 59. Graphical Diff & Merge UI for Structured Docs
Visual diff/merge tool for nested JSON/DOM-like documents with conflict resolution UI.

**Topics**: Tree-diffing, merge algorithms, UX for conflicts, CRDT vs OT

### 76. Dynamic CSS Container Queries Polyfill
Container query polyfill that re-renders elements when containers resize.

**Topics**: ResizeObserver, mutation batching, layout dependencies

### 88. Declarative Reactive Transitions Language
DSL describing transitions between UI states, compiled into efficient runtime code.

**Topics**: Parser/compiler, animation scheduling, Web Animations API

### 94. Continuous Interaction Recorder for UX Research
Privacy-aware recorder logging interactions, timing, and state transitions for analysis.

**Topics**: Event sampling, privacy redaction, chunked uploads

### 97. Efficient Multi-lingual Runtime Intl Loader
Load and switch i18n locale data at runtime with minimal bundle cost.

**Topics**: Chunked locale data, ICU message handling, pluralization

### 35. Cross-browser Feature Detection & Polyfill Orchestration
Detect feature availability, lazy-load polyfills only when needed, ensure ordering.

**Topics**: Feature detection, dynamic import, performance & caching

### 84. Predictive Prefetch with ML Integration
Train on-device ML model to predict next navigation and prefetch assets.

**Topics**: TensorFlow.js, caching strategies, network info API

### 57. Large-scale DOM Mutation Stress Tester
Generate pathological DOM mutations to stress-test layout/GC and detect regressions.

**Topics**: MutationObserver, synthetic workloads, perf instrumentation

### 47. Safe Dynamic Script Loader with Dependency Graph
Runtime loading third-party scripts with dependencies, isolation, timeouts, retry.

**Topics**: dynamic import, script tags vs modules, CSP, error handling

### 60. Composable ARIA Widgets Library
Low-level accessible primitives that are composable and themeable.

**Topics**: WAI-ARIA patterns, keyboard models, test-driven accessibility

---

## Category 8: Developer Experience & Tooling (6 problems)

Problems focused on debugging, testing, monitoring, build tools, and development workflows.

### 35. Cross-browser Feature Detection & Polyfill Orchestration
System detecting features and lazy-loading polyfills with dependency management.

**Topics**: Feature detection patterns, dynamic import, CSP considerations

### 47. Safe Dynamic Script Loader with Dependency Graph
Load third-party scripts with declared dependencies, isolation, and graceful degradation.

**Topics**: dynamic import, script tags vs modules, error handling

### 57. Large-scale DOM Mutation Stress Tester
Harness generating pathological DOM mutations to stress-test and auto-detect regressions.

**Topics**: MutationObserver, synthetic workloads, stability metrics

### 71. Performance Budget Enforcer in CI
CI tool running Lighthouse/DevTools audits, blocking builds on budget violations.

**Topics**: CI/CD, Lighthouse API, thresholds, metrics pipelines

### 72. Precise Input Latency Profiler
Profiler measuring input-to-paint latency per component with visualization.

**Topics**: PerformanceObserver, event timing API, flamecharts

### 84. Predictive Prefetch with ML Integration
On-device ML model predicting next navigation for asset prefetching.

**Topics**: TensorFlow.js, caching strategies, privacy considerations

---

## Additional High-Value Problems (Bonus)

### 101. WebAssembly-based Virtual Scrolling Engine
Build ultra-high-performance list virtualization using WebAssembly for index calculations, supporting 10M+ items with sub-millisecond query times.

**Topics**: WASM, SharedArrayBuffer, Rust/C++ compilation, JS interop

### 102. Distributed Tracing for Frontend Performance
Implement OpenTelemetry-compatible tracing for frontend with automatic instrumentation, trace propagation, and sampling strategies.

**Topics**: OpenTelemetry, distributed tracing, RUM, sampling

### 103. CSS Grid Layout Engine from Scratch
Implement CSS Grid specification algorithm from scratch, handling auto-placement, spanning, and alignment.

**Topics**: CSS Grid spec, layout algorithms, constraint solving

### 104. Cross-framework Component Wrapper System
Create adapters allowing React components to work in Vue/Angular/Svelte and vice versa with proper lifecycle mapping.

**Topics**: Framework internals, component lifecycle, event systems

### 105. AI-powered Code Refactoring Assistant
Build browser-based tool using ASTs to suggest and apply safe refactorings with impact analysis.

**Topics**: AST parsing, Babel/TypeScript compiler, static analysis

---

## Problem Selection Guide

**For Performance-focused Interviews**: Problems 1, 7, 17, 19, 39, 70, 71, 72, 90, 98, 99, 100

**For Accessibility-focused Interviews**: Problems 2, 11, 34, 42, 45, 51, 66, 78, 92

**For Security-focused Interviews**: Problems 8, 21, 32, 46, 49, 68, 73, 83, 89

**For Architecture-focused Interviews**: Problems 3, 4, 10, 20, 27, 28, 38, 41, 65, 69, 85, 95

**For Full-stack Frontend Interviews**: Problems 5, 6, 13, 16, 18, 30, 49, 74, 77, 79

**For Framework Authors/Library Builders**: Problems 3, 4, 10, 14, 20, 26, 28, 37, 50, 85, 103, 104

**For Principal/Staff-level Candidates**: Any 3-4 problems from different categories showing breadth

---

## Study Plan by Difficulty

### Foundation (Weeks 1-2)
- Problems: 2, 4, 5, 8, 11, 15, 18
- Focus: Browser APIs, events, accessibility basics, security fundamentals

### Intermediate (Weeks 3-5)
- Problems: 1, 3, 6, 7, 13, 14, 16, 17
- Focus: Performance optimization, state sync, rendering techniques

### Advanced (Weeks 6-8)
- Problems: 9, 10, 19, 22, 23, 24, 27, 28, 38, 41
- Focus: Architecture, constraint solving, tooling, migration strategies

### Expert (Weeks 9-12)
- Problems: 20, 36, 40, 44, 46, 49, 70, 90, 93, 98, 99, 100
- Focus: Advanced patterns, distributed systems, security, performance SLAs

---

## Common Topics Across All Problems

### Must-Know Browser APIs
- DOM: `getComputedStyle`, `getBoundingClientRect`, `Range`, `Selection`, `MutationObserver`, `ResizeObserver`, `IntersectionObserver`
- Performance: `PerformanceObserver`, `requestAnimationFrame`, `requestIdleCallback`
- Storage: `IndexedDB`, `localStorage`, `Cache API`
- Workers: `Web Worker`, `Service Worker`, `SharedArrayBuffer`, `BroadcastChannel`
- Security: `CSP`, `postMessage`, `WebCrypto`, `iframe sandbox`

### Core Engineering Skills
- Data structures: Trees, prefix sums, Fenwick trees, LRU caches, spatial indexing
- Algorithms: Diffing, reconciliation, constraint solving, conflict resolution
- Performance: Layout/paint/composite pipeline, batching, debouncing, virtualization
- Accessibility: ARIA patterns, focus management, screen reader behavior
- Security: XSS classes, CSP, origin isolation, secure communication

### Architecture Patterns
- Event delegation, command pattern, observer pattern, state machines
- Plugin systems, hot-reload, feature flags, capability-based permissions
- Batched updates, microtask vs macrotask, cooperative scheduling
- CRDT, operational transforms, conflict resolution strategies
- SSR hydration, progressive enhancement, incremental loading

---

**Document Version**: 1.0
**Last Updated**: 2025-10-30
**Total Problems**: 105 (100 original + 5 bonus)

