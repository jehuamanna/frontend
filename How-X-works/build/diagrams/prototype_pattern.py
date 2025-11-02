#!/usr/bin/env python3
# ./build/diagrams/prototype_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(6, 9.5, 'Prototype Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Prototype
prototype_box = FancyBboxPatch((1, 6.5), 3, 2, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#8b5cf6', 
                                facecolor='#f3e8ff', 
                                linewidth=2.5)
ax.add_patch(prototype_box)
ax.text(2.5, 8.2, 'Prototype', fontsize=13, fontweight='bold', ha='center', color='#8b5cf6')
ax.text(2.5, 7.85, 'property1: value1', fontsize=9, ha='center', family='monospace')
ax.text(2.5, 7.55, 'property2: value2', fontsize=9, ha='center', family='monospace')
ax.text(2.5, 7.25, 'method1()', fontsize=9, ha='center', family='monospace')
ax.text(2.5, 6.95, 'method2()', fontsize=9, ha='center', family='monospace')
ax.text(2.5, 6.65, 'clone()', fontsize=9, ha='center', family='monospace', fontweight='bold')

# Clone 1
clone1_box = FancyBboxPatch((5.5, 7.5), 2.5, 1.3, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#10b981', 
                             facecolor='#d1fae5', 
                             linewidth=2)
ax.add_patch(clone1_box)
ax.text(6.75, 8.5, 'Clone 1', fontsize=11, fontweight='bold', ha='center')
ax.text(6.75, 8.15, 'property1: value1', fontsize=8, ha='center', family='monospace')
ax.text(6.75, 7.85, 'property2: modified', fontsize=8, ha='center', family='monospace', color='#059669')
ax.text(6.75, 7.55, 'Shares methods ↑', fontsize=7, ha='center', style='italic')

# Clone 2
clone2_box = FancyBboxPatch((5.5, 5.5), 2.5, 1.3, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#10b981', 
                             facecolor='#d1fae5', 
                             linewidth=2)
ax.add_patch(clone2_box)
ax.text(6.75, 6.5, 'Clone 2', fontsize=11, fontweight='bold', ha='center')
ax.text(6.75, 6.15, 'property1: changed', fontsize=8, ha='center', family='monospace', color='#059669')
ax.text(6.75, 5.85, 'property2: value2', fontsize=8, ha='center', family='monospace')
ax.text(6.75, 5.55, 'Shares methods ↑', fontsize=7, ha='center', style='italic')

# Clone 3
clone3_box = FancyBboxPatch((8.5, 6.5), 2.5, 1.3, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#10b981', 
                             facecolor='#d1fae5', 
                             linewidth=2)
ax.add_patch(clone3_box)
ax.text(9.75, 7.5, 'Clone 3', fontsize=11, fontweight='bold', ha='center')
ax.text(9.75, 7.15, 'property1: value1', fontsize=8, ha='center', family='monospace')
ax.text(9.75, 6.85, 'property2: different', fontsize=8, ha='center', family='monospace', color='#059669')
ax.text(9.75, 6.55, 'Shares methods ↑', fontsize=7, ha='center', style='italic')

# Clone arrows
arrow_c1 = FancyArrowPatch((4, 7.8), (5.5, 7.9), 
                            arrowstyle='->', mutation_scale=18, 
                            linewidth=2, color='#8b5cf6')
ax.add_patch(arrow_c1)
ax.text(4.75, 8.2, 'clone()', fontsize=8, ha='center', fontweight='bold', color='#8b5cf6')

arrow_c2 = FancyArrowPatch((4, 7.2), (5.5, 6.5), 
                            arrowstyle='->', mutation_scale=18, 
                            linewidth=2, color='#8b5cf6')
ax.add_patch(arrow_c2)
ax.text(4.75, 6.9, 'clone()', fontsize=8, ha='center', fontweight='bold', color='#8b5cf6')

arrow_c3 = FancyArrowPatch((4, 7.5), (8.5, 7.1), 
                            arrowstyle='->', mutation_scale=18, 
                            linewidth=2, color='#8b5cf6')
ax.add_patch(arrow_c3)
ax.text(6.25, 7.5, 'clone()', fontsize=8, ha='center', fontweight='bold', color='#8b5cf6')

# Delegation arrows (dashed - showing method sharing)
for x in [6.75, 9.75]:
    y_start = 7.5 if x == 6.75 else 6.5
    arrow = FancyArrowPatch((x, y_start + 0.8), (2.5, 6.5), 
                             arrowstyle='->', mutation_scale=12, 
                             linewidth=1.5, color='#7c3aed', 
                             linestyle='dashed', alpha=0.5)
    ax.add_patch(arrow)

arrow_d2 = FancyArrowPatch((6.75, 5.5), (2.5, 6.5), 
                            arrowstyle='->', mutation_scale=12, 
                            linewidth=1.5, color='#7c3aed', 
                            linestyle='dashed', alpha=0.5)
ax.add_patch(arrow_d2)

# Cloning methods comparison
methods_box = FancyBboxPatch((0.5, 3.5), 5.5, 1.8, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#f59e0b', 
                              facecolor='#fef3c7', 
                              linewidth=2)
ax.add_patch(methods_box)
ax.text(3.25, 5, 'JavaScript Cloning Methods', 
        fontsize=11, fontweight='bold', ha='center', color='#f59e0b')
ax.text(3.25, 4.65, 'Object.create(proto) - Prototype delegation', 
        fontsize=8, ha='center', family='monospace')
ax.text(3.25, 4.35, '{...obj} / Object.assign() - Shallow copy', 
        fontsize=8, ha='center', family='monospace')
ax.text(3.25, 4.05, 'structuredClone(obj) - Deep copy', 
        fontsize=8, ha='center', family='monospace')
ax.text(3.25, 3.75, 'node.cloneNode(deep) - DOM cloning', 
        fontsize=8, ha='center', family='monospace')

# Benefits
benefits_box = FancyBboxPatch((6.5, 3.5), 5, 1.8, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#10b981', 
                               facecolor='#d1fae5', 
                               linewidth=2)
ax.add_patch(benefits_box)
ax.text(9, 5, 'Key Benefits', 
        fontsize=11, fontweight='bold', ha='center', color='#059669')
ax.text(9, 4.65, '✓ Fast: cloning faster than construction', 
        fontsize=8, ha='center')
ax.text(9, 4.35, '✓ Memory efficient: shared methods', 
        fontsize=8, ha='center')
ax.text(9, 4.05, '✓ Flexible: create by example', 
        fontsize=8, ha='center')
ax.text(9, 3.75, '✓ Dynamic: runtime object composition', 
        fontsize=8, ha='center')

# Use cases
usecase_box = FancyBboxPatch((0.5, 1.5), 11, 1.8, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#6366f1', 
                              facecolor='#e0e7ff', 
                              linewidth=1.5, alpha=0.8)
ax.add_patch(usecase_box)
ax.text(6, 3, 'Common Use Cases', 
        fontsize=11, fontweight='bold', ha='center', color='#6366f1')
ax.text(6, 2.65, '• Game Development: Clone enemy/item templates with slight variations', 
        fontsize=8, ha='center')
ax.text(6, 2.35, '• UI Frameworks: Clone component configurations or DOM templates', 
        fontsize=8, ha='center')
ax.text(6, 2.05, '• Data Processing: Clone data structures to avoid re-initialization', 
        fontsize=8, ha='center')
ax.text(6, 1.75, '• Configuration: Clone base configs and modify for different environments', 
        fontsize=8, ha='center')

# Example
ax.text(6, 1.1, 'Example: const clone = Object.create(prototype); clone.value = "modified";', 
        fontsize=9, ha='center', family='monospace', 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef3c7', alpha=0.8))

ax.text(6, 0.5, 'Pattern: Clone objects instead of constructing from scratch', 
        fontsize=9, ha='center', style='italic', color='#6b7280')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Prototype'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Clones'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('docs/images/prototype_pattern.png', dpi=300, bbox_inches='tight')
print("Prototype Pattern diagram saved to docs/images/prototype_pattern.png")

