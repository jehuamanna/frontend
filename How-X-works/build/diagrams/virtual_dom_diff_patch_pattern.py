#!/usr/bin/env python3
# ./build/diagrams/virtual_dom_diff_patch_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(16, 11))
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis('off')

# Title
ax.text(8, 10.5, 'Virtual DOM Diff-Patch Pattern', 
        fontsize=20, weight='bold', ha='center')
ax.text(8, 10.0, 'Efficient DOM Updates Through In-Memory Representation',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= Phase 1: Render Virtual DOM =============
ax.text(2, 9.3, 'Phase 1: Render', fontsize=11, weight='bold', color='#3b82f6')

component_box = FancyBboxPatch((0.5, 8), 3, 1,
                                boxstyle="round,pad=0.1",
                                edgecolor='#3b82f6', facecolor='#dbeafe', linewidth=2)
ax.add_patch(component_box)
ax.text(2, 8.7, 'Component', fontsize=10, weight='bold', ha='center')
ax.text(2, 8.35, 'render(state)', fontsize=8, ha='center', family='monospace')

vdom_box = FancyBboxPatch((4.5, 8), 3, 1,
                           boxstyle="round,pad=0.1",
                           edgecolor='#8b5cf6', facecolor='#f3e8ff', linewidth=2)
ax.add_patch(vdom_box)
ax.text(6, 8.7, 'Virtual DOM', fontsize=10, weight='bold', ha='center', color='#6b21a8')
ax.text(6, 8.35, 'JS Object Tree', fontsize=8, ha='center', family='monospace', style='italic')

arrow1 = FancyArrowPatch((3.5, 8.5), (4.5, 8.5),
                         arrowstyle='->', mutation_scale=20,
                         linewidth=2, color='#3b82f6')
ax.add_patch(arrow1)
ax.text(4, 8.8, 'creates', fontsize=7, ha='center', style='italic')

# ============= Virtual DOM Trees =============
ax.text(8, 8.5, 'Virtual DOM Representation:', fontsize=10, weight='bold', color='#8b5cf6')

# Old VTree
old_vtree_box = FancyBboxPatch((0.5, 5.5), 4.5, 2.2,
                                boxstyle="round,pad=0.1",
                                edgecolor='#f59e0b', facecolor='#fef3c7', linewidth=2)
ax.add_patch(old_vtree_box)
ax.text(2.75, 7.5, 'Old Virtual Tree', fontsize=10, weight='bold', ha='center', color='#92400e')

old_vdom = """{
  tag: 'div',
  props: { id: 'app' },
  children: [
    { tag: 'h1', 
      children: ['Hello'] },
    { tag: 'p', 
      children: ['Count: 5'] }
  ]
}"""
ax.text(0.7, 7.3, old_vdom, fontsize=6, ha='left', va='top', family='monospace')

# New VTree
new_vtree_box = FancyBboxPatch((5.5, 5.5), 4.5, 2.2,
                                boxstyle="round,pad=0.1",
                                edgecolor='#10b981', facecolor='#d1fae5', linewidth=2)
ax.add_patch(new_vtree_box)
ax.text(7.75, 7.5, 'New Virtual Tree', fontsize=10, weight='bold', ha='center', color='#047857')

new_vdom = """{
  tag: 'div',
  props: { id: 'app' },
  children: [
    { tag: 'h1', 
      children: ['Hello'] },
    { tag: 'p', 
      children: ['Count: 6'] }
  ]
}"""
ax.text(5.7, 7.3, new_vdom, fontsize=6, ha='left', va='top', family='monospace')

# ============= Phase 2: Diff Algorithm =============
ax.text(12, 9.3, 'Phase 2: Diff', fontsize=11, weight='bold', color='#ec4899')

diff_box = FancyBboxPatch((11, 6.5), 4.5, 2.5,
                           boxstyle="round,pad=0.1",
                           edgecolor='#ec4899', facecolor='#fce7f3', linewidth=2.5)
ax.add_patch(diff_box)
ax.text(13.25, 8.7, 'Diff Algorithm', fontsize=11, weight='bold', ha='center', color='#9f1239')
ax.text(13.25, 8.35, 'Compare Trees', fontsize=9, ha='center', style='italic')

diff_steps = """1. Compare node types
2. Compare props
3. Compare children
4. Find changes:
   • CREATE
   • UPDATE
   • DELETE
   • REPLACE"""
ax.text(11.2, 8.1, diff_steps, fontsize=7, ha='left', va='top', family='monospace')

# Arrows to diff
arrow_old_diff = FancyArrowPatch((5, 6.5), (11, 7.5),
                                 arrowstyle='->', mutation_scale=15,
                                 linewidth=1.5, color='#f59e0b', linestyle='dashed')
ax.add_patch(arrow_old_diff)

arrow_new_diff = FancyArrowPatch((10, 6.5), (11, 7.5),
                                 arrowstyle='->', mutation_scale=15,
                                 linewidth=1.5, color='#10b981', linestyle='dashed')
ax.add_patch(arrow_new_diff)

# ============= Phase 3: Patch (Minimal Changes) =============
ax.text(2, 5, 'Phase 3: Patch', fontsize=11, weight='bold', color='#ef4444')

patches_box = FancyBboxPatch((0.5, 3.2), 5, 1.5,
                              boxstyle="round,pad=0.1",
                              edgecolor='#ef4444', facecolor='#fee2e2', linewidth=2)
ax.add_patch(patches_box)
ax.text(3, 4.5, 'Patches (Minimal Ops)', fontsize=10, weight='bold', ha='center', color='#991b1b')

patches = """[
  { type: 'UPDATE_TEXT',
    path: [1, 0],
    value: 'Count: 6' }
]"""
ax.text(0.7, 4.3, patches, fontsize=7, ha='left', va='top', family='monospace', color='#7f1d1d')

# Arrow from diff to patches
arrow_diff_patch = FancyArrowPatch((11, 7), (5.5, 4.5),
                                   arrowstyle='->', mutation_scale=20,
                                   linewidth=2, color='#ec4899')
ax.add_patch(arrow_diff_patch)
ax.text(8, 5.5, 'generates', fontsize=8, ha='center', style='italic', color='#9f1239')

# ============= Real DOM =============
real_dom_box = FancyBboxPatch((6.5, 3.2), 4, 1.5,
                               boxstyle="round,pad=0.1",
                               edgecolor='#0ea5e9', facecolor='#e0f2fe', linewidth=2.5)
ax.add_patch(real_dom_box)
ax.text(8.5, 4.5, '🌐 Real DOM', fontsize=11, weight='bold', ha='center', color='#0369a1')
ax.text(8.5, 4.15, '<div id="app">', fontsize=7, ha='center', family='monospace')
ax.text(8.5, 3.9, '  <h1>Hello</h1>', fontsize=7, ha='center', family='monospace')
ax.text(8.5, 3.65, '  <p>Count: 6</p>', fontsize=7, ha='center', family='monospace')
ax.text(8.5, 3.4, '</div>', fontsize=7, ha='center', family='monospace')

# Arrow from patches to real DOM
arrow_patch_dom = FancyArrowPatch((5.5, 4), (6.5, 4),
                                  arrowstyle='->', mutation_scale=20,
                                  linewidth=2.5, color='#ef4444')
ax.add_patch(arrow_patch_dom)
ax.text(6, 4.3, 'apply', fontsize=8, ha='center', weight='bold', color='#991b1b')

# ============= Benefits =============
benefits_box = FancyBboxPatch((0.5, 0.1), 7, 2.9,
                               boxstyle="round,pad=0.1",
                               edgecolor='#10b981', facecolor='#d1fae5', linewidth=1.5)
ax.add_patch(benefits_box)
ax.text(4, 2.85, '✅ Why Virtual DOM?', fontsize=10, weight='bold', ha='center', color='#047857')

benefits = """✓ Performance: Batch DOM updates (avoid reflows)
✓ Minimal Changes: Only update what changed
✓ Declarative: Describe UI, let framework handle updates
✓ Cross-Platform: Same pattern for native (React Native)
✓ Time-Travel: Keep snapshots for debugging

Process Flow:
  State Change → Render Virtual → Diff → Patch Real DOM

Optimization Techniques:
  • Keys for list reconciliation
  • Component memoization (shouldComponentUpdate)
  • Fiber architecture (incremental rendering)"""

ax.text(0.7, 2.6, benefits, fontsize=7, ha='left', va='top')

# ============= Frameworks =============
frameworks_box = FancyBboxPatch((8, 0.1), 7.5, 2.9,
                                 boxstyle="round,pad=0.1",
                                 edgecolor='#8b5cf6', facecolor='#f3e8ff', linewidth=1.5)
ax.add_patch(frameworks_box)
ax.text(11.75, 2.85, 'Frameworks Using VDOM:', fontsize=10, weight='bold', ha='center', color='#6b21a8')

frameworks = """• React (pioneer, Fiber reconciliation)
• Vue 2 & 3 (with compiler optimization)
• Preact (lightweight React alternative)
• Inferno (fast VDOM)

Alternatives (No VDOM):
• Svelte (compile-time, no runtime VDOM)
• Solid.js (fine-grained reactivity, direct DOM)

Diff Algorithms:
  React: O(n) heuristic tree diff
  Vue: Optimized with compile-time hints
  Preact: Simplified, smaller runtime"""

ax.text(8.2, 2.6, frameworks, fontsize=7, ha='left', va='top')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Virtual DOM (In-Memory)'),
    mpatches.Patch(facecolor='#fee2e2', edgecolor='#ef4444', label='Patches (Operations)'),
    mpatches.Patch(facecolor='#e0f2fe', edgecolor='#0ea5e9', label='Real DOM (Browser)'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=9, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/virtual_dom_diff_patch_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Virtual DOM Diff-Patch Pattern diagram generated successfully")

