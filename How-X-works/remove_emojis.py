#!/usr/bin/env python3
"""
Remove all emojis from master_output.md
"""

import re

def remove_emojis(text):
    """
    Remove all emoji characters from text using comprehensive regex patterns
    """
    # Emoji pattern that covers most Unicode emoji ranges
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"  # dingbats
        "\U000024C2-\U0001F251"  # enclosed characters
        "\U0001F900-\U0001F9FF"  # supplemental symbols and pictographs
        "\U0001FA00-\U0001FA6F"  # chess symbols
        "\U0001FA70-\U0001FAFF"  # symbols and pictographs extended-A
        "\U00002600-\U000026FF"  # miscellaneous symbols
        "\U00002700-\U000027BF"  # dingbats
        "\U0001F018-\U0001F270"  # various symbols
        "\U0001F300-\U0001F5FF"  # misc symbols and pictographs
        "\U0001F680-\U0001F6FF"  # transport and map
        "\u2600-\u26FF"          # miscellaneous symbols (shorter range)
        "\u2700-\u27BF"          # dingbats
        "\uFE00-\uFE0F"          # variation selectors
        "\u200d"                 # zero width joiner
        "\u2640-\u2642"          # gender symbols
        "\u2695"                 # medical symbol
        "\u2699"                 # gear
        "\u269B-\u269C"          # atom, fleur-de-lis
        "\u26A0-\u26A1"          # warning, high voltage
        "\u26AA-\u26AB"          # circles
        "\u26B0-\u26B1"          # coffin, funeral urn
        "\u26BD-\u26BE"          # soccer, baseball
        "\u26C4-\u26C5"          # snowman
        "\u26CE"                 # Ophiuchus
        "\u26D4"                 # no entry
        "\u26EA"                 # church
        "\u26F2-\u26F3"          # fountain
        "\u26F5"                 # sailboat
        "\u26FA"                 # tent
        "\u26FD"                 # fuel pump
        "\u2705"                 # check mark button
        "\u270A-\u270B"          # fist
        "\u2728"                 # sparkles
        "\u274C"                 # cross mark
        "\u274E"                 # cross mark button
        "\u2753-\u2755"          # question marks
        "\u2757"                 # exclamation mark
        "\u2795-\u2797"          # plus/minus/division
        "\u27B0"                 # curly loop
        "\u27BF"                 # double curly loop
        "\u2B1B-\u2B1C"          # squares
        "\u2B50"                 # star
        "\u2B55"                 # circle
        "\u3030"                 # wavy dash
        "\u303D"                 # part alternation mark
        "\u3297"                 # circled ideograph congratulation
        "\u3299"                 # circled ideograph secret
        "]+",
        flags=re.UNICODE
    )
    
    # Remove emojis
    text = emoji_pattern.sub('', text)
    
    # Also remove some common emoji-like characters
    text = text.replace('✅', '')
    text = text.replace('❌', '')
    text = text.replace('✓', '')
    text = text.replace('✗', '')
    text = text.replace('⚠️', '')
    text = text.replace('⚠', '')
    text = text.replace('🎉', '')
    text = text.replace('🎯', '')
    text = text.replace('📊', '')
    text = text.replace('📁', '')
    text = text.replace('📸', '')
    text = text.replace('🔄', '')
    text = text.replace('⭐', '')
    text = text.replace('🚀', '')
    text = text.replace('💡', '')
    text = text.replace('🔍', '')
    text = text.replace('📝', '')
    text = text.replace('🏠', '')
    text = text.replace('📦', '')
    text = text.replace('🌐', '')
    
    # Clean up multiple spaces that might result from emoji removal
    text = re.sub(r' +', ' ', text)
    
    # Clean up lines that become empty after emoji removal
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
    
    return text

def main():
    input_file = 'master_output.md'
    output_file = 'master_output_no_emojis.md'
    
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_length = len(content)
    print(f"Original size: {original_length:,} characters")
    
    print("Removing emojis...")
    cleaned_content = remove_emojis(content)
    
    cleaned_length = len(cleaned_content)
    removed = original_length - cleaned_length
    
    print(f"Cleaned size: {cleaned_length:,} characters")
    print(f"Removed: {removed:,} characters ({removed / original_length * 100:.2f}%)")
    
    print(f"\nWriting to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"✓ Done! Emoji-free version saved to: {output_file}")
    print(f"\nTo replace the original file:")
    print(f"  mv {output_file} {input_file}")

if __name__ == '__main__':
    main()

