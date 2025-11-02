# PDF Generation System with Diagram Support

Complete solution for generating professional PDFs from markdown with beautiful diagrams and proper code formatting.

## Quick Start

### 1. Install diagram tools (one-time setup)

```bash
sudo bash install-diagram-tools.sh
```

This installs:
- Graphviz (system package)
- python3-graphviz (Python bindings)

### 2. Generate PDF with diagrams

```bash
bash generate-pdf.sh
```

This will:
1. Generate architecture diagrams as PNG images
2. Break long code lines (100 chars max)
3. Split large code blocks (200 lines max)
4. Create PDF with proper formatting

## What's Included

### Scripts

1. **generate-pdf.sh** - Main PDF generation script
   - Automatically generates diagrams
   - Preprocesses markdown (line breaking, block splitting)
   - Creates PDF with LuaLaTeX
   - Optimized for code-heavy documents

2. **generate_diagrams.py** - Diagram generation tool
   - Creates 5 architecture diagrams
   - Uses Graphviz for professional output
   - Outputs PNG files to `diagrams/` folder

3. **install-diagram-tools.sh** - One-time installation
   - Installs Graphviz system package
   - Installs Python bindings
   - Verifies installation

4. **add_newlines_before_lists.py** - List formatting
   - Adds blank lines before list items
   - Improves readability

## Generated Diagrams

The system generates these professional diagrams:

1. **virtuallist-architecture.png**
   - Fenwick Tree structure
   - Viewport management
   - Scroll handling
   - ResizeObserver integration

2. **canvas-architecture.png**
   - Canvas management with Hi-DPI support
   - Layer system
   - Render engine with RAF
   - Quadtree spatial indexing
   - Interaction handling

3. **reactive-engine-architecture.png**
   - Signal/Computed/Effect flow
   - Dependency tracking
   - Scheduler and batching
   - Topological sort for updates

4. **spreadsheet-architecture.png**
   - Three-layer architecture
   - Data layer (Sparse Matrix, Virtual Viewport)
   - Formula layer (Parser, Dependency Graph, Evaluator)
   - UI layer (Keyboard, Selection, Editor)

5. **charts-architecture.png**
   - Real-time data pipeline
   - WebSocket → Web Worker → Ring Buffer
   - Time-series aggregation
   - Canvas rendering with culling

## PDF Optimizations

### Code Block Handling

**Problem**: Long code blocks cause PDF generation to fail

**Solutions**:
1. **Horizontal**: Break lines at 100 characters
   - Breaks at logical points (operators, commas)
   - Adds continuation indentation
   
2. **Vertical**: Split blocks at 200 lines
   - Closes and reopens code fence
   - Maintains syntax highlighting

### Font Settings

- Body font: DejaVu Serif (9pt)
- Code font: Inconsolata (tiny)
- Margins: 0.5in left/right, 0.75in top/bottom
- Paper: US Letter (8.5" x 11")

### LaTeX Optimizations

- `breaklines=true` - Automatic line breaking
- `breakanywhere=true` - Break at any character if needed
- `\tolerance=9999` - Maximum tolerance
- `\scriptsize` code font - Fits more per line
- Minimal padding (1-2pt) - Maximizes space

### Character Handling

All emojis and special Unicode replaced with:
- `Yes` / `No` instead of ✓ / ✗
- `[OK]` / `[WARN]` / `[SEARCH]` instead of emojis
- Ensures compatibility with all fonts

## File Structure

```
frontend/
├── frontend-design-problems.md    (source)
├── frontend-design-problems.pdf   (output)
├── generate-pdf.sh               (main script)
├── generate_diagrams.py          (diagram generator)
├── install-diagram-tools.sh      (installation)
├── add_newlines_before_lists.py  (formatting)
├── diagrams/                     (generated images)
│   ├── virtuallist-architecture.png
│   ├── canvas-architecture.png
│   ├── reactive-engine-architecture.png
│   ├── spreadsheet-architecture.png
│   └── charts-architecture.png
└── README-PDF-GENERATION.md      (this file)
```

## Advanced Usage

### Generate diagrams only

```bash
python3 generate_diagrams.py
```

### Add newlines before lists

```bash
python3 add_newlines_before_lists.py frontend-design-problems.md
```

### Custom diagram

Edit `generate_diagrams.py` and add:

```python
def create_my_diagram():
    from graphviz import Digraph
    
    dot = Digraph(comment='My Diagram', format='png')
    dot.attr(rankdir='TB')
    dot.attr('node', shape='box', style='filled', fillcolor='lightblue')
    
    dot.node('A', 'Component A')
    dot.node('B', 'Component B')
    dot.edge('A', 'B', label='connects')
    
    return dot
```

Then add to `create_all_diagrams()`:
```python
diagrams = {
    'my-diagram': create_my_diagram(),
    # ... existing diagrams
}
```

### Adjust code line length

Edit `generate-pdf.sh`:
```bash
MAX_LINE_LENGTH=120  # Change from 100 to 120
```

### Adjust code block split

Edit `generate-pdf.sh`:
```bash
SPLIT_EVERY=300  # Change from 200 to 300
```

## Troubleshooting

### Graphviz not found

```bash
sudo apt-get install graphviz python3-graphviz
```

### PDF generation fails

Check for:
1. LuaLaTeX installed: `which lualatex`
2. Pandoc installed: `which pandoc`
3. Sufficient disk space
4. No special characters in file paths

### Diagrams not appearing

1. Check diagrams generated: `ls diagrams/*.png`
2. Verify image paths in markdown
3. Ensure Pandoc can access files

### Code still overflows

Reduce `MAX_LINE_LENGTH` further:
```bash
MAX_LINE_LENGTH=80  # or even 70
```

Or use even smaller font in `generate-pdf.sh`:
```latex
fontsize=\tiny  # already smallest
```

### Memory issues

For very large documents:
- Generate PDF in chunks
- Reduce image DPI
- Use compression

## Performance

**Typical generation time** (35,000 line document):
- Diagram generation: 5-10 seconds
- Markdown preprocessing: 10-15 seconds
- PDF compilation: 2-3 minutes
- **Total: ~3-4 minutes**

**Output size**:
- PDF: ~1.5-2 MB
- With diagrams: +200-300 KB

## Benefits

1. **Professional diagrams**: No more distorted ASCII art
2. **Readable code**: Proper line breaking and wrapping
3. **Automated**: One command for complete PDF
4. **Maintainable**: Diagrams are code, version controlled
5. **Scalable**: Easy to add more diagrams
6. **Reliable**: Handles large documents (35K+ lines)

## Dependencies

**Required**:
- Pandoc
- LuaLaTeX (texlive-luatex)
- Graphviz
- python3-graphviz

**Install all**:
```bash
sudo apt-get update
sudo apt-get install pandoc texlive-luatex graphviz python3-graphviz
```

## Credits

- **Graphviz**: Graph visualization
- **Pandoc**: Universal document converter
- **LuaLaTeX**: PDF engine
- **fvextra**: LaTeX package for code formatting
- **mdframed**: LaTeX package for code blocks

## Support

For issues or questions, check:
- DIAGRAM_GENERATION.md - Detailed diagram guide
- generate-pdf.sh - Script comments
- Pandoc documentation: https://pandoc.org
- Graphviz documentation: https://graphviz.org

