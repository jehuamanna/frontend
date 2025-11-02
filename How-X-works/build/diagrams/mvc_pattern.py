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
ax.text(7, 9.5, 'MVC Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Separate application into Model (data), View (UI), and Controller (input handling)',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_model = '#E8F5E9'
color_view = '#E3F2FD'
color_controller = '#FFF9E6'
color_user = '#FFE5CC'

# ===== MODEL =====
model_box = FancyBboxPatch((0.5, 5.5), 3.5, 2.5,
                           boxstyle="round,pad=0.1", 
                           edgecolor='#2E7D32', facecolor=color_model,
                           linewidth=3)
ax.add_patch(model_box)
ax.text(2.25, 7.75, 'MODEL', fontsize=14, ha='center', weight='bold', color='#2E7D32')
ax.text(2.25, 7.5, 'Data + Business Logic', fontsize=10, ha='center', style='italic', color='#666')

ax.text(0.7, 7.15, '• Manages application data', fontsize=8, ha='left')
ax.text(0.7, 6.9, '• Business rules & validation', fontsize=8, ha='left')
ax.text(0.7, 6.65, '• Notifies observers (View)', fontsize=8, ha='left')
ax.text(0.7, 6.4, '• Independent of UI', fontsize=8, ha='left')

ax.text(0.7, 6.05, 'Example:', fontsize=8, ha='left', weight='bold')
ax.text(0.7, 5.8, 'class TodoModel {', fontsize=7, ha='left', family='monospace', color='#2E7D32')
ax.text(0.9, 5.6, 'addTodo(text) {...}', fontsize=7, ha='left', family='monospace')
ax.text(0.9, 5.4, 'removeTodo(id) {...}', fontsize=7, ha='left', family='monospace')
ax.text(0.7, 5.2, '}', fontsize=7, ha='left', family='monospace', color='#2E7D32')

# ===== VIEW =====
view_box = FancyBboxPatch((5.0, 5.5), 3.5, 2.5,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#1976D2', facecolor=color_view,
                         linewidth=3)
ax.add_patch(view_box)
ax.text(6.75, 7.75, 'VIEW', fontsize=14, ha='center', weight='bold', color='#1976D2')
ax.text(6.75, 7.5, 'UI Presentation', fontsize=10, ha='center', style='italic', color='#666')

ax.text(5.2, 7.15, '• Displays data to user', fontsize=8, ha='left')
ax.text(5.2, 6.9, '• Observes Model for changes', fontsize=8, ha='left')
ax.text(5.2, 6.65, '• Sends user input to Controller', fontsize=8, ha='left')
ax.text(5.2, 6.4, '• No business logic', fontsize=8, ha='left')

ax.text(5.2, 6.05, 'Example:', fontsize=8, ha='left', weight='bold')
ax.text(5.2, 5.8, 'class TodoView {', fontsize=7, ha='left', family='monospace', color='#1976D2')
ax.text(5.4, 5.6, 'render() {...}', fontsize=7, ha='left', family='monospace')
ax.text(5.4, 5.4, 'bindAddTodo(handler) {...}', fontsize=7, ha='left', family='monospace')
ax.text(5.2, 5.2, '}', fontsize=7, ha='left', family='monospace', color='#1976D2')

# ===== CONTROLLER =====
controller_box = FancyBboxPatch((9.5, 5.5), 4.0, 2.5,
                               boxstyle="round,pad=0.1", 
                               edgecolor='#F57C00', facecolor=color_controller,
                               linewidth=3)
ax.add_patch(controller_box)
ax.text(11.5, 7.75, 'CONTROLLER', fontsize=14, ha='center', weight='bold', color='#F57C00')
ax.text(11.5, 7.5, 'Input Handling', fontsize=10, ha='center', style='italic', color='#666')

ax.text(9.7, 7.15, '• Handles user input from View', fontsize=8, ha='left')
ax.text(9.7, 6.9, '• Updates Model based on input', fontsize=8, ha='left')
ax.text(9.7, 6.65, '• Selects View to display', fontsize=8, ha='left')
ax.text(9.7, 6.4, '• Coordinates Model & View', fontsize=8, ha='left')

ax.text(9.7, 6.05, 'Example:', fontsize=8, ha='left', weight='bold')
ax.text(9.7, 5.8, 'class TodoController {', fontsize=7, ha='left', family='monospace', color='#F57C00')
ax.text(9.9, 5.6, 'handleAddTodo(text) {', fontsize=7, ha='left', family='monospace')
ax.text(10.1, 5.4, 'model.addTodo(text);', fontsize=6, ha='left', family='monospace')
ax.text(9.9, 5.2, '}', fontsize=7, ha='left', family='monospace')
ax.text(9.7, 5.0, '}', fontsize=7, ha='left', family='monospace', color='#F57C00')

# ===== USER =====
user_circle = Circle((11.5, 3.5), 0.6, facecolor=color_user, edgecolor='#E65100', linewidth=2)
ax.add_patch(user_circle)
ax.text(11.5, 3.5, 'USER', fontsize=10, ha='center', weight='bold', color='#E65100')

# ===== RELATIONSHIPS (ARROWS) =====

# 1. Model notifies View (Observer pattern)
arrow1 = FancyArrowPatch((4.0, 6.75), (5.0, 6.75),
                        arrowstyle='->', mutation_scale=20, 
                        color='#2E7D32', linewidth=2.5)
ax.add_patch(arrow1)
ax.text(4.5, 7.0, 'notifies', fontsize=9, ha='center', style='italic', color='#2E7D32', weight='bold')
ax.text(4.5, 6.5, '(Observer)', fontsize=7, ha='center', style='italic', color='#666')

# 2. View queries Model (read data)
arrow2 = FancyArrowPatch((5.0, 6.25), (4.0, 6.25),
                        arrowstyle='->', mutation_scale=15, 
                        color='#1976D2', linewidth=1.5, linestyle='dotted')
ax.add_patch(arrow2)
ax.text(4.5, 6.0, 'queries', fontsize=8, ha='center', style='italic', color='#1976D2')

# 3. Controller updates Model
arrow3 = FancyArrowPatch((9.5, 6.75), (4.0, 6.75),
                        arrowstyle='->', mutation_scale=20, 
                        color='#F57C00', linewidth=2.5)
ax.add_patch(arrow3)
ax.text(6.75, 7.05, 'updates', fontsize=9, ha='center', style='italic', color='#F57C00', weight='bold')

# 4. Controller updates View (selects view)
arrow4 = FancyArrowPatch((9.5, 6.25), (8.5, 6.25),
                        arrowstyle='->', mutation_scale=15, 
                        color='#F57C00', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow4)
ax.text(9.0, 6.5, 'selects', fontsize=8, ha='center', style='italic', color='#F57C00')

# 5. User interacts with View
arrow5 = FancyArrowPatch((11.5, 4.1), (6.75, 5.5),
                        arrowstyle='->', mutation_scale=20, 
                        color='#E65100', linewidth=2)
ax.add_patch(arrow5)
ax.text(9.0, 4.9, 'sees & interacts', fontsize=9, ha='center', style='italic', color='#E65100', weight='bold')

# 6. View sends input to Controller
arrow6 = FancyArrowPatch((8.5, 6.0), (9.5, 6.0),
                        arrowstyle='->', mutation_scale=20, 
                        color='#1976D2', linewidth=2)
ax.add_patch(arrow6)
ax.text(9.0, 5.75, 'input', fontsize=8, ha='center', style='italic', color='#1976D2')

# ===== FLOW DIAGRAM =====
flow_box = FancyBboxPatch((0.5, 0.1), 13, 4.5,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(flow_box)
ax.text(7, 4.4, 'MVC Flow: User Interaction', fontsize=11, ha='center', weight='bold')

# Step-by-step flow
steps = [
    ('1', 'User interacts with View (e.g., clicks button)', 4.0, '#E65100'),
    ('2', 'View sends user input to Controller', 3.6, '#1976D2'),
    ('3', 'Controller processes input and updates Model', 3.2, '#F57C00'),
    ('4', 'Model validates and updates data', 2.8, '#2E7D32'),
    ('5', 'Model notifies View of changes (Observer)', 2.4, '#2E7D32'),
    ('6', 'View queries Model for new data', 2.0, '#1976D2'),
    ('7', 'View re-renders UI with updated data', 1.6, '#1976D2'),
    ('8', 'User sees updated UI', 1.2, '#E65100')
]

for num, text, y, color in steps:
    ax.text(0.7, y, num, fontsize=10, ha='center', weight='bold',
           bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=2))
    ax.text(1.2, y, text, fontsize=9, ha='left', color=color)

# Visual flow arrows
for i in range(len(steps) - 1):
    _, _, y1, _ = steps[i]
    _, _, y2, _ = steps[i + 1]
    ax.annotate('', xy=(0.7, y2 + 0.1), xytext=(0.7, y1 - 0.1),
               arrowprops=dict(arrowstyle='->', color='#999', lw=1.5))

# ===== KEY BENEFITS =====
benefits_box = FancyBboxPatch((7.0, 0.5), 6.5, 0.8,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#2E7D32', facecolor='#E8F5E9',
                             linewidth=1)
ax.add_patch(benefits_box)
ax.text(10.25, 1.15, 'Key Benefits', fontsize=9, ha='center', weight='bold', color='#2E7D32')
ax.text(7.2, 0.9, '✓ Separation of concerns', fontsize=7, ha='left', color='#2E7D32')
ax.text(7.2, 0.7, '✓ Parallel development', fontsize=7, ha='left', color='#2E7D32')
ax.text(9.3, 0.9, '✓ Multiple views per model', fontsize=7, ha='left', color='#2E7D32')
ax.text(9.3, 0.7, '✓ Easy testing', fontsize=7, ha='left', color='#2E7D32')
ax.text(11.5, 0.9, '✓ Reusable components', fontsize=7, ha='left', color='#2E7D32')
ax.text(11.5, 0.7, '✓ Maintainable codebase', fontsize=7, ha='left', color='#2E7D32')

plt.tight_layout()
plt.savefig('docs/images/mvc_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ MVC Pattern diagram generated: docs/images/mvc_pattern.png")

