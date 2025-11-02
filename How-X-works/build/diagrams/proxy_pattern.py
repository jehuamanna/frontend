#!/usr/bin/env python3
# ./build/diagrams/proxy_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Proxy Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Subject (Interface)
subject_box = FancyBboxPatch((5, 7.5), 4, 1.5, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#8b5cf6', 
                              facecolor='#f3e8ff', 
                              linewidth=3)
ax.add_patch(subject_box)
ax.text(7, 8.7, '«interface»', fontsize=9, ha='center', style='italic', color='#7c3aed')
ax.text(7, 8.35, 'Subject', fontsize=13, fontweight='bold', ha='center', color='#7c3aed')
ax.text(7, 8, '+ request()', fontsize=9, ha='center', family='monospace')

# RealSubject
real_box = FancyBboxPatch((1, 5), 3.5, 1.5, 
                           boxstyle="round,pad=0.1", 
                           edgecolor='#10b981', 
                           facecolor='#d1fae5', 
                           linewidth=2.5)
ax.add_patch(real_box)
ax.text(2.75, 6.15, 'RealSubject', fontsize=11, fontweight='bold', ha='center', color='#059669')
ax.text(2.75, 5.75, '+ request() {', fontsize=9, ha='center', family='monospace')
ax.text(2.75, 5.45, '  // actual work', fontsize=8, ha='center', family='monospace', style='italic')
ax.text(2.75, 5.2, '}', fontsize=9, ha='center', family='monospace')

# Proxy
proxy_box = FancyBboxPatch((9.5, 5), 4, 1.5, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='#f59e0b', 
                            facecolor='#fef3c7', 
                            linewidth=2.5)
ax.add_patch(proxy_box)
ax.text(11.5, 6.15, 'Proxy', fontsize=12, fontweight='bold', ha='center', color='#d97706')
ax.text(11.5, 5.8, '- realSubject', fontsize=9, ha='center', family='monospace', style='italic')
ax.text(11.5, 5.5, '+ request() {', fontsize=8, ha='center', family='monospace')
ax.text(11.5, 5.2, '  // control logic', fontsize=7, ha='center', family='monospace', style='italic')

# Client
client_box = FancyBboxPatch((5.5, 3), 3, 1.3, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#0ea5e9', 
                             facecolor='#e0f2fe', 
                             linewidth=2.5)
ax.add_patch(client_box)
ax.text(7, 4, 'Client', fontsize=12, fontweight='bold', ha='center', color='#0369a1')
ax.text(7, 3.65, 'works with', fontsize=9, ha='center', style='italic')
ax.text(7, 3.35, 'Subject interface', fontsize=9, ha='center', style='italic')

# Arrows
# RealSubject implements Subject
arrow_real = FancyArrowPatch((2.75, 6.5), (6, 8.2), 
                              arrowstyle='->', mutation_scale=20, 
                              linewidth=2.5, color='#8b5cf6', 
                              linestyle='dashed')
ax.add_patch(arrow_real)
ax.text(4, 7.5, 'implements', fontsize=8, ha='center', 
        style='italic', color='#7c3aed', fontweight='bold')

# Proxy implements Subject
arrow_proxy = FancyArrowPatch((11.5, 6.5), (8, 8.2), 
                               arrowstyle='->', mutation_scale=20, 
                               linewidth=2.5, color='#8b5cf6', 
                               linestyle='dashed')
ax.add_patch(arrow_proxy)
ax.text(10.5, 7.5, 'implements', fontsize=8, ha='center', 
        style='italic', color='#7c3aed', fontweight='bold')

# Proxy delegates to RealSubject
arrow_delegates = FancyArrowPatch((9.5, 5.75), (4.5, 5.75), 
                                   arrowstyle='->', mutation_scale=20, 
                                   linewidth=2.5, color='#f59e0b')
ax.add_patch(arrow_delegates)
ax.text(7, 6.1, 'delegates to', fontsize=9, ha='center', 
        fontweight='bold', color='#d97706', style='italic')

# Client uses Subject
arrow_client = FancyArrowPatch((7, 4.3), (7, 7.5), 
                                arrowstyle='->', mutation_scale=20, 
                                linewidth=2.5, color='#0ea5e9')
ax.add_patch(arrow_client)
ax.text(7.5, 5.5, 'uses', fontsize=9, ha='left', 
        fontweight='bold', color='#0369a1')

# Types of Proxies (bottom section)
types_y = 2
ax.text(7, types_y - 0.3, 'Common Proxy Types', fontsize=12, fontweight='bold', 
        ha='center', color='#6366f1',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#e0e7ff', edgecolor='#6366f1', linewidth=2))

proxy_types = [
    (0.5, types_y - 1.5, 'Virtual Proxy\nLazy initialization'),
    (3.5, types_y - 1.5, 'Protection Proxy\nAccess control'),
    (6.5, types_y - 1.5, 'Remote Proxy\nRemote object\nrepresentative'),
    (9.5, types_y - 1.5, 'Caching Proxy\nCache results'),
    (12.5, types_y - 1.5, 'Logging Proxy\nLog operations')
]

for x, y, label in proxy_types:
    box = FancyBboxPatch((x, y), 2, 0.9, 
                          boxstyle="round,pad=0.05", 
                          edgecolor='#f59e0b', 
                          facecolor='#fffbeb', 
                          linewidth=1.5, alpha=0.8)
    ax.add_patch(box)
    lines = label.split('\n')
    for i, line in enumerate(lines):
        ax.text(x + 1, y + 0.7 - i * 0.25, line, fontsize=7, ha='center', 
                fontweight='bold' if i == 0 else 'normal',
                color='#d97706' if i == 0 else '#92400e')

# Benefits box (bottom)
benefits_box = FancyBboxPatch((0.5, types_y - 3.5), 13, 1, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#f59e0b', 
                               facecolor='#fffbeb', 
                               linewidth=2, alpha=0.9)
ax.add_patch(benefits_box)
ax.text(7, types_y - 2.7, 'Key Principle: Control Access Through Intermediary', 
        fontsize=11, fontweight='bold', ha='center', color='#d97706')
ax.text(7, types_y - 3, '✓ Same interface as real object  •  ✓ Adds control logic (lazy, security, cache, log)  •  ✓ Transparent to client', 
        fontsize=9, ha='center')
ax.text(7, types_y - 3.3, 'Pattern: Proxy implements Subject + holds RealSubject + delegates with added control', 
        fontsize=8, ha='center', family='monospace', style='italic', color='#92400e')

# Annotations
ax.text(2.75, 4.7, 'Real object\n(expensive/sensitive)', fontsize=7, ha='center', 
        style='italic', color='#059669')
ax.text(11.5, 4.7, 'Surrogate\n(controls access)', fontsize=7, ha='center', 
        style='italic', color='#d97706')

# ES6 Proxy annotation
es6_box = FancyBboxPatch((0.5, 7.8), 3.5, 1.5, 
                          boxstyle="round,pad=0.1", 
                          edgecolor='#6366f1', 
                          facecolor='#e0e7ff', 
                          linewidth=1.5, alpha=0.8)
ax.add_patch(es6_box)
ax.text(2.25, 9, 'ES6 Proxy', fontsize=10, fontweight='bold', ha='center', color='#4338ca')
ax.text(2.25, 8.65, 'new Proxy(target, {', fontsize=7, ha='center', family='monospace')
ax.text(2.25, 8.35, '  get() { ... },', fontsize=7, ha='center', family='monospace')
ax.text(2.25, 8.05, '  set() { ... }', fontsize=7, ha='center', family='monospace')
ax.text(2.25, 7.75, '})', fontsize=7, ha='center', family='monospace')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Subject (Interface)'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='RealSubject'),
    mpatches.Patch(facecolor='#fef3c7', edgecolor='#f59e0b', label='Proxy (Controls)'),
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Client'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/proxy_pattern.png', dpi=300, bbox_inches='tight')
print("Proxy Pattern diagram saved to docs/images/proxy_pattern.png")

