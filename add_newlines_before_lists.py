#!/usr/bin/env python3
"""
Add blank lines before list items in markdown files.
This ensures proper rendering and readability.
"""

import re
import sys

def is_list_item(line):
    """Check if a line is a list item."""
    stripped = line.lstrip()
    
    # Unordered list: starts with -, *, or +
    if re.match(r'^[-*+]\s', stripped):
        return True
    
    # Ordered list: starts with number followed by . or )
    if re.match(r'^\d+[.)]\s', stripped):
        return True
    
    return False

def is_blank_line(line):
    """Check if a line is blank or whitespace only."""
    return line.strip() == ''

def is_code_fence(line):
    """Check if line is a code fence."""
    return line.strip().startswith('```')

def add_newlines_before_lists(content):
    """Add blank lines before list items if not already present."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    
    for i, line in enumerate(lines):
        # Track code blocks
        if is_code_fence(line):
            in_code_block = not in_code_block
            result.append(line)
            continue
        
        # Don't modify lines inside code blocks
        if in_code_block:
            result.append(line)
            continue
        
        # Check if current line is a list item
        if is_list_item(line):
            # Check if previous line exists and is not blank
            if i > 0 and not is_blank_line(lines[i-1]):
                # Also check that previous line is not a list item (to avoid breaking existing lists)
                if not is_list_item(lines[i-1]):
                    # Add a blank line before this list item
                    result.append('')
        
        result.append(line)
    
    return '\n'.join(result)

def process_file(input_file, output_file=None):
    """Process the markdown file."""
    if output_file is None:
        output_file = input_file
    
    print(f"Reading: {input_file}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Original lines: {len(content.split(chr(10)))}")
    
    # Add newlines before lists
    modified_content = add_newlines_before_lists(content)
    
    print(f"Modified lines: {len(modified_content.split(chr(10)))}")
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"Output written to: {output_file}")
    
    # Calculate changes
    original_lines = len(content.split('\n'))
    modified_lines = len(modified_content.split('\n'))
    added_lines = modified_lines - original_lines
    
    print(f"Added {added_lines} blank lines before list items")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 add_newlines_before_lists.py <input_file> [output_file]")
        print("If output_file is not specified, input_file will be modified in place.")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    process_file(input_file, output_file)

if __name__ == '__main__':
    main()

