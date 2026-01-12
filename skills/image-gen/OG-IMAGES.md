# OpenGraph Images

> Templates og best practices for OG-bilder som ser bra ut ved deling.

---

## Spesifikasjoner

| Egenskap | Verdi |
|----------|-------|
| Dimensjon | 1200 × 630 px (ideelt) |
| Aspekt | 1.91:1 → Vi bruker 16:9 |
| Format | JPEG eller PNG |
| Filstørrelse | < 1MB (ideelt < 200KB) |

**Merk:** Gemini støtter ikke eksakt 1.91:1, så vi bruker 16:9 som er nærmest.

---

## Kommando

```bash
uv run scripts/generate_image.py "Din prompt" --type og
```

For høyere kvalitet:
```bash
uv run scripts/generate_image.py "Din prompt" --type og --resolution 2K
```

---

## Prompt Templates

### 1. Abstrakt / Geometrisk

Best for: Tech, SaaS, generelle artikler

```
Abstract geometric composition with [PRIMARY_COLOR] shapes and [ACCENT_COLOR] accents,
modern minimalist style, subtle gradients,
clean professional look, high contrast,
suitable for OpenGraph social preview
```

**Eksempel:**
```
Abstract geometric composition with deep blue (#1E40AF) triangular shapes
and vibrant orange (#F97316) accent lines,
modern minimalist style, subtle gradients,
clean professional look, white background with color blocks,
suitable for tech blog OpenGraph preview
```

### 2. Gradient Background

Best for: Annonsering, lanseringer, moderne brands

```
Smooth gradient background from [COLOR_1] to [COLOR_2],
with subtle [ELEMENT] floating in composition,
modern SaaS aesthetic, clean and premium feel,
suitable for social media sharing preview
```

**Eksempel:**
```
Smooth gradient background from deep purple (#7C3AED) to vibrant pink (#EC4899),
with subtle geometric shapes floating in composition,
modern SaaS aesthetic, clean and premium feel,
high contrast, suitable for product launch announcement
```

### 3. Illustrasjon / Konsept

Best for: Bloggposter, guider, tutorials

```
Modern flat illustration depicting [KONSEPT],
using [BRAND_COLORS] color palette,
clean vector-like style, professional business context,
balanced composition with space for potential text overlay
```

**Eksempel:**
```
Modern flat illustration depicting a rocket launching from a laptop screen,
representing startup growth and digital innovation,
using navy blue (#1E3A5F) and coral (#FF6B6B) color palette,
clean vector-like style, optimistic and dynamic mood
```

### 4. Isometrisk

Best for: Tech produkter, features, arkitektur

```
Isometric illustration of [ELEMENT/SCENE],
clean technical style with [COLOR] accents,
modern tech aesthetic, precise geometry,
white or light gray background
```

**Eksempel:**
```
Isometric illustration of interconnected data servers and cloud icons,
clean technical style with teal (#14B8A6) accents,
modern tech aesthetic, precise geometry,
light gray background, suitable for infrastructure article
```

### 5. Photo-style (ikke ansikter)

Best for: Lifestyle, workspace, produkter

```
Professional photo-style image of [SCENE/OBJECT],
soft natural lighting, shallow depth of field,
modern workspace aesthetic, warm color tones,
editorial quality, no visible faces or text
```

**Eksempel:**
```
Professional photo-style image of a minimal desk setup with laptop and coffee,
soft natural window lighting from the left,
modern workspace aesthetic, warm neutral tones,
shallow depth of field on the laptop screen,
editorial quality suitable for productivity article
```

---

## Hva fungerer for OG-bilder

### ✅ Gjør dette

- **Enkle komposisjoner** - Få elementer, tydelig fokus
- **Høy kontrast** - Skiller seg ut i feeds
- **Brand-farger** - Konsistent gjenkjennelse
- **Abstrakte former** - Unngår "stockphoto"-look
- **Plass for tekst** - La venstre/høyre side være åpen for overlay

### ❌ Unngå dette

- **Tekst i bildet** - Blir for liten/uleselig ved scaling
- **Detaljerte scener** - Mister detaljer i liten preview
- **Ansikter** - AI-genererte ansikter ser ofte unaturlige ut
- **Logoer** - Legg til logo i etterkant med Figma/Canva
- **For mange farger** - Hold det enkelt (2-3 farger)

---

## Workflow: Fra generering til publisering

### 1. Generer basisbilde

```bash
uv run scripts/generate_image.py "Abstract tech illustration, blue and orange" --type og
```

### 2. Åpne i Figma/Canva

- Legg til logo i hjørnet
- Legg til tittel-tekst hvis ønskelig
- Juster kontrast om nødvendig

### 3. Eksporter optimalt

- Format: JPEG med 80-85% kvalitet
- Maks filstørrelse: 200KB for rask lasting
- Navn: `[slug]-og.jpg` (f.eks. `seo-guide-og.jpg`)

### 4. Test i debuggere

| Plattform | Debugger |
|-----------|----------|
| Facebook | developers.facebook.com/tools/debug/ |
| LinkedIn | linkedin.com/post-inspector/ |
| Twitter | cards-dev.twitter.com/validator |

---

## Artikkeltype → Prompt-stil

| Artikkeltype | Anbefalt stil |
|--------------|---------------|
| How-to guide | Illustrasjon med steg-elementer |
| Nyhet/lansering | Gradient med dynamisk følelse |
| Teknisk deep-dive | Isometrisk eller abstrakt geometrisk |
| Mening/tanke | Enkelt gradient med tekstplass |
| Case study | Photo-style workspace/produkt |
| Sammenligning | Split-komposisjon med to elementer |

---

## Eksempler etter bransje

### SaaS / Software

```
Abstract network of connected nodes and lines,
representing data flow and connectivity,
using brand blue (#3B82F6) on dark navy (#0F172A) background,
modern tech aesthetic with subtle glow effects,
suitable for software product announcement
```

### E-commerce

```
Clean product showcase composition with floating geometric shapes,
premium e-commerce aesthetic,
using warm coral (#F97316) accents on cream background,
modern, trustworthy, suitable for shopping guide article
```

### Finance / Fintech

```
Abstract upward-trending graph visualization,
clean professional style with green (#10B981) accent,
trustworthy financial aesthetic,
navy and white color scheme,
suitable for investment guide preview
```

### Healthcare / Wellness

```
Soft, organic shapes suggesting calm and care,
gentle gradient from sage green (#86EFAC) to soft blue (#BAE6FD),
wellness aesthetic, reassuring mood,
suitable for health article preview
```

---

## Cache-busting tips

Når du oppdaterer OG-bilde:

1. **Facebook:** Bruk debugger → "Scrape Again"
2. **LinkedIn:** Legg til `?v=2` på bilde-URL midlertidig
3. **Twitter:** Vent 5-10 min, eller bruk validator

---

## Sjekkliste

- [ ] 16:9 aspect ratio (nærmest OG standard)
- [ ] Enkel komposisjon med tydelig fokus
- [ ] Brand-farger brukt konsistent
- [ ] Ingen tekst i selve bildet (legg til etterpå)
- [ ] Høy kontrast for synlighet i feeds
- [ ] Under 200KB filstørrelse
- [ ] Testet i Facebook/LinkedIn debugger
