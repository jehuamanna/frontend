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
ax.text(8, 9.5, 'Mixin Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(8, 9.0, 'Composition Over Inheritance - Mix Behaviors into Objects/Classes',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= Inheritance vs Composition =============
ax.text(1, 8.2, 'Inheritance vs Mixin Composition:', fontsize=11, weight='bold')

# Inheritance (rigid hierarchy)
inherit_box = FancyBboxPatch((0.5, 6.2), 3.5, 1.8,
                             boxstyle="round,pad=0.1",
                             edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=2)
ax.add_patch(inherit_box)
ax.text(2.25, 7.85, 'Inheritance (Rigid)', fontsize=10, weight='bold', ha='center', color='#e74c3c')

inherit_diagram = """   Vehicle
      ↓
    Car
      ↓
  SportsCar

❌ Single parent
❌ Deep hierarchy
❌ Tight coupling"""
ax.text(0.7, 7.65, inherit_diagram, fontsize=7, ha='left', va='top')
ax.text(2.25, 6.4, 'Hard to change', fontsize=8, ha='center', style='italic', color='#e74c3c')

# Mixin (flexible composition)
mixin_box = FancyBboxPatch((4.5, 6.2), 3.5, 1.8,
                           boxstyle="round,pad=0.1",
                           edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=2)
ax.add_patch(mixin_box)
ax.text(6.25, 7.85, 'Mixin (Flexible)', fontsize=10, weight='bold', ha='center', color='#2ecc71')

mixin_diagram = """Movable + Flyable
      + Drawable
         ↓
     Airplane

✓ Multiple behaviors
✓ Flat structure
✓ Loose coupling"""
ax.text(4.7, 7.65, mixin_diagram, fontsize=7, ha='left', va='top')
ax.text(6.25, 6.4, 'Easy to change', fontsize=8, ha='center', style='italic', color='#2ecc71')

# ============= Mixin Composition Flow =============
ax.text(9, 8.2, 'Mixin Composition:', fontsize=11, weight='bold')

# Mixins (sources)
mixin1 = FancyBboxPatch((9, 7.2), 1.8, 0.7,
                        boxstyle="round,pad=0.05",
                        edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(mixin1)
ax.text(9.9, 7.75, 'Mixin A', fontsize=9, weight='bold', ha='center')
ax.text(9.9, 7.5, 'withLogging', fontsize=7, ha='center', family='monospace')

mixin2 = FancyBboxPatch((11.2, 7.2), 1.8, 0.7,
                        boxstyle="round,pad=0.05",
                        edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=1.5)
ax.add_patch(mixin2)
ax.text(12.1, 7.75, 'Mixin B', fontsize=9, weight='bold', ha='center')
ax.text(12.1, 7.5, 'withTimestamp', fontsize=7, ha='center', family='monospace')

mixin3 = FancyBboxPatch((13.4, 7.2), 1.8, 0.7,
                        boxstyle="round,pad=0.05",
                        edgecolor='#e67e22', facecolor='#fef5e7', linewidth=1.5)
ax.add_patch(mixin3)
ax.text(14.3, 7.75, 'Mixin C', fontsize=9, weight='bold', ha='center')
ax.text(14.3, 7.5, 'withEvents', fontsize=7, ha='center', family='monospace')

# Arrows down to target
arrow1 = FancyArrowPatch((9.9, 7.2), (11.5, 6.5),
                        arrowstyle='->', mutation_scale=15,
                        linewidth=2, color='#34495e')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((12.1, 7.2), (11.5, 6.5),
                        arrowstyle='->', mutation_scale=15,
                        linewidth=2, color='#34495e')
ax.add_patch(arrow2)

arrow3 = FancyArrowPatch((14.3, 7.2), (11.5, 6.5),
                        arrowstyle='->', mutation_scale=15,
                        linewidth=2, color='#34495e')
ax.add_patch(arrow3)

# Target object/class
target_box = FancyBboxPatch((9.5, 5.5), 4, 0.9,
                            boxstyle="round,pad=0.1",
                            edgecolor='#2ecc71', facecolor='#d5f4e6', linewidth=3)
ax.add_patch(target_box)
ax.text(11.5, 6.2, 'Target Class / Object', fontsize=10, weight='bold', ha='center')
ax.text(11.5, 5.85, 'class User extends compose(withLogging, withTimestamp, withEvents)', 
        fontsize=7, ha='center', family='monospace')

# Result
result_box = FancyBboxPatch((9.5, 4.5), 4, 0.8,
                            boxstyle="round,pad=0.05",
                            edgecolor='#27ae60', facecolor='#abebc6', linewidth=2)
ax.add_patch(result_box)
ax.text(11.5, 5.1, 'User has all methods from all mixins:', fontsize=8, weight='bold', ha='center')
ax.text(11.5, 4.85, 'user.log(), user.getTimestamp(), user.on(), user.emit()', 
        fontsize=7, ha='center', family='monospace')

# ============= Implementation Approaches =============
ax.text(0.5, 5.5, 'Implementation Approaches:', fontsize=11, weight='bold')

# Object.assign
approach1_box = FancyBboxPatch((0.5, 4.3), 3.5, 1.0,
                               boxstyle="round,pad=0.1",
                               edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(approach1_box)
ax.text(2.25, 5.15, '1. Object.assign', fontsize=9, weight='bold', ha='center')

approach1_code = """const obj = {};
Object.assign(obj, 
  mixinA, 
  mixinB
);"""
ax.text(0.7, 5.0, approach1_code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.text(2.25, 4.45, 'Simple, direct', fontsize=7, ha='center', style='italic', color='gray')

# Functional mixin
approach2_box = FancyBboxPatch((4.5, 4.3), 3.5, 1.0,
                               boxstyle="round,pad=0.1",
                               edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=1.5)
ax.add_patch(approach2_box)
ax.text(6.25, 5.15, '2. Functional Mixin', fontsize=9, weight='bold', ha='center')

approach2_code = """const withMixin = (obj) =>
  Object.assign(obj, {
    method() {}
  });"""
ax.text(4.7, 5.0, approach2_code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.text(6.25, 4.45, 'Factory pattern', fontsize=7, ha='center', style='italic', color='gray')

# Class mixin
approach3_box = FancyBboxPatch((0.5, 3.0), 3.5, 1.0,
                               boxstyle="round,pad=0.1",
                               edgecolor='#e67e22', facecolor='#fef5e7', linewidth=1.5)
ax.add_patch(approach3_box)
ax.text(2.25, 3.85, '3. Class Mixin (Subclass Factory)', fontsize=9, weight='bold', ha='center')

approach3_code = """const Mixin = (Base) =>
  class extends Base {
    method() {}
  };"""
ax.text(0.7, 3.7, approach3_code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.text(2.25, 3.15, 'ES6 classes, inheritance', fontsize=7, ha='center', style='italic', color='gray')

# Composition helper
approach4_box = FancyBboxPatch((4.5, 3.0), 3.5, 1.0,
                               boxstyle="round,pad=0.1",
                               edgecolor='#16a085', facecolor='#d5f5e3', linewidth=1.5)
ax.add_patch(approach4_box)
ax.text(6.25, 3.85, '4. Compose Helper', fontsize=9, weight='bold', ha='center')

approach4_code = """const compose = (...mixins) =>
  (Base) => mixins.reduce(
    (acc, m) => m(acc), Base
  );"""
ax.text(4.7, 3.7, approach4_code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.text(6.25, 3.15, 'Multiple mixins, clean', fontsize=7, ha='center', style='italic', color='gray')

# ============= Complete Example =============
ax.text(0.5, 2.5, 'Complete Example:', fontsize=11, weight='bold')

example_box = FancyBboxPatch((0.5, 0.3), 7.5, 2.0,
                             boxstyle="round,pad=0.1",
                             edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=1)
ax.add_patch(example_box)

example_code = """// Define mixins
const withLogging = (Base) => class extends Base {
  log(msg) { console.log(`[${this.constructor.name}] ${msg}`); }
};

const withTimestamp = (Base) => class extends Base {
  constructor(...args) {
    super(...args);
    this.createdAt = Date.now();
  }
  getAge() { return Date.now() - this.createdAt; }
};

// Compose helper
const compose = (...mixins) => (Base = class {}) =>
  mixins.reduce((acc, mixin) => mixin(acc), Base);

// Apply to class
class User extends compose(withLogging, withTimestamp)() {
  constructor(name) {
    super();
    this.name = name;
    this.log('Created');
  }
}

const user = new User('Alice');
user.log('Hello');           // [User] Hello
console.log(user.getAge());  // 123 (milliseconds since creation)"""

ax.text(0.7, 2.25, example_code, fontsize=6.5, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ============= Benefits & Use Cases =============
ax.text(8.5, 2.5, 'Benefits & Use Cases:', fontsize=11, weight='bold')

benefits_box = FancyBboxPatch((8.5, 1.2), 7, 1.1,
                              boxstyle="round,pad=0.1",
                              edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=1.5)
ax.add_patch(benefits_box)
ax.text(12, 2.2, 'Key Benefits', fontsize=10, weight='bold', ha='center')

benefits_text = """✓ Code Reuse: Share behavior across unrelated classes
✓ Composition: Combine multiple behaviors flexibly
✓ Avoid Diamond Problem: No inheritance conflicts
✓ Flexibility: Add/remove behaviors dynamically
✓ Multiple Inheritance: Simulate multiple inheritance"""

ax.text(8.7, 2.0, benefits_text, fontsize=7, ha='left', va='top')

use_cases_box = FancyBboxPatch((8.5, 0.3), 7, 0.7,
                               boxstyle="round,pad=0.05",
                               edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(use_cases_box)
ax.text(12, 0.9, 'Common Use Cases', fontsize=9, weight='bold', ha='center')
ax.text(8.7, 0.7, '• Event emitters  • Logging  • Serialization  • Validation  • Timestamps', 
        fontsize=7, ha='left')
ax.text(8.7, 0.5, '• Observable  • Disposable  • Clonable  • Comparable  • Iterable behaviors', 
        fontsize=7, ha='left')

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#eafaf1', edgecolor='#2ecc71', label='Mixin Composition'),
    mpatches.Patch(facecolor='#fadbd8', edgecolor='#e74c3c', label='Inheritance'),
    mpatches.Patch(facecolor='#ebf5fb', edgecolor='#3498db', label='Mixin A'),
    mpatches.Patch(facecolor='#f4ecf7', edgecolor='#9b59b6', label='Mixin B'),
    mpatches.Patch(facecolor='#fef5e7', edgecolor='#e67e22', label='Mixin C')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/mixin_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Mixin Pattern architecture diagram generated successfully")

