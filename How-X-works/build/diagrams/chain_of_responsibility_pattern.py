#!/usr/bin/env python3
# ./build/diagrams/chain_of_responsibility_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Chain of Responsibility Pattern', 
        fontsize=18, fontweight='bold', ha='center')

# Client
client_box = FancyBboxPatch((0.5, 7), 2, 1.3, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#0ea5e9', 
                             facecolor='#e0f2fe', 
                             linewidth=2.5)
ax.add_patch(client_box)
ax.text(1.5, 7.9, 'Client', fontsize=12, fontweight='bold', ha='center', color='#0369a1')
ax.text(1.5, 7.5, 'initiates', fontsize=9, ha='center', style='italic')
ax.text(1.5, 7.2, 'request', fontsize=9, ha='center', style='italic')

# Handler (Abstract)
handler_box = FancyBboxPatch((4, 6.5), 3, 2, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#8b5cf6', 
                              facecolor='#f3e8ff', 
                              linewidth=2.5)
ax.add_patch(handler_box)
ax.text(5.5, 8.2, 'Handler', fontsize=12, fontweight='bold', ha='center', color='#7c3aed')
ax.text(5.5, 7.85, '- next: Handler', fontsize=8, ha='center', family='monospace', style='italic')
ax.text(5.5, 7.55, '+ setNext(h)', fontsize=8, ha='center', family='monospace')
ax.text(5.5, 7.25, '+ handle(req) {', fontsize=8, ha='center', family='monospace')
ax.text(5.5, 6.95, '  if (canHandle)', fontsize=7, ha='center', family='monospace', style='italic')
ax.text(5.5, 6.7, '    process', fontsize=7, ha='center', family='monospace', style='italic')

# Arrow: Client to Handler
arrow_client = FancyArrowPatch((2.5, 7.65), (4, 7.65), 
                                arrowstyle='->', mutation_scale=20, 
                                linewidth=2.5, color='#0ea5e9')
ax.add_patch(arrow_client)
ax.text(3.25, 8, 'sends request', fontsize=8, ha='center', 
        fontweight='bold', color='#0369a1', style='italic')

# Concrete Handlers (Chain)
handlers = [
    (8.5, 6.5, 'Handler1', '#10b981', '#d1fae5'),
    (10.5, 5, 'Handler2', '#f59e0b', '#fef3c7'),
    (12.5, 3.5, 'Handler3', '#dc2626', '#fee2e2')
]

for i, (x, y, label, edge_color, face_color) in enumerate(handlers):
    box = FancyBboxPatch((x, y), 1.3, 1.2, 
                          boxstyle="round,pad=0.05", 
                          edgecolor=edge_color, 
                          facecolor=face_color, 
                          linewidth=2)
    ax.add_patch(box)
    ax.text(x + 0.65, y + 0.85, label, fontsize=9, fontweight='bold', ha='center')
    ax.text(x + 0.65, y + 0.55, '+ handle()', fontsize=7, ha='center', family='monospace')
    ax.text(x + 0.65, y + 0.25, 'or pass →', fontsize=6, ha='center', style='italic')

# Inheritance arrows to Handler
for x, y, label, edge_color, face_color in handlers:
    arrow = FancyArrowPatch((x + 0.65, y + 1.2), (5.5, 6.5), 
                             arrowstyle='->', mutation_scale=12, 
                             linewidth=1.5, color='#8b5cf6', 
                             linestyle='dashed', alpha=0.6)
    ax.add_patch(arrow)

# Chain links (next references)
arrow_chain1 = FancyArrowPatch((9.8, 7), (10.5, 5.8), 
                                arrowstyle='->', mutation_scale=18, 
                                linewidth=2.5, color='#6366f1')
ax.add_patch(arrow_chain1)
ax.text(10, 6.5, 'next', fontsize=8, ha='center', fontweight='bold', 
        color='#4338ca', style='italic')

arrow_chain2 = FancyArrowPatch((11.8, 5.5), (12.5, 4.5), 
                                arrowstyle='->', mutation_scale=18, 
                                linewidth=2.5, color='#6366f1')
ax.add_patch(arrow_chain2)
ax.text(12, 5, 'next', fontsize=8, ha='center', fontweight='bold', 
        color='#4338ca', style='italic')

ax.text(13.3, 2.8, 'next = null\n(end of chain)', fontsize=7, ha='left', 
        style='italic', color='#6b7280')

# Flow annotation
flow_y = 2
ax.text(7, flow_y, 'Request Flow Through Chain', fontsize=11, fontweight='bold', 
        ha='center', color='#6366f1',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#e0e7ff', edgecolor='#6366f1', linewidth=2))

# Flow steps
steps = [
    (1, flow_y - 1, '1. Client →', '#0ea5e9'),
    (3, flow_y - 1, '2. Handler1', '#10b981'),
    (5.5, flow_y - 1, '3. Handler2', '#f59e0b'),
    (8, flow_y - 1, '4. Handler3', '#dc2626'),
    (10.5, flow_y - 1, '5. Process\nor pass', '#6366f1')
]

for x, y, text, color in steps:
    ax.text(x, y, text, fontsize=8, ha='center', fontweight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                      edgecolor=color, linewidth=1.5))
    if x < 10:
        ax.annotate('', xy=(x + 1.2, y), xytext=(x + 1.8, y),
                    arrowprops=dict(arrowstyle='->', lw=2, color=color, alpha=0.5))

# Decision box
decision_box = FancyBboxPatch((11.5, flow_y - 2), 2.5, 0.8, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#8b5cf6', 
                               facecolor='#f3e8ff', 
                               linewidth=1.5)
ax.add_patch(decision_box)
ax.text(12.75, flow_y - 1.35, 'Each handler decides:', fontsize=7, ha='center', fontweight='bold')
ax.text(12.75, flow_y - 1.65, '✓ Process & stop', fontsize=6, ha='center')
ax.text(12.75, flow_y - 1.85, '✓ Process & continue', fontsize=6, ha='center')
ax.text(12.75, flow_y - 2.05, '✓ Pass to next', fontsize=6, ha='center')

# Benefits box
benefits_box = FancyBboxPatch((0.5, 0.3), 13, 1, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#10b981', 
                               facecolor='#ecfdf5', 
                               linewidth=2, alpha=0.9)
ax.add_patch(benefits_box)
ax.text(7, 1.1, 'Key Principle: Decouple Sender from Receivers via Sequential Delegation', 
        fontsize=11, fontweight='bold', ha='center', color='#059669')
ax.text(7, 0.8, '✓ Dynamic chain configuration  •  ✓ Multiple potential handlers  •  ✓ Flexible processing order', 
        fontsize=9, ha='center')
ax.text(7, 0.5, 'Pattern: Each handler decides to process/pass → forms linked chain → request traverses until handled', 
        fontsize=8, ha='center', family='monospace', style='italic', color='#065f46')

# Real-world examples
examples_box = FancyBboxPatch((0.5, 8.8), 3, 0.6, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#6366f1', 
                               facecolor='#e0e7ff', 
                               linewidth=1.5, alpha=0.9)
ax.add_patch(examples_box)
ax.text(2, 9.3, 'Examples:', fontsize=9, fontweight='bold', ha='center', color='#4338ca')
ax.text(2, 9, 'Middleware, Event Bubbling, Validators', fontsize=7, ha='center')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Client'),
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Handler (Abstract)'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='ConcreteHandler'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/chain_of_responsibility_pattern.png', dpi=300, bbox_inches='tight')
print("Chain of Responsibility Pattern diagram saved to docs/images/chain_of_responsibility_pattern.png")

