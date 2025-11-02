#!/bin/bash

input_path="frontend.md"
output_path="frontend-complete.pdf"
temp_file=$(mktemp)

echo "Splitting long code blocks (max 60 lines each)..."

python3 << 'PYTHON' > "$temp_file"
import sys

in_code = False
code_lines = []
code_lang = ""
line_count = 0
block_num = 0
MAX_LINES = 60

with open("frontend.md", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip('\n')
        
        if line.startswith("```"):
            if in_code:
                # End code block
                if code_lines:
                    for l in code_lines:
                        print(l)
                print("```")
                print()
                in_code = False
                code_lines = []
                line_count = 0
                block_num = 0
            else:
                # Start code block
                in_code = True
                code_lang = line[3:].strip()
                code_lines = [line]
                line_count = 0
                block_num = 0
        elif in_code:
            line_count += 1
            code_lines.append(line)
            
            # Split if too long
            if line_count >= MAX_LINES:
                for l in code_lines:
                    print(l)
                print("```")
                print()
                block_num += 1
                if code_lang:
                    print(f"```{code_lang}")
                else:
                    print("```")
                code_lines = []
                line_count = 0
        else:
            print(line)

# Handle remaining code block
if in_code and code_lines:
    for l in code_lines:
        print(l)
    print("```")
PYTHON

echo "Generating PDF with lualatex..."

pandoc "$temp_file" \
    --pdf-engine=lualatex \
    --toc \
    --toc-depth=3 \
    --number-sections \
    --highlight-style=tango \
    --variable geometry:margin=0.75in \
    --variable fontsize=9pt \
    --variable mainfont="DejaVu Serif" \
    --variable monofont="DejaVu Sans Mono" \
    --variable colorlinks=true \
    --variable linkcolor=blue \
    --variable urlcolor=blue \
    --variable documentclass=report \
    --variable classoption=openany \
    --include-in-header=<(cat <<'EOF'
\usepackage{fvextra}
\RecustomVerbatimEnvironment{Verbatim}{Verbatim}{breaklines,breakanywhere,fontsize=\tiny}
\setlength{\emergencystretch}{3em}
EOF
) \
    -o "$output_path" 2>&1 | tail -20

rm "$temp_file"

if [ -f "$output_path" ]; then
    echo ""
    echo "================================================"
    echo "SUCCESS! Full PDF generated (no truncation)"
    echo "================================================"
    ls -lh "$output_path"
    pdfinfo "$output_path" 2>/dev/null | grep Pages || echo "PDF created!"
else
    echo "PDF generation failed - see errors above"
    exit 1
fi
