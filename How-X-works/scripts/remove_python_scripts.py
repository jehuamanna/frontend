#!/usr/bin/env python3
"""
Remove Python diagram scripts from master_output.md while keeping the images.
"""
import re

# Read the file
with open('master_output.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match:
# ### Python Architecture Diagram Snippet
# 
# ![Pattern Name](path)
# 
# *Figure: ...*
# 
# ```python
# ... (large code block) ...
# ```
pattern = r'(### Python Architecture Diagram Snippet\n\n!\[.*?\]\(.*?\)\n\n\*Figure:.*?\*)\n\n```python\n#.*?```'

# Replace with just the image and caption (rename section to "Architecture Diagram")
def replace_func(match):
    text = match.group(1)
    # Rename section
    text = text.replace('### Python Architecture Diagram Snippet', '### Architecture Diagram')
    return text

# Apply the replacement
new_content = re.sub(pattern, replace_func, content, flags=re.DOTALL)

# Write back
with open('master_output.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"✓ Removed Python scripts from master_output.md")
print(f"  Old size: {len(content)} characters")
print(f"  New size: {len(new_content)} characters")
print(f"  Saved: {len(content) - len(new_content)} characters")

