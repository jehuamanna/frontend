import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Memento Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Capture and restore object state without violating encapsulation',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_memento = '#E8D4F8'
color_originator = '#B8E6F0'
color_caretaker = '#FFE5CC'
color_client = '#D4E8D4'

# ===== MEMENTO =====
memento_box = FancyBboxPatch((0.5, 6.5), 2.5, 2.0,
                            boxstyle="round,pad=0.1", 
                            edgecolor='#9D4EDD', facecolor=color_memento,
                            linewidth=2)
ax.add_patch(memento_box)
ax.text(1.75, 8.2, 'Memento', fontsize=12, ha='center', weight='bold')
ax.text(1.75, 7.9, '(Snapshot)', fontsize=9, ha='center', style='italic', color='#666')
ax.text(1.75, 7.5, 'state: any', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(1.75, 7.2, 'timestamp: Date', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(1.75, 6.9, 'getState()', fontsize=10, ha='center', family='monospace')
ax.text(1.75, 6.6, '⚠ Opaque to others', fontsize=8, ha='center', style='italic', color='#9D4EDD')

# ===== ORIGINATOR =====
originator_box = FancyBboxPatch((5.0, 6.0), 3.5, 2.5,
                               boxstyle="round,pad=0.1", 
                               edgecolor='#2E86AB', facecolor=color_originator,
                               linewidth=2.5)
ax.add_patch(originator_box)
ax.text(6.75, 8.2, 'Originator', fontsize=12, ha='center', weight='bold')
ax.text(6.75, 7.9, '(TextEditor / Canvas)', fontsize=9, ha='center', style='italic', color='#666')
ax.text(6.75, 7.55, 'state: internal data', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(6.75, 7.25, 'doSomething()', fontsize=10, ha='center', family='monospace')
ax.text(6.75, 6.95, 'save(): Memento', fontsize=10, ha='center', family='monospace', color='#2E86AB')
ax.text(6.75, 6.65, 'restore(memento)', fontsize=10, ha='center', family='monospace', color='#2E86AB')
ax.text(6.75, 6.3, '✓ Controls state', fontsize=8, ha='center', style='italic', color='#2E86AB')

# ===== CARETAKER =====
caretaker_box = FancyBboxPatch((10.0, 6.5), 3.0, 2.0,
                              boxstyle="round,pad=0.1", 
                              edgecolor='#F77F00', facecolor=color_caretaker,
                              linewidth=2)
ax.add_patch(caretaker_box)
ax.text(11.5, 8.2, 'Caretaker', fontsize=12, ha='center', weight='bold')
ax.text(11.5, 7.9, '(History Manager)', fontsize=9, ha='center', style='italic', color='#666')
ax.text(11.5, 7.5, 'history: Memento[]', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(11.5, 7.2, 'currentIndex: int', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(11.5, 6.9, 'undo()', fontsize=10, ha='center', family='monospace')
ax.text(11.5, 6.6, 'redo()', fontsize=10, ha='center', family='monospace')
ax.text(11.5, 6.3, '⚠ Never modifies', fontsize=8, ha='center', style='italic', color='#F77F00')

# ===== CLIENT =====
client_box = FancyBboxPatch((5.5, 3.5), 2.5, 1.2,
                           boxstyle="round,pad=0.1", 
                           edgecolor='#52B788', facecolor=color_client,
                           linewidth=1.5)
ax.add_patch(client_box)
ax.text(6.75, 4.4, 'Client', fontsize=11, ha='center', weight='bold')
ax.text(6.75, 4.05, 'performs operations', fontsize=9, ha='center', style='italic', color='#555')
ax.text(6.75, 3.75, 'calls save/restore', fontsize=9, ha='center', style='italic', color='#555')

# ===== RELATIONSHIPS =====

# Originator creates Memento
arrow1 = FancyArrowPatch((5.0, 7.5), (3.0, 7.5),
                        arrowstyle='-|>', mutation_scale=20, 
                        color='#2E86AB', linewidth=2)
ax.add_patch(arrow1)
ax.text(4.0, 7.8, 'creates', fontsize=9, style='italic', color='#2E86AB')

# Memento accessed by Originator
arrow2 = FancyArrowPatch((3.0, 7.2), (5.0, 7.2),
                        arrowstyle='->', mutation_scale=15, 
                        color='#999', linewidth=1.5, linestyle='dotted')
ax.add_patch(arrow2)
ax.text(4.0, 6.9, 'restores from', fontsize=8, style='italic', color='#999')

# Caretaker holds Memento
arrow3 = FancyArrowPatch((10.0, 7.5), (3.0, 7.5),
                        arrowstyle='->', mutation_scale=20, 
                        color='#F77F00', linewidth=2, linestyle='dashed')
ax.add_patch(arrow3)
ax.text(6.5, 7.8, 'stores (opaque)', fontsize=9, style='italic', color='#F77F00')

# Caretaker uses Originator
arrow4 = FancyArrowPatch((10.0, 7.0), (8.5, 7.0),
                        arrowstyle='->', mutation_scale=15, 
                        color='#666', linewidth=1.5)
ax.add_patch(arrow4)
ax.text(9.2, 7.3, 'uses', fontsize=9, style='italic', color='#666')

# Client uses Originator
arrow5 = FancyArrowPatch((6.75, 4.7), (6.75, 6.0),
                        arrowstyle='->', mutation_scale=15, 
                        color='#52B788', linewidth=1.5)
ax.add_patch(arrow5)
ax.text(7.2, 5.3, 'operates', fontsize=9, style='italic', color='#52B788')

# Client uses Caretaker
arrow6 = FancyArrowPatch((8.0, 4.3), (10.0, 6.5),
                        arrowstyle='->', mutation_scale=15, 
                        color='#52B788', linewidth=1.5)
ax.add_patch(arrow6)
ax.text(9.0, 5.5, 'undo/redo', fontsize=9, style='italic', color='#52B788')

# ===== SEQUENCE FLOW =====
sequence_y = 2.5
ax.text(7, sequence_y + 0.5, 'Typical Flow', fontsize=11, ha='center', weight='bold', color='#333')

flow_box = FancyBboxPatch((0.5, sequence_y - 1.2), 13, 1.5,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#999', facecolor='#F9F9F9',
                         linewidth=1, linestyle='dashed')
ax.add_patch(flow_box)

ax.text(0.7, sequence_y + 0.1, '1.', fontsize=10, ha='left', weight='bold')
ax.text(1.1, sequence_y + 0.1, 'Client modifies Originator', fontsize=9, ha='left')

ax.text(0.7, sequence_y - 0.2, '2.', fontsize=10, ha='left', weight='bold')
ax.text(1.1, sequence_y - 0.2, 'Client calls originator.save() → returns Memento', fontsize=9, ha='left')

ax.text(0.7, sequence_y - 0.5, '3.', fontsize=10, ha='left', weight='bold')
ax.text(1.1, sequence_y - 0.5, 'Caretaker stores Memento (opaque)', fontsize=9, ha='left')

ax.text(0.7, sequence_y - 0.8, '4.', fontsize=10, ha='left', weight='bold')
ax.text(1.1, sequence_y - 0.8, 'Client calls caretaker.undo()', fontsize=9, ha='left')

ax.text(7.5, sequence_y + 0.1, '5.', fontsize=10, ha='left', weight='bold')
ax.text(7.9, sequence_y + 0.1, 'Caretaker retrieves Memento from history', fontsize=9, ha='left')

ax.text(7.5, sequence_y - 0.2, '6.', fontsize=10, ha='left', weight='bold')
ax.text(7.9, sequence_y - 0.2, 'Caretaker calls originator.restore(memento)', fontsize=9, ha='left')

ax.text(7.5, sequence_y - 0.5, '7.', fontsize=10, ha='left', weight='bold')
ax.text(7.9, sequence_y - 0.5, 'Originator extracts state from Memento', fontsize=9, ha='left')

ax.text(7.5, sequence_y - 0.8, '8.', fontsize=10, ha='left', weight='bold')
ax.text(7.9, sequence_y - 0.8, 'Originator restores internal state', fontsize=9, ha='left')

# ===== KEY CONCEPTS =====
concepts_box = FancyBboxPatch((0.5, 0.1), 4.5, 0.8,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#666', facecolor='#FAFAFA',
                             linewidth=1)
ax.add_patch(concepts_box)
ax.text(2.75, 0.7, 'Key Concepts', fontsize=10, ha='center', weight='bold')
ax.text(0.7, 0.45, '✓ Encapsulation preserved', fontsize=8, ha='left')
ax.text(0.7, 0.25, '✓ Memento opaque to Caretaker', fontsize=8, ha='left')
ax.text(2.8, 0.45, '✓ Originator creates/restores', fontsize=8, ha='left')
ax.text(2.8, 0.25, '✓ Caretaker manages history', fontsize=8, ha='left')

# ===== USE CASES =====
usecases_box = FancyBboxPatch((5.5, 0.1), 4.0, 0.8,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#666', facecolor='#FAFAFA',
                             linewidth=1)
ax.add_patch(usecases_box)
ax.text(7.5, 0.7, 'Common Use Cases', fontsize=10, ha='center', weight='bold')
ax.text(5.7, 0.45, '• Undo/Redo in editors', fontsize=8, ha='left')
ax.text(5.7, 0.25, '• Game save/checkpoint', fontsize=8, ha='left')
ax.text(7.5, 0.45, '• Form auto-save', fontsize=8, ha='left')
ax.text(7.5, 0.25, '• Transaction rollback', fontsize=8, ha='left')

# ===== BENEFITS =====
benefits_box = FancyBboxPatch((10.0, 0.1), 3.5, 0.8,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#2E7D32', facecolor='#E8F5E9',
                             linewidth=1)
ax.add_patch(benefits_box)
ax.text(11.75, 0.7, 'Benefits', fontsize=10, ha='center', weight='bold', color='#2E7D32')
ax.text(10.2, 0.45, '✓ No encapsulation violation', fontsize=8, ha='left', color='#2E7D32')
ax.text(10.2, 0.25, '✓ Multi-level undo/redo', fontsize=8, ha='left', color='#2E7D32')

plt.tight_layout()
plt.savefig('docs/images/memento_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Memento Pattern diagram generated: docs/images/memento_pattern.png")

