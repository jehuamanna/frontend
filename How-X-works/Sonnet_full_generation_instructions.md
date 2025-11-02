# 🧭 Sonnet 4.5 — Full Documentation Generation Instructions

This file contains **everything Sonnet 4.5 needs** to automatically generate, continue, and complete the full JavaScript & Browser Design Pattern documentation project.

---

## 🧩 PURPOSE

You will instruct Sonnet 4.5 (or similar) to:
- Generate in-depth documentation for **all 59 patterns**.
- Follow the **SONNET MASTER DIRECTIVE** and **continuation protocol** exactly.
- Automatically create structured markdown output, Python diagram snippets, and update `progress.json`.

---

## 🧭 MASTER COMMAND (Copy-Paste into Sonnet)

```
START TASK: Full Documentation Generation (Follow SONNET MASTER DIRECTIVE)

You have the SONNET MASTER DIRECTIVE already (top of file). Now act as follows — do not ask follow-ups; proceed.

PRIMARY OBJECTIVE
- Generate complete, in-depth documentation for each pattern listed in `javascript_patterns_full_instruction_with_header.md`, starting with:
  **Creational — Constructor Pattern**
- Continue sequentially through every pattern in the checklist until all are DONE.
- Use the CONTINUATION RULES exactly as defined in the Master Directive.

OUTPUT RULES (strict)
1. For each pattern produce a section **exactly** using the Example Section Template:
   - Begin with: `## CONTINUED: <Category> — <Pattern Name>`
   - Provide these subsections (in this order):
     1. Concept Overview (200–600 words)
     2. Problem It Solves
     3. Detailed Implementation (runnable ESNext code)
     4. Browser/DOM Usage
     5. Python Architecture Diagram Snippet (python file path & code)
     6. Real-world Use Cases
     7. Performance & Trade-offs
     8. Related Patterns
     9. RFC-style Summary (table)
   - End the segment with either:
     - If you can continue within limits: directly continue to the next pattern.
     - If you reach the token limit: output **only** the continuation marker:
       `--- [CONTINUE FROM HERE: <Next Pattern Name>] ---`
2. Append each finished pattern section to `master_output.md`. If section is partial (token limit forced stop), append the partial output and issue the continuation marker.
3. For `Python Architecture Diagram Snippet` include a small, runnable python script that:
   - Uses matplotlib and networkx (or plain matplotlib if nodes/edges simple).
   - Saves a PNG as `docs/images/<pattern_slug>.png`
   - Is saved to `build/diagrams/<pattern_slug>.py` (so automation can run it later).
   Example snippet header:
   ```python
   # ./build/diagrams/constructor_pattern.py
   import matplotlib.pyplot as plt
   import networkx as nx
   G = nx.DiGraph()
   # ... nodes/edges ...
   plt.savefig("docs/images/constructor_pattern.png")
   ```
4. Mark the pattern as `"done"` in `progress.json` only when:
   - All required subsections are present (including the Python snippet).
   - The snippet file has been created (you may create the file content; actual png generation is done by the build step).
   - If you only produced a partial section (token limit), keep `progress.json` as `"pending"` and end with continuation marker.
5. Directory and file creation:
   - Ensure these paths exist in your output:
     - `docs/images/` (pngs)
     - `build/diagrams/` (python snippets)
     - `master_output.md` (append-only aggregated doc)
     - `progress.json` (update statuses)
6. Formatting:
   - Use fenced code blocks for all code.
   - Use Markdown headings for subsections.
   - No external links unless requested.
   - Keep language technical, precise, and consistent.

CONTINUATION BEHAVIOR
- If truncated, emit **only** the continuation marker line (no explanation).
- When the user or automation sends the continuation request back to you including the marker, resume immediately from that marker using the same rules.
- When a pattern completes in full, append `--- [SECTION COMPLETE: <pattern name>] ---` to the end of that section.

START NOW
- Begin with: `## CONTINUED: Creational — Constructor Pattern`
- Produce a full section following the template above.
- If able, continue through the entire Creational category; otherwise, end with the continuation marker identifying the next pattern.
```

---

## 🧠 SUPERVISOR AUTOMATION SCRIPT (Python)

Save as: `tools/sonnet_runner.py`

```python
#!/usr/bin/env python3
import json
import os
from pathlib import Path
# Replace this with your real client import and usage
# from sonnet_api import SonnetClient

ROOT = Path.cwd()
SCAFFOLD = ROOT / "javascript_patterns_full_instruction_with_header.md"
MASTER_OUTPUT = ROOT / "master_output.md"
PROGRESS_FILE = ROOT / "progress.json"
BUILD_DIAGS = ROOT / "build" / "diagrams"
IMAGES_DIR = ROOT / "docs" / "images"

# Ensure directories
BUILD_DIAGS.mkdir(parents=True, exist_ok=True)
IMAGES_DIR.mkdir(parents=True, exist_ok=True)
MASTER_OUTPUT.write_text("# Master Output\n\n", encoding="utf-8")

# Load progress
with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
    progress = json.load(f)

def find_next():
    for cat, pats in progress.items():
        for name, status in pats.items():
            if status == "pending":
                return cat, name
    return None, None

# Replace with your Sonnet client/wrapper
class DummyClient:
    def generate(self, prompt, max_tokens=4000):
        raise NotImplementedError("Replace DummyClient with your real Sonnet client")

client = DummyClient()

while True:
    cat, pattern = find_next()
    if not cat:
        print("All done.")
        break

    prompt_header = open(SCAFFOLD, "r", encoding="utf-8").read()
    prompt = f"{prompt_header}\n\n# START\nBegin documentation for: {pattern}\nFollow the SONNET MASTER DIRECTIVE and CONTINUATION RULES. Output must be appended to master_output.md.\n"

    try:
        resp = client.generate(prompt, max_tokens=8000)
    except Exception as e:
        print("Client error:", e)
        break

    text = resp.text  # adjust per API

    with open(MASTER_OUTPUT, "a", encoding="utf-8") as f:
        f.write(text)
        f.write("\n\n")

    marker_prefix = "--- [CONTINUE FROM HERE:"
    if marker_prefix in text:
        print("Continuation marker found; will continue from marker.")
        cont_marker_line = [line for line in text.splitlines() if marker_prefix in line][0]
        cont_prompt = f"Refer to previous output. Continue from marker:\n{cont_marker_line}\nDo not recap. Begin with '## CONTINUED:'"
        try:
            cont_resp = client.generate(cont_prompt, max_tokens=8000)
        except Exception as e:
            print("Client error while continuing:", e)
            break
        cont_text = cont_resp.text
        with open(MASTER_OUTPUT, "a", encoding="utf-8") as f:
            f.write(cont_text)
            f.write("\n\n")
        continue
    else:
        progress[cat][pattern] = "done"
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(progress, f, indent=2)
        print(f"Marked done: {cat} -> {pattern}")
        continue
```

---

## 📁 REQUIRED DIRECTORY STRUCTURE

```
project_root/
├── build/
│   └── diagrams/          # Sonnet writes .py diagram snippets here
├── docs/
│   └── images/            # PNGs generated by Python build step
├── tools/
│   └── sonnet_runner.py   # Supervisor automation script
├── progress.json          # Pattern tracking state
├── javascript_patterns_full_instruction_with_header.md
├── Sonnet_continuation_template.md
└── master_output.md       # Aggregated documentation file
```

---

## ⚙️ BUILD STEP (Diagrams)

To generate all diagrams after documentation is complete, run:
```bash
python ./build/diagrams/*.py
```

All PNGs will appear under `docs/images/` and get linked automatically in the Markdown.

---

## ✅ SUMMARY

| Step | Description |
|------|--------------|
| 1 | Load `javascript_patterns_full_instruction_with_header.md` into Sonnet |
| 2 | Paste the **Master Command** above |
| 3 | Let Sonnet start from Constructor Pattern |
| 4 | If it stops, re-feed continuation marker |
| 5 | Use `tools/sonnet_runner.py` to automate the loop |
| 6 | Run `python ./build/diagrams/*.py` to render diagrams |
| 7 | Merge and polish final docs |

---

**All tools and templates are now complete.**
Sonnet can fully auto-generate, resume, and finish the complete design pattern documentation suite.
