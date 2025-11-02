import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Event Sourcing Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Store state changes as immutable events; rebuild state by replaying events',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_command = '#FF5722'
color_aggregate = '#FFC107'
color_event_store = '#9C27B0'
color_projection = '#4CAF50'
color_event = '#E91E63'

# ===== COMMAND =====
command_box = FancyBboxPatch((0.5, 6.5), 2.5, 1.5,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#FF5722', facecolor='#FFEBEE',
                            linewidth=2.5)
ax.add_patch(command_box)
ax.text(1.75, 7.85, 'COMMAND', fontsize=11, ha='center', weight='bold', color=color_command)
ax.text(1.75, 7.65, '(Write Intent)', fontsize=9, ha='center', style='italic', color=color_command)

ax.text(0.7, 7.4, 'ChangeUserName', fontsize=7, ha='left', family='monospace', color=color_command)
ax.text(0.7, 7.2, 'PlaceOrder', fontsize=7, ha='left', family='monospace', color=color_command)
ax.text(0.7, 7.0, 'CreateAccount', fontsize=7, ha='left', family='monospace', color=color_command)
ax.text(0.7, 6.75, 'IMPERATIVE', fontsize=6, ha='left', weight='bold', color=color_command, style='italic')

# ===== AGGREGATE =====
aggregate_box = FancyBboxPatch((4.0, 6.5), 2.5, 1.5,
                              boxstyle="round,pad=0.05", 
                              edgecolor='#FFC107', facecolor='#FFF9C4',
                              linewidth=2.5)
ax.add_patch(aggregate_box)
ax.text(5.25, 7.85, 'AGGREGATE', fontsize=11, ha='center', weight='bold', color='#F57C00')
ax.text(5.25, 7.65, '(Domain Model)', fontsize=9, ha='center', style='italic', color='#F57C00')

ax.text(4.2, 7.4, '• Business logic', fontsize=7, ha='left', color='#F57C00')
ax.text(4.2, 7.2, '• Validation', fontsize=7, ha='left', color='#F57C00')
ax.text(4.2, 7.0, '• Produces EVENTS', fontsize=7, ha='left', weight='bold', color=color_event)
ax.text(4.2, 6.75, 'Stateless logic', fontsize=6, ha='left', style='italic', color='#F57C00')

# ===== EVENT STORE (CENTER) =====
event_store_box = FancyBboxPatch((7.5, 5.5), 3.5, 3.0,
                                boxstyle="round,pad=0.1", 
                                edgecolor='#9C27B0', facecolor='#F3E5F5',
                                linewidth=4)
ax.add_patch(event_store_box)
ax.text(9.25, 8.25, 'EVENT STORE', fontsize=13, ha='center', weight='bold', color='#9C27B0')
ax.text(9.25, 8.0, '(Append-Only Log)', fontsize=10, ha='center', style='italic', color='#9C27B0')

ax.text(7.7, 7.7, '• IMMUTABLE events', fontsize=7, ha='left', weight='bold', color='#9C27B0')
ax.text(7.7, 7.5, '• APPEND-ONLY', fontsize=7, ha='left', weight='bold', color='#9C27B0')
ax.text(7.7, 7.3, '• Complete history', fontsize=7, ha='left', color='#9C27B0')
ax.text(7.7, 7.1, '• Source of truth', fontsize=7, ha='left', color='#9C27B0')

# Event log visualization
ax.text(7.7, 6.75, 'Event Log:', fontsize=7, ha='left', weight='bold', color='#9C27B0')
events_display = [
    ('v1', 'UserCreated', 6.5),
    ('v2', 'NameChanged', 6.3),
    ('v3', 'EmailChanged', 6.1),
    ('v4', 'NameChanged', 5.9),
    ('v5', '...', 5.7)
]

for version, event, y in events_display:
    ax.text(7.8, y, version, fontsize=6, ha='left', family='monospace', 
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#9C27B0', linewidth=0.5))
    ax.text(8.3, y, event, fontsize=6, ha='left', family='monospace', color=color_event)

# ===== PROJECTIONS (READ MODELS) =====
projection1_box = FancyBboxPatch((11.5, 7.0), 2.2, 1.0,
                                boxstyle="round,pad=0.05", 
                                edgecolor='#4CAF50', facecolor='#E8F5E9',
                                linewidth=2)
ax.add_patch(projection1_box)
ax.text(12.6, 7.85, 'Projection 1', fontsize=9, ha='center', weight='bold', color='#2E7D32')
ax.text(12.6, 7.7, '(User List)', fontsize=7, ha='center', style='italic', color='#2E7D32')
ax.text(11.7, 7.5, 'Denormalized', fontsize=6, ha='left', color='#2E7D32')
ax.text(11.7, 7.35, 'Fast reads', fontsize=6, ha='left', color='#2E7D32')
ax.text(11.7, 7.2, 'id, name', fontsize=5, ha='left', family='monospace', color='#2E7D32')

projection2_box = FancyBboxPatch((11.5, 5.6), 2.2, 1.0,
                                boxstyle="round,pad=0.05", 
                                edgecolor='#4CAF50', facecolor='#E8F5E9',
                                linewidth=2)
ax.add_patch(projection2_box)
ax.text(12.6, 6.45, 'Projection 2', fontsize=9, ha='center', weight='bold', color='#2E7D32')
ax.text(12.6, 6.3, '(User Detail)', fontsize=7, ha='center', style='italic', color='#2E7D32')
ax.text(11.7, 6.1, 'All fields', fontsize=6, ha='left', color='#2E7D32')
ax.text(11.7, 5.95, 'Full data', fontsize=6, ha='left', color='#2E7D32')
ax.text(11.7, 5.8, 'id, name, email', fontsize=5, ha='left', family='monospace', color='#2E7D32')

# ===== REPLAY/REBUILD =====
replay_box = FancyBboxPatch((4.0, 4.5), 3.0, 1.3,
                           boxstyle="round,pad=0.05", 
                           edgecolor='#E91E63', facecolor='#FCE4EC',
                           linewidth=2.5)
ax.add_patch(replay_box)
ax.text(5.5, 5.65, 'EVENT REPLAY', fontsize=10, ha='center', weight='bold', color=color_event)
ax.text(5.5, 5.45, '(State Reconstruction)', fontsize=8, ha='center', style='italic', color=color_event)

ax.text(4.2, 5.2, '• Rebuild state', fontsize=7, ha='left', color=color_event)
ax.text(4.2, 5.0, '• Time travel', fontsize=7, ha='left', color=color_event)
ax.text(4.2, 4.8, '• New projections', fontsize=7, ha='left', color=color_event)
ax.text(4.2, 4.6, 'Events → State', fontsize=6, ha='left', weight='bold', color=color_event, style='italic')

# ===== ARROWS =====

# 1. Command → Aggregate
arrow1 = FancyArrowPatch((3.0, 7.25), (4.0, 7.25),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_command, linewidth=3)
ax.add_patch(arrow1)
ax.text(3.5, 7.5, '1', fontsize=8, ha='center', weight='bold', color=color_command)

# 2. Aggregate → Event Store (append)
arrow2 = FancyArrowPatch((6.5, 7.25), (7.5, 7.25),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_event, linewidth=3)
ax.add_patch(arrow2)
ax.text(7.0, 7.5, '2. event', fontsize=8, ha='center', weight='bold', color=color_event)

# 3. Event Store → Projections
arrow3 = FancyArrowPatch((11.0, 7.5), (11.5, 7.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_projection, linewidth=2.5)
ax.add_patch(arrow3)
ax.text(11.25, 7.75, '3', fontsize=8, ha='center', weight='bold', color=color_projection)

arrow4 = FancyArrowPatch((11.0, 6.1), (11.5, 6.1),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_projection, linewidth=2.5)
ax.add_patch(arrow4)
ax.text(11.25, 6.35, '3', fontsize=8, ha='center', weight='bold', color=color_projection)

# 4. Event Store → Replay (read events)
arrow5 = FancyArrowPatch((7.5, 5.9), (7.0, 5.3),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_event, linewidth=2.5, linestyle='dashed')
ax.add_patch(arrow5)
ax.text(7.4, 5.6, '4. replay', fontsize=8, ha='center', weight='bold', color=color_event)

# 5. Replay → Aggregate (reconstruct)
arrow6 = FancyArrowPatch((5.5, 5.8), (5.25, 6.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_event, linewidth=2.5, linestyle='dashed')
ax.add_patch(arrow6)
ax.text(5.7, 6.15, '5', fontsize=8, ha='center', weight='bold', color=color_event)

# ===== KEY FEATURES =====
features_box = FancyBboxPatch((0.3, 2.8), 6.4, 1.5,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#666', facecolor='#FAFAFA',
                             linewidth=1.5)
ax.add_patch(features_box)
ax.text(3.5, 4.15, 'Key Features', fontsize=10, ha='center', weight='bold')

features = [
    ('✓ Complete audit trail (every change recorded)', 3.85, '#4CAF50'),
    ('✓ Time travel (replay to any point)', 3.60, '#4CAF50'),
    ('✓ Event replay (rebuild state)', 3.35, '#4CAF50'),
    ('✓ Multiple projections (tailored read models)', 3.10, '#4CAF50'),
    ('✓ Debugging (reproduce bugs by replaying)', 2.85, '#4CAF50')
]

for text, y, color in features:
    ax.text(0.5, y, text, fontsize=8, ha='left', color=color)

# ===== BENEFITS vs TRADE-OFFS =====
benefits_box = FancyBboxPatch((7.3, 2.8), 6.4, 1.5,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#666', facecolor='#FAFAFA',
                             linewidth=1.5)
ax.add_patch(benefits_box)
ax.text(10.5, 4.15, 'Benefits vs Trade-offs', fontsize=10, ha='center', weight='bold')

benefits = [
    ('✓ Never lose data (complete history)', 3.85, '#4CAF50'),
    ('✓ Reproducible (replay events)', 3.60, '#4CAF50'),
    ('✗ Complexity (learning curve)', 3.35, '#FF9800'),
    ('✗ Eventual consistency (projections)', 3.10, '#FF9800'),
    ('✗ Storage (more data)', 2.85, '#FF9800')
]

for text, y, color in benefits:
    ax.text(7.5, y, text, fontsize=8, ha='left', color=color)

# ===== FLOW DIAGRAM =====
flow_box = FancyBboxPatch((0.3, 0.1), 13.4, 2.5,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(flow_box)
ax.text(7, 2.5, 'Event Sourcing Flow', fontsize=10, ha='center', weight='bold')

flow_steps = [
    ('1', 'User issues COMMAND', 2.25, color_command),
    ('2', 'Aggregate validates, produces EVENT (immutable)', 2.05, color_event),
    ('3', 'Event APPENDED to Event Store (never updated)', 1.85, '#9C27B0'),
    ('4', 'Projections LISTEN and update read models', 1.65, color_projection),
    ('5', 'To rebuild state: REPLAY events from Event Store', 1.45, color_event),
    ('6', 'Time travel: Replay events up to timestamp T', 1.25, color_event)
]

for num, text, y, color in flow_steps:
    ax.text(0.5, y, num, fontsize=8, ha='center', weight='bold',
           bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=1.5))
    ax.text(1.0, y, text, fontsize=7, ha='left', color=color)

# Traditional vs Event Sourcing
comparison = [
    ('Traditional: UPDATE user SET name="John"', 0.95, '#666'),
    ('  → Old value LOST forever', 0.80, '#FF5722'),
    ('Event Sourcing: APPEND UserNameChanged(old, new)', 0.65, '#666'),
    ('  → History PRESERVED, can replay', 0.50, '#4CAF50')
]

for text, y, color in comparison:
    ax.text(0.5, y, text, fontsize=7, ha='left', color=color, style='italic')

# Key principle
principle_box = FancyBboxPatch((0.5, 0.2), 13.0, 0.2,
                              boxstyle="round,pad=0.05", 
                              edgecolor='#9C27B0', facecolor='#F3E5F5',
                              linewidth=2)
ax.add_patch(principle_box)
ax.text(7, 0.3, 'Key Principle: Store EVENTS (facts), not STATE. Current state = f(events). Never lose history.', 
       fontsize=8, ha='center', weight='bold', color='#9C27B0')

plt.tight_layout()
plt.savefig('docs/images/event_sourcing_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Event Sourcing Pattern diagram generated: docs/images/event_sourcing_pattern.png")

