import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Strategy Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Encapsulate algorithms and make them interchangeable at runtime',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_context = '#FFE5CC'
color_strategy = '#E8F4F8'
color_concrete = '#B8E6F0'

# ===== CONTEXT =====
context_box = FancyBboxPatch((0.5, 5.5), 3.0, 2.0,
                            boxstyle="round,pad=0.1", 
                            edgecolor='#E63946', facecolor=color_context,
                            linewidth=2.5)
ax.add_patch(context_box)
ax.text(2.0, 7.2, 'Context', fontsize=12, ha='center', weight='bold')
ax.text(2.0, 6.9, '(Sorter / Validator)', fontsize=9, ha='center', style='italic', color='#666')
ax.text(2.0, 6.55, 'strategy: Strategy', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(2.0, 6.25, 'setStrategy(s)', fontsize=10, ha='center', family='monospace')
ax.text(2.0, 5.95, 'execute()', fontsize=10, ha='center', family='monospace')
ax.text(2.0, 5.65, '→ strategy.algorithm()', fontsize=9, ha='center', style='italic', color='#E63946')

# ===== STRATEGY INTERFACE =====
strategy_interface = FancyBboxPatch((5.5, 6.0), 3.0, 1.5,
                                   boxstyle="round,pad=0.1", 
                                   edgecolor='#2E86AB', facecolor=color_strategy,
                                   linewidth=2, linestyle='--')
ax.add_patch(strategy_interface)
ax.text(7.0, 7.25, '«interface»', fontsize=9, ha='center', style='italic', color='#2E86AB')
ax.text(7.0, 7.0, 'Strategy', fontsize=12, ha='center', weight='bold')
ax.text(7.0, 6.65, 'algorithm(data)', fontsize=10, ha='center', family='monospace')
ax.text(7.0, 6.35, 'Algorithm interface', fontsize=8, ha='center', style='italic', color='#555')

# ===== CONCRETE STRATEGY A =====
strategyA = FancyBboxPatch((10.0, 6.5), 2.2, 1.3,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#2E86AB', facecolor=color_concrete,
                          linewidth=2)
ax.add_patch(strategyA)
ax.text(11.1, 7.6, 'ConcreteStrategyA', fontsize=10, ha='center', weight='bold')
ax.text(11.1, 7.35, '(BubbleSort)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(11.1, 7.05, 'algorithm()', fontsize=9, ha='center', family='monospace')
ax.text(11.1, 6.75, '// Implementation A', fontsize=7, ha='center', style='italic', color='#555')

# ===== CONCRETE STRATEGY B =====
strategyB = FancyBboxPatch((10.0, 4.8), 2.2, 1.3,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#2E86AB', facecolor=color_concrete,
                          linewidth=2)
ax.add_patch(strategyB)
ax.text(11.1, 5.9, 'ConcreteStrategyB', fontsize=10, ha='center', weight='bold')
ax.text(11.1, 5.65, '(QuickSort)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(11.1, 5.35, 'algorithm()', fontsize=9, ha='center', family='monospace')
ax.text(11.1, 5.05, '// Implementation B', fontsize=7, ha='center', style='italic', color='#555')

# ===== CONCRETE STRATEGY C =====
strategyC = FancyBboxPatch((10.0, 3.1), 2.2, 1.3,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#2E86AB', facecolor=color_concrete,
                          linewidth=2)
ax.add_patch(strategyC)
ax.text(11.1, 4.2, 'ConcreteStrategyC', fontsize=10, ha='center', weight='bold')
ax.text(11.1, 3.95, '(MergeSort)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(11.1, 3.65, 'algorithm()', fontsize=9, ha='center', family='monospace')
ax.text(11.1, 3.35, '// Implementation C', fontsize=7, ha='center', style='italic', color='#555')

# ===== RELATIONSHIPS =====

# Context holds Strategy
arrow1 = FancyArrowPatch((3.5, 6.5), (5.5, 6.75),
                        arrowstyle='->', mutation_scale=20, 
                        color='#E63946', linewidth=2)
ax.add_patch(arrow1)
ax.text(4.5, 6.9, 'uses', fontsize=9, style='italic', color='#E63946')

# Strategies implement interface
arrow2 = FancyArrowPatch((10.0, 7.1), (8.5, 6.9),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow2)

arrow3 = FancyArrowPatch((10.0, 5.4), (8.5, 6.5),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow3)

arrow4 = FancyArrowPatch((10.0, 3.7), (8.5, 6.2),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow4)

ax.text(9.2, 6.6, 'implement', fontsize=8, style='italic', color='#2E86AB')

# Context delegates
arrow_delegate = FancyArrowPatch((3.5, 6.0), (5.5, 6.3),
                               arrowstyle='->', mutation_scale=12, 
                               color='#999', linewidth=1.5, linestyle='dotted')
ax.add_patch(arrow_delegate)
ax.text(4.5, 6.0, 'delegates', fontsize=8, style='italic', color='#999')

# ===== USAGE EXAMPLE =====
usage_box = FancyBboxPatch((0.5, 3.0), 4.5, 2.0,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#52B788', facecolor='#E8F5E9',
                          linewidth=1.5)
ax.add_patch(usage_box)
ax.text(2.75, 4.8, 'Usage Example', fontsize=11, ha='center', weight='bold', color='#52B788')

ax.text(0.7, 4.45, 'const sorter = new Sorter(', fontsize=8, ha='left', family='monospace')
ax.text(0.9, 4.2, 'new BubbleSortStrategy()', fontsize=8, ha='left', family='monospace', color='#2E86AB')
ax.text(0.7, 3.95, ');', fontsize=8, ha='left', family='monospace')

ax.text(0.7, 3.6, 'sorter.sort(data);', fontsize=8, ha='left', family='monospace', color='#E63946')

ax.text(0.7, 3.3, '// Switch strategy', fontsize=8, ha='left', family='monospace', style='italic', color='#666')
ax.text(0.7, 3.1, 'sorter.setStrategy(', fontsize=8, ha='left', family='monospace')
ax.text(0.9, 2.85, 'new QuickSortStrategy()', fontsize=8, ha='left', family='monospace', color='#2E86AB')
ax.text(0.7, 2.6, ');', fontsize=8, ha='left', family='monospace')

# ===== STRATEGY VS STATE =====
comp_box = FancyBboxPatch((5.5, 3.0), 4.0, 2.0,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#9D4EDD', facecolor='#F8F0FF',
                         linewidth=1.5)
ax.add_patch(comp_box)
ax.text(7.5, 4.8, 'Strategy vs. State', fontsize=11, ha='center', weight='bold', color='#9D4EDD')

ax.text(5.7, 4.45, 'Strategy:', fontsize=9, ha='left', weight='bold', color='#2E86AB')
ax.text(5.9, 4.2, '• Algorithms are interchangeable', fontsize=8, ha='left')
ax.text(5.9, 3.95, '• Client chooses strategy', fontsize=8, ha='left')
ax.text(5.9, 3.7, '• Context doesn\'t know concrete', fontsize=8, ha='left')

ax.text(5.7, 3.4, 'State:', fontsize=9, ha='left', weight='bold', color='#E63946')
ax.text(5.9, 3.15, '• Behavior changes with state', fontsize=8, ha='left')
ax.text(5.9, 2.9, '• States transition themselves', fontsize=8, ha='left')
ax.text(5.9, 2.65, '• Context knows current state', fontsize=8, ha='left')

# ===== REAL WORLD EXAMPLES =====
examples_box = FancyBboxPatch((10.0, 0.5), 3.5, 2.5,
                             boxstyle="round,pad=0.1", 
                             edgecolor='#F77F00', facecolor='#FFF9E6',
                             linewidth=1.5)
ax.add_patch(examples_box)
ax.text(11.75, 2.8, 'Real-World Examples', fontsize=10, ha='center', weight='bold', color='#F77F00')

examples = [
    '• Sorting algorithms',
    '• Payment methods',
    '• Validation rules',
    '• Compression algorithms',
    '• Rendering strategies',
    '• Route finding (A*, Dijkstra)',
    '• Pricing strategies',
    '• Export formats (PDF, CSV)'
]

y_pos = 2.4
for example in examples:
    ax.text(10.2, y_pos, example, fontsize=7, ha='left')
    y_pos -= 0.25

# ===== KEY BENEFITS =====
benefits_box = FancyBboxPatch((0.5, 0.5), 4.0, 2.0,
                             boxstyle="round,pad=0.1", 
                             edgecolor='#2E7D32', facecolor='#E8F5E9',
                             linewidth=1.5)
ax.add_patch(benefits_box)
ax.text(2.5, 2.3, 'Key Benefits', fontsize=10, ha='center', weight='bold', color='#2E7D32')

benefits = [
    '✓ Eliminate conditionals',
    '✓ Algorithms interchangeable',
    '✓ Easy to extend',
    '✓ Runtime flexibility',
    '✓ Algorithms testable in isolation',
    '✓ Follows Open/Closed Principle'
]

y_pos = 1.95
for benefit in benefits:
    ax.text(0.7, y_pos, benefit, fontsize=8, ha='left', color='#2E7D32')
    y_pos -= 0.23

# ===== WHEN TO USE =====
when_box = FancyBboxPatch((5.0, 0.5), 4.5, 2.0,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1)
ax.add_patch(when_box)
ax.text(7.25, 2.3, 'When to Use', fontsize=10, ha='center', weight='bold')

ax.text(5.2, 1.95, '✓ Multiple algorithms for same task', fontsize=7, ha='left')
ax.text(5.2, 1.75, '✓ Need to switch algorithms at runtime', fontsize=7, ha='left')
ax.text(5.2, 1.55, '✓ Complex conditionals for algorithm selection', fontsize=7, ha='left')
ax.text(5.2, 1.35, '✓ Want to add algorithms without modifying context', fontsize=7, ha='left')

ax.text(5.2, 1.05, '⚠ When NOT to use:', fontsize=7, ha='left', weight='bold', color='#C41E3A')
ax.text(5.2, 0.85, '• Only one algorithm', fontsize=7, ha='left', color='#C41E3A')
ax.text(5.2, 0.65, '• Algorithm rarely changes', fontsize=7, ha='left', color='#C41E3A')

plt.tight_layout()
plt.savefig('docs/images/strategy_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Strategy Pattern diagram generated: docs/images/strategy_pattern.png")

