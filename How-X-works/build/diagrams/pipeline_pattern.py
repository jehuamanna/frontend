import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(8, 9.5, 'Pipeline Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(8, 9.0, 'Modular Data Processing with Stage Composition',
        fontsize=12, ha='center', style='italic', color='gray')

# ============= Main Pipeline Flow =============
# Input
input_box = FancyBboxPatch((0.5, 6.5), 1.2, 1, 
                           boxstyle="round,pad=0.1", 
                           edgecolor='#2ecc71', facecolor='#ecf9f2', linewidth=2)
ax.add_patch(input_box)
ax.text(1.1, 7, 'Input\nData', fontsize=10, weight='bold', ha='center', va='center')

# Stage 1
stage1_box = FancyBboxPatch((3, 6.5), 2, 1, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='#3498db', facecolor='#ebf5fb', linewidth=2)
ax.add_patch(stage1_box)
ax.text(4, 7.3, 'Stage 1', fontsize=11, weight='bold', ha='center')
ax.text(4, 6.85, 'transform()', fontsize=9, ha='center', style='italic')

# Stage 2
stage2_box = FancyBboxPatch((6.5, 6.5), 2, 1, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='#3498db', facecolor='#ebf5fb', linewidth=2)
ax.add_patch(stage2_box)
ax.text(7.5, 7.3, 'Stage 2', fontsize=11, weight='bold', ha='center')
ax.text(7.5, 6.85, 'validate()', fontsize=9, ha='center', style='italic')

# Stage 3
stage3_box = FancyBboxPatch((10, 6.5), 2, 1, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='#3498db', facecolor='#ebf5fb', linewidth=2)
ax.add_patch(stage3_box)
ax.text(11, 7.3, 'Stage 3', fontsize=11, weight='bold', ha='center')
ax.text(11, 6.85, 'format()', fontsize=9, ha='center', style='italic')

# Output
output_box = FancyBboxPatch((13.5, 6.5), 1.2, 1, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=2)
ax.add_patch(output_box)
ax.text(14.1, 7, 'Output\nData', fontsize=10, weight='bold', ha='center', va='center')

# Arrows connecting stages
arrow1 = FancyArrowPatch((1.7, 7), (3, 7),
                        arrowstyle='->', mutation_scale=20, 
                        linewidth=2, color='#34495e')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((5, 7), (6.5, 7),
                        arrowstyle='->', mutation_scale=20, 
                        linewidth=2, color='#34495e')
ax.add_patch(arrow2)

arrow3 = FancyArrowPatch((8.5, 7), (10, 7),
                        arrowstyle='->', mutation_scale=20, 
                        linewidth=2, color='#34495e')
ax.add_patch(arrow3)

arrow4 = FancyArrowPatch((12, 7), (13.5, 7),
                        arrowstyle='->', mutation_scale=20, 
                        linewidth=2, color='#34495e')
ax.add_patch(arrow4)

# ============= Parallel Processing View =============
ax.text(1, 5.5, 'Parallel Pipeline Execution:', fontsize=11, weight='bold')

# Timeline showing parallel execution
# Time labels
for i, time in enumerate(['t0', 't1', 't2', 't3', 't4']):
    ax.text(2.5 + i * 2.5, 5.0, time, fontsize=9, ha='center', style='italic', color='gray')

# Stage execution blocks (showing pipeline parallelism)
# At t0: Item 1 in Stage 1
exec_block1 = FancyBboxPatch((2.2, 4.2), 0.6, 0.5, 
                             boxstyle="round,pad=0.02", 
                             edgecolor='#3498db', facecolor='#85c1e9', linewidth=1)
ax.add_patch(exec_block1)
ax.text(2.5, 4.45, 'S1', fontsize=8, ha='center', va='center', weight='bold')

# At t1: Item 1 in Stage 2, Item 2 in Stage 1
exec_block2 = FancyBboxPatch((4.7, 4.2), 0.6, 0.5, 
                             boxstyle="round,pad=0.02", 
                             edgecolor='#3498db', facecolor='#5dade2', linewidth=1)
ax.add_patch(exec_block2)
ax.text(5, 4.45, 'S2', fontsize=8, ha='center', va='center', weight='bold')

exec_block3 = FancyBboxPatch((4.7, 3.5), 0.6, 0.5, 
                             boxstyle="round,pad=0.02", 
                             edgecolor='#3498db', facecolor='#85c1e9', linewidth=1)
ax.add_patch(exec_block3)
ax.text(5, 3.75, 'S1', fontsize=8, ha='center', va='center', weight='bold')

# At t2: All 3 stages processing different items
exec_block4 = FancyBboxPatch((7.2, 4.2), 0.6, 0.5, 
                             boxstyle="round,pad=0.02", 
                             edgecolor='#3498db', facecolor='#3498db', linewidth=1)
ax.add_patch(exec_block4)
ax.text(7.5, 4.45, 'S3', fontsize=8, ha='center', va='center', weight='bold', color='white')

exec_block5 = FancyBboxPatch((7.2, 3.5), 0.6, 0.5, 
                             boxstyle="round,pad=0.02", 
                             edgecolor='#3498db', facecolor='#5dade2', linewidth=1)
ax.add_patch(exec_block5)
ax.text(7.5, 3.75, 'S2', fontsize=8, ha='center', va='center', weight='bold')

exec_block6 = FancyBboxPatch((7.2, 2.8), 0.6, 0.5, 
                             boxstyle="round,pad=0.02", 
                             edgecolor='#3498db', facecolor='#85c1e9', linewidth=1)
ax.add_patch(exec_block6)
ax.text(7.5, 3.05, 'S1', fontsize=8, ha='center', va='center', weight='bold')

# Labels for items
ax.text(1.3, 4.45, 'Item 1:', fontsize=8, ha='right', va='center')
ax.text(1.3, 3.75, 'Item 2:', fontsize=8, ha='right', va='center')
ax.text(1.3, 3.05, 'Item 3:', fontsize=8, ha='right', va='center')

# ============= Code Examples =============
ax.text(1, 2.2, 'Implementation Patterns:', fontsize=11, weight='bold')

# Functional pipeline
code_box1 = FancyBboxPatch((0.5, 0.3), 4.5, 1.6,
                           boxstyle="round,pad=0.1",
                           edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=1)
ax.add_patch(code_box1)
ax.text(2.75, 1.75, 'Functional Pipeline', fontsize=10, weight='bold', ha='center')
code1 = """const pipe = (...fns) =>
  input => fns.reduce(
    (acc, fn) => fn(acc),
    input
  );

const pipeline = pipe(
  transform,
  validate,
  format
);"""
ax.text(0.7, 1.5, code1, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Async iterator pipeline
code_box2 = FancyBboxPatch((5.5, 0.3), 4.5, 1.6,
                           boxstyle="round,pad=0.1",
                           edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=1)
ax.add_patch(code_box2)
ax.text(7.75, 1.75, 'Async Iterator Pipeline', fontsize=10, weight='bold', ha='center')
code2 = """async function* pipeline(
  source, ...stages
) {
  let result = source;
  for (const stage of stages) {
    result = stage(result);
  }
  yield* result;
}"""
ax.text(5.7, 1.5, code2, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Stream pipeline
code_box3 = FancyBboxPatch((10.5, 0.3), 4.5, 1.6,
                           boxstyle="round,pad=0.1",
                           edgecolor='#95a5a6', facecolor='#f8f9f9', linewidth=1)
ax.add_patch(code_box3)
ax.text(12.75, 1.75, 'Node.js Stream Pipeline', fontsize=10, weight='bold', ha='center')
code3 = """await pipeline(
  createReadStream('in.txt'),
  new TransformStream(),
  createGzip(),
  createWriteStream('out.gz')
);"""
ax.text(10.7, 1.5, code3, fontsize=7, ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#ebf5fb', edgecolor='#3498db', label='Pipeline Stage'),
    mpatches.Patch(facecolor='#ecf9f2', edgecolor='#2ecc71', label='Input'),
    mpatches.Patch(facecolor='#fadbd8', edgecolor='#e74c3c', label='Output'),
    mpatches.Patch(facecolor='#85c1e9', edgecolor='#3498db', label='Stage Execution')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=9, framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/images/pipeline_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Pipeline Pattern architecture diagram generated successfully")

