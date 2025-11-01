#!/usr/bin/env python3
"""
Convert Markdown to Org-mode format while preserving all formatting.
"""

import re
import sys

def convert_md_to_org(md_content):
    """Convert Markdown content to Org-mode format."""
    lines = md_content.split('\n')
    org_lines = []
    in_code_block = False
    in_yaml_frontmatter = False
    code_language = ""
    in_table = False
    yaml_properties = {}
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Handle YAML frontmatter
        if i == 0 and line.strip() == '---':
            in_yaml_frontmatter = True
            i += 1
            continue
        
        if in_yaml_frontmatter:
            if line.strip() == '---':
                in_yaml_frontmatter = False
                # Add properties as Org properties
                for key, value in yaml_properties.items():
                    org_lines.append(f"#+{key.upper()}: {value}")
                org_lines.append("")
                i += 1
                continue
            else:
                # Parse YAML property
                match = re.match(r'^(\w+):\s*(.+)$', line)
                if match:
                    yaml_properties[match.group(1)] = match.group(2).strip('"')
                i += 1
                continue
        
        # Handle code blocks
        if line.startswith('```'):
            if not in_code_block:
                # Starting code block
                in_code_block = True
                code_language = line[3:].strip()
                if code_language:
                    org_lines.append(f"#+BEGIN_SRC {code_language}")
                else:
                    org_lines.append("#+BEGIN_EXAMPLE")
            else:
                # Ending code block
                in_code_block = False
                if code_language:
                    org_lines.append("#+END_SRC")
                else:
                    org_lines.append("#+END_EXAMPLE")
                code_language = ""
            i += 1
            continue
        
        # If inside code block, keep as-is
        if in_code_block:
            org_lines.append(line)
            i += 1
            continue
        
        # Handle headings
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            title = heading_match.group(2)
            # Convert bold/italic in heading
            title = convert_inline_formatting(title)
            org_lines.append('*' * level + ' ' + title)
            i += 1
            continue
        
        # Handle tables
        if '|' in line and line.strip().startswith('|'):
            # This is a table row
            org_lines.append(line)
            # Check if next line is a separator
            if i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|$', lines[i + 1]):
                # Convert separator line
                separator = lines[i + 1]
                # In org-mode, we use |--+--| style separators
                separator = re.sub(r'-+', '-', separator)
                separator = re.sub(r'\|', '|', separator)
                org_lines.append(separator)
                i += 2
                continue
            i += 1
            continue
        
        # Handle horizontal rules
        if re.match(r'^[\-*_]{3,}$', line.strip()):
            org_lines.append('-----')
            i += 1
            continue
        
        # Convert inline formatting
        converted_line = convert_inline_formatting(line)
        org_lines.append(converted_line)
        i += 1
    
    return '\n'.join(org_lines)

def convert_inline_formatting(text):
    """Convert inline Markdown formatting to Org-mode."""
    
    # Handle links [text](url) -> [[url][text]]
    text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'[[\2][\1]]', text)
    
    # Handle bold **text** or __text__ -> *text*
    # But need to be careful not to convert code or other special cases
    text = re.sub(r'\*\*(.+?)\*\*', r'*\1*', text)
    text = re.sub(r'__(.+?)__', r'*\1*', text)
    
    # Handle italic *text* or _text_ -> /text/
    # This is tricky because * is also used for bold
    # We need to handle single * carefully
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'/\1/', text)
    text = re.sub(r'(?<!_)_(?!_)(.+?)(?<!_)_(?!_)', r'/\1/', text)
    
    # Handle inline code `code` -> =code=
    text = re.sub(r'`([^`]+)`', r'=\1=', text)
    
    # Handle strikethrough ~~text~~ -> +text+
    text = re.sub(r'~~(.+?)~~', r'+\1+', text)
    
    return text

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'frontend-design-problems.md'
    output_file = input_file.rsplit('.', 1)[0] + '.org'
    
    print(f"Converting {input_file} to {output_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    org_content = convert_md_to_org(md_content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(org_content)
    
    print(f"Conversion complete! Output saved to {output_file}")
    print(f"Original lines: {len(md_content.split(chr(10)))}")
    print(f"Converted lines: {len(org_content.split(chr(10)))}")

if __name__ == '__main__':
    main()

