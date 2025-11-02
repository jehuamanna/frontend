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
ax.text(7, 9.5, 'Visitor Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Represent operations on object structure; add operations without changing elements',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_visitor = '#FFE5CC'
color_element = '#B8E6F0'
color_interface = '#E8F4F8'

# ===== VISITOR INTERFACE =====
visitor_interface = FancyBboxPatch((0.5, 6.5), 3.0, 1.8,
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#E63946', facecolor=color_interface,
                                  linewidth=2, linestyle='--')
ax.add_patch(visitor_interface)
ax.text(2.0, 8.05, '«interface»', fontsize=9, ha='center', style='italic', color='#E63946')
ax.text(2.0, 7.8, 'Visitor', fontsize=12, ha='center', weight='bold')
ax.text(2.0, 7.4, 'visitElementA(a)', fontsize=9, ha='center', family='monospace')
ax.text(2.0, 7.1, 'visitElementB(b)', fontsize=9, ha='center', family='monospace')
ax.text(2.0, 6.8, 'visitElementC(c)', fontsize=9, ha='center', family='monospace')

# ===== CONCRETE VISITOR 1 =====
visitor1 = FancyBboxPatch((0.5, 4.3), 2.5, 1.5,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#E63946', facecolor=color_visitor,
                         linewidth=2)
ax.add_patch(visitor1)
ax.text(1.75, 5.55, 'ConcreteVisitor1', fontsize=10, ha='center', weight='bold')
ax.text(1.75, 5.3, '(AreaCalculator)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(1.75, 5.0, 'visitElementA()', fontsize=8, ha='center', family='monospace')
ax.text(1.75, 4.75, 'visitElementB()', fontsize=8, ha='center', family='monospace')
ax.text(1.75, 4.5, 'visitElementC()', fontsize=8, ha='center', family='monospace')

# ===== CONCRETE VISITOR 2 =====
visitor2 = FancyBboxPatch((10.5, 4.3), 2.5, 1.5,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#E63946', facecolor=color_visitor,
                         linewidth=2)
ax.add_patch(visitor2)
ax.text(11.75, 5.55, 'ConcreteVisitor2', fontsize=10, ha='center', weight='bold')
ax.text(11.75, 5.3, '(ShapeDrawer)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(11.75, 5.0, 'visitElementA()', fontsize=8, ha='center', family='monospace')
ax.text(11.75, 4.75, 'visitElementB()', fontsize=8, ha='center', family='monospace')
ax.text(11.75, 4.5, 'visitElementC()', fontsize=8, ha='center', family='monospace')

# ===== ELEMENT INTERFACE =====
element_interface = FancyBboxPatch((5.5, 6.5), 3.0, 1.8,
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#2E86AB', facecolor=color_interface,
                                  linewidth=2, linestyle='--')
ax.add_patch(element_interface)
ax.text(7.0, 8.05, '«interface»', fontsize=9, ha='center', style='italic', color='#2E86AB')
ax.text(7.0, 7.8, 'Element', fontsize=12, ha='center', weight='bold')
ax.text(7.0, 7.4, 'accept(visitor)', fontsize=10, ha='center', family='monospace')
ax.text(7.0, 7.0, '→ visitor.visit(this)', fontsize=8, ha='center', style='italic', color='#2E86AB')

# ===== CONCRETE ELEMENTS =====
elementA = FancyBboxPatch((4.5, 4.3), 2.0, 1.5,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#2E86AB', facecolor=color_element,
                         linewidth=2)
ax.add_patch(elementA)
ax.text(5.5, 5.55, 'ElementA', fontsize=10, ha='center', weight='bold')
ax.text(5.5, 5.3, '(Circle)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(5.5, 5.0, 'accept(visitor) {', fontsize=8, ha='center', family='monospace')
ax.text(5.7, 4.75, 'visitor.visitA(this);', fontsize=7, ha='center', family='monospace', color='#E63946')
ax.text(5.5, 4.5, '}', fontsize=8, ha='center', family='monospace')

elementB = FancyBboxPatch((7.0, 4.3), 2.0, 1.5,
                         boxstyle="round,pad=0.1", 
                         edgecolor='#2E86AB', facecolor=color_element,
                         linewidth=2)
ax.add_patch(elementB)
ax.text(8.0, 5.55, 'ElementB', fontsize=10, ha='center', weight='bold')
ax.text(8.0, 5.3, '(Rectangle)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(8.0, 5.0, 'accept(visitor) {', fontsize=8, ha='center', family='monospace')
ax.text(8.2, 4.75, 'visitor.visitB(this);', fontsize=7, ha='center', family='monospace', color='#E63946')
ax.text(8.0, 4.5, '}', fontsize=8, ha='center', family='monospace')

# ===== RELATIONSHIPS =====

# Visitor implements interface
arrow1 = FancyArrowPatch((1.75, 6.5), (1.75, 5.8),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#E63946', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((11.75, 6.5), (2.0, 8.0),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#E63946', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow2)

# Element implements interface
arrow3 = FancyArrowPatch((5.5, 6.5), (5.5, 5.8),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow3)

arrow4 = FancyArrowPatch((8.0, 6.5), (8.0, 5.8),
                        arrowstyle='-|>', mutation_scale=15, 
                        color='#2E86AB', linewidth=1.5, linestyle='dashed')
ax.add_patch(arrow4)

# Element accepts Visitor
arrow5 = FancyArrowPatch((5.5, 4.9), (3.5, 5.0),
                        arrowstyle='->', mutation_scale=15, 
                        color='#F77F00', linewidth=2)
ax.add_patch(arrow5)
ax.text(4.5, 5.3, 'calls', fontsize=8, style='italic', color='#F77F00')

arrow6 = FancyArrowPatch((9.0, 4.9), (10.5, 5.0),
                        arrowstyle='->', mutation_scale=15, 
                        color='#F77F00', linewidth=2)
ax.add_patch(arrow6)
ax.text(9.7, 5.3, 'calls', fontsize=8, style='italic', color='#F77F00')

# ===== DOUBLE DISPATCH =====
dd_box = FancyBboxPatch((0.5, 2.0), 4.5, 1.8,
                       boxstyle="round,pad=0.1", 
                       edgecolor='#9D4EDD', facecolor='#F8F0FF',
                       linewidth=2)
ax.add_patch(dd_box)
ax.text(2.75, 3.6, 'Double Dispatch', fontsize=11, ha='center', weight='bold', color='#9D4EDD')

ax.text(0.7, 3.25, '1. element.accept(visitor)', fontsize=8, ha='left', family='monospace')
ax.text(0.9, 3.0, '→ element knows its type', fontsize=7, ha='left', style='italic', color='#666')

ax.text(0.7, 2.7, '2. visitor.visitElement(this)', fontsize=8, ha='left', family='monospace', color='#E63946')
ax.text(0.9, 2.45, '→ visitor knows element type', fontsize=7, ha='left', style='italic', color='#666')

ax.text(0.7, 2.15, 'Result: Type-safe operation', fontsize=8, ha='left', weight='bold', color='#9D4EDD')

# ===== USAGE EXAMPLE =====
usage_box = FancyBboxPatch((5.5, 2.0), 4.0, 1.8,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#52B788', facecolor='#E8F5E9',
                          linewidth=1.5)
ax.add_patch(usage_box)
ax.text(7.5, 3.6, 'Usage', fontsize=11, ha='center', weight='bold', color='#52B788')

ax.text(5.7, 3.25, 'const shapes = [', fontsize=8, ha='left', family='monospace')
ax.text(5.9, 3.0, 'new Circle(), new Rectangle()', fontsize=8, ha='left', family='monospace')
ax.text(5.7, 2.75, '];', fontsize=8, ha='left', family='monospace')

ax.text(5.7, 2.45, 'const visitor = new AreaCalc();', fontsize=8, ha='left', family='monospace', color='#E63946')
ax.text(5.7, 2.2, 'shapes.forEach(s => s.accept(visitor));', fontsize=8, ha='left', family='monospace', color='#2E86AB')

# ===== KEY BENEFITS =====
benefits_box = FancyBboxPatch((10.0, 2.0), 3.5, 1.8,
                             boxstyle="round,pad=0.1", 
                             edgecolor='#2E7D32', facecolor='#E8F5E9',
                             linewidth=1.5)
ax.add_patch(benefits_box)
ax.text(11.75, 3.6, 'Key Benefits', fontsize=10, ha='center', weight='bold', color='#2E7D32')

ax.text(10.2, 3.3, '✓ Easy to add operations', fontsize=8, ha='left', color='#2E7D32')
ax.text(10.2, 3.05, '✓ Separate concerns', fontsize=8, ha='left', color='#2E7D32')
ax.text(10.2, 2.8, '✓ Type-safe operations', fontsize=8, ha='left', color='#2E7D32')
ax.text(10.2, 2.55, '✓ Accumulate state', fontsize=8, ha='left', color='#2E7D32')
ax.text(10.2, 2.3, '✗ Hard to add element types', fontsize=8, ha='left', color='#C41E3A')

# ===== WHEN TO USE =====
when_box = FancyBboxPatch((0.5, 0.1), 13, 1.5,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1)
ax.add_patch(when_box)
ax.text(7, 1.45, 'When to Use: Stable element types, many operations | When NOT: Element types change frequently', 
        fontsize=8, ha='center', style='italic', color='#666')

ax.text(0.7, 1.15, 'Use Cases:', fontsize=9, ha='left', weight='bold')
ax.text(0.7, 0.9, '• Compiler ASTs (parse, interpret, optimize, generate)', fontsize=7, ha='left')
ax.text(0.7, 0.7, '• Document structures (export PDF, HTML, JSON)', fontsize=7, ha='left')
ax.text(0.7, 0.5, '• Graphics hierarchies (render, calculate bounds, serialize)', fontsize=7, ha='left')
ax.text(0.7, 0.3, '• DOM trees (count nodes, collect classes, validate)', fontsize=7, ha='left')

plt.tight_layout()
plt.savefig('docs/images/visitor_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Visitor Pattern diagram generated: docs/images/visitor_pattern.png")

