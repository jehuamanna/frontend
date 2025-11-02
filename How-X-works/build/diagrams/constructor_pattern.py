#!/usr/bin/env python3
# ./build/diagrams/constructor_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Constructor Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Constructor Class
constructor_box = FancyBboxPatch((0.5, 6), 2.5, 2, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#2563eb', 
                                  facecolor='#dbeafe', 
                                  linewidth=2)
ax.add_patch(constructor_box)
ax.text(1.75, 7.5, 'Constructor', fontsize=12, fontweight='bold', ha='center')
ax.text(1.75, 7.1, 'class User {', fontsize=9, ha='center', family='monospace')
ax.text(1.75, 6.8, '  constructor()', fontsize=9, ha='center', family='monospace')
ax.text(1.75, 6.5, '  methods()', fontsize=9, ha='center', family='monospace')
ax.text(1.75, 6.2, '}', fontsize=9, ha='center', family='monospace')

# Prototype
prototype_box = FancyBboxPatch((4, 6), 2.5, 2, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#7c3aed', 
                                facecolor='#ede9fe', 
                                linewidth=2)
ax.add_patch(prototype_box)
ax.text(5.25, 7.5, 'User.prototype', fontsize=12, fontweight='bold', ha='center')
ax.text(5.25, 7.1, 'getFullInfo()', fontsize=9, ha='center', family='monospace')
ax.text(5.25, 6.8, 'deactivate()', fontsize=9, ha='center', family='monospace')
ax.text(5.25, 6.5, 'updateRole()', fontsize=9, ha='center', family='monospace')

# Instance 1
instance1_box = FancyBboxPatch((1, 3), 2, 1.8, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#059669', 
                                facecolor='#d1fae5', 
                                linewidth=2)
ax.add_patch(instance1_box)
ax.text(2, 4.3, 'alice', fontsize=11, fontweight='bold', ha='center')
ax.text(2, 3.9, 'name: "Alice"', fontsize=8, ha='center', family='monospace')
ax.text(2, 3.6, 'email: "alice@..."', fontsize=8, ha='center', family='monospace')
ax.text(2, 3.3, 'role: "admin"', fontsize=8, ha='center', family='monospace')

# Instance 2
instance2_box = FancyBboxPatch((4, 3), 2, 1.8, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#059669', 
                                facecolor='#d1fae5', 
                                linewidth=2)
ax.add_patch(instance2_box)
ax.text(5, 4.3, 'bob', fontsize=11, fontweight='bold', ha='center')
ax.text(5, 3.9, 'name: "Bob"', fontsize=8, ha='center', family='monospace')
ax.text(5, 3.6, 'email: "bob@..."', fontsize=8, ha='center', family='monospace')
ax.text(5, 3.3, 'role: "user"', fontsize=8, ha='center', family='monospace')

# Instance 3
instance3_box = FancyBboxPatch((7, 3), 2, 1.8, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#059669', 
                                facecolor='#d1fae5', 
                                linewidth=2)
ax.add_patch(instance3_box)
ax.text(8, 4.3, 'charlie', fontsize=11, fontweight='bold', ha='center')
ax.text(8, 3.9, 'name: "Charlie"', fontsize=8, ha='center', family='monospace')
ax.text(8, 3.6, 'email: "charlie@..."', fontsize=8, ha='center', family='monospace')
ax.text(8, 3.3, 'role: "moderator"', fontsize=8, ha='center', family='monospace')

# Arrow from Constructor to Prototype
arrow1 = FancyArrowPatch((3, 7), (4, 7), 
                         arrowstyle='->', mutation_scale=20, 
                         linewidth=2, color='#7c3aed')
ax.add_patch(arrow1)
ax.text(3.5, 7.3, 'has', fontsize=9, ha='center', style='italic')

# Arrows from instances to prototype (delegation)
for i, x in enumerate([2, 5, 8]):
    arrow = FancyArrowPatch((x, 4.8), (5.25, 6), 
                            arrowstyle='->', mutation_scale=15, 
                            linewidth=1.5, color='#7c3aed', 
                            linestyle='dashed', alpha=0.6)
    ax.add_patch(arrow)

# Arrows from constructor to instances (creates)
for x in [2, 5, 8]:
    arrow = FancyArrowPatch((1.75, 6), (x, 4.8), 
                            arrowstyle='->', mutation_scale=15, 
                            linewidth=1.5, color='#2563eb', 
                            alpha=0.7)
    ax.add_patch(arrow)

# "new" keyword annotation
ax.text(1.75, 5.3, 'new User(...)', fontsize=10, ha='center', 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef3c7', edgecolor='#f59e0b'))

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#dbeafe', edgecolor='#2563eb', label='Constructor'),
    mpatches.Patch(facecolor='#ede9fe', edgecolor='#7c3aed', label='Prototype'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#059669', label='Instance'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10)

# Flow explanation
ax.text(5, 1.5, 'Prototype Chain: instance.__proto__ → Constructor.prototype', 
        fontsize=9, ha='center', style='italic', 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f3f4f6', alpha=0.8))

ax.text(5, 0.8, 'Shared methods in prototype save memory', 
        fontsize=9, ha='center', style='italic', color='#6b7280')

plt.tight_layout()
plt.savefig('docs/images/constructor_pattern.png', dpi=300, bbox_inches='tight')
print("Constructor Pattern diagram saved to docs/images/constructor_pattern.png")

