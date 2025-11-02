#!/usr/bin/env python3
# ./build/diagrams/factory_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 9))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Factory Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Client Code
client_box = FancyBboxPatch((0.5, 7), 2, 1.5, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#0ea5e9', 
                             facecolor='#e0f2fe', 
                             linewidth=2)
ax.add_patch(client_box)
ax.text(1.5, 8.2, 'Client Code', fontsize=12, fontweight='bold', ha='center')
ax.text(1.5, 7.8, 'const obj =', fontsize=9, ha='center', family='monospace')
ax.text(1.5, 7.5, '  factory.create()', fontsize=9, ha='center', family='monospace')
ax.text(1.5, 7.2, '    (type, ...args)', fontsize=8, ha='center', family='monospace', style='italic')

# Factory (Central)
factory_box = FancyBboxPatch((3.5, 6.5), 3, 2.5, 
                              boxstyle="round,pad=0.15", 
                              edgecolor='#8b5cf6', 
                              facecolor='#f3e8ff', 
                              linewidth=3)
ax.add_patch(factory_box)
ax.text(5, 8.5, 'Factory', fontsize=14, fontweight='bold', ha='center', color='#8b5cf6')
ax.text(5, 8.1, 'create(type, args)', fontsize=10, ha='center', family='monospace')
ax.text(5, 7.7, '├─ if (type === "A")', fontsize=8, ha='center', family='monospace')
ax.text(5, 7.4, '│   return new A()', fontsize=8, ha='center', family='monospace')
ax.text(5, 7.1, '├─ if (type === "B")', fontsize=8, ha='center', family='monospace')
ax.text(5, 6.8, '│   return new B()', fontsize=8, ha='center', family='monospace')

# Product A
productA_box = FancyBboxPatch((1, 4), 2, 1.5, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#10b981', 
                               facecolor='#d1fae5', 
                               linewidth=2)
ax.add_patch(productA_box)
ax.text(2, 5.1, 'Product A', fontsize=11, fontweight='bold', ha='center')
ax.text(2, 4.7, 'type: "circle"', fontsize=8, ha='center', family='monospace')
ax.text(2, 4.4, 'radius: 10', fontsize=8, ha='center', family='monospace')
ax.text(2, 4.1, 'area()', fontsize=8, ha='center', family='monospace')

# Product B
productB_box = FancyBboxPatch((4, 4), 2, 1.5, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#10b981', 
                               facecolor='#d1fae5', 
                               linewidth=2)
ax.add_patch(productB_box)
ax.text(5, 5.1, 'Product B', fontsize=11, fontweight='bold', ha='center')
ax.text(5, 4.7, 'type: "rectangle"', fontsize=8, ha='center', family='monospace')
ax.text(5, 4.4, 'width: 5', fontsize=8, ha='center', family='monospace')
ax.text(5, 4.1, 'area()', fontsize=8, ha='center', family='monospace')

# Product C
productC_box = FancyBboxPatch((7, 4), 2, 1.5, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#10b981', 
                               facecolor='#d1fae5', 
                               linewidth=2)
ax.add_patch(productC_box)
ax.text(8, 5.1, 'Product C', fontsize=11, fontweight='bold', ha='center')
ax.text(8, 4.7, 'type: "triangle"', fontsize=8, ha='center', family='monospace')
ax.text(8, 4.4, 'base: 8', fontsize=8, ha='center', family='monospace')
ax.text(8, 4.1, 'area()', fontsize=8, ha='center', family='monospace')

# Arrow from Client to Factory
arrow_client = FancyArrowPatch((2.5, 7.75), (3.5, 7.75), 
                                arrowstyle='->', mutation_scale=20, 
                                linewidth=2.5, color='#0ea5e9')
ax.add_patch(arrow_client)
ax.text(3, 8.1, 'calls', fontsize=9, ha='center', style='italic', color='#0ea5e9')

# Arrows from Factory to Products
arrow_A = FancyArrowPatch((4.2, 6.5), (2.5, 5.5), 
                           arrowstyle='->', mutation_scale=18, 
                           linewidth=2, color='#8b5cf6', linestyle='dashed')
ax.add_patch(arrow_A)

arrow_B = FancyArrowPatch((5, 6.5), (5, 5.5), 
                           arrowstyle='->', mutation_scale=18, 
                           linewidth=2, color='#8b5cf6', linestyle='dashed')
ax.add_patch(arrow_B)

arrow_C = FancyArrowPatch((5.8, 6.5), (7.5, 5.5), 
                           arrowstyle='->', mutation_scale=18, 
                           linewidth=2, color='#8b5cf6', linestyle='dashed')
ax.add_patch(arrow_C)

ax.text(3, 6, 'creates', fontsize=8, ha='center', style='italic', color='#8b5cf6')
ax.text(5, 6, 'creates', fontsize=8, ha='center', style='italic', color='#8b5cf6')
ax.text(7, 6, 'creates', fontsize=8, ha='center', style='italic', color='#8b5cf6')

# Return arrows (dashed, lighter)
for x in [2, 5, 8]:
    return_arrow = FancyArrowPatch((x, 4), (1.5, 7), 
                                    arrowstyle='->', mutation_scale=12, 
                                    linewidth=1, color='#10b981', 
                                    linestyle='dotted', alpha=0.5)
    ax.add_patch(return_arrow)

# Benefits box
benefits_box = FancyBboxPatch((0.5, 1.8), 9, 1.5, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#f59e0b', 
                               facecolor='#fef3c7', 
                               linewidth=1.5, alpha=0.7)
ax.add_patch(benefits_box)
ax.text(5, 3, 'Key Benefits', fontsize=11, fontweight='bold', ha='center', color='#f59e0b')
ax.text(5, 2.6, '✓ Client doesn\'t know concrete classes  •  ✓ Centralized creation logic', 
        fontsize=9, ha='center')
ax.text(5, 2.3, '✓ Easy to add new product types  •  ✓ Conditional/dynamic object creation', 
        fontsize=9, ha='center')
ax.text(5, 2, '✓ Decoupling  •  ✓ Testability (inject mock factories)', 
        fontsize=9, ha='center')

# Example usage
ax.text(5, 1.3, 'Example: createShape("circle", 10) → returns Product A', 
        fontsize=9, ha='center', family='monospace', 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#e0e7ff', alpha=0.8))

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Client'),
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Factory'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Products'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=9)

# Flow annotation
ax.text(5, 0.5, 'Flow: Client → Factory (decision logic) → Product (created & returned)', 
        fontsize=9, ha='center', style='italic', color='#6b7280')

plt.tight_layout()
plt.savefig('docs/images/factory_pattern.png', dpi=300, bbox_inches='tight')
print("Factory Pattern diagram saved to docs/images/factory_pattern.png")

