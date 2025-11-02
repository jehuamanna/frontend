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
ax.text(7, 9.5, 'Observer Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'One-to-many dependency: when subject changes, all observers notified automatically',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_subject = '#FFF3B0'
color_observer = '#B8E6F0'
color_interface = '#E8F4F8'
color_concrete = '#D4E8D4'

# ===== SUBJECT INTERFACE =====
subject_interface = FancyBboxPatch((0.5, 6.5), 2.5, 1.8,
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#F77F00', facecolor=color_interface,
                                  linewidth=2, linestyle='--')
ax.add_patch(subject_interface)
ax.text(1.75, 8.0, '«interface»', fontsize=9, ha='center', style='italic', color='#F77F00')
ax.text(1.75, 7.7, 'Subject', fontsize=12, ha='center', weight='bold')
ax.text(1.75, 7.3, 'attach(observer)', fontsize=10, ha='center', family='monospace')
ax.text(1.75, 7.0, 'detach(observer)', fontsize=10, ha='center', family='monospace')
ax.text(1.75, 6.7, 'notify()', fontsize=10, ha='center', family='monospace')

# ===== CONCRETE SUBJECT =====
concrete_subject = FancyBboxPatch((0.5, 4.0), 2.5, 2.0,
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='#F77F00', facecolor=color_subject,
                                 linewidth=2.5)
ax.add_patch(concrete_subject)
ax.text(1.75, 5.7, 'ConcreteSubject', fontsize=12, ha='center', weight='bold')
ax.text(1.75, 5.4, '(WeatherStation)', fontsize=9, ha='center', style='italic', color='#666')
ax.text(1.75, 5.05, 'observers[]', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(1.75, 4.75, 'state', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(1.75, 4.45, 'getState()', fontsize=9, ha='center', family='monospace')
ax.text(1.75, 4.15, 'setState()', fontsize=9, ha='center', family='monospace')

# ===== OBSERVER INTERFACE =====
observer_interface = FancyBboxPatch((5.0, 6.5), 2.5, 1.8,
                                   boxstyle="round,pad=0.1", 
                                   edgecolor='#2E86AB', facecolor=color_interface,
                                   linewidth=2, linestyle='--')
ax.add_patch(observer_interface)
ax.text(6.25, 8.0, '«interface»', fontsize=9, ha='center', style='italic', color='#2E86AB')
ax.text(6.25, 7.7, 'Observer', fontsize=12, ha='center', weight='bold')
ax.text(6.25, 7.3, 'update(data)', fontsize=10, ha='center', family='monospace')
ax.text(6.25, 7.0, 'called by subject', fontsize=8, ha='center', style='italic', color='#555')

# ===== CONCRETE OBSERVER A =====
observerA = FancyBboxPatch((4.0, 4.0), 1.8, 1.6,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#2E86AB', facecolor=color_observer,
                          linewidth=2)
ax.add_patch(observerA)
ax.text(4.9, 5.4, 'ObserverA', fontsize=10, ha='center', weight='bold')
ax.text(4.9, 5.1, '(PhoneDisplay)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(4.9, 4.8, 'subject', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(4.9, 4.5, 'update(data)', fontsize=9, ha='center', family='monospace')
ax.text(4.9, 4.2, 'display()', fontsize=9, ha='center', family='monospace')

# ===== CONCRETE OBSERVER B =====
observerB = FancyBboxPatch((6.2, 4.0), 1.8, 1.6,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#2E86AB', facecolor=color_observer,
                          linewidth=2)
ax.add_patch(observerB)
ax.text(7.1, 5.4, 'ObserverB', fontsize=10, ha='center', weight='bold')
ax.text(7.1, 5.1, '(WebDisplay)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(7.1, 4.8, 'subject', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(7.1, 4.5, 'update(data)', fontsize=9, ha='center', family='monospace')
ax.text(7.1, 4.2, 'render()', fontsize=9, ha='center', family='monospace')

# ===== CONCRETE OBSERVER C =====
observerC = FancyBboxPatch((8.4, 4.0), 1.8, 1.6,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#2E86AB', facecolor=color_observer,
                          linewidth=2)
ax.add_patch(observerC)
ax.text(9.3, 5.4, 'ObserverC', fontsize=10, ha='center', weight='bold')
ax.text(9.3, 5.1, '(Logger)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(9.3, 4.8, 'subject', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(9.3, 4.5, 'update(data)', fontsize=9, ha='center', family='monospace')
ax.text(9.3, 4.2, 'log()', fontsize=9, ha='center', family='monospace')

# ===== RELATIONSHIPS =====

# Subject implements interface
arrow1 = FancyArrowPatch((1.75, 6.5), (1.75, 6.0),
                        arrowstyle='-|>', mutation_scale=20, 
                        color='#F77F00', linewidth=2, linestyle='dashed')
ax.add_patch(arrow1)
ax.text(2.15, 6.2, 'implements', fontsize=8, style='italic', color='#F77F00')

# Observer implements interface
arrow2 = FancyArrowPatch((4.9, 6.5), (4.9, 5.6),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow2)

arrow3 = FancyArrowPatch((7.1, 6.5), (7.1, 5.6),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow3)

arrow4 = FancyArrowPatch((9.3, 6.5), (9.3, 5.6),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow4)

# Subject notifies observers (one-to-many)
arrow5 = FancyArrowPatch((3.0, 5.0), (4.0, 4.9),
                        arrowstyle='->', mutation_scale=15, 
                        color='#E63946', linewidth=2)
ax.add_patch(arrow5)

arrow6 = FancyArrowPatch((3.0, 5.0), (6.2, 4.9),
                        arrowstyle='->', mutation_scale=15, 
                        color='#E63946', linewidth=2)
ax.add_patch(arrow6)

arrow7 = FancyArrowPatch((3.0, 5.0), (8.4, 4.9),
                        arrowstyle='->', mutation_scale=15, 
                        color='#E63946', linewidth=2)
ax.add_patch(arrow7)
ax.text(3.5, 5.3, 'notifies', fontsize=9, style='italic', color='#E63946', weight='bold')

# Observers reference subject (optional)
arrow8 = FancyArrowPatch((4.9, 4.0), (1.75, 4.8),
                        arrowstyle='->', mutation_scale=10, 
                        color='#999', linewidth=1, linestyle='dotted')
ax.add_patch(arrow8)

# ===== SEQUENCE DIAGRAM =====
seq_y = 2.5
ax.text(7, seq_y + 0.6, 'Notification Sequence', fontsize=11, ha='center', weight='bold')

seq_box = FancyBboxPatch((0.5, seq_y - 1.0), 9.5, 1.3,
                        boxstyle="round,pad=0.05", 
                        edgecolor='#999', facecolor='#F9F9F9',
                        linewidth=1)
ax.add_patch(seq_box)

ax.text(0.7, seq_y + 0.2, '1.', fontsize=10, ha='left', weight='bold')
ax.text(1.1, seq_y + 0.2, 'Subject state changes (setState())', fontsize=9, ha='left')

ax.text(0.7, seq_y - 0.1, '2.', fontsize=10, ha='left', weight='bold')
ax.text(1.1, seq_y - 0.1, 'Subject calls notify()', fontsize=9, ha='left')

ax.text(0.7, seq_y - 0.4, '3.', fontsize=10, ha='left', weight='bold')
ax.text(1.1, seq_y - 0.4, 'For each observer: observer.update(data)', fontsize=9, ha='left')

ax.text(0.7, seq_y - 0.7, '4.', fontsize=10, ha='left', weight='bold')
ax.text(1.1, seq_y - 0.7, 'Observers retrieve subject state and update themselves', fontsize=9, ha='left')

# ===== MODERN VARIATIONS =====
modern_box = FancyBboxPatch((10.5, 4.0), 3.0, 4.3,
                           boxstyle="round,pad=0.1", 
                           edgecolor='#9D4EDD', facecolor='#F8F0FF',
                           linewidth=2)
ax.add_patch(modern_box)
ax.text(12.0, 8.0, 'Modern Variations', fontsize=11, ha='center', weight='bold', color='#9D4EDD')

ax.text(10.7, 7.6, 'EventEmitter', fontsize=9, ha='left', weight='bold')
ax.text(10.7, 7.35, '.on(event, callback)', fontsize=8, ha='left', family='monospace', color='#555')
ax.text(10.7, 7.1, '.emit(event, data)', fontsize=8, ha='left', family='monospace', color='#555')

ax.text(10.7, 6.7, 'RxJS Observable', fontsize=9, ha='left', weight='bold')
ax.text(10.7, 6.45, 'observable.subscribe()', fontsize=8, ha='left', family='monospace', color='#555')
ax.text(10.7, 6.2, '.pipe(map, filter)', fontsize=8, ha='left', family='monospace', color='#555')

ax.text(10.7, 5.8, 'Vue Reactivity', fontsize=9, ha='left', weight='bold')
ax.text(10.7, 5.55, 'reactive({ count: 0 })', fontsize=8, ha='left', family='monospace', color='#555')
ax.text(10.7, 5.3, 'Watcher auto-runs', fontsize=8, ha='left', family='monospace', color='#555')

ax.text(10.7, 4.9, 'React State', fontsize=9, ha='left', weight='bold')
ax.text(10.7, 4.65, 'useState()', fontsize=8, ha='left', family='monospace', color='#555')
ax.text(10.7, 4.4, 'setState() notifies', fontsize=8, ha='left', family='monospace', color='#555')

# ===== KEY BENEFITS =====
benefits_box = FancyBboxPatch((0.5, 0.1), 6.0, 0.8,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#2E7D32', facecolor='#E8F5E9',
                             linewidth=1)
ax.add_patch(benefits_box)
ax.text(3.5, 0.7, 'Key Benefits', fontsize=10, ha='center', weight='bold', color='#2E7D32')
ax.text(0.7, 0.45, '✓ Loose coupling', fontsize=8, ha='left', color='#2E7D32')
ax.text(0.7, 0.25, '✓ Dynamic subscriptions', fontsize=8, ha='left', color='#2E7D32')
ax.text(2.3, 0.45, '✓ Broadcast communication', fontsize=8, ha='left', color='#2E7D32')
ax.text(2.3, 0.25, '✓ Event-driven architecture', fontsize=8, ha='left', color='#2E7D32')
ax.text(4.5, 0.45, '✓ Easy to extend', fontsize=8, ha='left', color='#2E7D32')
ax.text(4.5, 0.25, '✓ Foundation for reactive programming', fontsize=8, ha='left', color='#2E7D32')

# ===== TRADE-OFFS =====
tradeoffs_box = FancyBboxPatch((7.0, 0.1), 6.5, 0.8,
                              boxstyle="round,pad=0.05", 
                              edgecolor='#C41E3A', facecolor='#FFEBEE',
                              linewidth=1)
ax.add_patch(tradeoffs_box)
ax.text(10.25, 0.7, 'Trade-offs', fontsize=10, ha='center', weight='bold', color='#C41E3A')
ax.text(7.2, 0.45, '⚠ Update order unpredictable', fontsize=8, ha='left', color='#C41E3A')
ax.text(7.2, 0.25, '⚠ Memory leaks if not unsubscribed', fontsize=8, ha='left', color='#C41E3A')
ax.text(10.0, 0.45, '⚠ Debugging difficult (indirect calls)', fontsize=8, ha='left', color='#C41E3A')
ax.text(10.0, 0.25, '⚠ Performance if too many observers', fontsize=8, ha='left', color='#C41E3A')

plt.tight_layout()
plt.savefig('docs/images/observer_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Observer Pattern diagram generated: docs/images/observer_pattern.png")

