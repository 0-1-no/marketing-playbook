# [Prosjektnavn] Design System

> Visuell identitet og komponentguide for [prosjektnavn].

---

## Aesthetic Direction

**Vibe:** [3-5 ord som beskriver stilen, f.eks. "Modern, bold, playful"]

**Direction:** [Valgt retning: Brutalist/Minimal/Maximalist/Organic/Retro-future/Editorial/Playful]

**The One Thing:** [Det ene elementet som gjør dette unikt og uforglemmelig]

### Aesthetic Tokens

```css
:root {
  --aesthetic: [valgt retning];
  --density: [compact|balanced|spacious];
  --contrast: [dramatic|balanced|subtle];
  --motion: [expressive|balanced|restrained|minimal];
  --edges: [sharp|balanced|rounded];
  --texture: [raw|textured|organic|smooth|digital|print|layered];
}
```

---

## Color Palette

### Core Colors

| Rolle | Navn | Hex | RGB | Bruk |
|-------|------|-----|-----|------|
| Primary | [Navn] | `#XXXXXX` | rgb(X,X,X) | CTAs, hovedhandlinger, brand |
| Secondary | [Navn] | `#XXXXXX` | rgb(X,X,X) | Sekundære elementer |
| Background | [Navn] | `#XXXXXX` | rgb(X,X,X) | Sidebakgrunn |
| Surface | [Navn] | `#XXXXXX` | rgb(X,X,X) | Kort, modaler, seksjoner |
| Text | [Navn] | `#XXXXXX` | rgb(X,X,X) | Primær tekst |
| Text Muted | [Navn] | `#XXXXXX` | rgb(X,X,X) | Sekundær tekst, hints |
| Accent | [Navn] | `#XXXXXX` | rgb(X,X,X) | Highlights, ikoner, lenker |
| Border | [Navn] | `#XXXXXX` | rgb(X,X,X) | Skillelinjer, rammer |

### Semantic Colors

| Rolle | Hex | Bruk |
|-------|-----|------|
| Success | `#XXXXXX` | Positive handlinger, bekreftelser |
| Warning | `#XXXXXX` | Advarsler, oppmerksomhet |
| Error | `#XXXXXX` | Feil, destruktive handlinger |
| Info | `#XXXXXX` | Informasjonsmeldinger |

### CSS Variables

```css
:root {
  /* Core */
  --color-primary: #XXXXXX;
  --color-primary-hover: #XXXXXX;
  --color-secondary: #XXXXXX;
  --color-background: #XXXXXX;
  --color-surface: #XXXXXX;

  /* Text */
  --color-text: #XXXXXX;
  --color-text-muted: #XXXXXX;
  --color-text-inverted: #XXXXXX;

  /* Border */
  --color-border: #XXXXXX;
  --color-border-focus: #XXXXXX;

  /* Semantic */
  --color-success: #XXXXXX;
  --color-warning: #XXXXXX;
  --color-error: #XXXXXX;
  --color-info: #XXXXXX;
}
```

### Tailwind Config

```js
// tailwind.config.js
colors: {
  brand: {
    50: '#XXXXXX',
    100: '#XXXXXX',
    200: '#XXXXXX',
    300: '#XXXXXX',
    400: '#XXXXXX',
    500: '#XXXXXX',  // Primary
    600: '#XXXXXX',
    700: '#XXXXXX',
    800: '#XXXXXX',
    900: '#XXXXXX',
  },
}
```

---

## Typography

### Font Stack

| Type | Font | Fallback | Bruk |
|------|------|----------|------|
| Display | [Font navn] | system-ui, sans-serif | Headlines, H1-H3 |
| Body | [Font navn] | system-ui, sans-serif | Brødtekst, UI |
| Mono | [Font navn] | monospace | Kode, teknisk |

### Type Scale

| Element | Font | Weight | Size | Line Height | Letter Spacing |
|---------|------|--------|------|-------------|----------------|
| Display | [font] | 700 | 4rem (64px) | 1.1 | -0.02em |
| H1 | [font] | 700 | 3rem (48px) | 1.15 | -0.02em |
| H2 | [font] | 600 | 2.25rem (36px) | 1.2 | -0.01em |
| H3 | [font] | 600 | 1.5rem (24px) | 1.3 | 0 |
| H4 | [font] | 600 | 1.25rem (20px) | 1.4 | 0 |
| Body Large | [font] | 400 | 1.125rem (18px) | 1.6 | 0 |
| Body | [font] | 400 | 1rem (16px) | 1.6 | 0 |
| Body Small | [font] | 400 | 0.875rem (14px) | 1.5 | 0 |
| Caption | [font] | 500 | 0.75rem (12px) | 1.4 | 0.01em |

### Font Loading

```tsx
// app/layout.tsx
import { [DisplayFont], [BodyFont] } from 'next/font/google';

const displayFont = [DisplayFont]({
  subsets: ['latin'],
  variable: '--font-display',
  display: 'swap',
  weight: ['600', '700'],
});

const bodyFont = [BodyFont]({
  subsets: ['latin'],
  variable: '--font-body',
  display: 'swap',
  weight: ['400', '500', '600'],
});

// I <html>
className={`${displayFont.variable} ${bodyFont.variable}`}
```

### Tailwind Config

```js
// tailwind.config.js
fontFamily: {
  display: ['var(--font-display)', 'system-ui', 'sans-serif'],
  body: ['var(--font-body)', 'system-ui', 'sans-serif'],
  mono: ['JetBrains Mono', 'monospace'],
},
```

---

## Components

### Buttons

#### Primary Button

```tsx
<button className="
  bg-brand-500 text-white
  px-6 py-3
  rounded-[radius]
  font-medium
  transition-all duration-200
  hover:bg-brand-600 hover:shadow-lg hover:-translate-y-0.5
  active:translate-y-0
  focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 focus-visible:ring-offset-2
">
  Primary Action
</button>
```

#### Secondary Button

```tsx
<button className="
  bg-transparent text-brand-500
  border-2 border-brand-500
  px-6 py-3
  rounded-[radius]
  font-medium
  transition-all duration-200
  hover:bg-brand-50
  focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 focus-visible:ring-offset-2
">
  Secondary Action
</button>
```

#### Ghost Button

```tsx
<button className="
  bg-transparent text-gray-600
  px-4 py-2
  rounded-[radius]
  font-medium
  transition-all duration-200
  hover:bg-gray-100 hover:text-gray-900
  focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-gray-500 focus-visible:ring-offset-2
">
  Ghost Action
</button>
```

### Cards

```tsx
<div className="
  bg-white dark:bg-gray-900
  border border-gray-200 dark:border-gray-800
  rounded-[card-radius]
  p-6
  transition-all duration-300
  hover:shadow-lg hover:border-gray-300
  hover:-translate-y-1
">
  <h3 className="font-display font-semibold text-lg">Tittel</h3>
  <p className="text-muted-foreground mt-2">Beskrivelse</p>
</div>
```

### Form Input

```tsx
<div className="space-y-2">
  <label htmlFor="input" className="text-sm font-medium">
    Label
  </label>
  <input
    id="input"
    type="text"
    className="
      w-full h-12 px-4
      bg-white dark:bg-gray-900
      border border-gray-300 dark:border-gray-700
      rounded-[input-radius]
      transition-all duration-200
      focus:border-brand-500 focus:ring-2 focus:ring-brand-500/20
      focus:outline-none
      placeholder:text-gray-400
    "
    placeholder="Placeholder"
  />
</div>
```

---

## Motion

### Timing

| Interaksjon | Varighet | Easing |
|-------------|----------|--------|
| Hover | 200ms | ease-out |
| Click/Press | 100ms | ease-in-out |
| Fade | 300ms | ease-out |
| Slide | 300ms | ease-out |
| Page transition | 400ms | ease-in-out |

### Easing Curves

```css
:root {
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

### Signature Animation

[Beskriv den ene signaturen animasjonen som er unik for dette designet]

```css
/* Eksempel */
.signature-animation {
  /* Implementasjon */
}
```

---

## Spacing

### Spacing Scale

```css
:root {
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-20: 5rem;     /* 80px */
  --space-24: 6rem;     /* 96px */
}
```

### Section Spacing

| Viewport | Padding Y |
|----------|-----------|
| Mobile | 4rem (64px) |
| Tablet | 6rem (96px) |
| Desktop | 8rem (128px) |

---

## Border Radius

```css
:root {
  --radius-sm: 0.25rem;   /* 4px - badges, tags */
  --radius-md: 0.5rem;    /* 8px - inputs */
  --radius-lg: 0.75rem;   /* 12px - buttons */
  --radius-xl: 1rem;      /* 16px - small cards */
  --radius-2xl: 1.5rem;   /* 24px - large cards */
  --radius-3xl: 2rem;     /* 32px - hero sections */
  --radius-full: 9999px;  /* Pills, avatars */
}
```

---

## Responsive Breakpoints

| Navn | Min-width | Tailwind |
|------|-----------|----------|
| sm | 640px | `sm:` |
| md | 768px | `md:` |
| lg | 1024px | `lg:` |
| xl | 1280px | `xl:` |
| 2xl | 1536px | `2xl:` |

---

## Do's and Don'ts

### ✅ Do

- [Konkret ting å gjøre basert på feedback]
- [Konkret ting å gjøre]
- [Konkret ting å gjøre]
- Bruk [display font] for headlines
- Hold kontrast over 4.5:1 for tekst
- Animer med GPU-akselererte properties (transform, opacity)

### ❌ Don't

- [Konkret ting å unngå basert på feedback]
- [Konkret ting å unngå]
- [Konkret ting å unngå]
- Bruk Inter som primærfont
- Lag lilla→blå gradienter
- Ha identisk border-radius på alt

---

## Quick Reference

### Primær palette

```
Primary:    #XXXXXX
Background: #XXXXXX
Text:       #XXXXXX
Accent:     #XXXXXX
```

### Fonts

```
Display: [Font] (600, 700)
Body: [Font] (400, 500, 600)
```

### Key Sizes

```
Button height: 48px
Input height: 48px
Card padding: 24px
Section padding: 64-128px
Container max-width: 1280px
```

---

*Generert: [DATO]*
*Iterasjoner: [ANTALL]*
*Godkjent av: [BRUKER]*
