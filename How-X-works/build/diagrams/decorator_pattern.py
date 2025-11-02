#!/usr/bin/env python3
# ./build/diagrams/decorator_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Decorator Pattern Architecture', 
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

# ConcreteComponent
concrete_box = FancyBboxPatch((0.5, 5), 3.5, 1.5, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#10b981', 
                               facecolor='#d1fae5', 
                               linewidth=2.5)
ax.add_patch(concrete_box)
ax.text(2.25, 6.15, 'ConcreteComponent', fontsize=11, fontweight='bold', ha='center', color='#059669')
ax.text(2.25, 5.75, '+ operation() {', fontsize=9, ha='center', family='monospace')
ax.text(2.25, 5.45, '  // base behavior', fontsize=8, ha='center', family='monospace', style='italic')
ax.text(2.25, 5.2, '}', fontsize=9, ha='center', family='monospace')

# Decorator (Abstract)
decorator_box = FancyBboxPatch((9.5, 5), 4, 1.5, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#f59e0b', 
                                facecolor='#fef3c7', 
                                linewidth=2.5)
ax.add_patch(decorator_box)
ax.text(11.5, 6.15, 'Decorator', fontsize=12, fontweight='bold', ha='center', color='#d97706')
ax.text(11.5, 5.8, '- component', fontsize=9, ha='center', family='monospace', style='italic')
ax.text(11.5, 5.5, '+ operation() {', fontsize=8, ha='center', family='monospace')
ax.text(11.5, 5.2, '  component.operation()', fontsize=8, ha='center', family='monospace')

# ConcreteDecoratorA
decoratorA_box = FancyBboxPatch((7, 2.5), 2, 1.5, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='#f59e0b', 
                                 facecolor='#fffbeb', 
                                 linewidth=2)
ax.add_patch(decoratorA_box)
ax.text(8, 3.7, 'DecoratorA', fontsize=10, fontweight='bold', ha='center', color='#d97706')
ax.text(8, 3.35, '+ operation() {', fontsize=8, ha='center', family='monospace')
ax.text(8, 3.05, '  super.operation()', fontsize=7, ha='center', family='monospace')
ax.text(8, 2.75, '  addedBehaviorA()', fontsize=7, ha='center', family='monospace')

# ConcreteDecoratorB
decoratorB_box = FancyBboxPatch((10, 2.5), 2, 1.5, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='#f59e0b', 
                                 facecolor='#fffbeb', 
                                 linewidth=2)
ax.add_patch(decoratorB_box)
ax.text(11, 3.7, 'DecoratorB', fontsize=10, fontweight='bold', ha='center', color='#d97706')
ax.text(11, 3.35, '+ operation() {', fontsize=8, ha='center', family='monospace')
ax.text(11, 3.05, '  super.operation()', fontsize=7, ha='center', family='monospace')
ax.text(11, 2.75, '  addedBehaviorB()', fontsize=7, ha='center', family='monospace')

# Inheritance arrows
arrow_concrete = FancyArrowPatch((2.25, 6.5), (6, 8.2), 
                                  arrowstyle='->', mutation_scale=20, 
                                  linewidth=2.5, color='#8b5cf6', 
                                  linestyle='dashed')
ax.add_patch(arrow_concrete)
ax.text(3.5, 7.5, 'implements', fontsize=8, ha='center', 
        style='italic', color='#7c3aed', fontweight='bold')

arrow_decorator = FancyArrowPatch((11.5, 6.5), (8, 8.2), 
                                   arrowstyle='->', mutation_scale=20, 
                                   linewidth=2.5, color='#8b5cf6', 
                                   linestyle='dashed')
ax.add_patch(arrow_decorator)
ax.text(10.5, 7.5, 'implements', fontsize=8, ha='center', 
        style='italic', color='#7c3aed', fontweight='bold')

# Decorator inheritance
arrow_decA = FancyArrowPatch((8, 4), (10.5, 5), 
                              arrowstyle='->', mutation_scale=15, 
                              linewidth=2, color='#f59e0b', 
                              linestyle='dashed')
ax.add_patch(arrow_decA)

arrow_decB = FancyArrowPatch((11, 4), (11.5, 5), 
                              arrowstyle='->', mutation_scale=15, 
                              linewidth=2, color='#f59e0b', 
                              linestyle='dashed')
ax.add_patch(arrow_decB)

ax.text(9.5, 4.3, 'extends', fontsize=7, ha='center', 
        style='italic', color='#d97706')

# Composition: Decorator contains Component
arrow_contains = FancyArrowPatch((9.5, 5.75), (7, 8.2), 
                                  arrowstyle='->', mutation_scale=20, 
                                  linewidth=2.5, color='#6366f1')
ax.add_patch(arrow_contains)
ax.text(8.5, 6.8, 'wraps', fontsize=9, ha='center', 
        fontweight='bold', color='#4f46e5', style='italic')

# Visual example (Wrapping/Stacking)
visual_y = 1.2
ax.text(1.5, visual_y, 'Visual: Decorator Stacking', fontsize=11, fontweight='bold', 
        ha='left', color='#6366f1',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#e0e7ff', edgecolor='#6366f1', linewidth=2))

# Core component
core = Circle((2, visual_y - 1), 0.3, edgecolor='#10b981', facecolor='#d1fae5', linewidth=2)
ax.add_patch(core)
ax.text(2, visual_y - 1, 'Core', fontsize=7, ha='center', va='center', fontweight='bold')

# First decorator wrapping
dec1_circle = Circle((2, visual_y - 1), 0.45, edgecolor='#f59e0b', 
                      facecolor='none', linewidth=2, linestyle='dashed')
ax.add_patch(dec1_circle)
ax.text(2, visual_y - 1.6, 'DecoratorA', fontsize=7, ha='center', color='#d97706')

# Second decorator wrapping
dec2_circle = Circle((2, visual_y - 1), 0.6, edgecolor='#f59e0b', 
                      facecolor='none', linewidth=2, linestyle='dotted')
ax.add_patch(dec2_circle)
ax.text(2, visual_y - 1.8, 'DecoratorB', fontsize=7, ha='center', color='#d97706')

# Flow diagram
flow_start_x = 5
flow_y = visual_y - 1

# Client
client_box = Rectangle((flow_start_x, flow_y - 0.3), 1.2, 0.6, 
                         edgecolor='#0ea5e9', facecolor='#e0f2fe', linewidth=1.5)
ax.add_patch(client_box)
ax.text(flow_start_x + 0.6, flow_y, 'Client', fontsize=8, ha='center', fontweight='bold')

# DecoratorB
decB_flow = Rectangle((flow_start_x + 2, flow_y - 0.3), 1.2, 0.6, 
                        edgecolor='#f59e0b', facecolor='#fef3c7', linewidth=1.5)
ax.add_patch(decB_flow)
ax.text(flow_start_x + 2.6, flow_y, 'DecB', fontsize=7, ha='center', fontweight='bold')

# DecoratorA
decA_flow = Rectangle((flow_start_x + 3.8, flow_y - 0.3), 1.2, 0.6, 
                        edgecolor='#f59e0b', facecolor='#fef3c7', linewidth=1.5)
ax.add_patch(decA_flow)
ax.text(flow_start_x + 4.4, flow_y, 'DecA', fontsize=7, ha='center', fontweight='bold')

# Core
core_flow = Rectangle((flow_start_x + 5.6, flow_y - 0.3), 1.2, 0.6, 
                        edgecolor='#10b981', facecolor='#d1fae5', linewidth=1.5)
ax.add_patch(core_flow)
ax.text(flow_start_x + 6.2, flow_y, 'Core', fontsize=7, ha='center', fontweight='bold')

# Flow arrows
for i in range(3):
    x_start = flow_start_x + 1.2 + i * 1.8
    x_end = x_start + 0.8
    arrow_flow = FancyArrowPatch((x_start, flow_y), (x_end, flow_y), 
                                  arrowstyle='->', mutation_scale=10, 
                                  linewidth=1.5, color='#6366f1')
    ax.add_patch(arrow_flow)

ax.text(flow_start_x + 3.5, flow_y - 0.7, 'calls →', fontsize=7, ha='center', 
        style='italic', color='#6366f1')

# Benefits box
benefits_box = FancyBboxPatch((0.5, visual_y - 3), 13, 1, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#f59e0b', 
                               facecolor='#fffbeb', 
                               linewidth=2, alpha=0.9)
ax.add_patch(benefits_box)
ax.text(7, visual_y - 2.2, 'Key Principle: Add Behavior Dynamically Through Wrapping', 
        fontsize=11, fontweight='bold', ha='center', color='#d97706')
ax.text(7, visual_y - 2.5, '✓ Runtime composition  •  ✓ Single Responsibility  •  ✓ Open/Closed (extend without modifying)', 
        fontsize=9, ha='center')
ax.text(7, visual_y - 2.8, 'Pattern: Decorator wraps Component + adds behavior + delegates to wrapped component', 
        fontsize=8, ha='center', family='monospace', style='italic', color='#92400e')

# Annotations
ax.text(2.25, 4.7, 'Original\nobject', fontsize=7, ha='center', 
        style='italic', color='#059669')
ax.text(11.5, 4.7, 'Wrapper that\nadds behavior', fontsize=7, ha='center', 
        style='italic', color='#d97706')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Component (Interface)'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='ConcreteComponent'),
    mpatches.Patch(facecolor='#fef3c7', edgecolor='#f59e0b', label='Decorators (Wrappers)'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/decorator_pattern.png', dpi=300, bbox_inches='tight')
print("Decorator Pattern diagram saved to docs/images/decorator_pattern.png")

