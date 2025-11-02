# Promise Compositions — Reference

A single-file reference of common and advanced JavaScript **Promise composition** patterns with reusable implementations and short explanations. Use these templates as building blocks in real projects or interviews.

---

## Table of contents

1. Core utilities
2. Mapping / Filtering / Reducing helpers
3. Concurrency control (pool / p-limit)
4. Timeout, race & cancellation helpers
5. Retry & backoff
6. Fallbacks, failover, and priority
7. AllSettled / error aggregation
8. Pipeline / compose helpers
9. Advanced patterns (fan-out/fan-in, multiplexing)
10. Small examples & usage notes

---

## 1. Core utilities

### `timeout` — wrap a promise with a timeout
```js
function timeout(promise, ms, message = 'Timeout') {
  const timer = new Promise((_, reject) =>
    setTimeout(() => reject(new Error(message)), ms)
  );
  return Promise.race([promise, timer]);
}
```

### `defer` — deferred promise (for advanced control)
```js
function defer() {
  let resolve, reject;
  const promise = new Promise((res, rej) => {
    resolve = res; reject = rej;
  });
  return { promise, resolve, reject };
}
```

---

## 2. Mapping / Filtering / Reducing helpers

### `mapAsync` — run mapper in parallel and preserve order
```js
async function mapAsync(array, mapper) {
  return Promise.all(array.map((item, i) => Promise.resolve().then(() => mapper(item, i))));
}
```

### `filterAsync` — async predicate (runs in parallel)
```js
async function filterAsync(array, predicate) {
  const results = await Promise.all(array.map((item, i) => Promise.resolve().then(() => predicate(item, i))));
  return array.filter((_, i) => results[i]);
}
```

### `reduceAsync` — sequential async reduce
```js
async function reduceAsync(array, reducer, initial) {
  let acc = initial;
  for (let i = 0; i < array.length; i++) {
    acc = await reducer(acc, array[i], i);
  }
  return acc;
}
```

---

## 3. Concurrency control

### `pMap` — limit concurrency (simple pool)
```js
function pMap(inputs, mapper, concurrency = 5) {
  const results = new Array(inputs.length);
  let i = 0;

  return new Promise((resolve, reject) => {
    let active = 0;
    function next() {
      if (i >= inputs.length && active === 0) return resolve(results);
      while (active < concurrency && i < inputs.length) {
        const idx = i++;
        active++;
        Promise.resolve()
          .then(() => mapper(inputs[idx], idx))
          .then((res) => { results[idx] = res; active--; next(); })
          .catch(reject);
      }
    }
    next();
  });
}
```

Usage: `await pMap(items, async item => fetchItem(item), 10)`

---

## 4. Timeout, race & cancellation helpers

### `firstFulfilled` — like `Promise.any`, but returns value or throws aggregated error
```js
async function firstFulfilled(promises) {
  // Native Promise.any exists in modern runtimes; this example demonstrates manual behaviour
  const errors = [];
  return new Promise((resolve, reject) => {
    let pending = promises.length;
    promises.forEach((p, i) => {
      Promise.resolve(p)
        .then(resolve)
        .catch(err => {
          errors[i] = err;
          pending -= 1;
          if (pending === 0) reject(new AggregateError(errors, 'All promises rejected'));
        });
    });
  });
}
```

### `withAbort` — attach AbortController to fetch-like APIs
```js
function withAbort(promiseFactory) {
  const controller = new AbortController();
  const promise = promiseFactory(controller.signal);
  return { promise, controller };
}
```

Example: `const { promise, controller } = withAbort(sig => fetch(url, { signal: sig }));` then `controller.abort()` to cancel.

---

## 5. Retry & backoff

### `retry` — simple retry with fixed attempts
```js
async function retry(fn, attempts = 3, delayMs = 1000) {
  let lastError;
  for (let i = 0; i < attempts; i++) {
    try {
      return await fn(i);
    } catch (err) {
      lastError = err;
      if (i < attempts - 1) await new Promise(r => setTimeout(r, delayMs));
    }
  }
  throw lastError;
}
```

### `retryWithBackoff` — exponential backoff with jitter
```js
async function retryWithBackoff(fn, {
  attempts = 5,
  minDelay = 200,
  maxDelay = 2000,
  factor = 2,
  jitter = true
} = {}) {
  let attempt = 0;
  let err;
  while (attempt < attempts) {
    try {
      return await fn(attempt);
    } catch (e) {
      err = e;
      attempt++;
      if (attempt >= attempts) break;
      let delay = Math.min(minDelay * Math.pow(factor, attempt - 1), maxDelay);
      if (jitter) delay = Math.random() * delay;
      await new Promise(r => setTimeout(r, delay));
    }
  }
  throw err;
}
```

---

## 6. Fallbacks, failover, and priority

### `tryInOrder` — attempt functions one-by-one until one resolves
```js
async function tryInOrder(fns) {
  let lastErr;
  for (const fn of fns) {
    try {
      return await fn();
    } catch (e) {
      lastErr = e;
    }
  }
  throw lastErr;
}
```

Usage: `await tryInOrder([() => fetch(primary), () => fetch(secondary), () => localCache()])`.

---

## 7. AllSettled / error aggregation

### `allSettledResults` — wrapper that throws if too many failures, else returns successes
```js
async function allSettledResults(promises, { allowFailures = Infinity } = {}) {
  const settled = await Promise.allSettled(promises);
  const errors = settled.filter(s => s.status === 'rejected').map(s => s.reason);
  const values = settled.filter(s => s.status === 'fulfilled').map(s => s.value);
  if (errors.length > allowFailures) {
    const err = new Error('Too many failures');
    err.errors = errors;
    throw err;
  }
  return { values, errors };
}
```

---

## 8. Pipeline / compose helpers

### `pipeAsync` — left-to-right composition
```js
function pipeAsync(...fns) {
  return async (input) => {
    let v = input;
    for (const fn of fns) {
      v = await fn(v);
    }
    return v;
  };
}
```

### `composeAsync` — right-to-left composition
```js
function composeAsync(...fns) {
  return pipeAsync(...fns.reverse());
}
```

### `sequence` — run promise-returning functions sequentially (
```js
async function sequence(funcs, initial) {
  let acc = initial;
  for (const fn of funcs) {
    acc = await fn(acc);
  }
  return acc;
}
```

---

## 9. Advanced patterns

### Fan-out / Fan-in (master-worker pattern)
```js
async function fanOutIn(seed, workers, workerFn) {
  // workers: array of inputs derived from seed
  // workerFn: async (workerInput) => result
  const tasks = workers.map(w => workerFn(w, seed));
  return Promise.all(tasks); // gather
}
```

### Multiplexing — share single in-flight promise result to many callers
```js
function makeSingletonAsync(fn) {
  let inFlight = null;
  return function(...args) {
    if (!inFlight) {
      inFlight = Promise.resolve().then(() => fn(...args)).finally(() => { inFlight = null; });
    }
    return inFlight;
  };
}
```

### Lazy promise — only start when called
```js
function lazy(fn) {
  return () => Promise.resolve().then(fn);
}
```

---

## 10. Small examples & usage notes

- **Parallel map with concurrency**: `await pMap(items, async i => fetch(i), 10)`.
- **Retrying fetch with timeout**:
```js
await retryWithBackoff(() => timeout(fetch(url), 5000), { attempts: 4 });
```
- **Pipeline example**:
```js
const transform = pipeAsync(parseJSON, enrich, saveToDb);
await transform(rawPayload);
```

---

## Appendix — extra helpers

### `delay` helper
```js
const delay = ms => new Promise(r => setTimeout(r, ms));
```

### `AggregateError` polyfill (for older runtimes)
```js
class SimpleAggregateError extends Error {
  constructor(errors, message = 'AggregateError') {
    super(message);
    this.name = 'AggregateError';
    this.errors = errors;
  }
}
```

---

## Closing notes
- Prefer small, composable functions (factories returning promises) rather than starting Promises eagerly.
- Use `AbortController` for cancellable APIs (fetch) and combine with `Promise.race` for timeouts.
- Keep concurrency bounded for network and CPU heavy tasks.


*End of file.*

