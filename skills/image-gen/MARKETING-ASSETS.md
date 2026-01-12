# Marketing Assets

> Templates for web-bannere, hero images, artikkelbilder og andre marketing-materialer.

---

## Oversikt

| Asset-type | Preset | Aspekt | Bruk |
|------------|--------|--------|------|
| Hero banner | `banner` | 16:9 | Landing pages, headers |
| Ultra-wide | `ultrawide` | 21:9 | Cinematic headers |
| Artikkel-header | `article` | 16:9 | Blogg, guider |
| Feature-boks | `instagram` | 1:1 | Produktfeatures, ikoner |
| Email header | `banner` | 16:9 | Nyhetsbrev |

---

## Hero Images / Web Banners

### Standard Hero (16:9)

```bash
uv run scripts/generate_image.py "Din prompt" --type banner --resolution 2K
```

**Template:**
```
Wide hero image for website landing page,
[STYLE] aesthetic with [BRAND_COLORS],
dynamic composition with visual interest,
space on [LEFT/RIGHT] for headline overlay,
modern web design suitable for full-width display
```

**Eksempel - SaaS landing:**
```
Abstract hero image with flowing data streams and geometric shapes,
modern tech aesthetic with deep navy (#0F172A) background,
cyan (#06B6D4) and purple (#8B5CF6) accent elements,
dynamic left-to-right flow,
space on left side for headline and CTA,
suitable for SaaS landing page above-the-fold
```

### Cinematic Ultra-wide (21:9)

```bash
uv run scripts/generate_image.py "Din prompt" --type ultrawide
```

**Template:**
```
Cinematic ultra-wide composition,
panoramic [STYLE] with [BRAND_COLORS],
horizontal visual narrative,
suitable for immersive website header,
dramatic and impactful mood
```

**Eksempel:**
```
Cinematic ultra-wide abstract landscape,
flowing gradient from deep blue (#1E3A8A) through purple (#7C3AED) to pink (#EC4899),
geometric mountain-like silhouettes in foreground,
premium tech aesthetic,
suitable for immersive website header section
```

---

## Artikkel- og Bloggbilder

### Artikkel Header (16:9)

```bash
uv run scripts/generate_image.py "Din prompt" --type article
```

**Template for ulike artikkeltyper:**

#### How-to / Tutorial
```
Illustrative composition showing [TOPIC] concept,
step-by-step visual metaphor with [NUMBER] elements,
clean educational style with [BRAND_COLORS],
professional blog header aesthetic,
optimistic, helpful mood
```

#### Thought Leadership
```
Abstract conceptual illustration representing [TOPIC],
sophisticated minimalist style,
[BRAND_COLORS] with premium feel,
intellectual, authoritative mood,
suitable for long-form article header
```

#### Nyhet / Announcement
```
Dynamic announcement-style composition,
bold [STYLE] with [BRAND_COLORS],
energetic, news-worthy aesthetic,
suitable for company news or product launch article
```

#### Case Study
```
Professional case study header composition,
data visualization elements with success metrics aesthetic,
[BRAND_COLORS] with corporate polish,
trustworthy, results-oriented mood
```

---

## Feature Sections

### Feature Illustration (1:1)

```bash
uv run scripts/generate_image.py "Din prompt" --type instagram
```

**Template:**
```
Clean feature illustration representing [FEATURE_NAME],
iconic, recognizable visual metaphor,
[BRAND_COLORS] on [LIGHT/DARK] background,
modern app/web aesthetic,
suitable for feature grid or comparison section
```

**Eksempler:**

```
# Security feature
Clean illustration of a shield with lock icon,
modern flat design in teal (#14B8A6),
subtle gradient background,
representing data security feature
```

```
# Speed/Performance feature
Dynamic illustration of a speedometer or rocket,
bold orange (#F97316) accent on navy,
conveying speed and efficiency,
modern tech aesthetic
```

```
# Integration feature
Illustration of connected puzzle pieces or nodes,
blue (#3B82F6) on light gray,
representing seamless integration,
clean minimalist style
```

---

## Email Marketing

### Newsletter Header (16:9)

```bash
uv run scripts/generate_image.py "Din prompt" --type banner --resolution 1K
```

**Template:**
```
Email newsletter header composition,
[BRAND_COLORS] with welcoming aesthetic,
clean, not too busy (email-friendly),
space for newsletter title,
optimized for email clients (keep simple)
```

**Tips for email-bilder:**
- Hold det enkelt - komplekse gradienter kan rendres dårlig
- Unngå for mørke bakgrunner (spam-filtre)
- Max 600px bredde i praksis
- Filstørrelse under 100KB

---

## Advertising

### Display Ad Background

```bash
uv run scripts/generate_image.py "Din prompt" --aspect 1:1 --resolution 1K
```

**Template:**
```
Clean advertising background,
[BRAND_COLORS] with high visual impact,
significant negative space for ad copy,
attention-grabbing without being cluttered,
suitable for display advertising
```

**Standard størrelser:**
- Leaderboard: Bruk `--aspect 21:9` (tilnærmet 728x90)
- Medium Rectangle: Bruk `--aspect 4:3` (tilnærmet 300x250)
- Wide Skyscraper: Bruk `--aspect 9:16` (tilnærmet 160x600)

---

## Presentasjoner

### Slide Background

```bash
uv run scripts/generate_image.py "Din prompt" --type banner
```

**Template:**
```
Presentation slide background,
subtle [STYLE] with [BRAND_COLORS],
professional, not distracting,
suitable for text overlay and content,
corporate presentation aesthetic
```

**Varianter:**

```
# Title slide
Bold branded title slide background,
[BRAND_COLORS] with confident aesthetic,
space center-right for title and subtitle,
professional keynote style
```

```
# Content slide
Subtle content slide background,
light [BRAND_COLOR] tint with clean texture,
minimally intrusive for data/bullet content,
professional, readable
```

```
# Divider/section slide
Section divider slide background,
medium saturation [BRAND_COLORS],
visual break between content sections,
bold but not overwhelming
```

---

## Print & Offline

### Trykk-kvalitet

For print, bruk alltid 4K:

```bash
uv run scripts/generate_image.py "Din prompt" --type banner --resolution 4K
```

**Template:**
```
High-resolution marketing material,
[STYLE] with [BRAND_COLORS],
suitable for print production,
crisp details, clean edges,
professional quality for [brochure/poster/flyer]
```

---

## Prompt-bank etter industri

### Tech / SaaS

```
Abstract data visualization with flowing lines and nodes,
modern tech aesthetic with [BRAND_COLORS],
representing [AI/cloud/automation/connectivity],
futuristic yet approachable mood
```

### E-commerce / Retail

```
Lifestyle product scene with [PRODUCT_CONTEXT],
warm, aspirational aesthetic,
[BRAND_COLORS] accents,
premium shopping experience mood
```

### Finance / Fintech

```
Clean financial visualization with upward trends,
trustworthy, established aesthetic,
[BRAND_COLORS] with corporate polish,
confidence-inspiring mood
```

### Healthcare / Wellness

```
Soft, organic composition suggesting care and wellness,
calming [BRAND_COLORS] palette,
human-centered, empathetic aesthetic,
reassuring, professional mood
```

### Education / EdTech

```
Bright, engaging educational illustration,
representing [LEARNING_CONCEPT],
[BRAND_COLORS] with approachable feel,
inspiring, growth-oriented mood
```

---

## Workflow for kampanjer

### 1. Definer kampanje-stil

Les BRAND.md og DESIGN-SYSTEM.md, definer:
- Primær farge for kampanjen
- Visuell stil (abstrakt, illustrasjon, foto-stil)
- Stemning (energisk, rolig, profesjonell)

### 2. Generer master-asset

Start med hero/hovedbilde:
```bash
uv run scripts/generate_image.py "[Kampanje-konsept]" --type banner --resolution 2K
```

### 3. Tilpass til alle touchpoints

Bruk samme prompt-base, juster format:
- Social media versioner
- Email header
- Display ads
- Presentasjoner

### 4. Legg til tekst og CTA i design-verktøy

Figma/Canva for:
- Headlines og copy
- CTA-knapper
- Logo plassering
- Lokalisering

---

## Sjekkliste

- [ ] Riktig oppløsning for bruksområde (1K draft, 4K final)
- [ ] Brand-farger konsistent med DESIGN-SYSTEM.md
- [ ] Stil matcher BRAND.md aesthetic direction
- [ ] Plass for nødvendig tekst-overlay
- [ ] Testet på tvers av enheter/skjermstørrelser
- [ ] Filstørrelse optimalisert for mediet
