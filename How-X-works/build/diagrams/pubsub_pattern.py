import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'Publish/Subscribe Pattern Architecture', 
        fontsize=20, weight='bold', ha='center')
ax.text(7, 9.0, 'Complete decoupling via event bus: publishers and subscribers don\'t know each other',
        fontsize=11, ha='center', style='italic', color='#555')

# Color scheme
color_publisher = '#FFE5CC'
color_subscriber = '#B8E6F0'
color_eventbus = '#FFF3B0'
color_topic = '#E8D4F8'

# ===== EVENT BUS (CENTER) =====
eventbus_box = FancyBboxPatch((5.0, 4.0), 4.0, 2.5,
                             boxstyle="round,pad=0.1", 
                             edgecolor='#F77F00', facecolor=color_eventbus,
                             linewidth=3)
ax.add_patch(eventbus_box)
ax.text(7.0, 6.2, 'Event Bus', fontsize=14, ha='center', weight='bold')
ax.text(7.0, 5.9, '(Message Broker)', fontsize=10, ha='center', style='italic', color='#666')
ax.text(7.0, 5.55, 'topics: Map<string, Subscriber[]>', fontsize=9, ha='center', family='monospace', color='#555')
ax.text(7.0, 5.2, 'subscribe(topic, callback)', fontsize=10, ha='center', family='monospace')
ax.text(7.0, 4.85, 'publish(topic, data)', fontsize=10, ha='center', family='monospace')
ax.text(7.0, 4.5, 'unsubscribe(topic, callback)', fontsize=10, ha='center', family='monospace')
ax.text(7.0, 4.15, '★ Routes messages', fontsize=9, ha='center', style='italic', color='#F77F00')

# ===== TOPICS =====
topic_y = 6.7
topics = [('user:login', 2.5), ('cart:update', 5.0), ('order:placed', 7.5), ('payment:success', 10.0)]

for topic, x in topics:
    topic_box = FancyBboxPatch((x - 0.8, topic_y), 1.6, 0.5,
                              boxstyle="round,pad=0.05", 
                              edgecolor='#9D4EDD', facecolor=color_topic,
                              linewidth=1.5)
    ax.add_patch(topic_box)
    ax.text(x, topic_y + 0.25, topic, fontsize=8, ha='center', family='monospace', weight='bold')

ax.text(7.0, topic_y + 0.8, 'Topics/Channels', fontsize=11, ha='center', weight='bold', color='#9D4EDD')

# ===== PUBLISHERS (LEFT) =====
publishers = [
    ('PublisherA', 'UserService', 1.5, 2.8),
    ('PublisherB', 'CartService', 1.5, 1.3),
    ('PublisherC', 'OrderService', 1.5, 0.0)
]

for name, desc, x, y in publishers:
    pub_box = FancyBboxPatch((x - 0.8, y), 1.6, 0.9,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#E63946', facecolor=color_publisher,
                            linewidth=2)
    ax.add_patch(pub_box)
    ax.text(x, y + 0.65, name, fontsize=9, ha='center', weight='bold')
    ax.text(x, y + 0.45, desc, fontsize=7, ha='center', style='italic', color='#666')
    ax.text(x, y + 0.2, 'publish()', fontsize=8, ha='center', family='monospace')

ax.text(1.5, 3.9, 'Publishers', fontsize=11, ha='center', weight='bold', color='#E63946')
ax.text(1.5, 3.6, '(Don\'t know subscribers)', fontsize=8, ha='center', style='italic', color='#E63946')

# ===== SUBSCRIBERS (RIGHT) =====
subscribers = [
    ('SubscriberA', 'Analytics', 12.5, 2.8),
    ('SubscriberB', 'UI Updates', 12.5, 1.8),
    ('SubscriberC', 'Notifications', 12.5, 0.8),
    ('SubscriberD', 'Logger', 12.5, -0.2)
]

for name, desc, x, y in subscribers:
    sub_box = FancyBboxPatch((x - 0.8, y), 1.6, 0.8,
                            boxstyle="round,pad=0.05", 
                            edgecolor='#2E86AB', facecolor=color_subscriber,
                            linewidth=2)
    ax.add_patch(sub_box)
    ax.text(x, y + 0.58, name, fontsize=9, ha='center', weight='bold')
    ax.text(x, y + 0.38, desc, fontsize=7, ha='center', style='italic', color='#666')
    ax.text(x, y + 0.15, 'subscribe()', fontsize=8, ha='center', family='monospace')

ax.text(12.5, 3.9, 'Subscribers', fontsize=11, ha='center', weight='bold', color='#2E86AB')
ax.text(12.5, 3.6, '(Don\'t know publishers)', fontsize=8, ha='center', style='italic', color='#2E86AB')

# ===== ARROWS: Publishers to Event Bus =====
arrow1 = FancyArrowPatch((2.3, 3.2), (5.0, 5.2),
                        arrowstyle='->', mutation_scale=20, 
                        color='#E63946', linewidth=2)
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((2.3, 1.7), (5.0, 4.8),
                        arrowstyle='->', mutation_scale=20, 
                        color='#E63946', linewidth=2)
ax.add_patch(arrow2)

arrow3 = FancyArrowPatch((2.3, 0.4), (5.0, 4.5),
                        arrowstyle='->', mutation_scale=20, 
                        color='#E63946', linewidth=2)
ax.add_patch(arrow3)

ax.text(3.5, 4.5, 'publish(topic, data)', fontsize=8, style='italic', color='#E63946')

# ===== ARROWS: Event Bus to Subscribers =====
arrow4 = FancyArrowPatch((9.0, 5.2), (11.7, 3.2),
                        arrowstyle='->', mutation_scale=20, 
                        color='#2E86AB', linewidth=2)
ax.add_patch(arrow4)

arrow5 = FancyArrowPatch((9.0, 5.0), (11.7, 2.2),
                        arrowstyle='->', mutation_scale=20, 
                        color='#2E86AB', linewidth=2)
ax.add_patch(arrow5)

arrow6 = FancyArrowPatch((9.0, 4.7), (11.7, 1.2),
                        arrowstyle='->', mutation_scale=20, 
                        color='#2E86AB', linewidth=2)
ax.add_patch(arrow6)

arrow7 = FancyArrowPatch((9.0, 4.4), (11.7, 0.2),
                        arrowstyle='->', mutation_scale=20, 
                        color='#2E86AB', linewidth=2)
ax.add_patch(arrow7)

ax.text(10.5, 4.5, 'notify(data)', fontsize=8, style='italic', color='#2E86AB')

# ===== COMPARISON: OBSERVER VS PUB/SUB =====
comp_y = 8.3

# Observer
obs_box = FancyBboxPatch((0.5, comp_y - 0.3), 3.0, 0.7,
                        boxstyle="round,pad=0.05", 
                        edgecolor='#C41E3A', facecolor='#FFE5E5',
                        linewidth=1.5)
ax.add_patch(obs_box)
ax.text(2.0, comp_y + 0.2, 'Observer Pattern', fontsize=10, ha='center', weight='bold', color='#C41E3A')
ax.text(2.0, comp_y - 0.05, 'Subject → Observer (Direct)', fontsize=8, ha='center', color='#C41E3A')

# Arrow showing direct connection
arrow_obs = FancyArrowPatch((1.2, comp_y - 0.05), (2.8, comp_y - 0.05),
                           arrowstyle='<->', mutation_scale=12, 
                           color='#C41E3A', linewidth=1.5)
ax.add_patch(arrow_obs)

# Pub/Sub
pubsub_box = FancyBboxPatch((10.5, comp_y - 0.3), 3.0, 0.7,
                           boxstyle="round,pad=0.05", 
                           edgecolor='#2E7D32', facecolor='#E8F5E9',
                           linewidth=1.5)
ax.add_patch(pubsub_box)
ax.text(12.0, comp_y + 0.2, 'Pub/Sub Pattern', fontsize=10, ha='center', weight='bold', color='#2E7D32')
ax.text(12.0, comp_y - 0.05, 'Pub → Bus → Sub (Decoupled)', fontsize=8, ha='center', color='#2E7D32')

# Arrow showing event bus in middle
circle1 = Circle((11.3, comp_y - 0.05), 0.1, facecolor='#2E7D32', edgecolor='#2E7D32')
ax.add_patch(circle1)
arrow_pub1 = FancyArrowPatch((11.0, comp_y - 0.05), (11.2, comp_y - 0.05),
                            arrowstyle='->', mutation_scale=10, 
                            color='#2E7D32', linewidth=1.5)
ax.add_patch(arrow_pub1)
arrow_pub2 = FancyArrowPatch((11.4, comp_y - 0.05), (11.9, comp_y - 0.05),
                            arrowstyle='->', mutation_scale=10, 
                            color='#2E7D32', linewidth=1.5)
ax.add_patch(arrow_pub2)
ax.text(11.3, comp_y - 0.35, 'Bus', fontsize=7, ha='center', color='#2E7D32')

# ===== KEY BENEFITS =====
benefits_box = FancyBboxPatch((4.0, 7.8), 6.0, 0.8,
                             boxstyle="round,pad=0.05", 
                             edgecolor='#2E7D32', facecolor='#E8F5E9',
                             linewidth=1)
ax.add_patch(benefits_box)
ax.text(7.0, 8.45, 'Key Benefits of Pub/Sub', fontsize=10, ha='center', weight='bold', color='#2E7D32')
ax.text(4.3, 8.15, '✓ Complete decoupling', fontsize=8, ha='left', color='#2E7D32')
ax.text(4.3, 7.95, '✓ Many-to-many', fontsize=8, ha='left', color='#2E7D32')
ax.text(6.5, 8.15, '✓ Topic-based filtering', fontsize=8, ha='left', color='#2E7D32')
ax.text(6.5, 7.95, '✓ Dynamic subscriptions', fontsize=8, ha='left', color='#2E7D32')
ax.text(8.7, 8.15, '✓ Scalable', fontsize=8, ha='left', color='#2E7D32')
ax.text(8.7, 7.95, '✓ Flexible routing', fontsize=8, ha='left', color='#2E7D32')

plt.tight_layout()
plt.savefig('docs/images/pubsub_pattern.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Pub/Sub Pattern diagram generated: docs/images/pubsub_pattern.png")

