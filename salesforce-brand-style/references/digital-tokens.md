# Salesforce Digital Tokens — SLDS2 Reference

**Source:** `@salesforce-ux/design-system-2` v2 (Cosmos theme), extracted from `slds2.cosmos.css`
**Purpose:** Authoritative CSS custom property names for all web, HTML, SVG, and LWC outputs. Use these instead of raw hex values wherever CSS is the delivery format.

---

## How to read this file

SLDS2 has three layers of tokens. Use them in this order — do not skip to palette hooks when a semantic hook covers your need:

| Priority | Layer | Prefix | Use |
|----------|-------|--------|-----|
| **1 — First choice** | **Global (semantic)** | `--slds-g-color-surface-*`, `--slds-g-color-accent-*`, etc. | Role-based tokens — auto-adapt to dark mode; cover 85%+ of cases |
| **2 — Edge cases** | **Global (system)** | `--slds-g-color-brand-base-*`, `--slds-g-color-error-base-*` | Grade-level control within a color category |
| **3 — Rare / specific** | **Global (palette)** | `--slds-g-color-palette-*` | Named palette colors — only when semantic/system don't fit |
| **Never** | **Primitive** | `--slds-r-color-*` | Raw values — internal aliasing chain only, not for authored code |

**When to use palette tokens:** Only when you need a specific named Salesforce brand color that doesn't have a semantic equivalent — e.g., you need exactly Electric Blue 15 by name for brand documentation, a diagram legend, or a design token mapping table.

**For all interactive UI:** use semantic hooks. They flip automatically between light and dark via `light-dark()` and have pre-validated contrast pairings.

**Always include a fallback hex:** `var(--slds-g-color-surface-1, #ffffff)`

---

## 2. Accessibility — The 50-Point Rule

SLDS colors use a 0–100 lightness scale per color family. A **50-point separation** between foreground and background guarantees 4.5:1 WCAG AA contrast for body text; a **40-point separation** guarantees 3:1 for UI elements and borders. This works across hues, not just within the same color family.

**Examples:**
- Body text: Electric Blue 15 (`#001e5b`, ~15) on Cloud Blue 95 (`#eaf5fe`, ~95) → 80-point gap → AA compliant
- CTA button: Electric Blue 50 (`#066afe`, ~50) on White (`#ffffff`, 100) → 50-point gap → AA compliant
- Body text on Electric Blue 50 background: use White (100) → 50 points → AA compliant

Use this rule to verify any custom pairing without a color picker. When in doubt, pick token pairs that are at least 50 points apart.

---

## 3. Brand Color Palette — Token Mapping

### Electric Blue (Primary blues)

Maps to `brand-system.md` Electric Blue colors.

| Brand name | Hex | SLDS palette token | SLDS primitive |
|-----------|-----|-------------------|----------------|
| Electric Blue 15 | `#001e5b` | `--slds-g-color-palette-electric-blue-15` | `--slds-r-color-brand-15` |
| Electric Blue 30 | `#022ac0` | `--slds-g-color-palette-electric-blue-30` | `--slds-r-color-brand-30` |
| Electric Blue 50 | `#066afe` | `--slds-g-color-palette-electric-blue-50` | `--slds-r-color-brand-50` |
| Electric Blue 60 | `#4992fe` | `--slds-g-color-palette-electric-blue-60` | `--slds-r-color-brand-60` |
| Electric Blue 70 | `#7cb1fe` | `--slds-g-color-palette-electric-blue-70` | `--slds-r-color-brand-70` |
| Electric Blue 80 | `#a8cbff` | `--slds-g-color-palette-electric-blue-80` | `--slds-r-color-brand-80` |
| Electric Blue 90 | `#d6e6ff` | `--slds-g-color-palette-electric-blue-90` | `--slds-r-color-brand-90` |
| Electric Blue 95 | `#edf4ff` | `--slds-g-color-palette-electric-blue-95` | `--slds-r-color-brand-95` |

Note: `--slds-g-color-palette-electric-blue-50` is invariant (same in light and dark). All others are `light-dark()` adaptive.

### Cloud Blue (Light blues)

Maps to `brand-system.md` Cloud Blue colors.

| Brand name | Hex | SLDS palette token |
|-----------|-----|--------------------|
| Cloud Blue 68 | `#00b3ff` | No direct palette token — use hex fallback |
| Cloud Blue 80 | `#90d0fe` | `--slds-g-color-palette-cloud-blue-80` |
| Cloud Blue 95 | `#eaf5fe` | `--slds-g-color-palette-cloud-blue-95` |

Note: Cloud Blue 68 (`#00b3ff`) has no exact named palette token in SLDS2. Use `--slds-g-color-palette-cloud-blue-70` (`#1ab9ff` light) as the closest match, or hard-code `#00b3ff` with a comment.

### Teal (Secondary — ≤20% use)

| Brand name | Hex | SLDS palette token | SLDS primitive |
|-----------|-----|-------------------|----------------|
| Teal 80 | `#04e1cb` | `--slds-g-color-palette-teal-80` | `--slds-r-color-success-80` |

### Yellow (Secondary — ≤20% use)

| Brand name | Hex | SLDS palette token | SLDS primitive |
|-----------|-----|-------------------|----------------|
| Yellow 80 | `#fcc003` | `--slds-g-color-palette-yellow-80` | `--slds-r-color-warning-80` |

### Pink / Violet (Secondary — ≤20% use)

| Brand name | Hex | SLDS palette token |
|-----------|-----|--------------------|
| Pink 60 | `#ff538a` | `--slds-g-color-palette-pink-60` |
| Violet 65 | `#d17dfe` | `--slds-g-color-palette-violet-65` |

---

## 4. Semantic Color Tokens

Use these for interactive components and anything that needs dark mode / theming support. These flip automatically between light and dark mode via `light-dark()`.

### Surface tokens (backgrounds)

| Token | Light value | Dark value | Use |
|-------|------------|------------|-----|
| `--slds-g-color-surface-1` | `#ffffff` | `#242424` | Primary content background |
| `--slds-g-color-surface-2` | `#f3f3f3` | `#181818` | Alternate/secondary background |
| `--slds-g-color-surface-container-1` | `#ffffff` | `#242424` | Card, modal, panel background |
| `--slds-g-color-surface-container-2` | `#f3f3f3` | `#181818` | Nested container background |
| `--slds-g-color-surface-container-3` | `#e5e5e5` | `#2e2e2e` | Pressed/selected container |
| `--slds-g-color-surface-inverse-1` | `#032d60` | `#aacbff` | Dark background (inverse) |
| `--slds-g-color-surface-container-inverse-1` | `#032d60` | `#aacbff` | Dark container (inverse) |

### Text / foreground tokens

| Token | Light value | Dark value | Use |
|-------|------------|------------|-----|
| `--slds-g-color-on-surface-1` | `#5c5c5c` | `#aeaeae` | Secondary/tertiary body text |
| `--slds-g-color-on-surface-2` | `#2e2e2e` | `#e5e5e5` | Primary body text |
| `--slds-g-color-on-surface-3` | `#03234d` | `#d8e6fe` | High-emphasis text (brand-tinted dark) |
| `--slds-g-color-on-surface-inverse-1` | `#ffffff` | `#181818` | Text on dark/inverse backgrounds |
| `--slds-g-color-on-surface-inverse-2` | `#a8cbff` | `#002775` | Accent text on dark backgrounds |

### Accent tokens (brand interactive)

| Token | Use |
|-------|-----|
| `--slds-g-color-accent-1` | Primary CTA background (Electric Blue 50) |
| `--slds-g-color-accent-2` | Hover state for primary CTA |
| `--slds-g-color-accent-3` | Active/pressed state for primary CTA |
| `--slds-g-color-accent-container-1` | Accent-tinted container background |
| `--slds-g-color-brand-base-10` | Brand blue — darkest (EB15 equivalent) |
| `--slds-g-color-brand-base-30` | Brand blue — dark (EB30 equivalent) |
| `--slds-g-color-brand-base-50` | Brand blue — mid (EB50 / accent) |
| `--slds-g-color-brand-base-80` | Brand blue — light (CB80 equivalent) |
| `--slds-g-color-brand-base-95` | Brand blue — near-white (CB95 equivalent) |

### Border tokens

| Token | Light value | Use |
|-------|------------|-----|
| `--slds-g-color-border-1` | `#c9c9c9` | Standard border |
| `--slds-g-color-border-2` | `#5c5c5c` | Emphasized border |
| `--slds-g-color-border-accent-1` | Electric Blue 50 | Focused/active border |

### Feedback tokens (status colors)

| Token | Light hex | Use |
|-------|-----------|-----|
| `--slds-g-color-error-1` | from `--slds-r-color-error-40` | Error text |
| `--slds-g-color-error-container-1` | from `--slds-r-color-error-90` | Error background |
| `--slds-g-color-success-base-40` | from `--slds-r-color-success-40` | Success text |
| `--slds-g-color-info-1` | from `--slds-r-color-info-40` | Info text |

---

## 5. Typography Tokens

### Font family

| Token | Value | Use |
|-------|-------|-----|
| `--slds-g-font-family-base` | `system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, 'Helvetica Neue', Arial, sans-serif` | All body and UI text |
| `--slds-g-font-family-monospace` | `Consolas, Menlo, Monaco, Courier, monospace` | Code, data |

**Note for Salesforce-branded outputs:** The SLDS base font stack resolves to system fonts. For client-facing deliverables (not product UI), use Arial directly to align with `brand-system.md` pptx guidance. For product UI (LWC, PWA), use `--slds-g-font-family-base`.

### Font scale (size)

| Token | Value | Approx px (16px base) | Equivalent role |
|-------|-------|------------------------|----------------|
| `--slds-g-font-scale-neg-2` | `0.625rem` | 10px | Caption |
| `--slds-g-font-scale-neg-1` | `0.75rem` | 12px | Small caption |
| `--slds-g-font-scale-base` | `0.8125rem` | 13px | Base UI text |
| `--slds-g-font-scale-1` | `0.875rem` | 14px | Body (B2) |
| `--slds-g-font-scale-2` | `1rem` | 16px | Body (B1) |
| `--slds-g-font-scale-3` | `1.25rem` | 20px | H4 / subhead |
| `--slds-g-font-scale-4` | `1.5rem` | 24px | H3 |
| `--slds-g-font-scale-5` | `1.75rem` | 28px | H2 |
| `--slds-g-font-scale-6` | `2rem` | 32px | H2 large |
| `--slds-g-font-scale-7` | `2.5rem` | 40px | H1 |
| `--slds-g-font-scale-8` | `3rem` | 48px | H1 display |

**Critical naming trap:** Use `--slds-g-font-scale-*` NOT `--slds-g-font-size-N`. Only `--slds-g-font-size-base` exists; numbered font-size tokens do not.

### Font weight

| Token | Value | Use |
|-------|-------|-----|
| `--slds-g-font-weight-4` | `400` | Regular body |
| `--slds-g-font-weight-6` | `600` | Semibold UI labels |
| `--slds-g-font-weight-7` | `700` | Bold headlines |
| `--slds-g-font-weight-bold` | `bold` | Bold (semantic) |

### Line height

| Token | Value | Use |
|-------|-------|-----|
| `--slds-g-font-line-height-1` | `1` | Tight (headlines) |
| `--slds-g-font-line-height-2` | `1.25` | Compact UI |
| `--slds-g-font-line-height-3` | `1.375` | Dense body |
| `--slds-g-font-line-height-4` | `1.5` | Standard body |
| `--slds-g-font-line-height-base` | `1.5` | Default |
| `--slds-g-font-line-height-5` | `1.75` | Relaxed reading |

---

## 6. Spacing Tokens

Spacing scale based on 4px base unit.

| Token | Value | px equiv | Use |
|-------|-------|----------|-----|
| `--slds-g-spacing-1` | `0.25rem` | 4px | Micro gap |
| `--slds-g-spacing-2` | `0.5rem` | 8px | Tight spacing |
| `--slds-g-spacing-3` | `0.75rem` | 12px | Compact padding |
| `--slds-g-spacing-4` | `1rem` | 16px | Standard padding |
| `--slds-g-spacing-5` | `1.5rem` | 24px | Section padding |
| `--slds-g-spacing-6` | `2rem` | 32px | Large section gap |
| `--slds-g-spacing-7` | `2.5rem` | 40px | Component separation |
| `--slds-g-spacing-8` | `3rem` | 48px | Section break |
| `--slds-g-spacing-9` | `3.5rem` | 56px | Large section break |
| `--slds-g-spacing-10` | `4rem` | 64px | Page-level spacing |

---

## 7. Border Radius Tokens

| Token | Value | Use |
|-------|-------|-----|
| `--slds-g-radius-border-1` | `0.25rem` (4px) | Tight — inputs, tags |
| `--slds-g-radius-border-2` | `0.5rem` (8px) | Standard — cards, panels |
| `--slds-g-radius-border-3` | `0.75rem` (12px) | Relaxed — modals |
| `--slds-g-radius-border-4` | `1.25rem` (20px) | Soft — badges, chips |
| `--slds-g-radius-border-pill` | `15rem` | Full pill shape |
| `--slds-g-radius-border-circle` | `100%` | Circle avatars, dots |

---

## 8. Elevation / Shadow Tokens

| Token | Use |
|-------|-----|
| `--slds-g-shadow-1` | Flat cards, subtle lift |
| `--slds-g-shadow-2` | Raised panels, dropdowns |
| `--slds-g-shadow-3` | Modals, floating elements |
| `--slds-g-shadow-4` | Toast, high-priority overlays |

---

## 9. Sizing Tokens (component dimensions)

| Token | Value | Typical use |
|-------|-------|-------------|
| `--slds-g-sizing-1` | `0.125rem` | 2px hairline |
| `--slds-g-sizing-2` | `0.25rem` | 4px micro |
| `--slds-g-sizing-3` | `0.5rem` | 8px |
| `--slds-g-sizing-4` | `0.75rem` | 12px |
| `--slds-g-sizing-5` | `1rem` | 16px — icon SM |
| `--slds-g-sizing-6` | `1.25rem` | 20px |
| `--slds-g-sizing-10` | `3rem` | 48px — icon LG, avatar |
| `--slds-g-sizing-11` | `4rem` | 64px |
| `--slds-g-sizing-12` | `5rem` | 80px |

---

## 10. Border Width Tokens

| Token | Value | Use |
|-------|-------|-----|
| `--slds-g-border-width-1` | `1px` | Standard border |

---

## 11. Output-Type Decision Guide

| Deliverable | Token strategy |
|-------------|---------------|
| **Mermaid / SVG diagram** | Use hex values from brand-system.md; token CSS vars are not renderable in static SVG |
| **HTML artifact / claude.ai** | Use `--slds-g-color-palette-*` tokens; include fallback hex; link or inline `slds2.cosmos.css` if needed |
| **PWA / web app** | Use full semantic token stack (`--slds-g-color-surface-*`, etc.); import `slds2.cosmos.css` from npm |
| **LWC component** | Use full SLDS stack: LBC first, then blueprints, then `--slds-g-*` hooks; run SLDS linter |
| **React/HTML in starter kit** | Use `--slds-g-*` hooks; do NOT hard-code hex; run `npx @salesforce-ux/slds-linter@latest lint` |
| **PowerPoint (pptx)** | Use hex values only — CSS vars are not supported; see salesforce-presentation skill |

---

## 12. Quick-Copy Patterns

### Branded card (HTML)
```css
.sf-card {
  background: var(--slds-g-color-surface-container-1, #ffffff);
  color: var(--slds-g-color-on-surface-2, #2e2e2e);
  border-radius: var(--slds-g-radius-border-2, 0.5rem);
  box-shadow: var(--slds-g-shadow-1);
  padding: var(--slds-g-spacing-5, 1.5rem);
}
```

### Dark hero section (brand-compliant)
```css
.sf-hero {
  background: var(--slds-g-color-palette-electric-blue-15, #001e5b);
  color: var(--slds-g-color-on-surface-inverse-1, #ffffff);
  padding: var(--slds-g-spacing-10, 4rem) var(--slds-g-spacing-6, 2rem);
}
```

### Stat callout (data visualization)
```css
.sf-stat-number {
  font-size: var(--slds-g-font-scale-8, 3rem);
  font-weight: var(--slds-g-font-weight-7, 700);
  color: var(--slds-g-color-palette-electric-blue-15, #001e5b);
  line-height: var(--slds-g-font-line-height-1, 1);
}
.sf-stat-label {
  font-size: var(--slds-g-font-scale-1, 0.875rem);
  color: var(--slds-g-color-on-surface-1, #5c5c5c);
  line-height: var(--slds-g-font-line-height-4, 1.5);
}
```

### Accent button (primary CTA)
```css
.sf-btn-primary {
  background: var(--slds-g-color-accent-1, #066afe);
  color: var(--slds-g-color-on-surface-inverse-1, #ffffff);
  border-radius: var(--slds-g-radius-border-1, 0.25rem);
  padding: var(--slds-g-spacing-2, 0.5rem) var(--slds-g-spacing-4, 1rem);
  font-weight: var(--slds-g-font-weight-7, 700);
  font-size: var(--slds-g-font-scale-2, 1rem);
}
```

---

## 13. SLDS Linter (development contexts only)

When producing HTML, CSS, or LWC files that will be linted:

```bash
npx @salesforce-ux/slds-linter@latest lint <file-path>
```

Violations to fix before delivery:
- Hard-coded hex colors → replace with `var(--slds-g-*)` token
- Deprecated `--lwc-*` tokens → replace with `--slds-g-*` equivalents
- Direct `.slds-*` class overrides → use custom `my-*` or `c-*` prefix classes instead
- Missing fallback values on `var()` calls → add hex fallback as second argument

The linter applies only to LWC, HTML, and CSS files — not to SVG, pptx, or Mermaid outputs.

