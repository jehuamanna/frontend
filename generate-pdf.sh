# input_path="frontend.md"
# output_path="frontend.pdf"

input_path="frontend-design-problems.md"
output_path="frontend-design-problems.pdf"
# Generate PDF with proper chapter structure and size limits
pandoc "$input_path" \
    --pdf-engine=lualatex \
    --toc \
    --toc-depth=4 \
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
    --variable linestretch=1.1 \
    --include-in-header=<(cat <<'EOF'
\usepackage{tocloft}
\setlength{\cftsecnumwidth}{3em}
\setlength{\cftsubsecnumwidth}{4em}
\setlength{\cftsubsubsecnumwidth}{5em}
\setlength{\cftparanumwidth}{6em}
\usepackage{fvextra}
\RecustomVerbatimEnvironment{Verbatim}{Verbatim}{breaklines,breakanywhere,fontsize=\footnotesize,commandchars=\\\{\}}
\usepackage{etoolbox}
\makeatletter
\preto{\@verbatim}{\topsep=2pt \partopsep=2pt}
\makeatother
\setlength{\emergencystretch}{3em}
\maxdeadcycles=200
\usepackage[export]{adjustbox}
EOF
) \
    -o "$output_path"