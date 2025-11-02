#!/usr/bin/env python3
# ./build/diagrams/facade_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Facade Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Client
client_box = FancyBboxPatch((0.5, 6.5), 2.5, 1.5, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#0ea5e9', 
                             facecolor='#e0f2fe', 
                             linewidth=2.5)
ax.add_patch(client_box)
ax.text(1.75, 7.7, 'Client', fontsize=13, fontweight='bold', ha='center', color='#0369a1')
ax.text(1.75, 7.3, 'uses simple', fontsize=9, ha='center', style='italic')
ax.text(1.75, 7, 'interface', fontsize=9, ha='center', style='italic')

# Facade (central)
facade_box = FancyBboxPatch((4.5, 6), 5, 2.5, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#8b5cf6', 
                             facecolor='#f3e8ff', 
                             linewidth=3.5)
ax.add_patch(facade_box)
ax.text(7, 8.2, 'FACADE', fontsize=14, fontweight='bold', ha='center', color='#7c3aed')
ax.text(7, 7.8, 'Simplified Interface', fontsize=10, ha='center', style='italic', color='#7c3aed')
ax.text(7, 7.45, '+ simpleMethod1()', fontsize=9, ha='center', family='monospace')
ax.text(7, 7.15, '+ simpleMethod2()', fontsize=9, ha='center', family='monospace')
ax.text(7, 6.85, '+ complexOperationSimplified() {', fontsize=8, ha='center', family='monospace')
ax.text(7, 6.55, '  subsystem1.op()', fontsize=7, ha='center', family='monospace', style='italic')
ax.text(7, 6.25, '  subsystem2.op()', fontsize=7, ha='center', family='monospace', style='italic')

# Arrow: Client to Facade
arrow_client = FancyArrowPatch((3, 7.25), (4.5, 7.25), 
                                arrowstyle='->', mutation_scale=20, 
                                linewidth=2.5, color='#0ea5e9')
ax.add_patch(arrow_client)
ax.text(3.75, 7.6, 'uses', fontsize=9, ha='center', fontweight='bold', color='#0369a1')

# Complex Subsystem (multiple classes)
subsystem_container = FancyBboxPatch((10.5, 1), 3, 7.5, 
                                      boxstyle="round,pad=0.15", 
                                      edgecolor='#f59e0b', 
                                      facecolor='#fffbeb', 
                                      linewidth=2.5, alpha=0.3)
ax.add_patch(subsystem_container)
ax.text(12, 8.2, 'Complex Subsystem', fontsize=11, fontweight='bold', 
        ha='center', color='#d97706')

# Subsystem classes
subsystem_classes = [
    (10.7, 6.8, 'SubsystemClass1'),
    (10.7, 5.6, 'SubsystemClass2'),
    (10.7, 4.4, 'SubsystemClass3'),
    (10.7, 3.2, 'SubsystemClass4'),
    (10.7, 2, 'SubsystemClass5'),
    (10.7, 1.2, '... more classes')
]

for x, y, label in subsystem_classes[:-1]:
    box = FancyBboxPatch((x, y), 2.5, 0.8, 
                          boxstyle="round,pad=0.05", 
                          edgecolor='#f59e0b', 
                          facecolor='#fef3c7', 
                          linewidth=1.5)
    ax.add_patch(box)
    ax.text(x + 1.25, y + 0.55, label, fontsize=8, fontweight='bold', ha='center', color='#d97706')
    ax.text(x + 1.25, y + 0.25, '+ complexOp()', fontsize=6, ha='center', family='monospace')

# Last item (ellipsis)
ax.text(12, 1.2, '... more classes', fontsize=8, ha='center', 
        style='italic', color='#92400e')

# Arrows: Facade to Subsystem (showing delegation)
arrow_positions = [
    (9.5, 7.5, 11.95, 7.2),
    (9.5, 7.2, 11.95, 6),
    (9.5, 6.9, 11.95, 4.8),
    (9.5, 6.6, 11.95, 3.6),
    (9.5, 6.3, 11.95, 2.4)
]

for x1, y1, x2, y2 in arrow_positions:
    arrow = FancyArrowPatch((x1, y1), (x2, y2), 
                             arrowstyle='->', mutation_scale=12, 
                             linewidth=1.5, color='#8b5cf6', 
                             alpha=0.6)
    ax.add_patch(arrow)

ax.text(10.5, 5, 'delegates', fontsize=8, ha='center', 
        fontweight='bold', color='#7c3aed', style='italic',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#f3e8ff', alpha=0.8))

# Comparison diagram (bottom)
compare_y = 0.5

# Without Facade
without_box = FancyBboxPatch((0.5, compare_y - 2.5), 6, 2, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#dc2626', 
                              facecolor='#fee2e2', 
                              linewidth=2, alpha=0.8)
ax.add_patch(without_box)
ax.text(3.5, compare_y - 0.7, '❌ Without Facade', fontsize=10, fontweight='bold', 
        ha='center', color='#dc2626')
ax.text(3.5, compare_y - 1.1, '• Client knows all subsystem classes', fontsize=7, ha='center')
ax.text(3.5, compare_y - 1.4, '• Tight coupling', fontsize=7, ha='center')
ax.text(3.5, compare_y - 1.7, '• Complex initialization', fontsize=7, ha='center')
ax.text(3.5, compare_y - 2, '• Hard to test', fontsize=7, ha='center')
ax.text(3.5, compare_y - 2.3, '• Changes ripple through client code', fontsize=7, ha='center')

# With Facade
with_box = FancyBboxPatch((7.5, compare_y - 2.5), 6, 2, 
                           boxstyle="round,pad=0.1", 
                           edgecolor='#10b981', 
                           facecolor='#d1fae5', 
                           linewidth=2, alpha=0.8)
ax.add_patch(with_box)
ax.text(10.5, compare_y - 0.7, '✓ With Facade', fontsize=10, fontweight='bold', 
        ha='center', color='#059669')
ax.text(10.5, compare_y - 1.1, '• Client uses simple interface', fontsize=7, ha='center')
ax.text(10.5, compare_y - 1.4, '• Loose coupling', fontsize=7, ha='center')
ax.text(10.5, compare_y - 1.7, '• Easy to use', fontsize=7, ha='center')
ax.text(10.5, compare_y - 2, '• Easy to test (mock facade)', fontsize=7, ha='center')
ax.text(10.5, compare_y - 2.3, '• Subsystem changes isolated', fontsize=7, ha='center')

# Example annotation
ax.text(0.8, 5, 'Example:', fontsize=8, fontweight='bold', ha='left')
ax.text(0.8, 4.7, 'jQuery = Facade', fontsize=7, ha='left')
ax.text(0.8, 4.45, 'over DOM API', fontsize=7, ha='left', style='italic')

# Benefits box (top)
benefits_box = FancyBboxPatch((0.5, 8.8), 9, 0.6, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#8b5cf6', 
                               facecolor='#f5f3ff', 
                               linewidth=2, alpha=0.9)
ax.add_patch(benefits_box)
ax.text(5, 9.1, 'Key Principle: Simplify Complex Subsystems with Unified Interface', 
        fontsize=10, fontweight='bold', ha='center', color='#7c3aed')

# Pattern formula
pattern_box = FancyBboxPatch((0.5, compare_y - 3.3), 13, 0.6, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#6366f1', 
                              facecolor='#e0e7ff', 
                              linewidth=2, alpha=0.9)
ax.add_patch(pattern_box)
ax.text(7, compare_y - 3, 'Pattern: Facade coordinates subsystem operations + provides high-level interface', 
        fontsize=8, ha='center', family='monospace', style='italic', color='#4338ca')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Client'),
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Facade'),
    mpatches.Patch(facecolor='#fef3c7', edgecolor='#f59e0b', label='Subsystem Classes'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/facade_pattern.png', dpi=300, bbox_inches='tight')
print("Facade Pattern diagram saved to docs/images/facade_pattern.png")

