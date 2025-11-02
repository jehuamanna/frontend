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
ax.text(7, 9.5, 'CQRS Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Command Query Responsibility Segregation: Separate reads from writes',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_command = '#FF5722'
color_query = '#2196F3'
color_write_model = '#FFC107'
color_read_model = '#4CAF50'
color_event = '#9C27B0'

# ===== CLIENT =====
client_box = FancyBboxPatch((0.5, 5.5), 2.0, 2.0,
                           boxstyle="round,pad=0.05", 
                           edgecolor='#666', facecolor='#F5F5F5',
                           linewidth=2.5)
ax.add_patch(client_box)
ax.text(1.5, 7.25, 'CLIENT', fontsize=12, ha='center', weight='bold', color='#333')
ax.text(0.7, 6.95, '• Issues commands', fontsize=7, ha='left', color=color_command)
ax.text(0.7, 6.75, '  (writes)', fontsize=7, ha='left', color=color_command)
ax.text(0.7, 6.5, '• Issues queries', fontsize=7, ha='left', color=color_query)
ax.text(0.7, 6.3, '  (reads)', fontsize=7, ha='left', color=color_query)
ax.text(0.7, 6.0, '• SEPARATE paths', fontsize=7, ha='left', weight='bold', color='#333')
ax.text(0.7, 5.8, '  for read/write', fontsize=7, ha='left', color='#333')

# ===== COMMAND SIDE (WRITE) =====
command_bus_box = FancyBboxPatch((3.5, 7.0), 2.5, 1.5,
                                boxstyle="round,pad=0.05", 
                                edgecolor='#FF5722', facecolor='#FFEBEE',
                                linewidth=3)
ax.add_patch(command_bus_box)
ax.text(4.75, 8.3, 'COMMAND BUS', fontsize=11, ha='center', weight='bold', color=color_command)
ax.text(4.75, 8.1, '(Write Side)', fontsize=9, ha='center', style='italic', color=color_command)

ax.text(3.7, 7.85, 'createUser()', fontsize=7, ha='left', family='monospace', color=color_command)
ax.text(3.7, 7.65, 'updateUser()', fontsize=7, ha='left', family='monospace', color=color_command)
ax.text(3.7, 7.45, 'deleteUser()', fontsize=7, ha='left', family='monospace', color=color_command)
ax.text(3.7, 7.2, 'IMPERATIVE', fontsize=6, ha='left', weight='bold', color=color_command, style='italic')

write_model_box = FancyBboxPatch((7.0, 7.0), 2.5, 1.5,
                                boxstyle="round,pad=0.05", 
                                edgecolor='#FFC107', facecolor='#FFF9C4',
                                linewidth=3)
ax.add_patch(write_model_box)
ax.text(8.25, 8.3, 'WRITE MODEL', fontsize=11, ha='center', weight='bold', color='#F57C00')
ax.text(8.25, 8.1, '(Domain Model)', fontsize=9, ha='center', style='italic', color='#F57C00')

ax.text(7.2, 7.85, '• Business logic', fontsize=7, ha='left', color='#F57C00')
ax.text(7.2, 7.65, '• Validation', fontsize=7, ha='left', color='#F57C00')
ax.text(7.2, 7.45, '• Normalized', fontsize=7, ha='left', color='#F57C00')
ax.text(7.2, 7.2, 'OPTIMIZED FOR', fontsize=6, ha='left', weight='bold', color='#F57C00', style='italic')
ax.text(7.2, 7.05, 'WRITES', fontsize=6, ha='left', weight='bold', color='#F57C00', style='italic')

# ===== QUERY SIDE (READ) =====
query_bus_box = FancyBboxPatch((3.5, 4.5), 2.5, 1.5,
                              boxstyle="round,pad=0.05", 
                              edgecolor='#2196F3', facecolor='#E3F2FD',
                              linewidth=3)
ax.add_patch(query_bus_box)
ax.text(4.75, 5.8, 'QUERY BUS', fontsize=11, ha='center', weight='bold', color=color_query)
ax.text(4.75, 5.6, '(Read Side)', fontsize=9, ha='center', style='italic', color=color_query)

ax.text(3.7, 5.35, 'getUser(id)', fontsize=7, ha='left', family='monospace', color=color_query)
ax.text(3.7, 5.15, 'searchUsers()', fontsize=7, ha='left', family='monospace', color=color_query)
ax.text(3.7, 4.95, 'getUserList()', fontsize=7, ha='left', family='monospace', color=color_query)
ax.text(3.7, 4.7, 'NO SIDE EFFECTS', fontsize=6, ha='left', weight='bold', color=color_query, style='italic')

read_model_box = FancyBboxPatch((7.0, 4.5), 2.5, 1.5,
                               boxstyle="round,pad=0.05", 
                               edgecolor='#4CAF50', facecolor='#E8F5E9',
                               linewidth=3)
ax.add_patch(read_model_box)
ax.text(8.25, 5.8, 'READ MODEL', fontsize=11, ha='center', weight='bold', color='#2E7D32')
ax.text(8.25, 5.6, '(Projection/DTO)', fontsize=9, ha='center', style='italic', color='#2E7D32')

ax.text(7.2, 5.35, '• Denormalized', fontsize=7, ha='left', color='#2E7D32')
ax.text(7.2, 5.15, '• Precomputed', fontsize=7, ha='left', color='#2E7D32')
ax.text(7.2, 4.95, '• Fast queries', fontsize=7, ha='left', color='#2E7D32')
ax.text(7.2, 4.7, 'OPTIMIZED FOR', fontsize=6, ha='left', weight='bold', color='#2E7D32', style='italic')
ax.text(7.2, 4.55, 'READS', fontsize=6, ha='left', weight='bold', color='#2E7D32', style='italic')

# ===== EVENT BUS (SYNCHRONIZATION) =====
event_box = FancyBboxPatch((10.5, 5.8), 3.0, 1.4,
                          boxstyle="round,pad=0.05", 
                          edgecolor='#9C27B0', facecolor='#F3E5F5',
                          linewidth=2.5)
ax.add_patch(event_box)
ax.text(12.0, 7.05, 'EVENT BUS', fontsize=11, ha='center', weight='bold', color='#9C27B0')
ax.text(12.0, 6.85, '(Synchronization)', fontsize=9, ha='center', style='italic', color='#9C27B0')

ax.text(10.7, 6.6, 'USER_CREATED', fontsize=7, ha='left', family='monospace', color='#9C27B0')
ax.text(10.7, 6.4, 'USER_UPDATED', fontsize=7, ha='left', family='monospace', color='#9C27B0')
ax.text(10.7, 6.2, 'USER_DELETED', fontsize=7, ha='left', family='monospace', color='#9C27B0')
ax.text(10.7, 5.95, 'Write → Read', fontsize=6, ha='left', weight='bold', color='#9C27B0', style='italic')

# ===== ARROWS =====

# Client → Command Bus
arrow1 = FancyArrowPatch((2.5, 6.8), (3.5, 7.75),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_command, linewidth=3)
ax.add_patch(arrow1)
ax.text(2.9, 7.4, '1. command', fontsize=8, ha='center', weight='bold', color=color_command)

# Command Bus → Write Model
arrow2 = FancyArrowPatch((6.0, 7.75), (7.0, 7.75),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_command, linewidth=3)
ax.add_patch(arrow2)
ax.text(6.5, 8.0, '2', fontsize=8, ha='center', weight='bold', color=color_command)

# Write Model → Event Bus
arrow3 = FancyArrowPatch((9.5, 7.5), (10.5, 6.8),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_event, linewidth=3)
ax.add_patch(arrow3)
ax.text(10.0, 7.3, '3. event', fontsize=8, ha='center', weight='bold', color=color_event)

# Event Bus → Read Model
arrow4 = FancyArrowPatch((10.5, 6.2), (9.5, 5.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_event, linewidth=3)
ax.add_patch(arrow4)
ax.text(10.2, 5.9, '4. project', fontsize=8, ha='center', weight='bold', color=color_event)

# Client → Query Bus
arrow5 = FancyArrowPatch((2.5, 6.2), (3.5, 5.25),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_query, linewidth=3)
ax.add_patch(arrow5)
ax.text(2.9, 5.6, '5. query', fontsize=8, ha='center', weight='bold', color=color_query)

# Query Bus → Read Model
arrow6 = FancyArrowPatch((6.0, 5.25), (7.0, 5.25),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_query, linewidth=3)
ax.add_patch(arrow6)
ax.text(6.5, 5.5, '6', fontsize=8, ha='center', weight='bold', color=color_query)

# Read Model → Query Bus (return)
arrow7 = FancyArrowPatch((7.0, 5.0), (6.0, 5.0),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_query, linewidth=2, linestyle='dashed')
ax.add_patch(arrow7)

# Query Bus → Client (return)
arrow8 = FancyArrowPatch((3.5, 5.0), (2.5, 5.9),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_query, linewidth=2, linestyle='dashed')
ax.add_patch(arrow8)
ax.text(2.9, 5.4, '7. data', fontsize=8, ha='center', weight='bold', color=color_query)

# ===== KEY PRINCIPLES =====
principles_box = FancyBboxPatch((0.3, 2.5), 6.4, 1.8,
                               boxstyle="round,pad=0.05", 
                               edgecolor='#666', facecolor='#FAFAFA',
                               linewidth=1.5)
ax.add_patch(principles_box)
ax.text(3.5, 4.15, 'CQRS Principles', fontsize=10, ha='center', weight='bold')

principles = [
    ('1. SEPARATE models for reads and writes', 3.85, '#333'),
    ('2. Commands CHANGE state (imperative)', 3.60, color_command),
    ('3. Queries RETURN data (no side effects)', 3.35, color_query),
    ('4. Events SYNCHRONIZE write → read model', 3.10, color_event),
    ('5. Eventually consistent reads', 2.85, '#F57C00')
]

for text, y, color in principles:
    ax.text(0.5, y, text, fontsize=8, ha='left', color=color, weight='bold')

# ===== BENEFITS =====
benefits_box = FancyBboxPatch((7.3, 2.5), 6.4, 1.8,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#666', facecolor='#FAFAFA',
                             linewidth=1.5)
ax.add_patch(benefits_box)
ax.text(10.5, 4.15, 'Benefits', fontsize=10, ha='center', weight='bold', color='#4CAF50')

benefits = [
    ('✓ Independent optimization (read vs write)', 3.85, '#4CAF50'),
    ('✓ Independent scaling', 3.60, '#4CAF50'),
    ('✓ Simpler, focused models', 3.35, '#4CAF50'),
    ('✓ Security: Different permissions', 3.10, '#4CAF50'),
    ('✗ Eventual consistency (trade-off)', 2.85, '#FF9800')
]

for text, y, color in benefits:
    ax.text(7.5, y, text, fontsize=8, ha='left', color=color)

# ===== FLOW DIAGRAM =====
flow_box = FancyBboxPatch((0.3, 0.1), 13.4, 2.2,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(flow_box)
ax.text(7, 2.2, 'CQRS Flow', fontsize=10, ha='center', weight='bold')

flow_steps = [
    ('1', 'Client sends COMMAND to Command Bus', 1.95, color_command),
    ('2', 'Command Bus invokes Command Handler → Write Model', 1.75, color_command),
    ('3', 'Write Model validates, processes, emits EVENT', 1.55, color_event),
    ('4', 'Event Bus projects event to Read Model (async)', 1.35, color_event),
    ('5', 'Client sends QUERY to Query Bus', 1.15, color_query),
    ('6', 'Query Bus retrieves data from Read Model (fast)', 0.95, color_query),
    ('7', 'Client receives data (eventual consistency)', 0.75, color_query)
]

for num, text, y, color in flow_steps:
    ax.text(0.5, y, num, fontsize=8, ha='center', weight='bold',
           bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=1.5))
    ax.text(1.0, y, text, fontsize=7, ha='left', color=color)

# Key insight
insight_box = FancyBboxPatch((0.5, 0.2), 13.0, 0.4,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#9C27B0', facecolor='#F3E5F5',
                            linewidth=2)
ax.add_patch(insight_box)
ax.text(7, 0.5, 'Key Insight: Reads ≠ Writes. Most apps are 90% reads, 10% writes. CQRS optimizes each independently.', 
       fontsize=8, ha='center', weight='bold', color='#9C27B0')
ax.text(7, 0.3, '(Often combined with Event Sourcing for complete event-driven architecture)', 
       fontsize=7, ha='center', style='italic', color='#9C27B0')

plt.tight_layout()
plt.savefig('docs/images/cqrs_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ CQRS Pattern diagram generated: docs/images/cqrs_pattern.png")

