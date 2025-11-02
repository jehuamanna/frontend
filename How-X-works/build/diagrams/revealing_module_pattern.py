import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(8, 9.5, 'Revealing Module Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(8, 9.0, 'All Private, Then Explicitly Reveal Public API',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= Pattern Comparison =============
ax.text(1, 8.2, 'Comparison: Module vs Revealing Module', fontsize=11, weight='bold')

# Module Pattern (left)
module_box = FancyBboxPatch((0.5, 6.2), 3.5, 1.8,
                            boxstyle="round,pad=0.1",
                            edgecolor='#e67e22', facecolor='#fef5e7', linewidth=2)
ax.add_patch(module_box)
ax.text(2.25, 7.85, 'Module Pattern', fontsize=10, weight='bold', ha='center', color='#e67e22')

module_code = """(function() {
  let private = 1;
  
  return {
    public() {
      // defined here
    }
  };
})();"""
ax.text(0.7, 7.65, module_code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.text(2.25, 6.4, '❌ Mixed styles', fontsize=8, ha='center', style='italic', color='#e67e22')

# Revealing Module Pattern (right)
revealing_box = FancyBboxPatch((4.5, 6.2), 3.5, 1.8,
                               boxstyle="round,pad=0.1",
                               edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=2)
ax.add_patch(revealing_box)
ax.text(6.25, 7.85, 'Revealing Module', fontsize=10, weight='bold', ha='center', color='#2ecc71')

revealing_code = """(function() {
  let private = 1;
  
  function public() {
    // defined here
  }
  
  return { public };
})();"""
ax.text(4.7, 7.65, revealing_code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.text(6.25, 6.4, '✓ Consistent style', fontsize=8, ha='center', style='italic', color='#2ecc71')

# ============= Detailed Structure =============
ax.text(9, 8.2, 'Revealing Module Structure:', fontsize=11, weight='bold')

# IIFE wrapper
iife_box = FancyBboxPatch((9, 4.8), 6.5, 3.2,
                          boxstyle="round,pad=0.15",
                          edgecolor='#34495e', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(iife_box)
ax.text(12.25, 7.85, 'IIFE (function() { ... })()', 
        fontsize=9, weight='bold', ha='center', family='monospace')

# Private definitions (all defined the same way)
private_defs = FancyBboxPatch((9.3, 5.8), 5.9, 1.8,
                              boxstyle="round,pad=0.1",
                              edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=1.5)
ax.add_patch(private_defs)
ax.text(12.25, 7.45, 'All Defined as Private (Consistent)', 
        fontsize=9, weight='bold', ha='center')

private_code = """let count = 0;

function privateHelper() { /* ... */ }

function publicMethod1() { /* ... */ }

function publicMethod2() { /* ... */ }"""
ax.text(9.5, 7.3, private_code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Return statement (revealing)
return_box = FancyBboxPatch((9.3, 5.0), 5.9, 0.6,
                            boxstyle="round,pad=0.05",
                            edgecolor='#2ecc71', facecolor='#d5f4e6', linewidth=2)
ax.add_patch(return_box)
ax.text(12.25, 5.5, 'Reveal Public API', 
        fontsize=9, weight='bold', ha='center', color='#2ecc71')
ax.text(12.25, 5.2, 'return { publicMethod1, publicMethod2 };', 
        fontsize=8, ha='center', family='monospace')

# Arrows showing what's revealed
arrow1 = FancyArrowPatch((10.5, 6.5), (10.5, 5.6),
                        arrowstyle='->', mutation_scale=15,
                        linewidth=2, color='#2ecc71', linestyle='dashed')
ax.add_patch(arrow1)
ax.text(10.1, 6.0, 'revealed', fontsize=7, ha='right', style='italic', color='#2ecc71')

arrow2 = FancyArrowPatch((14, 6.5), (14, 5.6),
                        arrowstyle='->', mutation_scale=15,
                        linewidth=2, color='#2ecc71', linestyle='dashed')
ax.add_patch(arrow2)
ax.text(14.4, 6.0, 'revealed', fontsize=7, ha='left', style='italic', color='#2ecc71')

# Not revealed
ax.text(11.8, 6.0, 'NOT revealed ✗', fontsize=7, ha='center', 
        style='italic', color='#e74c3c', weight='bold')

# ============= Key Benefits =============
ax.text(0.5, 5.5, 'Key Benefits:', fontsize=11, weight='bold')

benefit1_box = FancyBboxPatch((0.5, 4.6), 3.5, 0.7,
                              boxstyle="round,pad=0.05",
                              edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(benefit1_box)
ax.text(2.25, 5.15, '1. Consistency', fontsize=9, weight='bold', ha='center')
ax.text(0.7, 4.95, 'All functions defined the same way', fontsize=7, ha='left')
ax.text(0.7, 4.75, '(private by default, same syntax)', fontsize=7, ha='left', style='italic', color='gray')

benefit2_box = FancyBboxPatch((4.5, 4.6), 3.5, 0.7,
                              boxstyle="round,pad=0.05",
                              edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(benefit2_box)
ax.text(6.25, 5.15, '2. Clarity', fontsize=9, weight='bold', ha='center')
ax.text(4.7, 4.95, 'Public API clearly visible at bottom', fontsize=7, ha='left')
ax.text(4.7, 4.75, '(single return statement)', fontsize=7, ha='left', style='italic', color='gray')

benefit3_box = FancyBboxPatch((0.5, 3.6), 3.5, 0.7,
                              boxstyle="round,pad=0.05",
                              edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(benefit3_box)
ax.text(2.25, 4.15, '3. Aliasing', fontsize=9, weight='bold', ha='center')
ax.text(0.7, 3.95, 'Can expose with different names:', fontsize=7, ha='left')
ax.text(0.7, 3.75, 'return { publicName: privateName };', fontsize=7, ha='left', family='monospace')

benefit4_box = FancyBboxPatch((4.5, 3.6), 3.5, 0.7,
                              boxstyle="round,pad=0.05",
                              edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(benefit4_box)
ax.text(6.25, 4.15, '4. Direct Calls', fontsize=9, weight='bold', ha='center')
ax.text(4.7, 3.95, 'No need for "this" references:', fontsize=7, ha='left')
ax.text(4.7, 3.75, 'publicMethod1() calls publicMethod2()', fontsize=7, ha='left', family='monospace')

# ============= Complete Example =============
ax.text(0.5, 3.2, 'Complete Example:', fontsize=11, weight='bold')

example_box = FancyBboxPatch((0.5, 0.3), 7.5, 2.7,
                             boxstyle="round,pad=0.1",
                             edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=1)
ax.add_patch(example_box)

example_code = """const counterModule = (function() {
  // ===== All defined as private (consistent style) =====
  let count = 0;
  
  function logChange(oldValue, newValue) {
    console.log(`Count: ${oldValue} → ${newValue}`);
  }
  
  function increment() {
    const oldCount = count;
    count++;
    logChange(oldCount, count); // Direct call (no 'this')
  }
  
  function decrement() {
    const oldCount = count;
    count--;
    logChange(oldCount, count);
  }
  
  function getCount() {
    return count;
  }
  
  function reset() {
    count = 0;
    console.log('Counter reset');
  }
  
  // ===== Reveal public API (single place) =====
  return {
    increment,  // expose increment
    decrement,  // expose decrement
    getCount,   // expose getCount
    reset       // expose reset
    // logChange remains private (not revealed)
  };
})();

// Usage
counterModule.increment();        // ✓ Works
counterModule.getCount();          // ✓ Returns 1
counterModule.logChange();         // ✗ Error (private)"""

ax.text(0.7, 2.95, example_code, fontsize=6.5, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ============= Aliasing Example =============
ax.text(8.5, 3.2, 'Aliasing Example:', fontsize=11, weight='bold')

alias_box = FancyBboxPatch((8.5, 1.5), 7, 1.5,
                           boxstyle="round,pad=0.1",
                           edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=1.5)
ax.add_patch(alias_box)
ax.text(12, 2.85, 'Expose with Different Names', fontsize=10, weight='bold', ha='center')

alias_code = """const mathModule = (function() {
  // Private implementations (verbose names)
  function addTwoNumbers(a, b) { return a + b; }
  function subtractTwoNumbers(a, b) { return a - b; }
  
  // Reveal with cleaner public names
  return {
    add: addTwoNumbers,        // alias
    subtract: subtractTwoNumbers  // alias
  };
})();

// Usage with clean names
mathModule.add(2, 3);         // ✓ 5
mathModule.addTwoNumbers();   // ✗ Error (private name)"""

ax.text(8.7, 2.7, alias_code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ============= When to Use =============
ax.text(8.5, 1.2, 'When to Use:', fontsize=11, weight='bold')

use_box = FancyBboxPatch((8.5, 0.05), 7, 1.0,
                         boxstyle="round,pad=0.05",
                         edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=1.5)
ax.add_patch(use_box)

use_text = """✓ Want consistent function definitions
✓ Need clear view of public API
✓ Want to alias function names
✓ Prefer direct function calls (no 'this')
✓ Legacy code (ES5) or learning closures

❌ Modern projects → Use ES6 modules instead"""

ax.text(8.7, 0.95, use_text, fontsize=7, ha='left', va='top')

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#eafaf1', edgecolor='#2ecc71', label='Revealing Module'),
    mpatches.Patch(facecolor='#fef5e7', edgecolor='#e67e22', label='Module Pattern'),
    mpatches.Patch(facecolor='#f8f9f9', edgecolor='#95a5a6', label='Private Definitions'),
    mpatches.Patch(facecolor='#d5f4e6', edgecolor='#2ecc71', label='Public API (Revealed)')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/revealing_module_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Revealing Module Pattern architecture diagram generated successfully")

