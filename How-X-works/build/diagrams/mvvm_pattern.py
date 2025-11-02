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
ax.text(7, 9.5, 'MVVM Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Two-way data binding between View and ViewModel (automatic synchronization)',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_model = '#E8F5E9'
color_view = '#E3F2FD'
color_viewmodel = '#FFF3E6'
color_binding = '#F8BBD0'

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
ax.text(0.7, 6.65, '• Independent of UI', fontsize=8, ha='left')
ax.text(0.7, 6.4, '• Can notify ViewModel', fontsize=8, ha='left')

ax.text(0.7, 6.05, 'class TodoModel {', fontsize=7, ha='left', family='monospace', color='#2E7D32')
ax.text(0.9, 5.85, 'addTodo(text) {...}', fontsize=7, ha='left', family='monospace')
ax.text(0.9, 5.65, 'getTodos() {...}', fontsize=7, ha='left', family='monospace')
ax.text(0.7, 5.45, '}', fontsize=7, ha='left', family='monospace', color='#2E7D32')

# ===== VIEW =====
view_box = FancyBboxPatch((10.5, 5.5), 3.0, 2.5,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#1976D2', facecolor=color_view,
                         linewidth=3)
ax.add_patch(view_box)
ax.text(12.0, 7.75, 'VIEW', fontsize=14, ha='center', weight='bold', color='#1976D2')
ax.text(12.0, 7.5, 'Declarative UI Template', fontsize=10, ha='center', style='italic', color='#666')

ax.text(10.7, 7.15, '• DECLARATIVE bindings', fontsize=8, ha='left', weight='bold', color='#1976D2')
ax.text(10.7, 6.9, '• No imperative code', fontsize=8, ha='left')
ax.text(10.7, 6.65, '• Two-way data binding', fontsize=8, ha='left')
ax.text(10.7, 6.4, '• Automatic sync', fontsize=8, ha='left', weight='bold', color='#E91E63')

ax.text(10.7, 6.05, '<div>', fontsize=7, ha='left', family='monospace', color='#1976D2')
ax.text(10.9, 5.85, '<input v-model="count" />', fontsize=7, ha='left', family='monospace', color='#E91E63')
ax.text(10.9, 5.65, '<h2>{{ count }}</h2>', fontsize=7, ha='left', family='monospace')
ax.text(10.7, 5.45, '</div>', fontsize=7, ha='left', family='monospace', color='#1976D2')

# ===== VIEW MODEL =====
viewmodel_box = FancyBboxPatch((4.5, 5.0), 5.0, 3.0,
                              boxstyle="round,pad=0.1", 
                              edgecolor='#F57C00', facecolor=color_viewmodel,
                              linewidth=3)
ax.add_patch(viewmodel_box)
ax.text(7.0, 7.75, 'VIEW MODEL', fontsize=14, ha='center', weight='bold', color='#F57C00')
ax.text(7.0, 7.5, 'Exposes data & commands for View', fontsize=10, ha='center', style='italic', color='#666')

ax.text(4.7, 7.15, '• Observable/Reactive properties', fontsize=8, ha='left', weight='bold', color='#F57C00')
ax.text(4.7, 6.9, '• Computed properties', fontsize=8, ha='left')
ax.text(4.7, 6.65, '• Commands (methods)', fontsize=8, ha='left')
ax.text(4.7, 6.4, '• View binds to ViewModel', fontsize=8, ha='left')
ax.text(4.7, 6.15, '• Auto-notifies View on change', fontsize=8, ha='left', weight='bold', color='#E91E63')

ax.text(4.7, 5.75, 'class TodoViewModel {', fontsize=7, ha='left', family='monospace', color='#F57C00')
ax.text(4.9, 5.55, 'data() {', fontsize=7, ha='left', family='monospace')
ax.text(5.1, 5.35, 'return { count: 0 };', fontsize=6, ha='left', family='monospace', color='#E91E63')
ax.text(4.9, 5.15, '}', fontsize=7, ha='left', family='monospace')
ax.text(4.9, 4.95, 'computed: { ... }', fontsize=7, ha='left', family='monospace')
ax.text(4.9, 4.75, 'methods: { ... }', fontsize=7, ha='left', family='monospace')
ax.text(4.7, 4.55, '}', fontsize=7, ha='left', family='monospace', color='#F57C00')

# ===== TWO-WAY DATA BINDING =====
binding_box = FancyBboxPatch((5.5, 8.5), 3.0, 0.8,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#E91E63', facecolor=color_binding,
                            linewidth=2.5)
ax.add_patch(binding_box)
ax.text(7.0, 9.15, 'TWO-WAY DATA BINDING', fontsize=10, ha='center', weight='bold', color='#E91E63')
ax.text(7.0, 8.85, '(Automatic Synchronization)', fontsize=8, ha='center', style='italic', color='#E91E63')

# ===== RELATIONSHIPS =====

# 1. ViewModel observes Model
arrow1 = FancyArrowPatch((3.5, 6.75), (4.5, 6.75),
                        arrowstyle='->', mutation_scale=20, 
                        color='#2E7D32', linewidth=2)
ax.add_patch(arrow1)
ax.text(4.0, 7.0, 'observes/', fontsize=8, ha='center', style='italic', color='#2E7D32')
ax.text(4.0, 6.5, 'updates', fontsize=8, ha='center', style='italic', color='#2E7D32')

# 2. TWO-WAY BINDING between View and ViewModel
arrow2 = FancyArrowPatch((9.5, 6.75), (10.5, 6.75),
                        arrowstyle='<->', mutation_scale=25, 
                        color='#E91E63', linewidth=3)
ax.add_patch(arrow2)

# Binding label
ax.text(10.0, 7.15, 'TWO-WAY', fontsize=9, ha='center', style='italic', color='#E91E63', weight='bold')
ax.text(10.0, 6.95, 'DATA', fontsize=9, ha='center', style='italic', color='#E91E63', weight='bold')
ax.text(10.0, 6.75, 'BINDING', fontsize=9, ha='center', style='italic', color='#E91E63', weight='bold')
ax.text(10.0, 6.4, '(AUTOMATIC)', fontsize=8, ha='center', style='italic', color='#E91E63', weight='bold')

# Binding details
binding_detail_box = FancyBboxPatch((9.0, 5.8), 2.0, 0.4,
                                   boxstyle="round,pad=0.05", 
                                   edgecolor='#E91E63', facecolor='#FCE4EC',
                                   linewidth=1)
ax.add_patch(binding_detail_box)
ax.text(10.0, 6.1, 'ViewModel changes', fontsize=6, ha='center', color='#E91E63')
ax.text(10.0, 5.95, '→ View updates', fontsize=6, ha='center', color='#E91E63')

binding_detail_box2 = FancyBboxPatch((9.0, 5.2), 2.0, 0.4,
                                    boxstyle="round,pad=0.05", 
                                    edgecolor='#E91E63', facecolor='#FCE4EC',
                                    linewidth=1)
ax.add_patch(binding_detail_box2)
ax.text(10.0, 5.5, 'View changes (input)', fontsize=6, ha='center', color='#E91E63')
ax.text(10.0, 5.35, '→ ViewModel updates', fontsize=6, ha='center', color='#E91E63')

# ===== FLOW DIAGRAM =====
flow_box = FancyBboxPatch((0.5, 0.1), 13, 4.0,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(flow_box)
ax.text(7, 3.95, 'MVVM Flow with Two-Way Binding', fontsize=11, ha='center', weight='bold')

steps = [
    ('1', 'User changes input in View (e.g., types in textbox)', 3.55, '#1976D2'),
    ('2', 'Data binding automatically updates ViewModel property', 3.2, '#E91E63'),
    ('3', 'ViewModel processes change (computed properties, etc.)', 2.85, '#F57C00'),
    ('4', 'ViewModel may update Model (business logic)', 2.5, '#2E7D32'),
    ('5', 'Model notifies ViewModel of data changes', 2.15, '#2E7D32'),
    ('6', 'ViewModel reactive property changes', 1.8, '#F57C00'),
    ('7', 'Data binding automatically updates ALL bound View elements', 1.45, '#E91E63'),
    ('8', 'User sees updated UI (NO manual DOM manipulation)', 1.1, '#1976D2')
]

for num, text, y, color in steps:
    ax.text(0.7, y, num, fontsize=9, ha='center', weight='bold',
           bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=2))
    ax.text(1.2, y, text, fontsize=8, ha='left', color=color)

# Arrows
for i in range(len(steps) - 1):
    _, _, y1, _ = steps[i]
    _, _, y2, _ = steps[i + 1]
    ax.annotate('', xy=(0.7, y2 + 0.08), xytext=(0.7, y1 - 0.08),
               arrowprops=dict(arrowstyle='->', color='#999', lw=1.5))

# Key difference
diff_box = FancyBboxPatch((8.0, 0.5), 5.5, 0.9,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#E91E63', facecolor='#FCE4EC',
                         linewidth=2)
ax.add_patch(diff_box)
ax.text(10.75, 1.25, 'Key Difference from MVC/MVP', fontsize=9, ha='center', weight='bold', color='#E91E63')
ax.text(8.2, 0.95, 'MVC/MVP: Manual view updates (imperative)', fontsize=7, ha='left', color='#666')
ax.text(8.2, 0.75, 'MVVM: Two-way data binding (declarative)', fontsize=7, ha='left', color='#E91E63', weight='bold')
ax.text(8.2, 0.55, '           AUTOMATIC synchronization', fontsize=7, ha='left', color='#E91E63', weight='bold')

plt.tight_layout()
plt.savefig('docs/images/mvvm_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ MVVM Pattern diagram generated: docs/images/mvvm_pattern.png")

