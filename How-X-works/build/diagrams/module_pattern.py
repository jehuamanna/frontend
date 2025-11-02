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
ax.text(8, 9.5, 'Module Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(8, 9.0, 'Encapsulation via Closures and IIFEs',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= Module Structure =============
# IIFE wrapper
iife_box = FancyBboxPatch((0.5, 4.5), 6.5, 4,
                          boxstyle="round,pad=0.15",
                          edgecolor='#34495e', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(iife_box)
ax.text(3.75, 8.3, 'IIFE (Immediately Invoked Function Expression)', 
        fontsize=10, weight='bold', ha='center')
ax.text(3.75, 8.0, '(function() { ... })()', 
        fontsize=9, ha='center', family='monospace', style='italic', color='gray')

# Private scope
private_box = FancyBboxPatch((0.8, 6.2), 2.8, 1.8,
                             boxstyle="round,pad=0.1",
                             edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=2)
ax.add_patch(private_box)
ax.text(2.2, 7.85, 'Private Members', fontsize=10, weight='bold', ha='center')
ax.text(0.95, 7.5, '// Private vars', fontsize=8, ha='left', family='monospace', color='gray')
ax.text(0.95, 7.2, 'let count = 0;', fontsize=8, ha='left', family='monospace')
ax.text(0.95, 6.9, '', fontsize=8, ha='left')
ax.text(0.95, 6.6, '// Private funcs', fontsize=8, ha='left', family='monospace', color='gray')
ax.text(0.95, 6.3, 'function log() {}', fontsize=8, ha='left', family='monospace')

# Public API (return object)
public_box = FancyBboxPatch((4.2, 6.2), 2.5, 1.8,
                            boxstyle="round,pad=0.1",
                            edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=2)
ax.add_patch(public_box)
ax.text(5.45, 7.85, 'Public API', fontsize=10, weight='bold', ha='center')
ax.text(4.35, 7.5, 'return {', fontsize=8, ha='left', family='monospace')
ax.text(4.5, 7.2, 'increment() {},', fontsize=8, ha='left', family='monospace')
ax.text(4.5, 6.9, 'getCount() {},', fontsize=8, ha='left', family='monospace')
ax.text(4.5, 6.6, 'reset() {}', fontsize=8, ha='left', family='monospace')
ax.text(4.35, 6.3, '};', fontsize=8, ha='left', family='monospace')

# Closure arrow (public methods access private)
closure_arrow = FancyArrowPatch((3.6, 7), (4.2, 7),
                               arrowstyle='<->', mutation_scale=20,
                               linewidth=2, color='#9b59b6', linestyle='dashed')
ax.add_patch(closure_arrow)
ax.text(3.9, 7.3, 'Closure', fontsize=8, ha='center', 
        style='italic', color='#9b59b6', weight='bold')

# Module variable (assigned result)
module_box = FancyBboxPatch((0.8, 4.7), 5.9, 0.8,
                            boxstyle="round,pad=0.1",
                            edgecolor='#3498db', facecolor='#ebf5fb', linewidth=2)
ax.add_patch(module_box)
ax.text(3.75, 5.35, 'const module = (function() { ... })()', 
        fontsize=9, ha='center', family='monospace', weight='bold')
ax.text(3.75, 5.0, 'Module instance receives public API', 
        fontsize=8, ha='center', style='italic', color='gray')

# ============= Usage Example =============
ax.text(8, 8.3, 'Usage & Access Control:', fontsize=11, weight='bold')

# Global scope
global_box = FancyBboxPatch((8, 5.5), 7.5, 2.5,
                            boxstyle="round,pad=0.1",
                            edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=2)
ax.add_patch(global_box)
ax.text(11.75, 7.8, 'Global Scope (Outside Module)', fontsize=10, weight='bold', ha='center')

# Successful access (public)
success_box = FancyBboxPatch((8.3, 6.7), 3.2, 0.9,
                             boxstyle="round,pad=0.05",
                             edgecolor='#2ecc71', facecolor='#d5f4e6', linewidth=1.5)
ax.add_patch(success_box)
ax.text(8.5, 7.5, '✓ Can access:', fontsize=8, weight='bold', ha='left', color='#2ecc71')
ax.text(8.5, 7.2, 'module.increment()', fontsize=8, ha='left', family='monospace')
ax.text(8.5, 6.9, 'module.getCount()', fontsize=8, ha='left', family='monospace')

# Failed access (private)
fail_box = FancyBboxPatch((12.0, 6.7), 3.2, 0.9,
                          boxstyle="round,pad=0.05",
                          edgecolor='#e74c3c', facecolor='#f5b7b1', linewidth=1.5)
ax.add_patch(fail_box)
ax.text(12.2, 7.5, '✗ Cannot access:', fontsize=8, weight='bold', ha='left', color='#e74c3c')
ax.text(12.2, 7.2, 'module.count', fontsize=8, ha='left', family='monospace')
ax.text(12.2, 6.9, 'module.log()', fontsize=8, ha='left', family='monospace')

# Results
ax.text(8.5, 6.3, '→ Returns value', fontsize=7, ha='left', style='italic', color='gray')
ax.text(12.2, 6.3, '→ undefined', fontsize=7, ha='left', style='italic', color='gray')

# ============= Benefits =============
ax.text(8, 5.0, 'Key Benefits:', fontsize=11, weight='bold')

benefit_box = FancyBboxPatch((8, 3.5), 7.5, 1.3,
                             boxstyle="round,pad=0.1",
                             edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(benefit_box)

benefits = """1. Encapsulation: True privacy via closures
2. Namespace: Avoid global pollution (single module variable)
3. Organization: Logical grouping of related functionality
4. Backwards Compatible: Works in all browsers (ES5+)"""

ax.text(8.2, 4.65, benefits, fontsize=8, ha='left', va='top')

# ============= Code Example =============
ax.text(0.5, 4.0, 'Complete Example:', fontsize=11, weight='bold')

code_box = FancyBboxPatch((0.5, 0.3), 7, 3.5,
                          boxstyle="round,pad=0.1",
                          edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=1)
ax.add_patch(code_box)

code = """const counterModule = (function() {
  // Private members (not accessible outside)
  let count = 0;
  
  function logChange(oldValue, newValue) {
    console.log(`Count: ${oldValue} → ${newValue}`);
  }
  
  // Public API (returned object)
  return {
    increment() {
      const oldCount = count;
      count++;
      logChange(oldCount, count);
    },
    
    getCount() {
      return count; // Closure: access private 'count'
    },
    
    reset() {
      count = 0;
      console.log('Counter reset');
    }
  };
})();

// Usage
counterModule.increment();     // Works ✓
counterModule.getCount();       // Returns 1 ✓
console.log(counterModule.count); // undefined ✗ (private)
counterModule.logChange();      // Error ✗ (private)"""

ax.text(0.7, 3.65, code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ============= Variants =============
ax.text(8, 3.0, 'Common Variants:', fontsize=11, weight='bold')

# Revealing Module
variant1_box = FancyBboxPatch((8, 1.5), 3.5, 1.3,
                              boxstyle="round,pad=0.1",
                              edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=1.5)
ax.add_patch(variant1_box)
ax.text(9.75, 2.65, 'Revealing Module', fontsize=9, weight='bold', ha='center')
ax.text(8.2, 2.4, '// All funcs private', fontsize=7, ha='left', family='monospace', color='gray')
ax.text(8.2, 2.2, 'function inc() {}', fontsize=7, ha='left', family='monospace')
ax.text(8.2, 2.0, '', fontsize=7, ha='left')
ax.text(8.2, 1.8, 'return {', fontsize=7, ha='left', family='monospace')
ax.text(8.4, 1.6, 'increment: inc', fontsize=7, ha='left', family='monospace')
ax.text(8.2, 1.4, '};', fontsize=7, ha='left', family='monospace')
ax.text(9.75, 1.15, '(Expose via aliases)', fontsize=7, ha='center', style='italic', color='gray')

# Singleton Module
variant2_box = FancyBboxPatch((12, 1.5), 3.5, 1.3,
                              boxstyle="round,pad=0.1",
                              edgecolor='#e67e22', facecolor='#fef5e7', linewidth=1.5)
ax.add_patch(variant2_box)
ax.text(13.75, 2.65, 'Singleton Module', fontsize=9, weight='bold', ha='center')
ax.text(12.2, 2.4, 'const module = (', fontsize=7, ha='left', family='monospace')
ax.text(12.4, 2.2, 'function() {', fontsize=7, ha='left', family='monospace')
ax.text(12.6, 2.0, 'let instance;', fontsize=7, ha='left', family='monospace')
ax.text(12.6, 1.8, 'return {...};', fontsize=7, ha='left', family='monospace')
ax.text(12.4, 1.6, '}', fontsize=7, ha='left', family='monospace')
ax.text(12.2, 1.4, ')();', fontsize=7, ha='left', family='monospace')
ax.text(13.75, 1.15, '(Single instance)', fontsize=7, ha='center', style='italic', color='gray')

# ============= ES6 Comparison =============
ax.text(0.5, 1.0, 'Modern Alternative (ES6 Modules):', fontsize=11, weight='bold')

es6_box = FancyBboxPatch((0.5, 0.05), 7, 0.8,
                         boxstyle="round,pad=0.05",
                         edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=1.5)
ax.add_patch(es6_box)

es6_code = """// counter.js
let count = 0; // Private (not exported)
export function increment() { count++; }
export function getCount() { return count; }

// import { increment, getCount } from './counter.js';"""

ax.text(0.7, 0.75, es6_code, fontsize=7, ha='left', va='top', family='monospace')
ax.text(4, -0.05, '→ Native module system replaces Module Pattern', 
        fontsize=7, ha='center', style='italic', color='gray')

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#fadbd8', edgecolor='#e74c3c', label='Private (Closured)'),
    mpatches.Patch(facecolor='#eafaf1', edgecolor='#2ecc71', label='Public API'),
    mpatches.Patch(facecolor='#ecf0f1', edgecolor='#34495e', label='IIFE Scope'),
    mpatches.Patch(facecolor='#ebf5fb', edgecolor='#3498db', label='Module Instance')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/module_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Module Pattern architecture diagram generated successfully")

