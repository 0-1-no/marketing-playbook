---
name: image-gen
description: Genererer marketing-bilder med AI (Gemini / Nano Banana Pro). Aktiveres ved OG-bilder, social media grafikk, web-bannere, artikkelbilder, eller bildegenerering. Leser fra marketing/BRAND.md og marketing/DESIGN-SYSTEM.md for merkevare-konsistens.
---

# Image Generation Skill

Denne skillen hjelper deg med å generere merkevare-konsistente marketing-bilder ved hjelp av Gemini API (Nano Banana Pro).

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ IMAGE-GEN SKILL (Global Plugin)                                      │
│                                                                     │
│ Du leser dette nå. Inneholder:                                      │
│ • Prompt-templates for marketing-bilder                             │
│ • Best practices for AI-bildegenerering                             │
│ • Script for å generere bilder                                      │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/ (KODEBASEN DU JOBBER I)                                │
│                                                                     │
│ Les herfra for merkevare-verdier:                                   │
│ • BRAND.md: Tone of voice, verdier, posisjonering                  │
│ • DESIGN-SYSTEM.md: Farger, estetisk retning, vibe                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Forutsetninger

**Krav:** `GEMINI_API_KEY` miljøvariabel må være satt.

```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Les disse filene for merkevare-kontekst:**
- `marketing/BRAND.md` - Tone, verdier, målgruppe
- `marketing/DESIGN-SYSTEM.md` - Farger, estetikk, vibe

---

## Beslutningstre

```
Hva trenger du?
│
├── OpenGraph-bilde (deling på sosiale medier)
│   └── Les [OG-IMAGES.md](OG-IMAGES.md)
│
├── Social media grafikk
│   ├── Instagram, Twitter, LinkedIn, Pinterest
│   └── Les [SOCIAL-GRAPHICS.md](SOCIAL-GRAPHICS.md)
│
├── Web-banner eller hero image
│   └── Les [MARKETING-ASSETS.md](MARKETING-ASSETS.md)
│
├── Artikkel/blogg-bilde
│   └── Les [MARKETING-ASSETS.md](MARKETING-ASSETS.md)
│
└── Trenger hjelp med prompting?
    └── Les [PROMPT-GUIDE.md](PROMPT-GUIDE.md)
```

---

## Quick Start

### Generer bilde direkte

```bash
# OpenGraph-bilde (1200x630-ish)
uv run scripts/generate_image.py "Abstract tech illustration with blue gradients" --type og

# Instagram square
uv run scripts/generate_image.py "Minimalist product mockup" --type instagram

# Høyoppløselig banner (4K)
uv run scripts/generate_image.py "Modern gradient hero image" --type banner --resolution 4K
```

### Tilgjengelige presets

| Preset | Aspekt | Bruksområde |
|--------|--------|-------------|
| `og` | 16:9 | OpenGraph, Facebook, LinkedIn deling |
| `twitter` | 16:9 | Twitter Cards |
| `instagram` | 1:1 | Instagram feed |
| `story` | 9:16 | Instagram/TikTok stories |
| `linkedin` | 4:3 | LinkedIn posts |
| `banner` | 16:9 | Web-bannere, hero images |
| `ultrawide` | 21:9 | Cinematic headers |
| `article` | 16:9 | Blogg/artikkel headers |
| `portrait` | 3:4 | Portrett-format |
| `pinterest` | 2:3 | Pinterest pins |

### Oppløsninger

| Verdi | Beskrivelse | Anbefalt bruk |
|-------|-------------|---------------|
| `1K` | ~1024px (default) | Prototyping, raske iterasjoner |
| `2K` | ~2048px | Balansert kvalitet/hastighet |
| `4K` | ~4096px | Endelig produksjon, print |

---

## Workflow: Draft → Iterate → Final

**Anbefalt prosess:**

1. **Draft (1K)** - Rask feedback på prompt
   ```bash
   uv run scripts/generate_image.py "Din idé" --type og --resolution 1K
   ```

2. **Iterate** - Juster prompt basert på resultat

3. **Final (4K)** - Når prompten er perfekt
   ```bash
   uv run scripts/generate_image.py "Perfeksjonert prompt" --type og --resolution 4K
   ```

---

## Prompt-strategi for Marketing

### Bygg prompten fra merkevare-verdier

1. **Les DESIGN-SYSTEM.md** for:
   - Aesthetic direction (minimal, bold, organic, etc.)
   - Fargepalett (primary, accent, background)
   - Vibe-ord

2. **Les BRAND.md** for:
   - Tone of voice
   - Brand personality
   - Verdier og differensiatorer

### Prompt-struktur

```
[Stil/aesthetic]: [Hva skal vises], [Farger/stemning], [Tekniske detaljer]
```

**Eksempel:**
```
Modern minimalist illustration of a growth chart with upward arrows,
using deep blue (#1E3A5F) and vibrant orange (#FF6B35) accents,
clean geometric shapes, professional business context, white background
```

---

## Hva fungerer / Hva å unngå

### ✅ Fungerer godt

- **Abstrakte former** - Geometrisk, gradient, mønster
- **Illustrasjoner** - Flat design, isometrisk, line art
- **Produktbilder** - Mockups, studio-stil
- **Landskaper/scener** - Bakgrunner, miljøer
- **Enkle komposisjoner** - Få elementer, tydelig fokus

### ❌ Unngå

- **Tekst i bilder** - AI er dårlig på tekst. Legg til i Figma/Canva etterpå
- **Fotorealistiske ansikter** - Uncanny valley, etiske hensyn
- **Komplekse logoer** - Bruk overlay i etterkant
- **Veldig detaljerte scener** - Mister detaljer ved skalering
- **Spesifikke merkevarer** - Kan ikke reprodusere logoer nøyaktig

---

## Redigering av eksisterende bilder

```bash
# Legg til elementer
uv run scripts/generate_image.py "Add dramatic sunset lighting" --input ./photo.jpg

# Endre stil
uv run scripts/generate_image.py "Transform to watercolor painting style" --input ./image.png
```

Gemini bruker "semantic masking" - beskriv hva du vil endre, og den forstår konteksten.

---

## Integrasjon med andre skills

| Skill | Kobling |
|-------|---------|
| `design-system` | Les farger, fonts, aesthetic direction |
| `seo-aeo/SOCIAL-META.md` | Bildedimensjoner for OG-tags |
| `marketing-playbook` | Brand values for konsistent kommunikasjon |

---

## Ressurser (les ved behov)

| Fil | Bruk når du... |
|-----|----------------|
| [PROMPT-GUIDE.md](PROMPT-GUIDE.md) | Trenger hjelp med prompting-teknikker |
| [OG-IMAGES.md](OG-IMAGES.md) | Lager OpenGraph/social preview bilder |
| [SOCIAL-GRAPHICS.md](SOCIAL-GRAPHICS.md) | Lager Instagram, Twitter, LinkedIn grafikk |
| [MARKETING-ASSETS.md](MARKETING-ASSETS.md) | Lager bannere, artikkelbilder, hero images |

---

## Teknisk referanse

### API-modell

**Default:** `gemini-3-pro-image-preview` (Nano Banana Pro)
- Beste kvalitet for tekst i bilder
- Støtter 1K/2K/4K oppløsning
- Støtter image editing

**Alternativ:** `gemini-2.5-flash-image` (Nano Banana)
- Raskere og billigere
- Kun 1K/2K oppløsning
- God for prototyping

### Filformat

Gemini returnerer **JPEG** som default. Scriptet håndterer dette automatisk.

---

## Feilsøking

| Problem | Årsak | Løsning |
|---------|-------|---------|
| "No API key" | GEMINI_API_KEY ikke satt | `export GEMINI_API_KEY="..."` |
| "No image generated" | Prompt blokkert av safety | Reformuler prompten |
| Feil dimensjoner | Aspect ratio ikke støttet | Bruk en av: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 |
| Bilde ser generisk ut | Mangler stil-beskrivelse | Les PROMPT-GUIDE.md, legg til vibe-ord |
