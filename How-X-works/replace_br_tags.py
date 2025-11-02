#!/usr/bin/env python3
"""
Replace all <br> tags with actual newlines in master_output.md
"""

import re

def main():
    input_file = 'master_output.md'
    output_file = 'master_output_no_br.md'
    
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count <br> tags before replacement
    br_count = len(re.findall(r'<br>', content, re.IGNORECASE))
    print(f"Found {br_count} <br> tags")
    
    print("Replacing <br> tags with newlines...")
    
    # Replace all variations of <br> tags
    # <br>, <br/>, <br />, <BR>, etc.
    content = re.sub(r'<br\s*/?\s*>', '\n', content, flags=re.IGNORECASE)
    
    # Verify replacement
    remaining_br = len(re.findall(r'<br>', content, re.IGNORECASE))
    print(f"Remaining <br> tags: {remaining_br}")
    print(f"Replaced: {br_count - remaining_br}")
    
    print(f"\nWriting to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Done! File saved to: {output_file}")
    print(f"\nTo replace the original file:")
    print(f"  mv {output_file} {input_file}")

if __name__ == '__main__':
    main()

