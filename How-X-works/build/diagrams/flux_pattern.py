import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Flux Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Unidirectional data flow for predictable state management',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_view = '#E3F2FD'
color_action = '#FFF3E0'
color_dispatcher = '#E8F5E9'
color_store = '#F3E5F5'
color_flow = '#FF5722'

# ===== CIRCULAR FLOW DIAGRAM =====
# Center point
cx, cy = 7, 5.5

# Radius
r = 2.5

# Define positions for 4 components in circular flow
angles = {
    'VIEW': -90,      # top
    'ACTIONS': 0,     # right
    'DISPATCHER': 90, # bottom
    'STORE': 180      # left
}

# Draw components in circular arrangement
def draw_component(label, angle, color, size=1.2):
    rad = np.radians(angle)
    x = cx + r * np.cos(rad)
    y = cy + r * np.sin(rad)
    
    box = FancyBboxPatch((x - size/2, y - size/2), size, size,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#333', facecolor=color,
                         linewidth=2.5)
    ax.add_patch(box)
    ax.text(x, y, label, fontsize=12, ha='center', va='center', weight='bold')
    return x, y

view_x, view_y = draw_component('VIEW', angles['VIEW'], color_view)
action_x, action_y = draw_component('ACTIONS', angles['ACTIONS'], color_action)
disp_x, disp_y = draw_component('DISPATCHER', angles['DISPATCHER'], color_dispatcher)
store_x, store_y = draw_component('STORE', angles['STORE'], color_store)

# Draw circular flow arrows
def draw_flow_arrow(x1, y1, x2, y2, label, offset=0.3):
    # Calculate midpoint
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    
    # Offset for curved arrow
    dx, dy = y2 - y1, -(x2 - x1)
    length = np.sqrt(dx**2 + dy**2)
    if length > 0:
        dx, dy = dx/length * offset, dy/length * offset
    
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           connectionstyle=f"arc3,rad=0.3",
                           arrowstyle='->,head_width=0.6,head_length=0.8',
                           color=color_flow, linewidth=4,
                           zorder=5)
    ax.add_patch(arrow)
    
    # Label
    ax.text(mx + dx, my + dy, label, fontsize=9, ha='center', 
           bbox=dict(boxstyle='round', facecolor='white', edgecolor=color_flow, linewidth=1.5),
           weight='bold', color=color_flow)

# Draw flow: VIEW → ACTIONS → DISPATCHER → STORE → VIEW
draw_flow_arrow(view_x + 0.6, view_y + 0.4, action_x - 0.4, action_y + 0.6, '1')
draw_flow_arrow(action_x - 0.6, action_y - 0.4, disp_x + 0.4, disp_y - 0.6, '2')
draw_flow_arrow(disp_x - 0.4, disp_y - 0.6, store_x + 0.6, store_y - 0.4, '3')
draw_flow_arrow(store_x - 0.6, store_y + 0.4, view_x - 0.4, view_y - 0.6, '4')

# Center label
center_box = Circle((cx, cy), 0.4, facecolor='white', edgecolor=color_flow, linewidth=2.5)
ax.add_patch(center_box)
ax.text(cx, cy, 'ONE-WAY\nFLOW', fontsize=8, ha='center', va='center', 
       weight='bold', color=color_flow)

# ===== DETAILED COMPONENT DESCRIPTIONS =====

# VIEW Details
view_detail_box = FancyBboxPatch((0.2, 6.5), 2.5, 1.8,
                                boxstyle="round,pad=0.05", 
                                edgecolor='#1976D2', facecolor=color_view,
                                linewidth=2)
ax.add_patch(view_detail_box)
ax.text(1.45, 8.15, 'VIEW (UI)', fontsize=10, ha='center', weight='bold', color='#1976D2')
ax.text(0.35, 7.9, '• Renders UI from store state', fontsize=7, ha='left')
ax.text(0.35, 7.7, '• User interactions', fontsize=7, ha='left')
ax.text(0.35, 7.5, '• Dispatches ACTIONS', fontsize=7, ha='left', weight='bold', color=color_flow)
ax.text(0.35, 7.3, '• Listens to store changes', fontsize=7, ha='left')
ax.text(0.35, 6.95, 'onClick={() => {', fontsize=6, ha='left', family='monospace', color='#1976D2')
ax.text(0.5, 6.75, 'dispatch(addTodo())', fontsize=6, ha='left', family='monospace', color=color_flow)
ax.text(0.35, 6.55, '}', fontsize=6, ha='left', family='monospace', color='#1976D2')

# ACTIONS Details
action_detail_box = FancyBboxPatch((11.3, 6.5), 2.5, 1.8,
                                  boxstyle="round,pad=0.05", 
                                  edgecolor='#EF6C00', facecolor=color_action,
                                  linewidth=2)
ax.add_patch(action_detail_box)
ax.text(12.55, 8.15, 'ACTIONS', fontsize=10, ha='center', weight='bold', color='#EF6C00')
ax.text(11.45, 7.9, '• Plain objects', fontsize=7, ha='left')
ax.text(11.45, 7.7, '• Describe WHAT happened', fontsize=7, ha='left', weight='bold')
ax.text(11.45, 7.5, '• Have type + payload', fontsize=7, ha='left')
ax.text(11.45, 7.3, '• Created by action creators', fontsize=7, ha='left')
ax.text(11.45, 6.95, '{', fontsize=6, ha='left', family='monospace', color='#EF6C00')
ax.text(11.6, 6.75, 'type: "ADD_TODO",', fontsize=6, ha='left', family='monospace', color='#EF6C00')
ax.text(11.6, 6.55, 'payload: { text }', fontsize=6, ha='left', family='monospace', color='#EF6C00')
ax.text(11.45, 6.35, '}', fontsize=6, ha='left', family='monospace', color='#EF6C00')

# DISPATCHER Details
disp_detail_box = FancyBboxPatch((11.3, 2.8), 2.5, 1.8,
                                boxstyle="round,pad=0.05", 
                                edgecolor='#2E7D32', facecolor=color_dispatcher,
                                linewidth=2)
ax.add_patch(disp_detail_box)
ax.text(12.55, 4.45, 'DISPATCHER', fontsize=10, ha='center', weight='bold', color='#2E7D32')
ax.text(11.45, 4.2, '• Central hub', fontsize=7, ha='left', weight='bold')
ax.text(11.45, 4.0, '• Receives ALL actions', fontsize=7, ha='left')
ax.text(11.45, 3.8, '• Dispatches to ALL stores', fontsize=7, ha='left')
ax.text(11.45, 3.6, '• Only ONE dispatcher', fontsize=7, ha='left')
ax.text(11.45, 3.25, 'dispatch(action) {', fontsize=6, ha='left', family='monospace', color='#2E7D32')
ax.text(11.6, 3.05, 'stores.forEach(...)', fontsize=6, ha='left', family='monospace')
ax.text(11.45, 2.85, '}', fontsize=6, ha='left', family='monospace', color='#2E7D32')

# STORE Details
store_detail_box = FancyBboxPatch((0.2, 2.8), 2.5, 1.8,
                                boxstyle="round,pad=0.05", 
                                edgecolor='#6A1B9A', facecolor=color_store,
                                linewidth=2)
ax.add_patch(store_detail_box)
ax.text(1.45, 4.45, 'STORE', fontsize=10, ha='center', weight='bold', color='#6A1B9A')
ax.text(0.35, 4.2, '• Holds application state', fontsize=7, ha='left', weight='bold')
ax.text(0.35, 4.0, '• Contains business logic', fontsize=7, ha='left')
ax.text(0.35, 3.8, '• Registered with dispatcher', fontsize=7, ha='left')
ax.text(0.35, 3.6, '• Emits change events', fontsize=7, ha='left')
ax.text(0.35, 3.25, 'handleAction(action) {', fontsize=6, ha='left', family='monospace', color='#6A1B9A')
ax.text(0.5, 3.05, 'updateState();', fontsize=6, ha='left', family='monospace')
ax.text(0.5, 2.85, 'emitChange();', fontsize=6, ha='left', family='monospace', color=color_flow)
ax.text(0.35, 2.65, '}', fontsize=6, ha='left', family='monospace', color='#6A1B9A')

# ===== DATA FLOW STEPS =====
flow_box = FancyBboxPatch((3.5, 0.1), 7, 2.0,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(flow_box)
ax.text(7, 2.0, 'Unidirectional Data Flow', fontsize=10, ha='center', weight='bold')

steps = [
    ('1', 'User clicks button in VIEW → creates ACTION', 1.7, '#1976D2'),
    ('2', 'ACTION sent to DISPATCHER', 1.45, '#EF6C00'),
    ('3', 'DISPATCHER broadcasts to all STORES', 1.2, '#2E7D32'),
    ('4', 'STORE updates state & emits change → VIEW re-renders', 0.95, '#6A1B9A')
]

for num, text, y, color in steps:
    ax.text(3.7, y, num, fontsize=8, ha='center', weight='bold',
           bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=1.5))
    ax.text(4.2, y, text, fontsize=7, ha='left', color=color)

# Key principle
principle_box = FancyBboxPatch((3.7, 0.2), 6.6, 0.5,
                              boxstyle="round,pad=0.05", 
                              edgecolor=color_flow, facecolor='#FFEBEE',
                              linewidth=2)
ax.add_patch(principle_box)
ax.text(7, 0.55, 'NO BIDIRECTIONAL FLOW: Data flows in ONE direction only', 
       fontsize=8, ha='center', weight='bold', color=color_flow)
ax.text(7, 0.35, '(Predictable, Debuggable, Scalable)', 
       fontsize=7, ha='center', style='italic', color=color_flow)

plt.tight_layout()
plt.savefig('docs/images/flux_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Flux Pattern diagram generated: docs/images/flux_pattern.png")

