import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Async Iterator Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Pull-based async iteration with backpressure (for await...of)',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_iterator = '#9C27B0'
color_consumer = '#2196F3'
color_value = '#4CAF50'
color_promise = '#FF5722'

# ===== ASYNC ITERATOR =====
iterator_box = FancyBboxPatch((1.0, 5.5), 3.0, 2.5,
                              boxstyle="round,pad=0.05", 
                              edgecolor='#9C27B0', facecolor='#F3E5F5',
                              linewidth=3)
ax.add_patch(iterator_box)
ax.text(2.5, 7.85, 'ASYNC ITERATOR', fontsize=12, ha='center', weight='bold', color='#9C27B0')
ax.text(2.5, 7.65, '(Data Source)', fontsize=9, ha='center', style='italic', color='#9C27B0')

ax.text(1.2, 7.4, '• Async data source', fontsize=7, ha='left', color='#9C27B0')
ax.text(1.2, 7.2, '  (API, stream, DB)', fontsize=7, ha='left', color='#9C27B0')
ax.text(1.2, 7.0, '• next() returns', fontsize=7, ha='left', weight='bold', color='#9C27B0')
ax.text(1.4, 6.8, 'Promise<{value, done}>', fontsize=6, ha='left', family='monospace', color='#FF5722')

ax.text(1.2, 6.5, '• Pull-based', fontsize=7, ha='left', weight='bold', color='#9C27B0')
ax.text(1.2, 6.3, '  (waits for request)', fontsize=7, ha='left', color='#9C27B0')
ax.text(1.2, 6.1, '• Lazy', fontsize=7, ha='left', color='#9C27B0')

# Symbol
ax.text(1.2, 5.8, '[Symbol.asyncIterator]', fontsize=6, ha='left', family='monospace', color='#9C27B0', weight='bold')

# ===== CONSUMER =====
consumer_box = FancyBboxPatch((5.5, 5.5), 3.0, 2.5,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#2196F3', facecolor='#E3F2FD',
                             linewidth=3)
ax.add_patch(consumer_box)
ax.text(7.0, 7.85, 'CONSUMER', fontsize=12, ha='center', weight='bold', color='#1976D2')
ax.text(7.0, 7.65, '(for await...of)', fontsize=9, ha='center', style='italic', color='#1976D2')

ax.text(5.7, 7.4, '• Pulls values', fontsize=7, ha='left', weight='bold', color='#1976D2')
ax.text(5.7, 7.2, '  (controls pace)', fontsize=7, ha='left', color='#1976D2')
ax.text(5.7, 7.0, '• Awaits each value', fontsize=7, ha='left', color='#1976D2')
ax.text(5.7, 6.8, '• Backpressure', fontsize=7, ha='left', weight='bold', color='#4CAF50')

# Code
ax.text(5.7, 6.5, 'for await (const x', fontsize=6, ha='left', family='monospace', color='#1976D2')
ax.text(5.9, 6.3, 'of iterator) {', fontsize=6, ha='left', family='monospace', color='#1976D2')
ax.text(6.1, 6.1, 'await process(x);', fontsize=6, ha='left', family='monospace', color='#4CAF50')
ax.text(5.9, 5.9, '}', fontsize=6, ha='left', family='monospace', color='#1976D2')

# ===== VALUES (STREAM) =====
values_box = FancyBboxPatch((10.0, 5.5), 3.5, 2.5,
                           boxstyle="round,pad=0.05", 
                           edgecolor='#4CAF50', facecolor='#E8F5E9',
                           linewidth=3)
ax.add_patch(values_box)
ax.text(11.75, 7.85, 'ASYNC STREAM', fontsize=12, ha='center', weight='bold', color='#2E7D32')
ax.text(11.75, 7.65, '(Values Over Time)', fontsize=9, ha='center', style='italic', color='#2E7D32')

# Stream visualization
stream_values = [
    ('{ value: 1, done: false }', 7.4, '#4CAF50'),
    ('await delay...', 7.15, '#666'),
    ('{ value: 2, done: false }', 6.9, '#4CAF50'),
    ('await delay...', 6.65, '#666'),
    ('{ value: 3, done: false }', 6.4, '#4CAF50'),
    ('await delay...', 6.15, '#666'),
    ('{ done: true }', 5.9, '#FF5722')
]

for text, y, color in stream_values:
    ax.text(10.2, y, text, fontsize=6, ha='left', family='monospace', color=color)

# ===== FLOW ARROWS =====

# 1. Consumer → Iterator (pull request)
arrow1 = FancyArrowPatch((5.5, 6.75), (4.0, 6.75),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color='#2196F3', linewidth=3)
ax.add_patch(arrow1)
ax.text(4.75, 7.0, '1. next()', fontsize=8, ha='center', weight='bold', color='#2196F3')
ax.text(4.75, 6.5, 'PULL', fontsize=7, ha='center', style='italic', color='#2196F3', weight='bold')

# 2. Iterator → Consumer (promise returns value)
arrow2 = FancyArrowPatch((4.0, 6.5), (5.5, 6.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color='#FF5722', linewidth=3)
ax.add_patch(arrow2)
ax.text(4.75, 6.25, '2. Promise<{value}>', fontsize=7, ha='center', weight='bold', color='#FF5722')

# 3. Values from stream
arrow3 = FancyArrowPatch((10.0, 6.75), (8.5, 6.75),
                        arrowstyle='->,head_width=0.3,head_length=0.5',
                        color='#4CAF50', linewidth=2, linestyle='dashed')
ax.add_patch(arrow3)
ax.text(9.25, 7.0, 'async', fontsize=7, ha='center', style='italic', color='#4CAF50')

# ===== PULL VS PUSH =====
pull_push_box = FancyBboxPatch((0.3, 2.8), 6.4, 2.4,
                              boxstyle="round,pad=0.05", 
                              edgecolor='#666', facecolor='#FAFAFA',
                              linewidth=1.5)
ax.add_patch(pull_push_box)
ax.text(3.5, 5.05, 'Pull vs Push (Backpressure)', fontsize=11, ha='center', weight='bold')

ax.text(0.5, 4.75, 'PULL (Async Iterator):', fontsize=9, ha='left', weight='bold', color='#2196F3')
ax.text(0.5, 4.55, '• Consumer requests next value', fontsize=7, ha='left', color='#2196F3')
ax.text(0.5, 4.40, '• Consumer controls pace', fontsize=7, ha='left', weight='bold', color='#4CAF50')
ax.text(0.5, 4.25, '• Backpressure: slow consumer → producer waits', fontsize=7, ha='left', color='#4CAF50')
ax.text(0.5, 4.10, '• Example: for await (const x of iter) { await slow(x); }', fontsize=6, ha='left', family='monospace', color='#2196F3')

ax.text(0.5, 3.8, 'PUSH (Observable):', fontsize=9, ha='left', weight='bold', color='#FF5722')
ax.text(0.5, 3.60, '• Producer pushes values', fontsize=7, ha='left', color='#FF5722')
ax.text(0.5, 3.45, '• Producer controls pace', fontsize=7, ha='left', color='#FF5722')
ax.text(0.5, 3.30, '• No backpressure: fast producer → consumer overwhelmed', fontsize=7, ha='left', weight='bold', color='#F44336')
ax.text(0.5, 3.15, '• Example: observable.subscribe(x => { await slow(x); })', fontsize=6, ha='left', family='monospace', color='#FF5722')
ax.text(0.5, 3.00, '  → Can\'t keep up!', fontsize=6, ha='left', style='italic', color='#F44336')

# ===== OPERATORS =====
operators_box = FancyBboxPatch((7.3, 2.8), 6.4, 2.4,
                              boxstyle="round,pad=0.05", 
                              edgecolor='#666', facecolor='#FAFAFA',
                              linewidth=1.5)
ax.add_patch(operators_box)
ax.text(10.5, 5.05, 'Async Iterator Operators', fontsize=11, ha='center', weight='bold')

operators_code = [
    ('async function* map(iter, fn) {', 4.75),
    ('  for await (const x of iter) {', 4.60),
    ('    yield await fn(x);', 4.45),
    ('  }', 4.30),
    ('}', 4.15),
    ('', 3.95),
    ('async function* filter(iter, pred) {', 3.80),
    ('  for await (const x of iter) {', 3.65),
    ('    if (await pred(x)) yield x;', 3.50),
    ('  }', 3.35),
    ('}', 3.20),
    ('', 3.00)
]

for code, y in operators_code:
    if code:
        ax.text(7.5, y, code, fontsize=6, ha='left', family='monospace', color='#9C27B0')

ax.text(10.5, 2.95, 'Composable like Observables!', fontsize=7, ha='center', style='italic', color='#4CAF50')

# ===== FLOW =====
flow_box = FancyBboxPatch((0.3, 0.1), 13.4, 2.5,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(flow_box)
ax.text(7, 2.5, 'Async Iterator Flow', fontsize=10, ha='center', weight='bold')

flow_steps = [
    ('1', 'Consumer calls next() (PULL)', 2.25, '#2196F3'),
    ('2', 'Iterator awaits async operation (API, DB, etc.)', 2.05, '#9C27B0'),
    ('3', 'Iterator returns Promise<{value, done}>', 1.85, '#FF5722'),
    ('4', 'Consumer awaits promise', 1.65, '#2196F3'),
    ('5', 'Consumer processes value (slow OK!)', 1.45, '#4CAF50'),
    ('6', 'Consumer ready → calls next() again (BACKPRESSURE)', 1.25, '#2196F3')
]

for num, text, y, color in flow_steps:
    ax.text(0.5, y, num, fontsize=8, ha='center', weight='bold',
           bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=1.5))
    ax.text(1.0, y, text, fontsize=7, ha='left', color=color)

# vs Promise
comparison = [
    ('vs Promise: Promise = single async value. Async Iterator = MULTIPLE async values (sequential)', 0.95, '#666'),
    ('vs Observable: Observable = push (no backpressure). Async Iterator = PULL (backpressure)', 0.80, '#666'),
    ('for await...of: Elegant syntax for consuming async iterators', 0.65, '#2196F3')
]

for text, y, color in comparison:
    ax.text(0.5, y, text, fontsize=7, ha='left', style='italic', color=color)

# Key principle
principle_box = FancyBboxPatch((0.5, 0.2), 13.0, 0.4,
                              boxstyle="round,pad=0.03", 
                              edgecolor='#9C27B0', facecolor='#F3E5F5',
                              linewidth=2)
ax.add_patch(principle_box)
ax.text(7, 0.5, 'Key: PULL-based async iteration. Consumer controls pace → BACKPRESSURE. for await...of syntax.', 
       fontsize=7, ha='center', weight='bold', color='#9C27B0')
ax.text(7, 0.3, '(Perfect for paginated APIs, streams, file reading)', 
       fontsize=7, ha='center', style='italic', color='#9C27B0')

plt.tight_layout()
plt.savefig('docs/images/async_iterator_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Async Iterator Pattern diagram generated: docs/images/async_iterator_pattern.png")

