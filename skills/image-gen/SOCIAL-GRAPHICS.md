# Social Media Graphics

> Templates og spesifikasjoner for Instagram, Twitter, LinkedIn og Pinterest.

---

## Plattform-oversikt

| Plattform | Preset | Aspekt | Bruk |
|-----------|--------|--------|------|
| Instagram Feed | `instagram` | 1:1 | Standard post |
| Instagram Story | `story` | 9:16 | Stories, Reels |
| Twitter | `twitter` | 16:9 | Tweet images |
| LinkedIn | `linkedin` | 4:3 | Feed posts |
| Pinterest | `pinterest` | 2:3 | Pins |

---

## Instagram

### Feed Post (1:1 Square)

```bash
uv run scripts/generate_image.py "Din prompt" --type instagram
```

**Template:**
```
Bold, eye-catching composition for Instagram feed,
using [BRAND_COLORS] with high saturation,
modern social media aesthetic,
clean design with strong visual impact,
square format optimized for mobile viewing
```

**Eksempel:**
```
Bold quote card background with abstract geometric shapes,
using vibrant coral (#FF6B6B) and deep navy (#1E3A5F),
modern social media aesthetic,
leave center space for text overlay,
high contrast for mobile feed visibility
```

### Story / Reels (9:16 Vertical)

```bash
uv run scripts/generate_image.py "Din prompt" --type story
```

**Template:**
```
Vertical composition optimized for mobile full-screen,
[STYLE] with [BRAND_COLORS],
dynamic visual flow from top to bottom,
space for text in upper third and lower third,
Instagram story aesthetic
```

**Eksempel:**
```
Vertical gradient composition from purple (#8B5CF6) at top to pink (#EC4899) at bottom,
with subtle floating geometric particles,
modern story aesthetic,
space in center for product/message,
optimized for mobile full-screen viewing
```

---

## Twitter

### Tweet Image (16:9)

```bash
uv run scripts/generate_image.py "Din prompt" --type twitter
```

**Template:**
```
Wide composition for Twitter feed,
[STYLE] with [BRAND_COLORS],
clean and professional look,
high contrast for timeline visibility,
space on left or right for potential text
```

**Eksempel:**
```
Modern tech illustration showing AI concept,
abstract neural network visualization,
using blue (#3B82F6) on dark background (#0F172A),
clean professional look optimized for Twitter feed,
wide 16:9 composition
```

---

## LinkedIn

### Feed Post (4:3)

```bash
uv run scripts/generate_image.py "Din prompt" --type linkedin
```

**Template:**
```
Professional composition for LinkedIn feed,
corporate yet modern aesthetic,
using [BRAND_COLORS] with balanced saturation,
trustworthy and polished appearance,
suitable for business audience
```

**Eksempel:**
```
Professional abstract composition representing business growth,
upward-trending elements with subtle data visualization,
using corporate blue (#1E40AF) and silver (#94A3B8),
modern yet trustworthy aesthetic,
suitable for LinkedIn thought leadership post
```

### LinkedIn Article Header

For artikler, bruk `--type og` (16:9).

---

## Pinterest

### Pin (2:3 Vertical)

```bash
uv run scripts/generate_image.py "Din prompt" --type pinterest
```

**Template:**
```
Vertical Pinterest-optimized composition,
[STYLE] with [BRAND_COLORS],
visually striking for Pinterest feed,
space at top and bottom for text overlays,
aspirational or informative mood
```

**Eksempel:**
```
Vertical infographic-style composition,
step-by-step visual elements flowing downward,
using warm terracotta (#C2410C) and cream (#FEF3C7),
Pinterest-friendly aesthetic,
space at top for title, bottom for call-to-action
```

---

## Stil-guide per plattform

### Instagram

- **Estetikk:** Bold, fargerikt, trend-bevisst
- **Farger:** Høy metning, kontrast
- **Komposisjon:** Sentral fokus, regel-av-tre
- **Mood:** Inspirerende, aspirerende, ekte

### Twitter

- **Estetikk:** Informativt, delbart, news-worthy
- **Farger:** Klar, profesjonell
- **Komposisjon:** Wide format, les fra venstre
- **Mood:** Aktuelt, engasjerende, smart

### LinkedIn

- **Estetikk:** Profesjonell, troverdig, polert
- **Farger:** Korporat men moderne
- **Komposisjon:** Balansert, luftig
- **Mood:** Autoritativ, innsiktsfull, karriere-fokusert

### Pinterest

- **Estetikk:** Aspirerende, organisert, estetisk
- **Farger:** Harmonisk, ofte pasteller eller rike jordtoner
- **Komposisjon:** Vertikal flyt, lagdelt informasjon
- **Mood:** Inspirerende, "save-worthy", tutorial-vennlig

---

## Prompt-templates per formål

### Quote Card

```
Abstract background for quote card,
[BRAND_COLORS] with subtle gradient,
space in center for quote text,
modern, inspiring aesthetic,
[PLATFORM] optimized format
```

### Produkt-teaser

```
Product showcase composition with [STYLE] aesthetic,
floating product placeholder in center,
[BRAND_COLORS] background with subtle depth,
premium feel, suitable for [PLATFORM] announcement
```

### Event/Webinar

```
Dynamic event promotion background,
energetic [STYLE] with [BRAND_COLORS],
space for event details and date,
professional yet exciting mood,
[PLATFORM] optimized
```

### Tips/Liste

```
Clean infographic-style background,
numbered or bulleted visual elements,
[BRAND_COLORS] with clear hierarchy,
educational, scannable aesthetic,
optimized for [PLATFORM] engagement
```

### Behind-the-scenes

```
Authentic workspace aesthetic,
warm natural lighting feel,
[BRAND_COLORS] as accents,
genuine, relatable mood,
[PLATFORM] story format
```

---

## Multi-plattform workflow

### 1. Start med master-design

Generer et 1:1 (Instagram) som basis:
```bash
uv run scripts/generate_image.py "Din konsept" --type instagram
```

### 2. Tilpass til andre formater

Bruk samme konsept, juster komposisjon:
```bash
# Twitter (videre)
uv run scripts/generate_image.py "Same concept, wide composition" --type twitter

# Story (høyere)
uv run scripts/generate_image.py "Same concept, vertical flow" --type story

# LinkedIn (profesjonelt)
uv run scripts/generate_image.py "Same concept, professional tone" --type linkedin
```

### 3. Legg til plattform-spesifikke elementer i Figma/Canva

- Tekst med riktig fontstørrelse per plattform
- Logo/watermark plassering
- CTA-knapper der relevant

---

## Engagement-tips

### Instagram

- Ansikter og mennesker (illustrert, ikke AI-foto)
- Sterke farger som popper i feed
- "Pattern interrupt" - noe uventet

### Twitter

- Data/statistikk visualisert
- Kontroversielle eller tankevekkende bilder
- News-aktig presentasjon

### LinkedIn

- Profesjonelle ikoner og symboler
- Infografikk-elementer
- Thought leadership estetikk

### Pinterest

- Tutorial/how-to layout
- Før/etter konsepter
- Sjekklister og lister visuelt

---

## Sjekkliste

- [ ] Riktig aspect ratio for plattformen
- [ ] Brand-farger konsistent
- [ ] Plattform-passende estetikk
- [ ] Plass for tekst/overlay
- [ ] Testet på mobil
- [ ] Under filstørrelse-grenser
