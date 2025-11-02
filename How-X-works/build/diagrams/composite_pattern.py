#!/usr/bin/env python3
# ./build/diagrams/composite_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Composite Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Component (Interface)
component_box = FancyBboxPatch((5, 7.5), 4, 1.5, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#8b5cf6', 
                                facecolor='#f3e8ff', 
                                linewidth=3)
ax.add_patch(component_box)
ax.text(7, 8.7, '«interface»', fontsize=9, ha='center', style='italic', color='#7c3aed')
ax.text(7, 8.35, 'Component', fontsize=13, fontweight='bold', ha='center', color='#7c3aed')
ax.text(7, 8, '+ operation()', fontsize=9, ha='center', family='monospace')

# Leaf
leaf_box = FancyBboxPatch((1.5, 5), 3, 1.5, 
                           boxstyle="round,pad=0.1", 
                           edgecolor='#10b981', 
                           facecolor='#d1fae5', 
                           linewidth=2.5)
ax.add_patch(leaf_box)
ax.text(3, 6.15, 'Leaf', fontsize=12, fontweight='bold', ha='center', color='#059669')
ax.text(3, 5.8, '+ operation() {', fontsize=9, ha='center', family='monospace')
ax.text(3, 5.5, '  // do work', fontsize=8, ha='center', family='monospace', style='italic')
ax.text(3, 5.2, '}', fontsize=9, ha='center', family='monospace')

# Composite
composite_box = FancyBboxPatch((9.5, 5), 3, 1.5, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#f59e0b', 
                                facecolor='#fef3c7', 
                                linewidth=2.5)
ax.add_patch(composite_box)
ax.text(11, 6.15, 'Composite', fontsize=12, fontweight='bold', ha='center', color='#d97706')
ax.text(11, 5.8, '- children[]', fontsize=9, ha='center', family='monospace', style='italic')
ax.text(11, 5.5, '+ add(Component)', fontsize=8, ha='center', family='monospace')
ax.text(11, 5.2, '+ operation() { ... }', fontsize=8, ha='center', family='monospace')

# Inheritance arrows
arrow_leaf = FancyArrowPatch((3, 7.5), (6.2, 7.5), 
                              arrowstyle='->', mutation_scale=20, 
                              linewidth=2.5, color='#8b5cf6', 
                              linestyle='dashed')
ax.add_patch(arrow_leaf)
ax.text(4.5, 7.8, 'implements', fontsize=8, ha='center', 
        style='italic', color='#7c3aed', fontweight='bold')

arrow_composite = FancyArrowPatch((11, 7.5), (7.8, 7.5), 
                                   arrowstyle='->', mutation_scale=20, 
                                   linewidth=2.5, color='#8b5cf6', 
                                   linestyle='dashed')
ax.add_patch(arrow_composite)
ax.text(9.4, 7.8, 'implements', fontsize=8, ha='center', 
        style='italic', color='#7c3aed', fontweight='bold')

# Composition (Composite contains Components)
arrow_contains = FancyArrowPatch((11, 5), (7, 7.5), 
                                  arrowstyle='->', mutation_scale=20, 
                                  linewidth=2.5, color='#f59e0b')
ax.add_patch(arrow_contains)
ax.text(9.5, 6, 'contains *', fontsize=9, ha='center', 
        fontweight='bold', color='#d97706', style='italic')

# Tree structure example
tree_y = 3
ax.text(7, tree_y + 0.6, 'Tree Structure Example', fontsize=12, fontweight='bold', 
        ha='center', color='#6366f1',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#e0e7ff', edgecolor='#6366f1', linewidth=2))

# Root Composite
root_box = FancyBboxPatch((6, tree_y - 0.8), 2, 0.6, 
                           boxstyle="round,pad=0.05", 
                           edgecolor='#f59e0b', 
                           facecolor='#fef3c7', 
                           linewidth=2)
ax.add_patch(root_box)
ax.text(7, tree_y - 0.5, 'Composite', fontsize=9, fontweight='bold', ha='center', color='#d97706')

# Level 2: Composite and Leaves
composite2_box = FancyBboxPatch((1.5, tree_y - 2.3), 1.5, 0.6, 
                                 boxstyle="round,pad=0.05", 
                                 edgecolor='#f59e0b', 
                                 facecolor='#fef3c7', 
                                 linewidth=1.5)
ax.add_patch(composite2_box)
ax.text(2.25, tree_y - 2, 'Composite', fontsize=7, fontweight='bold', ha='center', color='#d97706')

leaf1_box = FancyBboxPatch((4, tree_y - 2.3), 1.2, 0.6, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#10b981', 
                            facecolor='#d1fae5', 
                            linewidth=1.5)
ax.add_patch(leaf1_box)
ax.text(4.6, tree_y - 2, 'Leaf', fontsize=7, fontweight='bold', ha='center', color='#059669')

leaf2_box = FancyBboxPatch((6, tree_y - 2.3), 1.2, 0.6, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#10b981', 
                            facecolor='#d1fae5', 
                            linewidth=1.5)
ax.add_patch(leaf2_box)
ax.text(6.6, tree_y - 2, 'Leaf', fontsize=7, fontweight='bold', ha='center', color='#059669')

composite3_box = FancyBboxPatch((8, tree_y - 2.3), 1.5, 0.6, 
                                 boxstyle="round,pad=0.05", 
                                 edgecolor='#f59e0b', 
                                 facecolor='#fef3c7', 
                                 linewidth=1.5)
ax.add_patch(composite3_box)
ax.text(8.75, tree_y - 2, 'Composite', fontsize=7, fontweight='bold', ha='center', color='#d97706')

leaf3_box = FancyBboxPatch((10.5, tree_y - 2.3), 1.2, 0.6, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#10b981', 
                            facecolor='#d1fae5', 
                            linewidth=1.5)
ax.add_patch(leaf3_box)
ax.text(11.1, tree_y - 2, 'Leaf', fontsize=7, fontweight='bold', ha='center', color='#059669')

# Arrows from root to children
for x_child in [2.25, 4.6, 6.6, 8.75, 11.1]:
    arrow = FancyArrowPatch((7, tree_y - 0.8), (x_child, tree_y - 1.7), 
                             arrowstyle='-', linewidth=1.5, color='#6366f1')
    ax.add_patch(arrow)

# Level 3: Leaves under first composite
leaf4_box = FancyBboxPatch((1, tree_y - 3.5), 0.9, 0.5, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#10b981', 
                            facecolor='#d1fae5', 
                            linewidth=1.2)
ax.add_patch(leaf4_box)
ax.text(1.45, tree_y - 3.25, 'Leaf', fontsize=6, fontweight='bold', ha='center', color='#059669')

leaf5_box = FancyBboxPatch((2.3, tree_y - 3.5), 0.9, 0.5, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#10b981', 
                            facecolor='#d1fae5', 
                            linewidth=1.2)
ax.add_patch(leaf5_box)
ax.text(2.75, tree_y - 3.25, 'Leaf', fontsize=6, fontweight='bold', ha='center', color='#059669')

for x_child in [1.45, 2.75]:
    arrow = FancyArrowPatch((2.25, tree_y - 2.3), (x_child, tree_y - 3), 
                             arrowstyle='-', linewidth=1.2, color='#6366f1')
    ax.add_patch(arrow)

# Level 3: Leaves under second composite
leaf6_box = FancyBboxPatch((7.5, tree_y - 3.5), 0.9, 0.5, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#10b981', 
                            facecolor='#d1fae5', 
                            linewidth=1.2)
ax.add_patch(leaf6_box)
ax.text(7.95, tree_y - 3.25, 'Leaf', fontsize=6, fontweight='bold', ha='center', color='#059669')

leaf7_box = FancyBboxPatch((8.9, tree_y - 3.5), 0.9, 0.5, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#10b981', 
                            facecolor='#d1fae5', 
                            linewidth=1.2)
ax.add_patch(leaf7_box)
ax.text(9.35, tree_y - 3.25, 'Leaf', fontsize=6, fontweight='bold', ha='center', color='#059669')

for x_child in [7.95, 9.35]:
    arrow = FancyArrowPatch((8.75, tree_y - 2.3), (x_child, tree_y - 3), 
                             arrowstyle='-', linewidth=1.2, color='#6366f1')
    ax.add_patch(arrow)

# Benefits box
benefits_box = FancyBboxPatch((0.5, 0.3), 13, 1, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#8b5cf6', 
                               facecolor='#f5f3ff', 
                               linewidth=2, alpha=0.9)
ax.add_patch(benefits_box)
ax.text(7, 1.1, 'Key Principle: Uniform Treatment of Objects and Compositions', 
        fontsize=11, fontweight='bold', ha='center', color='#7c3aed')
ax.text(7, 0.8, '✓ Tree structures  •  ✓ Recursive operations  •  ✓ Uniform interface (leaf = composite)', 
        fontsize=9, ha='center')
ax.text(7, 0.5, 'Pattern: Both Leaf and Composite implement Component interface + Composite contains Components', 
        fontsize=8, ha='center', family='monospace', style='italic', color='#6d28d9')

# Annotations
ax.text(3, 4.7, 'Simple element\n(no children)', fontsize=7, ha='center', 
        style='italic', color='#059669')
ax.text(11, 4.7, 'Container element\n(has children)', fontsize=7, ha='center', 
        style='italic', color='#d97706')

# Operation flow annotation
ax.text(0.8, 8, 'Client calls:', fontsize=8, fontweight='bold', ha='left')
ax.text(0.8, 7.7, 'component.operation()', fontsize=7, ha='left', family='monospace')
ax.text(0.8, 7.45, '↳ works for both', fontsize=7, ha='left', style='italic')
ax.text(0.8, 7.2, '  Leaf & Composite', fontsize=7, ha='left', style='italic')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Component (Interface)'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Leaf (Simple)'),
    mpatches.Patch(facecolor='#fef3c7', edgecolor='#f59e0b', label='Composite (Container)'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/composite_pattern.png', dpi=300, bbox_inches='tight')
print("Composite Pattern diagram saved to docs/images/composite_pattern.png")

