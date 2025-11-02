#!/usr/bin/env python3
# ./build/diagrams/adapter_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Adapter Pattern Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# Client
client_box = FancyBboxPatch((0.5, 6.5), 2.5, 1.5, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#0ea5e9', 
                             facecolor='#e0f2fe', 
                             linewidth=2.5)
ax.add_patch(client_box)
ax.text(1.75, 7.7, 'Client', fontsize=13, fontweight='bold', ha='center', color='#0369a1')
ax.text(1.75, 7.3, 'expects', fontsize=9, ha='center', style='italic')
ax.text(1.75, 7, 'Target', fontsize=9, ha='center', style='italic')
ax.text(1.75, 6.7, 'interface', fontsize=9, ha='center', style='italic')

# Target Interface
target_box = FancyBboxPatch((4.5, 6.5), 2.5, 1.5, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#8b5cf6', 
                             facecolor='#f3e8ff', 
                             linewidth=2.5)
ax.add_patch(target_box)
ax.text(5.75, 7.7, '«interface»', fontsize=9, ha='center', style='italic', color='#7c3aed')
ax.text(5.75, 7.35, 'Target', fontsize=12, fontweight='bold', ha='center', color='#7c3aed')
ax.text(5.75, 7, '+ operation()', fontsize=9, ha='center', family='monospace')

# Adapter
adapter_box = FancyBboxPatch((8, 6.5), 2.5, 1.5, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#10b981', 
                              facecolor='#d1fae5', 
                              linewidth=2.5)
ax.add_patch(adapter_box)
ax.text(9.25, 7.7, 'Adapter', fontsize=12, fontweight='bold', ha='center', color='#059669')
ax.text(9.25, 7.35, '- adaptee', fontsize=9, ha='center', family='monospace', style='italic')
ax.text(9.25, 7, '+ operation() {', fontsize=9, ha='center', family='monospace')
ax.text(9.25, 6.7, '  adaptee.specific()', fontsize=8, ha='center', family='monospace')

# Adaptee (Incompatible interface)
adaptee_box = FancyBboxPatch((11.5, 6.5), 2.5, 1.5, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#f59e0b', 
                              facecolor='#fef3c7', 
                              linewidth=2.5)
ax.add_patch(adaptee_box)
ax.text(12.75, 7.7, 'Adaptee', fontsize=12, fontweight='bold', ha='center', color='#d97706')
ax.text(12.75, 7.35, '(Legacy/3rd party)', fontsize=8, ha='center', style='italic', color='#92400e')
ax.text(12.75, 7, '+ specificRequest()', fontsize=9, ha='center', family='monospace')

# Arrow: Client uses Target
arrow_client_target = FancyArrowPatch((3, 7.25), (4.5, 7.25), 
                                       arrowstyle='->', mutation_scale=20, 
                                       linewidth=2, color='#0ea5e9')
ax.add_patch(arrow_client_target)
ax.text(3.75, 7.6, 'uses', fontsize=9, ha='center', fontweight='bold', color='#0369a1')

# Arrow: Adapter implements Target (dashed)
arrow_implements = FancyArrowPatch((9.25, 6.5), (5.75, 6.5), 
                                    arrowstyle='->', mutation_scale=20, 
                                    linewidth=2, color='#8b5cf6', 
                                    linestyle='dashed')
ax.add_patch(arrow_implements)
ax.text(7.5, 6.1, '«implements»', fontsize=9, ha='center', 
        style='italic', color='#7c3aed', fontweight='bold')

# Arrow: Adapter wraps Adaptee (composition)
arrow_wraps = FancyArrowPatch((10.5, 7.25), (11.5, 7.25), 
                               arrowstyle='->', mutation_scale=20, 
                               linewidth=2, color='#10b981')
ax.add_patch(arrow_wraps)
ax.text(11, 7.6, 'wraps', fontsize=9, ha='center', fontweight='bold', color='#059669')

# Real-world example section (Payment Processors)
example_y = 4

# Example Title
ax.text(7, example_y + 0.8, 'Real-World Example: Payment Processors', 
        fontsize=13, fontweight='bold', ha='center', 
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#e0e7ff', edgecolor='#6366f1', linewidth=2))

# PaymentProcessor interface (Target)
payment_interface = FancyBboxPatch((4.5, example_y - 1.5), 2.5, 1.3, 
                                    boxstyle="round,pad=0.1", 
                                    edgecolor='#8b5cf6', 
                                    facecolor='#f3e8ff', 
                                    linewidth=2)
ax.add_patch(payment_interface)
ax.text(5.75, example_y - 0.5, 'PaymentProcessor', fontsize=10, fontweight='bold', ha='center', color='#7c3aed')
ax.text(5.75, example_y - 0.8, '+ processPayment()', fontsize=8, ha='center', family='monospace')
ax.text(5.75, example_y - 1.1, '+ refund()', fontsize=8, ha='center', family='monospace')

# StripeAdapter
stripe_adapter = FancyBboxPatch((0.5, example_y - 1.5), 2, 1.3, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='#10b981', 
                                 facecolor='#d1fae5', 
                                 linewidth=1.5)
ax.add_patch(stripe_adapter)
ax.text(1.5, example_y - 0.5, 'StripeAdapter', fontsize=9, fontweight='bold', ha='center', color='#059669')
ax.text(1.5, example_y - 0.85, 'adapts', fontsize=7, ha='center', style='italic')
ax.text(1.5, example_y - 1.15, 'Stripe API', fontsize=7, ha='center', style='italic')

# PayPalAdapter
paypal_adapter = FancyBboxPatch((8, example_y - 1.5), 2, 1.3, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='#10b981', 
                                 facecolor='#d1fae5', 
                                 linewidth=1.5)
ax.add_patch(paypal_adapter)
ax.text(9, example_y - 0.5, 'PayPalAdapter', fontsize=9, fontweight='bold', ha='center', color='#059669')
ax.text(9, example_y - 0.85, 'adapts', fontsize=7, ha='center', style='italic')
ax.text(9, example_y - 1.15, 'PayPal API', fontsize=7, ha='center', style='italic')

# SquareAdapter
square_adapter = FancyBboxPatch((11, example_y - 1.5), 2, 1.3, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='#10b981', 
                                 facecolor='#d1fae5', 
                                 linewidth=1.5)
ax.add_patch(square_adapter)
ax.text(12, example_y - 0.5, 'SquareAdapter', fontsize=9, fontweight='bold', ha='center', color='#059669')
ax.text(12, example_y - 0.85, 'adapts', fontsize=7, ha='center', style='italic')
ax.text(12, example_y - 1.15, 'Square API', fontsize=7, ha='center', style='italic')

# Implement arrows
for x_pos in [1.5, 9, 12]:
    arrow = FancyArrowPatch((x_pos, example_y - 0.2), (5.75, example_y - 0.2), 
                             arrowstyle='->', mutation_scale=12, 
                             linewidth=1.5, color='#8b5cf6', 
                             linestyle='dashed', alpha=0.6)
    ax.add_patch(arrow)

# Benefits box
benefits_box = FancyBboxPatch((0.5, 0.3), 13, 1, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#10b981', 
                               facecolor='#ecfdf5', 
                               linewidth=2, alpha=0.9)
ax.add_patch(benefits_box)
ax.text(7, 1.1, 'Key Benefits: Interface Translation & Compatibility', 
        fontsize=11, fontweight='bold', ha='center', color='#059669')
ax.text(7, 0.8, '✓ Integrate incompatible interfaces  •  ✓ Wrap legacy code  •  ✓ Decouple from 3rd party APIs', 
        fontsize=9, ha='center')
ax.text(7, 0.5, 'Pattern: Adapter implements Target interface + wraps Adaptee + translates method calls', 
        fontsize=8, ha='center', family='monospace', style='italic', color='#065f46')

# Annotations
ax.text(1.75, 5.5, '1. Client calls', fontsize=8, ha='center', 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#dbeafe', alpha=0.9))
ax.text(5.75, 5.5, '2. Via interface', fontsize=8, ha='center', 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f3e8ff', alpha=0.9))
ax.text(9.25, 5.5, '3. Adapter translates', fontsize=8, ha='center', 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#d1fae5', alpha=0.9))
ax.text(12.75, 5.5, '4. To Adaptee', fontsize=8, ha='center', 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef3c7', alpha=0.9))

# Use Case annotation
ax.text(0.8, 9, 'Use Cases:', fontsize=9, fontweight='bold', ha='left')
ax.text(0.8, 8.7, '• 3rd party APIs', fontsize=7, ha='left')
ax.text(0.8, 8.45, '• Legacy systems', fontsize=7, ha='left')
ax.text(0.8, 8.2, '• Testing/Mocking', fontsize=7, ha='left')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Client'),
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Target Interface'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Adapter'),
    mpatches.Patch(facecolor='#fef3c7', edgecolor='#f59e0b', label='Adaptee'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/adapter_pattern.png', dpi=300, bbox_inches='tight')
print("Adapter Pattern diagram saved to docs/images/adapter_pattern.png")

