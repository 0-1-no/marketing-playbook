---
name: typography
description: Font-valg, pairing og hierarki. Bruk ved typografi-beslutninger.
---

# Typography

> **Metodikk-fil:** Dette er prinsipper og forslag for font-valg.
> Faktiske fonts dokumenteres i `./marketing/DESIGN-SYSTEM.md`.
> Font-navnene under er EKSEMPLER å vurdere - ikke påkrevde valg.

---

## Font Pairing Prinsipper

### Regel 1: Kontrast, ikke konflikt

God pairing har **tydelig kontrast** mellom display og body:

| Fungerer | Hvorfor |
|----------|---------|
| Serif headline + Sans body | Klassisk kontrast |
| Bold sans + Light sans | Vekt-kontrast |
| Display + Neutral | Personlighet + lesbarhet |

| Fungerer IKKE | Hvorfor |
|---------------|---------|
| To serif-fonter | For like |
| To display-fonter | Konkurrerer |
| Lik vekt på begge | Ingen hierarki |

### Regel 2: Maks 2-3 fonter

```
✅ God:
- Display: Clash Display
- Body: Satoshi

✅ OK:
- Display: Clash Display
- Body: Satoshi
- Mono: JetBrains Mono (kun kode)

❌ Dårlig:
- 4+ fonter = kaos
```

---

## Font-kategorier

### Display Fonts (Headlines)

Karakterfulle, distinkte, brukes stort.

| Font | Vibe | Passer for |
|------|------|-----------|
| **Clash Display** | Modern, bold | Tech, startup |
| **Cabinet Grotesk** | Geometric, clean | SaaS, minimal |
| **Fraunces** | Soft serif, warm | Lifestyle, organic |
| **Space Grotesk** | Futuristic | Tech, innovation |
| **Syne** | Experimental | Creative, art |
| **Playfair Display** | Elegant serif | Luxury, editorial |
| **Archivo Black** | Heavy, impact | Bold statements |
| **Bricolage Grotesque** | Quirky, friendly | Playful brands |

### Body Fonts (Brødtekst)

Lesbare, nøytrale, fungerer i lange tekster.

| Font | Vibe | Passer for |
|------|------|-----------|
| **Satoshi** | Modern, clean | Alt |
| **Plus Jakarta Sans** | Friendly, soft | B2C, apps |
| **DM Sans** | Geometric, neutral | SaaS |
| **Source Sans 3** | Professional | Enterprise |
| **Nunito Sans** | Rounded, friendly | Consumer |
| **IBM Plex Sans** | Technical, precise | Dev tools |

### Monospace (Kode, teknisk)

| Font | Vibe |
|------|------|
| **JetBrains Mono** | Developer-focused |
| **Fira Code** | Ligatures |
| **IBM Plex Mono** | Clean, professional |
| **Space Mono** | Retro-tech |

---

## AI Slop Fonts (Unngå som primær)

Disse er ikke dårlige, men overbrukt av AI:

| Font | Problem |
|------|---------|
| Inter | Default AI-valg |
| Roboto | Google default |
| Open Sans | Safe, boring |
| Lato | Overused |
| Poppins | Trendy → kjedelig |
| Montserrat | Everywhere |

**Unntak:** Kan brukes som body hvis display-font er distinkt.

---

## Typografi-skala

### Modular Scale

Bruk en konsistent skala. Anbefalt: **1.25 (Major Third)**

```css
:root {
  --text-xs: 0.75rem;     /* 12px */
  --text-sm: 0.875rem;    /* 14px */
  --text-base: 1rem;      /* 16px */
  --text-lg: 1.25rem;     /* 20px */
  --text-xl: 1.563rem;    /* 25px */
  --text-2xl: 1.953rem;   /* 31px */
  --text-3xl: 2.441rem;   /* 39px */
  --text-4xl: 3.052rem;   /* 49px */
  --text-5xl: 3.815rem;   /* 61px */
}
```

### Line Height

| Element | Line Height |
|---------|-------------|
| Headlines | 1.1 - 1.2 |
| Subheadlines | 1.2 - 1.3 |
| Body | 1.5 - 1.7 |
| UI labels | 1.2 - 1.4 |

### Letter Spacing

| Element | Tracking |
|---------|----------|
| Large headlines | -0.02em til -0.05em (tighter) |
| Body | 0 (default) |
| All caps | 0.05em til 0.1em (looser) |
| Small text | 0.01em (slightly looser) |

---

## Font Loading

### Next.js med next/font

```tsx
// app/layout.tsx
import { Clash_Display, Satoshi } from 'next/font/google';

const clashDisplay = Clash_Display({
  subsets: ['latin'],
  variable: '--font-display',
  display: 'swap',
});

const satoshi = Satoshi({
  subsets: ['latin'],
  variable: '--font-body',
  display: 'swap',
});

export default function RootLayout({ children }) {
  return (
    <html className={`${clashDisplay.variable} ${satoshi.variable}`}>
      <body className="font-body">{children}</body>
    </html>
  );
}
```

### Tailwind Config

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        display: ['var(--font-display)', 'system-ui'],
        body: ['var(--font-body)', 'system-ui'],
        mono: ['JetBrains Mono', 'monospace'],
      },
    },
  },
};
```

### Fallback Strategy

Alltid inkluder fallbacks:

```css
font-family: 'Clash Display', 'SF Pro Display', system-ui, sans-serif;
```

---

## Pairing Eksempler

### Modern Tech
```
Display: Space Grotesk (700)
Body: DM Sans (400, 500)
Mono: JetBrains Mono
```

### Warm & Friendly
```
Display: Fraunces (600)
Body: Plus Jakarta Sans (400, 500)
```

### Bold & Confident
```
Display: Clash Display (700)
Body: Satoshi (400, 500, 700)
```

### Editorial
```
Display: Playfair Display (700)
Body: Source Serif Pro (400)
```

### Playful
```
Display: Bricolage Grotesque (700)
Body: Nunito Sans (400, 600)
```

---

## Typografi-regler

### Hierarki

1. **Kun én H1 per side**
2. **Tydelig størrelseforskjell** mellom nivåer
3. **Vekt for sublevels**, ikke bare størrelse
4. **Farge for tertiær info** (muted text)

### Lesbarhet

| Regel | Verdi |
|-------|-------|
| Optimal linjelengde | 50-75 tegn |
| Minimum kontrast | 4.5:1 for body |
| Minimum fontstørrelse | 16px for body |
| Avstand mellom avsnitt | 1.5x line-height |

### Responsive

```css
/* Fluid typography */
h1 {
  font-size: clamp(2rem, 5vw + 1rem, 4rem);
}
```

---

## Sjekkliste

Før levering, bekreft:

- [ ] Display-font er IKKE Inter/Roboto/Arial
- [ ] Tydelig kontrast mellom display og body
- [ ] Maks 3 font-familier totalt
- [ ] Konsistent typografi-skala
- [ ] Line-height tilpasset bruk
- [ ] Font-loading optimalisert (swap)
- [ ] Fallbacks definert
- [ ] Lesbar på mobil (16px+ body)
