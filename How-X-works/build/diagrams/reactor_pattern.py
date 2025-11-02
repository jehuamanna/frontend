import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Wedge
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Reactor Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Single-threaded event loop for handling concurrent I/O (Node.js, browser event loop)',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_event_loop = '#9C27B0'
color_demux = '#FF5722'
color_handler = '#4CAF50'
color_io_source = '#2196F3'

# ===== EVENT LOOP (CENTER) =====
event_loop_circle = Circle((7, 5.5), 1.2, facecolor='#F3E5F5', edgecolor='#9C27B0', linewidth=4)
ax.add_patch(event_loop_circle)
ax.text(7, 5.8, 'EVENT', fontsize=12, ha='center', weight='bold', color='#9C27B0')
ax.text(7, 5.5, 'LOOP', fontsize=12, ha='center', weight='bold', color='#9C27B0')
ax.text(7, 5.2, '(Single Thread)', fontsize=8, ha='center', style='italic', color='#9C27B0')

# Loop arrow
loop_arrow = Wedge((7, 5.5), 1.5, 45, 315, width=0.15, 
                   facecolor='none', edgecolor='#9C27B0', linewidth=3)
ax.add_patch(loop_arrow)

# Arrow head for loop
arrow_head = FancyArrowPatch((7.9, 6.6), (8.1, 6.3),
                            arrowstyle='->,head_width=0.3,head_length=0.4',
                            color='#9C27B0', linewidth=3)
ax.add_patch(arrow_head)

ax.text(8.5, 6.5, 'while(true)', fontsize=8, ha='left', style='italic', color='#9C27B0', weight='bold')

# ===== DEMULTIPLEXER =====
demux_box = FancyBboxPatch((4.5, 7.5), 5.0, 1.3,
                          boxstyle="round,pad=0.05", 
                          edgecolor='#FF5722', facecolor='#FFEBEE',
                          linewidth=3)
ax.add_patch(demux_box)
ax.text(7, 8.6, 'DEMULTIPLEXER', fontsize=12, ha='center', weight='bold', color='#FF5722')
ax.text(7, 8.4, '(select / epoll / event queue)', fontsize=9, ha='center', style='italic', color='#FF5722')

ax.text(4.7, 8.1, '• Monitors multiple I/O sources', fontsize=7, ha='left', color='#FF5722')
ax.text(4.7, 7.9, '• Waits for events (blocking)', fontsize=7, ha='left', color='#FF5722')
ax.text(4.7, 7.7, '• Returns ready events', fontsize=7, ha='left', weight='bold', color='#FF5722')

# ===== I/O SOURCES =====
io_sources = [
    ('Socket 1', 1.0, 7.5, 0.8),
    ('Socket 2', 1.0, 6.5, 0.8),
    ('Timer', 1.0, 5.5, 0.8),
    ('File I/O', 1.0, 4.5, 0.8),
    ('Socket N', 1.0, 3.5, 0.8)
]

for label, x, y, size in io_sources:
    box = FancyBboxPatch((x - size/2, y - size/2), size, size,
                        boxstyle="round,pad=0.03", 
                        edgecolor='#2196F3', facecolor='#E3F2FD',
                        linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, y, label, fontsize=7, ha='center', va='center', color='#1976D2', weight='bold')
    
    # Arrow from I/O source to demux
    if label != 'Socket N':
        arrow = FancyArrowPatch((x + size/2, y), (4.5, 8.0),
                              arrowstyle='->,head_width=0.2,head_length=0.3',
                              color='#2196F3', linewidth=1.5, linestyle='dotted')
        ax.add_patch(arrow)

# "..." indicator
ax.text(1.0, 4.0, '...', fontsize=12, ha='center', color='#2196F3', weight='bold')

# Label
io_label_box = FancyBboxPatch((0.2, 2.8), 1.6, 0.5,
                             boxstyle="round,pad=0.03", 
                             edgecolor='#2196F3', facecolor='#E3F2FD',
                             linewidth=1.5)
ax.add_patch(io_label_box)
ax.text(1.0, 3.15, 'I/O SOURCES', fontsize=8, ha='center', weight='bold', color='#1976D2')
ax.text(1.0, 2.95, '(thousands)', fontsize=6, ha='center', style='italic', color='#1976D2')

# ===== EVENT HANDLERS =====
handlers = [
    ('Handler 1', 13.0, 7.5, 0.8),
    ('Handler 2', 13.0, 6.5, 0.8),
    ('Handler 3', 13.0, 5.5, 0.8),
    ('Handler 4', 13.0, 4.5, 0.8),
    ('Handler N', 13.0, 3.5, 0.8)
]

for label, x, y, size in handlers:
    box = FancyBboxPatch((x - size/2, y - size/2), size, size,
                        boxstyle="round,pad=0.03", 
                        edgecolor='#4CAF50', facecolor='#E8F5E9',
                        linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, y, label, fontsize=7, ha='center', va='center', color='#2E7D32', weight='bold')
    
    # Arrow from event loop to handler
    if label != 'Handler N':
        arrow = FancyArrowPatch((8.2, 5.5), (x - size/2, y),
                              arrowstyle='->,head_width=0.2,head_length=0.3',
                              color='#4CAF50', linewidth=1.5, linestyle='dotted')
        ax.add_patch(arrow)

# "..." indicator
ax.text(13.0, 4.0, '...', fontsize=12, ha='center', color='#4CAF50', weight='bold')

# Label
handler_label_box = FancyBboxPatch((12.2, 2.8), 1.6, 0.5,
                                  boxstyle="round,pad=0.03", 
                                  edgecolor='#4CAF50', facecolor='#E8F5E9',
                                  linewidth=1.5)
ax.add_patch(handler_label_box)
ax.text(13.0, 3.15, 'HANDLERS', fontsize=8, ha='center', weight='bold', color='#2E7D32')
ax.text(13.0, 2.95, '(callbacks)', fontsize=6, ha='center', style='italic', color='#2E7D32')

# ===== FLOW ARROWS =====

# 1. Demux → Event Loop
arrow1 = FancyArrowPatch((7, 7.5), (7, 6.7),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color='#FF5722', linewidth=3)
ax.add_patch(arrow1)
ax.text(7.3, 7.1, '1. event', fontsize=9, ha='left', weight='bold', color='#FF5722')

# 2. Event Loop → Handler (dispatch)
arrow2 = FancyArrowPatch((8.2, 5.5), (12.2, 5.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color='#4CAF50', linewidth=3)
ax.add_patch(arrow2)
ax.text(10.2, 5.75, '2. dispatch', fontsize=9, ha='center', weight='bold', color='#4CAF50')

# ===== FLOW STEPS =====
flow_box = FancyBboxPatch((2.5, 0.1), 9.0, 2.5,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(flow_box)
ax.text(7, 2.5, 'Reactor Flow (Single-Threaded Event Loop)', fontsize=10, ha='center', weight='bold')

flow_steps = [
    ('1', 'I/O sources (sockets, files, timers) wait for events', 2.25, '#2196F3'),
    ('2', 'Demultiplexer monitors all sources (select/epoll)', 2.05, '#FF5722'),
    ('3', 'Event Loop BLOCKS until event is ready', 1.85, '#9C27B0'),
    ('4', 'Demux returns ready event to Event Loop', 1.65, '#FF5722'),
    ('5', 'Event Loop DISPATCHES to registered handler', 1.45, '#4CAF50'),
    ('6', 'Handler executes (quickly, non-blocking)', 1.25, '#4CAF50'),
    ('7', 'Loop repeats (back to step 2)', 1.05, '#9C27B0')
]

for num, text, y, color in flow_steps:
    ax.text(2.7, y, num, fontsize=8, ha='center', weight='bold',
           bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=1.5))
    ax.text(3.2, y, text, fontsize=7, ha='left', color=color)

# Key advantages
advantages = [
    ('✓ ONE thread handles THOUSANDS of connections', 0.75, '#4CAF50'),
    ('✓ No thread-per-connection overhead', 0.60, '#4CAF50'),
    ('✓ Non-blocking I/O (high throughput)', 0.45, '#4CAF50'),
    ('✗ Handlers must NOT block (or event loop stalls)', 0.30, '#FF9800')
]

for text, y, color in advantages:
    ax.text(2.7, y, text, fontsize=7, ha='left', color=color, weight='bold')

# ===== COMPARISON =====
comparison_box = FancyBboxPatch((0.3, 0.1), 1.8, 2.5,
                               boxstyle="round,pad=0.05", 
                               edgecolor='#666', facecolor='#FAFAFA',
                               linewidth=1.5)
ax.add_patch(comparison_box)
ax.text(1.2, 2.5, 'Thread vs Reactor', fontsize=9, ha='center', weight='bold')

ax.text(0.5, 2.25, 'Thread-per-conn:', fontsize=7, ha='left', weight='bold', color='#666')
ax.text(0.5, 2.10, '10K clients', fontsize=6, ha='left', color='#FF5722')
ax.text(0.5, 1.95, '= 10K threads', fontsize=6, ha='left', color='#FF5722')
ax.text(0.5, 1.80, '= ~10 GB RAM!', fontsize=6, ha='left', color='#FF5722', weight='bold')

ax.text(0.5, 1.55, 'Reactor:', fontsize=7, ha='left', weight='bold', color='#666')
ax.text(0.5, 1.40, '10K clients', fontsize=6, ha='left', color='#4CAF50')
ax.text(0.5, 1.25, '= 1 thread', fontsize=6, ha='left', color='#4CAF50', weight='bold')
ax.text(0.5, 1.10, '= ~10 MB RAM', fontsize=6, ha='left', color='#4CAF50', weight='bold')

ax.text(0.5, 0.80, '1000x more', fontsize=7, ha='left', weight='bold', color='#4CAF50')
ax.text(0.5, 0.65, 'efficient!', fontsize=7, ha='left', weight='bold', color='#4CAF50')

# ===== KNOWN USES =====
uses_box = FancyBboxPatch((12.0, 0.1), 1.7, 2.5,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(uses_box)
ax.text(12.85, 2.5, 'Known Uses', fontsize=9, ha='center', weight='bold')

uses = [
    ('Node.js', 2.25),
    ('Browser', 2.05),
    ('Netty (Java)', 1.85),
    ('libuv', 1.65),
    ('Twisted (Py)', 1.45),
    ('Nginx', 1.25),
    ('Redis', 1.05),
    ('EventMachine', 0.85)
]

for text, y in uses:
    ax.text(12.2, y, f'• {text}', fontsize=7, ha='left', color='#2196F3')

# Key principle
principle_box = FancyBboxPatch((0.3, 0.2), 11.4, 0.2,
                              boxstyle="round,pad=0.03", 
                              edgecolor='#9C27B0', facecolor='#F3E5F5',
                              linewidth=2)
ax.add_patch(principle_box)
ax.text(6.0, 0.3, 'Key: One thread, event loop, non-blocking I/O → handle thousands of concurrent connections efficiently', 
       fontsize=7, ha='center', weight='bold', color='#9C27B0')

plt.tight_layout()
plt.savefig('docs/images/reactor_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Reactor Pattern diagram generated: docs/images/reactor_pattern.png")

