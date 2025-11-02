#!/usr/bin/env python3
# ./build/diagrams/object_pool_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Object Pool Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Object Pool Container
pool_container = FancyBboxPatch((1, 4), 12, 4, 
                                 boxstyle="round,pad=0.15", 
                                 edgecolor='#8b5cf6', 
                                 facecolor='#faf5ff', 
                                 linewidth=3)
ax.add_patch(pool_container)
ax.text(7, 7.7, 'Object Pool Manager', fontsize=14, fontweight='bold', ha='center', color='#8b5cf6')

# Available Pool (left side)
available_box = FancyBboxPatch((1.5, 4.5), 5, 2.8, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#10b981', 
                                facecolor='#d1fae5', 
                                linewidth=2)
ax.add_patch(available_box)
ax.text(4, 7.1, 'Available Objects', fontsize=11, fontweight='bold', ha='center', color='#059669')

# Available objects (circles)
available_positions = [
    (2.5, 6.3), (3.5, 6.3), (4.5, 6.3), (5.5, 6.3),
    (2.5, 5.5), (3.5, 5.5), (4.5, 5.5), (5.5, 5.5),
    (2.5, 4.8), (3.5, 4.8)
]

for x, y in available_positions:
    obj_circle = Circle((x, y), 0.3, 
                         edgecolor='#10b981', 
                         facecolor='#a7f3d0', 
                         linewidth=1.5)
    ax.add_patch(obj_circle)
    ax.text(x, y, '✓', fontsize=10, ha='center', va='center', fontweight='bold', color='#059669')

# In-Use Pool (right side)
inuse_box = FancyBboxPatch((7.5, 4.5), 5, 2.8, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='#f59e0b', 
                            facecolor='#fef3c7', 
                            linewidth=2)
ax.add_patch(inuse_box)
ax.text(10, 7.1, 'In-Use Objects', fontsize=11, fontweight='bold', ha='center', color='#d97706')

# In-use objects (circles)
inuse_positions = [
    (8.5, 6.3), (9.5, 6.3), (10.5, 6.3),
    (8.5, 5.5), (9.5, 5.5)
]

for x, y in inuse_positions:
    obj_circle = Circle((x, y), 0.3, 
                         edgecolor='#f59e0b', 
                         facecolor='#fcd34d', 
                         linewidth=1.5)
    ax.add_patch(obj_circle)
    ax.text(x, y, '⚙', fontsize=10, ha='center', va='center', color='#d97706')

# Factory function (top)
factory_box = FancyBboxPatch((5.5, 8.5), 3, 0.7, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#6366f1', 
                              facecolor='#e0e7ff', 
                              linewidth=2)
ax.add_patch(factory_box)
ax.text(7, 8.85, 'Factory: () => new Object()', fontsize=9, ha='center', family='monospace', color='#4338ca')

# Clients (bottom)
client_positions = [
    (1, 2, 'Client A'),
    (4, 2, 'Client B'),
    (7, 2, 'Client C'),
    (10, 2, 'Client D'),
    (13, 2, 'Client E')
]

for x, y, label in client_positions:
    client_box = FancyBboxPatch((x, y), 1.5, 0.8, 
                                 boxstyle="round,pad=0.05", 
                                 edgecolor='#0ea5e9', 
                                 facecolor='#e0f2fe', 
                                 linewidth=1.5)
    ax.add_patch(client_box)
    ax.text(x + 0.75, y + 0.55, label, fontsize=9, fontweight='bold', ha='center')
    ax.text(x + 0.75, y + 0.25, 'needs object', fontsize=6, ha='center', style='italic')

# Arrows: Factory creates objects when pool is empty
arrow_factory = FancyArrowPatch((7, 8.5), (4, 7.4), 
                                 arrowstyle='->', mutation_scale=15, 
                                 linewidth=2, color='#6366f1', 
                                 linestyle='dashed')
ax.add_patch(arrow_factory)
ax.text(5.5, 8.2, 'creates new\nif empty', fontsize=7, ha='center', 
        fontweight='bold', color='#4338ca', style='italic')

# Arrows: Clients acquire from available
acquire_clients = [(1.75, 2.8, 3, 5.5), (4.75, 2.8, 4, 5)]
for x1, y1, x2, y2 in acquire_clients:
    arrow = FancyArrowPatch((x1, y1), (x2, y2), 
                             arrowstyle='->', mutation_scale=12, 
                             linewidth=1.5, color='#10b981')
    ax.add_patch(arrow)

ax.text(2.5, 3.5, 'acquire()', fontsize=8, ha='center', 
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#d1fae5', alpha=0.8))

# Arrows: Objects move to in-use
arrow_move = FancyArrowPatch((6.5, 6), (7.5, 6), 
                              arrowstyle='->', mutation_scale=18, 
                              linewidth=2.5, color='#f59e0b')
ax.add_patch(arrow_move)
ax.text(7, 6.3, 'move to in-use', fontsize=8, ha='center', 
        fontweight='bold', color='#d97706', style='italic',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef3c7', alpha=0.8))

# Arrows: Return objects
return_clients = [(10.75, 2.8, 10, 5), (7.75, 2.8, 9, 5)]
for x1, y1, x2, y2 in return_clients:
    arrow = FancyArrowPatch((x1, y1), (x2, y2), 
                             arrowstyle='->', mutation_scale=12, 
                             linewidth=1.5, color='#d97706', 
                             linestyle='dotted')
    ax.add_patch(arrow)

ax.text(11, 3.5, 'release()', fontsize=8, ha='center', 
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef3c7', alpha=0.8))

# Arrows: Objects returned to available (with reset)
arrow_return = FancyArrowPatch((7.5, 5.2), (6.5, 5.2), 
                                arrowstyle='->', mutation_scale=18, 
                                linewidth=2.5, color='#10b981', 
                                linestyle='dashed')
ax.add_patch(arrow_return)
ax.text(7, 4.8, 'reset & return', fontsize=8, ha='center', 
        fontweight='bold', color='#059669', style='italic',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#d1fae5', alpha=0.8))

# Lifecycle flow annotation
lifecycle_box = FancyBboxPatch((0.5, 0.3), 13, 1.2, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#8b5cf6', 
                                facecolor='#f3e8ff', 
                                linewidth=2, alpha=0.9)
ax.add_patch(lifecycle_box)
ax.text(7, 1.3, 'Object Lifecycle: Create Once → Acquire → Use → Release → Reset → Reuse', 
        fontsize=10, fontweight='bold', ha='center', color='#7c3aed')
ax.text(7, 0.95, 'Benefits: ⚡ Eliminate allocation overhead  •  ♻️ Reduce GC pressure  •  🎯 Predictable performance', 
        fontsize=8, ha='center', color='#6d28d9')
ax.text(7, 0.6, 'Pattern: pool.acquire() → use object → pool.release(object) → reset for reuse', 
        fontsize=7, ha='center', family='monospace', style='italic', color='#5b21b6')

# Stats annotation
stats_text = f'Pool Stats: Available={len(available_positions)}  In-Use={len(inuse_positions)}  Total={len(available_positions) + len(inuse_positions)}'
ax.text(7, 4.2, stats_text, fontsize=9, ha='center', 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#8b5cf6', linewidth=1.5),
        fontweight='bold', color='#8b5cf6')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Available (Ready)'),
    mpatches.Patch(facecolor='#fef3c7', edgecolor='#f59e0b', label='In-Use (Borrowed)'),
    mpatches.Patch(facecolor='#e0e7ff', edgecolor='#6366f1', label='Factory (Creates)'),
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Clients (Users)'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/object_pool_pattern.png', dpi=300, bbox_inches='tight')
print("Object Pool Pattern diagram saved to docs/images/object_pool_pattern.png")

