#!/usr/bin/env python3
"""
Replace Python code blocks in diagram sections with PNG references only
"""

import re
import os

def extract_pattern_name_from_code(code_block):
    """Extract pattern name from the Python code's filename comment or savefig call"""
    # Look for ./build/diagrams/<pattern>.py or docs/images/<pattern>.png
    match = re.search(r'docs/images/(\w+)\.png', code_block)
    if match:
        return match.group(1)
    
    match = re.search(r'diagrams/(\w+)\.py', code_block)
    if match:
        return match.group(1)
    
    return None

def main():
    with open('master_output.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find diagram sections with Python code
    # Match: ## Python Architecture Diagram Snippet OR ## Architecture Diagram
    #        followed by optional blank lines
    #        followed by ```python...``` block
    #        and capture what comes after
    
    sections_replaced = 0
    
    def replace_diagram_section(match):
        nonlocal sections_replaced
        header = match.group(1)  # The header line
        python_code = match.group(2)  # The Python code block content
        after_code = match.group(3)  # Content after the code block
        
        # Extract pattern name from code
        pattern_name = extract_pattern_name_from_code(python_code)
        
        if not pattern_name:
            # If we can't find pattern name, just remove the code
            sections_replaced += 1
            return f"{header}\n\n{after_code}"
        
        # Check if there's already a PNG reference in after_code
        if f'{pattern_name}.png' in after_code[:200]:  # Check first 200 chars
            # PNG reference already exists, just remove code
            sections_replaced += 1
            return f"{header}\n\n{after_code}"
        
        # Add PNG reference and remove code
        sections_replaced += 1
        png_ref = f"![{pattern_name.replace('_', ' ').title()} Architecture](docs/images/{pattern_name}.png)\n\n"
        
        return f"{header}\n\n{png_ref}{after_code}"
    
    # Regex pattern to match diagram sections with Python code
    pattern = r'(## (?:Python Architecture Diagram Snippet|Architecture Diagram)\n)\n```python\n(.*?)```\n\n(.*?)(?=\n## |\Z)'
    
    modified_content = re.sub(pattern, replace_diagram_section, content, flags=re.DOTALL)
    
    with open('master_output_with_png.md', 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"✓ Replaced {sections_replaced} Python code blocks with PNG references")
    
    # Count remaining code blocks
    remaining_python = len(re.findall(r'```python', modified_content))
    print(f"✓ Remaining Python code blocks (in examples): {remaining_python}")
    
    # Count PNG references
    png_refs = len(re.findall(r'!\[.*?\]\(docs/images/.*?\.png\)', modified_content))
    print(f"✓ Total PNG diagram references: {png_refs}")

if __name__ == '__main__':
    main()

