#!/bin/bash

input_path="frontend.md"
output_path="frontend-full.pdf"

# Create a temporary file with split code blocks
temp_file=$(mktemp)

awk '
/^```/ {
    if (in_code) {
        # End of code block
        if (code_lines > 0) {
            print code_buffer
        }
        print $0
        in_code = 0
        code_lines = 0
        code_buffer = ""
        block_num = 0
    } else {
        # Start of code block
        in_code = 1
        code_lang = substr($0, 4)
        code_buffer = $0
        code_lines = 0
        block_num = 0
    }
    next
}
{
    if (in_code) {
        code_lines++
        code_buffer = code_buffer "\n" $0
        
        # Split every 80 lines
        if (code_lines >= 80) {
            print code_buffer
            print "```"
            print ""
            block_num++
            print "```" code_lang " (continued " block_num ")"
            code_buffer = ""
            code_lines = 0
        }
    } else {
        print $0
    }
}
END {
    if (in_code && code_lines > 0) {
        print code_buffer
        print "```"
    }
}
' "$input_path" > "$temp_file"

echo "Preprocessing complete. Generating PDF..."

# Generate PDF from split version
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
    --variable classoption=openany \
    --variable documentclass=report \
    --variable linestretch=1.05 \
    --include-in-header=<(cat <<'EOF'
\usepackage{tocloft}
\setlength{\cftsecnumwidth}{3em}
\setlength{\cftsubsecnumwidth}{4em}
\setlength{\cftsubsubsecnumwidth}{5em}
\usepackage{fvextra}
\RecustomVerbatimEnvironment{Verbatim}{Verbatim}{breaklines,breakanywhere,fontsize=\scriptsize}
\usepackage{etoolbox}
\makeatletter
\preto{\@verbatim}{\topsep=1pt \partopsep=1pt}
\makeatother
\setlength{\emergencystretch}{3em}
\maxdeadcycles=300
EOF
) \
    -o "$output_path"

rm "$temp_file"

if [ $? -eq 0 ]; then
    echo ""
    echo "=============================================="
    echo "✓ Full PDF generated successfully!"
    echo "=============================================="
    echo "File: $output_path"
    echo "All code is included (split into 80-line blocks for LaTeX compatibility)"
    ls -lh "$output_path"
else
    echo "PDF generation failed"
    exit 1
fi
