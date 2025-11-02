import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(8, 9.5, 'Signal Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(8, 9.0, 'Fine-Grained Reactive State Management',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= Core Concepts =============
ax.text(1, 8.2, 'Core Reactive Primitives:', fontsize=11, weight='bold')

# Signal (State)
signal_box = FancyBboxPatch((0.5, 6.8), 2, 1.2, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='#3498db', facecolor='#ebf5fb', linewidth=2)
ax.add_patch(signal_box)
ax.text(1.5, 7.7, 'Signal', fontsize=11, weight='bold', ha='center')
ax.text(1.5, 7.35, 'const [count,', fontsize=8, ha='center', family='monospace')
ax.text(1.5, 7.1, 'setCount] =', fontsize=8, ha='center', family='monospace')
ax.text(1.5, 6.85, 'createSignal(0)', fontsize=8, ha='center', family='monospace')
ax.text(1.5, 6.5, '(Reactive State)', fontsize=7, ha='center', style='italic', color='gray')

# Computed (Derived)
computed_box = FancyBboxPatch((3.5, 6.8), 2, 1.2, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=2)
ax.add_patch(computed_box)
ax.text(4.5, 7.7, 'Computed', fontsize=11, weight='bold', ha='center')
ax.text(4.5, 7.35, 'const doubled =', fontsize=8, ha='center', family='monospace')
ax.text(4.5, 7.1, 'createComputed(', fontsize=8, ha='center', family='monospace')
ax.text(4.5, 6.85, '() => count()*2', fontsize=8, ha='center', family='monospace')
ax.text(4.5, 6.5, '(Auto-updates)', fontsize=7, ha='center', style='italic', color='gray')

# Effect (Side Effect)
effect_box = FancyBboxPatch((6.5, 6.8), 2, 1.2, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=2)
ax.add_patch(effect_box)
ax.text(7.5, 7.7, 'Effect', fontsize=11, weight='bold', ha='center')
ax.text(7.5, 7.35, 'createEffect(', fontsize=8, ha='center', family='monospace')
ax.text(7.5, 7.1, '() => console.log', fontsize=8, ha='center', family='monospace')
ax.text(7.5, 6.85, '(count())', fontsize=8, ha='center', family='monospace')
ax.text(7.5, 6.5, '(Auto-runs)', fontsize=7, ha='center', style='italic', color='gray')

# Arrows showing data flow
arrow1 = FancyArrowPatch((2.5, 7.4), (3.5, 7.4),
                        arrowstyle='->', mutation_scale=20, 
                        linewidth=2, color='#34495e')
ax.add_patch(arrow1)
ax.text(3, 7.7, 'reads', fontsize=8, ha='center', style='italic', color='gray')

arrow2 = FancyArrowPatch((5.5, 7.4), (6.5, 7.4),
                        arrowstyle='->', mutation_scale=20, 
                        linewidth=2, color='#34495e')
ax.add_patch(arrow2)
ax.text(6, 7.7, 'reads', fontsize=8, ha='center', style='italic', color='gray')

# ============= Dependency Tracking =============
ax.text(9.5, 8.2, 'Automatic Dependency Tracking:', fontsize=11, weight='bold')

# Tracking visualization
# Signal
track_signal = Circle((10, 7.4), 0.3, edgecolor='#3498db', facecolor='#ebf5fb', linewidth=2)
ax.add_patch(track_signal)
ax.text(10, 7.4, 'S', fontsize=12, weight='bold', ha='center', va='center')
ax.text(10, 6.9, 'Signal', fontsize=8, ha='center')

# Subscribers
sub1 = Circle((11.5, 8), 0.25, edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=1.5)
ax.add_patch(sub1)
ax.text(11.5, 8, 'C1', fontsize=9, weight='bold', ha='center', va='center')

sub2 = Circle((11.5, 7.4), 0.25, edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=1.5)
ax.add_patch(sub2)
ax.text(11.5, 7.4, 'C2', fontsize=9, weight='bold', ha='center', va='center')

sub3 = Circle((11.5, 6.8), 0.25, edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=1.5)
ax.add_patch(sub3)
ax.text(11.5, 6.8, 'E', fontsize=9, weight='bold', ha='center', va='center')

# Dependency arrows
dep_arrow1 = FancyArrowPatch((10.3, 7.55), (11.25, 7.9),
                            arrowstyle='->', mutation_scale=15, 
                            linewidth=1.5, color='#95a5a6', linestyle='dashed')
ax.add_patch(dep_arrow1)

dep_arrow2 = FancyArrowPatch((10.3, 7.4), (11.25, 7.4),
                            arrowstyle='->', mutation_scale=15, 
                            linewidth=1.5, color='#95a5a6', linestyle='dashed')
ax.add_patch(dep_arrow2)

dep_arrow3 = FancyArrowPatch((10.3, 7.25), (11.25, 6.9),
                            arrowstyle='->', mutation_scale=15, 
                            linewidth=1.5, color='#95a5a6', linestyle='dashed')
ax.add_patch(dep_arrow3)

ax.text(10.75, 6.4, 'Tracked\nDependencies', fontsize=7, ha='center', style='italic', color='gray')

# ============= Update Flow =============
ax.text(1, 5.8, 'Update Propagation:', fontsize=11, weight='bold')

# Timeline
steps = [
    ('1. State Change', 1, '#3498db'),
    ('2. Notify Deps', 3.5, '#9b59b6'),
    ('3. Re-compute', 6, '#9b59b6'),
    ('4. Run Effects', 8.5, '#e74c3c'),
    ('5. Update DOM', 11, '#2ecc71')
]

for i, (label, x, color) in enumerate(steps):
    # Step box
    step_box = FancyBboxPatch((x - 0.8, 4.5), 1.6, 0.8,
                              boxstyle="round,pad=0.05",
                              edgecolor=color, facecolor=f'{color}22', linewidth=2)
    ax.add_patch(step_box)
    
    # Step number
    step_circle = Circle((x, 5.2), 0.2, edgecolor=color, facecolor='white', linewidth=2)
    ax.add_patch(step_circle)
    ax.text(x, 5.2, str(i+1), fontsize=10, weight='bold', ha='center', va='center', color=color)
    
    # Label
    ax.text(x, 4.8, label.split('. ')[1], fontsize=8, ha='center', va='center', weight='bold')
    
    # Arrow to next step
    if i < len(steps) - 1:
        arrow = FancyArrowPatch((x + 0.8, 4.9), (steps[i+1][1] - 0.8, 4.9),
                               arrowstyle='->', mutation_scale=15,
                               linewidth=1.5, color='#34495e')
        ax.add_patch(arrow)

# ============= Fine-Grained vs Coarse-Grained =============
ax.text(1, 3.8, 'Comparison: Fine-Grained vs Coarse-Grained:', fontsize=11, weight='bold')

# Fine-grained (Signals)
fine_box = FancyBboxPatch((0.5, 1.8), 7, 1.8,
                          boxstyle="round,pad=0.1",
                          edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=2)
ax.add_patch(fine_box)
ax.text(4, 3.4, 'Fine-Grained (Signals)', fontsize=10, weight='bold', ha='center', color='#2ecc71')

fine_text = """✓ Only affected computations re-run
✓ Updates specific DOM nodes
✓ No re-renders
✓ Automatic dependency tracking
✓ Minimal work on updates

Example: count changes → only <span>{count}</span> updates"""
ax.text(0.7, 3.2, fine_text, fontsize=7, ha='left', va='top', family='sans-serif',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

# Coarse-grained (React)
coarse_box = FancyBboxPatch((8.5, 1.8), 7, 1.8,
                            boxstyle="round,pad=0.1",
                            edgecolor='#e67e22', facecolor='#fef5e7', linewidth=2)
ax.add_patch(coarse_box)
ax.text(12, 3.4, 'Coarse-Grained (React useState)', fontsize=10, weight='bold', ha='center', color='#e67e22')

coarse_text = """• Entire component re-renders
• All JSX re-evaluated
• Virtual DOM diffing
• Manual dependency arrays
• More work on updates

Example: count changes → entire component function runs"""
ax.text(8.7, 3.2, coarse_text, fontsize=7, ha='left', va='top', family='sans-serif',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

# ============= Code Example =============
ax.text(1, 1.4, 'Usage Example:', fontsize=11, weight='bold')

code_box = FancyBboxPatch((0.5, 0.1), 7, 1.1,
                          boxstyle="round,pad=0.1",
                          edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=1)
ax.add_patch(code_box)

code = """// Create signal
const [count, setCount] = createSignal(0);

// Create computed (auto-updates when count changes)
const doubled = createComputed(() => count() * 2);

// Create effect (auto-runs when dependencies change)
createEffect(() => {
  console.log(`Count: ${count()}, Doubled: ${doubled()}`);
});

setCount(5); // Effect automatically runs, logs: Count: 5, Doubled: 10"""

ax.text(0.7, 1.05, code, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Benefits box
benefits_box = FancyBboxPatch((8.5, 0.1), 7, 1.1,
                              boxstyle="round,pad=0.1",
                              edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1)
ax.add_patch(benefits_box)
ax.text(12, 1.05, 'Key Benefits:', fontsize=10, weight='bold', ha='center')

benefits = """• Fine-grained reactivity (minimal updates)
• Automatic dependency tracking
• No manual subscriptions
• Better performance (no re-renders)
• Simpler mental model
• Works great for large-scale apps
• Framework-agnostic (SolidJS, Vue 3, Angular, Preact)"""

ax.text(8.7, 0.9, benefits, fontsize=7, ha='left', va='top')

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#ebf5fb', edgecolor='#3498db', label='Signal (State)'),
    mpatches.Patch(facecolor='#f4ecf7', edgecolor='#9b59b6', label='Computed (Derived)'),
    mpatches.Patch(facecolor='#fadbd8', edgecolor='#e74c3c', label='Effect (Side Effect)'),
    mpatches.Patch(facecolor='#eafaf1', edgecolor='#2ecc71', label='Fine-Grained Update')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/signal_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Signal Pattern architecture diagram generated successfully")

