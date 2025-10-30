1. Virtualized Infinite List with Dynamic Heights
Problem statement
Implement a highly-performant, memory-efficient virtualized scrolling list component that can render millions of items. Items have variable heights (unknown until rendered). The component must support:

Smooth scrolling (no jank at 60fps target).

Windowing: only DOM nodes for visible items + small buffer are attached.

Jump to arbitrary index with correct scroll position.

Insertions/deletions at arbitrary positions while preserving scroll location.

Correct behavior when container is resized or font size changes.

Constraints & deliverables

API: new VirtualList(container, {getItem}) with getItem(index) returning a DOM node or render function.

Provide scrollToIndex(i) and updateItem(index, newData) methods.

Memory: DOM nodes O(viewportSize + buffer).

Time: updates / scrolling must avoid O(n) on every frame.

Provide tests or usage demo and explain complexity.

What to evaluate

Strategy for measuring unknown heights (e.g., binary search + cached heights, sentinel elements, progressive measurement).

How to maintain mapping index ↔ offset efficiently (segment tree / Fenwick / binary indexed tree / bucketed averages).

Techniques to avoid layout thrashing (read/write separation, requestAnimationFrame).

Handling inserting/removing items while preserving scroll offset (adjust offsets).

Rendering fallback for very dynamic heights.

Follow-ups

Support sticky headers.

Grouped lists and virtualization of groups.

Server-side rendering / hydration.

Topics to learn

Layout & reflow, forced synchronous layout, paint pipeline.

windowing / virtualization patterns.

Data structures: prefix-sum trees, Fenwick trees, segment trees.

requestAnimationFrame, IntersectionObserver, ResizeObserver.

Memory & GC patterns in browsers.

2. Build an Accessible, Keyboard-navigable Date Range Picker
Problem statement
Implement a reusable date-range picker UI (calendar popover) that:

Supports keyboard navigation (arrow keys, PgUp/PgDn, Home/End, Enter/Escape).

Is fully accessible (WAI-ARIA roles and announcements for screen readers).

Allows picking start & end date with clear focus behavior and visible focus ring.

Handles localization (first day of week, month names) and min/max dates.

Efficiently renders months (lazy render), and supports keyboard + mouse + touch.

Constraints & deliverables

Expose onChange callback with {start, end}.

Provide aria attributes, live region updates for selection changes.

Must not leak Global state; support multiple instances.

Provide tests for keyboard flows and accessibility.

What to evaluate

Semantic HTML & ARIA usage (grid role for calendar, aria-selected, aria-activedescendant).

Keyboard focus model and roving tabindex pattern.

Handling edge cases (selecting reversed ranges, quick drags, disabled dates).

Localization / time-zone pitfalls.

Follow-ups

Add date range presets (Last 7 days) and keyboard activation.

Add range via shift+click and touch-compatible selection.

Topics to learn

WAI-ARIA authoring practices, screen reader behavior.

Roving tabindex, focus management.

Intl.DateTimeFormat and calendar localization.

Pointer/touch event differences.

Unit & accessibility testing (axe, jest + DOM Testing Library).

3. DOM Diffing Engine (mini React reconcile)
Problem statement
Create a small DOM diffing/reconciliation engine that takes two lightweight virtual trees and updates the real DOM with minimal operations. The vDOM representation is: {type: 'div'|'text'|func', props: {...}, children: [...]}. It must:

Reuse existing DOM nodes where possible.

Perform keyed list reconciliation (insert/move/delete).

Support functional components (pure functions returning vDOM).

Minimize DOM operations and avoid full re-rendering.

Constraints & deliverables

Implement render(vnode, container) and update(newVnode) semantics.

Provide examples demonstrating keyed list moves, nested components.

Include complexity analysis for common operations.

What to evaluate

Correct keyed reconciliation algorithm (O(n) common subsequence heuristics).

Handling of component lifecycle (mount/unmount).

Avoiding unnecessary attribute updates and event re-binding.

Handling of text node vs element node replacements.

Follow-ups

Add batched updates and async scheduling (microtask/macrotask).

Support portals and fragments.

Topics to learn

Virtual DOM theory, diff/reconciliation algorithms (React’s heuristics).

Keyed lists and move detection (LCS vs fastest O(n) heuristics).

Event delegation and synthetic events.

Batching updates, microtask queue (Promise) vs macrotask.

4. Event Delegation System & Custom Event Propagation
Problem statement
Design and implement a custom event system on top of the DOM that supports:

Delegated event handlers with CSS-selector matching (attach once at root).

Event namespaces, priority, and the ability to stop propagation for delegated handlers without affecting native DOM propagation.

Ability to delegate.on(root, 'click.ns1', '.btn', handler, {priority: 10}).

Correct ordering and deterministic behavior across nested roots and dynamic DOM insertion.

Constraints & deliverables

Implement registration, matching, and dispatch algorithms.

Explain complexity and memory footprint.

Demonstrate correctness with nested, overlapping selectors and stopPropagation behavior.

What to evaluate

Efficient selector matching (useEventPath + matches, caching).

Handling dynamic DOM (mutation observers or relying on event bubbling + matching).

Priority model and ordering guarantees.

Memory leaks avoidance on handler removal.

Follow-ups

Add synthetic event features (persisted event objects, pooling).

Integrate with shadow DOM boundaries.

Topics to learn

Event propagation phases, composedPath(), event.target, currentTarget.

CSS selector matching (Element.matches), performance considerations.

MutationObserver basics.

Shadow DOM & event retargeting.

5. Diagnosing and Fixing Memory Leaks in a SPA
Problem statement
Given a sample single page app (you’ll be shown a codebase or snippet), find and fix memory leaks causing heap growth over time when navigating between views. Provide a report describing the root cause(s), patches, and a reproducible test harness that demonstrates the leak fix.

Constraints & deliverables

Use Chrome DevTools/heap snapshots to identify detached DOM nodes, event listener leaks, closures holding large objects.

Provide code diffs that fix leaks.

Provide automated repro (script or instructions) and metrics showing reduced retained memory.

What to evaluate

Use of DevTools allocation timeline, heap profiler, comparison snapshots.

Understanding of closure lifetimes, detached DOM nodes, RxJS subscriptions, and timers.

Applying correct fixes: removeEventListener, cancel timers, unsubscribe, null out references, weak refs.

Follow-ups

Propose architecture patterns to minimize leaks (lifecycle hooks, centralized resource registry).

Topics to learn

Chrome DevTools Memory Profiler (collection, comparison).

JS closures, GC roots, WeakMap/WeakRef.

Common sources of leaks: DOM references, timers, event listeners, RxJS observables.

6. ContentEditable Rich-Text Editor: Undo/Redo & Cursor Preservation
Problem statement
Implement a content-editable rich text editor with:

Bold/italic/underline, lists, and inline images.

Robust undo/redo stack that preserves cursor/selection position across edits, even after operations that re-render DOM.

Paste sanitization (strip disallowed tags).

Efficient representation to support very large documents (~100k words) without huge reflows.

Constraints & deliverables

API: execCommand(cmd), undo(), redo().

Provide a strategy to record granular changes and map selection state back after DOM changes.

Demonstrate complex sequences (format, paste, delete, undo/redo).

What to evaluate

Capture and restore of selection (Range, selection anchors) with node migrations.

Change representation: operational transforms, diffs, or deltas.

Performance (batching edits, avoiding full innerHTML rewrites).

Follow-ups

Add collaborative editing (CRDT/OT basics).

Add mention/autocomplete with async suggestions.

Topics to learn

Selection and Range APIs, getSelection(), caret positioning.

Serializing selection positions (path + offset), handling node identity changes.

Deltas/operational transform/CRDT basics.

Clipboard API & sanitization.

7. Browser Layout Engine Optimization — Minimize Reflows
Problem statement
You’re given a slow page that performs multiple DOM updates per frame, causing 30fps. Propose and implement optimizations to reach 60fps on scroll and resize interactions. Provide before/after metrics (frame timings), and explain each change’s effect on layout/paint.

Constraints & deliverables

Identify code paths causing forced synchronous layouts (e.g., reading layout after writes).

Provide a set of patch changes and performance measurements.

Explain tradeoffs and maintainability concerns.

What to evaluate

Ability to detect layout thrashers (repeated read/write cycles).

Use of batching, will-change, transform vs top/left, compositing layers.

Use of requestAnimationFrame, transform: translateZ(0), but discuss costs.

Follow-ups

Explain when will-change hurts performance.

Handling of large DOM trees and paint cost reduction (containment, contain CSS).

Topics to learn

Reflow/relayout, repaint, composite layers.

Browser rendering pipeline and paint profiler.

CSS containment, compositing, GPU vs CPU painting.

Tools: Chrome Performance, Paint Profiler.

8. Implement a Secure HTML Sanitizer with CSP-aware Output
Problem statement
Create a sanitization library that takes arbitrary HTML and returns safe HTML for injection into innerHTML, preventing XSS while preserving safe markup (links, formatting). Additionally, the sanitizer must:

Respect an allowlist of tags/attributes, and disallow javascript: URIs, data: in sensitive contexts.

Rewrite resource URLs to be CSP-compatible (e.g., convert inline scripts to external via nonce if configured).

Provide an API to integrate with a Content Security Policy (CSP) that forbids certain inline styles/scripts.

Constraints & deliverables

No use of eval. Provide tests showing typical attack vectors blocked and allowed content preserved.

Explain tradeoffs for sanitizing vs CSP vs server-side escaping.

What to evaluate

Understanding of DOMParser edge cases, attribute canonicalization, URL parsing.

Handling of exotic vectors: event handler attributes, srcdoc, <svg> with script, CSS url() values.

Safe decoding of HTML entities to avoid bypasses.

Follow-ups

Add sanitizer hooks for custom component embedding.

Discuss server-side vs client-side sanitization tradeoffs.

Topics to learn

XSS attack classes and mitigations.

CSP headers, nonces, and hashes.

DOMParser, URL parsing, attribute canonicalization, SVG attack surface.

Security testing (fuzzing inputs).

9. Cross-window / WebWorker Shared State with Low-latency Updates
Problem statement
Design a system that synchronizes a piece of application state between the main thread, multiple iframes, and a Web Worker with:

Low latency updates and eventual consistency.

A mechanism to avoid thrashing when many updates occur concurrently.

A small API for subscribe/publish with conflict resolution.

Constraints & deliverables

Use postMessage, BroadcastChannel, SharedArrayBuffer (where available), or IndexedDB as fallback.

Provide architecture diagram, and prototype demonstrating update flow and conflict handling.

Discuss security (origin checks) and cross-origin limitations.

What to evaluate

Choosing appropriate primitives for use-cases (BroadcastChannel for same-origin tabs, SharedArrayBuffer for high throughput).

Backpressure and aggregation strategies (debounce, coalesce, operation batching).

Handling worker termination and reconnection.

Follow-ups

Add encryption for cross-origin messaging via postMessage.

Add CRDT-based approach for true multi-writer editing.

Topics to learn

postMessage, BroadcastChannel, SharedArrayBuffer, Atomics.

Web Worker lifecycle, message serialization cost.

CRDTs, conflict resolution strategies, IndexedDB for persistence.

10. Design & Implement a Pluggable Plugin System for a UI Framework
Problem statement
Design a robust plugin architecture for a frontend UI framework so third-party plugins can:

Register UI components, lifecycle hooks, routes, and reducers.

Be isolated so faulty plugins cannot break the main app (fault containment).

Be hot-pluggable (load/unload at runtime) with dependency versioning and capability negotiation.

Constraints & deliverables

Define plugin API surface, registration process, and lifecycle (install, mount, unmount).

Implement sandboxing (e.g., iframe-based or VM-like isolation) and explain tradeoffs.

Demonstrate how plugin state is namespaced and how plugin errors are handled.

What to evaluate

Versioning strategy and dependency resolution.

Fault-isolation: communication channels, timeouts, circuit-breakers.

Security risks of third-party code and mitigation strategies.

Global state containment and deterministic unmounting.

Follow-ups

Enable plugins to add routes and lazy-load assets securely.

Marketplace model and permission prompts.

Topics to learn

Module systems, dynamic import, CSP implications.

Iframe sandboxing, postMessage APIs, proxied communication.

Feature flags, capability-based permissions, circuit breakers.

Packaging & semver strategies.

Quick study plan / common topics across all problems
Deep DOM APIs: getComputedStyle, offsetHeight, getBoundingClientRect, Range & Selection, MutationObserver, ResizeObserver.

Browser internals: layout, paint, composite, event loop (microtasks vs macrotasks), GC.

Performance tooling: Chrome DevTools (Performance, Memory, Rendering), Lighthouse.

Accessibility: WAI-ARIA patterns, screen readers, keyboard interactions.

Security: XSS classes, CSP, sandboxing.

Data structures & algorithms: trees, prefix sums, Fenwick, LRU caches, sequences/deltas.

Concurrency & offline: Web Workers, SharedArrayBuffer, BroadcastChannel, IndexedDB.

Engineering leadership: API design, backward compatibility, observability, test strategy, risk tradeoffs.

If you want, I can:

Convert any one of these into a full interview prompt with starter code, a rubric, and sample solutions (slow, medium, optimized).

Or produce an exercise kit (starter repo + tests + evaluation checklist) for a specific problem.

Which one should I expand into a full interview exercise first?

You said:
I need much more problems 
ChatGPT said:
Nice — got it. Below are 20 more hard frontend / DOM problems (principal/staff level). Each entry gives a focused problem statement, minimal deliverables/constraints, and the topics to learn to master it. I kept each one compact so you can scan quickly and pick the ones you want expanded into full interview prompts, starter code, or rubrics.

11. High-performance Drag & Drop with Accessibility
Problem: Build a drag-and-drop list supporting thousands of items with smooth dragging, keyboard reordering, multi-select drag, and accessible announcements for screen readers. Must avoid expensive layout thrashing and support touch + mouse + keyboard.
Deliverables: onDragStart, onDrop, keyboard reorder API, accessible live-region updates, example with 10k items.
Topics: Pointer Events, dragstart vs Pointer API, hit-testing, virtualization, aria-dropeffect/aria-grabbed, assistive announcements, avoid layout thrash.

12. Predictive Pre-rendering / Speculative Fetching Layer
Problem: Implement a client-side speculative loader that prefetches resources (HTML, data, images) based on user behavior predictions while respecting bandwidth, battery, and privacy.
Deliverables: Prediction heuristic, quota/backoff controls, devtools-visible metrics.
Topics: link rel=prefetch/preload, navigator.connection (save-data), heuristics, rate-limiting, privacy considerations.

13. Robust Offline-first Sync with Conflict Resolution
Problem: Create an offline-first data layer for a todo app that syncs with server when online, supports optimistic UI, and resolves conflicts using a last-writer-wins and CRDT hybrid.
Deliverables: Sync protocol, undo/redo across offline/online, conflict demo.
Topics: Service Worker, Background Sync, IndexedDB, CRDT basics, retries/exponential backoff.

14. Fine-grained CSS-in-JS Engine
Problem: Implement a CSS-in-JS engine that generates atomic CSS classes, supports server-side rendering/hydration, deduplication, theming, and minimal runtime cost.
Deliverables: API for css({ color }), SSR token generation, runtime dedupe.
Topics: CSSOM, performance of style insertion, SSR hydration tokens, specificity, style scoping, critical CSS.

15. Advanced Input Masking & Validation Library
Problem: Build an input masking library for international phone numbers, credit cards, and date inputs that preserves cursor, supports undo, and works with composition events (IME).
Deliverables: API to attach mask, tests for caret behavior and IME composition.
Topics: Composition events, Selection API, Unicode normalization, input event order, regex performance.

16. Secure File Upload Widget with Chunking & Resume
Problem: Implement a file uploader that uploads large files in chunks with resume support, progress across tabs, client-side hashing for dedup, and secure upload token refresh.
Deliverables: Chunking protocol, resume demo, token refresh flow.
Topics: fetch streaming, Service Worker, BroadcastChannel, resumable upload protocols (tus), content hashing (SHA-256), CORS & auth.

17. Tiny Animations Engine with Motion Planning
Problem: Create an animation engine that can run 1000+ simultaneous UI transitions at 60fps using GPU compositing and supports interruption, easing, and timeline control.
Deliverables: Animation API, example with many moving elements, interruption semantics.
Topics: requestAnimationFrame, CSS transforms vs layout-affecting properties, composing animations, Web Animations API.

18. Large-scale Form Engine with Conditional Logic & Autosave
Problem: Build a form engine that renders dynamic forms from JSON schema, supports conditional fields, autosave with debounce and offline queue, and incremental validation.
Deliverables: Schema format, autosave queue, validation hooks.
Topics: JSON Schema, validation strategies, debounce vs throttle, optimistic UI, IndexedDB for queue.

19. High-fidelity Pixel-Perfect Zoomable Canvas
Problem: Implement a zoomable, pannable canvas (SVG/Canvas/WebGL) that supports billions-of-pixels virtual space with tiled rendering and progressive LOD.
Deliverables: Smooth pan/zoom, tile loader, editing of vector objects with hit-testing.
Topics: Canvas vs SVG vs WebGL tradeoffs, spatial indexing (quadtrees), tile streaming, device pixel ratio handling.

20. Runtime Type Validation & Prop Contracts for UI Components
Problem: Build a runtime type-checking layer for components that validates props/contracts at runtime in dev, supports shape diffs, and reports minimal, actionable errors.
Deliverables: Lightweight runtime validator with error formatting, optional instrumentation hooks.
Topics: Structural typing, JSON schema, babel plugin integration for dev-only instrumentation, performance gating.

21. Hierarchical Permission System in Client UI
Problem: Design a client-side permission system for a large app enabling feature flags, role-based UI adjustments, and remote policy updates without a full reload.
Deliverables: Permission DSL, policy refresh mechanism, secure storage, graceful degradation.
Topics: Capability-based security, policy caches, caching/staleness, encryption for sensitive flags.

22. Browser-native PDF Viewer with Annotations
Problem: Build an in-browser PDF viewer supporting panning, zooming, text selection, and persistent annotations that sync to server.
Deliverables: Annotation model, highlight/notes, export/import annotations.
Topics: PDF.js integration, coordinate mapping across scales, text layer mapping, storage sync.

23. Precise Time/Alarm Scheduler in Web (multi-tab)
Problem: Provide a scheduling API that fires JS callbacks at precise wall-clock times across multiple tabs (one master elects, others subscribe) and survives tab crashes.
Deliverables: Election algorithm, fallback strategies, alarm accuracy analysis.
Topics: BroadcastChannel, leader election, Visibility API, timers/clamping, Service Worker alarms.

24. Custom Layout Engine (Constraint-based)
Problem: Build a small constraint-based layout engine (like Auto Layout) in JS that lays out UI nodes according to constraints and solves them efficiently.
Deliverables: Constraint solver, example UIs with dynamic resizing.
Topics: Cassowary solver basics, constraint propagation, performance engineering, integration with DOM.

25. Progressive Image Loading with Perceptual Metrics
Problem: Implement progressive loading strategy that selects image quality based on viewport, network, and perceptual saliency (e.g., faces in view).
Deliverables: Saliency detector, adaptive loader, metrics showing perceived quality vs bandwidth.
Topics: IntersectionObserver, lightweight on-device saliency heuristics, LQIP, responsive images srcset/sizes.

26. Shadow DOM + CSS Isolation Framework
Problem: Architect a UI component system using Shadow DOM that supports theme propagation, CSS custom properties fallback, and cross-shadow-styling primitives.
Deliverables: Theming API, cross-shadow focus management, style overrides.
Topics: Shadow DOM, ::part/::slotted, CSS custom properties, style scoping.

27. Deterministic Replay Tool for UI Bugs
Problem: Build a recorder/replayer that captures user events and DOM mutations to deterministically reproduce UI bugs (with serialization efficient enough for long sessions).
Deliverables: Recorder, replayer UI, compression strategy.
Topics: Event serialization, DOM mutationObserver, snapshot checkpoints, privacy/data scrubbing.

28. Component Graph Hot-reload w/o State Loss
Problem: Implement hot-reload for a component system that can swap component implementations at runtime while preserving local state and DOM where possible.
Deliverables: State migration strategy, module replacement demo.
Topics: Module hot-swapping, stable instance identity, serialization of closures/state, version migration.

29. Multi-language Right-to-left Layout Engine
Problem: Implement UI layout that supports mixed LTR and RTL content, bidi reordering, mirrored icons, and test cases across languages including Arabic/Hebrew.
Deliverables: Rendering engine handling embedded LTR runs, mirroring rules.
Topics: Unicode Bidirectional Algorithm, CSS direction, mirroring images, localized formatting.

30. Event Storming Resilience — Backpressure & Sampling
Problem: Design a client-side telemetry pipeline that tolerates bursty event generation, applies sampling/backpressure, persists during offline, and guarantees eventual delivery with bounded memory.
Deliverables: Sampling strategy, persistent queue, metrics, graceful drop policy.
Topics: Rate-limiting algorithms (token bucket), batching, IndexedDB, privacy-aware sampling.

31. Fast Diff/Highlight Changes for Code Editor
Problem: Implement an algorithm that diffs two large text documents (100k+ lines) in-browser and highlights changed regions with an O(n) or near-linear approach.
Deliverables: Diff algorithm, incremental update when small edits applied.
Topics: Myers diff tradeoffs, patience diff, suffix arrays, chunking strategies.

32. Cross-origin Embedding & Secure Communication Layer
Problem: Build a library to safely embed third-party widgets in iframes with controlled capabilities (DOM access denied), message passing with capability checks and fine-grained API surface.
Deliverables: Sandbox patterns, message protocol with auth, revocation flows.
Topics: iframe sandbox attributes, postMessage origin/security, proxy capabilities, CSP.

33. Declarative Gesture Recognition Library
Problem: Implement a gesture recognition system supporting pinch/rotate/complex gestures declaratively, works across touch/mouse/pen, and coexists with native browser gestures.
Deliverables: Gesture DSL, recognizer composability, preventDefault semantics.
Topics: Pointer Events, gesture state machines, hit testing, passive listeners.

34. Large-scale Accessibility Audit Automation
Problem: Create a tool that programmatically inspects a complex SPA for accessibility issues beyond basic rules (focus order, landmark usage, semantic misuses) and suggests prioritized fixes.
Deliverables: Audit runner, rule engine, prioritized report.
Topics: Accessibility heuristics, aXe rules, programmatic focus analysis, heuristic scoring.

35. Cross-browser Feature Detection & Polyfill Orchestration
Problem: Build a system that detects feature availability precisely (not user-agent sniffing), lazy-loads polyfills only when needed, and ensures ordering and minimal bundle impact.
Deliverables: Feature detection registry, polyfill loader with dependencies.
Topics: Feature detection patterns, dynamic import, performance & caching, CSP considerations.

Want me to:

Expand any of these into a full interview exercise (starter repo, test suite, rubric, hints)?

Produce a 30–60 minute take-home or full-day onsite variant for a specific problem?

Generate sample solutions (simple / optimized) for a chosen problem?

Pick one (or list a few) and I’ll convert it into a ready-to-use interview kit.

You said:
Are there still more unique problems? Or 
ChatGPT said:

Thought for a couple of seconds
Yes — absolutely. There are tons more unique, high-signal problems for Principal / Staff frontend engineers. Below I’ll give you 25 more distinct, high-difficulty problems (short statement + what to measure + core topics to study). If you want, I can immediately expand any single one into a full interview kit (starter repo, tests, rubric, sample solution).

36–60 — More unique, hard frontend / DOM problems
Composable Gesture-driven Canvas Editor
Build a vector editor that composes gestures (drag, double-tap, long-press) into commands, with undo/redo and precise hit-testing on transformed objects.
Topics: Pointer events, transform math, spatial indexing, command pattern, selection handles.

Deterministic CSS Cascade Visualizer
Create a tool that shows — for any element — the exact origin, specificity and cascade order of every computed style, including UA, user, author, inline, !important, and shadow roots.
Topics: CSS cascade, specificity, computed style internals, Shadow DOM.

Zero-downtime Frontend Migration Strategy
Design and prototype a rollout system that allows migrating parts of a legacy app to a new framework incrementally with no downtime and rollback support.
Topics: Feature flags, routing, module federation, incremental hydration, data migration.

High-volume Real-time Charts with Backfill
Implement charts that render tens of thousands of streaming points per second, support pause/backfill, zooming, and downsampling with visual fidelity.
Topics: WebGL/Canvas, downsampling (LTTB), decimation, time-series buffering.

Privacy-preserving Analytics SDK
Create an analytics SDK that guarantees differential-privacy-like guarantees on client-side aggregation and supports on-device aggregation before upload.
Topics: Differential privacy basics, aggregation, batching, privacy budgets, local-first metrics.

Reactive Formulas Engine (spreadsheet-like)
Build a reactive engine where cells contain formulas depending on other cells, supporting cycles detection, dependency graph, and batch recompute.
Topics: Topological sort, incremental recomputation, cycle detection, expression parsing.

Universal Focus Management for Modal/Drawer System
Design a library that manages focus trapping, restore, stacking, nested modals and portal patterns across Shadow DOM and iframes.
Topics: Focus management, inert, tabindex, aria-hidden patterns, portal focus edge-cases.

Pluggable Theming System with A/Bable Runtime
Implement runtime theming supporting CSS variables, classless fallbacks, on-the-fly theme switching, and A/B experiment hooks.
Topics: CSS custom properties, SSR theme hydration, feature flags, perceived flicker avoidance.

Efficient DOM Snapshot & Diff for Time Travel Debugging
Produce serialized snapshots of DOM + JS state cheaply and allow fast time-travel diffs to reproduce earlier app states.
Topics: Serialization, incremental checkpoints, compression, sanitization.

High-performance Accessibility Tree Sync
Implement a system to efficiently update an accessibility tree for a complex virtualized UI (screen-readers rely on it) without creating O(n) accessibility updates.
Topics: Accessibility tree model, ARIA, batching updates, role mappings.

Inline Code Execution Sandbox for Educational App
Design a secure in-browser sandbox enabling users to run JS/TS snippets safely with resource/time limits and state isolation.
Topics: iframe sandboxing, WebAssembly isolation, worker timeouts, resource limiting.

Predictable CSS Layouts via Constraint Solving
Create an engine that compiles high-level layout constraints into efficient DOM/CSS updates ensuring minimal reflow.
Topics: Constraint solvers, incremental layout compilers, layout invalidation minimization.

Adaptive Input Pipeline for IME-heavy Languages
Build controls that behave correctly across composition sequences (IME), mobile virtual keyboards, and assistive tech with selection stability.
Topics: Composition events, input event ordering, caret handling, mobile keyboard quirks.

End-to-end Encrypted Sync of User Settings
Create a client-side system that encrypts user settings before syncing to server so server never sees plaintext, supporting key rotation and multi-device sync.
Topics: WebCrypto API, key management, conflict resolution, secure backups.

Large-scale DOM Mutation Stress Tester
Build a harness that generates pathological DOM mutation patterns to stress-test layout, GC, and incremental rendering; then auto-detects regressions.
Topics: MutationObserver, synthetic workloads, perf instrumentation, stability metrics.

Composable ARIA Widgets Library (low-level primitives)
Implement primitives (roving focus, combobox, tree, grid) that are accessible, composable, testable, and themeable, with tiny runtime.
Topics: WAI-ARIA patterns, keyboard models, semantics-first APIs, test-driven accessibility.

Latency-adaptive UI Throttle
Design a client-side scheduler that adapts UI update frequency based on measured input-to-display latency and device capabilities.
Topics: Latency measurement, adaptive algorithms, rAF cadence, battery/network heuristics.

Safe Dynamic Script Loader with Dependency Graph
Implement a runtime that loads third-party scripts with declared dependencies, isolation, timeouts, retry/backoff and graceful degradation.
Topics: dynamic import, script tags vs modules, CSP, error handling, dependency resolution.

High-throughput Clipboard Manager for Complex Data
Create a clipboard manager that supports multiple serialized formats, incremental paste previews, and security restrictions.
Topics: Clipboard API, MIME types, paste sanitization, async clipboard.

Graphical Diff & Merge UI for Structured Docs
Build a visual diff/merge tool for nested JSON/DOM-like documents with conflict resolution UI for end-users.
Topics: Tree-diffing, merge algorithms, UX for conflicts, CRDT vs OT tradeoffs.

Composable Animation Keyframe Compiler
Create a compiler that takes high-level motion specifications and outputs performant CSS or Web Animations API usage with cross-browser fallbacks.
Topics: Web Animations API, easing curves, GPU-accelerated properties, compile-time transforms.

Universal Input Abstraction for Game-like UIs
Design an input layer that standardizes mouse/keyboard/touch/gamepad/VR controllers with mapping, rebinding, and latency compensation.
Topics: Gamepad API, pointer capture, input event normalization, mapping layers.

Dynamic Accessibility Role Inference Engine
Implement a system that infers missing semantics (roles, labels) for legacy markup, auto-injects ARIA safely, and explains changes to devs.
Topics: Heuristics, ML-assisted suggestions (or rule-based), false positives mitigation, explainability.

Composable Streaming Parser for Large HTML Documents
Build a streaming HTML parser that can progressively render and index a huge HTML stream in the browser without full DOM materialization.
Topics: Streaming parsing, incremental rendering, virtual DOM slices, backpressure.

Predictive Form Autofill with Privacy Controls
Implement smart autofill that predicts form intent, handles conditional fields, respects privacy policies, and offers per-field controls.
Topics: Heuristics, privacy-by-default, input heuristics, user prompts, secure storage.

If you want more I can:

Produce another batch (I can easily generate 100+ unique prompts).

Immediately expand any one of the items above into a full interview task: starter code, test harness, rubric, sample solutions (simple & optimized).

Organize problems into themed sets (performance, security, accessibility, architecture) and produce a timed panel of questions for onsite interviews.

Which direction should I take next — another huge batch, or expand one into a full exercise right away?

You said:
Another batch 
ChatGPT said:
Perfect ✅ — let’s go deeper. Here’s batch #61–85, all unique, tough frontend/DOM engineering problems that staff/principal-level interviews might use to probe deep system thinking, browser internals, and architectural leadership.

61–85 — More unique hard frontend/DOM problems
61. DOM Snapshot Compression for Error Reporting
Problem: Capture and transmit DOM snapshots on error reports without sending sensitive data, using structural hashing, compression, and redaction.
Topics: MutationObserver, DOM serialization, compression (gzip, brotli), privacy filters.

62. Client-side Search Index for Rich Content
Problem: Implement a full-text search index for 100k+ DOM nodes (docs, articles) that supports stemming, stopwords, incremental updates, and highlighting.
Topics: Inverted indexes, tokenization, web workers, memory optimization.

63. Predictive Layout Prefetcher
Problem: Build a runtime system that predicts which DOM elements will enter the viewport soon and precomputes their layout/styles to reduce jank.
Topics: IntersectionObserver, speculative rendering, layout/paint pipeline.

64. Sandbox for Untrusted Widgets with CSS Isolation
Problem: Design a framework that lets third-party widgets mount into your DOM without breaking global styles or leaking information.
Topics: Shadow DOM, iframe sandbox, CSS scoping, CSP.

65. State-machine Driven UI Workflow Engine
Problem: Model complex UI flows (multi-step forms, wizards, error recovery) as explicit state machines, with persistence and replay.
Topics: Statecharts, persistence, serialization, guard conditions.

66. Optimized Accessibility Announcer Queue
Problem: Implement a live-region announcer that batches and prioritizes screen reader messages to avoid spamming users.
Topics: ARIA live regions, debouncing, priority queues, UX heuristics.

67. Font Loading & FOUT/FOIT Mitigation
Problem: Architect a font loader that avoids flashes of invisible text (FOIT) while balancing layout shifts and performance.
Topics: Font Loading API, fallback stacks, layout stability, performance tradeoffs.

68. Multi-origin Authentication in SPAs
Problem: Implement a frontend auth manager that can handle multiple origins (iframe-embedded apps) securely with token refresh and logout sync.
Topics: postMessage, SameSite cookies, CORS, OAuth 2.0.

69. Declarative Undo/Redo History for Any Component
Problem: Design a global undo/redo manager where components register atomic actions and can be rolled back deterministically.
Topics: Command pattern, immutability, action logs, snapshots.

70. DOM-based Spreadsheet Renderer (Excel clone)
Problem: Render 1M+ spreadsheet cells efficiently in the DOM, supporting frozen rows/columns, scrolling, formulas, and selections.
Topics: Virtualization, canvas vs DOM tradeoffs, dependency graphs.

71. Performance Budget Enforcer in CI
Problem: Create a CI tool that runs Lighthouse/DevTools audits, blocks builds if bundle size/CLS/LCP exceed budget, and auto-generates reports.
Topics: CI/CD, Lighthouse API, thresholds, metrics pipelines.

72. Precise Input Latency Profiler
Problem: Build a profiler that measures input-to-paint latency per component and visualizes bottlenecks.
Topics: PerformanceObserver, event timing API, paint timing, flamecharts.

73. Secure Drag-drop Across Origins
Problem: Implement drag-drop where source/target may be different origins, ensuring no data leaks and enforcing policy.
Topics: HTML5 drag-drop, DataTransfer security, origin isolation.

74. DOM-based Collaborative Whiteboard
Problem: Build a collaborative whiteboard app where strokes sync across clients in real time with CRDTs for vector graphics.
Topics: Canvas/SVG, WebRTC/WebSocket, CRDT, delta compression.

75. Streaming Form Data Validator
Problem: As a user fills out a massive form, validate fields in real-time using streaming server responses while ensuring responsiveness.
Topics: Streams API, async validation, debounce, cancelation with AbortController.

76. Dynamic CSS Container Queries Polyfill
Problem: Implement a container query polyfill that re-renders elements when their container resizes.
Topics: ResizeObserver, mutation batching, layout dependencies.

77. Deterministic Multi-tab State Sync with Leader Election
Problem: Keep app state consistent across multiple open tabs, elect a leader tab for expensive operations, and survive tab close/crash.
Topics: BroadcastChannel, leader election algorithms, storage events.

78. Accessibility-First Rich Chart Component
Problem: Build an accessible chart that has full keyboard navigation, screen reader narration, and zoom/pan controls.
Topics: SVG, ARIA roles for charts, focus rings, screen reader UX.

79. Multi-stage Progressive Web App Bootstrapping
Problem: Architect a PWA startup flow that progressively hydrates: shell → skeleton UI → cached content → live content, with minimal blocking.
Topics: App shell model, hydration, SW caching, skeleton screens.

80. DOM Layout Stress Simulator
Problem: Write a tool that generates pathological DOM layouts (deep nesting, massive reflows) and measures browser perf regressions.
Topics: Benchmark harnesses, DOM APIs, layout thrash detection.

81. Incremental Static DOM Rehydration
Problem: Implement an algorithm that rehydrates server-rendered DOM progressively (prioritizing visible elements).
Topics: SSR hydration, priority queues, idle tasks, streaming.

82. DOM Virtual Filesystem Explorer
Problem: Render a filesystem tree with millions of files/folders, lazy-load children, support search/filter, and keyboard nav.
Topics: Virtualization, async loading, keyboard UX, tree widgets.

83. Client-only Secure Secret Manager
Problem: Implement client-side secret storage (like API keys) with encryption-at-rest and no server exposure.
Topics: WebCrypto, localStorage/IndexedDB encryption, key rotation.

84. Predictive Prefetch with ML Integration
Problem: Train a small on-device ML model to predict next navigation and prefetch assets, respecting privacy & bandwidth.
Topics: TensorFlow.js, caching strategies, network info API.

85. Component Error Boundary System
Problem: Build a reusable error boundary system (like React’s) for vanilla JS components, capturing errors and showing fallbacks without full reload.
Topics: window.onerror, unhandledrejection, component lifecycle, resilience.

🔥 That brings us up to 85 unique problems so far.

Would you like me to keep going to hit 100+ unique problems, or pause here and start organizing them into categories (Performance, Accessibility, Security, Architecture, DX, etc.) so you can quickly pick interview themes?

You said:
100
ChatGPT said:
Nice — let’s finish the list to 100. Below are problems 86–100, each unique, high-difficulty, and suitable for Principal/Staff frontend interviews. Short statement + one-line notes on deliverables and core topics to study.

86. Deterministic Cross-browser Rendering Diff Tool
Problem: Build a tool that loads a page in multiple browser engines (or browser versions) and highlights pixel and layout diffs, attributing differences to CSS/HTML/JS causes.
Deliverables/Topics: Screenshot diffing, DOM/CSS blame heuristics, CSSOM differences, cross-browser quirks.

87. Resource-aware Image CDN Client
Problem: Create a client-side image selection layer that picks optimal image variants from a CDN based on DPR, viewport, user motion preference, and quota.
Deliverables/Topics: srcset/sizes auto-generation, DPR handling, save-data, heuristics.

88. Declarative Reactive Transitions Language
Problem: Design a small DSL that describes transitions between UI states (enter/exit/stagger) and compile it into efficient runtime code.
Deliverables/Topics: Parser/compiler, animation scheduling, cancellation semantics, Web Animations API.

89. Secure WebAuthn Multi-factor Flow
Problem: Implement a frontend flow that orchestrates password + WebAuthn device registration and fallback gracefully across browsers.
Deliverables/Topics: WebAuthn API, credential management, attestation, UX for fallbacks.

90. Tiny Deterministic Scheduler for Heavy DOM Work
Problem: Build a cooperative scheduler that slices large DOM tasks (tree updates, diffing) into micro-jobs, keeps UI responsive, and is deterministic for testing.
Deliverables/Topics: Task slicing, cooperative scheduling, Jest-friendly determinism, time-slicing.

91. Adaptive Layouts for Foldable / Multi-screen Devices
Problem: Design UI components and breakpoints that adapt to hinge/fold states and multi-screen layouts (local emulator support).
Deliverables/Topics: CSS viewport segments API, window segments, fold-aware UX patterns.

92. Accessibility-aware Image Annotation Tool
Problem: Build an image annotation tool that also generates alt-text suggestions and semantic labels for each region for assistive tech.
Deliverables/Topics: Region mapping, alt-text heuristics, accessibility metadata formats.

93. High-performance DOM Merging for Microfrontends
Problem: Implement a DOM-merge protocol so independently-deployed microfrontends can coexist in a page and share common DOM root without conflicts.
Deliverables/Topics: Namespacing, CSS isolation, event containment, lifecycle contracts.

94. Continuous Interaction Recorder for UX Research
Problem: Create a privacy-aware recorder that logs interactions, input timing, and UI state transitions for later analysis, with scrub options.
Deliverables/Topics: Event sampling, privacy redaction, chunked uploads, analysis-ready export.

95. Structured Content Editor with Plugin API
Problem: Build a document editor for nested content (blocks/components) with a plugin system that can add block types, serialization, and schema validation.
Deliverables/Topics: Block model, schema validation, plugin lifecycle, collaborative hooks.

96. Cross-platform Native-like Tactile Feedback Layer
Problem: Implement an abstract haptic & audio feedback layer that maps UI actions to device-native sensations across platforms.
Deliverables/Topics: Vibration API, platform capability detection, fallbacks, UX tuning.

97. Efficient Multi-lingual Runtime Intl Loader
Problem: Create a system for loading and switching i18n locale data at runtime with minimal bundle cost and instant UI swap without reload.
Deliverables/Topics: Chunked locale data, ICU message handling, pluralization, caching.

98. Component-level Performance SLA Enforcement
Problem: Build tooling that monitors component render times in production and triggers fallbacks or degrades features when a component exceeds defined SLAs.
Deliverables/Topics: Performance marks/measures, feature-flagged degradation, alerting & observability.

99. Progressive Hydration with Interaction Tracing
Problem: Implement progressive hydration that hydrates components in priority order based on actual user interactions traced from server-rendered markup.
Deliverables/Topics: Interaction tracing, priority queue hydration, idle-time scheduling.

100. Low-latency Image Editing Pipeline in Browser
Problem: Build an in-browser image editor supporting nondestructive edits (layers/filters), undo history, and GPU-accelerated filters for large images.
Deliverables/Topics: WebGL or OffscreenCanvas pipeline, layer compositing, history/delta storage, memory management.

That’s 100 total — a comprehensive playground of problems across performance, accessibility, security, architecture, and UX.