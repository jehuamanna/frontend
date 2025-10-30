🧭 A. Execution Control Utilities

Functions that control when or how often another function runs.

Function	Description
once(fn)	Ensures fn runs only once, caching its result.
before(n, fn)	Allows fn to run at most n times.
after(n, fn)	Runs fn only after it’s been called n times.
throttle(fn, wait)	Limits fn to run at most once per wait ms.
debounce(fn, wait)	Delays execution until no calls happen for wait ms.
delay(fn, ms)	Defers execution of fn by ms milliseconds.
defer(fn)	Queues function execution to the next event loop tick.
rateLimit(fn, limit, window)	Like throttle, but limits calls per time window.
poll(fn, interval)	Continuously invokes fn at fixed intervals until stopped.
retry(fn, times)	Retries a failing function up to times attempts.
batch(fn, limit)	Queues multiple calls and runs them together.
🧮 B. Caching & Optimization Utilities

Functions that store results or intermediate data between calls.

Function	Description
memoize(fn, resolver?)	Caches results by input args.
onceAsync(fn)	Async version of once, caches the returned promise.
cache(fn, keyFn)	Similar to memoize but uses custom key logic.
lazy(fn)	Executes only once and stores the result for future calls.
initOnce(factory)	Initializes a resource once, returns the same instance.
withCache(fn, ttl)	Caches function output with expiration time.
⚙️ C. Function Transformation Utilities

Functions that create new functions with behavior derived from another.

Function	Description
curry(fn)	Transforms fn(a, b, c) → fn(a)(b)(c).
partial(fn, ...args)	Pre-fills some arguments for later.
compose(...fns)	Composes right-to-left function execution.
pipe(...fns)	Composes left-to-right execution.
wrap(fn, wrapper)	Returns a new function wrapping another with extra logic.
flip(fn)	Swaps the order of function arguments.
negate(fn)	Returns a function that negates the result of fn.
guard(fn, predicate)	Runs fn only if predicate passes.
tap(fn)	Runs fn for side effects and returns the original input.
🧱 D. State & Encapsulation Utilities

Functions that hold internal state via closures.

Function	Description
counter(initial = 0)	Returns functions to increment/decrement a private number.
toggle(...states)	Cycles through multiple values on each call.
onceFlag()	Returns a closure that reports whether it’s been triggered.
accumulator()	Stores accumulated values over time.
createStore(initial)	Returns getter/setter closures for data.
namespace(obj)	Encapsulates data for modular namespaces.
sequentialId(prefix)	Generates unique IDs via internal counter.
🔁 E. Asynchronous & Promise Utilities

Functions that manage async state or concurrency via closures.

Function	Description
onceAsync(fn)	Like once, but works with async/await and caches the promise.
debounceAsync(fn, wait)	Debounces async functions.
throttleAsync(fn, wait)	Async-safe throttling.
queue(fn, concurrency)	Controls concurrency by tracking running promises.
limit(fn, n)	Only allows n concurrent executions of fn.
retryAsync(fn, attempts, delay)	Retries async function until success or limit.
cachePromise(fn)	Stores and reuses in-flight promises for identical inputs.
deferAsync(fn)	Runs async after current stack clears.
🧩 F. Utility Closures for Events & DOM

Functions that encapsulate event state or behavior.

Function	Description
onceEvent(element, event, handler)	Adds a one-time event listener.
debouncedResize(handler, wait)	Handles resize with debounce.
eventBuffer(fn, delay)	Buffers multiple rapid events into one call.
lazyLoader(selector)	Loads DOM content only once when needed.
withContextMenu(state)	Retains last right-clicked element.
🔒 G. Security / Privacy via Closure

Functions that use closures to hide internal data.

Function	Description
createPrivateStore()	Uses a closure or WeakMap for private object data.
makeCounter()	Returns { inc, dec } with hidden value.
privateMethodFactory()	Hides methods not meant for public use.
onceSecret(key)	Returns function that validates secret only once.
🧠 H. Miscellaneous Functional Tools

Other closure-driven helpers often seen in libraries like Lodash, Ramda, etc.

Function	Description
constant(value)	Always returns the same value.
identity(x)	Returns its argument (used in functional chains).
noop()	Does nothing, but still a closure returning a function.
uniqueId(prefix)	Uses internal counter to create unique IDs.
times(n, fn)	Executes a function n times, maintaining counter state.
sequence(...fns)	Runs multiple functions in order.
predicateChain(...predicates)	Combines multiple boolean closures.
withRetry(fn, maxTries)	Repeats until success.
oncePerTick(fn)	Runs at most once per event loop tick.
📦 I. Popular Libraries That Implement These
Library	Common Closure Utilities
Lodash / Underscore	once, debounce, throttle, memoize, before, after, partial, curry, wrap, delay
Ramda	curry, compose, pipe, memoizeWith, partial, flip
Async.js	queue, retry, memoize, limit
React	Hooks like useState, useEffect, useCallback, useMemo
RxJS	Operators like throttleTime, debounceTime, shareReplay use closure state internally