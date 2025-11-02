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
ax.text(7, 9.5, 'Template Method Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Define algorithm skeleton in base class; let subclasses override specific steps',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_abstract = '#FFF3B0'
color_concrete = '#B8E6F0'

# ===== ABSTRACT CLASS =====
abstract_box = FancyBboxPatch((0.5, 5.0), 4.5, 3.0,
                             boxstyle="round,pad=0.1", 
                             edgecolor='#F77F00', facecolor=color_abstract,
                             linewidth=2.5)
ax.add_patch(abstract_box)
ax.text(2.75, 7.75, 'AbstractClass', fontsize=12, ha='center', weight='bold')
ax.text(2.75, 7.5, '(ReportGenerator)', fontsize=9, ha='center', style='italic', color='#666')

# Template method
ax.text(0.7, 7.15, 'templateMethod() {', fontsize=10, ha='left', family='monospace', weight='bold', color='#E63946')
ax.text(1.0, 6.9, 'this.step1();', fontsize=9, ha='left', family='monospace')
ax.text(1.0, 6.7, 'this.step2();  // abstract', fontsize=9, ha='left', family='monospace', color='#2E86AB')
ax.text(1.0, 6.5, 'this.step3();  // abstract', fontsize=9, ha='left', family='monospace', color='#2E86AB')
ax.text(1.0, 6.3, 'if (this.hook()) {', fontsize=9, ha='left', family='monospace')
ax.text(1.2, 6.1, 'this.step4();', fontsize=9, ha='left', family='monospace')
ax.text(1.0, 5.9, '}', fontsize=9, ha='left', family='monospace')
ax.text(0.7, 5.7, '}', fontsize=10, ha='left', family='monospace', weight='bold')

# Methods
ax.text(0.7, 5.4, 'step1() { }  // Common', fontsize=9, ha='left', family='monospace', color='#52B788')
ax.text(0.7, 5.2, 'step2() { }  // Abstract', fontsize=9, ha='left', family='monospace', color='#C41E3A')
ax.text(0.7, 5.0, 'step3() { }  // Abstract', fontsize=9, ha='left', family='monospace', color='#C41E3A')
ax.text(0.7, 4.8, 'hook() { return true; }  // Hook', fontsize=9, ha='left', family='monospace', color='#9D4EDD')
ax.text(0.7, 4.6, 'step4() { }  // Common', fontsize=9, ha='left', family='monospace', color='#52B788')

# ===== CONCRETE CLASS A =====
concreteA = FancyBboxPatch((6.5, 6.0), 3.0, 1.8,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#2E86AB', facecolor=color_concrete,
                          linewidth=2)
ax.add_patch(concreteA)
ax.text(8.0, 7.6, 'ConcreteClassA', fontsize=11, ha='center', weight='bold')
ax.text(8.0, 7.35, '(PDFReport)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(6.7, 7.0, 'step2() {', fontsize=9, ha='left', family='monospace')
ax.text(6.9, 6.8, '// PDF-specific', fontsize=8, ha='left', family='monospace', style='italic', color='#666')
ax.text(6.7, 6.6, '}', fontsize=9, ha='left', family='monospace')
ax.text(6.7, 6.35, 'step3() {', fontsize=9, ha='left', family='monospace')
ax.text(6.9, 6.15, '// PDF-specific', fontsize=8, ha='left', family='monospace', style='italic', color='#666')
ax.text(6.7, 5.95, '}', fontsize=9, ha='left', family='monospace')

# ===== CONCRETE CLASS B =====
concreteB = FancyBboxPatch((10.0, 6.0), 3.0, 1.8,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#2E86AB', facecolor=color_concrete,
                          linewidth=2)
ax.add_patch(concreteB)
ax.text(11.5, 7.6, 'ConcreteClassB', fontsize=11, ha='center', weight='bold')
ax.text(11.5, 7.35, '(HTMLReport)', fontsize=8, ha='center', style='italic', color='#666')
ax.text(10.2, 7.0, 'step2() {', fontsize=9, ha='left', family='monospace')
ax.text(10.4, 6.8, '// HTML-specific', fontsize=8, ha='left', family='monospace', style='italic', color='#666')
ax.text(10.2, 6.6, '}', fontsize=9, ha='left', family='monospace')
ax.text(10.2, 6.35, 'step3() {', fontsize=9, ha='left', family='monospace')
ax.text(10.4, 6.15, '// HTML-specific', fontsize=8, ha='left', family='monospace', style='italic', color='#666')
ax.text(10.2, 5.95, '}', fontsize=9, ha='left', family='monospace')

# ===== RELATIONSHIPS =====

# Inheritance
arrow1 = FancyArrowPatch((8.0, 6.0), (2.75, 8.0),
                        arrowstyle='-|>', mutation_scale=20, 
                        color='#2E86AB', linewidth=2, linestyle='dashed')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((11.5, 6.0), (2.75, 8.0),
                        arrowstyle='-|>', mutation_scale=20, 
                        color='#2E86AB', linewidth=2, linestyle='dashed')
ax.add_patch(arrow2)

ax.text(5.0, 7.2, 'extends', fontsize=9, style='italic', color='#2E86AB')

# ===== SEQUENCE DIAGRAM =====
seq_y = 4.5
ax.text(7, seq_y + 0.5, 'Execution Flow (Template Method)', fontsize=11, ha='center', weight='bold')

seq_box = FancyBboxPatch((0.5, seq_y - 1.8), 13, 2.0,
                        boxstyle="round,pad=0.05", 
                        edgecolor='#999', facecolor='#F9F9F9',
                        linewidth=1.5)
ax.add_patch(seq_box)

# Client calls template method
ax.text(0.7, seq_y + 0.1, '1.', fontsize=9, ha='left', weight='bold')
ax.text(1.0, seq_y + 0.1, 'Client calls', fontsize=8, ha='left')
ax.text(2.0, seq_y + 0.1, 'concreteA.templateMethod()', fontsize=8, ha='left', family='monospace', color='#E63946')

# Template method executes steps
ax.text(0.7, seq_y - 0.2, '2.', fontsize=9, ha='left', weight='bold')
ax.text(1.0, seq_y - 0.2, 'Template method calls', fontsize=8, ha='left')
ax.text(2.5, seq_y - 0.2, 'step1()', fontsize=8, ha='left', family='monospace', color='#52B788')
ax.text(3.2, seq_y - 0.2, '(common implementation in base class)', fontsize=7, ha='left', style='italic', color='#666')

ax.text(0.7, seq_y - 0.5, '3.', fontsize=9, ha='left', weight='bold')
ax.text(1.0, seq_y - 0.5, 'Template method calls', fontsize=8, ha='left')
ax.text(2.5, seq_y - 0.5, 'step2()', fontsize=8, ha='left', family='monospace', color='#2E86AB')
ax.text(3.2, seq_y - 0.5, '(overridden in ConcreteClassA)', fontsize=7, ha='left', style='italic', color='#666')

ax.text(0.7, seq_y - 0.8, '4.', fontsize=9, ha='left', weight='bold')
ax.text(1.0, seq_y - 0.8, 'Template method calls', fontsize=8, ha='left')
ax.text(2.5, seq_y - 0.8, 'step3()', fontsize=8, ha='left', family='monospace', color='#2E86AB')
ax.text(3.2, seq_y - 0.8, '(overridden in ConcreteClassA)', fontsize=7, ha='left', style='italic', color='#666')

ax.text(0.7, seq_y - 1.1, '5.', fontsize=9, ha='left', weight='bold')
ax.text(1.0, seq_y - 1.1, 'Template method calls', fontsize=8, ha='left')
ax.text(2.5, seq_y - 1.1, 'hook()', fontsize=8, ha='left', family='monospace', color='#9D4EDD')
ax.text(3.1, seq_y - 1.1, '(returns true)', fontsize=7, ha='left', style='italic', color='#666')

ax.text(0.7, seq_y - 1.4, '6.', fontsize=9, ha='left', weight='bold')
ax.text(1.0, seq_y - 1.4, 'Template method calls', fontsize=8, ha='left')
ax.text(2.5, seq_y - 1.4, 'step4()', fontsize=8, ha='left', family='monospace', color='#52B788')
ax.text(3.2, seq_y - 1.4, '(common implementation in base class)', fontsize=7, ha='left', style='italic', color='#666')

# ===== METHOD TYPES =====
types_box = FancyBboxPatch((0.5, 0.1), 4.5, 1.2,
                          boxstyle="round,pad=0.05", 
                          edgecolor='#666', facecolor='#FAFAFA',
                          linewidth=1)
ax.add_patch(types_box)
ax.text(2.75, 1.15, 'Method Types', fontsize=10, ha='center', weight='bold')

ax.text(0.7, 0.85, 'Template Method:', fontsize=8, ha='left', weight='bold', color='#E63946')
ax.text(1.8, 0.85, 'Defines algorithm skeleton (final)', fontsize=7, ha='left')

ax.text(0.7, 0.65, 'Abstract Methods:', fontsize=8, ha='left', weight='bold', color='#C41E3A')
ax.text(1.8, 0.65, 'Must be overridden by subclasses', fontsize=7, ha='left')

ax.text(0.7, 0.45, 'Hook Methods:', fontsize=8, ha='left', weight='bold', color='#9D4EDD')
ax.text(1.5, 0.45, 'Optional override; default behavior', fontsize=7, ha='left')

ax.text(0.7, 0.25, 'Common Methods:', fontsize=8, ha='left', weight='bold', color='#52B788')
ax.text(1.7, 0.25, 'Shared implementation in base class', fontsize=7, ha='left')

# ===== KEY BENEFITS =====
benefits_box = FancyBboxPatch((5.5, 0.1), 4.0, 1.2,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#2E7D32', facecolor='#E8F5E9',
                             linewidth=1)
ax.add_patch(benefits_box)
ax.text(7.5, 1.15, 'Key Benefits', fontsize=10, ha='center', weight='bold', color='#2E7D32')

ax.text(5.7, 0.9, '✓ Code reuse (common steps)', fontsize=8, ha='left', color='#2E7D32')
ax.text(5.7, 0.7, '✓ Guaranteed algorithm structure', fontsize=8, ha='left', color='#2E7D32')
ax.text(5.7, 0.5, '✓ Inversion of control', fontsize=8, ha='left', color='#2E7D32')
ax.text(5.7, 0.3, '✓ Easy to extend specific steps', fontsize=8, ha='left', color='#2E7D32')

# ===== HOLLYWOOD PRINCIPLE =====
hollywood_box = FancyBboxPatch((10.0, 0.1), 3.5, 1.2,
                              boxstyle="round,pad=0.05", 
                              edgecolor='#F77F00', facecolor='#FFF9E6',
                              linewidth=1.5)
ax.add_patch(hollywood_box)
ax.text(11.75, 1.15, 'Hollywood Principle', fontsize=10, ha='center', weight='bold', color='#F77F00')
ax.text(10.2, 0.85, '"Don\'t call us,', fontsize=9, ha='left', style='italic')
ax.text(10.4, 0.65, 'we\'ll call you"', fontsize=9, ha='left', style='italic')
ax.text(10.2, 0.4, 'Parent controls flow;', fontsize=7, ha='left', color='#666')
ax.text(10.2, 0.2, 'child provides implementations', fontsize=7, ha='left', color='#666')

plt.tight_layout()
plt.savefig('docs/images/template_method_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Template Method Pattern diagram generated: docs/images/template_method_pattern.png")

