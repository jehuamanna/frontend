#!/usr/bin/env python3
# ./build/diagrams/abstract_factory_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(16, 10))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(6, 9.5, 'Abstract Factory Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Client
client_box = FancyBboxPatch((0.5, 7.5), 2, 1.2, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#0ea5e9', 
                             facecolor='#e0f2fe', 
                             linewidth=2)
ax.add_patch(client_box)
ax.text(1.5, 8.5, 'Client', fontsize=12, fontweight='bold', ha='center')
ax.text(1.5, 8.1, 'Uses factory', fontsize=9, ha='center', style='italic')
ax.text(1.5, 7.8, 'to create', fontsize=9, ha='center', style='italic')
ax.text(1.5, 7.5, 'product families', fontsize=9, ha='center', style='italic')

# Abstract Factory Interface
abstract_box = FancyBboxPatch((3.5, 7.2), 2.5, 1.8, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#8b5cf6', 
                               facecolor='#f3e8ff', 
                               linewidth=2.5, 
                               linestyle='dashed')
ax.add_patch(abstract_box)
ax.text(4.75, 8.7, '«interface»', fontsize=9, ha='center', style='italic')
ax.text(4.75, 8.4, 'AbstractFactory', fontsize=11, fontweight='bold', ha='center')
ax.text(4.75, 8, 'createProductA()', fontsize=9, ha='center', family='monospace')
ax.text(4.75, 7.7, 'createProductB()', fontsize=9, ha='center', family='monospace')
ax.text(4.75, 7.4, 'createProductC()', fontsize=9, ha='center', family='monospace')

# Concrete Factory 1 (Light Theme)
factory1_box = FancyBboxPatch((7, 7.5), 2, 1.5, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#8b5cf6', 
                               facecolor='#ede9fe', 
                               linewidth=2)
ax.add_patch(factory1_box)
ax.text(8, 8.7, 'LightFactory', fontsize=11, fontweight='bold', ha='center')
ax.text(8, 8.3, 'createProductA()', fontsize=8, ha='center', family='monospace')
ax.text(8, 8, '  → LightButtonA', fontsize=8, ha='center', family='monospace')
ax.text(8, 7.7, 'createProductB()', fontsize=8, ha='center', family='monospace')

# Concrete Factory 2 (Dark Theme)
factory2_box = FancyBboxPatch((9.5, 7.5), 2, 1.5, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#8b5cf6', 
                               facecolor='#ede9fe', 
                               linewidth=2)
ax.add_patch(factory2_box)
ax.text(10.5, 8.7, 'DarkFactory', fontsize=11, fontweight='bold', ha='center')
ax.text(10.5, 8.3, 'createProductA()', fontsize=8, ha='center', family='monospace')
ax.text(10.5, 8, '  → DarkButtonA', fontsize=8, ha='center', family='monospace')
ax.text(10.5, 7.7, 'createProductB()', fontsize=8, ha='center', family='monospace')

# Implements arrows
arrow_impl1 = FancyArrowPatch((6, 8), (7, 8), 
                               arrowstyle='->', mutation_scale=15, 
                               linewidth=1.5, color='#8b5cf6', linestyle='dashed')
ax.add_patch(arrow_impl1)
ax.text(6.5, 8.3, 'implements', fontsize=8, ha='center', style='italic', color='#8b5cf6')

arrow_impl2 = FancyArrowPatch((6, 8.5), (9.5, 8.5), 
                               arrowstyle='->', mutation_scale=15, 
                               linewidth=1.5, color='#8b5cf6', linestyle='dashed')
ax.add_patch(arrow_impl2)

# Client uses factory
arrow_client = FancyArrowPatch((2.5, 8.1), (3.5, 8.1), 
                                arrowstyle='->', mutation_scale=18, 
                                linewidth=2, color='#0ea5e9')
ax.add_patch(arrow_client)
ax.text(3, 8.4, 'uses', fontsize=9, ha='center', style='italic', color='#0ea5e9')

# Product A Family
productA_abstract = FancyBboxPatch((3.5, 4.8), 2, 1.2, 
                                    boxstyle="round,pad=0.1", 
                                    edgecolor='#10b981', 
                                    facecolor='#d1fae5', 
                                    linewidth=2, 
                                    linestyle='dashed')
ax.add_patch(productA_abstract)
ax.text(4.5, 5.7, '«interface» ProductA', fontsize=10, fontweight='bold', ha='center')
ax.text(4.5, 5.3, 'operation()', fontsize=8, ha='center', family='monospace')

lightA_box = FancyBboxPatch((7, 4.8), 1.8, 1.2, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#10b981', 
                             facecolor='#d1fae5', 
                             linewidth=2)
ax.add_patch(lightA_box)
ax.text(7.9, 5.7, 'LightButtonA', fontsize=9, fontweight='bold', ha='center')
ax.text(7.9, 5.3, 'operation()', fontsize=8, ha='center', family='monospace')

darkA_box = FancyBboxPatch((9.3, 4.8), 1.8, 1.2, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='#10b981', 
                            facecolor='#d1fae5', 
                            linewidth=2)
ax.add_patch(darkA_box)
ax.text(10.2, 5.7, 'DarkButtonA', fontsize=9, fontweight='bold', ha='center')
ax.text(10.2, 5.3, 'operation()', fontsize=8, ha='center', family='monospace')

# Product B Family
productB_abstract = FancyBboxPatch((3.5, 2.8), 2, 1.2, 
                                    boxstyle="round,pad=0.1", 
                                    edgecolor='#f59e0b', 
                                    facecolor='#fef3c7', 
                                    linewidth=2, 
                                    linestyle='dashed')
ax.add_patch(productB_abstract)
ax.text(4.5, 3.7, '«interface» ProductB', fontsize=10, fontweight='bold', ha='center')
ax.text(4.5, 3.3, 'render()', fontsize=8, ha='center', family='monospace')

lightB_box = FancyBboxPatch((7, 2.8), 1.8, 1.2, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#f59e0b', 
                             facecolor='#fef3c7', 
                             linewidth=2)
ax.add_patch(lightB_box)
ax.text(7.9, 3.7, 'LightInputB', fontsize=9, fontweight='bold', ha='center')
ax.text(7.9, 3.3, 'render()', fontsize=8, ha='center', family='monospace')

darkB_box = FancyBboxPatch((9.3, 2.8), 1.8, 1.2, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='#f59e0b', 
                            facecolor='#fef3c7', 
                            linewidth=2)
ax.add_patch(darkB_box)
ax.text(10.2, 3.7, 'DarkInputB', fontsize=9, fontweight='bold', ha='center')
ax.text(10.2, 3.3, 'render()', fontsize=8, ha='center', family='monospace')

# Implements arrows for products
for x in [7.9, 10.2]:
    arrow = FancyArrowPatch((x, 4.8), (5, 5.2), 
                             arrowstyle='->', mutation_scale=12, 
                             linewidth=1.5, color='#10b981', 
                             linestyle='dashed', alpha=0.6)
    ax.add_patch(arrow)

for x in [7.9, 10.2]:
    arrow = FancyArrowPatch((x, 2.8), (5, 3.5), 
                             arrowstyle='->', mutation_scale=12, 
                             linewidth=1.5, color='#f59e0b', 
                             linestyle='dashed', alpha=0.6)
    ax.add_patch(arrow)

# Factory creates product arrows
arrow_f1_pA = FancyArrowPatch((8, 7.5), (7.9, 6), 
                               arrowstyle='->', mutation_scale=15, 
                               linewidth=1.5, color='#8b5cf6', alpha=0.7)
ax.add_patch(arrow_f1_pA)
ax.text(7.5, 6.7, 'creates', fontsize=7, ha='center', style='italic', color='#8b5cf6')

arrow_f2_pA = FancyArrowPatch((10.5, 7.5), (10.2, 6), 
                               arrowstyle='->', mutation_scale=15, 
                               linewidth=1.5, color='#8b5cf6', alpha=0.7)
ax.add_patch(arrow_f2_pA)

arrow_f1_pB = FancyArrowPatch((8, 7.5), (7.9, 4), 
                               arrowstyle='->', mutation_scale=15, 
                               linewidth=1.5, color='#8b5cf6', alpha=0.5)
ax.add_patch(arrow_f1_pB)

arrow_f2_pB = FancyArrowPatch((10.5, 7.5), (10.2, 4), 
                               arrowstyle='->', mutation_scale=15, 
                               linewidth=1.5, color='#8b5cf6', alpha=0.5)
ax.add_patch(arrow_f2_pB)

# Key insight box
insight_box = FancyBboxPatch((0.5, 0.5), 11, 1.8, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#6366f1', 
                              facecolor='#e0e7ff', 
                              linewidth=1.5, alpha=0.8)
ax.add_patch(insight_box)
ax.text(6, 2, 'Key Concept: Product Families', fontsize=12, fontweight='bold', ha='center', color='#6366f1')
ax.text(6, 1.6, 'Each factory creates a complete family of related products (A, B, C...)', 
        fontsize=9, ha='center')
ax.text(6, 1.3, 'LightFactory → {LightButtonA, LightInputB, ...} (consistent light theme)', 
        fontsize=9, ha='center', family='monospace')
ax.text(6, 1, 'DarkFactory → {DarkButtonA, DarkInputB, ...} (consistent dark theme)', 
        fontsize=9, ha='center', family='monospace')
ax.text(6, 0.7, 'Client code works with any factory, ensuring all products in use are from the same family', 
        fontsize=8, ha='center', style='italic')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Client'),
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Factory (Abstract/Concrete)'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Product Family A'),
    mpatches.Patch(facecolor='#fef3c7', edgecolor='#f59e0b', label='Product Family B'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=9)

plt.tight_layout()
plt.savefig('docs/images/abstract_factory_pattern.png', dpi=300, bbox_inches='tight')
print("Abstract Factory Pattern diagram saved to docs/images/abstract_factory_pattern.png")

