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
ax.text(7, 9.5, 'Interpreter Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Define grammar representation and interpreter to process language sentences',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_context = '#FFF9E6'
color_expression = '#E8F4F8'
color_terminal = '#B8E6F0'
color_nonterminal = '#E8D4F8'

# ===== CONTEXT =====
context_box = FancyBboxPatch((0.5, 7.0), 2.5, 1.5,
                            boxstyle="round,pad=0.1", 
                            edgecolor='#F77F00', facecolor=color_context,
                            linewidth=2)
ax.add_patch(context_box)
ax.text(1.75, 8.25, 'Context', fontsize=12, ha='center', weight='bold')
ax.text(1.75, 8.0, '(Global state)', fontsize=9, ha='center', style='italic', color='#666')
ax.text(1.75, 7.65, 'variables: Map', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(1.75, 7.35, 'get(name)', fontsize=9, ha='center', family='monospace')
ax.text(1.75, 7.05, 'set(name, value)', fontsize=9, ha='center', family='monospace')

# ===== EXPRESSION INTERFACE =====
expression_interface = FancyBboxPatch((5.5, 7.0), 3.0, 1.5,
                                     boxstyle="round,pad=0.1", 
                                     edgecolor='#2E86AB', facecolor=color_expression,
                                     linewidth=2, linestyle='--')
ax.add_patch(expression_interface)
ax.text(7.0, 8.25, '«interface»', fontsize=9, ha='center', style='italic', color='#2E86AB')
ax.text(7.0, 8.0, 'Expression', fontsize=12, ha='center', weight='bold')
ax.text(7.0, 7.6, 'interpret(context)', fontsize=10, ha='center', family='monospace')
ax.text(7.0, 7.25, 'Grammar rule', fontsize=8, ha='center', style='italic', color='#555')

# ===== TERMINAL EXPRESSIONS =====
terminal_y = 4.8

# Number
terminal_num = FancyBboxPatch((0.5, terminal_y), 2.0, 1.3,
                             boxstyle="round,pad=0.1", 
                             edgecolor='#52B788', facecolor=color_terminal,
                             linewidth=2)
ax.add_patch(terminal_num)
ax.text(1.5, terminal_y + 1.05, 'NumberExpression', fontsize=9, ha='center', weight='bold')
ax.text(1.5, terminal_y + 0.8, 'value: number', fontsize=8, ha='center', family='monospace', color='#555')
ax.text(1.5, terminal_y + 0.55, 'interpret(ctx) {', fontsize=8, ha='center', family='monospace')
ax.text(1.65, terminal_y + 0.3, 'return this.value;', fontsize=7, ha='center', family='monospace', color='#52B788')
ax.text(1.5, terminal_y + 0.05, '}', fontsize=8, ha='center', family='monospace')

# Variable
terminal_var = FancyBboxPatch((3.0, terminal_y), 2.0, 1.3,
                             boxstyle="round,pad=0.1", 
                             edgecolor='#52B788', facecolor=color_terminal,
                             linewidth=2)
ax.add_patch(terminal_var)
ax.text(4.0, terminal_y + 1.05, 'VariableExpression', fontsize=9, ha='center', weight='bold')
ax.text(4.0, terminal_y + 0.8, 'name: string', fontsize=8, ha='center', family='monospace', color='#555')
ax.text(4.0, terminal_y + 0.55, 'interpret(ctx) {', fontsize=8, ha='center', family='monospace')
ax.text(4.15, terminal_y + 0.3, 'return ctx.get(name);', fontsize=7, ha='center', family='monospace', color='#52B788')
ax.text(4.0, terminal_y + 0.05, '}', fontsize=8, ha='center', family='monospace')

ax.text(3.0, terminal_y - 0.3, 'Terminal Expressions (Leaf nodes)', fontsize=10, ha='center', weight='bold', color='#52B788')

# ===== NON-TERMINAL EXPRESSIONS =====
nonterminal_y = 2.3

# Add
nonterminal_add = FancyBboxPatch((0.5, nonterminal_y), 2.3, 1.5,
                                boxstyle="round,pad=0.1", 
                                edgecolor='#9D4EDD', facecolor=color_nonterminal,
                                linewidth=2)
ax.add_patch(nonterminal_add)
ax.text(1.65, nonterminal_y + 1.25, 'AddExpression', fontsize=9, ha='center', weight='bold')
ax.text(1.65, nonterminal_y + 1.0, 'left: Expression', fontsize=8, ha='center', family='monospace', color='#555')
ax.text(1.65, nonterminal_y + 0.75, 'right: Expression', fontsize=8, ha='center', family='monospace', color='#555')
ax.text(1.65, nonterminal_y + 0.5, 'interpret(ctx) {', fontsize=8, ha='center', family='monospace')
ax.text(1.8, nonterminal_y + 0.25, 'return left.interpret(ctx)', fontsize=6, ha='center', family='monospace', color='#9D4EDD')
ax.text(1.8, nonterminal_y + 0.05, '+ right.interpret(ctx);', fontsize=6, ha='center', family='monospace', color='#9D4EDD')
ax.text(1.65, nonterminal_y - 0.15, '}', fontsize=8, ha='center', family='monospace')

# Multiply
nonterminal_mul = FancyBboxPatch((3.3, nonterminal_y), 2.3, 1.5,
                                boxstyle="round,pad=0.1", 
                                edgecolor='#9D4EDD', facecolor=color_nonterminal,
                                linewidth=2)
ax.add_patch(nonterminal_mul)
ax.text(4.45, nonterminal_y + 1.25, 'MultiplyExpression', fontsize=9, ha='center', weight='bold')
ax.text(4.45, nonterminal_y + 1.0, 'left: Expression', fontsize=8, ha='center', family='monospace', color='#555')
ax.text(4.45, nonterminal_y + 0.75, 'right: Expression', fontsize=8, ha='center', family='monospace', color='#555')
ax.text(4.45, nonterminal_y + 0.5, 'interpret(ctx) {', fontsize=8, ha='center', family='monospace')
ax.text(4.6, nonterminal_y + 0.25, 'return left.interpret(ctx)', fontsize=6, ha='center', family='monospace', color='#9D4EDD')
ax.text(4.6, nonterminal_y + 0.05, '* right.interpret(ctx);', fontsize=6, ha='center', family='monospace', color='#9D4EDD')
ax.text(4.45, nonterminal_y - 0.15, '}', fontsize=8, ha='center', family='monospace')

ax.text(3.0, nonterminal_y - 0.5, 'Non-Terminal Expressions (Composite nodes)', fontsize=10, ha='center', weight='bold', color='#9D4EDD')

# ===== RELATIONSHIPS =====

# Expression interface
arrow1 = FancyArrowPatch((1.5, 7.0), (1.5, 6.1),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((4.0, 7.0), (4.0, 6.1),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow2)

arrow3 = FancyArrowPatch((7.0, 7.0), (1.65, 3.8),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow3)

arrow4 = FancyArrowPatch((7.0, 7.0), (4.45, 3.8),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow4)

ax.text(6.0, 6.5, 'implements', fontsize=8, style='italic', color='#2E86AB')

# Context used by expressions
arrow5 = FancyArrowPatch((3.0, 7.75), (5.5, 7.75),
                        arrowstyle='->', mutation_scale=15, 
                        color='#F77F00', linewidth=1.5, linestyle='dotted')
ax.add_patch(arrow5)
ax.text(4.25, 8.0, 'uses', fontsize=8, style='italic', color='#F77F00')

# ===== AST EXAMPLE =====
ast_box = FancyBboxPatch((9.5, 5.5), 4.0, 3.0,
                        boxstyle="round,pad=0.1", 
                        edgecolor='#E63946', facecolor='#FFF5F5',
                        linewidth=2)
ax.add_patch(ast_box)
ax.text(11.5, 8.25, 'AST Example: (x + 5) * 2', fontsize=11, ha='center', weight='bold', color='#E63946')

# Tree visualization
# Root: Multiply
ax.text(11.5, 7.75, '*', fontsize=14, ha='center', weight='bold',
       bbox=dict(boxstyle='circle', facecolor=color_nonterminal, edgecolor='#9D4EDD', linewidth=1.5))

# Left: Add
ax.text(10.5, 7.05, '+', fontsize=12, ha='center', weight='bold',
       bbox=dict(boxstyle='circle', facecolor=color_nonterminal, edgecolor='#9D4EDD', linewidth=1.5))

# Right: 2
ax.text(12.5, 7.05, '2', fontsize=12, ha='center', weight='bold',
       bbox=dict(boxstyle='circle', facecolor=color_terminal, edgecolor='#52B788', linewidth=1.5))

# Left-Left: x
ax.text(10.0, 6.35, 'x', fontsize=11, ha='center', weight='bold',
       bbox=dict(boxstyle='circle', facecolor=color_terminal, edgecolor='#52B788', linewidth=1.5))

# Left-Right: 5
ax.text(11.0, 6.35, '5', fontsize=11, ha='center', weight='bold',
       bbox=dict(boxstyle='circle', facecolor=color_terminal, edgecolor='#52B788', linewidth=1.5))

# Tree edges
ax.plot([11.5, 10.5], [7.65, 7.15], 'k-', linewidth=1)
ax.plot([11.5, 12.5], [7.65, 7.15], 'k-', linewidth=1)
ax.plot([10.5, 10.0], [6.95, 6.45], 'k-', linewidth=1)
ax.plot([10.5, 11.0], [6.95, 6.45], 'k-', linewidth=1)

ax.text(9.7, 5.95, 'Evaluation:', fontsize=9, ha='left', weight='bold')
ax.text(9.7, 5.7, 'x = 10 → (10 + 5) * 2 = 30', fontsize=8, ha='left', family='monospace', color='#52B788')

# ===== USE CASES =====
uses_box = FancyBboxPatch((9.5, 0.1), 4.0, 5.0,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1)
ax.add_patch(uses_box)
ax.text(11.5, 4.95, 'Common Use Cases', fontsize=10, ha='center', weight='bold')

use_cases = [
    '• Expression evaluators',
    '• Rule engines',
    '• Query languages (SQL-like)',
    '• Configuration parsers',
    '• Template engines',
    '• CSS selectors',
    '• RegEx engines',
    '• Math expression parsers',
    '• Boolean logic evaluators',
    '• DSL interpreters',
    '• Command interpreters',
    '• Scripting languages'
]

y_pos = 4.6
for use_case in use_cases:
    ax.text(9.7, y_pos, use_case, fontsize=7, ha='left')
    y_pos -= 0.35

# ===== KEY POINTS =====
points_box = FancyBboxPatch((0.5, 0.1), 8.5, 1.5,
                           boxstyle="round,pad=0.05", 
                           edgecolor='#2E7D32', facecolor='#E8F5E9',
                           linewidth=1)
ax.add_patch(points_box)
ax.text(4.75, 1.45, 'Key Points', fontsize=10, ha='center', weight='bold', color='#2E7D32')

ax.text(0.7, 1.15, '✓ Grammar as classes', fontsize=8, ha='left', color='#2E7D32')
ax.text(0.7, 0.9, '✓ Recursive evaluation', fontsize=8, ha='left', color='#2E7D32')
ax.text(0.7, 0.65, '✓ Easy to extend grammar', fontsize=8, ha='left', color='#2E7D32')
ax.text(0.7, 0.4, '⚠ Can be slow for complex grammars', fontsize=8, ha='left', color='#C41E3A')

ax.text(3.5, 1.15, '✓ Type-safe operations', fontsize=8, ha='left', color='#2E7D32')
ax.text(3.5, 0.9, '✓ Composable expressions', fontsize=8, ha='left', color='#2E7D32')
ax.text(3.5, 0.65, '✓ Visitor Pattern compatible', fontsize=8, ha='left', color='#2E7D32')
ax.text(3.5, 0.4, '⚠ Many classes for complex grammar', fontsize=8, ha='left', color='#C41E3A')

ax.text(6.5, 1.15, 'When to use:', fontsize=8, ha='left', weight='bold')
ax.text(6.5, 0.9, '• Simple grammar', fontsize=7, ha='left')
ax.text(6.5, 0.7, '• Grammar rarely changes', fontsize=7, ha='left')
ax.text(6.5, 0.5, '• Performance not critical', fontsize=7, ha='left')
ax.text(6.5, 0.3, '• Need to eval expressions', fontsize=7, ha='left')

plt.tight_layout()
plt.savefig('docs/images/interpreter_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Interpreter Pattern diagram generated: docs/images/interpreter_pattern.png")

