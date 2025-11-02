#!/usr/bin/env python3
"""
Script to add Python diagram code snippets to master_output.md
Finds empty "## Python Architecture Diagram Snippet" sections and adds the corresponding Python code.
"""

import re
import os
from pathlib import Path

def find_pattern_name_before_line(lines, line_num):
    """Find the pattern name by looking backward for ## CONTINUED: header"""
    for i in range(line_num - 1, max(0, line_num - 1000), -1):
        if lines[i].startswith('## CONTINUED:'):
            return lines[i]
    return None

def pattern_name_to_filename(pattern_header):
    """Convert pattern header to Python filename"""
    # Example: "# CONTINUED: Creational — Constructor Pattern" -> "constructor_pattern"
    if not pattern_header:
        return None
    
    # Extract pattern name after the em dash or hyphen
    match = re.search(r'[—-]\s*(.+)$', pattern_header)
    if not match:
        return None
    
    pattern_name = match.group(1).strip()
    
    # Convert to snake_case filename
    filename = pattern_name.lower()
    filename = filename.replace(' / ', '_')
    filename = filename.replace('/', '_')
    filename = filename.replace(' ', '_')
    filename = filename.replace('(', '')
    filename = filename.replace(')', '')
    filename = filename.replace('-', '_')
    filename = filename.replace('&', '')
    filename = filename.replace(',', '')
    
    # Add _pattern suffix if not present
    if not filename.endswith('_pattern'):
        filename = f"{filename}_pattern"
    
    # Special cases - check AFTER adding suffix
    mapping = {
        'observer_reactive_streams_pattern': 'observer_reactive_streams_pattern',
        'currying_partial_application_pattern': 'currying_partial_application',
        'chain_of_responsibility_pattern': 'chain_of_responsibility_pattern',
        'pub_sub_pattern': 'pubsub_pattern',
        'mvc_model_view_controller_pattern': 'mvc_pattern',
        'mvp_model_view_presenter_pattern': 'mvp_pattern',
        'mvvm_model_view_viewmodel_pattern': 'mvvm_pattern',
        'cqrs_command_query_responsibility_segregation_pattern': 'cqrs_pattern',
        'functional_composition_pattern': 'functional_composition',
    }
    
    if filename in mapping:
        filename = mapping[filename]
    
    return filename

def main():
    base_dir = Path(__file__).parent
    master_file = base_dir / 'master_output.md'
    diagrams_dir = base_dir / 'build' / 'diagrams'
    
    print(f"Reading {master_file}...")
    with open(master_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find all "## Python Architecture Diagram Snippet" sections
    snippet_sections = []
    for i, line in enumerate(lines):
        if line.strip() == "## Python Architecture Diagram Snippet":
            snippet_sections.append(i)
    
    print(f"Found {len(snippet_sections)} Python Architecture Diagram Snippet sections")
    
    # Process each section (in reverse to preserve line numbers)
    modifications = []
    for section_line_num in reversed(snippet_sections):
        # Check if next line is empty (indicating missing code)
        if section_line_num + 1 < len(lines) and lines[section_line_num + 1].strip() == '':
            # Find the pattern name
            pattern_header = find_pattern_name_before_line(lines, section_line_num)
            if not pattern_header:
                print(f"Warning: Could not find pattern name for section at line {section_line_num + 1}")
                continue
            
            pattern_name = pattern_name_to_filename(pattern_header)
            if not pattern_name:
                print(f"Warning: Could not parse pattern name from: {pattern_header.strip()}")
                continue
            
            python_file = diagrams_dir / f"{pattern_name}.py"
            
            if not python_file.exists():
                print(f"Warning: Python file not found: {python_file}")
                continue
            
            # Read the Python code
            with open(python_file, 'r', encoding='utf-8') as f:
                python_code = f.read()
            
            # Insert the Python code after the section header
            # Format: blank line, code block with python tag, blank line
            insert_text = f"\n```python\n{python_code}```\n\n"
            
            modifications.append({
                'line_num': section_line_num + 1,
                'pattern': pattern_header.strip(),
                'filename': pattern_name,
                'code_length': len(python_code)
            })
            
            # Insert the code
            lines[section_line_num + 1] = insert_text
    
    # Write the modified content
    print(f"\nModified {len(modifications)} sections:")
    for mod in reversed(modifications):
        print(f"  Line {mod['line_num']}: {mod['pattern']} ({mod['filename']}.py, {mod['code_length']} chars)")
    
    output_file = base_dir / 'master_output_updated.md'
    print(f"\nWriting to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"\n✓ Done! Review {output_file} and replace master_output.md if correct.")
    print(f"\nTo replace:")
    print(f"  mv {output_file} {master_file}")

if __name__ == '__main__':
    main()

