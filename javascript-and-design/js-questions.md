# 📘 JavaScript Interview Questions
| # | Title | Description | Category / Topic |
|---|--------|--------------|------------------|
| 1 | Promise.all() polyfill | Implement `Promise.all()` manually. | Promises / Polyfills |
| 2 | Promise.any() polyfill | Resolve as soon as any promise resolves. | Promises / Polyfills |
| 3 | Promise.race() polyfill | Return first settled (resolved or rejected) promise. | Promises / Polyfills |
| 4 | Promise.finally() polyfill | Always execute cleanup logic after promise settles. | Promises / Polyfills |
| 5 | Promise.allSettled() polyfill | Wait for all promises (fulfilled/rejected). | Promises / Polyfills |
| 6 | Custom Promise | Implement your own minimal `Promise` class. | Promises / Internals |
| 7 | Execute async functions in Series | Run async tasks one by one. | Async Control Flow |
| 8 | Execute async functions in Parallel | Run async tasks concurrently. | Async Control Flow |
| 9 | Retry promises N number of times | Retry failed promises with limits. | Async Retry Logic |
| 10 | mapSeries async function | Process async items sequentially and map results. | Async Utilities |
| 11 | mapLimit async function | Run async tasks with a concurrency cap. | Async Utilities |
| 12 | async filter function | Filter asynchronously with predicate logic. | Async Utilities |
| 13 | async reject function | Reject/filter out items asynchronously. | Async Utilities |
| 14 | Execute promises with priority | Execute promises based on assigned priority. | Async Scheduling |
| 15 | Dependent async tasks | Chain async tasks that depend on previous results. | Async Control Flow |
| 16 | Pausable auto incrementor | Timer-based counter that can pause/resume. | Timers / Closures |
| 17 | Queue using stack | Implement queue data structure using two stacks. | Data Structures |
| 18 | Stack using queue | Implement stack using two queues. | Data Structures |
| 19 | Stack with min and max | Stack with real-time min/max tracking. | Data Structures |
| 20 | Two stacks with one array | Implement two stacks in a single array. | Data Structures |
| 21 | Priority Queue | Build a queue with element priorities. | Data Structures |
| 22 | LRU Cache | Implement Least Recently Used cache system. | Caching / Data Structures |
| 23 | Debounce function | Delay execution until input stabilizes. | Timing / Closures |
| 24 | Debounce (immediate flag) | Support immediate-start debounce calls. | Timing / Closures |
| 25 | Throttle function | Limit function calls to fixed intervals. | Timing / Closures |
| 26 | Custom Instanceof | Polyfill for JavaScript’s `instanceof`. | Language Mechanics |
| 27 | Detect new keyword | Check if function invoked via `new`. | Language Mechanics |
| 28 | HashSet | Simple unique-value storage system. | Data Structures |
| 29 | Toggle function | Function that alternates behavior/state. | Utilities |
| 30 | Sampling function | Randomly sample items from a dataset. | Utilities / Math |
| 31 | Sleep function | Pause async execution for given time. | Async Utilities |
| 32 | Remove cycle from object | Detect and remove circular references. | Objects / JSON |
| 33 | Filter multidimensional array | Filter nested arrays recursively. | Arrays |
| 34 | Count elements in multidimensional array | Count total elements in nested array. | Arrays |
| 35 | HEX → RGB | Convert hex color string to RGB. | String / Conversion |
| 36 | RGB → HEX | Convert RGB value to hex string. | String / Conversion |
| 37 | In-memory filesystem | Create virtual filesystem using JS objects. | Simulation / OOP |
| 38 | Streams API (basic) | Implement simplified version of streams. | Node.js Concepts |
| 39 | Memoizer function | Cache results of expensive computations. | Optimization / Closures |
| 40 | Method chaining (1) | Support chaining via method returns. | OOP / Functional |
| 41 | Method chaining (2) | Extend chaining with custom states. | OOP / Functional |
| 42 | clearAllTimeout | Cancel all active timeouts. | Timers |
| 43 | clearAllInterval | Cancel all active intervals. | Timers |
| 44 | Fake setTimeout | Simulate timer functionality manually. | Timers / Polyfills |
| 45 | Currying (1) | Implement currying for simple functions. | Functional Programming |
| 46 | Currying (2) | Extend currying with variable arguments. | Functional Programming |
| 47 | Currying (3) | Advanced curried function pipeline. | Functional Programming |
| 48 | Time → 24-hour format | Convert 12h clock time to 24h format. | String / Date |
| 49 | Time → 12-hour format | Convert 24h to 12h time with AM/PM. | String / Date |
| 50 | Digital clock | Create real-time updating clock display. | DOM / Timing |
| 51 | Chunk array | Split array into chunks of given size. | Arrays |
| 52 | Chunk string | Split string into equal-sized parts. | Strings |
| 53 | Deep flatten object | Recursively flatten nested object properties. | Objects |
| 54 | Restrict object modifications | Implement immutability like `Object.freeze()`. | Objects / Design |
| 55 | Merge objects | Merge multiple nested objects deeply. | Objects |
| 56 | Browser history | Simulate browser’s back/forward behavior. | Simulation / Stack |
| 57 | Singleton pattern | Restrict class to a single instance. | Design Patterns |
| 58 | Observer pattern | Publisher-subscriber system. | Design Patterns |
| 59 | groupBy() method | Group array items by computed key. | Arrays / Data |
| 60 | Compare arrays/objects | Perform deep equality comparison. | Objects / Comparison |
| 61 | Array iterator | Custom iterator supporting `next()`. | Iterators / ES6 |
| 62 | Array with event listeners | Extend Array to emit mutation events. | OOP / Reactive |
| 63 | Filter array of objects | Filter based on value or index. | Arrays |
| 64 | Aggregate array by key | Aggregate using specific key property. | Arrays / Data |
| 65 | Entity → ancestry tree | Convert flat list to nested tree structure. | Algorithms / Trees |
| 66 | Get object value from path | Access deep values via `'a.b.c'`. | Objects |
| 67 | Set object value from path | Set deep object values via string path. | Objects |
| 68 | JSON.stringify() polyfill | Implement serialization manually. | JSON / Polyfills |
| 69 | JSON.parse() polyfill | Parse JSON strings manually. | JSON / Polyfills |
| 70 | HTML encode string | Escape HTML entities safely. | Security / Strings |
| 71 | CSS selector generator | Generate unique CSS selector for an element. | DOM / CSS |
| 72 | Aggregate input values | Combine multiple numeric or text inputs. | Utilities |
| 73 | Fetch interceptors | Implement request/response hooks. | Networking / Fetch |
| 74 | Cache API call with expiry | Cache fetch results with expiration. | Networking / Caching |
| 75 | getElementsByClassName() polyfill | Manual DOM traversal to find class elements. | DOM / Polyfills |
| 76 | getElementsByClassNameHierarchy() polyfill | Hierarchical DOM class selector. | DOM / Polyfills |
| 77 | Find element by color | Search DOM elements by computed color. | DOM / CSS |
| 78 | Throttle an array of tasks | Control rate of async task execution. | Async Control |
| 79 | Decode string | Decode encoded text (e.g., base64 or unicode). | Strings |
| 80 | Trie data structure | Implement prefix tree for word search. | Data Structures |
| 81 | First & last index in sorted array | Find first and last occurrence efficiently. | Algorithms / Binary Search |
| 82 | Piping function (1) | Compose functions sequentially. | Functional Programming |
| 83 | Piping function (2) | Enhanced function pipeline system. | Functional Programming |
| 84 | Analytics SDK | Create a basic analytics tracking SDK. | SDK / Design |
| 85 | Check full binary tree | Verify if binary tree is complete/full. | Data Structures / Trees |
| 86 | Get height & width of binary tree | Compute structural dimensions of tree. | Data Structures / Trees |
| 87 | extend() polyfill | Implement `Object.extend` merging behavior. | Objects / Polyfills |
| 88 | Animate elements in sequence | Sequential animation of DOM nodes. | DOM / Animation |
| 89 | LocalStorage with expiry | Add TTL support to localStorage items. | Storage / Web APIs |
| 90 | Custom cookie handler | Manage cookies manually in JS. | Storage / Web APIs |
| 91 | Immutability helper (1) | Build helper for immutable updates. | State Management |
| 92 | Immutability helper (2) | Extend helper for nested immutability. | State Management |
| 93 | High-priority API call | Execute critical API calls with precedence. | Networking |
| 94 | Convert JSON → HTML | Render structured data into HTML. | Conversion / DOM |
| 95 | Convert HTML → JSON | Parse HTML into JSON representation. | Conversion / DOM |
| 96 | Concurrent history tracker | Track multiple navigation histories. | Simulation / History |
| 97 | In-memory search engine | Simple search with indexing logic. | Algorithms / Search |
| 98 | Fuzzy search function | Approximate text-matching algorithm. | Algorithms / Search |
| 99 | Cancel API request | Cancel fetch or XHR requests gracefully. | Networking |
| 100 | Highlight words in string | Highlight search terms in text. | Strings / UI Utilities |
