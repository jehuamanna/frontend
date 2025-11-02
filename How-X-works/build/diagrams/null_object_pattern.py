#!/usr/bin/env python3
# ./build/diagrams/null_object_pattern.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Null Object Pattern', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Avoiding null Checks with Default Do-Nothing Behavior',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= WITHOUT Null Object (Lots of checks) =============
ax.text(2.5, 8.2, 'Without Null Object:', fontsize=11, weight='bold', color='#dc2626')

bad_client = FancyBboxPatch((0.5, 5.5), 4, 2.3,
                             boxstyle="round,pad=0.1",
                             edgecolor='#dc2626', facecolor='#fee2e2', linewidth=2)
ax.add_patch(bad_client)
ax.text(2.5, 7.5, 'Client (Lots of Checks)', fontsize=10, weight='bold', ha='center', color='#7f1d1d')

bad_code = """if (logger != null) {
  logger.log("msg");
}

if (user != null) {
  user.getName();
} else {
  return "Guest";
}"""

ax.text(0.7, 7.2, bad_code, fontsize=7, ha='left', va='top', family='monospace', color='#991b1b')

ax.text(2.5, 5.2, '❌ Verbose code', fontsize=8, ha='center', color='#7f1d1d')
ax.text(2.5, 4.9, '❌ Error-prone', fontsize=8, ha='center', color='#7f1d1d')
ax.text(2.5, 4.6, '❌ Repeated checks', fontsize=8, ha='center', color='#7f1d1d')

# ============= WITH Null Object =============
ax.text(10, 8.2, 'With Null Object:', fontsize=11, weight='bold', color='#059669')

# Interface/Abstract
interface_box = FancyBboxPatch((6, 6.5), 3, 1.2,
                                boxstyle="round,pad=0.1",
                                edgecolor='#3b82f6', facecolor='#dbeafe', linewidth=2)
ax.add_patch(interface_box)
ax.text(7.5, 7.4, '«interface» Logger', fontsize=10, weight='bold', ha='center', color='#1e40af')
ax.text(7.5, 7.05, 'log(message)', fontsize=8, ha='center', family='monospace', style='italic')

# Real Object
real_box = FancyBboxPatch((5, 4.5), 2.5, 1.5,
                           boxstyle="round,pad=0.1",
                           edgecolor='#10b981', facecolor='#d1fae5', linewidth=2)
ax.add_patch(real_box)
ax.text(6.25, 5.7, 'ConsoleLogger', fontsize=10, weight='bold', ha='center', color='#047857')
ax.text(6.25, 5.35, 'log(msg) {', fontsize=7, ha='center', family='monospace')
ax.text(6.25, 5.1, '  console.log(msg)', fontsize=7, ha='center', family='monospace', color='#047857')
ax.text(6.25, 4.85, '}', fontsize=7, ha='center', family='monospace')

# Null Object
null_box = FancyBboxPatch((8.5, 4.5), 2.5, 1.5,
                           boxstyle="round,pad=0.1",
                           edgecolor='#8b5cf6', facecolor='#f3e8ff', linewidth=2.5)
ax.add_patch(null_box)
ax.text(9.75, 5.7, 'NullLogger', fontsize=10, weight='bold', ha='center', color='#6b21a8')
ax.text(9.75, 5.35, 'log(msg) {', fontsize=7, ha='center', family='monospace')
ax.text(9.75, 5.1, '  // do nothing', fontsize=7, ha='center', family='monospace', color='#6b21a8', style='italic')
ax.text(9.75, 4.85, '}', fontsize=7, ha='center', family='monospace')

# Inheritance arrows
arrow1 = FancyArrowPatch((6.25, 6), (7.5, 6.5),
                         arrowstyle='->', mutation_scale=15,
                         linewidth=2, color='#10b981', linestyle='dashed')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((9.75, 6), (7.5, 6.5),
                         arrowstyle='->', mutation_scale=15,
                         linewidth=2, color='#8b5cf6', linestyle='dashed')
ax.add_patch(arrow2)

ax.text(5.5, 6.2, 'implements', fontsize=7, ha='center', style='italic', color='#047857')
ax.text(9.5, 6.2, 'implements', fontsize=7, ha='center', style='italic', color='#6b21a8')

# Clean Client
clean_client = FancyBboxPatch((9.5, 1.5), 4, 2.5,
                               boxstyle="round,pad=0.1",
                               edgecolor='#059669', facecolor='#d1fae5', linewidth=2)
ax.add_patch(clean_client)
ax.text(11.5, 3.7, 'Client (No Checks!)', fontsize=10, weight='bold', ha='center', color='#047857')

clean_code = """const logger = 
  hasLogging 
    ? new ConsoleLogger()
    : new NullLogger();

// Always safe to call
logger.log("message");

// No null check needed!"""

ax.text(9.7, 3.4, clean_code, fontsize=7, ha='left', va='top', family='monospace', color='#047857')

# Arrow from client to logger
arrow_use = FancyArrowPatch((10.5, 4), (9.75, 4.5),
                            arrowstyle='->', mutation_scale=15,
                            linewidth=1.5, color='#059669', linestyle='dashed')
ax.add_patch(arrow_use)
ax.text(10, 4.3, 'uses', fontsize=7, ha='center', style='italic', color='#047857')

ax.text(11.5, 1.2, '✅ Clean code', fontsize=8, ha='center', color='#047857')
ax.text(11.5, 0.9, '✅ No null checks', fontsize=8, ha='center', color='#047857')
ax.text(11.5, 0.6, '✅ Safe defaults', fontsize=8, ha='center', color='#047857')

# ============= Use Cases =============
usecases_box = FancyBboxPatch((0.5, 0.1), 5.5, 3.5,
                               boxstyle="round,pad=0.1",
                               edgecolor='#6366f1', facecolor='#eef2ff', linewidth=1.5)
ax.add_patch(usecases_box)
ax.text(3.25, 3.45, 'Common Use Cases:', fontsize=10, weight='bold', ha='center', color='#4338ca')

usecases = """• Logging (NullLogger)
  Production: ConsoleLogger
  Testing: NullLogger (silent)

• Strategies (NullStrategy)
  Default: DoNothingStrategy

• Callbacks (NullCallback)
  Optional callbacks without checks

• Collections (NullCollection)
  Empty collection operations

• UI Components (NullComponent)
  Placeholder components"""

ax.text(0.7, 3.2, usecases, fontsize=7, ha='left', va='top', family='sans-serif')

# ============= Example Box =============
example_box = FancyBboxPatch((0.5, 4.2), 4, 1.1,
                              boxstyle="round,pad=0.1",
                              edgecolor='#f59e0b', facecolor='#fef3c7', linewidth=1.5)
ax.add_patch(example_box)

example = """Other Examples:
• NullUser (Guest user)  •  • NullTask (no-op task)
• NullAnimation (instant)  •  • NullValidator (always valid)"""

ax.text(0.7, 5.1, example, fontsize=7, ha='left', va='top')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#dbeafe', edgecolor='#3b82f6', label='Interface/Abstract'),
    mpatches.Patch(facecolor='#d1fae5', edgecolor='#10b981', label='Real Implementation'),
    mpatches.Patch(facecolor='#f3e8ff', edgecolor='#8b5cf6', label='Null Object (Do Nothing)'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=9, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/null_object_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Null Object Pattern diagram generated successfully")

