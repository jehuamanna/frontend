#!/usr/bin/env python3
# ./build/diagrams/command_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Command Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Client
client_box = FancyBboxPatch((0.5, 6.5), 2, 1.5, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#0ea5e9', 
                             facecolor='#e0f2fe', 
                             linewidth=2.5)
ax.add_patch(client_box)
ax.text(1.5, 7.7, 'Client', fontsize=12, fontweight='bold', ha='center', color='#0369a1')
ax.text(1.5, 7.3, 'creates', fontsize=9, ha='center', style='italic')
ax.text(1.5, 7, 'commands', fontsize=9, ha='center', style='italic')

# Command (Interface)
command_box = FancyBboxPatch((4, 6.5), 3, 1.5, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#8b5cf6', 
                              facecolor='#f3e8ff', 
                              linewidth=3)
ax.add_patch(command_box)
ax.text(5.5, 7.7, '«interface»', fontsize=9, ha='center', style='italic', color='#7c3aed')
ax.text(5.5, 7.35, 'Command', fontsize=12, fontweight='bold', ha='center', color='#7c3aed')
ax.text(5.5, 7, '+ execute()', fontsize=9, ha='center', family='monospace')

# ConcreteCommand
concrete_box = FancyBboxPatch((4, 4), 3, 1.5, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#10b981', 
                               facecolor='#d1fae5', 
                               linewidth=2.5)
ax.add_patch(concrete_box)
ax.text(5.5, 5.2, 'ConcreteCommand', fontsize=11, fontweight='bold', ha='center', color='#059669')
ax.text(5.5, 4.85, '- receiver', fontsize=8, ha='center', family='monospace', style='italic')
ax.text(5.5, 4.55, '+ execute() {', fontsize=8, ha='center', family='monospace')
ax.text(5.5, 4.25, '  receiver.action()', fontsize=7, ha='center', family='monospace', style='italic')

# Receiver
receiver_box = FancyBboxPatch((9, 4), 3, 1.5, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#f59e0b', 
                               facecolor='#fef3c7', 
                               linewidth=2.5)
ax.add_patch(receiver_box)
ax.text(10.5, 5.2, 'Receiver', fontsize=12, fontweight='bold', ha='center', color='#d97706')
ax.text(10.5, 4.85, '+ action()', fontsize=9, ha='center', family='monospace')
ax.text(10.5, 4.55, '(knows how to', fontsize=7, ha='center', style='italic')
ax.text(10.5, 4.3, 'perform operation)', fontsize=7, ha='center', style='italic')

# Invoker
invoker_box = FancyBboxPatch((4, 8.5), 3, 1, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#dc2626', 
                              facecolor='#fee2e2', 
                              linewidth=2.5)
ax.add_patch(invoker_box)
ax.text(5.5, 9.2, 'Invoker', fontsize=11, fontweight='bold', ha='center', color='#dc2626')
ax.text(5.5, 8.85, '- command', fontsize=8, ha='center', family='monospace', style='italic')
ax.text(5.5, 8.6, '+ invoke()', fontsize=8, ha='center', family='monospace')

# Arrows
# Client creates Command
arrow_client_cmd = FancyArrowPatch((2.5, 7.25), (4, 7.25), 
                                    arrowstyle='->', mutation_scale=20, 
                                    linewidth=2.5, color='#0ea5e9')
ax.add_patch(arrow_client_cmd)
ax.text(3.25, 7.6, 'creates', fontsize=8, ha='center', 
        fontweight='bold', color='#0369a1', style='italic')

# Command implemented by ConcreteCommand
arrow_implements = FancyArrowPatch((5.5, 6.5), (5.5, 5.5), 
                                    arrowstyle='->', mutation_scale=20, 
                                    linewidth=2.5, color='#8b5cf6', 
                                    linestyle='dashed')
ax.add_patch(arrow_implements)
ax.text(5.9, 6, 'implements', fontsize=8, ha='left', 
        style='italic', color='#7c3aed', fontweight='bold')

# ConcreteCommand references Receiver
arrow_receiver = FancyArrowPatch((7, 4.75), (9, 4.75), 
                                  arrowstyle='->', mutation_scale=20, 
                                  linewidth=2.5, color='#10b981')
ax.add_patch(arrow_receiver)
ax.text(8, 5.1, 'calls', fontsize=8, ha='center', 
        fontweight='bold', color='#059669', style='italic')

# Invoker holds Command
arrow_invoker = FancyArrowPatch((5.5, 8.5), (5.5, 8), 
                                 arrowstyle='->', mutation_scale=20, 
                                 linewidth=2.5, color='#dc2626')
ax.add_patch(arrow_invoker)
ax.text(6, 8.25, 'holds', fontsize=8, ha='left', 
        fontweight='bold', color='#dc2626', style='italic')

# Flow diagram
flow_y = 2.5
ax.text(7, flow_y + 0.5, 'Execution Flow', fontsize=11, fontweight='bold', 
        ha='center', color='#6366f1',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#e0e7ff', edgecolor='#6366f1', linewidth=2))

# Flow steps
steps = [
    (1, flow_y - 0.5, 'Client\ncreates', '#0ea5e9'),
    (3, flow_y - 0.5, 'Invoker\ncalls', '#dc2626'),
    (5, flow_y - 0.5, 'Command\nexecutes', '#8b5cf6'),
    (7, flow_y - 0.5, 'ConcreteCmd\ncalls', '#10b981'),
    (9, flow_y - 0.5, 'Receiver\nperforms', '#f59e0b')
]

for i, (x, y, text, color) in enumerate(steps):
    ax.text(x, y, text, fontsize=7, ha='center', fontweight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                      edgecolor=color, linewidth=1.5))
    if i < len(steps) - 1:
        ax.annotate('', xy=(steps[i+1][0] - 0.6, y), xytext=(x + 0.6, y),
                    arrowprops=dict(arrowstyle='->', lw=2, color='#6366f1', alpha=0.5))

# Undo/Redo example
undo_y = 0.8
ax.text(2, undo_y, 'Undo/Redo Support:', fontsize=10, fontweight='bold', ha='left', color='#10b981')
ax.text(2, undo_y - 0.4, '+ undo() - reverses execute()', fontsize=7, ha='left', family='monospace')
ax.text(2, undo_y - 0.7, 'History: [cmd1, cmd2, cmd3] ← undo/redo', fontsize=7, ha='left', family='monospace')

# Benefits box
benefits_box = FancyBboxPatch((0.5, flow_y - 2.5), 13, 0.8, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#8b5cf6', 
                               facecolor='#f5f3ff', 
                               linewidth=2, alpha=0.9)
ax.add_patch(benefits_box)
ax.text(7, flow_y - 1.9, 'Key Principle: Encapsulate Requests as Objects', 
        fontsize=11, fontweight='bold', ha='center', color='#7c3aed')
ax.text(7, flow_y - 2.2, '✓ Undo/Redo  •  ✓ Queue/Log operations  •  ✓ Decouple invoker from receiver  •  ✓ Macro commands', 
        fontsize=9, ha='center')

# Real-world examples
examples_box = FancyBboxPatch((9, 8.5), 4.5, 1, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#6366f1', 
                               facecolor='#e0e7ff', 
                               linewidth=1.5, alpha=0.9)
ax.add_patch(examples_box)
ax.text(11.25, 9.2, 'Examples:', fontsize=9, fontweight='bold', ha='center', color='#4338ca')
ax.text(11.25, 8.95, 'Text editor undo/redo', fontsize=7, ha='center')
ax.text(11.25, 8.75, 'Redux actions', fontsize=7, ha='center')
ax.text(11.25, 8.55, 'Transaction systems', fontsize=7, ha='center')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Client'),
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Command (Interface)'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='ConcreteCommand'),
    mpatches.Patch(facecolor='#fef3c7', edgecolor='#f59e0b', label='Receiver'),
    mpatches.Patch(facecolor='#fee2e2', edgecolor='#dc2626', label='Invoker'),
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=7, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/command_pattern.png', dpi=300, bbox_inches='tight')
print("Command Pattern diagram saved to docs/images/command_pattern.png")

