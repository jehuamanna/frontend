input_path="frontend.md"
output_path="frontend.pdf"

# input_path="frontend-design-problems.md"
# output_path="frontend-design-problems.pdf"

# Preprocess: split long fenced code blocks every N lines to avoid LaTeX overflow
SPLIT_EVERY=200
# Create a temp markdown file (ensure .md suffix for pandoc format detection)
TMP_INPUT=$(mktemp --suffix .md 2>/dev/null || mktemp -t tmp.XXXXXX.md)
awk -v N="$SPLIT_EVERY" '
  BEGIN { inside=0; count=0; fence="" }
  {
    # Detect fence lines starting with ```
    if ($0 ~ /^```/) {
      if (inside==0) {
        inside=1; count=0; fence=$0; print $0; next
      } else {
        inside=0; count=0; fence=""; print $0; next
      }
    }

    if (inside==1) {
      count++
      print $0
      if (count % N == 0) {
        # Close and reopen the same fence to split huge blocks
        print "```"
        print ""
        print fence
      }
      next
    }

    # Normal line
    print $0
  }
' "$input_path" > "$TMP_INPUT"

# Generate PDF with proper chapter structure and size limits
pandoc "$TMP_INPUT" \
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
\usepackage{mdframed}
\definecolor{shadecolor}{rgb}{0.97,0.97,0.97}
% Redefine Shaded to a breakable mdframed (replaces Pandoc's colorbox)
\renewenvironment{Shaded}{\begin{mdframed}[hidealllines=true,backgroundcolor=shadecolor,innertopmargin=4pt,innerbottommargin=4pt,innerleftmargin=6pt,innerrightmargin=6pt]}{\end{mdframed}}
\let\Oldincludegraphics\includegraphics
\renewcommand{\includegraphics}[2][]{\Oldincludegraphics[max width=\textwidth,max height=0.9\textheight,keepaspectratio]{#2}}
EOF
) \
    -o "$output_path"

# Cleanup temp file
rm -f "$TMP_INPUT"