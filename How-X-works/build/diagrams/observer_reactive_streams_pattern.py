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
ax.text(7, 9.5, 'Observer (Reactive Streams) Pattern', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Asynchronous data streams over time with operators (RxJS, reactive programming)',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_observable = '#9C27B0'
color_observer = '#2196F3'
color_operator = '#FF5722'
color_value = '#4CAF50'

# ===== OBSERVABLE (SOURCE) =====
observable_box = FancyBboxPatch((0.5, 6.0), 2.5, 2.5,
                                boxstyle="round,pad=0.05", 
                                edgecolor='#9C27B0', facecolor='#F3E5F5',
                                linewidth=3)
ax.add_patch(observable_box)
ax.text(1.75, 8.3, 'OBSERVABLE', fontsize=12, ha='center', weight='bold', color='#9C27B0')
ax.text(1.75, 8.1, '(Stream Source)', fontsize=9, ha='center', style='italic', color='#9C27B0')

ax.text(0.7, 7.85, '• Emits values', fontsize=7, ha='left', color='#9C27B0')
ax.text(0.7, 7.65, '  over time', fontsize=7, ha='left', color='#9C27B0')
ax.text(0.7, 7.45, '• Async', fontsize=7, ha='left', weight='bold', color='#9C27B0')
ax.text(0.7, 7.25, '• Push-based', fontsize=7, ha='left', color='#9C27B0')

# Value stream visualization
ax.text(0.7, 6.95, 'Stream:', fontsize=7, ha='left', weight='bold', color='#9C27B0')
ax.text(0.7, 6.75, '[1, 2, 3, ...]', fontsize=6, ha='left', family='monospace', color='#4CAF50')
ax.text(0.7, 6.55, '  or', fontsize=6, ha='left', style='italic', color='#666')
ax.text(0.7, 6.35, 'error / complete', fontsize=6, ha='left', family='monospace', color='#F44336')

# ===== OPERATORS (MIDDLE) =====
operators_box = FancyBboxPatch((4.0, 6.0), 3.0, 2.5,
                              boxstyle="round,pad=0.05", 
                              edgecolor='#FF5722', facecolor='#FFEBEE',
                              linewidth=3)
ax.add_patch(operators_box)
ax.text(5.5, 8.3, 'OPERATORS', fontsize=12, ha='center', weight='bold', color='#FF5722')
ax.text(5.5, 8.1, '(Transformations)', fontsize=9, ha='center', style='italic', color='#FF5722')

ax.text(4.2, 7.85, '• map, filter', fontsize=7, ha='left', color='#FF5722')
ax.text(4.2, 7.65, '• merge, concat', fontsize=7, ha='left', color='#FF5722')
ax.text(4.2, 7.45, '• debounce, throttle', fontsize=7, ha='left', color='#FF5722')
ax.text(4.2, 7.25, '• switchMap', fontsize=7, ha='left', color='#FF5722')

# Operator chain
ax.text(4.2, 6.95, 'Chain:', fontsize=7, ha='left', weight='bold', color='#FF5722')
ax.text(4.2, 6.75, 'obs$.map().filter()', fontsize=6, ha='left', family='monospace', color='#FF5722')
ax.text(4.2, 6.55, '  .debounce()', fontsize=6, ha='left', family='monospace', color='#FF5722')
ax.text(4.2, 6.35, 'COMPOSABLE', fontsize=6, ha='left', weight='bold', color='#FF5722', style='italic')

# ===== OBSERVER (SUBSCRIBER) =====
observer_box = FancyBboxPatch((8.0, 6.0), 2.5, 2.5,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#2196F3', facecolor='#E3F2FD',
                             linewidth=3)
ax.add_patch(observer_box)
ax.text(9.25, 8.3, 'OBSERVER', fontsize=12, ha='center', weight='bold', color='#1976D2')
ax.text(9.25, 8.1, '(Subscriber)', fontsize=9, ha='center', style='italic', color='#1976D2')

ax.text(8.2, 7.85, '• Subscribes', fontsize=7, ha='left', color='#1976D2')
ax.text(8.2, 7.65, '• Receives:', fontsize=7, ha='left', weight='bold', color='#1976D2')
ax.text(8.4, 7.45, 'next(value)', fontsize=6, ha='left', family='monospace', color='#4CAF50')
ax.text(8.4, 7.25, 'error(err)', fontsize=6, ha='left', family='monospace', color='#F44336')
ax.text(8.4, 7.05, 'complete()', fontsize=6, ha='left', family='monospace', color='#9C27B0')

ax.text(8.2, 6.7, 'Unsubscribe:', fontsize=7, ha='left', weight='bold', color='#1976D2')
ax.text(8.2, 6.5, 'subscription()', fontsize=6, ha='left', family='monospace', color='#1976D2')

# ===== ARROWS =====

# 1. Observable → Operators
arrow1 = FancyArrowPatch((3.0, 7.25), (4.0, 7.25),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color='#9C27B0', linewidth=3)
ax.add_patch(arrow1)
ax.text(3.5, 7.5, 'emit', fontsize=8, ha='center', weight='bold', color='#9C27B0')

# 2. Operators → Observer
arrow2 = FancyArrowPatch((7.0, 7.25), (8.0, 7.25),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color='#FF5722', linewidth=3)
ax.add_patch(arrow2)
ax.text(7.5, 7.5, 'transform', fontsize=8, ha='center', weight='bold', color='#FF5722')

# 3. Observer subscribes
arrow3 = FancyArrowPatch((9.25, 6.0), (5.5, 5.0),
                        arrowstyle='->,head_width=0.3,head_length=0.5',
                        color='#2196F3', linewidth=2, linestyle='dashed')
ax.add_patch(arrow3)
ax.text(7.5, 5.5, 'subscribe', fontsize=7, ha='center', style='italic', color='#2196F3')

# ===== HOT VS COLD =====
hot_cold_box = FancyBboxPatch((11, 6.0), 2.7, 2.5,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#666', facecolor='#F5F5F5',
                             linewidth=2)
ax.add_patch(hot_cold_box)
ax.text(12.35, 8.3, 'Hot vs Cold', fontsize=10, ha='center', weight='bold')

ax.text(11.2, 7.95, 'Cold (Unicast):', fontsize=7, ha='left', weight='bold', color='#2196F3')
ax.text(11.2, 7.75, '• New producer', fontsize=6, ha='left', color='#2196F3')
ax.text(11.2, 7.60, '  per subscriber', fontsize=6, ha='left', color='#2196F3')
ax.text(11.2, 7.45, '• Lazy', fontsize=6, ha='left', color='#2196F3')

ax.text(11.2, 7.15, 'Hot (Multicast):', fontsize=7, ha='left', weight='bold', color='#FF5722')
ax.text(11.2, 6.95, '• Shared producer', fontsize=6, ha='left', color='#FF5722')
ax.text(11.2, 6.80, '• All subscribers', fontsize=6, ha='left', color='#FF5722')
ax.text(11.2, 6.65, '  get same values', fontsize=6, ha='left', color='#FF5722')
ax.text(11.2, 6.50, '• Eager', fontsize=6, ha='left', color='#FF5722')

# ===== OPERATORS SHOWCASE =====
operators_showcase_box = FancyBboxPatch((0.3, 2.8), 6.4, 2.9,
                                       boxstyle="round,pad=0.05", 
                                       edgecolor='#666', facecolor='#FAFAFA',
                                       linewidth=1.5)
ax.add_patch(operators_showcase_box)
ax.text(3.5, 5.55, 'Common Operators', fontsize=11, ha='center', weight='bold')

operators_list = [
    ('Transformation:', '', 5.25),
    ('  map, filter, scan', '#FF5722', 5.05),
    ('Combination:', '', 4.80),
    ('  merge, concat, zip, combineLatest', '#9C27B0', 4.60),
    ('Filtering:', '', 4.35),
    ('  debounce, throttle, distinctUntilChanged', '#4CAF50', 4.15),
    ('Error Handling:', '', 3.90),
    ('  catchError, retry, retryWhen', '#F44336', 3.70),
    ('Utility:', '', 3.45),
    ('  tap, delay, timeout', '#2196F3', 3.25),
    ('Higher-Order:', '', 3.00),
    ('  switchMap, mergeMap, concatMap', '#FF9800', 2.80)
]

for label, color, y in operators_list:
    if color:
        ax.text(0.5, y, label, fontsize=7, ha='left', family='monospace', color=color)
    else:
        ax.text(0.5, y, label, fontsize=7, ha='left', weight='bold', color='#333')

# ===== EXAMPLE STREAM =====
example_box = FancyBboxPatch((7.3, 2.8), 6.4, 2.9,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#666', facecolor='#FAFAFA',
                            linewidth=1.5)
ax.add_patch(example_box)
ax.text(10.5, 5.55, 'Example: Search with Debounce', fontsize=11, ha='center', weight='bold')

example_code = [
    ('const search$ = fromEvent(input, "input")', 5.25, '#9C27B0'),
    ('  .map(e => e.target.value)', 5.05, '#FF5722'),
    ('  .debounceTime(300) // Wait 300ms', 4.85, '#4CAF50'),
    ('  .distinctUntilChanged() // Skip duplicates', 4.65, '#4CAF50'),
    ('  .switchMap(query => // Cancel prev request', 4.45, '#FF9800'),
    ('    fetch(`/api/search?q=${query}`)', 4.25, '#2196F3'),
    ('      .then(r => r.json())', 4.05, '#2196F3'),
    ('  )', 3.85, '#2196F3'),
    ('  .subscribe(results => {', 3.65, '#2196F3'),
    ('    displayResults(results);', 3.45, '#2196F3'),
    ('  });', 3.25, '#2196F3')
]

for code, y, color in example_code:
    ax.text(7.5, y, code, fontsize=6, ha='left', family='monospace', color=color)

ax.text(10.5, 3.0, '✓ Debounce (wait for user to stop typing)', fontsize=6, ha='center', color='#4CAF50')
ax.text(10.5, 2.85, '✓ Cancel previous request (switchMap)', fontsize=6, ha='center', color='#4CAF50')

# ===== FLOW =====
flow_box = FancyBboxPatch((0.3, 0.1), 13.4, 2.5,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(flow_box)
ax.text(7, 2.5, 'Reactive Streams Flow', fontsize=10, ha='center', weight='bold')

flow_steps = [
    ('1', 'Observable emits values OVER TIME (async)', 2.25, '#9C27B0'),
    ('2', 'Operators transform stream (map, filter, etc.)', 2.05, '#FF5722'),
    ('3', 'Observer subscribes (next/error/complete)', 1.85, '#2196F3'),
    ('4', 'Observer receives transformed values', 1.65, '#4CAF50'),
    ('5', 'Unsubscribe to stop receiving values', 1.45, '#2196F3')
]

for num, text, y, color in flow_steps:
    ax.text(0.5, y, num, fontsize=8, ha='center', weight='bold',
           bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=1.5))
    ax.text(1.0, y, text, fontsize=7, ha='left', color=color)

# Key differences
differences = [
    ('vs Promise: Promises are single value; Observables are MULTIPLE values over time', 1.15, '#666'),
    ('vs Callbacks: Observables are composable, declarative; callbacks are not', 0.95, '#666'),
    ('vs Events: Observables support operators, backpressure; events do not', 0.75, '#666')
]

for text, y, color in differences:
    ax.text(0.5, y, text, fontsize=7, ha='left', style='italic', color=color)

# Key principle
principle_box = FancyBboxPatch((0.5, 0.2), 13.0, 0.4,
                              boxstyle="round,pad=0.03", 
                              edgecolor='#9C27B0', facecolor='#F3E5F5',
                              linewidth=2)
ax.add_patch(principle_box)
ax.text(7, 0.5, 'Key: Treat events, async data, and values as STREAMS. Compose with operators. Subscribe to receive.', 
       fontsize=7, ha='center', weight='bold', color='#9C27B0')
ax.text(7, 0.3, '(Foundation of RxJS, reactive programming, event-driven architectures)', 
       fontsize=7, ha='center', style='italic', color='#9C27B0')

plt.tight_layout()
plt.savefig('docs/images/observer_reactive_streams_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Observer (Reactive Streams) Pattern diagram generated: docs/images/observer_reactive_streams_pattern.png")


