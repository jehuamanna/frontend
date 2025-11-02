#!/usr/bin/env python3
# ./build/diagrams/dependency_injection_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(8, 9.5, 'Dependency Injection Pattern', 
        fontsize=20, weight='bold', ha='center')
ax.text(8, 9.0, 'Inversion of Control: Dependencies Provided, Not Created',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= WITHOUT DI (Tight Coupling) =============
ax.text(3, 8.2, 'Without DI (Tight Coupling):', fontsize=11, weight='bold', color='#dc2626')

tight_component = FancyBboxPatch((0.5, 6.3), 5, 1.5,
                                  boxstyle="round,pad=0.1",
                                  edgecolor='#dc2626', facecolor='#fee2e2', linewidth=2)
ax.add_patch(tight_component)
ax.text(3, 7.5, 'Component', fontsize=11, weight='bold', ha='center')
ax.text(3, 7.1, 'constructor() {', fontsize=8, ha='center', family='monospace')
ax.text(3, 6.85, '  this.service = new Service();', fontsize=8, ha='center', family='monospace', color='#dc2626', weight='bold')
ax.text(3, 6.6, '}', fontsize=8, ha='center', family='monospace')

tight_service = FancyBboxPatch((1.5, 4.5), 3, 1,
                                boxstyle="round,pad=0.1",
                                edgecolor='#dc2626', facecolor='#fecaca', linewidth=1.5)
ax.add_patch(tight_service)
ax.text(3, 5.2, 'Service', fontsize=10, weight='bold', ha='center')
ax.text(3, 4.8, 'created internally', fontsize=7, ha='center', style='italic', color='#7f1d1d')

arrow_tight = FancyArrowPatch((3, 6.3), (3, 5.5),
                              arrowstyle='->', mutation_scale=20,
                              linewidth=2, color='#dc2626')
ax.add_patch(arrow_tight)
ax.text(3.5, 5.9, 'creates', fontsize=8, ha='left', style='italic', color='#dc2626')

ax.text(3, 4, '❌ Hard to test', fontsize=8, ha='center', color='#991b1b')
ax.text(3, 3.7, '❌ Tight coupling', fontsize=8, ha='center', color='#991b1b')

# ============= WITH DI (Loose Coupling) =============
ax.text(11, 8.2, 'With DI (Loose Coupling):', fontsize=11, weight='bold', color='#059669')

# Injector/Container
injector_box = FancyBboxPatch((9, 5.5), 6, 1.8,
                               boxstyle="round,pad=0.1",
                               edgecolor='#3b82f6', facecolor='#dbeafe', linewidth=2.5)
ax.add_patch(injector_box)
ax.text(12, 7, 'DI Container / Injector', fontsize=11, weight='bold', ha='center', color='#1e40af')
ax.text(12, 6.65, 'register(Service)', fontsize=8, ha='center', family='monospace')
ax.text(12, 6.35, 'inject(Component)', fontsize=8, ha='center', family='monospace')
ax.text(12, 6.05, 'resolve dependencies', fontsize=8, ha='center', family='monospace')
ax.text(12, 5.75, 'wire connections', fontsize=8, ha='center', family='monospace')

# Component (loose)
loose_component = FancyBboxPatch((7.5, 2.5), 4, 1.5,
                                  boxstyle="round,pad=0.1",
                                  edgecolor='#059669', facecolor='#d1fae5', linewidth=2)
ax.add_patch(loose_component)
ax.text(9.5, 3.7, 'Component', fontsize=11, weight='bold', ha='center')
ax.text(9.5, 3.3, 'constructor(service) {', fontsize=8, ha='center', family='monospace')
ax.text(9.5, 3.05, '  this.service = service;', fontsize=8, ha='center', family='monospace', color='#059669', weight='bold')
ax.text(9.5, 2.8, '}', fontsize=8, ha='center', family='monospace')

# Service
loose_service = FancyBboxPatch((13, 2.5), 2.5, 1.5,
                                boxstyle="round,pad=0.1",
                                edgecolor='#9333ea', facecolor='#f3e8ff', linewidth=1.5)
ax.add_patch(loose_service)
ax.text(14.25, 3.5, 'Service', fontsize=10, weight='bold', ha='center')
ax.text(14.25, 3.15, 'fetch()', fontsize=8, ha='center', family='monospace')
ax.text(14.25, 2.85, 'save()', fontsize=8, ha='center', family='monospace')

# Arrows
arrow_inject1 = FancyArrowPatch((10.5, 5.5), (9.5, 4),
                                arrowstyle='->', mutation_scale=20,
                                linewidth=2, color='#3b82f6')
ax.add_patch(arrow_inject1)
ax.text(9.8, 4.7, 'injects', fontsize=8, ha='left', style='italic', color='#1e40af')

arrow_inject2 = FancyArrowPatch((13, 5.5), (14.25, 4),
                                arrowstyle='->', mutation_scale=20,
                                linewidth=2, color='#3b82f6')
ax.add_patch(arrow_inject2)

arrow_uses = FancyArrowPatch((11.5, 3.25), (13, 3.25),
                             arrowstyle='->', mutation_scale=15,
                             linewidth=1.5, color='#059669', linestyle='dashed')
ax.add_patch(arrow_uses)
ax.text(12.25, 3.5, 'uses', fontsize=7, ha='center', style='italic', color='#059669')

ax.text(9.5, 2.1, '✅ Easy to test (mock service)', fontsize=8, ha='center', color='#047857')
ax.text(9.5, 1.8, '✅ Loose coupling', fontsize=8, ha='center', color='#047857')
ax.text(9.5, 1.5, '✅ Flexible & maintainable', fontsize=8, ha='center', color='#047857')

# ============= DI Types =============
ax.text(1, 2.5, 'DI Types:', fontsize=10, weight='bold')

types_box = FancyBboxPatch((0.5, 0.1), 6, 2.2,
                            boxstyle="round,pad=0.1",
                            edgecolor='#6366f1', facecolor='#eef2ff', linewidth=1.5)
ax.add_patch(types_box)

di_types = """1. Constructor Injection (most common)
   constructor(service) { ... }

2. Property/Setter Injection
   component.service = service;

3. Method Injection
   component.doWork(service);

4. Interface Injection
   component.injectService(service);"""

ax.text(0.7, 2.1, di_types, fontsize=7, ha='left', va='top', family='monospace')

# ============= Benefits Box =============
benefits_box = FancyBboxPatch((7, 0.1), 8.5, 1.2,
                              boxstyle="round,pad=0.1",
                              edgecolor='#10b981', facecolor='#d1fae5', linewidth=1.5)
ax.add_patch(benefits_box)
ax.text(11.25, 1.1, 'Benefits:', fontsize=10, weight='bold', ha='center', color='#047857')

benefits = """✓ Testability: Easy to inject mocks/stubs  •  ✓ Flexibility: Swap implementations
✓ Decoupling: Components don't create dependencies  •  ✓ Reusability: Share services
✓ Maintainability: Change one place  •  ✓ Lifecycle Control: Container manages lifecycles"""

ax.text(7.2, 0.85, benefits, fontsize=7, ha='left', va='top')

# Example annotation
ax.text(11.25, 0.35, 'Example: Angular DI, React Context, InversifyJS, TSyringe', 
        fontsize=7, ha='center', style='italic', color='#6b7280')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#dbeafe', edgecolor='#3b82f6', label='DI Container'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#059669', label='Component (Consumer)'),
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#9333ea', label='Service (Dependency)'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=9, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/dependency_injection_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Dependency Injection Pattern diagram generated successfully")

