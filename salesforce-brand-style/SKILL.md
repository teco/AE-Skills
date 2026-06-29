---
name: salesforce-brand-style
description: Apply Salesforce brand guidelines to any client-facing visual output that is NOT a PowerPoint — including diagrams, flowcharts, architecture visuals, Mermaid charts, SVG illustrations, HTML prototypes, interactive artifacts, PWAs, web components, and LWC development work. Use this skill whenever producing any Salesforce-branded visual content outside of slide decks. Trigger on: "make a diagram", "create a chart", "draw a flow", "build a prototype", "create an artifact", "make this look Salesforce", "Salesforce-branded HTML", "Salesforce colors", "SLDS", "Lightning Design System", or any request to produce a visual deliverable in a Salesforce context. For PowerPoint/pptx outputs, use the salesforce-presentation skill instead — this skill handles everything else.
---

# Salesforce Brand Style Skill

Enforces Salesforce Brand Central guidelines across all non-pptx visual outputs: diagrams, charts, SVG, HTML artifacts, interactive prototypes, PWAs, and LWC components.

This skill routes by output type. Read Step 0 first, then jump directly to the section for your deliverable.

---

## Step 0 — Read brand rules before anything else

**Before any design or code decision, read:**

```
references/brand-system.md
```

This is the authoritative Salesforce Brand Central ruleset — colors, typography, shapes, iconography, data visualization rules, and cloud imagery restrictions. Do not rely on memory. Read it every time.

The output-type router below tells you what additional references to load. Do not load all references upfront — load only what your deliverable requires.

---

## Output-Type Router

Identify the deliverable, then jump to that section.

| Deliverable | Section |
|-------------|---------|
| Mermaid diagram, flowchart, architecture diagram | → Section A |
| SVG illustration, infographic | → Section B |
| HTML artifact, interactive prototype (claude.ai) | → Section C |
| PWA, web app, standalone HTML/CSS project | → Section D |
| LWC component, SLDS-backed development | → Section E |
| Data chart (bar, line, pie for non-pptx) | → Section F |
| Ambiguous / mixed output | → Read brand-system.md, then pick the closest section |

For PowerPoint: use `salesforce-presentation` skill, not this one.

---

## Section A — Mermaid Diagrams and Flowcharts

**Token strategy:** Hex values only. Mermaid does not consume CSS custom properties.

### Color defaults

Use these hex values directly in Mermaid `classDef` and `style` blocks:

| Role | Color name | Hex |
|------|-----------|-----|
| Primary node fill (dark) | Electric Blue 15 | `#001E5B` |
| Primary node fill (mid) | Electric Blue 30 | `#022AC0` |
| Primary node fill (accent) | Electric Blue 50 | `#066AFE` |
| Light node fill | Cloud Blue 95 | `#EAF5FE` |
| Node stroke / border | Electric Blue 30 | `#022AC0` |
| Text on dark nodes | White | `#FFFFFF` |
| Text on light nodes | Electric Blue 15 | `#001E5B` |
| Secondary accent node | Teal 80 | `#04E1CB` |
| Warning / highlight node | Yellow 80 | `#FCC003` |
| Diagram background | White | `#FFFFFF` |
| Edge / arrow color | Electric Blue 30 | `#022AC0` |

### Typography

Mermaid uses the renderer's default font. Specify `Arial` in `%%{init}` config where supported:

```
%%{init: {'theme': 'base', 'themeVariables': {'fontFamily': 'Arial', 'fontSize': '14px', 'primaryColor': '#EAF5FE', 'primaryTextColor': '#001E5B', 'primaryBorderColor': '#022AC0', 'lineColor': '#022AC0', 'secondaryColor': '#FFFFFF', 'tertiaryColor': '#EAF5FE'}}}%%
```

### Brand compliance checks

Before delivering:
- [ ] 80/20 rule: primary blues dominant, secondary colors (Teal, Yellow) ≤20% of nodes
- [ ] No cloud-shaped nodes or cloud-named labels
- [ ] All text meets AA contrast against its node fill (50-point separation on 0–100 scale)
- [ ] Sentence case on all node labels — no ALL CAPS

---

## Section B — SVG Illustrations and Infographics

**Token strategy:** Hex values only. SVG `fill` and `stroke` attributes take hex; CSS vars are only usable inside an embedded `<style>` block.

### Shape language

Follow brand-system.md Section 5 for shapes. Three permitted shapes: Panorama (high-impact only), Rounded Rectangle (workhorse), Circle (accent use). Do not create arbitrary polygons or abrupt angles.

### Color application

Use hex values from brand-system.md Section 2. Key rule: 80% of the SVG visual weight uses primary blues; secondary palette ≤20%.

Apply gradient fills using the named gradient moods from brand-system.md:
- **Evening** (dark hero): `#001E5B → #022AC0 → #066AFE → #00B3FF`
- **Morning** (light background): `#90D0FE → #EAF5FE`

### Infographic-specific rules

- Data numerals: Arial Bold, largest element on the slide; symbol (%, $) in superscript
- Attribution line below every chart: Arial Regular, 9–11pt equivalent, `#022AC0` or muted
- Approved chart shapes only: bar, line, circle — see brand-system.md Section 7

### Brand compliance checks

Before delivering:
- [ ] No cloud imagery or cloud-shaped elements (logo excepted)
- [ ] Shape vocabulary follows brand-system.md Section 5
- [ ] All color pairs meet AA contrast
- [ ] 80/20 primary/secondary color distribution
- [ ] Data attributed if present

---

## Section C — HTML Artifacts and Interactive Prototypes

**Context:** claude.ai artifacts, standalone HTML deliverables, interactive explainers. No Salesforce platform required. SLDS2 tokens available via CSS custom properties.

**Token strategy:** `var(--slds-g-*)` with hex fallbacks. Load `digital-tokens.md` for the full reference.

```
references/digital-tokens.md
```

### Hook selection hierarchy (in order)

1. **Semantic hooks** — `--slds-g-color-surface-*`, `--slds-g-color-on-surface-*`, `--slds-g-color-accent-*` — use for 85%+ of color decisions; auto-adapts to dark mode
2. **System hooks** — `--slds-g-color-brand-base-*` — use when you need a specific position on the brand blue scale
3. **Palette hooks** — `--slds-g-color-palette-electric-blue-*`, `--slds-g-color-palette-cloud-blue-*`, etc. — use only when targeting a specific named brand color

Always include a hex fallback: `var(--slds-g-color-surface-1, #ffffff)`

### CSS baseline for artifacts

```css
/* Import or inline at the top of every Salesforce-branded HTML artifact */
:root {
  /* Brand foundations — use these as aliases in your component CSS */
  --sf-bg-dark:       var(--slds-g-color-palette-electric-blue-15, #001e5b);
  --sf-bg-mid:        var(--slds-g-color-palette-electric-blue-30, #022ac0);
  --sf-bg-light:      var(--slds-g-color-palette-cloud-blue-95, #eaf5fe);
  --sf-text-on-dark:  var(--slds-g-color-on-surface-inverse-1, #ffffff);
  --sf-text-on-light: var(--slds-g-color-on-surface-3, #001e5b);
  --sf-text-body:     var(--slds-g-color-on-surface-2, #2e2e2e);
  --sf-accent:        var(--slds-g-color-accent-1, #066afe);
  --sf-teal:          var(--slds-g-color-palette-teal-80, #04e1cb);
  --sf-yellow:        var(--slds-g-color-palette-yellow-80, #fcc003);

  /* Typography */
  font-family: var(--slds-g-font-family-base, Arial, sans-serif);
  font-size: var(--slds-g-font-scale-2, 1rem);
  line-height: var(--slds-g-font-line-height-4, 1.5);
}
```

### Layout defaults

- Outer padding: `var(--slds-g-spacing-5, 1.5rem)` minimum
- Card border-radius: `var(--slds-g-radius-border-2, 0.5rem)`
- Card shadow: `var(--slds-g-shadow-1)`
- Grid gutters: `var(--slds-g-spacing-4, 1rem)`

### Color distribution rule

Match the SLDS 85-5-10 distribution:
- 85% foundation: surfaces, backgrounds, neutral containers (`--slds-g-color-surface-*`)
- 5% accent: CTAs, active states, key emphasis (`--slds-g-color-accent-*`)
- 10% expressive: data viz, brand moments — Teal, Yellow, Pink, Violet from palette hooks

### Typography in HTML

| Role | Hook | Fallback | Notes |
|------|------|----------|-------|
| H1 | `--slds-g-font-scale-7` | `2.5rem` | `font-weight: 700`, `line-height: 1` |
| H2 | `--slds-g-font-scale-5` | `1.75rem` | `font-weight: 700` |
| H3 | `--slds-g-font-scale-4` | `1.5rem` | `font-weight: 600` |
| Body | `--slds-g-font-scale-2` | `1rem` | `font-weight: 400`, `line-height: 1.5` |
| Caption | `--slds-g-font-scale-neg-1` | `0.75rem` | `font-weight: 400` |
| Data numeral | `--slds-g-font-scale-8` | `3rem` | `font-weight: 700`, `line-height: 1` |

**Critical naming trap:** Use `--slds-g-font-scale-*` not `--slds-g-font-size-N`. Only `--slds-g-font-size-base` exists; numbered font-size tokens do not.

### Brand compliance checks

Before delivering:
- [ ] No cloud imagery or cloud-shaped elements
- [ ] No hard-coded hex values — all colors via `var(--slds-g-*)` with fallbacks
- [ ] 85-5-10 color distribution maintained
- [ ] All color pairs meet AA contrast (50-point separation rule)
- [ ] Sentence case throughout — no ALL CAPS
- [ ] Font scale uses `--slds-g-font-scale-*`, not invented `--slds-g-font-size-N` tokens
- [ ] Custom classes use `my-*` or `sf-*` prefix — never override `slds-*` classes

---

## Section D — PWAs, Web Apps, Standalone HTML/CSS Projects

**Context:** Multi-file web projects that run outside Salesforce platform — like the PWA agenda. Requires a Node/npm environment. SLDS2 is available as an npm package.

**Token strategy:** Full `--slds-g-*` semantic hook stack. Load and use `slds2.cosmos.css` from npm.

### Setup

```bash
npm install @salesforce-ux/design-system-2
```

Import in your entry CSS or HTML:
```html
<link rel="stylesheet" href="node_modules/@salesforce-ux/design-system-2/dist/css/bundled/slds2.cosmos.css">
```

Or in JS/module bundlers:
```js
import '@salesforce-ux/design-system-2/dist/css/bundled/slds2.cosmos.css';
```

Once loaded, all `--slds-g-*` hooks are available globally. Dark mode is handled automatically via `light-dark()` in the token definitions.

### Architecture guidance

Follow the starter kit's component namespace pattern:
- `page-*` — route-level views
- `ui-*` — reusable components
- `shell-*` — app shell only

For complex routing and multi-page PWAs, reference the starter kit structure:
```
https://github.com/salesforce-ux/design-system-2-starter-kit
```

### Coding rules

- Use `--slds-g-*` hooks for all color, spacing, typography, border-radius, and shadow values
- Never hard-code hex, px spacing, or font sizes
- Custom classes: `my-*` or `sf-*` prefix — never override `slds-*`
- Spacing via `--slds-g-spacing-*` tokens or SLDS utility classes (`slds-p-*`, `slds-m-*`)
- Grid via SLDS utilities: `slds-grid`, `slds-col`, `slds-size_*`

### Validation (run before delivery)

```bash
npx @salesforce-ux/slds-linter@latest lint <file-or-directory>
```

Linter catches: hard-coded colors, deprecated `--lwc-*` tokens, `.slds-*` class overrides.

### Brand compliance checks

Before delivering:
- [ ] `slds2.cosmos.css` imported and active
- [ ] All color via `--slds-g-*` hooks with fallbacks — no raw hex
- [ ] Linter passes with zero violations
- [ ] 85-5-10 color distribution maintained
- [ ] No cloud imagery
- [ ] Sentence case throughout

---

## Section E — LWC Components and SLDS Development

**Context:** Building or editing Lightning Web Components, Salesforce platform UI, or anything that runs inside a Salesforce org.

**Load the full SLDS sub-skill before writing any code:**

```
references/applying-slds/GUIDE.md
```

That skill contains the complete authoring workflow: component selection hierarchy (LBC → Blueprint → Hooks → Custom), search scripts for the 523 hooks / 85 blueprints / 1,732 icons, validation checklists, and worked examples. Do not duplicate its guidance here — read it and follow it.

### Key rules summary (do not rely on these alone — read the sub-skill)

- **LBC first:** if a `lightning-*` component exists, use it instead of hand-rolling SLDS markup
- **Blueprint second:** search `references/applying-slds/scripts/search-blueprints.cjs` before building custom
- **Hooks third:** `var(--slds-g-*, fallback)` for all themeable values; never hard-code
- **Verify before emit:** run search scripts — never guess hook or utility class names
- **Linter mandatory:** `npx @salesforce-ux/slds-linter@latest lint <path>` — zero violations target

### Brand overlay on SLDS defaults

SLDS2 Cosmos theme IS the Salesforce brand for UI contexts. No manual brand color overrides are needed — the semantic hooks resolve to the correct brand blues automatically. Only apply palette hooks (`--slds-g-color-palette-electric-blue-*`) when you explicitly need a specific brand color that semantic hooks don't cover.

### Starter kit (for local dev / prototyping)

```
https://github.com/salesforce-ux/design-system-2-starter-kit
```

Clone for a ready-to-use LWC + Vite environment. The `afv-library` skills sync automatically on `npm install` and include the `applying-slds` skill at `.agent/skills/afv-library/applying-slds/`.

---

## Section F — Data Charts and Visualization (non-pptx)

**Context:** Charts produced as SVG, HTML canvas, or via a charting library (Recharts, D3, Chart.js, Plotly) for use in artifacts, reports, or web deliverables.

### Approved chart types

Bar, line, and circle (pie/donut) only — brand-system.md Section 7. No other types.

### Color sequencing for chart series

Use primary blues in this priority order for multi-series charts:

| Series order | Color | Hex |
|-------------|-------|-----|
| 1 (primary) | Cloud Blue 68 | `#00B3FF` |
| 2 | Electric Blue 50 | `#066AFE` |
| 3 | Electric Blue 30 | `#022AC0` |
| 4 | Electric Blue 15 | `#001E5B` |
| Highlight (one series only) | Yellow 80 or Teal 80 | `#FCC003` / `#04E1CB` |

Never use secondary colors for more than one highlighted series. For HTML contexts, use the SLDS system hooks: `--slds-g-color-brand-base-60`, `-50`, `-30`, `-15`.

### Data callout treatment

Mic-drop a single stat: large numeral (60–72pt equivalent), symbol superscript, label below in body size.

### Attribution rule

Every chart must have a source line: `Source: [Name], [Year]` in caption size, below the chart. No exceptions.

### Accessibility

Key data point expressed in body copy, not only in the visual.

### Brand compliance checks

Before delivering:
- [ ] Approved chart type (bar, line, circle only)
- [ ] Primary blue series, one secondary accent maximum
- [ ] Attribution line present
- [ ] Key data point stated in copy
- [ ] 80/20 color distribution across the full deliverable

---

## Universal Brand Constraints

These apply to every output type regardless of section:

1. **No cloud imagery** — no cloud shapes, cloud-named elements, or cloud illustrations anywhere except the logo
2. **No off-palette colors** — only colors from brand-system.md Section 2; no arbitrary hex values
3. **80/20 (presentation) / 85-5-10 (UI) rule** — primary blues dominate; secondary palette is accent only
4. **AA contrast on all pairings** — 50-point separation on the 0–100 scale guarantees compliance
5. **Sentence case** — headlines and labels always sentence case, never ALL CAPS
6. **No decorative edge stripes, accent bars, or title underlines**
7. **Approved chart types only** — bar, line, circle; no radar, scatter, bubble, heatmap, etc.
8. **Data always attributed** — source line on every chart

---

## Reference Files

| File | Load when |
|------|-----------|
| `references/brand-system.md` | Every build — colors, type, shapes, icons, data viz, cloud guidance |
| `references/digital-tokens.md` | HTML / CSS / PWA outputs — full SLDS2 token reference with hex mappings |
| `references/applying-slds/GUIDE.md` | LWC / SLDS development — component selection, hooks, blueprints, validation |
| `references/applying-slds/references/styling-decision-guide.md` | Detailed hook selection, 85-5-10 rule, spacing and typography decisions |
| `references/applying-slds/references/component-selection.md` | LBC vs blueprint decision flow |
| `references/applying-slds/checklists.md` | Pre-delivery validation checklist for SLDS outputs (T/Q/C/A checks) |
| `references/slide-patterns.md` | Layout reference when an HTML artifact mirrors a presentation structure |

