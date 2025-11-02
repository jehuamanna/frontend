#!/usr/bin/env python3
# ./build/diagrams/micro_frontend_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(16, 11))
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis('off')

# Title
ax.text(8, 10.5, 'Micro-Frontend Architecture Pattern', 
        fontsize=20, weight='bold', ha='center')
ax.text(8, 10.0, 'Decomposing Frontend Monoliths into Independent, Deployable Modules',
        fontsize=11, ha='center', style='italic', color='gray')

# ============= Container/Shell Application =============
container_box = FancyBboxPatch((1, 8), 14, 1.5,
                                boxstyle="round,pad=0.1",
                                edgecolor='#3b82f6', facecolor='#dbeafe', linewidth=3)
ax.add_patch(container_box)
ax.text(8, 9.15, '🏠 Container/Shell Application', fontsize=13, weight='bold', ha='center', color='#1e40af')
ax.text(8, 8.75, 'Routing  •  Layout  •  Shared State  •  Micro-Frontend Orchestration', 
        fontsize=9, ha='center', family='sans-serif')
ax.text(8, 8.4, 'import(\'./products/main.js\')  •  <app-products></app-products>', 
        fontsize=7, ha='center', family='monospace', style='italic', color='#6b7280')

# ============= Micro-Frontends =============
micro_frontends = [
    (1, 5, 'Products', '#10b981', 'products.example.com', 'React 18'),
    (5.5, 5, 'Cart', '#8b5cf6', 'cart.example.com', 'Vue 3'),
    (10, 5, 'Checkout', '#f59e0b', 'checkout.example.com', 'Angular 15'),
]

for x, y, name, color, domain, framework in micro_frontends:
    # Micro-frontend box
    mf_box = FancyBboxPatch((x, y), 4, 2.3,
                             boxstyle="round,pad=0.1",
                             edgecolor=color, facecolor=f'{color}22', linewidth=2.5)
    ax.add_patch(mf_box)
    
    ax.text(x + 2, y + 2, f'📦 {name} MFE', fontsize=11, weight='bold', ha='center', color=color)
    ax.text(x + 2, y + 1.65, f'{framework}', fontsize=8, ha='center', weight='bold')
    ax.text(x + 2, y + 1.35, '✓ Independent repo', fontsize=7, ha='center')
    ax.text(x + 2, y + 1.1, '✓ Independent deploy', fontsize=7, ha='center')
    ax.text(x + 2, y + 0.85, '✓ Own build pipeline', fontsize=7, ha='center')
    ax.text(x + 2, y + 0.6, '✓ Own dependencies', fontsize=7, ha='center')
    ax.text(x + 2, y + 0.3, domain, fontsize=7, ha='center', family='monospace', 
            style='italic', color='#6b7280')
    
    # Arrow from container to micro-frontend
    arrow = FancyArrowPatch((8, 8), (x + 2, y + 2.3),
                            arrowstyle='->', mutation_scale=20,
                            linewidth=2, color=color, alpha=0.7)
    ax.add_patch(arrow)

ax.text(8, 7.3, 'Loads & Composes', fontsize=9, ha='center', style='italic', color='#1e40af', weight='bold')

# ============= Integration Strategies =============
ax.text(1, 4.3, 'Integration Methods:', fontsize=10, weight='bold')

strategies_box = FancyBboxPatch((0.5, 1.8), 7, 2.3,
                                 boxstyle="round,pad=0.1",
                                 edgecolor='#6366f1', facecolor='#eef2ff', linewidth=1.5)
ax.add_patch(strategies_box)

strategies = """1. Build-Time Integration (Module Federation)
   webpack ModuleFederationPlugin

2. Runtime Integration (iframes)
   <iframe src="products.example.com"></iframe>

3. Web Components
   <app-products></app-products>

4. JavaScript Integration
   import('https://cdn.../products.js')"""

ax.text(0.7, 3.95, strategies, fontsize=7, ha='left', va='top', family='monospace')

# ============= Communication =============
ax.text(9, 4.3, 'Inter-MFE Communication:', fontsize=10, weight='bold')

comm_box = FancyBboxPatch((8.5, 1.8), 7, 2.3,
                           boxstyle="round,pad=0.1",
                           edgecolor='#ec4899', facecolor='#fce7f3', linewidth=1.5)
ax.add_patch(comm_box)

comm = """• Custom Events
  window.dispatchEvent(new CustomEvent('cart:add'))

• Shared State (Redux, Zustand, Context)
  window.__SHARED_STATE__

• Browser APIs
  LocalStorage, SessionStorage, BroadcastChannel

• Pub/Sub (Event Bus)"""

ax.text(8.7, 3.95, comm, fontsize=7, ha='left', va='top', family='monospace')

# ============= Benefits & Challenges =============
benefits_box = FancyBboxPatch((0.5, 0.1), 7, 1.5,
                               boxstyle="round,pad=0.1",
                               edgecolor='#10b981', facecolor='#d1fae5', linewidth=1.5)
ax.add_patch(benefits_box)
ax.text(4, 1.45, '✅ Benefits:', fontsize=10, weight='bold', ha='center', color='#047857')
benefits = """✓ Team autonomy  •  ✓ Independent deployments
✓ Tech stack flexibility  •  ✓ Incremental upgrades
✓ Faster development  •  ✓ Scalability"""
ax.text(0.7, 1.2, benefits, fontsize=7, ha='left', va='top')

challenges_box = FancyBboxPatch((8.5, 0.1), 7, 1.5,
                                 boxstyle="round,pad=0.1",
                                 edgecolor='#ef4444', facecolor='#fee2e2', linewidth=1.5)
ax.add_patch(challenges_box)
ax.text(12, 1.45, '⚠️ Challenges:', fontsize=10, weight='bold', ha='center', color='#991b1b')
challenges = """• Shared dependencies (duplication)
• Performance overhead (multiple bundles)
• Consistent UX  •  • State management complexity
• Testing complexity  •  • Deployment coordination"""
ax.text(8.7, 1.2, challenges, fontsize=7, ha='left', va='top')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#dbeafe', edgecolor='#3b82f6', label='Container/Shell'),
    mpatches.Patch(facecolor='#d1fae522', edgecolor='#10b981', label='Micro-Frontend (Independent)'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=9, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/micro_frontend_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Micro-Frontend Pattern diagram generated successfully")

