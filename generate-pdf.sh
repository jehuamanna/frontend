input_path="frontend.md"
output_path="frontend.pdf"

# Generate PDF with proper chapter structure
pandoc "$input_path" \
    --pdf-engine=xelatex \
    --toc \
    --toc-depth=4 \
    --number-sections \
    --highlight-style=tango \
    --variable geometry:margin=1in \
    --variable fontsize=11pt \
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
\setlength{\cftparanumwidth}{6em}
EOF
) \
    -o "$output_path"