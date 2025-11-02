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
ax.text(7, 9.5, 'Mediator Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Centralized communication hub reducing coupling between components',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_mediator = '#FFF3B0'
color_colleague = '#B8E6F0'
color_interface = '#E8F4F8'

# ===== MEDIATOR INTERFACE =====
mediator_interface = FancyBboxPatch((5.5, 7.0), 3.0, 1.5,
                                   boxstyle="round,pad=0.1", 
                                   edgecolor='#F77F00', facecolor=color_interface,
                                   linewidth=2, linestyle='--')
ax.add_patch(mediator_interface)
ax.text(7.0, 8.2, '«interface»', fontsize=9, ha='center', style='italic', color='#F77F00')
ax.text(7.0, 7.9, 'Mediator', fontsize=12, ha='center', weight='bold')
ax.text(7.0, 7.5, 'notify(sender, event)', fontsize=10, ha='center', family='monospace')
ax.text(7.0, 7.2, 'register(colleague)', fontsize=10, ha='center', family='monospace')

# ===== CONCRETE MEDIATOR =====
concrete_mediator = FancyBboxPatch((5.5, 4.5), 3.0, 2.0,
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#F77F00', facecolor=color_mediator,
                                  linewidth=2.5)
ax.add_patch(concrete_mediator)
ax.text(7.0, 6.2, 'ConcreteMediator', fontsize=12, ha='center', weight='bold')
ax.text(7.0, 5.85, '(ChatRoom / EventBus)', fontsize=9, ha='center', style='italic', color='#666')
ax.text(7.0, 5.5, 'colleagues[]', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(7.0, 5.2, 'notify(sender, event)', fontsize=10, ha='center', family='monospace')
ax.text(7.0, 4.9, 'registerColleague(c)', fontsize=10, ha='center', family='monospace')
ax.text(7.0, 4.6, 'coordinateAction()', fontsize=9, ha='center', family='monospace')

# ===== COLLEAGUE INTERFACE =====
colleague_interface = FancyBboxPatch((0.5, 2.5), 2.5, 1.3,
                                    boxstyle="round,pad=0.1", 
                                    edgecolor='#2E86AB', facecolor=color_interface,
                                    linewidth=2, linestyle='--')
ax.add_patch(colleague_interface)
ax.text(1.75, 3.6, '«interface»', fontsize=9, ha='center', style='italic', color='#2E86AB')
ax.text(1.75, 3.3, 'Colleague', fontsize=11, ha='center', weight='bold')
ax.text(1.75, 3.0, 'mediator', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(1.75, 2.7, 'send(msg)', fontsize=9, ha='center', family='monospace')

# ===== COLLEAGUE A =====
colleagueA = FancyBboxPatch((0.3, 0.3), 1.2, 1.5,
                           boxstyle="round,pad=0.1", 
                           edgecolor='#2E86AB', facecolor=color_colleague,
                           linewidth=2)
ax.add_patch(colleagueA)
ax.text(0.9, 1.6, 'ColleagueA', fontsize=10, ha='center', weight='bold')
ax.text(0.9, 1.35, '(User)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(0.9, 1.1, 'mediator', fontsize=8, ha='center', family='monospace', color='#555')
ax.text(0.9, 0.85, 'send()', fontsize=9, ha='center', family='monospace')
ax.text(0.9, 0.6, 'receive()', fontsize=9, ha='center', family='monospace')

# ===== COLLEAGUE B =====
colleagueB = FancyBboxPatch((1.8, 0.3), 1.2, 1.5,
                           boxstyle="round,pad=0.1", 
                           edgecolor='#2E86AB', facecolor=color_colleague,
                           linewidth=2)
ax.add_patch(colleagueB)
ax.text(2.4, 1.6, 'ColleagueB', fontsize=10, ha='center', weight='bold')
ax.text(2.4, 1.35, '(User)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(2.4, 1.1, 'mediator', fontsize=8, ha='center', family='monospace', color='#555')
ax.text(2.4, 0.85, 'send()', fontsize=9, ha='center', family='monospace')
ax.text(2.4, 0.6, 'receive()', fontsize=9, ha='center', family='monospace')

# ===== COLLEAGUE C =====
colleagueC = FancyBboxPatch((3.3, 0.3), 1.2, 1.5,
                           boxstyle="round,pad=0.1", 
                           edgecolor='#2E86AB', facecolor=color_colleague,
                           linewidth=2)
ax.add_patch(colleagueC)
ax.text(3.9, 1.6, 'ColleagueC', fontsize=10, ha='center', weight='bold')
ax.text(3.9, 1.35, '(User)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(3.9, 1.1, 'mediator', fontsize=8, ha='center', family='monospace', color='#555')
ax.text(3.9, 0.85, 'send()', fontsize=9, ha='center', family='monospace')
ax.text(3.9, 0.6, 'receive()', fontsize=9, ha='center', family='monospace')

# ===== RELATIONSHIPS =====

# Mediator implements interface
arrow1 = FancyArrowPatch((7.0, 7.0), (7.0, 6.5),
                        arrowstyle='-|>', mutation_scale=20, 
                        color='#F77F00', linewidth=2, linestyle='dashed')
ax.add_patch(arrow1)
ax.text(7.4, 6.7, 'implements', fontsize=8, style='italic', color='#F77F00')

# Colleague implements interface
arrow2 = FancyArrowPatch((1.75, 2.5), (1.75, 1.8),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow2)

arrow3 = FancyArrowPatch((2.4, 2.5), (2.4, 1.8),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow3)

arrow4 = FancyArrowPatch((3.9, 2.5), (3.9, 1.8),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow4)

# Colleagues reference mediator
arrow5 = FancyArrowPatch((0.9, 1.8), (5.5, 5.5),
                        arrowstyle='->', mutation_scale=15, 
                        color='#666', linewidth=1.5)
ax.add_patch(arrow5)
ax.text(2.5, 3.8, 'uses', fontsize=8, style='italic', color='#666')

arrow6 = FancyArrowPatch((2.4, 1.8), (6.0, 4.5),
                        arrowstyle='->', mutation_scale=15, 
                        color='#666', linewidth=1.5)
ax.add_patch(arrow6)

arrow7 = FancyArrowPatch((3.9, 1.8), (6.5, 4.5),
                        arrowstyle='->', mutation_scale=15, 
                        color='#666', linewidth=1.5)
ax.add_patch(arrow7)

# Mediator knows about colleagues
arrow8 = FancyArrowPatch((6.0, 4.5), (1.5, 1.8),
                        arrowstyle='->', mutation_scale=12, 
                        color='#999', linewidth=1, linestyle='dotted')
ax.add_patch(arrow8)

arrow9 = FancyArrowPatch((7.0, 4.5), (2.7, 1.8),
                        arrowstyle='->', mutation_scale=12, 
                        color='#999', linewidth=1, linestyle='dotted')
ax.add_patch(arrow9)

arrow10 = FancyArrowPatch((8.0, 4.5), (4.0, 1.8),
                         arrowstyle='->', mutation_scale=12, 
                         color='#999', linewidth=1, linestyle='dotted')
ax.add_patch(arrow10)
ax.text(7.8, 3.5, 'coordinates', fontsize=8, style='italic', color='#999')

# ===== COMPARISON: WITHOUT MEDIATOR (BAD) =====
ax.text(10.5, 7.5, 'Without Mediator', fontsize=11, ha='center', weight='bold', color='#C41E3A')
ax.text(10.5, 7.2, '(Tight Coupling)', fontsize=9, ha='center', style='italic', color='#C41E3A')

# Create nodes for mesh
node_positions = [
    (9.5, 6.5), (10.5, 6.5), (11.5, 6.5),
    (9.5, 5.5), (10.5, 5.5), (11.5, 5.5)
]

for x, y in node_positions:
    circle = Circle((x, y), 0.2, facecolor='#FFB3B3', edgecolor='#C41E3A', linewidth=1.5)
    ax.add_patch(circle)

# Mesh of arrows (spaghetti!)
for i, (x1, y1) in enumerate(node_positions):
    for j, (x2, y2) in enumerate(node_positions):
        if i < j:
            arrow = FancyArrowPatch((x1, y1), (x2, y2),
                                  arrowstyle='<->', mutation_scale=8, 
                                  color='#C41E3A', linewidth=0.8, alpha=0.5)
            ax.add_patch(arrow)

ax.text(10.5, 4.8, 'N² connections! 😱', fontsize=9, ha='center', color='#C41E3A', weight='bold')

# ===== COMPARISON: WITH MEDIATOR (GOOD) =====
ax.text(10.5, 3.8, 'With Mediator', fontsize=11, ha='center', weight='bold', color='#2E7D32')
ax.text(10.5, 3.5, '(Loose Coupling)', fontsize=9, ha='center', style='italic', color='#2E7D32')

# Center mediator
center_circle = Circle((10.5, 2.5), 0.3, facecolor=color_mediator, edgecolor='#F77F00', linewidth=2)
ax.add_patch(center_circle)
ax.text(10.5, 2.5, 'M', fontsize=10, ha='center', weight='bold')

# Colleague nodes
colleague_positions = [
    (9.2, 3.2), (10.5, 3.5), (11.8, 3.2),
    (9.2, 1.8), (11.8, 1.8)
]

for x, y in colleague_positions:
    circle = Circle((x, y), 0.18, facecolor=color_colleague, edgecolor='#2E86AB', linewidth=1.5)
    ax.add_patch(circle)
    # Arrow to mediator
    arrow = FancyArrowPatch((x, y), (10.5, 2.5),
                          arrowstyle='->', mutation_scale=10, 
                          color='#2E7D32', linewidth=1.2)
    ax.add_patch(arrow)

ax.text(10.5, 1.2, 'N connections ✓', fontsize=9, ha='center', color='#2E7D32', weight='bold')

# ===== KEY BENEFITS =====
benefits_box = FancyBboxPatch((5.0, 0.1), 4.0, 0.8,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#666', facecolor='#FAFAFA',
                             linewidth=1)
ax.add_patch(benefits_box)
ax.text(7.0, 0.7, 'Key Benefits: Reduced coupling • Centralized logic • Easy testing • Simplified maintenance',
        fontsize=8, ha='center', style='italic', color='#666')
ax.text(7.0, 0.4, 'Use When: Many-to-many communication • Complex interactions • Need to add/remove components dynamically',
        fontsize=8, ha='center', style='italic', color='#666')

plt.tight_layout()
plt.savefig('docs/images/mediator_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Mediator Pattern diagram generated: docs/images/mediator_pattern.png")

