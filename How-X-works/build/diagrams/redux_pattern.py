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
ax.text(7, 9.5, 'Redux Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Single store, pure reducers, unidirectional flow',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_store = '#764AF1'  # Purple (single store)
color_action = '#FFA500'
color_reducer = '#00BCD4'
color_view = '#4CAF50'
color_middleware = '#FF5722'

# ===== CENTRAL STORE (SINGLE SOURCE OF TRUTH) =====
store_box = FancyBboxPatch((5.5, 4.5), 3.0, 2.0,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#764AF1', facecolor='#F3E5F5',
                          linewidth=4)
ax.add_patch(store_box)
ax.text(7, 6.25, 'SINGLE STORE', fontsize=13, ha='center', weight='bold', color='#764AF1')
ax.text(7, 6.0, '(One State Tree)', fontsize=10, ha='center', style='italic', color='#764AF1')

ax.text(5.7, 5.7, '{', fontsize=9, ha='left', family='monospace', color='#764AF1')
ax.text(5.85, 5.5, 'user: {...},', fontsize=8, ha='left', family='monospace')
ax.text(5.85, 5.3, 'todos: {...},', fontsize=8, ha='left', family='monospace')
ax.text(5.85, 5.1, 'cart: {...}', fontsize=8, ha='left', family='monospace')
ax.text(5.7, 4.9, '}', fontsize=9, ha='left', family='monospace', color='#764AF1')

# Three principles
principles_box = FancyBboxPatch((5.5, 3.5), 3.0, 0.8,
                               boxstyle="round,pad=0.05", 
                               edgecolor='#764AF1', facecolor='#EDE7F6',
                               linewidth=2)
ax.add_patch(principles_box)
ax.text(7, 4.15, '3 Principles:', fontsize=8, ha='center', weight='bold', color='#764AF1')
ax.text(7, 3.95, '1. Single source of truth', fontsize=6, ha='center')
ax.text(7, 3.80, '2. State is read-only', fontsize=6, ha='center')
ax.text(7, 3.65, '3. Changes via pure functions', fontsize=6, ha='center')

# ===== VIEW =====
view_box = FancyBboxPatch((0.5, 4.5), 2.5, 2.0,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#4CAF50', facecolor='#E8F5E9',
                         linewidth=2.5)
ax.add_patch(view_box)
ax.text(1.75, 6.25, 'VIEW (UI)', fontsize=11, ha='center', weight='bold', color='#4CAF50')

ax.text(0.7, 5.95, '• Subscribes to store', fontsize=7, ha='left')
ax.text(0.7, 5.75, '• Re-renders on change', fontsize=7, ha='left')
ax.text(0.7, 5.55, '• Dispatches actions', fontsize=7, ha='left', weight='bold', color=color_action)

ax.text(0.7, 5.25, 'const state = ', fontsize=6, ha='left', family='monospace')
ax.text(0.7, 5.05, '  useSelector(s => s);', fontsize=6, ha='left', family='monospace', color='#4CAF50')
ax.text(0.7, 4.85, 'dispatch(action);', fontsize=6, ha='left', family='monospace', color=color_action)

# ===== ACTIONS =====
action_box = FancyBboxPatch((0.5, 7.5), 2.5, 1.3,
                           boxstyle="round,pad=0.05", 
                           edgecolor='#FFA500', facecolor='#FFF3E0',
                           linewidth=2.5)
ax.add_patch(action_box)
ax.text(1.75, 8.6, 'ACTIONS', fontsize=11, ha='center', weight='bold', color='#FFA500')

ax.text(0.7, 8.3, '• Plain objects', fontsize=7, ha='left')
ax.text(0.7, 8.1, '• { type, payload }', fontsize=7, ha='left', weight='bold')
ax.text(0.7, 7.9, '• Describe events', fontsize=7, ha='left')

ax.text(0.7, 7.6, '{ type: "ADD_TODO",', fontsize=6, ha='left', family='monospace', color='#FFA500')
ax.text(0.8, 7.4, 'payload: {...} }', fontsize=6, ha='left', family='monospace')

# ===== MIDDLEWARE =====
middleware_box = FancyBboxPatch((4.0, 7.5), 2.5, 1.3,
                               boxstyle="round,pad=0.05", 
                               edgecolor='#FF5722', facecolor='#FFEBEE',
                               linewidth=2.5)
ax.add_patch(middleware_box)
ax.text(5.25, 8.6, 'MIDDLEWARE', fontsize=11, ha='center', weight='bold', color='#FF5722')

ax.text(4.2, 8.3, '• Intercepts actions', fontsize=7, ha='left')
ax.text(4.2, 8.1, '• Async logic (thunks)', fontsize=7, ha='left')
ax.text(4.2, 7.9, '• Logging, etc.', fontsize=7, ha='left')

ax.text(4.2, 7.6, 'action => {', fontsize=6, ha='left', family='monospace', color='#FF5722')
ax.text(4.35, 7.4, '// logic', fontsize=6, ha='left', family='monospace')
ax.text(4.35, 7.2, 'next(action);', fontsize=6, ha='left', family='monospace')
ax.text(4.2, 7.0, '}', fontsize=6, ha='left', family='monospace', color='#FF5722')

# ===== REDUCERS =====
reducer_box = FancyBboxPatch((7.5, 7.5), 2.5, 1.3,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#00BCD4', facecolor='#E0F7FA',
                            linewidth=2.5)
ax.add_patch(reducer_box)
ax.text(8.75, 8.6, 'REDUCERS', fontsize=11, ha='center', weight='bold', color='#00BCD4')

ax.text(7.7, 8.3, '• PURE functions', fontsize=7, ha='left', weight='bold', color='#00BCD4')
ax.text(7.7, 8.1, '• (state, action)', fontsize=7, ha='left')
ax.text(7.7, 7.9, '   => newState', fontsize=7, ha='left')
ax.text(7.7, 7.7, '• IMMUTABLE', fontsize=7, ha='left', weight='bold', color='#00BCD4')

ax.text(7.7, 7.4, '(s, a) => ({', fontsize=6, ha='left', family='monospace', color='#00BCD4')
ax.text(7.85, 7.2, '...s, count: s+1', fontsize=6, ha='left', family='monospace')
ax.text(7.7, 7.0, '})', fontsize=6, ha='left', family='monospace', color='#00BCD4')

# ===== SUBSCRIBERS =====
sub_box = FancyBboxPatch((11, 4.5), 2.5, 2.0,
                        boxstyle="round,pad=0.05", 
                        edgecolor='#4CAF50', facecolor='#E8F5E9',
                        linewidth=2.5)
ax.add_patch(sub_box)
ax.text(12.25, 6.25, 'SUBSCRIBERS', fontsize=11, ha='center', weight='bold', color='#4CAF50')

ax.text(11.2, 5.95, '• Listen to store', fontsize=7, ha='left')
ax.text(11.2, 5.75, '• Get notified', fontsize=7, ha='left')
ax.text(11.2, 5.55, '• Re-render UI', fontsize=7, ha='left')

ax.text(11.2, 5.25, 'store.subscribe', fontsize=6, ha='left', family='monospace', color='#4CAF50')
ax.text(11.2, 5.05, '  (() => {', fontsize=6, ha='left', family='monospace')
ax.text(11.35, 4.85, 'render();', fontsize=6, ha='left', family='monospace', color='#4CAF50')
ax.text(11.2, 4.65, '});', fontsize=6, ha='left', family='monospace')

# ===== DATA FLOW ARROWS =====

# 1. View → Action
arrow1 = FancyArrowPatch((1.75, 6.5), (1.75, 7.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_action, linewidth=3)
ax.add_patch(arrow1)
ax.text(2.1, 7.0, '1. dispatch', fontsize=8, ha='left', weight='bold', color=color_action)

# 2. Action → Middleware
arrow2 = FancyArrowPatch((3.0, 8.15), (4.0, 8.15),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_action, linewidth=3)
ax.add_patch(arrow2)
ax.text(3.5, 8.4, '2', fontsize=8, ha='center', weight='bold', color=color_action)

# 3. Middleware → Reducer
arrow3 = FancyArrowPatch((6.5, 8.15), (7.5, 8.15),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_action, linewidth=3)
ax.add_patch(arrow3)
ax.text(7.0, 8.4, '3', fontsize=8, ha='center', weight='bold', color=color_action)

# 4. Reducer → Store
arrow4 = FancyArrowPatch((8.75, 7.5), (7.75, 6.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color=color_reducer, linewidth=3)
ax.add_patch(arrow4)
ax.text(8.5, 7.0, '4. new state', fontsize=8, ha='left', weight='bold', color=color_reducer)

# 5. Store → Subscribers
arrow5 = FancyArrowPatch((8.5, 5.5), (11.0, 5.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color='#764AF1', linewidth=3)
ax.add_patch(arrow5)
ax.text(9.75, 5.75, '5. notify', fontsize=8, ha='center', weight='bold', color='#764AF1')

# 6. Subscribers → View (re-render)
arrow6 = FancyArrowPatch((12.25, 4.5), (12.25, 3.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color='#4CAF50', linewidth=2.5)
ax.add_patch(arrow6)
arrow6b = FancyArrowPatch((12.25, 3.5), (3.0, 3.5),
                         arrowstyle='->,head_width=0.4,head_length=0.6',
                         color='#4CAF50', linewidth=2.5)
ax.add_patch(arrow6b)
arrow6c = FancyArrowPatch((3.0, 3.5), (1.75, 4.5),
                         arrowstyle='->,head_width=0.4,head_length=0.6',
                         color='#4CAF50', linewidth=2.5)
ax.add_patch(arrow6c)
ax.text(7.0, 3.2, '6. re-render', fontsize=8, ha='center', weight='bold', color='#4CAF50')

# ===== COMPARISON TABLE =====
comparison_box = FancyBboxPatch((0.3, 0.1), 13.4, 2.8,
                               boxstyle="round,pad=0.05", 
                               edgecolor='#666', facecolor='#FAFAFA',
                               linewidth=1.5)
ax.add_patch(comparison_box)
ax.text(7, 2.75, 'Redux vs Flux Comparison', fontsize=11, ha='center', weight='bold')

# Table headers
ax.text(1.5, 2.5, 'Aspect', fontsize=9, ha='center', weight='bold', color='#333')
ax.text(4.5, 2.5, 'Flux', fontsize=9, ha='center', weight='bold', color='#FF9800')
ax.text(8.5, 2.5, 'Redux', fontsize=9, ha='center', weight='bold', color='#764AF1')
ax.text(11.5, 2.5, 'Benefit', fontsize=9, ha='center', weight='bold', color='#4CAF50')

# Divider
ax.plot([0.5, 13.5], [2.4, 2.4], color='#999', linewidth=1)

# Table rows
rows = [
    ('Stores', 'Multiple stores', 'SINGLE store', 'Simpler'),
    ('State Updates', 'Store methods', 'Pure reducers', 'Testable'),
    ('Dispatcher', 'Central dispatcher', 'No dispatcher', 'Less boilerplate'),
    ('Async', 'In action creators', 'Middleware', 'Pluggable'),
    ('Time Travel', 'Difficult', 'Built-in', 'DevTools')
]

y_pos = 2.2
for label, flux, redux, benefit in rows:
    ax.text(1.5, y_pos, label, fontsize=7, ha='center', color='#333')
    ax.text(4.5, y_pos, flux, fontsize=7, ha='center', color='#FF9800')
    ax.text(8.5, y_pos, redux, fontsize=7, ha='center', color='#764AF1', weight='bold')
    ax.text(11.5, y_pos, benefit, fontsize=7, ha='center', color='#4CAF50')
    y_pos -= 0.35

# Key advantage
key_box = FancyBboxPatch((1.0, 0.2), 12.0, 0.4,
                        boxstyle="round,pad=0.05", 
                        edgecolor='#764AF1', facecolor='#F3E5F5',
                        linewidth=2)
ax.add_patch(key_box)
ax.text(7, 0.5, 'Key Advantage: Single store + Pure reducers = Predictable, Testable, Time-travel debugging', 
       fontsize=8, ha='center', weight='bold', color='#764AF1')
ax.text(7, 0.3, '(Most popular state management for React)', 
       fontsize=7, ha='center', style='italic', color='#764AF1')

plt.tight_layout()
plt.savefig('docs/images/redux_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Redux Pattern diagram generated: docs/images/redux_pattern.png")

