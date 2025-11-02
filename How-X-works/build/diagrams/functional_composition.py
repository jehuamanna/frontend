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
ax.text(8, 9.5, 'Functional Composition Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(8, 9.0, 'Combining Functions to Create Data Transformation Pipelines',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= Compose vs Pipe =============
ax.text(1, 8.2, 'Compose vs Pipe:', fontsize=11, weight='bold')

# Compose (right-to-left)
compose_box = FancyBboxPatch((0.5, 6.5), 3.5, 1.5,
                             boxstyle="round,pad=0.1",
                             edgecolor='#3498db', facecolor='#ebf5fb', linewidth=2)
ax.add_patch(compose_box)
ax.text(2.25, 7.85, 'compose (right-to-left)', fontsize=10, weight='bold', ha='center', color='#3498db')

compose_code = """compose(f, g, h)(x)
=  f(g(h(x)))

   f ← g ← h ← x
   3   2   1  (order)

Mathematical style"""
ax.text(0.7, 7.65, compose_code, fontsize=7, ha='left', va='top', family='monospace')

# Pipe (left-to-right)
pipe_box = FancyBboxPatch((4.5, 6.5), 3.5, 1.5,
                          boxstyle="round,pad=0.1",
                          edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=2)
ax.add_patch(pipe_box)
ax.text(6.25, 7.85, 'pipe (left-to-right)', fontsize=10, weight='bold', ha='center', color='#2ecc71')

pipe_code = """pipe(f, g, h)(x)
=  h(g(f(x)))

   x → f → g → h
       1   2   3  (order)

More readable"""
ax.text(4.7, 7.65, pipe_code, fontsize=7, ha='left', va='top', family='monospace')

# ============= Data Flow Visualization =============
ax.text(9, 8.2, 'Data Flow (Pipe):', fontsize=11, weight='bold')

# Input
input_circle = Circle((9.5, 7.4), 0.3, edgecolor='#27ae60', facecolor='#d5f4e6', linewidth=2)
ax.add_patch(input_circle)
ax.text(9.5, 7.4, 'x', fontsize=12, weight='bold', ha='center', va='center')
ax.text(9.5, 6.9, 'Input', fontsize=8, ha='center')

# Function 1
fn1_box = FancyBboxPatch((10.5, 7.1), 1, 0.6,
                         boxstyle="round,pad=0.05",
                         edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(fn1_box)
ax.text(11, 7.4, 'f(x)', fontsize=9, weight='bold', ha='center', va='center')

# Arrow 1
arrow1 = FancyArrowPatch((9.8, 7.4), (10.5, 7.4),
                        arrowstyle='->', mutation_scale=15,
                        linewidth=2, color='#34495e')
ax.add_patch(arrow1)

# Function 2
fn2_box = FancyBboxPatch((12, 7.1), 1, 0.6,
                         boxstyle="round,pad=0.05",
                         edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=1.5)
ax.add_patch(fn2_box)
ax.text(12.5, 7.4, 'g(…)', fontsize=9, weight='bold', ha='center', va='center')

# Arrow 2
arrow2 = FancyArrowPatch((11.5, 7.4), (12, 7.4),
                        arrowstyle='->', mutation_scale=15,
                        linewidth=2, color='#34495e')
ax.add_patch(arrow2)

# Function 3
fn3_box = FancyBboxPatch((13.5, 7.1), 1, 0.6,
                         boxstyle="round,pad=0.05",
                         edgecolor='#e67e22', facecolor='#fef5e7', linewidth=1.5)
ax.add_patch(fn3_box)
ax.text(14, 7.4, 'h(…)', fontsize=9, weight='bold', ha='center', va='center')

# Arrow 3
arrow3 = FancyArrowPatch((13, 7.4), (13.5, 7.4),
                        arrowstyle='->', mutation_scale=15,
                        linewidth=2, color='#34495e')
ax.add_patch(arrow3)

# Output
output_circle = Circle((15, 7.4), 0.3, edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=2)
ax.add_patch(output_circle)
ax.text(15, 7.4, 'y', fontsize=12, weight='bold', ha='center', va='center')
ax.text(15, 6.9, 'Output', fontsize=8, ha='center')

# Arrow 4
arrow4 = FancyArrowPatch((14.5, 7.4), (14.7, 7.4),
                        arrowstyle='->', mutation_scale=15,
                        linewidth=2, color='#34495e')
ax.add_patch(arrow4)

# ============= Problem Solution =============
ax.text(0.5, 5.8, 'Problem → Solution:', fontsize=11, weight='bold')

# Nested calls (problem)
problem_box = FancyBboxPatch((0.5, 4.5), 3.5, 1.1,
                             boxstyle="round,pad=0.1",
                             edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=2)
ax.add_patch(problem_box)
ax.text(2.25, 5.45, '❌ Nested Calls (Unreadable)', fontsize=9, weight='bold', ha='center', color='#e74c3c')

problem_code = """// Hard to read
const result = 
  format(
    validate(
      transform(
        sanitize(input)
      )
    )
  );"""
ax.text(0.7, 5.3, problem_code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Composition (solution)
solution_box = FancyBboxPatch((4.5, 4.5), 3.5, 1.1,
                              boxstyle="round,pad=0.1",
                              edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=2)
ax.add_patch(solution_box)
ax.text(6.25, 5.45, '✓ Composition (Clear)', fontsize=9, weight='bold', ha='center', color='#2ecc71')

solution_code = """// Clear data flow
const process = pipe(
  sanitize,
  transform,
  validate,
  format
);
const result = process(input);"""
ax.text(4.7, 5.3, solution_code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ============= Implementation =============
ax.text(9, 5.8, 'Implementation:', fontsize=11, weight='bold')

impl_box = FancyBboxPatch((9, 4.5), 6.5, 1.1,
                          boxstyle="round,pad=0.1",
                          edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(impl_box)

impl_code = """// compose: right-to-left
const compose = (...fns) =>
  input => fns.reduceRight((acc, fn) => fn(acc), input);

// pipe: left-to-right
const pipe = (...fns) =>
  input => fns.reduce((acc, fn) => fn(acc), input);"""

ax.text(9.2, 5.4, impl_code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ============= Example =============
ax.text(0.5, 4.0, 'Complete Example:', fontsize=11, weight='bold')

example_box = FancyBboxPatch((0.5, 0.3), 7.5, 3.5,
                             boxstyle="round,pad=0.1",
                             edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=1)
ax.add_patch(example_box)

example_code = """// Define small, focused functions
const toUpperCase = (str) => str.toUpperCase();
const exclaim = (str) => `${str}!`;
const trim = (str) => str.trim();
const split = (delimiter) => (str) => str.split(delimiter);
const reverse = (arr) => [...arr].reverse();
const join = (delimiter) => (arr) => arr.join(delimiter);

// Compose into pipeline
const shout = pipe(
  trim,
  toUpperCase,
  exclaim
);

console.log(shout('  hello world  ')); // "HELLO WORLD!"

// More complex: reverse words
const reverseWords = pipe(
  trim,
  split(' '),
  reverse,
  join(' ')
);

console.log(reverseWords('  Hello World from JS  '));
// "JS from World Hello"

// Array processing
const map = (fn) => (arr) => arr.map(fn);
const filter = (fn) => (arr) => arr.filter(fn);
const take = (n) => (arr) => arr.slice(0, n);

const processNumbers = pipe(
  filter(x => x % 2 === 0),
  map(x => x * 2),
  take(3)
);

console.log(processNumbers([1,2,3,4,5,6,7,8]));
// [4, 8, 12]"""

ax.text(0.7, 3.75, example_code, fontsize=6.5, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ============= Benefits =============
ax.text(8.5, 4.0, 'Key Benefits:', fontsize=11, weight='bold')

benefits_box = FancyBboxPatch((8.5, 2.0), 7, 1.8,
                              boxstyle="round,pad=0.1",
                              edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=1.5)
ax.add_patch(benefits_box)

benefits_text = """1. Reusability
   • Small functions, infinite combinations
   • Build complex from simple

2. Readability
   • Clear data flow (left-to-right with pipe)
   • Self-documenting pipelines

3. Testability
   • Test small functions independently
   • Easy to isolate and verify

4. Maintainability
   • Add/remove/reorder steps easily
   • Change one function without affecting others

5. Declarative Style
   • Describe what, not how
   • Focus on transformations, not implementation"""

ax.text(8.7, 3.7, benefits_text, fontsize=7, ha='left', va='top')

# ============= Use Cases =============
ax.text(8.5, 1.6, 'Common Use Cases:', fontsize=11, weight='bold')

use_cases_box = FancyBboxPatch((8.5, 0.3), 7, 1.1,
                               boxstyle="round,pad=0.05",
                               edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=1.5)
ax.add_patch(use_cases_box)

use_cases = """• Data transformation pipelines (ETL)
• Form validation & sanitization
• String manipulation & parsing
• Array/collection processing
• Async workflows (promises)
• Middleware chains (Express, Redux)
• State transformations (reducers)
• Functional utilities (Ramda, Lodash/fp)"""

ax.text(8.7, 1.3, use_cases, fontsize=7, ha='left', va='top')

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#ebf5fb', edgecolor='#3498db', label='Function 1'),
    mpatches.Patch(facecolor='#f4ecf7', edgecolor='#9b59b6', label='Function 2'),
    mpatches.Patch(facecolor='#fef5e7', edgecolor='#e67e22', label='Function 3'),
    mpatches.Patch(facecolor='#d5f4e6', edgecolor='#27ae60', label='Input'),
    mpatches.Patch(facecolor='#fadbd8', edgecolor='#e74c3c', label='Output')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/functional_composition.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Functional Composition architecture diagram generated successfully")


