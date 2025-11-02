#!/usr/bin/env python3
# ./build/diagrams/bridge_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Bridge Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Abstraction Hierarchy (Left)
ax.text(3, 8.8, 'Abstraction Hierarchy', fontsize=12, fontweight='bold', 
        ha='center', color='#8b5cf6',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f3e8ff', edgecolor='#8b5cf6', linewidth=2))

# Abstraction
abstraction_box = FancyBboxPatch((1, 6.5), 4, 1.8, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#8b5cf6', 
                                  facecolor='#f3e8ff', 
                                  linewidth=2.5)
ax.add_patch(abstraction_box)
ax.text(3, 8, 'Abstraction', fontsize=12, fontweight='bold', ha='center', color='#7c3aed')
ax.text(3, 7.6, '- implementation', fontsize=9, ha='center', family='monospace', style='italic')
ax.text(3, 7.3, '+ operation()', fontsize=9, ha='center', family='monospace')
ax.text(3, 7, '+ setImplementation()', fontsize=9, ha='center', family='monospace')

# Refined Abstractions
refined1_box = FancyBboxPatch((0.5, 4.5), 2, 1.3, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#a78bfa', 
                               facecolor='#ede9fe', 
                               linewidth=2)
ax.add_patch(refined1_box)
ax.text(1.5, 5.5, 'RefinedA', fontsize=10, fontweight='bold', ha='center', color='#7c3aed')
ax.text(1.5, 5.2, '+ operation() {', fontsize=8, ha='center', family='monospace')
ax.text(1.5, 4.9, '  impl.doA()', fontsize=8, ha='center', family='monospace')
ax.text(1.5, 4.65, '}', fontsize=8, ha='center', family='monospace')

refined2_box = FancyBboxPatch((3.5, 4.5), 2, 1.3, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#a78bfa', 
                               facecolor='#ede9fe', 
                               linewidth=2)
ax.add_patch(refined2_box)
ax.text(4.5, 5.5, 'RefinedB', fontsize=10, fontweight='bold', ha='center', color='#7c3aed')
ax.text(4.5, 5.2, '+ operation() {', fontsize=8, ha='center', family='monospace')
ax.text(4.5, 4.9, '  impl.doB()', fontsize=8, ha='center', family='monospace')
ax.text(4.5, 4.65, '}', fontsize=8, ha='center', family='monospace')

# Inheritance arrows (Abstraction → Refined)
arrow_ref1 = FancyArrowPatch((1.5, 6.5), (1.5, 5.8), 
                              arrowstyle='->', mutation_scale=15, 
                              linewidth=2, color='#8b5cf6', 
                              linestyle='dashed')
ax.add_patch(arrow_ref1)

arrow_ref2 = FancyArrowPatch((4.5, 6.5), (4.5, 5.8), 
                              arrowstyle='->', mutation_scale=15, 
                              linewidth=2, color='#8b5cf6', 
                              linestyle='dashed')
ax.add_patch(arrow_ref2)

# Implementation Hierarchy (Right)
ax.text(11, 8.8, 'Implementation Hierarchy', fontsize=12, fontweight='bold', 
        ha='center', color='#10b981',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#d1fae5', edgecolor='#10b981', linewidth=2))

# Implementation Interface
implementation_box = FancyBboxPatch((9, 6.5), 4, 1.8, 
                                     boxstyle="round,pad=0.1", 
                                     edgecolor='#10b981', 
                                     facecolor='#d1fae5', 
                                     linewidth=2.5)
ax.add_patch(implementation_box)
ax.text(11, 8, '«interface»', fontsize=9, ha='center', style='italic', color='#059669')
ax.text(11, 7.6, 'Implementation', fontsize=12, fontweight='bold', ha='center', color='#059669')
ax.text(11, 7.25, '+ doA()', fontsize=9, ha='center', family='monospace')
ax.text(11, 6.95, '+ doB()', fontsize=9, ha='center', family='monospace')

# Concrete Implementations
concrete1_box = FancyBboxPatch((8.5, 4.5), 2, 1.3, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#34d399', 
                                facecolor='#ecfdf5', 
                                linewidth=2)
ax.add_patch(concrete1_box)
ax.text(9.5, 5.5, 'ConcreteImpl1', fontsize=10, fontweight='bold', ha='center', color='#059669')
ax.text(9.5, 5.15, '+ doA() { ... }', fontsize=8, ha='center', family='monospace')
ax.text(9.5, 4.85, '+ doB() { ... }', fontsize=8, ha='center', family='monospace')

concrete2_box = FancyBboxPatch((11.5, 4.5), 2, 1.3, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#34d399', 
                                facecolor='#ecfdf5', 
                                linewidth=2)
ax.add_patch(concrete2_box)
ax.text(12.5, 5.5, 'ConcreteImpl2', fontsize=10, fontweight='bold', ha='center', color='#059669')
ax.text(12.5, 5.15, '+ doA() { ... }', fontsize=8, ha='center', family='monospace')
ax.text(12.5, 4.85, '+ doB() { ... }', fontsize=8, ha='center', family='monospace')

# Implementation arrows (Implementation → Concrete)
arrow_impl1 = FancyArrowPatch((9.5, 6.5), (9.5, 5.8), 
                               arrowstyle='->', mutation_scale=15, 
                               linewidth=2, color='#10b981', 
                               linestyle='dashed')
ax.add_patch(arrow_impl1)

arrow_impl2 = FancyArrowPatch((12.5, 6.5), (12.5, 5.8), 
                               arrowstyle='->', mutation_scale=15, 
                               linewidth=2, color='#10b981', 
                               linestyle='dashed')
ax.add_patch(arrow_impl2)

# BRIDGE: Composition arrow (Abstraction → Implementation)
bridge_arrow = FancyArrowPatch((5, 7.4), (9, 7.4), 
                                arrowstyle='->', mutation_scale=25, 
                                linewidth=3.5, color='#f59e0b')
ax.add_patch(bridge_arrow)

# Bridge label with background
bridge_label_box = FancyBboxPatch((5.8, 7.1), 2.4, 0.6, 
                                   boxstyle="round,pad=0.1", 
                                   edgecolor='#f59e0b', 
                                   facecolor='#fef3c7', 
                                   linewidth=2.5)
ax.add_patch(bridge_label_box)
ax.text(7, 7.4, '⭐ BRIDGE', fontsize=11, ha='center', fontweight='bold', color='#d97706')

# Example section
example_y = 2.5
ax.text(7, example_y + 0.8, 'Real-World Example: Shape + Renderer', 
        fontsize=12, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#e0e7ff', edgecolor='#6366f1', linewidth=2))

# Shapes (Abstraction)
ax.text(2, example_y + 0.2, 'Shapes:', fontsize=9, fontweight='bold', ha='center', color='#8b5cf6')
shapes = ['Circle', 'Square', 'Triangle']
for i, shape in enumerate(shapes):
    shape_box = Rectangle((0.5 + i*1.8, example_y - 0.5), 1.5, 0.5, 
                            edgecolor='#8b5cf6', facecolor='#f3e8ff', linewidth=1.5)
    ax.add_patch(shape_box)
    ax.text(1.25 + i*1.8, example_y - 0.25, shape, fontsize=8, ha='center', fontweight='bold')

# Renderers (Implementation)
ax.text(10, example_y + 0.2, 'Renderers:', fontsize=9, fontweight='bold', ha='center', color='#10b981')
renderers = ['Canvas', 'SVG', 'WebGL']
for i, renderer in enumerate(renderers):
    renderer_box = Rectangle((8.5 + i*1.8, example_y - 0.5), 1.5, 0.5, 
                               edgecolor='#10b981', facecolor='#d1fae5', linewidth=1.5)
    ax.add_patch(renderer_box)
    ax.text(9.25 + i*1.8, example_y - 0.25, renderer, fontsize=8, ha='center', fontweight='bold')

# Bridge connection in example
bridge_example_arrow = FancyArrowPatch((6, example_y - 0.25), (8.5, example_y - 0.25), 
                                        arrowstyle='<->', mutation_scale=15, 
                                        linewidth=2.5, color='#f59e0b')
ax.add_patch(bridge_example_arrow)
ax.text(7.25, example_y - 0.6, 'Bridge', fontsize=8, ha='center', 
        fontweight='bold', color='#d97706', style='italic')

# Without Bridge (Explosion)
ax.text(7, example_y - 1.2, 'Without Bridge: 3 × 3 = 9 classes', fontsize=9, ha='center', 
        color='#dc2626', fontweight='bold')
ax.text(7, example_y - 1.5, 'With Bridge: 3 + 3 = 6 classes', fontsize=9, ha='center', 
        color='#059669', fontweight='bold')

# Benefits box
benefits_box = FancyBboxPatch((0.5, 0.3), 13, 1, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#f59e0b', 
                               facecolor='#fffbeb', 
                               linewidth=2, alpha=0.9)
ax.add_patch(benefits_box)
ax.text(7, 1.1, 'Key Principle: Decouple Abstraction from Implementation', 
        fontsize=11, fontweight='bold', ha='center', color='#d97706')
ax.text(7, 0.8, '✓ Vary independently  •  ✓ Avoid class explosion (n×m → n+m)  •  ✓ Runtime implementation swap', 
        fontsize=9, ha='center')
ax.text(7, 0.5, 'Pattern: Abstraction holds reference to Implementation + delegates operations', 
        fontsize=8, ha='center', family='monospace', style='italic', color='#92400e')

# Annotations
ax.text(3, 6.2, 'extends', fontsize=7, ha='center', 
        style='italic', color='#8b5cf6')
ax.text(11, 6.2, 'implements', fontsize=7, ha='center', 
        style='italic', color='#10b981')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Abstraction'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Implementation'),
    mpatches.Patch(facecolor='#fef3c7', edgecolor='#f59e0b', label='Bridge (Composition)'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=9, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/bridge_pattern.png', dpi=300, bbox_inches='tight')
print("Bridge Pattern diagram saved to docs/images/bridge_pattern.png")

