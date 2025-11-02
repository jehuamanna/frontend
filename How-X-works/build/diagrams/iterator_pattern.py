import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Iterator Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Sequential access to collection elements without exposing internal structure',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_interface = '#E8F4F8'
color_concrete = '#B8E6F0'
color_client = '#FFE5CC'
color_collection = '#D4E8D4'

# ===== ITERATOR INTERFACE =====
iterator_interface = FancyBboxPatch((0.5, 6.5), 2.5, 1.8,
                                   boxstyle="round,pad=0.1", 
                                   edgecolor='#2E86AB', facecolor=color_interface,
                                   linewidth=2, linestyle='--')
ax.add_patch(iterator_interface)
ax.text(1.75, 8.0, '«interface»', fontsize=9, ha='center', style='italic', color='#2E86AB')
ax.text(1.75, 7.7, 'Iterator', fontsize=12, ha='center', weight='bold')
ax.text(1.75, 7.3, 'next()', fontsize=10, ha='center', family='monospace')
ax.text(1.75, 7.0, 'hasNext()', fontsize=10, ha='center', family='monospace')

# ===== CONCRETE ITERATOR =====
concrete_iterator = FancyBboxPatch((0.5, 4.0), 2.5, 1.8,
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#2E86AB', facecolor=color_concrete,
                                  linewidth=2)
ax.add_patch(concrete_iterator)
ax.text(1.75, 5.5, 'ConcreteIterator', fontsize=12, ha='center', weight='bold')
ax.text(1.75, 5.1, 'collection', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(1.75, 4.8, 'currentIndex', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(1.75, 4.5, 'next()', fontsize=10, ha='center', family='monospace')
ax.text(1.75, 4.2, 'hasNext()', fontsize=10, ha='center', family='monospace')

# ===== ITERABLE INTERFACE =====
iterable_interface = FancyBboxPatch((5.0, 6.5), 3.0, 1.8,
                                   boxstyle="round,pad=0.1", 
                                   edgecolor='#52B788', facecolor=color_interface,
                                   linewidth=2, linestyle='--')
ax.add_patch(iterable_interface)
ax.text(6.5, 8.0, '«interface»', fontsize=9, ha='center', style='italic', color='#52B788')
ax.text(6.5, 7.7, 'Iterable', fontsize=12, ha='center', weight='bold')
ax.text(6.5, 7.3, '[Symbol.iterator]()', fontsize=10, ha='center', family='monospace')
ax.text(6.5, 7.0, 'returns Iterator', fontsize=9, ha='center', style='italic', color='#555')

# ===== CONCRETE COLLECTION =====
concrete_collection = FancyBboxPatch((5.0, 4.0), 3.0, 1.8,
                                    boxstyle="round,pad=0.1", 
                                    edgecolor='#52B788', facecolor=color_collection,
                                    linewidth=2)
ax.add_patch(concrete_collection)
ax.text(6.5, 5.5, 'ConcreteCollection', fontsize=12, ha='center', weight='bold')
ax.text(6.5, 5.1, 'items[]', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(6.5, 4.8, '[Symbol.iterator]()', fontsize=10, ha='center', family='monospace')
ax.text(6.5, 4.5, 'add(item)', fontsize=9, ha='center', family='monospace')
ax.text(6.5, 4.2, 'remove(item)', fontsize=9, ha='center', family='monospace')

# ===== CLIENT =====
client_box = FancyBboxPatch((10.0, 5.5), 2.8, 2.0,
                           boxstyle="round,pad=0.1", 
                           edgecolor='#F77F00', facecolor=color_client,
                           linewidth=2)
ax.add_patch(client_box)
ax.text(11.4, 7.2, 'Client', fontsize=12, ha='center', weight='bold')
ax.text(11.4, 6.8, 'Uses Iterator', fontsize=9, ha='center', style='italic', color='#555')
ax.text(11.4, 6.4, 'for (item of collection)', fontsize=9, ha='center', family='monospace')
ax.text(11.4, 6.0, '  process(item)', fontsize=9, ha='center', family='monospace')

# ===== GENERATOR (ALTERNATIVE) =====
generator_box = FancyBboxPatch((0.5, 1.0), 3.5, 2.0,
                              boxstyle="round,pad=0.1", 
                              edgecolor='#9D4EDD', facecolor='#F3E5F5',
                              linewidth=2)
ax.add_patch(generator_box)
ax.text(2.25, 2.7, 'Generator Function', fontsize=12, ha='center', weight='bold')
ax.text(2.25, 2.3, 'function* generator()', fontsize=10, ha='center', family='monospace')
ax.text(2.25, 1.9, '  yield value1', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(2.25, 1.6, '  yield value2', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(2.25, 1.3, '  yield value3', fontsize=9, ha='center', family='monospace', color='#555')

# ===== ASYNC ITERATOR (MODERN) =====
async_iterator = FancyBboxPatch((5.0, 1.0), 4.0, 2.0,
                               boxstyle="round,pad=0.1", 
                               edgecolor='#06AED5', facecolor='#E0F7FA',
                               linewidth=2)
ax.add_patch(async_iterator)
ax.text(7.0, 2.7, 'Async Iterator', fontsize=12, ha='center', weight='bold')
ax.text(7.0, 2.35, '[Symbol.asyncIterator]()', fontsize=10, ha='center', family='monospace')
ax.text(7.0, 2.0, 'async next()', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(7.0, 1.65, 'Promise<{value, done}>', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(7.0, 1.3, 'for await...of', fontsize=9, ha='center', style='italic', color='#06AED5')

# ===== RELATIONSHIPS =====

# Iterator implements interface
arrow1 = FancyArrowPatch((1.75, 6.5), (1.75, 5.8),
                        arrowstyle='-|>', mutation_scale=20, 
                        color='#2E86AB', linewidth=2, linestyle='dashed')
ax.add_patch(arrow1)
ax.text(2.1, 6.1, 'implements', fontsize=8, style='italic', color='#2E86AB')

# Collection implements iterable
arrow2 = FancyArrowPatch((6.5, 6.5), (6.5, 5.8),
                        arrowstyle='-|>', mutation_scale=20, 
                        color='#52B788', linewidth=2, linestyle='dashed')
ax.add_patch(arrow2)
ax.text(6.9, 6.1, 'implements', fontsize=8, style='italic', color='#52B788')

# Collection creates iterator
arrow3 = FancyArrowPatch((5.0, 4.9), (3.0, 4.9),
                        arrowstyle='-|>', mutation_scale=20, 
                        color='#666', linewidth=2)
ax.add_patch(arrow3)
ax.text(4.0, 5.2, 'creates', fontsize=9, style='italic', color='#666')

# Iterator accesses collection
arrow4 = FancyArrowPatch((3.0, 4.5), (5.0, 4.5),
                        arrowstyle='->', mutation_scale=15, 
                        color='#999', linewidth=1.5, linestyle='dotted')
ax.add_patch(arrow4)
ax.text(4.0, 4.2, 'accesses', fontsize=8, style='italic', color='#999')

# Client uses iterator
arrow5 = FancyArrowPatch((10.0, 6.9), (8.0, 7.4),
                        arrowstyle='->', mutation_scale=20, 
                        color='#F77F00', linewidth=2)
ax.add_patch(arrow5)
ax.text(9.2, 7.5, 'uses', fontsize=9, style='italic', color='#F77F00')

# Client uses collection
arrow6 = FancyArrowPatch((10.0, 6.2), (8.0, 5.5),
                        arrowstyle='->', mutation_scale=20, 
                        color='#F77F00', linewidth=2)
ax.add_patch(arrow6)
ax.text(9.2, 6.0, 'uses', fontsize=9, style='italic', color='#F77F00')

# Generator is alternative
arrow7 = FancyArrowPatch((2.25, 3.0), (2.25, 4.0),
                        arrowstyle='<->', mutation_scale=15, 
                        color='#9D4EDD', linewidth=1.5, linestyle='dotted')
ax.add_patch(arrow7)
ax.text(2.7, 3.5, 'alternative', fontsize=8, style='italic', color='#9D4EDD')

# ===== KEY CONCEPTS BOX =====
concepts_box = FancyBboxPatch((10.0, 0.5), 3.5, 2.5,
                             boxstyle="round,pad=0.1", 
                             edgecolor='#666', facecolor='#FAFAFA',
                             linewidth=1.5, linestyle='dashed')
ax.add_patch(concepts_box)
ax.text(11.75, 2.7, 'Key Concepts', fontsize=11, ha='center', weight='bold')
ax.text(10.3, 2.3, '• Lazy evaluation', fontsize=9, ha='left')
ax.text(10.3, 2.0, '• Stateful traversal', fontsize=9, ha='left')
ax.text(10.3, 1.7, '• Multiple iterators', fontsize=9, ha='left')
ax.text(10.3, 1.4, '• Uniform interface', fontsize=9, ha='left')
ax.text(10.3, 1.1, '• Composition support', fontsize=9, ha='left')
ax.text(10.3, 0.8, '• Native JS support', fontsize=9, ha='left')

# ===== SEQUENCE FLOW =====
ax.text(7, 0.3, '1. Client calls collection[Symbol.iterator]() → 2. Returns Iterator → 3. Client calls next() repeatedly → 4. Iterator returns {value, done}',
        fontsize=8, ha='center', style='italic', color='#666',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF9E6', edgecolor='#FFD700', linewidth=1))

plt.tight_layout()
plt.savefig('docs/images/iterator_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Iterator Pattern diagram generated: docs/images/iterator_pattern.png")

