#!/usr/bin/env python3
# ./build/diagrams/flyweight_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Flyweight Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# FlyweightFactory
factory_box = FancyBboxPatch((0.5, 6.5), 3, 2, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#8b5cf6', 
                              facecolor='#f3e8ff', 
                              linewidth=2.5)
ax.add_patch(factory_box)
ax.text(2, 8.1, 'FlyweightFactory', fontsize=11, fontweight='bold', ha='center', color='#7c3aed')
ax.text(2, 7.75, '- flyweights: Map', fontsize=8, ha='center', family='monospace', style='italic')
ax.text(2, 7.45, '+ getFlyweight(key) {', fontsize=8, ha='center', family='monospace')
ax.text(2, 7.15, '  if (!exists) create', fontsize=7, ha='center', family='monospace', style='italic')
ax.text(2, 6.85, '  return cached', fontsize=7, ha='center', family='monospace', style='italic')
ax.text(2, 6.6, '}', fontsize=8, ha='center', family='monospace')

# Flyweight (Shared - Intrinsic State)
flyweight_box = FancyBboxPatch((5, 6.5), 3.5, 2, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#10b981', 
                                facecolor='#d1fae5', 
                                linewidth=2.5)
ax.add_patch(flyweight_box)
ax.text(6.75, 8.1, 'Flyweight', fontsize=12, fontweight='bold', ha='center', color='#059669')
ax.text(6.75, 7.75, 'Intrinsic State', fontsize=9, ha='center', style='italic', color='#059669')
ax.text(6.75, 7.4, '(Shared/Immutable)', fontsize=8, ha='center', style='italic')
ax.text(6.75, 7.05, '+ color', fontsize=8, ha='center', family='monospace')
ax.text(6.75, 6.75, '+ texture', fontsize=8, ha='center', family='monospace')
ax.text(6.75, 6.55, '+ operation(extrinsic)', fontsize=7, ha='center', family='monospace')

# Arrow: Factory creates/caches Flyweights
arrow_factory = FancyArrowPatch((3.5, 7.5), (5, 7.5), 
                                 arrowstyle='->', mutation_scale=20, 
                                 linewidth=2.5, color='#8b5cf6')
ax.add_patch(arrow_factory)
ax.text(4.25, 7.85, 'creates/caches', fontsize=8, ha='center', 
        fontweight='bold', color='#7c3aed', style='italic')

# Context Objects (Multiple instances with extrinsic state)
context_y_positions = [4.5, 3, 1.5]
context_labels = ['Context 1', 'Context 2', 'Context 3']

for i, (y, label) in enumerate(zip(context_y_positions, context_labels)):
    context_box = FancyBboxPatch((9.5, y), 4, 1.2, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#f59e0b', 
                                  facecolor='#fef3c7', 
                                  linewidth=2)
    ax.add_patch(context_box)
    ax.text(11.5, y + 0.8, label, fontsize=10, fontweight='bold', ha='center', color='#d97706')
    ax.text(11.5, y + 0.5, f'Extrinsic State (x={10+i*10}, y={20+i*10})', fontsize=7, ha='center', style='italic')
    ax.text(11.5, y + 0.2, '- flyweight: Flyweight', fontsize=7, ha='center', family='monospace', style='italic')

# Arrows: Contexts reference shared Flyweight
for y in context_y_positions:
    arrow = FancyArrowPatch((9.5, y + 0.6), (8.5, 7.5), 
                             arrowstyle='->', mutation_scale=15, 
                             linewidth=2, color='#f59e0b', 
                             linestyle='dashed')
    ax.add_patch(arrow)

ax.text(9, 4.5, 'all reference\nsame Flyweight', fontsize=8, ha='center', 
        fontweight='bold', color='#d97706', style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef3c7', alpha=0.9))

# Visual comparison (top right)
compare_x = 5
compare_y = 9

# Memory usage visualization
ax.text(9, compare_y, 'Memory Comparison', fontsize=11, fontweight='bold', 
        ha='left', color='#6366f1',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#e0e7ff', edgecolor='#6366f1', linewidth=2))

# Without Flyweight
without_y = compare_y - 0.7
ax.text(9, without_y, 'Without Flyweight:', fontsize=9, fontweight='bold', ha='left', color='#dc2626')
for i in range(10):
    small_box = Rectangle((9 + i * 0.35, without_y - 0.4), 0.3, 0.3, 
                            edgecolor='#dc2626', facecolor='#fee2e2', linewidth=1)
    ax.add_patch(small_box)
ax.text(11.75, without_y - 0.25, '= 10 objects', fontsize=7, ha='left')
ax.text(11.75, without_y - 0.45, '(all data duplicated)', fontsize=6, ha='left', style='italic')

# With Flyweight
with_y = without_y - 1
ax.text(9, with_y, 'With Flyweight:', fontsize=9, fontweight='bold', ha='left', color='#10b981')
# Shared flyweight
large_box = Rectangle((9, with_y - 0.5), 0.6, 0.4, 
                        edgecolor='#10b981', facecolor='#d1fae5', linewidth=2)
ax.add_patch(large_box)
ax.text(9.3, with_y - 0.3, 'F', fontsize=10, ha='center', fontweight='bold', color='#059669')

# Contexts
for i in range(10):
    tiny_box = Circle((9.8 + i * 0.25, with_y - 0.3), 0.08, 
                       edgecolor='#f59e0b', facecolor='#fef3c7', linewidth=0.8)
    ax.add_patch(tiny_box)
    # Arrow to shared flyweight
    if i < 3:  # Show only a few arrows for clarity
        ax.plot([9.8 + i * 0.25, 9.3], [with_y - 0.3, with_y - 0.3], 
                'k-', linewidth=0.5, alpha=0.3)

ax.text(11.75, with_y - 0.2, '= 1 flyweight', fontsize=7, ha='left')
ax.text(11.75, with_y - 0.4, '+ 10 contexts', fontsize=7, ha='left')
ax.text(11.75, with_y - 0.6, '(shared data)', fontsize=6, ha='left', style='italic', color='#10b981')

# Savings annotation
ax.text(12, with_y - 1, '90% memory saved!', fontsize=9, fontweight='bold', 
        ha='center', color='#10b981',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#d1fae5'))

# Benefits box (bottom)
benefits_box = FancyBboxPatch((0.5, 0.3), 13, 1, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#10b981', 
                               facecolor='#ecfdf5', 
                               linewidth=2, alpha=0.9)
ax.add_patch(benefits_box)
ax.text(7, 1.1, 'Key Principle: Share Intrinsic State to Minimize Memory Usage', 
        fontsize=11, fontweight='bold', ha='center', color='#059669')
ax.text(7, 0.8, '✓ Separate intrinsic (shared) from extrinsic (unique) state  •  ✓ Factory manages sharing  •  ✓ Massive memory savings', 
        fontsize=9, ha='center')
ax.text(7, 0.5, 'Pattern: Factory caches Flyweights + Contexts hold extrinsic state + reference shared Flyweights', 
        fontsize=8, ha='center', family='monospace', style='italic', color='#065f46')

# Annotations
ax.text(1, 5.5, '1. Request flyweight', fontsize=7, ha='left', 
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#dbeafe', alpha=0.9))
ax.text(5, 5.5, '2. Return cached', fontsize=7, ha='left', 
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#d1fae5', alpha=0.9))
ax.text(9.5, 6, '3. Many contexts\nshare one flyweight', fontsize=7, ha='left', 
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef3c7', alpha=0.9))

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Factory (Manages Sharing)'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Flyweight (Intrinsic/Shared)'),
    mpatches.Patch(facecolor='#fef3c7', edgecolor='#f59e0b', label='Context (Extrinsic/Unique)'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/flyweight_pattern.png', dpi=300, bbox_inches='tight')
print("Flyweight Pattern diagram saved to docs/images/flyweight_pattern.png")

