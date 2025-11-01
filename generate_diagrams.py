#!/usr/bin/env python3
"""
Generate beautiful diagrams from code and insert them into markdown.
Uses Graphviz for flowcharts, architecture diagrams, and dependency graphs.
"""

import os
import re
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
        print("\nOr create a virtual environment:")
        print("  python3 -m venv venv")
        print("  source venv/bin/activate")
        print("  pip install graphviz")
        return False
    
    # Check if graphviz system package is installed
    if os.system("which dot > /dev/null 2>&1") != 0:
        print("WARNING: Graphviz system package not found.")
        print("Install with: sudo apt-get install graphviz")
        return False
    
    return True

def create_virtuallist_architecture():
    """Create VirtualList architecture diagram."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='VirtualList Architecture', format='png')
        dot.attr(rankdir='TB', size='10,8')
        dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue')
        
        # Main component
        dot.node('VL', 'VirtualList Component', fillcolor='lightcoral', fontsize='14', fontname='Arial Bold')
        
        # Sub-components
        dot.node('FT', 'Fenwick Tree\n(Height Index)\nO(log n) queries', fillcolor='lightgreen')
        dot.node('VP', 'Viewport\n(Visible Area)\n10-20 items rendered', fillcolor='lightyellow')
        dot.node('SM', 'Scroll Manager\nRAF-based\nThreshold rendering', fillcolor='lightcyan')
        dot.node('RO', 'ResizeObserver\nContainer resize\nItem height tracking', fillcolor='plum')
        
        # Connections
        dot.edge('VL', 'FT', label='height queries')
        dot.edge('VL', 'VP', label='render items')
        dot.edge('VL', 'SM', label='scroll events')
        dot.edge('VL', 'RO', label='resize events')
        dot.edge('SM', 'FT', label='calculate range')
        dot.edge('RO', 'FT', label='update heights')
        
        return dot
    except Exception as e:
        print(f"Error creating VirtualList diagram: {e}")
        return None

def create_canvas_architecture():
    """Create Canvas architecture diagram."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='Canvas Architecture', format='png')
        dot.attr(rankdir='TB', size='10,8')
        dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue')
        
        # Main component
        dot.node('ZC', 'ZoomableCanvas', fillcolor='lightcoral', fontsize='14', fontname='Arial Bold')
        
        # Sub-components
        dot.node('CM', 'Canvas Manager\nHi-DPI support\nTransform matrix', fillcolor='lightgreen')
        dot.node('LM', 'Layer Manager\nVector/Raster layers\nCaching', fillcolor='lightyellow')
        dot.node('RM', 'Render Engine\nRAF loop\nDirty tracking', fillcolor='lightcyan')
        dot.node('IM', 'Interaction\nPan/Zoom\nSelection', fillcolor='plum')
        dot.node('QT', 'Quadtree\nSpatial indexing\nCulling', fillcolor='orange')
        
        # Connections
        dot.edge('ZC', 'CM', label='setup')
        dot.edge('ZC', 'LM', label='layers')
        dot.edge('ZC', 'RM', label='render')
        dot.edge('ZC', 'IM', label='events')
        dot.edge('RM', 'LM', label='draw layers')
        dot.edge('RM', 'QT', label='query visible')
        dot.edge('IM', 'RM', label='trigger redraw')
        
        return dot
    except Exception as e:
        print(f"Error creating Canvas diagram: {e}")
        return None

def create_reactive_engine_architecture():
    """Create Reactive Engine architecture diagram."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='Reactive Engine', format='png')
        dot.attr(rankdir='LR', size='12,8')
        dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue')
        
        # Core components
        dot.node('SIG', 'Signal\n(State)', fillcolor='lightcoral', shape='ellipse')
        dot.node('COMP', 'Computed\n(Derived)', fillcolor='lightgreen', shape='ellipse')
        dot.node('EFF', 'Effect\n(Side effects)', fillcolor='lightyellow', shape='ellipse')
        
        # Supporting components
        dot.node('TRK', 'TrackingContext\nAuto-dependency\ntracking', fillcolor='lightcyan')
        dot.node('SCH', 'Scheduler\nBatching\nMicrotask queue', fillcolor='plum')
        dot.node('TOPO', 'TopologicalSort\nGlitch-free\nupdates', fillcolor='orange')
        
        # Data flow
        dot.edge('SIG', 'COMP', label='reads')
        dot.edge('COMP', 'EFF', label='triggers')
        dot.edge('SIG', 'EFF', label='subscribes')
        dot.edge('TRK', 'COMP', label='tracks deps', style='dashed')
        dot.edge('TRK', 'EFF', label='tracks deps', style='dashed')
        dot.edge('COMP', 'SCH', label='schedule update')
        dot.edge('EFF', 'SCH', label='schedule run')
        dot.edge('SCH', 'TOPO', label='sort updates')
        dot.edge('TOPO', 'COMP', label='execute')
        dot.edge('TOPO', 'EFF', label='execute')
        
        return dot
    except Exception as e:
        print(f"Error creating Reactive Engine diagram: {e}")
        return None

def create_spreadsheet_architecture():
    """Create Spreadsheet architecture diagram."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='Spreadsheet Architecture', format='png')
        dot.attr(rankdir='TB', size='12,10')
        dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue')
        
        # Main component
        dot.node('SS', 'Spreadsheet', fillcolor='lightcoral', fontsize='14', fontname='Arial Bold')
        
        # Data layer
        with dot.subgraph(name='cluster_0') as c:
            c.attr(label='Data Layer', style='filled', color='lightgrey')
            c.node('SM', 'Sparse Matrix\nO(1) access\nMemory efficient', fillcolor='lightgreen')
            c.node('VV', 'Virtual Viewport\n2D scrolling\nDOM pooling', fillcolor='lightyellow')
        
        # Formula layer
        with dot.subgraph(name='cluster_1') as c:
            c.attr(label='Formula Layer', style='filled', color='lightgrey')
            c.node('FP', 'Formula Parser\nTokenizer\nAST', fillcolor='lightcyan')
            c.node('DG', 'Dependency Graph\nDAG\nTopo sort', fillcolor='plum')
            c.node('FE', 'Formula Evaluator\nBuilt-in functions\nCell refs', fillcolor='orange')
        
        # UI layer
        with dot.subgraph(name='cluster_2') as c:
            c.attr(label='UI Layer', style='filled', color='lightgrey')
            c.node('KB', 'Keyboard Nav\nArrow keys\nTab', fillcolor='pink')
            c.node('SEL', 'Selection\nMulti-range\nDrag', fillcolor='lightblue')
            c.node('ED', 'Cell Editor\nInline edit\nFormula bar', fillcolor='wheat')
        
        # Connections
        dot.edge('SS', 'SM', label='data access')
        dot.edge('SS', 'VV', label='render')
        dot.edge('SS', 'FP', label='parse formula')
        dot.edge('FP', 'DG', label='build graph')
        dot.edge('DG', 'FE', label='eval order')
        dot.edge('FE', 'SM', label='get/set values')
        dot.edge('VV', 'SM', label='read data')
        dot.edge('KB', 'SEL', label='update')
        dot.edge('SEL', 'ED', label='trigger edit')
        dot.edge('ED', 'FP', label='submit')
        
        return dot
    except Exception as e:
        print(f"Error creating Spreadsheet diagram: {e}")
        return None

def create_charts_architecture():
    """Create Real-time Charts architecture diagram."""
    try:
        from graphviz import Digraph
        
        dot = Digraph(comment='Real-time Charts', format='png')
        dot.attr(rankdir='LR', size='12,8')
        dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue')
        
        # Data pipeline
        with dot.subgraph(name='cluster_0') as c:
            c.attr(label='Data Pipeline', style='filled', color='lightgrey')
            c.node('WS', 'WebSocket\nReal-time stream', fillcolor='lightcoral')
            c.node('WW', 'Web Worker\nBackground\nprocessing', fillcolor='lightgreen')
            c.node('RB', 'Ring Buffer\nCircular queue\nFixed size', fillcolor='lightyellow')
            c.node('TSA', 'TimeSeriesAgg\nHierarchical\ndata', fillcolor='lightcyan')
        
        # Rendering
        with dot.subgraph(name='cluster_1') as c:
            c.attr(label='Rendering', style='filled', color='lightgrey')
            c.node('CV', 'Canvas 2D\nGPU accelerated', fillcolor='plum')
            c.node('RAF', 'RAF Loop\n60fps target', fillcolor='orange')
            c.node('CULL', 'Viewport Cull\nVisible data only', fillcolor='pink')
        
        # Flow
        dot.edge('WS', 'WW', label='raw data')
        dot.edge('WW', 'RB', label='parsed')
        dot.edge('WW', 'TSA', label='aggregate')
        dot.edge('RB', 'CULL', label='latest data')
        dot.edge('TSA', 'CULL', label='historical')
        dot.edge('CULL', 'CV', label='visible range')
        dot.edge('RAF', 'CULL', label='trigger')
        dot.edge('CV', 'RAF', label='complete')
        
        return dot
    except Exception as e:
        print(f"Error creating Charts diagram: {e}")
        return None

def create_all_diagrams(output_dir='diagrams'):
    """Generate all diagrams."""
    Path(output_dir).mkdir(exist_ok=True)
    
    diagrams = {
        'virtuallist-architecture': create_virtuallist_architecture(),
        'canvas-architecture': create_canvas_architecture(),
        'reactive-engine-architecture': create_reactive_engine_architecture(),
        'spreadsheet-architecture': create_spreadsheet_architecture(),
        'charts-architecture': create_charts_architecture(),
    }
    
    generated = []
    for name, diagram in diagrams.items():
        if diagram:
            output_path = os.path.join(output_dir, name)
            try:
                diagram.render(output_path, cleanup=True)
                generated.append(f"{output_path}.png")
                print(f"Generated: {output_path}.png")
            except Exception as e:
                print(f"Error rendering {name}: {e}")
    
    return generated

def replace_ascii_diagrams_with_images(markdown_file, output_file=None, diagram_dir='diagrams'):
    """Insert diagram images after specific section headings and Architecture Overview sections."""
    if output_file is None:
        output_file = markdown_file
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Define primary insertions: section heading -> diagram path
    primary_insertions = {
        '# Virtualized Infinite List with Dynamic Heights': 'virtuallist-architecture.png',
        '# High-Fidelity Pixel-Perfect Zoomable Canvas': 'canvas-architecture.png',
        '# Reactive Formulas Engine (Spreadsheet-like)': 'reactive-engine-architecture.png',
        '# DOM-Based Spreadsheet Renderer (Excel Clone)': 'spreadsheet-architecture.png',
        '# High-Volume Real-Time Charts with Backfill': 'charts-architecture.png',
    }
    
    # Track which sections we've seen to know which diagram to insert at Architecture Overview
    current_section = None
    
    modified_lines = []
    i = 0
    inserted_count = 0
    removed_count = 0
    in_code_block = False
    skip_until_code_end = False
    
    while i < len(lines):
        line = lines[i]
        
        # Track code blocks to avoid processing code
        if line.strip().startswith('```'):
            # Check if this is an ASCII diagram block to remove
            if not in_code_block and current_section:
                # Look ahead to see if this is an ASCII art diagram
                # (contains box-drawing characters)
                is_ascii_diagram = False
                for j in range(i, min(i + 20, len(lines))):
                    if any(char in lines[j] for char in ['┌', '│', '├', '└', '─', '┐', '┘', '┤', '┬', '┴']):
                        is_ascii_diagram = True
                        break
                    if lines[j].strip().startswith('```'):
                        break
                
                if is_ascii_diagram:
                    skip_until_code_end = True
                    removed_count += 1
                    i += 1
                    continue
            
            in_code_block = not in_code_block
            
            # If we're ending a block we're skipping, stop skipping
            if not in_code_block and skip_until_code_end:
                skip_until_code_end = False
                i += 1
                continue
        
        # Skip lines in ASCII diagram blocks
        if skip_until_code_end:
            i += 1
            continue
        
        modified_lines.append(line)
        
        # Check if this line matches any of our section headings
        for heading, diagram in primary_insertions.items():
            if line.strip() == heading:
                current_section = diagram
                # Skip the next line if it's blank
                if i + 1 < len(lines) and lines[i + 1].strip() == '':
                    i += 1
                    modified_lines.append(lines[i])
                
                # Insert diagram after heading and blank line
                diagram_path = f'{diagram_dir}/{diagram}'
                diagram_text = f'\n![Architecture Diagram]({diagram_path})\n\n'
                modified_lines.append(diagram_text)
                inserted_count += 1
                print(f"  Inserted diagram at heading: {heading[:50]}...")
                break
        
        # Also insert at "**Architecture Overview**:" if we're in a known section
        if not in_code_block and current_section:
            if line.strip() == '**Architecture Overview**:':
                # Skip blank line if present
                if i + 1 < len(lines) and lines[i + 1].strip() == '':
                    i += 1
                    modified_lines.append(lines[i])
                
                # Insert diagram after Architecture Overview heading
                diagram_path = f'{diagram_dir}/{current_section}'
                diagram_text = f'\n![Architecture Diagram]({diagram_path})\n\n'
                modified_lines.append(diagram_text)
                inserted_count += 1
                print(f"  Inserted diagram at Architecture Overview for: {current_section}")
                
                # Now skip the ASCII art code block that follows
                # Look ahead for code fence with ASCII art
                j = i + 1
                # Skip any blank lines
                while j < len(lines) and lines[j].strip() == '':
                    j += 1
                
                # Check if we're at a code fence
                if j < len(lines) and lines[j].strip() == '```':
                    code_start = j
                    # Check if code block contains ASCII art
                    is_ascii_block = False
                    k = j + 1
                    while k < len(lines):
                        if lines[k].strip().startswith('```'):
                            # Found closing fence
                            if is_ascii_block:
                                # Skip from current position to end of code block
                                # (including closing fence and following blank lines)
                                i = k
                                # Skip trailing blank lines
                                while i + 1 < len(lines) and lines[i + 1].strip() == '':
                                    i += 1
                                removed_count += 1
                                print(f"    Removed ASCII art code block")
                            break
                        # Check for box-drawing characters
                        if any(char in lines[k] for char in ['┌', '│', '├', '└', '─', '┐', '┘', '┤', '┬', '┴', '┼']):
                            is_ascii_block = True
                        k += 1
        
        i += 1
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(modified_lines)
    
    print(f"Inserted {inserted_count} diagrams, removed {removed_count} ASCII art blocks")
    print(f"Output written to: {output_file}")

def main():
    print("=" * 60)
    print("Diagram Generation Tool")
    print("=" * 60)
    
    # Check dependencies
    if not install_dependencies():
        print("\nPlease install Graphviz and try again.")
        return
    
    # Generate diagrams
    print("\nGenerating diagrams...")
    generated = create_all_diagrams()
    
    print(f"\nGenerated {len(generated)} diagrams")
    
    # Optionally replace in markdown
    if len(sys.argv) > 1:
        markdown_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        print(f"\nProcessing markdown file: {markdown_file}")
        replace_ascii_diagrams_with_images(markdown_file, output_file)
    else:
        print("\nTo insert diagrams into markdown:")
        print("  python3 generate_diagrams.py <input.md> [output.md]")

if __name__ == '__main__':
    main()

