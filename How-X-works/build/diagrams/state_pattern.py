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
ax.text(7, 9.5, 'State Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Object behavior changes when internal state changes (appears to change class)',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_context = '#FFE5CC'
color_state = '#E8F4F8'
color_concrete = '#B8E6F0'

# ===== CONTEXT =====
context_box = FancyBboxPatch((0.5, 6.0), 2.8, 2.0,
                            boxstyle="round,pad=0.1", 
                            edgecolor='#E63946', facecolor=color_context,
                            linewidth=2.5)
ax.add_patch(context_box)
ax.text(1.9, 7.7, 'Context', fontsize=12, ha='center', weight='bold')
ax.text(1.9, 7.4, '(Document/Connection)', fontsize=9, ha='center', style='italic', color='#666')
ax.text(1.9, 7.05, 'state: State', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(1.9, 6.75, 'setState(state)', fontsize=10, ha='center', family='monospace')
ax.text(1.9, 6.45, 'request()', fontsize=10, ha='center', family='monospace')
ax.text(1.9, 6.15, '→ state.handle()', fontsize=9, ha='center', style='italic', color='#E63946')

# ===== STATE INTERFACE =====
state_interface = FancyBboxPatch((5.5, 6.5), 3.0, 1.5,
                                boxstyle="round,pad=0.1", 
                                edgecolor='#2E86AB', facecolor=color_state,
                                linewidth=2, linestyle='--')
ax.add_patch(state_interface)
ax.text(7.0, 7.75, '«interface»', fontsize=9, ha='center', style='italic', color='#2E86AB')
ax.text(7.0, 7.5, 'State', fontsize=12, ha='center', weight='bold')
ax.text(7.0, 7.15, 'handle(context)', fontsize=10, ha='center', family='monospace')
ax.text(7.0, 6.85, 'State-specific behavior', fontsize=8, ha='center', style='italic', color='#555')

# ===== CONCRETE STATE A =====
stateA = FancyBboxPatch((10.0, 6.5), 2.2, 1.5,
                       boxstyle="round,pad=0.1", 
                       edgecolor='#2E86AB', facecolor=color_concrete,
                       linewidth=2)
ax.add_patch(stateA)
ax.text(11.1, 7.75, 'StateA', fontsize=11, ha='center', weight='bold')
ax.text(11.1, 7.5, '(DraftState)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(11.1, 7.2, 'handle()', fontsize=9, ha='center', family='monospace')
ax.text(11.1, 6.9, '→ setState(B)', fontsize=8, ha='center', style='italic', color='#2E86AB')

# ===== CONCRETE STATE B =====
stateB = FancyBboxPatch((10.0, 4.5), 2.2, 1.5,
                       boxstyle="round,pad=0.1", 
                       edgecolor='#2E86AB', facecolor=color_concrete,
                       linewidth=2)
ax.add_patch(stateB)
ax.text(11.1, 5.75, 'StateB', fontsize=11, ha='center', weight='bold')
ax.text(11.1, 5.5, '(ReviewState)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(11.1, 5.2, 'handle()', fontsize=9, ha='center', family='monospace')
ax.text(11.1, 4.9, '→ setState(C)', fontsize=8, ha='center', style='italic', color='#2E86AB')

# ===== CONCRETE STATE C =====
stateC = FancyBboxPatch((10.0, 2.5), 2.2, 1.5,
                       boxstyle="round,pad=0.1", 
                       edgecolor='#2E86AB', facecolor=color_concrete,
                       linewidth=2)
ax.add_patch(stateC)
ax.text(11.1, 3.75, 'StateC', fontsize=11, ha='center', weight='bold')
ax.text(11.1, 3.5, '(PublishedState)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(11.1, 3.2, 'handle()', fontsize=9, ha='center', family='monospace')
ax.text(11.1, 2.9, 'Final state', fontsize=8, ha='center', style='italic', color='#555')

# ===== RELATIONSHIPS =====

# Context holds State
arrow1 = FancyArrowPatch((3.3, 7.0), (5.5, 7.0),
                        arrowstyle='->', mutation_scale=20, 
                        color='#E63946', linewidth=2)
ax.add_patch(arrow1)
ax.text(4.4, 7.3, 'holds', fontsize=9, style='italic', color='#E63946')

# Context delegates to State
arrow_delegate = FancyArrowPatch((3.3, 6.5), (5.5, 6.8),
                               arrowstyle='->', mutation_scale=15, 
                               color='#999', linewidth=1.5, linestyle='dotted')
ax.add_patch(arrow_delegate)
ax.text(4.4, 6.3, 'delegates', fontsize=8, style='italic', color='#999')

# States implement interface
arrow2 = FancyArrowPatch((10.0, 7.2), (8.5, 7.2),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow2)
ax.text(9.2, 7.5, 'implements', fontsize=8, style='italic', color='#2E86AB')

arrow3 = FancyArrowPatch((10.0, 5.2), (8.5, 6.8),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow3)

arrow4 = FancyArrowPatch((10.0, 3.2), (8.5, 6.5),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow4)

# State transitions
trans1 = FancyArrowPatch((11.1, 6.5), (11.1, 6.0),
                        arrowstyle='->', mutation_scale=15, 
                        color='#52B788', linewidth=2)
ax.add_patch(trans1)
ax.text(11.6, 6.25, 'transition', fontsize=8, style='italic', color='#52B788')

trans2 = FancyArrowPatch((11.1, 4.5), (11.1, 4.0),
                        arrowstyle='->', mutation_scale=15, 
                        color='#52B788', linewidth=2)
ax.add_patch(trans2)
ax.text(11.6, 4.25, 'transition', fontsize=8, style='italic', color='#52B788')

# ===== STATE MACHINE DIAGRAM =====
sm_y = 5.0
ax.text(2.5, sm_y + 0.3, 'State Machine', fontsize=11, ha='center', weight='bold', color='#9D4EDD')

# Draw states as circles
states_pos = {
    'Draft': (1.0, sm_y - 0.8),
    'Review': (2.5, sm_y - 0.8),
    'Published': (4.0, sm_y - 0.8)
}

for state, (x, y) in states_pos.items():
    circle = Circle((x, y), 0.35, facecolor='#F3E5F5', edgecolor='#9D4EDD', linewidth=2)
    ax.add_patch(circle)
    ax.text(x, y, state, fontsize=8, ha='center', va='center', weight='bold')

# Transitions
trans_draft_review = FancyArrowPatch((1.35, sm_y - 0.8), (2.15, sm_y - 0.8),
                                    arrowstyle='->', mutation_scale=12, 
                                    color='#9D4EDD', linewidth=1.5)
ax.add_patch(trans_draft_review)
ax.text(1.75, sm_y - 0.55, 'review()', fontsize=7, ha='center', style='italic', color='#9D4EDD')

trans_review_published = FancyArrowPatch((2.85, sm_y - 0.8), (3.65, sm_y - 0.8),
                                        arrowstyle='->', mutation_scale=12, 
                                        color='#9D4EDD', linewidth=1.5)
ax.add_patch(trans_review_published)
ax.text(3.25, sm_y - 0.55, 'publish()', fontsize=7, ha='center', style='italic', color='#9D4EDD')

# Back transition
trans_back = FancyArrowPatch((3.65, sm_y - 1.1), (1.35, sm_y - 1.1),
                            arrowstyle='->', mutation_scale=10, 
                            color='#999', linewidth=1, linestyle='dashed')
ax.add_patch(trans_back)
ax.text(2.5, sm_y - 1.35, 'unpublish()', fontsize=7, ha='center', style='italic', color='#999')

# ===== SEQUENCE DIAGRAM =====
seq_y = 2.5
ax.text(2.5, seq_y + 0.5, 'Execution Flow', fontsize=11, ha='center', weight='bold')

seq_box = FancyBboxPatch((0.5, seq_y - 1.2), 4.0, 1.5,
                        boxstyle="round,pad=0.05", 
                        edgecolor='#999', facecolor='#F9F9F9',
                        linewidth=1)
ax.add_patch(seq_box)

ax.text(0.7, seq_y + 0.1, '1.', fontsize=9, ha='left', weight='bold')
ax.text(1.0, seq_y + 0.1, 'Client calls context.request()', fontsize=8, ha='left')

ax.text(0.7, seq_y - 0.2, '2.', fontsize=9, ha='left', weight='bold')
ax.text(1.0, seq_y - 0.2, 'Context delegates to state.handle()', fontsize=8, ha='left')

ax.text(0.7, seq_y - 0.5, '3.', fontsize=9, ha='left', weight='bold')
ax.text(1.0, seq_y - 0.5, 'State executes behavior', fontsize=8, ha='left')

ax.text(0.7, seq_y - 0.8, '4.', fontsize=9, ha='left', weight='bold')
ax.text(1.0, seq_y - 0.8, 'State may call context.setState(newState)', fontsize=8, ha='left')

# ===== WITHOUT VS WITH STATE PATTERN =====
comp_y = 1.0

# Without
without_box = FancyBboxPatch((5.5, comp_y - 0.5), 3.5, 1.0,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#C41E3A', facecolor='#FFE5E5',
                            linewidth=1.5)
ax.add_patch(without_box)
ax.text(7.25, comp_y + 0.35, '❌ Without State Pattern', fontsize=10, ha='center', weight='bold', color='#C41E3A')
ax.text(5.7, comp_y + 0.05, '• if/switch statements', fontsize=7, ha='left', color='#C41E3A')
ax.text(5.7, comp_y - 0.15, '• Scattered state logic', fontsize=7, ha='left', color='#C41E3A')
ax.text(5.7, comp_y - 0.35, '• Hard to extend', fontsize=7, ha='left', color='#C41E3A')

# With
with_box = FancyBboxPatch((9.5, comp_y - 0.5), 3.5, 1.0,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#2E7D32', facecolor='#E8F5E9',
                         linewidth=1.5)
ax.add_patch(with_box)
ax.text(11.25, comp_y + 0.35, '✓ With State Pattern', fontsize=10, ha='center', weight='bold', color='#2E7D32')
ax.text(9.7, comp_y + 0.05, '• State objects', fontsize=7, ha='left', color='#2E7D32')
ax.text(9.7, comp_y - 0.15, '• Encapsulated logic', fontsize=7, ha='left', color='#2E7D32')
ax.text(9.7, comp_y - 0.35, '• Easy to extend', fontsize=7, ha='left', color='#2E7D32')

# ===== KEY BENEFITS =====
benefits_box = FancyBboxPatch((5.5, 0.05), 7.5, 0.5,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#666', facecolor='#FAFAFA',
                             linewidth=1)
ax.add_patch(benefits_box)
ax.text(9.25, 0.4, 'Key Benefits: Eliminate conditionals • Encapsulate state logic • Easy to extend • Clear transitions',
        fontsize=8, ha='center', style='italic', color='#666')

plt.tight_layout()
plt.savefig('docs/images/state_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ State Pattern diagram generated: docs/images/state_pattern.png")

