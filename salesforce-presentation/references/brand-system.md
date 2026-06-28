# Salesforce Brand System — Presentation Reference

This file is the authoritative brand ruleset for all Salesforce presentation work.
Read this in full before generating any slide content, layout decisions, or color choices.

---

## 1. Brand Positioning

Salesforce is positioned as the leader in the **Agentic Enterprise**. Three traits define the personality:
- **Tight** — focused, intentional, no fluff
- **Bright** — energetic, optimistic, digitally vibrant
- **Bold** — confident, clear, disruptive

Every slide should embody at least one of these traits. When in doubt, default to Tight.

---

## 2. Color System

### Primary palette (digital)

| Name | Hex | RGB | Use |
|------|-----|-----|-----|
| Cloud Blue 68 | `#00B3FF` | R0 G179 B255 | Primary brand anchor — dominant color |
| Electric Blue 50 | `#066AFE` | R6 G106 B254 | High-contrast headlines, CTAs |
| Electric Blue 30 | `#022AC0` | R2 G42 B192 | Dark backgrounds, strong contrast |
| Electric Blue 15 | `#001E5B` | R0 G30 B91 | Darkest — near-black brand blue |
| Cloud Blue 80 | `#90D0FE` | R144 G208 B254 | Light accents, morning gradient |
| Cloud Blue 95 | `#EAF5FE` | R234 G245 B254 | Near-white backgrounds |
| White | `#FFFFFF` | R255 G255 B255 | Text on dark, clean backgrounds |

### Secondary palette (use sparingly — 20% maximum)

| Name | Hex | RGB |
|------|-----|-----|
| Teal 80 | `#04E1CB` | R4 G225 B203 |
| Yellow 80 | `#FCC003` | R252 G192 B3 |
| Pink 60 | `#FF538A` | R255 G83 B138 |
| Violet 65 | `#D17DFE` | R209 G125 B254 |

### 80/20 rule
80% of any slide uses the primary blue palette. 20% maximum uses secondary colors.
Secondary colors are for accents, data highlights, and single-word emphasis — never backgrounds or dominant elements.

### Gradient moods (named for reference)
- **Morning**: Cloud Blue 80 → Cloud Blue 95
- **Midday**: Cloud Blue 68 → Cloud Blue 80
- **Dusk**: Electric Blue 50 → Cloud Blue 68 → Cloud Blue 80 → Cloud Blue 95
- **Evening**: Electric Blue 15 → Electric Blue 30 → Electric Blue 50 → Cloud Blue 68

Use gradients for hero/title slides and high-impact moments. Solid colors for content slides.

### Accessibility
All color pairings must meet AA contrast standards.
Minimum contrast difference between foreground and background color scale values:
- Large text (above 18pt): 30 points
- Normal text (below 18pt): 50 points

Approved accessible primary pairings (text color / background):
- Electric Blue 50 / White
- Electric Blue 50 / Cloud Blue 95
- Electric Blue 15 / Cloud Blue 80
- White / Electric Blue 50
- White / Electric Blue 30
- White / Electric Blue 15

### Color don'ts
- Do NOT use unapproved colors or off-palette neutrals
- Do NOT use low-contrast pairings (e.g. Cloud Blue 68 text on white — borderline)
- Do NOT apply multiple colors within a single word
- Do NOT use secondary colors on body copy
- Do NOT mix secondary color type on secondary color backgrounds outside approved pairings
- Do NOT default to cream, beige, or warm-neutral backgrounds

---

## 3. Typography

### Typefaces

**Avant Garde for Salesforce** — Headlines and display copy only
- Weight: Demi exclusively
- Case: Sentence case (no ALL CAPS on primary headlines)
- Use for: H1, H2–H4 subheads, CTAs that need to stand out
- Tracking: -2% (-20pt) for H1; 0% for H2–H4
- Hero copy: 3–6 words maximum

**Salesforce Sans** — All body copy, supporting text, data labels
- Weight: Regular (Bold permitted sparingly with specific visual intent)
- Case: Sentence case
- Do NOT use Salesforce Sans Bold as headline copy

**Fallback for pptx (font substitution)**
Avant Garde for Salesforce → use **Arial** (closest safe substitute, Demi weight = Bold)
Salesforce Sans → use **Arial** Regular/Bold

When building pptx files: use Arial throughout. Apply tight tracking (-2% = approximately -0.3pt at 14pt) to headline text boxes to approximate Avant Garde's geometric character.

### Type scale

| Level | Font | Weight | Size | Line spacing | Notes |
|-------|------|--------|------|--------------|-------|
| H1 Headline | Avant Garde / Arial | Demi/Bold | As large as possible | 100% | Max 6 words |
| H2 Subhead | Avant Garde / Arial | Demi/Bold | ~50% of H1 | 100–110% | |
| H3–H4 | Avant Garde / Arial | Demi/Bold | ~25% of H1 | 100–110% | |
| Body (B1) | Salesforce Sans / Arial | Regular | ≥20% of H1, min 14pt | 150% | |
| Small body (B2) | Salesforce Sans / Arial | Regular | 75% of B1 | 150% | |
| CTA | Avant Garde / Arial | Demi/Bold | ~20% of H1 | 130% | |
| Caption (C1) | Salesforce Sans / Arial | Regular | 50–75% of B1 | 130% | |

### Typography rules
- H1 line spacing is 100% (NOT 110% — most tools default to 110%, must be manually corrected)
- Body line spacing is 150%
- No ALL CAPS for primary headlines or subtitles
- Do NOT bold body copy throughout (defeats hierarchy)
- Do NOT make body copy larger than headline copy
- Color in type: legibility first. Use secondary colors for emphasis only — maximum one highlighted section per sentence, never more than half the sentence
- Do NOT use more than two colors in a headline
- Do NOT apply visual type-breaking technique to body copy (headlines only)

### Visual type breaking
Place an icon within a headline to create energy. Rules:
- Icon must be semantically connected to the word it replaces or interrupts
- Horizontal margin: ¼ of the text's x-height on each side of the icon
- Vertical alignment: anchor to baseline above, cap height below
- Only use approved 3D product marketing icons or storytelling icons
- Get brand team approval before shipping type-breaking executions

---

## 4. Layout & Grid

### Grid system
1. Divide the slide into a grid that is a multiple of 2 columns
2. Set margins and gutters to 5% of the shortest slide dimension
   - For 16:9 (10" × 7.5"): margins = 0.375" ≈ 0.4"
   - For compact/dense layouts: gutters may compress to 2.5%
3. All content must snap to grid lines — no floating or eyeballed placement
4. Logo and headline must snap directly to one or more grid lines

### Hierarchy priority order (for every slide)
1. Illustration / hero visual
2. Headline
3. Body copy
4. URL or logo

### Focal point rule
Align the primary focal point (character's eye, product hero, key number) to a vertical grid line — NOT dead center.

### Framing rule
Photography, illustrations, and 3D icons may extend 1.2× beyond their container's edge for dynamism.

### Layout don'ts
- Do NOT place elements loosely between columns or "eyeball" the center of a gutter
- Do NOT push type or art to sit on the 5% margin line — it either locks inside or bleeds out
- Do NOT mix paragraph alignments within a slide
- Do NOT mix inconsistent gutters (e.g. 5% between some elements, arbitrary px between others)
- Do NOT center body text — left-align paragraphs; center only titles
- Do NOT use accent lines under titles
- Do NOT use decorative color bars or accent stripes along edges

---

## 5. Graphic Shapes

All shapes derive from the Salesforce Cloud logo geometry. Three core shapes:

### Panorama
- Most distinctive — adds depth and orbit around subject
- Reserved for HIGH-IMPACT moments (title slides, section dividers, hero moments)
- Use selectively — its power comes from scarcity
- Subtle curve preferred over dramatic curve (more flexible for cropping)
- Never: dramatic curves on both sides; multiple panoramas per layout; overly pinched shapes

### Rounded Rectangle
- Most common workhorse shape
- Creates containers for imagery and content
- Most effective with clear margins and full-bleed imagery
- Corner radii: 20px, 40px, or 60px (consistent within a deck)

### Circle
- Accent shape — use less frequently than the other two
- Best for: portraiture, UI elements, infographics, 360-degree product benefit representation
- Allow imagery to break the outer edge for depth

### Shape don'ts
- Do NOT use overly dramatic curves
- Do NOT apply multiple panoramas to a single layout
- Do NOT create new shapes or awkward geometry
- Do NOT use abrupt angles
- Do NOT make oval shapes
- Do NOT overlap shapes
- Do NOT scale shapes until unrecognizable
- Do NOT crop only one side of a panorama

---

## 6. Iconography

### Four icon types (never mix 3D with 2D in one asset)

**Product marketing icons (3D)**
- Use for: top-of-funnel — campaigns, presentations, events, social
- Full color 3D renders of product icons
- The fuzzy Agent Astro head (Agentforce) may be used more liberally than other 3D icons

**Storytelling icons (3D)**
- Intricate 3D visuals for conceptual ideas
- Maximum two storytelling icons per layout
- Same top-of-funnel use cases as product marketing icons

**Emoji icons**
- Decorative accent use — signal energy and focus
- Maximum two sparkle colors at a time

**2D icons (product UI contexts)**
- Use multicolor for lower-funnel marketing (emails, webinars, paid search)
- Use one-color for first appearance in UI; stroke for repeat appearances

### Icon application rules
- Icons are not decorative accents — they must serve the message
- Do NOT use random assortments of icons without narrative purpose
- Do NOT recolor icons
- Do NOT composite existing icons to create new ones
- Do NOT mix 3D and 2D icons in the same asset
- Do NOT use blur effect on static (non-animated) assets
- Do NOT use more than two storytelling icons per layout
- Do NOT overcrowd a layout with icons
- Need a new icon: contact #ask-brand, do not create your own

---

## 7. Data Visualization

### Type styling for data
- Headlines and numerals: Avant Garde / Arial (Bold)
- Supporting copy and fine data points: Salesforce Sans / Arial (Regular)
- Symbols (%, $): Superscript — let the numeral dominate
- Abbreviations (M, B, K): Same size as the numeral

### Approved chart types only
- Bar charts — compare categories, show rankings
- Line charts — show trends, acceleration, evolution over time
- Circle charts (pie, donut) — show composition / parts of a whole

No other chart types are approved.

### Color in charts
- Standard Salesforce infographics: primary blue palette only
- One bold secondary color permitted to highlight a single data point
- Product infographics: use that product's specific color palette
- Comparative infographics: Salesforce data = blue; partner data = their non-blue colors

### Visual treatments (choose by context)
- **Solid color**: dense reports, slide decks, documents — prioritizes legibility
- **Glass effect**: social, event displays, hero banners — high-impact channels

### Data callouts
Use large callout treatments to mic-drop a single stat. Effective for breaking up dense content.

### Attribution
All data must be attributed below the chart. Formula: Source, Year, methodology note if needed.

### Accessibility
Key data point must also be expressed in copy (not only in the visual).

---

## 8. Cloud Guidance (Critical — Read Carefully)

Salesforce is moving AWAY from cloud imagery. In all new corporate marketing and presentations:

**DO NOT:**
- Create cloud-themed names or event names (e.g., "Cloud for Platinum Club")
- Use cloud-based or cloud-shaped icons
- Use the Salesforce cloud logo as a decorative graphic shape (e.g., as a text container)
- Create any illustrations that reference or depict clouds

**The logo remains the logo.** It is the only permitted cloud reference. Everything else must move to the agentic enterprise visual language: gradients, geometric shapes, 3D icons, bold type.

---

## 9. Presentation-Specific Rules

### Slide structure
- Title/hero slides: gradient background (Dusk or Evening), white headline, Panorama shape optional
- Content slides: light background (Cloud Blue 95 or White), Electric Blue or Electric Blue 15 headline
- Section dividers: solid Electric Blue 30 or Electric Blue 15 background
- "Sandwich" structure: dark title → light content → dark close (or commit to dark throughout)

### Storytelling principles
Hierarchy → Contrast → White Space (in that order of priority)

### Logo placement
- Eight approved positions (any corner, any top/bottom center, or top/bottom center)
- Clear space: equal to the height and width of the cloud shape on all sides
- Minimum digital size: 40px (cloud logo) / 96px (horizontal logo)
- When below minimums: drop the wordmark, use cloud symbol only
- Do NOT use the logo as a decorative element or shape container

### Photography in slides
- Style: "1pm energy" — bright, authentic, natural midday lighting
- Feature real customers, employees, Trailblazers — not stock photography
- Four approved categories: Customer, Employee, Product/Industry, SMB
- Always include attribution (text-only or backed style)
- Photography on devices: must show Precise real UI (not conceptual UI)

### Brand voice for slide copy
Three principles (dial up or down by audience):
- **Tell it straight** — no buzzwords, no hype
- **Make it possible** — action-oriented, empowering
- **Disrupt the default** — challenge convention, be memorable

Jargon to AVOID: leverage, synergy, accelerate, disrupt, paradigm, revolutionary
Use instead: use, teamwork, fast, change, model, new

---

## 10. Quick Compliance Checklist

Before finalizing any slide deck, verify:

- [ ] 80/20 color rule observed (primary blues dominant)
- [ ] All color pairings meet AA accessibility contrast
- [ ] No ALL CAPS headlines
- [ ] Avant Garde / Arial Bold for headlines; Arial Regular for body
- [ ] H1 line spacing set to 100% (not 110%)
- [ ] All elements snap to grid lines
- [ ] Focal point aligned to vertical grid line (not dead center)
- [ ] 5% margins respected throughout
- [ ] No cloud imagery, cloud-shaped icons, or cloud-themed names
- [ ] Icons purposeful, not decorative; no 3D/2D mixing
- [ ] Approved chart types only (bar, line, circle)
- [ ] Data attributed below every chart
- [ ] Logo clear space maintained; minimum size respected
- [ ] No accent lines under titles
- [ ] No decorative color bars or edge stripes
- [ ] No secondary colors on body copy
- [ ] No low-contrast color pairings
