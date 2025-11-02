#!/usr/bin/env python3
"""
Generate unique architectural diagrams for each chapter.
Each diagram represents the specific problem's architecture/flow.
"""

import os
import sys
from pathlib import Path

def install_dependencies():
    """Check and install required dependencies."""
    try:
        import graphviz
    except ImportError:
        print("ERROR: python3-graphviz not found.")
        print("\nTo install, run:")
        print("  sudo apt-get update")
        print("  sudo apt-get install graphviz python3-graphviz")
        return False
    
    if os.system("which dot > /dev/null 2>&1") != 0:
        print("WARNING: Graphviz system package not found.")
        print("Install with: sudo apt-get install graphviz")
        return False
    
    return True

def create_virtuallist_architecture():
    """VirtualList: Show viewport sliding window over items."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='VirtualList Viewport', format='png')
        dot.attr(rankdir='LR', size='12,8')
        dot.attr('node', shape='box', style='filled')
        
        # Create item list
        with dot.subgraph(name='cluster_items') as c:
            c.attr(label='10,000 Items (Total)', style='dashed')
            c.node('I0', 'Item 0', fillcolor='white')
            c.node('I1', '...', shape='plaintext')
            c.node('I50', 'Item 50\n(visible)', fillcolor='lightgreen')
            c.node('I51', 'Item 51\n(visible)', fillcolor='lightgreen')
            c.node('I52', 'Item 52\n(visible)', fillcolor='lightgreen')
            c.node('I53', '...', shape='plaintext')
            c.node('I999', 'Item 9999', fillcolor='white')
        
        # Viewport
        dot.node('VP', 'Viewport\n(Visible Area)\nRenders 10-20 items', 
                fillcolor='lightcoral', shape='box3d')
        
        # Fenwick Tree for height lookups
        dot.node('FT', 'Fenwick Tree\nO(log n) height\nquery/update', 
                fillcolor='lightblue', shape='cylinder')
        
        # Scroll position
        dot.node('SP', 'Scroll Position\n→ Visible Range\nCalc', 
                fillcolor='lightyellow')
        
        # Edges showing flow
        dot.edge('SP', 'FT', 'Query heights')
        dot.edge('FT', 'VP', 'Return visible\nitem indices')
        dot.edge('VP', 'I50', 'Render only\nvisible items', style='bold')
        dot.edge('VP', 'I51', style='bold')
        dot.edge('VP', 'I52', style='bold')
        
        return dot
    except Exception as e:
        print(f"Error creating virtuallist diagram: {e}")
        return None

def create_canvas_architecture():
    """Canvas: Show transformation pipeline."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='Canvas Transformation Pipeline', format='png')
        dot.attr(rankdir='LR', size='12,6')
        dot.attr('node', shape='box', style='rounded,filled')
        
        # Input
        dot.node('Input', 'User Input\n(Mouse/Touch)\nDrag, Zoom, Pan', 
                fillcolor='lightcoral', shape='parallelogram')
        
        # Transform calculation
        dot.node('TM', 'Transformation\nMatrix\n[a, b, c, d, e, f]', 
                fillcolor='lightblue')
        
        # Apply transforms
        with dot.subgraph(name='cluster_transforms') as c:
            c.attr(label='Transform Operations', style='rounded')
            c.node('Scale', 'Scale\n(Zoom)', fillcolor='lightgreen')
            c.node('Translate', 'Translate\n(Pan)', fillcolor='lightgreen')
            c.node('Rotate', 'Rotate', fillcolor='lightgreen')
        
        # Rendering
        dot.node('Canvas', 'Canvas 2D\nctx.setTransform()\nRender shapes', 
                fillcolor='lightyellow', shape='box3d')
        
        # DPI scaling
        dot.node('DPI', 'devicePixelRatio\nHigh-DPI scaling', 
                fillcolor='lightcyan')
        
        # Output
        dot.node('Output', 'Screen\n(Crisp rendering)', 
                fillcolor='lightcoral', shape='parallelogram')
        
        # Flow
        dot.edge('Input', 'TM', 'Calculate')
        dot.edge('TM', 'Scale')
        dot.edge('TM', 'Translate')
        dot.edge('TM', 'Rotate')
        dot.edge('Scale', 'Canvas')
        dot.edge('Translate', 'Canvas')
        dot.edge('Rotate', 'Canvas')
        dot.edge('DPI', 'Canvas', 'Scale context')
        dot.edge('Canvas', 'Output')
        
        return dot
    except Exception as e:
        print(f"Error creating canvas diagram: {e}")
        return None

def create_charts_architecture():
    """Charts: Show data flow from WebSocket to Canvas."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='Real-time Charts Data Flow', format='png')
        dot.attr(rankdir='TB', size='10,10')
        dot.attr('node', shape='box', style='rounded,filled')
        
        # Data source
        dot.node('WS', 'WebSocket\nMarket Data\n1000 msgs/sec', 
                fillcolor='lightcoral', shape='cylinder')
        
        # Worker processing
        with dot.subgraph(name='cluster_worker') as c:
            c.attr(label='Web Worker (Background)', style='rounded')
            c.node('RB', 'Ring Buffer\nO(1) insert\n10k points', fillcolor='lightblue')
            c.node('AGG', 'Aggregation\n1s → 1m → 1h', fillcolor='lightgreen')
            c.node('CALC', 'Indicators\nMA, EMA, VWAP', fillcolor='lightyellow')
        
        # Main thread rendering
        with dot.subgraph(name='cluster_render') as c:
            c.attr(label='Main Thread (60fps)', style='rounded')
            c.node('VP2', 'Viewport Culling\nOnly visible data', fillcolor='lightcyan')
            c.node('Canvas2', 'Canvas Rendering\nCandlesticks\nVolume bars', 
                  fillcolor='lightyellow', shape='box3d')
        
        # User interaction
        dot.node('UI', 'User Interaction\nZoom, Pan,\nCrosshair', 
                fillcolor='lightgreen', shape='parallelogram')
        
        # Flow
        dot.edge('WS', 'RB', 'Stream')
        dot.edge('RB', 'AGG', 'Process')
        dot.edge('AGG', 'CALC', 'Calculate')
        dot.edge('CALC', 'VP2', 'Transfer to\nmain thread')
        dot.edge('VP2', 'Canvas2', 'Render visible')
        dot.edge('UI', 'VP2', 'Update viewport')
        dot.edge('Canvas2', 'UI', 'Display')
        
        return dot
    except Exception as e:
        print(f"Error creating charts diagram: {e}")
        return None

def create_spreadsheet_architecture():
    """Spreadsheet: Show cell dependency graph."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='Spreadsheet Cell Dependencies', format='png')
        dot.attr(rankdir='TB', size='10,8')
        dot.attr('node', shape='box', style='filled')
        
        # Cells with values
        dot.node('A1', 'A1\n= 10', fillcolor='lightgreen')
        dot.node('A2', 'A2\n= 20', fillcolor='lightgreen')
        dot.node('A3', 'A3\n= 30', fillcolor='lightgreen')
        
        # Formula cells
        dot.node('B1', 'B1\n= A1 + A2\n(30)', fillcolor='lightyellow')
        dot.node('B2', 'B2\n= A2 * 2\n(40)', fillcolor='lightyellow')
        dot.node('C1', 'C1\n= SUM(A1:A3)\n(60)', fillcolor='lightcoral')
        dot.node('D1', 'D1\n= B1 + C1\n(90)', fillcolor='lightblue')
        
        # Dependency arrows
        dot.edge('A1', 'B1', 'depends on')
        dot.edge('A2', 'B1', 'depends on')
        dot.edge('A2', 'B2', 'depends on')
        dot.edge('A1', 'C1', 'depends on')
        dot.edge('A2', 'C1', 'depends on')
        dot.edge('A3', 'C1', 'depends on')
        dot.edge('B1', 'D1', 'depends on')
        dot.edge('C1', 'D1', 'depends on')
        
        # Evaluation order
        with dot.subgraph() as s:
            s.attr(rank='same')
            s.node('Order', 'Topological Sort:\n1. A1, A2, A3\n2. B1, B2, C1\n3. D1', 
                  fillcolor='white', shape='note')
        
        return dot
    except Exception as e:
        print(f"Error creating spreadsheet diagram: {e}")
        return None

def create_reactive_engine_architecture():
    """Reactive Engine: Show signal graph with dependencies."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='Reactive Signals Graph', format='png')
        dot.attr(rankdir='TB', size='10,10')
        dot.attr('node', shape='box', style='rounded,filled')
        
        # Signals (state)
        with dot.subgraph(name='cluster_signals') as c:
            c.attr(label='Signals (State)', style='rounded', fillcolor='lightgreen')
            c.node('S1', 'signal(count)\nvalue: 5', fillcolor='lightgreen')
            c.node('S2', 'signal(price)\nvalue: 100', fillcolor='lightgreen')
        
        # Computed (derived)
        with dot.subgraph(name='cluster_computed') as c:
            c.attr(label='Computed (Derived)', style='rounded')
            c.node('C1', 'computed(() =>\n  count * 2)\nvalue: 10', fillcolor='lightyellow')
            c.node('C2', 'computed(() =>\n  count * price)\nvalue: 500', fillcolor='lightyellow')
            c.node('C3', 'computed(() =>\n  double + total)\nvalue: 510', fillcolor='lightyellow')
        
        # Effects (side effects)
        with dot.subgraph(name='cluster_effects') as c:
            c.attr(label='Effects (Side Effects)', style='rounded')
            c.node('E1', 'effect(() =>\n  console.log(count))', fillcolor='lightcoral')
            c.node('E2', 'effect(() =>\n  updateDOM(total))', fillcolor='lightcoral')
        
        # Dependencies
        dot.edge('S1', 'C1', 'reads', style='bold')
        dot.edge('S1', 'C2', 'reads', style='bold')
        dot.edge('S2', 'C2', 'reads', style='bold')
        dot.edge('C1', 'C3', 'reads')
        dot.edge('C2', 'C3', 'reads')
        dot.edge('S1', 'E1', 'subscribes', color='red')
        dot.edge('C2', 'E2', 'subscribes', color='red')
        
        # Update flow
        dot.node('Update', 'count.set(6)\n→ Triggers cascade', 
                fillcolor='lightblue', shape='diamond')
        dot.edge('Update', 'S1', 'updates')
        
        return dot
    except Exception as e:
        print(f"Error creating reactive diagram: {e}")
        return None

def create_editor_architecture():
    """Editor: Show command pattern with undo/redo stacks."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='Editor Command Pattern', format='png')
        dot.attr(rankdir='LR', size='12,8')
        dot.attr('node', shape='box', style='filled')
        
        # User actions
        dot.node('User', 'User Types:\n"Hello World"', 
                fillcolor='lightcoral', shape='parallelogram')
        
        # Commands
        with dot.subgraph(name='cluster_commands') as c:
            c.attr(label='Commands Created', style='rounded')
            c.node('CMD1', 'InsertText("H")', fillcolor='lightblue')
            c.node('CMD2', 'InsertText("e")', fillcolor='lightblue')
            c.node('CMD3', 'InsertText("llo")\n(merged)', fillcolor='lightgreen')
            c.node('CMD4', 'FormatBold()', fillcolor='lightyellow')
        
        # Undo stack
        with dot.subgraph(name='cluster_undo') as c:
            c.attr(label='Undo Stack', style='rounded', fillcolor='lightcyan')
            c.node('U1', 'CMD1', shape='box', fillcolor='lightcyan')
            c.node('U2', 'CMD2', shape='box', fillcolor='lightcyan')
            c.node('U3', 'CMD3', shape='box', fillcolor='lightcyan')
            c.node('U4', 'CMD4', shape='box', fillcolor='lightcyan')
        
        # Redo stack
        with dot.subgraph(name='cluster_redo') as c:
            c.attr(label='Redo Stack\n(empty)', style='rounded', fillcolor='lightyellow')
            c.node('R0', '(empty)', shape='plaintext')
        
        # DOM
        dot.node('DOM', 'ContentEditable\n<div>Hello World</div>', 
                fillcolor='lightgreen', shape='box3d')
        
        # Flow
        dot.edge('User', 'CMD1', 'create')
        dot.edge('User', 'CMD2', 'create')
        dot.edge('User', 'CMD3', 'create')
        dot.edge('User', 'CMD4', 'create')
        dot.edge('CMD1', 'U1', 'push')
        dot.edge('CMD2', 'U2', 'push')
        dot.edge('CMD3', 'U3', 'push')
        dot.edge('CMD4', 'U4', 'push')
        dot.edge('CMD4', 'DOM', 'execute()')
        
        # Undo operation
        dot.node('Undo', 'Ctrl+Z\n(Undo)', fillcolor='lightcoral', shape='diamond')
        dot.edge('Undo', 'U4', 'pop()', style='dashed', color='red')
        dot.edge('U4', 'R0', 'push to redo', style='dashed', color='red')
        
        return dot
    except Exception as e:
        print(f"Error creating editor diagram: {e}")
        return None

def create_pdf_architecture():
    """PDF: Show parsing pipeline from binary to rendered pages."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='PDF Parsing and Rendering Pipeline', format='png')
        dot.attr(rankdir='TB', size='10,12')
        dot.attr('node', shape='box', style='rounded,filled')
        
        # Input
        dot.node('PDF', 'PDF Binary\n(ArrayBuffer)\n%PDF-1.7...', 
                fillcolor='lightcoral', shape='cylinder')
        
        # Parsing stage
        with dot.subgraph(name='cluster_parse') as c:
            c.attr(label='Parsing (Web Worker)', style='rounded')
            c.node('Stream', 'BinaryStream\nByte reading', fillcolor='lightblue')
            c.node('XRef', 'Cross-Reference\nTable parsing', fillcolor='lightblue')
            c.node('Catalog', 'Document Catalog\nPage tree', fillcolor='lightblue')
            c.node('Decompress', 'Stream Decoder\nFlate, LZW, ASCII85', fillcolor='lightgreen')
        
        # Page content
        dot.node('Page', 'Page Objects\nContent streams\nResources', 
                fillcolor='lightyellow')
        
        # Rendering stage
        with dot.subgraph(name='cluster_render') as c:
            c.attr(label='Rendering (Main Thread)', style='rounded')
            c.node('Ops', 'PDF Operators\n40+ graphics ops', fillcolor='lightcyan')
            c.node('Canvas', 'Canvas 2D API\nPath, text, images', fillcolor='lightyellow')
            c.node('Text', 'Text Layer\nInvisible overlay\nfor selection', fillcolor='lightgreen')
        
        # Annotations
        dot.node('Annot', 'Annotations\nOverlay rendering', 
                fillcolor='lightcoral')
        
        # Output
        dot.node('Screen', 'Rendered Page\n(Canvas + Text)', 
                fillcolor='lightgreen', shape='box3d')
        
        # Flow
        dot.edge('PDF', 'Stream', '1. Parse')
        dot.edge('Stream', 'XRef', '2. Find objects')
        dot.edge('XRef', 'Catalog', '3. Get pages')
        dot.edge('Catalog', 'Page', '4. Extract content')
        dot.edge('Page', 'Decompress', '5. Decompress streams')
        dot.edge('Decompress', 'Ops', '6. Parse operators')
        dot.edge('Ops', 'Canvas', '7. Execute graphics')
        dot.edge('Ops', 'Text', '8. Extract text')
        dot.edge('Canvas', 'Screen', '9. Display')
        dot.edge('Text', 'Screen')
        dot.edge('Annot', 'Screen', 'Overlay')
        
        return dot
    except Exception as e:
        print(f"Error creating PDF diagram: {e}")
        return None

def save_diagram(diagram, filename, output_dir='diagrams'):
    """Save diagram to file."""
    if diagram is None:
        return False
    
    try:
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Save diagram
        output_path = os.path.join(output_dir, filename.replace('.png', ''))
        diagram.render(output_path, format='png', cleanup=True)
        
        print(f"  ✓ Generated: {output_dir}/{filename}")
        return True
    except Exception as e:
        print(f"  ✗ Failed to save {filename}: {e}")
        return False

def replace_ascii_diagrams_with_images(markdown_file, output_file=None, diagram_dir='diagrams'):
    """Insert diagram images after specific section headings."""
    if output_file is None:
        output_file = markdown_file

    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Define insertions: section heading -> diagram path
    primary_insertions = {
        '# Virtualized Infinite List with Dynamic Heights': 'virtuallist-architecture.png',
        '# High-Fidelity Pixel-Perfect Zoomable Canvas': 'canvas-architecture.png',
        '# Reactive Formulas Engine (Spreadsheet-like)': 'reactive-engine-architecture.png',
        '# DOM-Based Spreadsheet Renderer (Excel Clone)': 'spreadsheet-architecture.png',
        '# High-Volume Real-Time Charts with Backfill': 'charts-architecture.png',
        '# ContentEditable Rich-Text Editor with Undo/Redo': 'editor-architecture.png',
        '# Browser-Native PDF Viewer with Annotations': 'pdf-architecture.png',
    }

    current_section = None
    modified_lines = []
    i = 0
    inserted_count = 0
    in_code_block = False

    while i < len(lines):
        line = lines[i]

        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block

        modified_lines.append(line)

        # Check if this line matches any section heading
        for heading, diagram in primary_insertions.items():
            if line.strip() == heading:
                current_section = diagram
                # Skip blank line if present
                if i + 1 < len(lines) and lines[i + 1].strip() == '':
                    i += 1
                    modified_lines.append(lines[i])

                # Insert diagram
                diagram_path = f'{diagram_dir}/{diagram}'
                diagram_text = f'\n![Architecture Diagram]({diagram_path})\n\n'
                modified_lines.append(diagram_text)
                inserted_count += 1
                print(f"  Inserted diagram at: {heading[:50]}...")
                break

        # Also insert at "**Architecture Overview**:"
        if not in_code_block and current_section:
            if line.strip() == '**Architecture Overview**:':
                # Skip blank line if present
                if i + 1 < len(lines) and lines[i + 1].strip() == '':
                    i += 1
                    modified_lines.append(lines[i])

                # Insert diagram
                diagram_path = f'{diagram_dir}/{current_section}'
                diagram_text = f'\n![Architecture Diagram]({diagram_path})\n\n'
                modified_lines.append(diagram_text)
                inserted_count += 1
                print(f"  Inserted diagram at Architecture Overview for: {current_section}")

        i += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(modified_lines)

    print(f"Inserted {inserted_count} diagrams total into: {output_file}")

def main():
    """Generate all diagrams."""
    print("=" * 60)
    print("Generating unique architectural diagrams for each chapter")
    print("=" * 60)
    
    # Check dependencies
    if not install_dependencies():
        print("\nSkipping diagram generation (dependencies not found)")
        return 1
    
    print("\nGenerating diagrams...")
    
    # Generate each diagram
    diagrams = {
        'virtuallist-architecture.png': create_virtuallist_architecture(),
        'canvas-architecture.png': create_canvas_architecture(),
        'charts-architecture.png': create_charts_architecture(),
        'spreadsheet-architecture.png': create_spreadsheet_architecture(),
        'reactive-engine-architecture.png': create_reactive_engine_architecture(),
        'editor-architecture.png': create_editor_architecture(),
        'pdf-architecture.png': create_pdf_architecture(),
    }
    
    # Save diagrams
    success_count = 0
    for filename, diagram in diagrams.items():
        if save_diagram(diagram, filename):
            success_count += 1
    
    print(f"\n{success_count}/{len(diagrams)} diagrams generated successfully")
    
    # Insert diagrams into markdown
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else input_file
        
        print(f"\nInserting diagrams into: {output_file}")
        replace_ascii_diagrams_with_images(input_file, output_file)
    
    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
