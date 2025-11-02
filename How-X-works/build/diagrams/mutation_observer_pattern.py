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
ax.text(8, 9.5, 'Mutation Observer Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(8, 9.0, 'Asynchronous DOM Change Detection with Batched Callbacks',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= Observer Flow =============
ax.text(1, 8.2, 'Observer Flow:', fontsize=11, weight='bold')

# Target element
target_box = FancyBboxPatch((0.5, 7), 2, 1,
                            boxstyle="round,pad=0.1",
                            edgecolor='#3498db', facecolor='#ebf5fb', linewidth=2)
ax.add_patch(target_box)
ax.text(1.5, 7.75, 'Target Element', fontsize=10, weight='bold', ha='center')
ax.text(1.5, 7.4, '<div id="app">', fontsize=8, ha='center', family='monospace')

# Observer
observer_box = FancyBboxPatch((3.5, 7), 2.5, 1,
                              boxstyle="round,pad=0.1",
                              edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=2)
ax.add_patch(observer_box)
ax.text(4.75, 7.75, 'MutationObserver', fontsize=10, weight='bold', ha='center')
ax.text(4.75, 7.4, 'observer.observe()', fontsize=8, ha='center', family='monospace')

# Config
config_box = FancyBboxPatch((6.5, 7), 2, 1,
                            boxstyle="round,pad=0.1",
                            edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=2)
ax.add_patch(config_box)
ax.text(7.5, 7.75, 'Configuration', fontsize=10, weight='bold', ha='center')
ax.text(7.5, 7.5, 'attributes: true', fontsize=7, ha='center', family='monospace')
ax.text(7.5, 7.3, 'childList: true', fontsize=7, ha='center', family='monospace')
ax.text(7.5, 7.1, 'subtree: true', fontsize=7, ha='center', family='monospace')

# Arrows
arrow1 = FancyArrowPatch((2.5, 7.5), (3.5, 7.5),
                        arrowstyle='->', mutation_scale=15,
                        linewidth=2, color='#34495e')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((6, 7.5), (6.5, 7.5),
                        arrowstyle='->', mutation_scale=15,
                        linewidth=2, color='#34495e')
ax.add_patch(arrow2)

# ============= Mutation Types =============
ax.text(10, 8.2, 'Observable Mutations:', fontsize=11, weight='bold')

mutation_types = [
    ('attributes', '#3498db', '• Class, style, id changes'),
    ('childList', '#2ecc71', '• Nodes added/removed'),
    ('characterData', '#e67e22', '• Text content changes'),
    ('subtree', '#9b59b6', '• Deep observation')
]

y_pos = 7.8
for mtype, color, desc in mutation_types:
    box = FancyBboxPatch((10, y_pos - 0.4), 5.5, 0.35,
                         boxstyle="round,pad=0.05",
                         edgecolor=color, facecolor=f'{color}22', linewidth=1.5)
    ax.add_patch(box)
    ax.text(10.2, y_pos - 0.15, mtype, fontsize=9, weight='bold', ha='left', color=color)
    ax.text(12, y_pos - 0.15, desc, fontsize=7, ha='left', style='italic')
    y_pos -= 0.6

# ============= Change Detection Flow =============
ax.text(0.5, 6.3, 'Change Detection & Callback Flow:', fontsize=11, weight='bold')

# Step 1: DOM Change
step1_box = FancyBboxPatch((0.5, 5.3), 2.5, 0.8,
                           boxstyle="round,pad=0.05",
                           edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=1.5)
ax.add_patch(step1_box)
ax.text(1.75, 5.9, '1. DOM Modified', fontsize=9, weight='bold', ha='center')
ax.text(1.75, 5.6, 'el.className = "new"', fontsize=7, ha='center', family='monospace')

# Arrow
flow_arrow1 = FancyArrowPatch((3, 5.7), (4, 5.7),
                             arrowstyle='->', mutation_scale=15,
                             linewidth=2, color='#34495e')
ax.add_patch(flow_arrow1)

# Step 2: Observer Detects
step2_box = FancyBboxPatch((4, 5.3), 2.5, 0.8,
                           boxstyle="round,pad=0.05",
                           edgecolor='#f39c12', facecolor='#fef5e7', linewidth=1.5)
ax.add_patch(step2_box)
ax.text(5.25, 5.9, '2. Change Detected', fontsize=9, weight='bold', ha='center')
ax.text(5.25, 5.6, 'Mutation recorded', fontsize=7, ha='center', family='monospace')

# Arrow
flow_arrow2 = FancyArrowPatch((6.5, 5.7), (7.5, 5.7),
                             arrowstyle='->', mutation_scale=15,
                             linewidth=2, color='#34495e')
ax.add_patch(flow_arrow2)

# Step 3: Batched
step3_box = FancyBboxPatch((7.5, 5.3), 2.5, 0.8,
                           boxstyle="round,pad=0.05",
                           edgecolor='#3498db', facecolor='#ebf5fb', linewidth=1.5)
ax.add_patch(step3_box)
ax.text(8.75, 5.9, '3. Batched Queue', fontsize=9, weight='bold', ha='center')
ax.text(8.75, 5.6, 'Async microtask', fontsize=7, ha='center', family='monospace')

# Arrow
flow_arrow3 = FancyArrowPatch((10, 5.7), (11, 5.7),
                             arrowstyle='->', mutation_scale=15,
                             linewidth=2, color='#34495e')
ax.add_patch(flow_arrow3)

# Step 4: Callback
step4_box = FancyBboxPatch((11, 5.3), 2.5, 0.8,
                           boxstyle="round,pad=0.05",
                           edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=1.5)
ax.add_patch(step4_box)
ax.text(12.25, 5.9, '4. Callback Fired', fontsize=9, weight='bold', ha='center')
ax.text(12.25, 5.6, 'Process mutations', fontsize=7, ha='center', family='monospace')

# ============= Code Example =============
ax.text(0.5, 4.8, 'Implementation Example:', fontsize=11, weight='bold')

code_box = FancyBboxPatch((0.5, 0.3), 7.5, 4.3,
                          boxstyle="round,pad=0.1",
                          edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=1)
ax.add_patch(code_box)

code = """// Create observer
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    console.log('Type:', mutation.type);
    console.log('Target:', mutation.target);
    
    if (mutation.type === 'childList') {
      console.log('Added:', mutation.addedNodes);
      console.log('Removed:', mutation.removedNodes);
    } else if (mutation.type === 'attributes') {
      console.log('Attribute:', mutation.attributeName);
      console.log('Old value:', mutation.oldValue);
    }
  });
});

// Configuration
const config = {
  attributes: true,           // Observe attribute changes
  attributeOldValue: true,    // Record old values
  childList: true,            // Watch children add/remove
  subtree: true,              // Observe all descendants
  characterData: true,        // Watch text content
  characterDataOldValue: true // Record old text
};

// Start observing
const target = document.getElementById('app');
observer.observe(target, config);

// Make changes (will trigger callback)
target.className = 'active';  // Attribute mutation
target.appendChild(div);       // ChildList mutation

// Stop observing
observer.disconnect();"""

ax.text(0.7, 4.6, code, fontsize=6.5, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ============= Benefits =============
ax.text(8.5, 4.8, 'Key Benefits:', fontsize=11, weight='bold')

benefits_box = FancyBboxPatch((8.5, 2.5), 7, 2.1,
                              boxstyle="round,pad=0.1",
                              edgecolor='#2ecc71', facecolor='#eafaf1', linewidth=1.5)
ax.add_patch(benefits_box)

benefits = """✓ Asynchronous & Batched
  • Changes queued and delivered in batches
  • No synchronous overhead

✓ Performance
  • Replaces deprecated Mutation Events
  • Efficient, non-blocking

✓ Precise Control
  • Configure exactly what to observe
  • Fine-grained change detection

✓ Reactive UI
  • Auto-respond to DOM changes
  • No manual polling needed

✓ Use Cases
  • Custom elements lifecycle
  • Dynamic content monitoring
  • Browser extensions
  • UI synchronization"""

ax.text(8.7, 4.5, benefits, fontsize=7, ha='left', va='top')

# ============= Mutation Record Properties =============
ax.text(8.5, 2.0, 'MutationRecord Properties:', fontsize=11, weight='bold')

props_box = FancyBboxPatch((8.5, 0.3), 7, 1.5,
                           boxstyle="round,pad=0.05",
                           edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=1.5)
ax.add_patch(props_box)

props = """• type: 'attributes' | 'childList' | 'characterData'
• target: Element where mutation occurred
• addedNodes: NodeList of added nodes
• removedNodes: NodeList of removed nodes
• previousSibling, nextSibling: Adjacent nodes
• attributeName: Name of changed attribute
• attributeNamespace: Namespace of attribute
• oldValue: Previous value (if configured)"""

ax.text(8.7, 1.7, props, fontsize=7, ha='left', va='top', family='monospace')

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#ebf5fb', edgecolor='#3498db', label='Target Element'),
    mpatches.Patch(facecolor='#eafaf1', edgecolor='#2ecc71', label='Observer'),
    mpatches.Patch(facecolor='#fadbd8', edgecolor='#e74c3c', label='DOM Change'),
    mpatches.Patch(facecolor='#fef5e7', edgecolor='#f39c12', label='Detection')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/mutation_observer_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Mutation Observer Pattern architecture diagram generated successfully")

