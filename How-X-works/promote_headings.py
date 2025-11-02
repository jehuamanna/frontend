#!/usr/bin/env python3
"""
Promote all heading levels in master_output.md:
- ## becomes #
- ### becomes ##
- #### becomes ###
- etc.
"""
import re

# Read the file
with open('master_output.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Check if line starts with heading markers
    if line.startswith('#'):
        # Count the number of # symbols
        heading_match = re.match(r'^(#+)\s', line)
        if heading_match:
            hashes = heading_match.group(1)
            # Promote by removing one #
            if len(hashes) > 1:
                new_line = line[1:]  # Remove one #
                new_lines.append(new_line)
            else:
                # Already level 1, keep as is
                new_lines.append(line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

# Write back
with open('master_output.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("✓ Promoted all heading levels in master_output.md")
print("  ## → #")
print("  ### → ##")
print("  #### → ###")

