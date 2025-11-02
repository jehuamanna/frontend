# input_path="frontend.md"
# output_path="frontend.pdf"

input_path="frontend-design-problems.md"
output_path="frontend-design-problems.pdf"

# Step 1: Generate diagrams and create temp file with diagrams inserted
echo "Step 1: Generating diagrams and inserting into markdown..."
TMP_WITH_DIAGRAMS=$(mktemp --suffix .md 2>/dev/null || mktemp -t tmp.XXXXXX.md)

# Generate diagrams and insert them into markdown
python3 generate_diagrams.py "$input_path" "$TMP_WITH_DIAGRAMS" 2>&1 | grep -v "^$" || {
    echo "Warning: Diagram generation skipped (graphviz not installed)"
    # If diagram generation fails, just copy the original
    cp "$input_path" "$TMP_WITH_DIAGRAMS"
}

# Preprocess: split long fenced code blocks every N lines to avoid LaTeX overflow
# Don't change this.
SPLIT_EVERY=200
MAX_LINE_LENGTH=80

# Create a temp markdown file (ensure .md suffix for pandoc format detection)
TMP_INPUT=$(mktemp --suffix .md 2>/dev/null || mktemp -t tmp.XXXXXX.md)

# Two-stage preprocessing: 
# 1. Break long horizontal lines in code blocks
# 2. Split very long vertical code blocks

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

awk -v N="$SPLIT_EVERY" -v MAX="$MAX_LINE_LENGTH" '
  BEGIN { inside=0; count=0; fence="" }
  
  # Function to break long lines intelligently
  function break_long_line(line, max_len) {
    if (length(line) <= max_len) {
      return line
    }
    
    # Get leading whitespace
    match(line, /^[ \t]*/)
    indent = substr(line, 1, RLENGTH)
    continuation_indent = indent "  "
    
    result = ""
    remaining = line
    first_line = 1
    
    while (length(remaining) > max_len) {
      # Try to break at logical points
      chunk = substr(remaining, 1, max_len)
      
      # Find best break point (prefer after operators, commas, spaces)
      break_pos = max_len
      
      # Try to break after: , ; + - * / = ( { [ || && . 
      for (i = max_len; i > max_len - 20 && i > 0; i--) {
        c = substr(remaining, i, 1)
        if (c ~ /[,;=+\-*\/\(\{\[]/ || substr(remaining, i, 2) ~ /(&&|\|\||=>)/) {
          break_pos = i
          break
        }
      }
      
      # If no good break point, try space
      if (break_pos == max_len) {
        for (i = max_len; i > max_len - 20 && i > 0; i--) {
          if (substr(remaining, i, 1) == " ") {
            break_pos = i
            break
          }
        }
      }
      
      chunk = substr(remaining, 1, break_pos)
      remaining = substr(remaining, break_pos + 1)
      
      # Strip leading spaces from remaining
      sub(/^[ \t]+/, "", remaining)
      
      if (first_line) {
        result = chunk
        first_line = 0
      } else {
        result = result "\n" continuation_indent remaining
        break
      }
      
      remaining = continuation_indent remaining
    }
    
    if (first_line) {
      return line
    }
    
    if (remaining != "") {
      if (result != "") {
        result = result "\n" remaining
      } else {
        result = remaining
      }
    }
    
    return result
  }
  
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
      
      # Break long lines in code blocks
      if (length($0) > MAX) {
        broken = break_long_line($0, MAX)
        print broken
      } else {
        print $0
      }
      
      if (count % N == 0) {
        # Close and reopen the same fence to split huge blocks
        print "```"
        print ""
        print fence
      }
      next
    }

    # Normal line - no processing
    print $0
  }
' "$TMP_WITH_DIAGRAMS" | iconv -f UTF-8 -t UTF-8 -c > "$TMP_INPUT"

# Generate PDF with proper chapter structure and size limits
pandoc "$TMP_INPUT" \
    --from=markdown \
    --pdf-engine=lualatex \
    --toc \
    --toc-depth=4 \
    --number-sections \
    --highlight-style=tango \
    --variable geometry:left=0.5in \
    --variable geometry:right=0.5in \
    --variable geometry:top=0.75in \
    --variable geometry:bottom=0.75in \
    --variable geometry:paperwidth=8.5in \
    --variable geometry:paperheight=11in \
    --variable fontsize=9pt \
    --variable mainfont="DejaVu Serif" \
    --variable monofont="Inconsolata" \
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
\RecustomVerbatimEnvironment{Verbatim}{Verbatim}{
  breaklines=true,
  breakanywhere=true,
  breaksymbolleft={},
  breakanywheresymbolpre={},
  fontsize=\tiny,
  commandchars=\\\{\},
  xleftmargin=1pt,
  xrightmargin=1pt,
  frame=none,
  numbers=none,
  tabsize=2
}
\usepackage{etoolbox}
\makeatletter
\preto{\@verbatim}{\topsep=2pt \partopsep=2pt}
\makeatother
\setlength{\emergencystretch}{3em}
\tolerance=9999
\hbadness=9999
\maxdeadcycles=200
\usepackage[export]{adjustbox}
\usepackage{mdframed}
\definecolor{shadecolor}{rgb}{0.97,0.97,0.97}
% Redefine Shaded to a breakable mdframed (replaces Pandoc's colorbox)
\renewenvironment{Shaded}{\begin{mdframed}[hidealllines=true,backgroundcolor=shadecolor,innertopmargin=2pt,innerbottommargin=2pt,innerleftmargin=2pt,innerrightmargin=2pt,skipabove=4pt,skipbelow=4pt]}{\end{mdframed}}
\let\Oldincludegraphics\includegraphics
\renewcommand{\includegraphics}[2][]{\Oldincludegraphics[max width=\textwidth,max height=0.9\textheight,keepaspectratio]{#2}}
% Better handling for long URLs and inline code
\usepackage{xurl}
\usepackage{hyphenat}
EOF
) \
    -o "$output_path"

# Cleanup temp files
rm -f "$TMP_INPUT" "$TMP_WITH_DIAGRAMS"