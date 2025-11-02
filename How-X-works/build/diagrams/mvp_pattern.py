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
ax.text(7, 9.5, 'MVP Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Presenter mediates ALL communication between Model and View (Passive View)',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_model = '#E8F5E9'
color_view = '#E3F2FD'
color_presenter = '#FFF9E6'
color_user = '#FFE5CC'

# ===== MODEL =====
model_box = FancyBboxPatch((0.5, 5.5), 3.0, 2.5,
                           boxstyle="round,pad=0.1", 
                           edgecolor='#2E7D32', facecolor=color_model,
                           linewidth=3)
ax.add_patch(model_box)
ax.text(2.0, 7.75, 'MODEL', fontsize=14, ha='center', weight='bold', color='#2E7D32')
ax.text(2.0, 7.5, 'Data + Business Logic', fontsize=10, ha='center', style='italic', color='#666')

ax.text(0.7, 7.15, '• Application data', fontsize=8, ha='left')
ax.text(0.7, 6.9, '• Business rules', fontsize=8, ha='left')
ax.text(0.7, 6.65, '• NO Observer pattern', fontsize=8, ha='left', weight='bold', color='#C41E3A')
ax.text(0.7, 6.4, '• Completely independent', fontsize=8, ha='left')
ax.text(0.7, 6.1, 'class TodoModel {', fontsize=7, ha='left', family='monospace', color='#2E7D32')
ax.text(0.9, 5.9, 'addTodo(text) {...}', fontsize=7, ha='left', family='monospace')
ax.text(0.9, 5.7, 'getTodos() {...}', fontsize=7, ha='left', family='monospace')
ax.text(0.7, 5.5, '}', fontsize=7, ha='left', family='monospace', color='#2E7D32')

# ===== VIEW =====
view_box = FancyBboxPatch((10.5, 5.5), 3.0, 2.5,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#1976D2', facecolor=color_view,
                         linewidth=3)
ax.add_patch(view_box)
ax.text(12.0, 7.75, 'VIEW', fontsize=14, ha='center', weight='bold', color='#1976D2')
ax.text(12.0, 7.5, 'Passive UI (Interface)', fontsize=10, ha='center', style='italic', color='#666')

ax.text(10.7, 7.15, '• PASSIVE (no logic)', fontsize=8, ha='left', weight='bold', color='#1976D2')
ax.text(10.7, 6.9, '• Just an interface', fontsize=8, ha='left')
ax.text(10.7, 6.65, '• Delegates to Presenter', fontsize=8, ha='left')
ax.text(10.7, 6.4, '• Easy to mock/test', fontsize=8, ha='left')
ax.text(10.7, 6.1, 'class TodoView {', fontsize=7, ha='left', family='monospace', color='#1976D2')
ax.text(10.9, 5.9, 'displayTodos(todos) {...}', fontsize=7, ha='left', family='monospace')
ax.text(10.9, 5.7, 'bindAddTodo(handler) {...}', fontsize=7, ha='left', family='monospace')
ax.text(10.7, 5.5, '}', fontsize=7, ha='left', family='monospace', color='#1976D2')

# ===== PRESENTER =====
presenter_box = FancyBboxPatch((4.5, 5.0), 5.0, 3.0,
                              boxstyle="round,pad=0.1", 
                              edgecolor='#F57C00', facecolor=color_presenter,
                              linewidth=3)
ax.add_patch(presenter_box)
ax.text(7.0, 7.75, 'PRESENTER', fontsize=14, ha='center', weight='bold', color='#F57C00')
ax.text(7.0, 7.5, 'Mediator (ALL logic here)', fontsize=10, ha='center', style='italic', color='#666')

ax.text(4.7, 7.15, '• Mediates ALL M-V communication', fontsize=8, ha='left', weight='bold', color='#F57C00')
ax.text(4.7, 6.9, '• Handles user input from View', fontsize=8, ha='left')
ax.text(4.7, 6.65, '• Updates Model', fontsize=8, ha='left')
ax.text(4.7, 6.4, '• Updates View via interface methods', fontsize=8, ha='left')
ax.text(4.7, 6.15, '• Contains presentation logic', fontsize=8, ha='left')

ax.text(4.7, 5.75, 'class TodoPresenter {', fontsize=7, ha='left', family='monospace', color='#F57C00')
ax.text(4.9, 5.55, 'constructor(model, view) {...}', fontsize=7, ha='left', family='monospace')
ax.text(4.9, 5.35, 'handleAddTodo(text) {', fontsize=7, ha='left', family='monospace')
ax.text(5.1, 5.15, 'model.addTodo(text);', fontsize=6, ha='left', family='monospace', color='#2E7D32')
ax.text(5.1, 4.95, 'view.displayTodos(...);', fontsize=6, ha='left', family='monospace', color='#1976D2')
ax.text(4.9, 4.75, '}', fontsize=7, ha='left', family='monospace')
ax.text(4.7, 4.55, '}', fontsize=7, ha='left', family='monospace', color='#F57C00')

# ===== USER =====
user_circle = Circle((12.0, 3.0), 0.5, facecolor=color_user, edgecolor='#E65100', linewidth=2)
ax.add_patch(user_circle)
ax.text(12.0, 3.0, 'USER', fontsize=10, ha='center', weight='bold', color='#E65100')

# ===== RELATIONSHIPS =====

# 1. Presenter queries Model
arrow1 = FancyArrowPatch((4.5, 6.5), (3.5, 6.5),
                        arrowstyle='<->', mutation_scale=20, 
                        color='#F57C00', linewidth=2.5)
ax.add_patch(arrow1)
ax.text(4.0, 6.8, 'queries/', fontsize=8, ha='center', style='italic', color='#F57C00', weight='bold')
ax.text(4.0, 6.3, 'updates', fontsize=8, ha='center', style='italic', color='#F57C00', weight='bold')

# 2. Presenter updates View
arrow2 = FancyArrowPatch((9.5, 6.5), (10.5, 6.5),
                        arrowstyle='<->', mutation_scale=20, 
                        color='#F57C00', linewidth=2.5)
ax.add_patch(arrow2)
ax.text(10.0, 6.8, 'updates/', fontsize=8, ha='center', style='italic', color='#F57C00', weight='bold')
ax.text(10.0, 6.3, 'events', fontsize=8, ha='center', style='italic', color='#F57C00', weight='bold')

# 3. User interacts with View
arrow3 = FancyArrowPatch((12.0, 3.5), (12.0, 5.5),
                        arrowstyle='<->', mutation_scale=20, 
                        color='#E65100', linewidth=2)
ax.add_patch(arrow3)
ax.text(12.5, 4.5, 'interacts', fontsize=9, ha='left', style='italic', color='#E65100', weight='bold')

# X mark: NO direct M-V connection
ax.plot([3.5, 10.5], [6.5, 6.5], 'r--', linewidth=2, alpha=0.3)
ax.text(7.0, 9.2, '✗ NO direct Model-View communication', fontsize=10, ha='center', weight='bold', color='#C41E3A',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFEBEE', edgecolor='#C41E3A', linewidth=2))

# ===== FLOW DIAGRAM =====
flow_box = FancyBboxPatch((0.5, 0.1), 13, 4.0,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(flow_box)
ax.text(7, 3.95, 'MVP Flow: User Interaction', fontsize=11, ha='center', weight='bold')

steps = [
    ('1', 'User interacts with View (e.g., clicks button)', 3.55, '#E65100'),
    ('2', 'View delegates input to Presenter', 3.2, '#1976D2'),
    ('3', 'Presenter processes input', 2.85, '#F57C00'),
    ('4', 'Presenter updates Model', 2.5, '#2E7D32'),
    ('5', 'Presenter queries Model for updated data', 2.15, '#2E7D32'),
    ('6', 'Presenter updates View via interface methods', 1.8, '#1976D2'),
    ('7', 'View renders updated UI', 1.45, '#1976D2'),
    ('8', 'User sees updated UI', 1.1, '#E65100')
]

for num, text, y, color in steps:
    ax.text(0.7, y, num, fontsize=9, ha='center', weight='bold',
           bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=2))
    ax.text(1.2, y, text, fontsize=8, ha='left', color=color)

# Arrows between steps
for i in range(len(steps) - 1):
    _, _, y1, _ = steps[i]
    _, _, y2, _ = steps[i + 1]
    ax.annotate('', xy=(0.7, y2 + 0.08), xytext=(0.7, y1 - 0.08),
               arrowprops=dict(arrowstyle='->', color='#999', lw=1.5))

# Key difference highlight
diff_box = FancyBboxPatch((8.0, 0.5), 5.5, 0.9,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#1976D2', facecolor='#E3F2FD',
                         linewidth=2)
ax.add_patch(diff_box)
ax.text(10.75, 1.25, 'Key Difference from MVC', fontsize=9, ha='center', weight='bold', color='#1976D2')
ax.text(8.2, 0.95, 'MVC: View observes Model directly', fontsize=7, ha='left', color='#C41E3A')
ax.text(8.2, 0.75, 'MVP: Presenter mediates ALL communication', fontsize=7, ha='left', color='#1976D2', weight='bold')
ax.text(8.2, 0.55, '        View is completely PASSIVE', fontsize=7, ha='left', color='#1976D2', weight='bold')

plt.tight_layout()
plt.savefig('docs/images/mvp_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ MVP Pattern diagram generated: docs/images/mvp_pattern.png")

