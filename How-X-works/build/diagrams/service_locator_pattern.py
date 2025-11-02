#!/usr/bin/env python3
# ./build/diagrams/service_locator_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Service Locator Pattern', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Central Registry for Service Discovery',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= Service Locator (Central) =============
locator_box = FancyBboxPatch((4, 6), 6, 2.5,
                              boxstyle="round,pad=0.1",
                              edgecolor='#3b82f6', facecolor='#dbeafe', linewidth=3)
ax.add_patch(locator_box)
ax.text(7, 8.2, 'Service Locator', fontsize=14, weight='bold', ha='center', color='#1e40af')
ax.text(7, 7.8, 'Map<string, Service>', fontsize=9, ha='center', family='monospace', style='italic', color='#6b7280')
ax.text(7, 7.4, 'register(name, service)', fontsize=9, ha='center', family='monospace')
ax.text(7, 7.05, 'get(name): Service', fontsize=9, ha='center', family='monospace')
ax.text(7, 6.7, 'has(name): boolean', fontsize=9, ha='center', family='monospace')
ax.text(7, 6.35, 'unregister(name)', fontsize=9, ha='center', family='monospace')

# ============= Services (Registered) =============
services = [
    (1, 3.5, 'Logger', '#10b981', '#d1fae5'),
    (4.5, 3.5, 'Database', '#8b5cf6', '#f3e8ff'),
    (8, 3.5, 'Cache', '#f59e0b', '#fef3c7'),
    (11.5, 3.5, 'API Client', '#ef4444', '#fee2e2'),
]

for x, y, name, edge_color, face_color in services:
    service_box = FancyBboxPatch((x, y), 2.2, 1.2,
                                  boxstyle="round,pad=0.1",
                                  edgecolor=edge_color, facecolor=face_color, linewidth=2)
    ax.add_patch(service_box)
    ax.text(x + 1.1, y + 0.8, name, fontsize=10, weight='bold', ha='center')
    ax.text(x + 1.1, y + 0.4, 'Service', fontsize=8, ha='center', family='monospace', style='italic')
    
    # Registration arrows
    arrow = FancyArrowPatch((x + 1.1, y + 1.2), (7, 6),
                            arrowstyle='->', mutation_scale=15,
                            linewidth=1.5, color=edge_color, linestyle='dashed', alpha=0.6)
    ax.add_patch(arrow)

ax.text(7, 5, 'Registered Services', fontsize=9, ha='center', style='italic', color='#6b7280')

# ============= Clients =============
clients = [
    (0.5, 0.8, 'Client A'),
    (4, 0.8, 'Client B'),
    (7.5, 0.8, 'Client C'),
    (11, 0.8, 'Client D'),
]

for x, y, name in clients:
    client_box = FancyBboxPatch((x, y), 2, 1,
                                 boxstyle="round,pad=0.1",
                                 edgecolor='#0ea5e9', facecolor='#e0f2fe', linewidth=1.5)
    ax.add_patch(client_box)
    ax.text(x + 1, y + 0.65, name, fontsize=10, weight='bold', ha='center')
    ax.text(x + 1, y + 0.25, 'Locator.get(...)', fontsize=7, ha='center', family='monospace')
    
    # Request arrows (up to locator)
    arrow_up = FancyArrowPatch((x + 1, y + 1), (7, 6),
                               arrowstyle='->', mutation_scale=15,
                               linewidth=1.5, color='#0ea5e9', alpha=0.8)
    ax.add_patch(arrow_up)

ax.text(7, 2.7, 'Clients Request Services', fontsize=9, ha='center', style='italic', color='#0369a1', weight='bold')

# Flow annotations
flow_steps = [
    '1. Register services',
    '2. Client requests service',
    '3. Locator finds & returns',
    '4. Client uses service'
]
for i, step in enumerate(flow_steps):
    ax.text(0.5, 9 - i * 0.4, step, fontsize=8, ha='left',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef3c7', edgecolor='#f59e0b', alpha=0.8))

# Comparison box
compare_box = FancyBboxPatch((0.2, 0.05), 13.6, 0.5,
                              boxstyle="round,pad=0.1",
                              edgecolor='#6b7280', facecolor='#f3f4f6', linewidth=1)
ax.add_patch(compare_box)

compare_text = """Service Locator vs DI:  Locator = Services pull dependencies (ask for them)  •  DI = Services push dependencies (inject them)  •  Locator hides deps (anti-pattern risk)"""
ax.text(7, 0.25, compare_text, fontsize=7, ha='center', va='center')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#dbeafe', edgecolor='#3b82f6', label='Service Locator'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Registered Services'),
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Clients'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=9, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/service_locator_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Service Locator Pattern diagram generated successfully")

