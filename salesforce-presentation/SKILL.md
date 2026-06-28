---
name: salesforce-presentation
description: Build Salesforce-branded presentations (.pptx) that strictly comply with official Salesforce Brand Central guidelines. Use this skill whenever creating, editing, or designing any slide deck, presentation, or set of slides that must follow Salesforce brand standards — including sales decks, QBRs, customer proposals, event decks, internal readouts, or any other presentation format. Also trigger when the user asks to "make slides", "build a deck", "create a presentation", or "put this in a deck" in a Salesforce context, or when they explicitly invoke Salesforce brand guidelines. This skill overrides the default pptx skill's color, font, and layout guidance with Salesforce-specific requirements.
---

# Salesforce Presentation Skill

Produces pptx files that comply strictly with Salesforce Brand Central guidelines.
This skill wraps the pptx skill's technical execution while enforcing Salesforce brand constraints as hard rules, not suggestions.

---

## Step 0 — Read brand rules before anything else

**Before writing a single line of code or making any layout decisions, read:**

```
~/.claude/skills/salesforce-presentation/references/brand-system.md
```

This file is the authoritative brand ruleset. Every color, font, spacing, shape, and icon decision must comply with it. Do not rely on memory of these guidelines — read the file.

**Technical execution uses python-pptx** (installed at system level). Generate slides by writing a Python script that uses the `pptx` library and running it with `python3`. See the generation pattern in Step 3 below.

---

## Step 1 — Gather requirements

Before generating slides, confirm:

1. **Content**: What is the deck about? What's the audience and goal?
2. **Slide count**: How many slides? (If not specified, propose a structure and confirm)
3. **Deck type**: Sales proposal / QBR / event / internal readout / other?
4. **Content provided**: Is the user providing the content, or should it be generated?
5. **Data**: Any charts or statistics? (Need data and attribution source)

If content is thin, propose an outline first and get confirmation before building.

---

## Step 2 — Plan the deck structure

Map each slide to a pattern from:
```
~/.claude/skills/salesforce-presentation/references/slide-patterns.md
```

Always open with Pattern 1 (Title/Hero) and close with Pattern 9 (Closing).
Use Pattern 2 (Section Divider) between major sections.
Propose the structure to the user if the deck is more than 5 slides.

---

## Step 3 — Build with brand-compliant defaults

### Color defaults (pptx hex values)

Override any pptx skill color suggestions with these:

| Role | Color name | Hex |
|------|-----------|-----|
| Title slide background gradient start | Electric Blue 15 | `001E5B` |
| Title slide background gradient end | Cloud Blue 68 | `00B3FF` |
| Content slide background | Cloud Blue 95 | `EAF5FE` |
| Alternative content background | White | `FFFFFF` |
| Section divider background | Electric Blue 30 | `022AC0` |
| Primary headline color (light bg) | Electric Blue 15 | `001E5B` |
| Primary headline color (dark bg) | White | `FFFFFF` |
| Body text (light bg) | Electric Blue 30 | `022AC0` |
| Body text (dark bg) | Cloud Blue 80 | `90D0FE` |
| Accent / emphasis | Cloud Blue 68 | `00B3FF` |
| Secondary accent (use sparingly) | Teal 80 | `04E1CB` |
| Data highlight accent | Yellow 80 | `FCC003` |

### Font defaults (pptx)

All text uses **Arial** (closest available substitute for Salesforce's proprietary fonts).

| Level | Font | Bold | Size |
|-------|------|------|------|
| H1 headline | Arial | Yes | 48pt (adjust to fill) |
| H2 subhead | Arial | Yes | 28–32pt |
| H3–H4 | Arial | Yes | 20–24pt |
| Body (B1) | Arial | No | 14–16pt |
| Small body (B2) | Arial | No | 11–13pt |
| CTA | Arial | Yes | 14–16pt |
| Caption | Arial | No | 9–11pt |
| Data numerals | Arial | Yes | 60–72pt |

**Critical type rules:**
- H1 line spacing: set to exactly 100% (not default 110%)
- Body line spacing: 150%
- No ALL CAPS on headlines
- No bold on body copy paragraphs
- Sentence case throughout

### Grid and spacing defaults

For 16:9 slides (10" × 7.5"):
- Outer margins: 0.4" on all sides (≈5% of shortest dimension)
- Gutters between columns: 0.4"
- Minimum gap between elements: 0.3"
- Logo: 0.75" wide minimum, placed in corner within margin

### python-pptx generation pattern

Write a Python script and run it with `python3`. Basic scaffold:

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import pptx.oxml.ns as nsmap
from lxml import etree

prs = Presentation()
prs.slide_width  = Inches(10)
prs.slide_height = Inches(7.5)   # 4:3 — use 5.625 for 16:9

blank_layout = prs.slide_layouts[6]  # blank

# Add a slide
slide = prs.slides.add_slide(blank_layout)

# Fill background color
bg = slide.background
fill = bg.fill
fill.solid()
fill.fore_color.rgb = RGBColor(0x00, 0x1E, 0x5B)  # Electric Blue 15

# Add text box
from pptx.util import Inches, Pt
txBox = slide.shapes.add_textbox(Inches(0.4), Inches(0.4), Inches(9.2), Inches(2))
tf = txBox.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Headline text"
p.font.bold = True
p.font.size = Pt(48)
p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
p.font.name = "Arial"

# Set H1 line spacing to exactly 100%
from pptx.oxml.ns import qn
from lxml import etree
pPr = p._p.get_or_add_pPr()
lnSpc = etree.SubElement(pPr, qn('a:lnSpc'))
spcPct = etree.SubElement(lnSpc, qn('a:spcPct'))
spcPct.set('val', '100000')  # 100% in thousandths of a percent

prs.save("/Users/treis/Desktop/output.pptx")
print("Saved.")
```

Key python-pptx notes:
- All measurements in EMU (English Metric Units): 1 inch = 914400 EMU. Use `Inches()` helper.
- Colors via `RGBColor(r, g, b)` with hex split into three ints
- Line spacing 100% requires direct XML manipulation (shown above) — python-pptx has no direct API
- For solid shape fills: `shape.fill.solid(); shape.fill.fore_color.rgb = RGBColor(...)`
- Rounded rectangles: use `add_shape(MSO_SHAPE_TYPE.ROUNDED_RECTANGLE, ...)` with `shape.adjustments[0]` for corner radius
- Save to `/Users/treis/Desktop/` for easy access, or another path if specified

---

## Step 4 — Brand compliance enforcement

Before finalizing any slide, apply the compliance checklist from brand-system.md Section 10.

**Hard stops — fix before delivering:**
- Any cloud imagery, cloud-shaped icons, or cloud-named elements → remove
- ALL CAPS headlines → convert to sentence case
- Color pairings that fail AA contrast → replace
- 3D and 2D icons mixed on same slide → standardize
- Non-approved chart types → replace with bar, line, or circle
- Data without attribution → add source line
- Unapproved colors (off-palette neutrals, arbitrary hex values) → replace
- Decorative accent bars or edge stripes → remove
- Underlines beneath titles → remove

---

## Step 5 — QA

Run the generated script, open the .pptx in PowerPoint or Keynote, and visually verify each slide.

Salesforce-specific QA:
- Run the compliance checklist (brand-system.md Section 10)
- Verify the "sandwich" structure: title slide dark → content slides light → closing slide dark
- Confirm no slide uses the same layout as the slide immediately before it
- Verify at least one visual element (icon, chart, image, or shape) per slide

---

## Step 6 — Deliver

Save the .pptx to `/Users/treis/Desktop/` (or a path the user specifies) and tell the user where to find it.

PDF export: open in PowerPoint and export, or the user can request a PDF version.

---

## Key constraints summary

These are absolute — they cannot be overridden by user preference unless the user explicitly says they want to break from Salesforce brand guidelines:

1. **No cloud imagery** anywhere except the logo itself
2. **No off-palette colors** — only hex values from brand-system.md
3. **80/20 rule** — primary blues dominate; secondary colors ≤20%
4. **AA contrast** on all color pairings
5. **Sentence case** headlines — never ALL CAPS
6. **Arial only** for fonts (substituting for Salesforce proprietary typefaces)
7. **H1 line spacing = 100%** — must be set manually
8. **Approved chart types only**: bar, line, circle
9. **All data attributed** below charts
10. **No decorative edge stripes, accent bars, or title underlines**

---

## Reference files

| File | When to read |
|------|-------------|
| `references/brand-system.md` | Before every build — colors, type, layout, shapes, icons, data viz, cloud guidance |
| `references/slide-patterns.md` | When planning deck structure and choosing per-slide layouts |
