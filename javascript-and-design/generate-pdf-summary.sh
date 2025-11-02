#!/bin/bash

input_path="frontend.md"
output_path="frontend-summary.pdf"

# Create a temporary file with truncated code blocks
temp_file=$(mktemp)

awk '
/^```/ {
    in_code = !in_code
    if (in_code) {
        code_lines = 0
        print $0
    } else {
        if (code_lines > 100) {
            print "... (truncated " (code_lines - 100) " lines for PDF generation)"
        }
        print $0
    }
    next
}
{
    if (in_code) {
        code_lines++
        if (code_lines <= 100) {
            print $0
        }
    } else {
        print $0
    }
}
' "$input_path" > "$temp_file"

# Generate PDF from truncated version
pandoc "$temp_file" \
    --pdf-engine=lualatex \
    --toc \
    --toc-depth=3 \
    --number-sections \
    --highlight-style=tango \
    --variable geometry:margin=0.75in \
    --variable fontsize=10pt \
    --variable mainfont="DejaVu Serif" \
    --variable monofont="DejaVu Sans Mono" \
    --variable colorlinks=true \
    --variable linkcolor=blue \
    --variable urlcolor=blue \
    --variable classoption=openany \
    --variable documentclass=report \
    --include-in-header=<(cat <<'EOF'
\usepackage{tocloft}
\setlength{\cftsecnumwidth}{3em}
\setlength{\cftsubsecnumwidth}{4em}
\setlength{\cftsubsubsecnumwidth}{5em}
\usepackage{fvextra}
\RecustomVerbatimEnvironment{Verbatim}{Verbatim}{breaklines,breakanywhere,fontsize=\footnotesize}
\setlength{\emergencystretch}{3em}
EOF
) \
    -o "$output_path"

rm "$temp_file"

echo "PDF generated: $output_path"
echo "Note: Code blocks over 100 lines were truncated for PDF compatibility"
echo "For complete code, please refer to frontend.md directly"
