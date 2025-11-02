<!-- SONNET CONTINUATION TEMPLATE HEADER - DO NOT REMOVE -->

# Sonnet Continuation Template
A ready-to-use continuation protocol for **Sonnet 4.5** (or similar LLMs) to generate long-form documentation **until completion**.


---

## 1. Master Directive (Paste at top of every Sonnet prompt)
```
# SONNET MASTER DIRECTIVE

You are generating comprehensive technical documentation for all JavaScript & Browser Design Patterns
based on the provided scaffolding file `javascript_patterns_full_instruction.md`.

CRITICAL CONTINUATION RULES:
- Continue automatically until every pattern in the checklist is documented in full depth.
- If you reach the response or token limit, **you must** output a single CONTINUATION MARKER at the end and stop. The next input will instruct you to resume.
- When continuing, never repeat previously completed sections; only output the next section(s) sequentially.
- Each generated segment MUST begin with:
  ## CONTINUED: [Category] — [Pattern Name]
- Each generated segment MUST end with:
  --- [CONTINUE FROM HERE: <Next Pattern Name>] ---
- For each pattern output, include the exact structure:
  1. Concept Overview
  2. Problem It Solves
  3. Detailed Implementation (ESNext code)
  4. Browser/DOM Usage
  5. Python Architecture Diagram Snippet (file path & code)
  6. Real-world Use Cases
  7. Performance & Trade-offs
  8. Related Patterns
  9. RFC-style Summary (table)

DEPTH REQUIREMENTS:
- Each pattern should be at least 200–600 words plus code examples and one Python diagram snippet.
- Keep code clear, runnable, and idiomatic ESNext.
- Python diagram snippets should use matplotlib/networkx and save PNG to ./docs/images/<pattern_slug>.png

SAFETY & FORMAT:
- Use fenced code blocks for code and python.
- Do not include external links unless asked.
- Do not summarize previously generated content; only continue with new content.
```

---

## 2. Continuation Marker Protocol
When Sonnet hits its token/response limit, it must end the current message with **only** the following marker (no extra prose):

```
--- [CONTINUE FROM HERE: <next pattern name>] ---
```

Example:
```
--- [CONTINUE FROM HERE: Builder Pattern] ---
```

You (or an automation script) will feed that marker back to Sonnet along with the master directive to continue.

---

## 3. Example "Continue" Prompt (what you send next)
When you receive the continuation marker, send Sonnet a short prompt like:

```
# CONTINUE REQUEST
Refer to the previous output and the SONNET MASTER DIRECTIVE.
Continue from the marker:
--- [CONTINUE FROM HERE: Builder Pattern] ---
Do not recap. Begin with:
## CONTINUED: Creational — Builder Pattern
```

If you prefer batching, you can ask Sonnet to "continue until the end of the Creational category" with this same continuation protocol — but still require markers if token limits are reached.

---

## 4. Supervisor / Progress File (progress.json)
Maintain a small JSON to track completed patterns:

```json
{
  "Creational": {
    "Constructor Pattern": "revise-again",
    "Factory Pattern": "revise-again",
    "Abstract Factory Pattern": "revise-again",
    "Builder Pattern": "revise-again",
    "Prototype Pattern": "revise-again",
    "Singleton Pattern": "revise-again",
    "Object Pool Pattern": "revise-again"
  },
  "Structural": {
    "Adapter Pattern": "revise-again",
    "Bridge Pattern": "revise-again"
    // ...
  }
}
```

Update each entry to `"done"` when Sonnet outputs the finalized section.

---

## 5. Recommended Automation Script (Python pseudocode)
Use this to loop through checklist and re-feed Sonnet until all patterns are done.

```python
# pseudocode - adapt to your API
import json
from sonnet_api import SonnetClient  # replace with real client

client = SonnetClient(api_key="...")

with open("progress.json") as f:
    progress = json.load(f)

master_directive = open("Sonnet_continuation_template.md").read()
scaffolding = open("javascript_patterns_full_instruction.md").read()

def find_next_pending(progress):
    for cat, patterns in progress.items():
        for name, status in patterns.items():
            if status == "pending":
                return cat, name
    return None, None

while True:
    cat, pattern = find_next_pending(progress)
    if not cat:
        print("All done")
        break

    prompt = f"""{master_directive}

# TASK
Start documentation for: {pattern}
Use the scaffolding file for context:
{scaffolding}

Begin output now.
"""
    resp = client.generate(prompt, max_tokens=8000)
    save_to_file(cat, pattern, resp.text)
    # If response ends with continuation marker, extract marker and re-run loop with a CONTINUE request
    if "--- [CONTINUE FROM HERE:" in resp.text:
        # leave pattern as pending until you verify finality
        continue
    else:
        progress[cat][pattern] = "done"
        with open("progress.json","w") as f:
            json.dump(progress, f, indent=2)
```

---

## 6. Example Section Template (what Sonnet should produce)
Use this exact template so outputs are uniform and machine-parseable.

```
## CONTINUED: Creational — Constructor Pattern

### Concept Overview
[200–600 words]

### Problem It Solves
[...]

### Detailed Implementation
```js
// runnable ESNext code
```

### Browser / DOM Usage
[...]

### Python Architecture Diagram Snippet
```python
# ./build/diagrams/constructor_pattern.py
import matplotlib.pyplot as plt
import networkx as nx
# ...
plt.savefig("docs/images/constructor_pattern.png")
```

### Real-world Use Cases
[...]

### Performance & Trade-offs
[...]

### Related Patterns
[...]

### RFC-style Summary
| Field | Description |
|-------|-------------|
| Pattern | Constructor Pattern |
| Category | Creational |
| Use Case | ... |
```

Each finished section should be appended to `master_output.md` and the `progress.json` should be updated.

---

## 7. Handling Edge Cases & Quality Control
- **If Sonnet repeats content:** reject the output and resend the last prompt with `REJECT: duplicate` to force a fresh attempt.
- **If Sonnet misses a required subsection:** send a targeted follow-up: `Add subsection: "Performance & Trade-offs" for [pattern name].`
- **If Sonnet output is low quality:** request `REFINE: increase depth and add code examples` with the previously generated content included.

---

## 8. Suggested Initial Prompt (copy/paste)
```
# START
SONNET MASTER DIRECTIVE (above) applies.
Scaffolding file: javascript_patterns_full_instruction.md
Begin with first pending pattern:
Creational — Constructor Pattern

Produce a complete section following the Example Section Template.
If you reach the token limit, end ONLY with:
--- [CONTINUE FROM HERE: <next pattern name>] ---
```

---

## 9. Quick Checklist to Track Execution
- [ ] Prepare `javascript_patterns_full_instruction.md`
- [ ] Prepare `Sonnet_continuation_template.md` (this file)
- [ ] Initialize `progress.json` with all patterns marked "pending"
- [ ] Start Sonnet with the START prompt
- [ ] Re-feed continuation markers until all sections show `"done"`
- [ ] Merge into `master_output.md` and run final style pass

---

## 10. Notes & Best Practices
- Keep prompts concise but explicit.
- Save state locally (`progress.json`) so you can resume if a run fails.
- Use a small validation script that checks each generated section includes required headings.
- Consider generating one category at a time to keep context manageable.

---

# End of Template


---

# 🧭 Sonnet 4.5 — JavaScript & Browser Design Patterns Documentation Scaffolding

> **Purpose:** This file provides full scaffolding for documenting **JavaScript, DOM, and Browser Design Patterns** with deep explanations, examples, and visual diagrams (generated by Python during build).  
> Each pattern section below is preformatted for **Sonnet 4.5** to fill in automatically.

---

## 🧱 1. Creational Design Patterns
Focus: Object creation mechanisms — how objects are instantiated and composed.

### Checklist
- [ ] Constructor Pattern
- [ ] Factory Pattern
- [ ] Abstract Factory Pattern
- [ ] Builder Pattern
- [ ] Prototype Pattern
- [ ] Singleton Pattern
- [ ] Object Pool Pattern

---

### 🧩 Pattern: Constructor Pattern
> Category: Creational

#### Concept Overview
Defines a blueprint for object creation using the `new` keyword or class syntax.

#### Problem It Solves
Creating many similar objects with shared properties and behavior.

#### Implementation
```js
class User {
  constructor(name, role) {
    this.name = name;
    this.role = role;
  }
}
const admin = new User("Alice", "Admin");
```

#### Browser / DOM Use Case
DOM constructors like `new Date()`, `new Error()`.

#### Diagram
`![Constructor Pattern](./images/constructor_pattern.png)`

#### Real-World Use
React class components, native constructors.

---

### 🧩 Pattern: Factory Pattern
> Category: Creational

#### Concept Overview
Creates objects without specifying their exact type or class.

#### Problem It Solves
Need to generate related objects without tight coupling to specific classes.

#### Implementation
```js
function elementFactory(type, text) {
  const el = document.createElement(type);
  el.textContent = text;
  return el;
}
```

#### Use Case
`document.createElement()`, UI component factories.

---

### 🧩 Pattern: Abstract Factory Pattern
> Category: Creational

#### Concept Overview
Factory of factories — creates related object families without specifying concrete classes.

#### Implementation
```js
function themeFactory(theme) {
  return {
    createButton: () => new Button(theme),
    createCard: () => new Card(theme),
  };
}
```

#### Example
UI kits generating components by theme.

---

### 🧩 Pattern: Builder Pattern
> Category: Creational

#### Concept Overview
Separates construction of a complex object from its representation.

#### Implementation
```js
class QueryBuilder {
  constructor() { this.query = ""; }
  select(fields) { this.query += `SELECT ${fields}`; return this; }
  from(table) { this.query += ` FROM ${table}`; return this; }
  build() { return this.query; }
}
```

#### Use Case
Fluent APIs, query builders (Knex.js).

---

### 🧩 Pattern: Prototype Pattern
> Category: Creational

#### Concept Overview
Clone objects based on a prototype.

#### Implementation
```js
const prototype = { greet() { return `Hi, I'm ${this.name}`; } };
const user = Object.create(prototype);
user.name = "Alice";
```

---

### 🧩 Pattern: Singleton Pattern
> Category: Creational

#### Concept Overview
Ensures one instance exists globally.

#### Implementation
```js
const AppConfig = (function() {
  let instance;
  function init() { return { env: "production" }; }
  return { getInstance: () => instance || (instance = init()) };
})();
```

---

### 🧩 Pattern: Object Pool Pattern
> Category: Creational

#### Concept Overview
Reuses initialized objects instead of creating/destroying repeatedly.

#### Implementation
```js
class ObjectPool {
  constructor(createFn) { this.pool = []; this.create = createFn; }
  acquire() { return this.pool.pop() || this.create(); }
  release(obj) { this.pool.push(obj); }
}
```

---

## 🏗️ 2. Structural Design Patterns
Focus: Object composition — combining classes to form larger systems.

### Checklist
- [ ] Adapter Pattern
- [ ] Bridge Pattern
- [ ] Composite Pattern
- [ ] Decorator Pattern
- [ ] Facade Pattern
- [ ] Flyweight Pattern
- [ ] Proxy Pattern

---

### 🧩 Pattern: Adapter Pattern
> Category: Structural

Adapts one API to another expected interface.

Example:
```js
class LegacyAPI { getData() { return "old"; } }
class ModernAdapter {
  constructor(legacy) { this.legacy = legacy; }
  fetch() { return this.legacy.getData(); }
}
```

---

### 🧩 Pattern: Proxy Pattern
> Category: Structural

Controls access to another object, e.g., caching or validation.

```js
const api = new Proxy({}, {
  get(_, prop) { console.log("Accessing", prop); return fetch(prop); }
});
```

Used in: API interceptors, lazy loading, caching layers.

---

## 🎭 3. Behavioral Design Patterns
Focus: Object interaction and delegation.

### Checklist
- [ ] Chain of Responsibility
- [ ] Command
- [ ] Iterator
- [ ] Mediator
- [ ] Memento
- [ ] Observer
- [ ] Pub/Sub
- [ ] State
- [ ] Strategy
- [ ] Template Method
- [ ] Visitor
- [ ] Interpreter

---

### 🧩 Pattern: Observer Pattern
> Category: Behavioral

One-to-many dependency where subjects notify observers.

```js
class Subject {
  constructor() { this.observers = []; }
  subscribe(fn) { this.observers.push(fn); }
  notify(data) { this.observers.forEach(fn => fn(data)); }
}
```

Used in DOM Events, RxJS, MobX.

---

### 🧩 Pattern: Chain of Responsibility
Pass requests along a sequence of handlers until one processes it.

Used in: Express.js middleware, event pipelines.

---

### 🧩 Pattern: Command Pattern
Encapsulates actions for undo/redo systems.

---

## 🏛️ 4. Architectural / High-Level Patterns
Focus: Large-scale application architecture.

### Checklist
- [ ] MVC
- [ ] MVP
- [ ] MVVM
- [ ] Flux
- [ ] Redux
- [ ] CQRS
- [ ] Event Sourcing
- [ ] Micro-Frontend
- [ ] Service Locator
- [ ] Dependency Injection

---

### 🧩 Pattern: Flux Pattern
> Category: Architectural

Unidirectional data flow architecture.

```
Actions → Dispatcher → Store → View
```

Example: React + Flux, Redux.

---

## ⚙️ 5. Concurrency & Reactive Patterns
Focus: Asynchronous behavior and reactive systems.

### Checklist
- [ ] Reactor Pattern
- [ ] Scheduler Pattern
- [ ] Promise Pattern
- [ ] Observer (Reactive Streams)
- [ ] Actor Model
- [ ] Async Iterator Pattern
- [ ] Pipeline Pattern

---

### 🧩 Pattern: Signal Pattern
> Category: Reactive

Fine-grained reactive dataflow pattern.

```js
class Signal {
  constructor(value) { this.value = value; this.subs = new Set(); }
  get() { Signal.active && this.subs.add(Signal.active); return this.value; }
  set(v) { this.value = v; this.subs.forEach(fn => fn()); }
}
```

Used in SolidJS, spreadsheet reactivity.

---

## 🧩 Bonus: JavaScript-Specific / Language Idioms

### Checklist
- [ ] Module Pattern
- [ ] Revealing Module Pattern
- [ ] Mixin Pattern
- [ ] Functional Composition
- [ ] Currying / Partial Application
- [ ] Null Object Pattern

---

### 🧩 Pattern: Module Pattern
Encapsulates private variables and exposes public API.

```js
const Counter = (function() {
  let count = 0;
  return { inc: () => ++count, val: () => count };
})();
```

---

### 🧩 Pattern: Currying / Partial Application
Transforms functions into unary sequences.

```js
const add = a => b => a + b;
add(2)(3); // 5
```

---

## 📈 Progress Tracking

| Category | Total | Completed | % |
|-----------|--------|-----------|--|
| Creational | 7 | 0 | 0% |
| Structural | 7 | 0 | 0% |
| Behavioral | 12 | 0 | 0% |
| Architectural | 10 | 0 | 0% |
| Reactive | 7 | 0 | 0% |
| JS Idioms | 6 | 0 | 0% |
| **Total** | **49** | **0** | **0%** |

---

### Build Step
```bash
python ./build/diagrams/*.py
```

Each Python script generates architecture diagrams for the relevant pattern.

---
