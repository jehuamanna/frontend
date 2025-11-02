import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(8, 9.5, 'Currying & Partial Application Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(8, 9.0, 'Transform Multi-Argument Functions into Specialized Versions',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= Currying vs Partial Application =============
ax.text(1, 8.2, 'Currying vs Partial Application:', fontsize=11, weight='bold')

# Normal function
normal_box = FancyBboxPatch((0.5, 7.2), 2.5, 0.8,
                            boxstyle="round,pad=0.05",
                            edgecolor='#95a5a6', facecolor='#ecf0f1', linewidth=1.5)
ax.add_patch(normal_box)
ax.text(1.75, 7.75, 'Normal Function', fontsize=9, weight='bold', ha='center')
ax.text(1.75, 7.45, 'add(a, b, c)', fontsize=8, ha='center', family='monospace')

# Currying
curry_box = FancyBboxPatch((3.5, 7.2), 2.5, 0.8,
                           boxstyle="round,pad=0.05",
                           edgecolor='#3498db', facecolor='#ebf5fb', linewidth=2)
ax.add_patch(curry_box)
ax.text(4.75, 7.75, 'Currying', fontsize=9, weight='bold', ha='center', color='#3498db')
ax.text(4.75, 7.45, 'add(a)(b)(c)', fontsize=8, ha='center', family='monospace')

# Partial Application
partial_box = FancyBboxPatch((6.5, 7.2), 2.5, 0.8,
                             boxstyle="round,pad=0.05",
                             edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=2)
ax.add_patch(partial_box)
ax.text(7.75, 7.75, 'Partial Application', fontsize=9, weight='bold', ha='center', color='#2ecc71')
ax.text(7.75, 7.45, 'add(10, b, c)', fontsize=8, ha='center', family='monospace')

# ============= Currying Flow =============
ax.text(10, 8.2, 'Currying Flow:', fontsize=11, weight='bold')

# Step 1
step1_box = FancyBboxPatch((10, 7.5), 1.5, 0.5,
                           boxstyle="round,pad=0.05",
                           edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(step1_box)
ax.text(10.75, 7.75, 'add(1)', fontsize=8, weight='bold', ha='center', family='monospace')

arrow1 = FancyArrowPatch((11.5, 7.75), (12, 7.75),
                        arrowstyle='->', mutation_scale=12,
                        linewidth=1.5, color='#34495e')
ax.add_patch(arrow1)

# Step 2
step2_box = FancyBboxPatch((12, 7.5), 1.5, 0.5,
                           boxstyle="round,pad=0.05",
                           edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=1.5)
ax.add_patch(step2_box)
ax.text(12.75, 7.75, '(2)', fontsize=8, weight='bold', ha='center', family='monospace')

arrow2 = FancyArrowPatch((13.5, 7.75), (14, 7.75),
                        arrowstyle='->', mutation_scale=12,
                        linewidth=1.5, color='#34495e')
ax.add_patch(arrow2)

# Step 3
step3_box = FancyBboxPatch((14, 7.5), 1.5, 0.5,
                           boxstyle="round,pad=0.05",
                           edgecolor='#e67e22', facecolor='#fef5e7', linewidth=1.5)
ax.add_patch(step3_box)
ax.text(14.75, 7.75, '(3)', fontsize=8, weight='bold', ha='center', family='monospace')

# Result
ax.text(12.75, 7.2, '→ 6', fontsize=9, ha='center', style='italic', color='#27ae60', weight='bold')

# ============= Detailed Comparison =============
ax.text(0.5, 6.5, 'Detailed Comparison:', fontsize=11, weight='bold')

# Currying detailed
curry_detail_box = FancyBboxPatch((0.5, 4.8), 3.8, 1.5,
                                  boxstyle="round,pad=0.1",
                                  edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(curry_detail_box)
ax.text(2.4, 6.15, 'Currying', fontsize=10, weight='bold', ha='center', color='#3498db')

curry_detail = """• Transforms to N unary functions
• Each call takes 1 argument
• Returns function until all args

// Example
const add = a => b => c =>
  a + b + c;

add(1)(2)(3); // 6

// Create specialized
const add1 = add(1);
const add1And2 = add1(2);
add1And2(3); // 6"""

ax.text(0.7, 6.0, curry_detail, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Partial Application detailed
partial_detail_box = FancyBboxPatch((4.8, 4.8), 3.8, 1.5,
                                    boxstyle="round,pad=0.1",
                                    edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=1.5)
ax.add_patch(partial_detail_box)
ax.text(6.7, 6.15, 'Partial Application', fontsize=10, weight='bold', ha='center', color='#2ecc71')

partial_detail = """• Fix some arguments
• Returns function for rest
• Flexible argument fixing

// Example
const partial = (fn, ...args) =>
  (...rest) => fn(...args, ...rest);

const add = (a,b,c) => a+b+c;
const add10 = partial(add, 10);

add10(5, 2); // 17

// Fix any position
partial(add, _, 5, _)(10, 3)"""

ax.text(5.0, 6.0, partial_detail, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ============= Use Cases =============
ax.text(9, 6.5, 'Common Use Cases:', fontsize=11, weight='bold')

use_cases_box = FancyBboxPatch((9, 4.8), 6.5, 1.5,
                               boxstyle="round,pad=0.1",
                               edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=1.5)
ax.add_patch(use_cases_box)

use_cases = """1. Function Specialization
   const greet = greeting => name => `${greeting}, ${name}!`;
   const sayHello = greet('Hello');
   sayHello('Alice'); // "Hello, Alice!"

2. Configuration
   const log = prefix => level => msg => console.log(`[${prefix}] [${level}] ${msg}`);
   const appLog = log('APP');
   const appError = appLog('ERROR');
   appError('Failed'); // [APP] [ERROR] Failed

3. Composition
   const map = fn => arr => arr.map(fn);
   const filter = pred => arr => arr.filter(pred);
   const process = pipe(filter(isEven), map(double));

4. Event Handlers
   const on = event => el => handler => el.addEventListener(event, handler);
   const onClick = on('click');
   onClick(button)(() => console.log('Clicked'));"""

ax.text(9.2, 6.3, use_cases, fontsize=6.5, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ============= Example =============
ax.text(0.5, 4.2, 'Complete Example:', fontsize=11, weight='bold')

example_box = FancyBboxPatch((0.5, 0.3), 15, 3.7,
                             boxstyle="round,pad=0.1",
                             edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=1)
ax.add_patch(example_box)

example_code = """// Auto-curry function
const curry = (fn) => {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    }
    return (...nextArgs) => curried.apply(this, args.concat(nextArgs));
  };
};

// Example function
function add(a, b, c) {
  return a + b + c;
}

const curriedAdd = curry(add);

// All at once
curriedAdd(1, 2, 3);        // 6

// One at a time
curriedAdd(1)(2)(3);        // 6

// Mixed
curriedAdd(1, 2)(3);        // 6
curriedAdd(1)(2, 3);        // 6

// Create specialized functions
const add10 = curriedAdd(10);
add10(5, 2);                 // 17
add10(3)(4);                 // 17

// Partial application
const partial = (fn, ...fixedArgs) =>
  (...remainingArgs) => fn(...fixedArgs, ...remainingArgs);

function greet(greeting, punctuation, name) {
  return `${greeting}, ${name}${punctuation}`;
}

const sayHello = partial(greet, 'Hello', '!');
sayHello('Alice');           // "Hello, Alice!"

// Use in composition
const map = fn => arr => arr.map(fn);
const filter = pred => arr => arr.filter(pred);

const double = map(x => x * 2);
const isEven = filter(x => x % 2 === 0);

const processNumbers = pipe(isEven, double);
processNumbers([1,2,3,4,5,6]);  // [4, 8, 12]"""

ax.text(0.7, 3.95, example_code, fontsize=6.5, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#ebf5fb', edgecolor='#3498db', label='Currying'),
    mpatches.Patch(facecolor='#eafaf1', edgecolor='#2ecc71', label='Partial Application'),
    mpatches.Patch(facecolor='#f4ecf7', edgecolor='#9b59b6', label='Use Cases'),
    mpatches.Patch(facecolor='#ecf0f1', edgecolor='#95a5a6', label='Normal Function')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/currying_partial_application.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Currying / Partial Application architecture diagram generated successfully")


