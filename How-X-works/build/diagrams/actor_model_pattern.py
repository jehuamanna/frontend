import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Actor Model Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Isolated actors with private state; communicate via asynchronous messages',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_actor = '#9C27B0'
color_mailbox = '#FF5722'
color_state = '#4CAF50'
color_message = '#2196F3'

# ===== ACTOR A =====
actorA_box = FancyBboxPatch((1.0, 5.5), 2.5, 2.5,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#9C27B0', facecolor='#F3E5F5',
                            linewidth=3)
ax.add_patch(actorA_box)
ax.text(2.25, 7.85, 'ACTOR A', fontsize=12, ha='center', weight='bold', color='#9C27B0')

# Mailbox
mailbox_a = FancyBboxPatch((1.2, 7.3), 2.1, 0.5,
                          boxstyle="round,pad=0.02", 
                          edgecolor='#FF5722', facecolor='#FFEBEE',
                          linewidth=2)
ax.add_patch(mailbox_a)
ax.text(2.25, 7.55, 'Mailbox: [msg1, msg2]', fontsize=6, ha='center', weight='bold', color='#FF5722')

# State
state_a = FancyBboxPatch((1.2, 6.5), 2.1, 0.6,
                        boxstyle="round,pad=0.02", 
                        edgecolor='#4CAF50', facecolor='#E8F5E9',
                        linewidth=2)
ax.add_patch(state_a)
ax.text(2.25, 6.95, 'Private State:', fontsize=7, ha='center', weight='bold', color='#4CAF50')
ax.text(2.25, 6.75, '{ counter: 5 }', fontsize=6, ha='center', family='monospace', color='#4CAF50')
ax.text(2.25, 6.6, 'NO SHARED!', fontsize=5, ha='center', weight='bold', color='#4CAF50', style='italic')

# Behavior
ax.text(2.25, 6.2, 'Behavior:', fontsize=7, ha='center', weight='bold', color='#9C27B0')
ax.text(2.25, 6.0, 'process(msg)', fontsize=6, ha='center', family='monospace', color='#9C27B0')
ax.text(2.25, 5.8, 'One at a time', fontsize=5, ha='center', style='italic', color='#666')

# ===== ACTOR B =====
actorB_box = FancyBboxPatch((5.5, 5.5), 2.5, 2.5,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#9C27B0', facecolor='#F3E5F5',
                            linewidth=3)
ax.add_patch(actorB_box)
ax.text(6.75, 7.85, 'ACTOR B', fontsize=12, ha='center', weight='bold', color='#9C27B0')

# Mailbox
mailbox_b = FancyBboxPatch((5.7, 7.3), 2.1, 0.5,
                          boxstyle="round,pad=0.02", 
                          edgecolor='#FF5722', facecolor='#FFEBEE',
                          linewidth=2)
ax.add_patch(mailbox_b)
ax.text(6.75, 7.55, 'Mailbox: [msg3]', fontsize=6, ha='center', weight='bold', color='#FF5722')

# State
state_b = FancyBboxPatch((5.7, 6.5), 2.1, 0.6,
                        boxstyle="round,pad=0.02", 
                        edgecolor='#4CAF50', facecolor='#E8F5E9',
                        linewidth=2)
ax.add_patch(state_b)
ax.text(6.75, 6.95, 'Private State:', fontsize=7, ha='center', weight='bold', color='#4CAF50')
ax.text(6.75, 6.75, '{ users: [...] }', fontsize=6, ha='center', family='monospace', color='#4CAF50')
ax.text(6.75, 6.6, 'ISOLATED!', fontsize=5, ha='center', weight='bold', color='#4CAF50', style='italic')

# Behavior
ax.text(6.75, 6.2, 'Behavior:', fontsize=7, ha='center', weight='bold', color='#9C27B0')
ax.text(6.75, 6.0, 'process(msg)', fontsize=6, ha='center', family='monospace', color='#9C27B0')
ax.text(6.75, 5.8, 'Sequential', fontsize=5, ha='center', style='italic', color='#666')

# ===== ACTOR C =====
actorC_box = FancyBboxPatch((10.0, 5.5), 2.5, 2.5,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#9C27B0', facecolor='#F3E5F5',
                            linewidth=3)
ax.add_patch(actorC_box)
ax.text(11.25, 7.85, 'ACTOR C', fontsize=12, ha='center', weight='bold', color='#9C27B0')

# Mailbox
mailbox_c = FancyBboxPatch((10.2, 7.3), 2.1, 0.5,
                          boxstyle="round,pad=0.02", 
                          edgecolor='#FF5722', facecolor='#FFEBEE',
                          linewidth=2)
ax.add_patch(mailbox_c)
ax.text(11.25, 7.55, 'Mailbox: []', fontsize=6, ha='center', weight='bold', color='#FF5722')

# State
state_c = FancyBboxPatch((10.2, 6.5), 2.1, 0.6,
                        boxstyle="round,pad=0.02", 
                        edgecolor='#4CAF50', facecolor='#E8F5E9',
                        linewidth=2)
ax.add_patch(state_c)
ax.text(11.25, 6.95, 'Private State:', fontsize=7, ha='center', weight='bold', color='#4CAF50')
ax.text(11.25, 6.75, '{ data: {...} }', fontsize=6, ha='center', family='monospace', color='#4CAF50')

# Behavior
ax.text(11.25, 6.2, 'Behavior:', fontsize=7, ha='center', weight='bold', color='#9C27B0')
ax.text(11.25, 6.0, 'process(msg)', fontsize=6, ha='center', family='monospace', color='#9C27B0')

# ===== MESSAGE PASSING =====

# A → B
message_arrow1 = FancyArrowPatch((3.5, 6.75), (5.5, 6.75),
                                arrowstyle='->,head_width=0.4,head_length=0.6',
                                color='#2196F3', linewidth=3)
ax.add_patch(message_arrow1)
ax.text(4.5, 7.0, 'message', fontsize=8, ha='center', weight='bold', color='#2196F3')

# B → C
message_arrow2 = FancyArrowPatch((8.0, 6.75), (10.0, 6.75),
                                arrowstyle='->,head_width=0.4,head_length=0.6',
                                color='#2196F3', linewidth=3)
ax.add_patch(message_arrow2)
ax.text(9.0, 7.0, 'message', fontsize=8, ha='center', weight='bold', color='#2196F3')

# C → A (async)
message_arrow3 = FancyArrowPatch((11.25, 5.5), (11.25, 4.5),
                                arrowstyle='->,head_width=0.3,head_length=0.5',
                                color='#2196F3', linewidth=2, linestyle='dashed')
ax.add_patch(message_arrow3)
message_arrow3b = FancyArrowPatch((11.25, 4.5), (2.25, 4.5),
                                 arrowstyle='->,head_width=0.3,head_length=0.5',
                                 color='#2196F3', linewidth=2, linestyle='dashed')
ax.add_patch(message_arrow3b)
message_arrow3c = FancyArrowPatch((2.25, 4.5), (2.25, 5.5),
                                 arrowstyle='->,head_width=0.3,head_length=0.5',
                                 color='#2196F3', linewidth=2, linestyle='dashed')
ax.add_patch(message_arrow3c)
ax.text(6.75, 4.2, 'async message (no blocking)', fontsize=7, ha='center', style='italic', color='#2196F3')

# ===== KEY PRINCIPLES =====
principles_box = FancyBboxPatch((0.3, 2.5), 6.4, 2.7,
                               boxstyle="round,pad=0.05", 
                               edgecolor='#666', facecolor='#FAFAFA',
                               linewidth=1.5)
ax.add_patch(principles_box)
ax.text(3.5, 5.05, 'Actor Model Principles', fontsize=11, ha='center', weight='bold')

principles = [
    ('1. NO SHARED STATE', 'Each actor has private state', 4.75, '#4CAF50'),
    ('2. Message Passing', 'Actors communicate via messages (async)', 4.45, '#2196F3'),
    ('3. Mailbox', 'Messages queued in mailbox', 4.15, '#FF5722'),
    ('4. Sequential Processing', 'One message at a time per actor', 3.85, '#9C27B0'),
    ('5. Isolation', 'Actor failure doesn\'t crash others', 3.55, '#F44336'),
    ('6. Concurrency', 'Actors run independently (parallel)', 3.25, '#FF9800')
]

for num_label, desc, y, color in principles:
    ax.text(0.5, y, num_label, fontsize=8, ha='left', weight='bold', color=color)
    ax.text(0.7, y - 0.15, desc, fontsize=7, ha='left', style='italic', color='#666')

ax.text(3.5, 2.9, '→ No race conditions!', fontsize=8, ha='center', weight='bold', color='#4CAF50')
ax.text(3.5, 2.7, '→ No locks/mutexes!', fontsize=8, ha='center', weight='bold', color='#4CAF50')

# ===== COMPARISON =====
comparison_box = FancyBboxPatch((7.3, 2.5), 6.4, 2.7,
                               boxstyle="round,pad=0.05", 
                               edgecolor='#666', facecolor='#FAFAFA',
                               linewidth=1.5)
ax.add_patch(comparison_box)
ax.text(10.5, 5.05, 'Shared State vs Actor Model', fontsize=11, ha='center', weight='bold')

ax.text(7.5, 4.75, '❌ Shared State (Threads):', fontsize=9, ha='left', weight='bold', color='#F44336')
ax.text(7.5, 4.55, '• Thread 1: counter++', fontsize=7, ha='left', family='monospace', color='#F44336')
ax.text(7.5, 4.40, '• Thread 2: counter++', fontsize=7, ha='left', family='monospace', color='#F44336')
ax.text(7.5, 4.25, '→ Race condition!', fontsize=7, ha='left', weight='bold', color='#F44336')
ax.text(7.5, 4.10, '→ Need locks/mutexes', fontsize=7, ha='left', color='#F44336')
ax.text(7.5, 3.95, '→ Complex, error-prone', fontsize=7, ha='left', color='#F44336')

ax.text(7.5, 3.65, '✅ Actor Model:', fontsize=9, ha='left', weight='bold', color='#4CAF50')
ax.text(7.5, 3.45, '• Actor A: increment msg', fontsize=7, ha='left', family='monospace', color='#4CAF50')
ax.text(7.5, 3.30, '• Actor A: increment msg', fontsize=7, ha='left', family='monospace', color='#4CAF50')
ax.text(7.5, 3.15, '→ Processed sequentially', fontsize=7, ha='left', weight='bold', color='#4CAF50')
ax.text(7.5, 3.00, '→ No race condition!', fontsize=7, ha='left', color='#4CAF50')
ax.text(7.5, 2.85, '→ No locks needed!', fontsize=7, ha='left', color='#4CAF50')
ax.text(7.5, 2.70, '→ Simple, safe', fontsize=7, ha='left', color='#4CAF50')

# ===== FLOW =====
flow_box = FancyBboxPatch((0.3, 0.1), 13.4, 2.2,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(flow_box)
ax.text(7, 2.2, 'Actor Model Flow', fontsize=10, ha='center', weight='bold')

flow_steps = [
    ('1', 'Actor A sends message to Actor B (async)', 1.95, '#2196F3'),
    ('2', 'Message added to Actor B\'s mailbox (queue)', 1.75, '#FF5722'),
    ('3', 'Actor B processes mailbox sequentially', 1.55, '#9C27B0'),
    ('4', 'Actor B updates its PRIVATE state (isolated)', 1.35, '#4CAF50'),
    ('5', 'Actor B may send messages to other actors', 1.15, '#2196F3')
]

for num, text, y, color in flow_steps:
    ax.text(0.5, y, num, fontsize=8, ha='center', weight='bold',
           bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=1.5))
    ax.text(1.0, y, text, fontsize=7, ha='left', color=color)

# Known uses
ax.text(0.5, 0.85, 'Known Uses:', fontsize=8, ha='left', weight='bold')
ax.text(0.5, 0.70, 'Erlang/OTP, Akka (JVM), Pony, Orleans, Web Workers', fontsize=7, ha='left', style='italic', color='#666')

# Key benefit
ax.text(0.5, 0.50, '✓ Key Benefit: NO SHARED STATE = NO RACE CONDITIONS = SAFER CONCURRENCY', fontsize=7, ha='left', weight='bold', color='#4CAF50')

# Key principle
principle_box = FancyBboxPatch((0.5, 0.2), 13.0, 0.2,
                              boxstyle="round,pad=0.03", 
                              edgecolor='#9C27B0', facecolor='#F3E5F5',
                              linewidth=2)
ax.add_patch(principle_box)
ax.text(7, 0.3, 'Key: Actors = isolated units. Messages = async communication. NO shared state → NO race conditions!', 
       fontsize=7, ha='center', weight='bold', color='#9C27B0')

plt.tight_layout()
plt.savefig('docs/images/actor_model_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Actor Model Pattern diagram generated: docs/images/actor_model_pattern.png")


