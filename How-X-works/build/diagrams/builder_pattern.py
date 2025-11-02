#!/usr/bin/env python3
# ./build/diagrams/builder_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(6, 9.5, 'Builder Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Client
client_box = FancyBboxPatch((0.5, 7.5), 2, 1.3, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#0ea5e9', 
                             facecolor='#e0f2fe', 
                             linewidth=2)
ax.add_patch(client_box)
ax.text(1.5, 8.5, 'Client', fontsize=12, fontweight='bold', ha='center')
ax.text(1.5, 8.1, 'builder', fontsize=9, ha='center', family='monospace')
ax.text(1.5, 7.85, '  .setProp1()', fontsize=8, ha='center', family='monospace')
ax.text(1.5, 7.6, '  .setProp2()', fontsize=8, ha='center', family='monospace')

# Builder
builder_box = FancyBboxPatch((3.5, 6.8), 2.5, 2.5, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#8b5cf6', 
                              facecolor='#f3e8ff', 
                              linewidth=2.5)
ax.add_patch(builder_box)
ax.text(4.75, 9, 'Builder', fontsize=13, fontweight='bold', ha='center', color='#8b5cf6')
ax.text(4.75, 8.6, 'setProp1(val)', fontsize=9, ha='center', family='monospace')
ax.text(4.75, 8.35, '  return this', fontsize=8, ha='center', family='monospace', style='italic')
ax.text(4.75, 8, 'setProp2(val)', fontsize=9, ha='center', family='monospace')
ax.text(4.75, 7.75, '  return this', fontsize=8, ha='center', family='monospace', style='italic')
ax.text(4.75, 7.4, 'setProp3(val)', fontsize=9, ha='center', family='monospace')
ax.text(4.75, 7.15, '  return this', fontsize=8, ha='center', family='monospace', style='italic')
ax.text(4.75, 6.9, 'build() → Product', fontsize=9, ha='center', family='monospace', fontweight='bold')

# Product
product_box = FancyBboxPatch((7.5, 7), 3, 2, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#10b981', 
                              facecolor='#d1fae5', 
                              linewidth=2)
ax.add_patch(product_box)
ax.text(9, 8.7, 'Product (Immutable)', fontsize=12, fontweight='bold', ha='center')
ax.text(9, 8.3, 'prop1: value1', fontsize=9, ha='center', family='monospace')
ax.text(9, 8, 'prop2: value2', fontsize=9, ha='center', family='monospace')
ax.text(9, 7.7, 'prop3: value3', fontsize=9, ha='center', family='monospace')
ax.text(9, 7.4, 'createdAt: Date', fontsize=9, ha='center', family='monospace')
ax.text(9, 7.1, 'Object.freeze()', fontsize=8, ha='center', style='italic', color='#059669')

# Arrow: Client uses Builder
arrow_client = FancyArrowPatch((2.5, 8.1), (3.5, 8.1), 
                                arrowstyle='->', mutation_scale=20, 
                                linewidth=2.5, color='#0ea5e9')
ax.add_patch(arrow_client)
ax.text(3, 8.4, 'uses', fontsize=9, ha='center', style='italic', color='#0ea5e9')

# Arrow: Builder creates Product
arrow_build = FancyArrowPatch((6, 7.5), (7.5, 7.5), 
                               arrowstyle='->', mutation_scale=20, 
                               linewidth=2.5, color='#8b5cf6')
ax.add_patch(arrow_build)
ax.text(6.75, 7.8, 'build()', fontsize=9, ha='center', 
        fontweight='bold', color='#8b5cf6')

# Chaining visualization
chain_box = FancyBboxPatch((0.5, 4.5), 5, 1.8, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='#f59e0b', 
                            facecolor='#fef3c7', 
                            linewidth=2, alpha=0.8)
ax.add_patch(chain_box)
ax.text(3, 6, 'Method Chaining (Fluent Interface)', 
        fontsize=11, fontweight='bold', ha='center', color='#f59e0b')
ax.text(3, 5.6, 'builder.setProp1("a")', fontsize=9, ha='center', family='monospace')
ax.text(3, 5.3, '       .setProp2("b")  ← returns this (builder)', 
        fontsize=8, ha='center', family='monospace')
ax.text(3, 5, '       .setProp3("c")  ← returns this (builder)', 
        fontsize=8, ha='center', family='monospace')
ax.text(3, 4.7, '       .build()       → returns new Product', 
        fontsize=8, ha='center', family='monospace', fontweight='bold')

# Comparison: Constructor vs Builder
compare_box = FancyBboxPatch((6.5, 4.5), 5, 1.8, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#6366f1', 
                              facecolor='#e0e7ff', 
                              linewidth=2, alpha=0.8)
ax.add_patch(compare_box)
ax.text(9, 6, 'Constructor vs Builder', 
        fontsize=11, fontweight='bold', ha='center', color='#6366f1')
ax.text(9, 5.6, '❌ new User(a, b, c, d, e, f)', 
        fontsize=8, ha='center', family='monospace', color='#dc2626')
ax.text(9, 5.35, '   (order matters, hard to read)', 
        fontsize=7, ha='center', style='italic', color='#dc2626')
ax.text(9, 5, '✓ new UserBuilder()', 
        fontsize=8, ha='center', family='monospace', color='#059669')
ax.text(9, 4.75, '    .setName(a).setEmail(b).build()', 
        fontsize=8, ha='center', family='monospace', color='#059669')

# Benefits
benefits_box = FancyBboxPatch((0.5, 1.2), 11, 2.8, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#10b981', 
                               facecolor='#d1fae5', 
                               linewidth=1.5, alpha=0.7)
ax.add_patch(benefits_box)
ax.text(6, 3.7, 'Builder Pattern Benefits', fontsize=12, fontweight='bold', ha='center', color='#059669')

benefits_text = [
    '✓ Readable: self-documenting construction',
    '✓ Flexible: optional parameters without null placeholders',
    '✓ Immutable products: mutable builder → immutable result',
    '✓ Validation: check validity at each step and before build()',
    '✓ Step-by-step: complex construction broken into manageable methods',
    '✓ Multiple representations: same builder, different outputs',
    '✓ Test-friendly: builders with defaults simplify test data creation'
]

y_pos = 3.3
for benefit in benefits_text:
    ax.text(6, y_pos, benefit, fontsize=8, ha='center')
    y_pos -= 0.3

# Example use case
ax.text(6, 0.7, 'Common Uses: Query builders, HTTP request builders, DOM builders, Configuration builders', 
        fontsize=9, ha='center', style='italic', 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef3c7', alpha=0.8))

ax.text(6, 0.3, 'Example: new QueryBuilder("users").select("name").where("age", ">", 18).limit(10).build()', 
        fontsize=8, ha='center', family='monospace', color='#6b7280')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Client'),
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Builder'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Product'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('docs/images/builder_pattern.png', dpi=300, bbox_inches='tight')
print("Builder Pattern diagram saved to docs/images/builder_pattern.png")

