import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Promise Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Represent future values; chain async operations; avoid callback hell',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_pending = '#FFC107'
color_fulfilled = '#4CAF50'
color_rejected = '#F44336'
color_chain = '#2196F3'

# ===== PROMISE STATES =====
# Pending
pending_circle = Circle((3, 7), 0.8, facecolor='#FFF9C4', edgecolor='#FFC107', linewidth=3)
ax.add_patch(pending_circle)
ax.text(3, 7.2, 'PENDING', fontsize=10, ha='center', weight='bold', color='#F57C00')
ax.text(3, 6.8, '(initial)', fontsize=8, ha='center', style='italic', color='#F57C00')

# Fulfilled
fulfilled_circle = Circle((7, 5), 0.8, facecolor='#E8F5E9', edgecolor='#4CAF50', linewidth=3)
ax.add_patch(fulfilled_circle)
ax.text(7, 5.2, 'FULFILLED', fontsize=10, ha='center', weight='bold', color='#2E7D32')
ax.text(7, 4.8, '(success)', fontsize=8, ha='center', style='italic', color='#2E7D32')

# Rejected
rejected_circle = Circle((11, 7), 0.8, facecolor='#FFEBEE', edgecolor='#F44336', linewidth=3)
ax.add_patch(rejected_circle)
ax.text(11, 7.2, 'REJECTED', fontsize=10, ha='center', weight='bold', color='#C62828')
ax.text(11, 6.8, '(failure)', fontsize=8, ha='center', style='italic', color='#C62828')

# State transitions
arrow_fulfill = FancyArrowPatch((3.7, 6.7), (6.3, 5.3),
                                arrowstyle='->,head_width=0.4,head_length=0.6',
                                color='#4CAF50', linewidth=3)
ax.add_patch(arrow_fulfill)
ax.text(5, 6.2, 'resolve(value)', fontsize=8, ha='center', weight='bold', color='#4CAF50')

arrow_reject = FancyArrowPatch((3.7, 7.3), (10.3, 7.3),
                               arrowstyle='->,head_width=0.4,head_length=0.6',
                               color='#F44336', linewidth=3)
ax.add_patch(arrow_reject)
ax.text(7, 7.6, 'reject(reason)', fontsize=8, ha='center', weight='bold', color='#F44336')

# Note: Immutable
immutable_box = FancyBboxPatch((1, 5.5), 2, 0.5,
                              boxstyle="round,pad=0.03", 
                              edgecolor='#666', facecolor='#F5F5F5',
                              linewidth=1)
ax.add_patch(immutable_box)
ax.text(2, 5.85, 'Once settled:', fontsize=7, ha='center', weight='bold', color='#666')
ax.text(2, 5.65, 'state IMMUTABLE', fontsize=6, ha='center', style='italic', color='#666')

# ===== PROMISE CHAINING =====
chain_box = FancyBboxPatch((0.3, 3.0), 6.4, 2.0,
                          boxstyle="round,pad=0.05", 
                          edgecolor='#2196F3', facecolor='#E3F2FD',
                          linewidth=2.5)
ax.add_patch(chain_box)
ax.text(3.5, 4.85, 'Promise Chaining (Flat, Not Nested!)', fontsize=11, ha='center', weight='bold', color='#1976D2')

# Chain visualization
chain_steps = [
    ('Promise 1', 4.5, '#2196F3'),
    ('.then()', 4.15, '#1976D2'),
    ('Promise 2', 3.8, '#2196F3'),
    ('.then()', 3.45, '#1976D2'),
    ('Promise 3', 3.1, '#2196F3')
]

x_pos = 1.0
for label, y, color in chain_steps:
    if '.then()' in label:
        ax.text(x_pos, y, label, fontsize=7, ha='left', weight='bold', color=color)
    else:
        rect = FancyBboxPatch((x_pos, y - 0.12), 1.2, 0.24,
                             boxstyle="round,pad=0.02", 
                             edgecolor=color, facecolor='white',
                             linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x_pos + 0.6, y, label, fontsize=7, ha='center', va='center', color=color, weight='bold')
    x_pos += 1.5

# Error handling
ax.text(3.5, 3.7, '.catch(error)', fontsize=8, ha='center', weight='bold', color='#F44336')
ax.text(3.5, 3.5, '(Centralized error handling)', fontsize=7, ha='center', style='italic', color='#F44336')

ax.text(3.5, 3.2, '.finally()', fontsize=8, ha='center', weight='bold', color='#9C27B0')

# ===== COMBINATORS =====
combinators_box = FancyBboxPatch((7.3, 3.0), 6.4, 2.0,
                                boxstyle="round,pad=0.05", 
                                edgecolor='#FF5722', facecolor='#FFEBEE',
                                linewidth=2.5)
ax.add_patch(combinators_box)
ax.text(10.5, 4.85, 'Promise Combinators', fontsize=11, ha='center', weight='bold', color='#D84315')

combinators = [
    ('Promise.all([p1, p2, p3])', 'Wait for ALL (parallel)', 4.5, '#4CAF50'),
    ('Promise.race([p1, p2, p3])', 'First to settle wins', 4.15, '#FFC107'),
    ('Promise.allSettled([...])', 'Wait for all, never rejects', 3.8, '#2196F3'),
    ('Promise.any([p1, p2, p3])', 'First to fulfill wins', 3.45, '#9C27B0')
]

for name, desc, y, color in combinators:
    ax.text(7.5, y, name, fontsize=7, ha='left', weight='bold', color=color, family='monospace')
    ax.text(7.7, y - 0.15, desc, fontsize=6, ha='left', style='italic', color='#666')

# ===== CALLBACK HELL VS PROMISES =====
comparison_box = FancyBboxPatch((0.3, 0.1), 13.4, 2.7,
                               boxstyle="round,pad=0.05", 
                               edgecolor='#666', facecolor='#FAFAFA',
                               linewidth=1.5)
ax.add_patch(comparison_box)
ax.text(7, 2.65, 'Callback Hell vs Promises', fontsize=11, ha='center', weight='bold')

# Callback Hell (left)
ax.text(0.5, 2.4, '❌ Callback Hell (Pyramid of Doom)', fontsize=9, ha='left', weight='bold', color='#F44336')

callback_code = [
    ('fetchUser(id, (user) => {', 2.15, 0.5),
    ('  fetchPosts(user.id, (posts) => {', 1.95, 0.7),
    ('    fetchComments(posts[0].id, (comments) => {', 1.75, 0.9),
    ('      console.log(comments); // 😵', 1.55, 1.1),
    ('    });', 1.35, 0.9),
    ('  });', 1.15, 0.7),
    ('});', 0.95, 0.5)
]

for code, y, indent in callback_code:
    ax.text(indent, y, code, fontsize=6, ha='left', family='monospace', color='#F44336')

ax.text(1.5, 0.75, '• Nested (hard to read)', fontsize=7, ha='left', color='#F44336')
ax.text(1.5, 0.60, '• Error handling scattered', fontsize=7, ha='left', color='#F44336')
ax.text(1.5, 0.45, '• Hard to compose', fontsize=7, ha='left', color='#F44336')

# Promises (right)
ax.text(7.5, 2.4, '✅ Promises (Flat Chain)', fontsize=9, ha='left', weight='bold', color='#4CAF50')

promise_code = [
    ('fetchUser(id)', 2.15),
    ('  .then(user => fetchPosts(user.id))', 1.95),
    ('  .then(posts => fetchComments(posts[0].id))', 1.75),
    ('  .then(comments => console.log(comments))', 1.55),
    ('  .catch(error => console.error(error))', 1.35),
    ('  .finally(() => cleanup());', 1.15)
]

for code, y in promise_code:
    ax.text(7.5, y, code, fontsize=6, ha='left', family='monospace', color='#4CAF50')

ax.text(8.5, 0.75, '✓ Flat (readable)', fontsize=7, ha='left', color='#4CAF50')
ax.text(8.5, 0.60, '✓ Centralized error handling', fontsize=7, ha='left', color='#4CAF50')
ax.text(8.5, 0.45, '✓ Easy to compose', fontsize=7, ha='left', color='#4CAF50')

# Async/Await
ax.text(11.5, 2.4, '✅ Async/Await (Even Better!)', fontsize=9, ha='left', weight='bold', color='#2196F3')

async_code = [
    ('async function() {', 2.15),
    ('  try {', 1.95),
    ('    const user = await fetchUser(id);', 1.75),
    ('    const posts = await fetchPosts(user.id);', 1.55),
    ('    const comments = await fetchComments(posts[0]);', 1.35),
    ('  } catch (error) { ... }', 1.15),
    ('}', 0.95)
]

for code, y in async_code:
    ax.text(11.5, y, code, fontsize=6, ha='left', family='monospace', color='#2196F3')

ax.text(12.0, 0.75, '✓ Looks synchronous', fontsize=7, ha='left', color='#2196F3')
ax.text(12.0, 0.60, '✓ Easy to understand', fontsize=7, ha='left', color='#2196F3')

# Key principle
principle_box = FancyBboxPatch((0.5, 0.2), 13.0, 0.2,
                              boxstyle="round,pad=0.03", 
                              edgecolor='#4CAF50', facecolor='#E8F5E9',
                              linewidth=2)
ax.add_patch(principle_box)
ax.text(7, 0.3, 'Key: Promise = future value. Chain with .then(), handle errors with .catch(). Avoid callback hell!', 
       fontsize=7, ha='center', weight='bold', color='#2E7D32')

plt.tight_layout()
plt.savefig('docs/images/promise_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Promise Pattern diagram generated: docs/images/promise_pattern.png")


