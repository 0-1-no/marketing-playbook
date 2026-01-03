---
name: color-theory
description: Fargepaletter, semantikk og kontrast. Bruk ved fargevalg.
---

# Color Theory

> **Metodikk-fil:** Dette er prinsipper og strategier for fargevalg.
> Faktiske hex-verdier dokumenteres i `./marketing/DESIGN-SYSTEM.md`.
> Hex-kodene under er EKSEMPLER - bruk verdier fra prosjektets design system.

---

## Palett-struktur

### Minimum Viable Palette

```
┌─────────────────────────────────────────────────────────────┐
│ PRIMÆR       │ Hovedfarge, CTA, brand-identitet            │
│ BAKGRUNN     │ Side-bakgrunn                               │
│ OVERFLATE    │ Kort, modaler, sections                     │
│ TEKST        │ Primær tekst                                │
│ MUTED        │ Sekundær tekst, borders                     │
│ AKSENT       │ Highlights, ikoner, lenker                  │
└─────────────────────────────────────────────────────────────┘
```

### Utvidet Palette

```
┌─────────────────────────────────────────────────────────────┐
│ SEMANTIC COLORS                                             │
│ SUCCESS      │ Grønn - positive actions, confirmations      │
│ WARNING      │ Gul/oransje - caution, attention             │
│ ERROR        │ Rød - errors, destructive actions            │
│ INFO         │ Blå - informational messages                 │
└─────────────────────────────────────────────────────────────┘
```

---

## AI Slop Farger (Unngå)

### The AI Gradient

```css
/* UNNGÅ - brukt av 90% av AI-sider */
background: linear-gradient(135deg, #7C3AED, #3B82F6);
```

### Safe But Boring

| Farge | Problem |
|-------|---------|
| #3B82F6 (Tailwind blue-500) | Default |
| #7C3AED (Tailwind violet-500) | AI-gradient |
| #10B981 (Tailwind emerald-500) | Generic success |
| Hvit bakgrunn + blå CTA | Overalt |

### Hvordan Unngå

1. **Velg én distinkt primærfarge** som eies
2. **Bruk uventede aksenter**
3. **Vurder mørk bakgrunn**
4. **Eksperimenter med tone** (varm vs kald)

---

## Fargevalg Strategier

### Strategi 1: Monokrom + Aksent

```
Bakgrunn:  #0A0A0A (nesten svart)
Overflate: #171717
Tekst:     #FAFAFA
Muted:     #A3A3A3
Aksent:    #FF6B35 (oransje)
```

**Passer for:** Tech, minimal, sofistikert

### Strategi 2: Warm & Natural

```
Bakgrunn:  #FBF9F4 (varm hvit)
Overflate: #FFFFFF
Tekst:     #1C1917
Muted:     #78716C
Primær:    #7C5E3C (brun/gull)
Aksent:    #2D5A27 (skoggrønn)
```

**Passer for:** Organic, lifestyle, mat

### Strategi 3: Bold & Playful

```
Bakgrunn:  #FFFBEB (varm gul)
Overflate: #FFFFFF
Tekst:     #1F2937
Primær:    #F97316 (oransje)
Aksent:    #7C3AED (lilla)
Sekundær:  #06B6D4 (cyan)
```

**Passer for:** B2C, kreativ, ung

### Strategi 4: Dark & Premium

```
Bakgrunn:  #000000
Overflate: #0A0A0A
Tekst:     #FFFFFF
Muted:     #666666
Primær:    #FFD700 (gull)
Aksent:    #C0C0C0 (sølv)
```

**Passer for:** Luxury, finans, gaming

---

## Kontrast-regler (WCAG)

### Minimum Requirements

| Element | Kontrast-ratio |
|---------|---------------|
| Normal tekst | 4.5:1 |
| Stor tekst (18px+, eller 14px bold) | 3:1 |
| UI komponenter | 3:1 |
| Dekorative elementer | Ingen krav |

### Test Kontrast

```
Verktøy:
- WebAIM Contrast Checker
- Stark (Figma plugin)
- axe DevTools
```

### Vanlige Feil

| Problem | Løsning |
|---------|---------|
| Lys grå tekst på hvit | Mørk opp til minst #767676 |
| Lys knapp på lys bakgrunn | Legg til border eller mørkere farge |
| Placeholder tekst for lys | Bruk mørkere placeholder |

---

## CSS Variables

### Light Mode

```css
:root {
  /* Core */
  --color-background: #FFFFFF;
  --color-surface: #F9FAFB;
  --color-primary: #2563EB;
  --color-primary-hover: #1D4ED8;

  /* Text */
  --color-text: #111827;
  --color-text-muted: #6B7280;
  --color-text-inverted: #FFFFFF;

  /* Border */
  --color-border: #E5E7EB;
  --color-border-focus: #2563EB;

  /* Semantic */
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
  --color-info: #3B82F6;
}
```

### Dark Mode

```css
.dark {
  --color-background: #0A0A0A;
  --color-surface: #171717;
  --color-primary: #3B82F6;
  --color-primary-hover: #60A5FA;

  --color-text: #FAFAFA;
  --color-text-muted: #A3A3A3;
  --color-text-inverted: #0A0A0A;

  --color-border: #262626;
  --color-border-focus: #3B82F6;

  /* Semantic - justert for mørk bakgrunn */
  --color-success: #34D399;
  --color-warning: #FBBF24;
  --color-error: #F87171;
  --color-info: #60A5FA;
}
```

---

## Tailwind Config

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#FFF7ED',
          100: '#FFEDD5',
          // ... generert fra primærfarge
          500: '#F97316',
          600: '#EA580C',
          900: '#7C2D12',
        },
        surface: {
          DEFAULT: 'var(--color-surface)',
        },
      },
    },
  },
};
```

---

## Fargepsykologi

| Farge | Assosiasjon | Bruk for |
|-------|-------------|----------|
| **Blå** | Tillit, profesjonell, rolig | Finans, helse, tech |
| **Grønn** | Vekst, natur, suksess | Bærekraft, finans, helse |
| **Rød** | Energi, handling, advarsel | Mat, underholdning, CTAs |
| **Oransje** | Vennlig, entusiastisk, kreativ | E-commerce, sport, mat |
| **Lilla** | Premium, kreativ, mystisk | Luksus, skjønnhet, tech |
| **Gul** | Optimisme, varme, oppmerksomhet | Barn, mat, underholdning |
| **Svart** | Eleganse, kraft, luksus | Premium, mote, tech |
| **Hvit** | Renhet, enkelhet, rom | Minimal, helse, tech |

---

## Sjekkliste

Før levering, bekreft:

- [ ] Primærfarge er IKKE standard Tailwind blue/violet
- [ ] Palett har tydelig hierarki (primær, sekundær, aksent)
- [ ] Alle tekst-kombinasjoner har 4.5:1 kontrast
- [ ] UI-elementer har 3:1 kontrast
- [ ] Semantic colors definert (success, error, warning)
- [ ] Dark mode vurdert eller implementert
- [ ] CSS variables brukes for konsistens
- [ ] Farger reflekterer BRAND.md personlighet
