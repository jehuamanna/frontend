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
ax.text(7, 9.5, 'Scheduler Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Control when and how tasks execute (priorities, timing, concurrency limits)',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_queue = '#2196F3'
color_scheduler = '#9C27B0'
color_task = '#4CAF50'
color_policy = '#FF5722'

# ===== TASK QUEUE =====
queue_box = FancyBboxPatch((0.5, 5.0), 2.5, 3.0,
                          boxstyle="round,pad=0.05", 
                          edgecolor='#2196F3', facecolor='#E3F2FD',
                          linewidth=3)
ax.add_patch(queue_box)
ax.text(1.75, 7.85, 'TASK QUEUE', fontsize=12, ha='center', weight='bold', color='#1976D2')

# Task items in queue
tasks_in_queue = [
    ('Task A (P:1)', 7.5, '#F44336'),
    ('Task B (P:5)', 7.2, '#FFC107'),
    ('Task C (P:2)', 6.9, '#FF5722'),
    ('Task D (P:10)', 6.6, '#4CAF50'),
    ('...', 6.3, '#666')
]

for label, y, color in tasks_in_queue:
    if label != '...':
        task_rect = FancyBboxPatch((0.7, y - 0.12), 2.1, 0.24,
                                  boxstyle="round,pad=0.02", 
                                  edgecolor=color, facecolor='white',
                                  linewidth=1.5)
        ax.add_patch(task_rect)
        ax.text(1.75, y, label, fontsize=7, ha='center', va='center', color=color, weight='bold')
    else:
        ax.text(1.75, y, label, fontsize=12, ha='center', color=color, weight='bold')

ax.text(1.75, 5.7, 'P = Priority', fontsize=6, ha='center', style='italic', color='#666')
ax.text(1.75, 5.5, 'Pending tasks', fontsize=7, ha='center', style='italic', color='#1976D2')
ax.text(1.75, 5.3, 'awaiting execution', fontsize=7, ha='center', style='italic', color='#1976D2')

# ===== SCHEDULER (CENTER) =====
scheduler_box = FancyBboxPatch((4.0, 5.0), 3.0, 3.0,
                              boxstyle="round,pad=0.1", 
                              edgecolor='#9C27B0', facecolor='#F3E5F5',
                              linewidth=4)
ax.add_patch(scheduler_box)
ax.text(5.5, 7.75, 'SCHEDULER', fontsize=13, ha='center', weight='bold', color='#9C27B0')
ax.text(5.5, 7.5, '(Orchestrator)', fontsize=10, ha='center', style='italic', color='#9C27B0')

ax.text(4.2, 7.2, '• Dequeues tasks', fontsize=7, ha='left', color='#9C27B0')
ax.text(4.2, 7.0, '• Applies policy', fontsize=7, ha='left', weight='bold', color='#FF5722')
ax.text(4.2, 6.8, '• Controls timing', fontsize=7, ha='left', color='#9C27B0')
ax.text(4.2, 6.6, '• Manages resources', fontsize=7, ha='left', color='#9C27B0')

# Scheduling policies
policy_box = FancyBboxPatch((4.2, 5.5), 2.6, 0.8,
                           boxstyle="round,pad=0.03", 
                           edgecolor='#FF5722', facecolor='#FFEBEE',
                           linewidth=2)
ax.add_patch(policy_box)
ax.text(5.5, 6.15, 'Policies:', fontsize=8, ha='center', weight='bold', color='#FF5722')
ax.text(4.3, 5.95, '• FIFO, Priority', fontsize=6, ha='left', color='#FF5722')
ax.text(4.3, 5.80, '• Time-based', fontsize=6, ha='left', color='#FF5722')
ax.text(4.3, 5.65, '• Concurrency limit', fontsize=6, ha='left', color='#FF5722')

# ===== EXECUTION =====
exec_box = FancyBboxPatch((8.0, 5.0), 2.5, 3.0,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#4CAF50', facecolor='#E8F5E9',
                         linewidth=3)
ax.add_patch(exec_box)
ax.text(9.25, 7.85, 'EXECUTION', fontsize=12, ha='center', weight='bold', color='#2E7D32')

# Running tasks
running_tasks = [
    ('Running: Task A', 7.5, '#F44336'),
    ('Running: Task C', 7.0, '#FF5722')
]

for label, y, color in running_tasks:
    task_rect = FancyBboxPatch((8.2, y - 0.12), 2.1, 0.24,
                              boxstyle="round,pad=0.02", 
                              edgecolor=color, facecolor='#FFFFCC',
                              linewidth=1.5)
    ax.add_patch(task_rect)
    ax.text(9.25, y, label, fontsize=7, ha='center', va='center', color=color, weight='bold')

ax.text(9.25, 6.5, 'Max: 2 concurrent', fontsize=7, ha='center', style='italic', color='#2E7D32')
ax.text(9.25, 6.3, '(Concurrency limit)', fontsize=7, ha='center', style='italic', color='#2E7D32')

# Completed indicator
ax.text(9.25, 5.9, 'Completed:', fontsize=7, ha='center', weight='bold', color='#666')
ax.text(9.25, 5.7, '✓ Task X', fontsize=6, ha='center', color='#4CAF50')
ax.text(9.25, 5.5, '✓ Task Y', fontsize=6, ha='center', color='#4CAF50')
ax.text(9.25, 5.3, '...', fontsize=8, ha='center', color='#666')

# ===== COMPLETED TASKS =====
completed_box = FancyBboxPatch((11.0, 5.0), 2.5, 3.0,
                              boxstyle="round,pad=0.05", 
                              edgecolor='#4CAF50', facecolor='#E8F5E9',
                              linewidth=2, linestyle='dashed')
ax.add_patch(completed_box)
ax.text(12.25, 7.85, 'COMPLETED', fontsize=11, ha='center', weight='bold', color='#2E7D32')
ax.text(11.2, 7.5, '✓ Task X', fontsize=7, ha='left', color='#4CAF50')
ax.text(11.2, 7.3, '✓ Task Y', fontsize=7, ha='left', color='#4CAF50')
ax.text(11.2, 7.1, '✓ Task Z', fontsize=7, ha='left', color='#4CAF50')
ax.text(12.25, 6.7, '...', fontsize=10, ha='center', color='#666')

ax.text(12.25, 6.3, 'Results stored/', fontsize=7, ha='center', style='italic', color='#2E7D32')
ax.text(12.25, 6.1, 'callbacks invoked', fontsize=7, ha='center', style='italic', color='#2E7D32')

# ===== ARROWS =====

# 1. Queue → Scheduler
arrow1 = FancyArrowPatch((3.0, 6.5), (4.0, 6.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color='#2196F3', linewidth=3)
ax.add_patch(arrow1)
ax.text(3.5, 6.75, '1. dequeue', fontsize=8, ha='center', weight='bold', color='#2196F3')

# 2. Scheduler → Execution
arrow2 = FancyArrowPatch((7.0, 6.5), (8.0, 6.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color='#9C27B0', linewidth=3)
ax.add_patch(arrow2)
ax.text(7.5, 6.75, '2. execute', fontsize=8, ha='center', weight='bold', color='#9C27B0')

# 3. Execution → Completed
arrow3 = FancyArrowPatch((10.5, 6.5), (11.0, 6.5),
                        arrowstyle='->,head_width=0.4,head_length=0.6',
                        color='#4CAF50', linewidth=3)
ax.add_patch(arrow3)
ax.text(10.75, 6.75, '3. done', fontsize=8, ha='center', weight='bold', color='#4CAF50')

# ===== SCHEDULING POLICIES =====
policies_box = FancyBboxPatch((0.3, 2.0), 6.4, 2.7,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#666', facecolor='#FAFAFA',
                             linewidth=1.5)
ax.add_patch(policies_box)
ax.text(3.5, 4.55, 'Scheduling Policies', fontsize=11, ha='center', weight='bold')

policies = [
    ('1. FIFO (First-In-First-Out)', 'Execute in arrival order', 4.25, '#2196F3'),
    ('2. Priority', 'High priority first (min heap)', 3.95, '#FF5722'),
    ('3. Time-based', 'Execute at scheduled time', 3.65, '#FFC107'),
    ('4. Concurrency-limited', 'Max N tasks concurrently', 3.35, '#4CAF50'),
    ('5. Round-robin', 'Fair time slices', 3.05, '#9C27B0'),
    ('6. Deadline-based', 'Earliest deadline first', 2.75, '#E91E63')
]

for name, desc, y, color in policies:
    ax.text(0.5, y, name, fontsize=8, ha='left', weight='bold', color=color)
    ax.text(0.7, y - 0.15, desc, fontsize=6, ha='left', style='italic', color='#666')

# ===== BROWSER TASK QUEUES =====
browser_box = FancyBboxPatch((7.3, 2.0), 6.4, 2.7,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#666', facecolor='#FAFAFA',
                            linewidth=1.5)
ax.add_patch(browser_box)
ax.text(10.5, 4.55, 'Browser Task Queues (Scheduler)', fontsize=11, ha='center', weight='bold')

browser_queues = [
    ('Microtask Queue', 'Promise.then, queueMicrotask', 4.20, '#E91E63'),
    ('  → Runs after current task', '', 4.05, '#666'),
    ('Macrotask Queue', 'setTimeout, setInterval, I/O', 3.75, '#2196F3'),
    ('  → Next event loop iteration', '', 3.60, '#666'),
    ('Animation Queue', 'requestAnimationFrame', 3.30, '#4CAF50'),
    ('  → Before next paint', '', 3.15, '#666'),
    ('Idle Queue', 'requestIdleCallback', 2.85, '#9C27B0'),
    ('  → When browser is idle', '', 2.70, '#666')
]

for label, desc, y, color in browser_queues:
    if desc:
        ax.text(7.5, y, label, fontsize=7, ha='left', weight='bold', color=color)
        ax.text(7.7, y - 0.1, desc, fontsize=6, ha='left', style='italic', color='#666')
    else:
        ax.text(7.5, y, label, fontsize=6, ha='left', style='italic', color=color)

# ===== FLOW =====
flow_box = FancyBboxPatch((0.3, 0.1), 13.4, 1.7,
                         boxstyle="round,pad=0.05", 
                         edgecolor='#666', facecolor='#FAFAFA',
                         linewidth=1.5)
ax.add_patch(flow_box)
ax.text(7, 1.7, 'Scheduler Flow', fontsize=10, ha='center', weight='bold')

flow_steps = [
    ('1', 'Tasks arrive, enqueued', 1.45, '#2196F3'),
    ('2', 'Scheduler dequeues based on POLICY', 1.25, '#FF5722'),
    ('3', 'Task executed (respecting concurrency limit)', 1.05, '#9C27B0'),
    ('4', 'Task completes → result stored/callback invoked', 0.85, '#4CAF50'),
    ('5', 'Repeat: Scheduler picks next task', 0.65, '#9C27B0')
]

for num, text, y, color in flow_steps:
    ax.text(0.5, y, num, fontsize=8, ha='center', weight='bold',
           bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=1.5))
    ax.text(1.0, y, text, fontsize=7, ha='left', color=color)

# Key benefits
benefits = [
    ('✓ Control execution order (priority)', 0.40, '#4CAF50'),
    ('✓ Resource management (concurrency)', 0.25, '#4CAF50')
]

for text, y, color in benefits:
    ax.text(0.5, y, text, fontsize=7, ha='left', color=color, weight='bold')

# Key principle
principle_box = FancyBboxPatch((0.5, 0.2), 13.0, 0.2,
                              boxstyle="round,pad=0.03", 
                              edgecolor='#9C27B0', facecolor='#F3E5F5',
                              linewidth=2)
ax.add_patch(principle_box)
ax.text(7, 0.3, 'Key: Don\'t execute immediately; queue tasks and control WHEN & HOW they run (policy-driven execution)', 
       fontsize=7, ha='center', weight='bold', color='#9C27B0')

plt.tight_layout()
plt.savefig('docs/images/scheduler_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Scheduler Pattern diagram generated: docs/images/scheduler_pattern.png")

