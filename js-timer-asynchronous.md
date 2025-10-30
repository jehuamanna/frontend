|   # | Title                                     | Problem / Prompt                                                                                    |
| --: | ----------------------------------------- | --------------------------------------------------------------------------------------------------- |
|   1 | Microtask vs Macrotask Order              | Predict the exact console order for mixed `Promise.then`, `queueMicrotask`, and `setTimeout` calls. |
|   2 | Nested Timers Ordering                    | Explain order and timing when `setTimeout` schedules another `setTimeout` inside its callback.      |
|   3 | Promise + setTimeout Race                 | Does a `then(() => setTimeout(...)) .then(() => ...)` wait for the timeout? Fix it so it does.      |
|   4 | Blocking Loop & Timers                    | Demonstrate how a long synchronous loop delays a pending `setTimeout`.                              |
|   5 | Zero Delay Timers                         | Show how `setTimeout(fn, 0)` differs from `Promise.resolve().then(fn)` in execution order.          |
|   6 | Implement mySetInterval                   | Implement `mySetInterval` using only `setTimeout` and provide `myClearInterval`.                    |
|   7 | Debounce Implementation                   | Implement `debounce(fn, wait, options)` supporting leading/trailing calls and cancellation.         |
|   8 | Throttle Implementation                   | Implement `throttle(fn, wait, options)` supporting `leading` and `trailing`.                        |
|   9 | Sleep / Wait Utility                      | Implement `wait(ms)` that returns a `Promise` and doesn't block the event loop.                     |
|  10 | Timeout Promise Wrapper                   | Implement `withTimeout(promise, ms)` that rejects with `TimeoutError`.                              |
|  11 | Retry with Backoff                        | Implement `retry(fn, attempts, delay, factor)` with exponential backoff.                            |
|  12 | Rate Limiter (Token Bucket)               | Implement a token-bucket rate limiter that schedules calls using timers.                            |
|  13 | Scheduler with Concurrency                | Implement a scheduler that runs N tasks concurrently and queues the rest.                           |
|  14 | setInterval Drift Measurement             | Write code to measure drift of `setInterval(fn, 1000)` over 1 minute.                               |
|  15 | Drift-Correcting Clock                    | Create a clock using timers that corrects for drift/throttling to stay accurate.                    |
|  16 | Retry with Jitter                         | Extend exponential backoff to include random jitter to avoid thundering herd.                       |
|  17 | Sequential Tasks with Gaps                | Run an array of async tasks sequentially with X ms gap between each.                                |
|  18 | Parallel Completion Order                 | Run N promises with random delays and log results in completion order.                              |
|  19 | sleepSort Deterministic                   | Implement sleep sort deterministically using `await` instead of `setTimeout` only.                  |
|  20 | Implement setImmediate Polyfill           | Implement `setImmediate` using available browser features and explain differences.                  |
|  21 | queueMicrotask vs process.nextTick        | Compare microtasks in browser and Node: `queueMicrotask` vs `process.nextTick`.                     |
|  22 | Long `setTimeout` Handling                | How to schedule a callback after >2^31-1 ms reliably (long timeouts).                               |
|  23 | Cancel Within Callback                    | Show behavior of calling `clearTimeout` for a timer ID inside its own callback.                     |
|  24 | Nested clearTimeout Race                  | Race between `clearTimeout(id)` and the timer firing — explain edge cases.                          |
|  25 | Debounce + Promise-returning fn           | Implement debounce that returns a promise resolving to the debounced function's result.             |
|  26 | Throttle with Trailing Value              | Throttle that returns last-call’s arguments on trailing invocation.                                 |
|  27 | requestAnimationFrame vs setTimeout       | Compare `requestAnimationFrame` and `setTimeout` for animation timing.                              |
|  28 | Use performance.now() for Accuracy        | Re-implement a periodic timer using `performance.now()` to minimize drift.                          |
|  29 | Visibility API & Timers                   | Pause/resume scheduled background tasks when page is hidden/visible.                                |
|  30 | Web Worker Timer Limitations              | Show how timers in web workers behave and implement a timer-based worker pool.                      |
|  31 | setInterval vs Recursive setTimeout       | Demonstrate why recursive `setTimeout` avoids drift under load.                                     |
|  32 | Implement debounce leading/trailing       | Debounce function supporting both leading and trailing invocation semantics.                        |
|  33 | Timer Heap / Priority Queue               | Implement a timer scheduler using a min-heap (priority queue) for many timeouts.                    |
|  34 | Task Slicing (Cooperative Multitasking)   | Slice long tasks into chunks using timers to keep UI responsive.                                    |
|  35 | Cooperative Yield API                     | Implement `yieldToEventLoop()` that yields repeatedly until a condition is met.                     |
|  36 | Timers + Async Generators                 | Implement an async generator that yields on intervals: `async function* ticker(ms)`.                |
|  37 | Timeout for fetch with AbortController    | Implement fetch with timeout using `AbortController` and `setTimeout`.                              |
|  38 | Promise.race Timer Bug                    | Show common bug when `Promise.race([p, timeout])` leaks if timeout resolves after rejection.        |
|  39 | Watchdog Timer                            | Implement a watchdog: cancel a long-running async task if it doesn't heartbeat.                     |
|  40 | Rate-limited Queue                        | Build a queue that processes at most M tasks per T milliseconds using timers.                       |
|  41 | Sliding Window Rate Limit                 | Implement sliding-window rate limiter with timers to expire counts.                                 |
|  42 | Rate-limit with Queue Persistence         | Persist queued tasks (IndexedDB) and schedule them after reload using timers.                       |
|  43 | Cron-like Scheduler                       | Implement a cron expression parser and scheduler that uses timers to run jobs.                      |
|  44 | scheduleAtSpecificTime                    | Schedule a function to run at a specific absolute Date (handles DST & clock changes).               |
|  45 | Pause/Resume Interval                     | Implement pause/resume API for a recurring scheduled job (accurate resume).                         |
|  46 | Heartbeat + reconnect backoff             | Implement heartbeat with reconnect backoff for a WebSocket client.                                  |
|  47 | Timer-based Semaphore                     | Implement a semaphore that releases permits after a timeout automatically.                          |
|  48 | Timers across iframes                     | Demonstrate and handle timers across nested iframes (same-origin and cross-origin caveats).         |
|  49 | Thundering Herd Simulation                | Simulate many clients retrying with timers and implement mitigation strategies.                     |
|  50 | requestIdleCallback Fallback              | Implement `requestIdleCallback` fallback using `setTimeout` and `postMessage`.                      |
|  51 | Microtask Starvation Demo                 | Create a scenario where continuous microtasks starve macrotasks and explain fix.                    |
|  52 | Timer Cancellation Token                  | Implement cancellable timers using an `AbortSignal`-like API.                                       |
|  53 | Async Throttle with Queue                 | Throttle async jobs: ensure only K run per window and queue the rest with timers.                   |
|  54 | Promise Timeout with Cleanup              | Ensure `withTimeout` cleans up timers to avoid memory leaks on early settle.                        |
|  55 | Multi-stage Timeout                       | Chain multiple increasing timeouts until a condition is satisfied, then stop.                       |
|  56 | Periodic Background Sync (Service Worker) | Outline how to schedule periodic work in service worker environment (limitations).                  |
|  57 | Timer-based Lock with TTL                 | Implement a distributed-like lock with local TTL using timers and persistence.                      |
|  58 | Timer Leak Detection                      | Write a utility to detect and log un-cleared timers that leak across component unmounts.            |
|  59 | Fake Timers for Tests                     | Implement a minimal fake timer system to test timer-based code deterministically.                   |
|  60 | Timers + CSS Transitions Sync             | Coordinate JS timers with CSS transitions and `transitionend` for consistent UI.                    |
|  61 | Polling with Backoff                      | Implement a poller that fetches until success with backoff & cancellation.                          |
|  62 | Throttle Promises by Rate                 | Given API that accepts at most R req/sec, throttle promise calls across app.                        |
|  63 | Worker Pool with Timers                   | Build a pool of Web Workers and use timers to assign/check tasks and timeouts.                      |
|  64 | Batch Requests using Timers               | Coalesce frequent calls into a single batched call after X ms (batch window).                       |
|  65 | Timers + localStorage Fallback            | Schedule a job and survive page reloads by saving schedule to `localStorage`.                       |
|  66 | Adaptive Interval                         | Dynamically adapt revisit interval depending on success/error rates using timers.                   |
|  67 | Binary Exponential Backoff                | Implement binary exponential backoff with maximum cap and reset on success.                         |
|  68 | Periodic Cleanup Job                      | Schedule periodic cleanup (like cache TTL) and ensure single-run across tabs.                       |
|  69 | Single-Tab Leader Election                | Use `localStorage` + timers to elect a leader tab for periodic jobs.                                |
|  70 | Multi-tab Queue Consumer                  | Balance timer-driven job consumption across multiple browser tabs.                                  |
|  71 | Timer-based Sliding Window Counters       | Implement sliding counters for metrics aggregation using timers to evict buckets.                   |
|  72 | Timer Precision Benchmark                 | Measure precision/accuracy of timers on different browser throttling states.                        |
|  73 | Monotonic Clock vs System Clock           | Re-schedule jobs safely if system clock changes (use performance.now).                              |
|  74 | Debounce with Immediate Reject            | Debounce wrapper that rejects previous pending promise when a new call arrives.                     |
|  75 | Auto-retry with Circuit Breaker           | Retry failed ops with timers, but trip circuit breaker after N failures.                            |
|  76 | Rate Limit Headers Parsing                | Use timer-driven tokens to honor server `RateLimit-Reset` headers.                                  |
|  77 | Progressive Backoff for UI Polling        | Poll UI data faster on active use, slow down using timers when inactive.                            |
|  78 | Timer-based Priority Queue                | Implement priority scheduling where timers schedule high-priority sooner.                           |
|  79 | Sleepable Promise Queue                   | Implement a queue where `dequeue()` waits (async) until an item is available using timers.          |
|  80 | Cascading Timeouts                        | Run tasks with cascading timeouts where child tasks inherit parent's remaining time.                |
|  81 | Periodic Metrics Aggregator               | Aggregate metrics every T ms with timer and ensure no overlap if run takes long.                    |
|  82 | Timer Reentrancy Problem                  | Demonstrate and fix reentrancy bug when a timer callback triggers same timer creation.              |
|  83 | Clock with leap-second handling           | Design scheduling to handle rare system clock adjustments (leap seconds).                           |
|  84 | Timer-load Balancer                       | Distribute scheduled jobs across multiple workers to avoid spikes using timers.                     |
|  85 | JS animation timeline                     | Build timeline API for scheduling animations with precise start/duration using raf.                 |
|  86 | Batch DB Writes with Delay                | Buffer writes for X ms and flush in a batch using a timer.                                          |
|  87 | Timeout-aware Promise.map                 | Implement `mapWithTimeout(array, fn, timeout)` cancelling late tasks.                               |
|  88 | Timers + CSP/Workers restrictions         | Explain issues scheduling timers in strict CSP or cross-origin worker contexts.                     |
|  89 | Lazy Initialization with Timer            | Initialize heavy resource on first use, with a deferred timer-start fallback.                       |
|  90 | Throttle plus leading/trailing Promise    | Throttle an async function where calls return a promise that resolves when executed.                |
|  91 | Timeout-aware Event Listener              | Add an event listener that auto-removes after inactivity timeout.                                   |
|  92 | Circuit Breaker Reset Timer               | Implement auto-reset of circuit breaker state after a cooldown timer.                               |
|  93 | CPU-friendly Polling                      | Implement polling that backs off and yields to event loop between checks.                           |
|  94 | Prefetcher with Timers                    | Schedule background prefetching tasks with dynamic delays and cancellation.                         |
|  95 | Rate-limit with Burst Capacity            | Implement rate limiter allowing short bursts using tokens refilled by timer.                        |
|  96 | Task Deadline Enforcement                 | Given task and deadline, abort or skip tasks that would exceed deadline using timers.               |
|  97 | Timer-based Mutex                         | Implement a mutex where lock acquisition times out after X ms automatically.                        |
|  98 | Coordinated Timers across Devices         | Design sync strategy for scheduled tasks across devices with clock skew.                            |
|  99 | Progressive Retry with Max Concurrency    | Retry failed tasks progressively but maintain max concurrency using timers.                         |
| 100 | Visualizing Event Loop                    | Build a visualization tool that logs stack/microtask/macrotask order over time.                     |
