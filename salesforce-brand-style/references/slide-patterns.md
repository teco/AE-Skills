# Salesforce Slide Patterns — Content Type Reference

Use this file to select the right layout pattern for each slide's content type.
All patterns must be implemented using the brand-system.md color, type, and grid rules.

---

## Pattern 1: Title / Hero Slide

**Use for:** Deck opener, major section title

**Background:** Evening gradient (Electric Blue 15 → Electric Blue 30 → Electric Blue 50 → Cloud Blue 68)
**Shape:** Panorama (optional, top-right or spanning the right half)

**Layout:**
- Logo: top-left, snapped to grid
- H1 headline: large, white, left-aligned, bottom-left quadrant
- Optional subhead: Cloud Blue 80, below H1
- Optional visual: 3D icon or illustration in panorama shape, right side

**Type:**
- H1: Arial Bold, as large as possible (48–60pt for 16:9), 100% line spacing
- Subhead: Arial Bold, ~50% of H1 size, Cloud Blue 80

---

## Pattern 2: Section Divider

**Use for:** Transitioning between major deck sections

**Background:** Solid Electric Blue 30 or Electric Blue 15
**Shape:** None required

**Layout:**
- Section number (optional): small, Cloud Blue 80, top-left
- Section title: H1 white, centered vertically left-aligned, large
- Optional accent: single 3D icon or Teal 80 / Yellow 80 accent word

**Type:**
- H1: Arial Bold, ~48pt, white, 100% line spacing
- Section label: Arial Regular, ~12pt, Cloud Blue 80

---

## Pattern 3: Content — Two Column

**Use for:** Comparison, side-by-side concepts, feature + benefit

**Background:** White or Cloud Blue 95
**Shape:** Rounded rectangles as content containers (optional)

**Layout:**
- H2 headline: top, Electric Blue 15, left-aligned
- Left column: text / bullets / icon + label rows
- Right column: image, chart, 3D icon, or UI screenshot in rounded rectangle
- Logo: corner, small

**Type:**
- H2: Arial Bold, ~28–32pt, Electric Blue 15
- Body: Arial Regular, 14–16pt, Electric Blue 15 or Electric Blue 30
- Column labels: Arial Bold, ~16pt

---

## Pattern 4: Content — Full Bleed Visual + Copy

**Use for:** Customer story, product hero, aspirational moment

**Background:** Photography or gradient fills the slide; rounded rectangle contains copy

**Layout:**
- Photography/illustration: full bleed or right half
- Copy block: left side, in light rounded rectangle container (white or Cloud Blue 95 fill)
- H2 headline in container: Electric Blue 15
- Body copy in container: Electric Blue 30

**Important:** If photography contains a device, it must show Precise real UI.

---

## Pattern 5: Data / Stat Callout

**Use for:** Single powerful statistic, KPI highlight

**Background:** White or Cloud Blue 95 (solid color treatment) OR gradient (glass effect for high-impact)

**Layout:**
- Large numeral: center or left-aligned, Arial Bold, 60–72pt, Electric Blue 50 or Electric Blue 15
- Symbol (%, $): superscript, same font, smaller
- Abbreviation (M, B, K): same size as numeral
- Label: Arial Regular, 14pt, below numeral, Electric Blue 30
- Attribution: Arial Regular, 9pt, bottom of slide, Electric Blue 30 or muted
- Optional: single secondary color accent (Teal 80 or Yellow 80) on the numeral for emphasis

**Note:** One secondary color maximum across the entire callout.

---

## Pattern 6: Chart / Infographic Slide

**Use for:** Data storytelling, trend visualization, composition breakdown

**Background:** White or Cloud Blue 95

**Layout:**
- H2 headline: top-left, Electric Blue 15, Arial Bold
- Chart: center or right, using approved types only (bar, line, circle)
- Chart colors: primary blues unless product-specific or comparative
- Key insight / callout: left or below chart, large numeral treatment
- Data attribution: bottom of slide, small Arial Regular, muted

**Chart colors by use case:**
- Standard Salesforce: Cloud Blue 68, Electric Blue 50, Electric Blue 30, Electric Blue 15 (in that priority order)
- One secondary accent for a single highlighted data point
- Product-specific: use that product's approved color palette
- Comparative (Salesforce vs partner): Salesforce = blue; partner = non-blue colors from secondary palette

---

## Pattern 7: Quote / Testimonial

**Use for:** Customer voice, Trailblazer story

**Background:** White or Cloud Blue 95

**Layout:**
- Large quotation mark or open quote: Cloud Blue 80, decorative but minimal
- Quote text: H2 or large body size, Electric Blue 15, italic permitted
- Attribution: name bold + role/company regular, Arial, 12pt, Electric Blue 30
- Customer photo: circle shape, right side or bottom-left, with image breaking the circle edge
- Optional: customer logo (follow their brand guidelines for sizing)

---

## Pattern 8: Agenda / Table of Contents

**Use for:** Deck roadmap, meeting agenda

**Background:** White or Cloud Blue 95

**Layout:**
- H2 headline: "Agenda" or equivalent, top-left, Electric Blue 15
- Items: numbered list, Arial Bold for item title + Arial Regular for description
- Visual accent: small 3D icons or colored circles (Electric Blue 50 or Teal 80) as list markers
- Active/current item: Electric Blue 50 or Cloud Blue 68 highlight; others in Electric Blue 15

---

## Pattern 9: Closing / Thank You

**Use for:** Deck close, next steps, call to action

**Background:** Evening gradient (same as title slide — close the sandwich)
**Shape:** Panorama optional (mirroring or contrasting the title)

**Layout:**
- H1 closing statement: white, large, left-aligned (short — 3–5 words)
- CTA or next steps: Arial Bold, Cloud Blue 80, below H1
- Logo: prominent, bottom-left or bottom-center
- URL or contact: Arial Regular, Cloud Blue 80, small

---

## Pattern 10: Product UI Showcase

**Use for:** Demonstrating Salesforce product capability

**Background:** Cloud Blue 95 or White

**UI treatment options (choose based on context):**
- **Precise**: unmodified screenshot for demos and technical audiences
- **Hero**: enlarged key section, slightly redacted secondary elements — for presentations and website headers
- **Abstract/Vignette**: simplified, key elements only — for awareness contexts, digital ads

**Rules:**
- Device mockups must always show real UI (never conceptual UI)
- Conceptual UI (glass effect, simplified elements) is for storytelling only — never when showcasing an actual product experience
- Never mix UI perspectives or disproportionately displace paired devices

---

## Deck Construction Rules

### Slide sequence
- Open with Pattern 1 (Title/Hero)
- Use Pattern 2 (Section Divider) between major sections
- Close with Pattern 9 (Closing)
- This creates the "sandwich" structure: dark → light → dark

### Visual variety
- Never repeat the same layout on consecutive slides
- Rotate between: two-column, full-bleed, stat callout, chart
- Each slide must have at least one visual element (icon, chart, image, shape)

### Consistency within deck
- Commit to one corner radius and use it throughout (20px, 40px, or 60px)
- One background treatment per section (don't mix white and Cloud Blue 95 within a section)
- One visual motif (e.g., rounded rectangles for all containers) carried through every slide

### Icon usage in decks
- 3D icons for high-impact slides (title, section dividers, hero moments)
- 2D multicolor for content slides in lower-funnel decks
- Never mix 3D and 2D on the same slide
- Maximum two storytelling icons per slide

