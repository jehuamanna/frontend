#!/usr/bin/env python3
# ./build/diagrams/singleton_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(6, 9.5, 'Singleton Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Singleton Class
singleton_box = FancyBboxPatch((4, 6.5), 4, 2, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#8b5cf6', 
                                facecolor='#f3e8ff', 
                                linewidth=3)
ax.add_patch(singleton_box)
ax.text(6, 8.2, 'Singleton Class', fontsize=13, fontweight='bold', ha='center', color='#8b5cf6')
ax.text(6, 7.85, 'static instance = null', fontsize=9, ha='center', family='monospace', style='italic')
ax.text(6, 7.5, 'constructor() { ... }', fontsize=9, ha='center', family='monospace')
ax.text(6, 7.15, 'static getInstance() {', fontsize=9, ha='center', family='monospace')
ax.text(6, 6.85, '  return instance', fontsize=9, ha='center', family='monospace')
ax.text(6, 6.55, '}', fontsize=9, ha='center', family='monospace')

# Single Instance (highlighted)
instance_box = FancyBboxPatch((4.5, 4), 3, 1.5, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#10b981', 
                               facecolor='#d1fae5', 
                               linewidth=2.5)
ax.add_patch(instance_box)
ax.text(6, 5.2, '⭐ Single Instance', fontsize=12, fontweight='bold', ha='center', color='#059669')
ax.text(6, 4.8, 'state: { ... }', fontsize=9, ha='center', family='monospace')
ax.text(6, 4.5, 'method1()', fontsize=9, ha='center', family='monospace')
ax.text(6, 4.2, 'method2()', fontsize=9, ha='center', family='monospace')

# Multiple Clients
client_positions = [
    (0.5, 2.5, 'Client A'),
    (3.5, 2.5, 'Client B'),
    (6.5, 2.5, 'Client C'),
    (9.5, 2.5, 'Client D')
]

for x, y, label in client_positions:
    client_box = FancyBboxPatch((x, y), 1.8, 1, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='#0ea5e9', 
                                 facecolor='#e0f2fe', 
                                 linewidth=1.5)
    ax.add_patch(client_box)
    ax.text(x + 0.9, y + 0.7, label, fontsize=10, fontweight='bold', ha='center')
    ax.text(x + 0.9, y + 0.3, 'getInstance()', fontsize=7, ha='center', family='monospace')

# Arrows from clients to getInstance
for x, y, label in client_positions:
    arrow = FancyArrowPatch((x + 0.9, y + 1), (6, 6.5), 
                             arrowstyle='->', mutation_scale=15, 
                             linewidth=1.5, color='#0ea5e9', 
                             alpha=0.7)
    ax.add_patch(arrow)

# Arrow from Singleton to Instance
arrow_create = FancyArrowPatch((6, 6.5), (6, 5.5), 
                                arrowstyle='->', mutation_scale=20, 
                                linewidth=2.5, color='#8b5cf6')
ax.add_patch(arrow_create)
ax.text(6.5, 6, 'creates once', fontsize=8, ha='left', 
        fontweight='bold', color='#8b5cf6', style='italic')

# Return arrows (showing all get same instance)
for i, (x, y, label) in enumerate(client_positions):
    arrow_return = FancyArrowPatch((6, 4), (x + 0.9, y + 1), 
                                    arrowstyle='->', mutation_scale=12, 
                                    linewidth=1.5, color='#10b981', 
                                    linestyle='dashed', alpha=0.6)
    ax.add_patch(arrow_return)

ax.text(6, 3.5, 'All clients get same instance', 
        fontsize=9, ha='center', fontweight='bold', 
        style='italic', color='#059669')

# Key principle box
principle_box = FancyBboxPatch((0.5, 0.5), 11, 1.5, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#f59e0b', 
                                facecolor='#fef3c7', 
                                linewidth=2, alpha=0.8)
ax.add_patch(principle_box)
ax.text(6, 1.7, 'Key Principle: Single Instance Shared Globally', 
        fontsize=11, fontweight='bold', ha='center', color='#f59e0b')
ax.text(6, 1.35, '✓ Only ONE instance created  •  ✓ Global access point  •  ✓ Lazy initialization', 
        fontsize=9, ha='center')
ax.text(6, 1, '✓ Controlled access  •  ✓ State consistency  •  ✓ Resource management', 
        fontsize=9, ha='center')
ax.text(6, 0.65, 'Pattern: if (!instance) { instance = new Singleton(); } return instance;', 
        fontsize=8, ha='center', family='monospace', style='italic', color='#92400e')

# Flow annotation
ax.text(2, 5, '1. Request', fontsize=8, ha='center', 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#dbeafe', alpha=0.9))
ax.text(9, 5, '2. Return', fontsize=8, ha='center', 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#d1fae5', alpha=0.9))

# Warning annotation
ax.text(10.5, 8, '⚠️ Caution:', fontsize=9, fontweight='bold', ha='center', color='#dc2626')
ax.text(10.5, 7.6, 'Global state', fontsize=7, ha='center', color='#dc2626')
ax.text(10.5, 7.3, 'Testing challenges', fontsize=7, ha='center', color='#dc2626')
ax.text(10.5, 7, 'Hidden dependencies', fontsize=7, ha='center', color='#dc2626')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Singleton Class'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Single Instance'),
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Clients'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=9)

plt.tight_layout()
plt.savefig('docs/images/singleton_pattern.png', dpi=300, bbox_inches='tight')
print("Singleton Pattern diagram saved to docs/images/singleton_pattern.png")

