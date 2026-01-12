# Prompt Guide for Marketing Images

> Best practices for å skrive effektive prompts til Gemini bildegenerering.

---

## Grunnleggende struktur

En god prompt har disse elementene:

```
[Stil] + [Subjekt] + [Detaljer] + [Stemning/farger] + [Teknisk]
```

**Eksempel:**
```
Modern flat illustration of a rocket launching upward,
using vibrant orange and deep blue color palette,
clean geometric shapes, dynamic composition,
white background, suitable for web banner
```

---

## Teknikk 1: Narrative Prompts

Start enkelt med en beskrivende setning:

```
A professional headshot of a woman with brown hair, wearing a navy blazer,
against a soft gray studio background. Natural lighting, confident expression.
```

**Avslutt med stil-anker:**
```
Corporate professional style: polished, trustworthy, approachable.
```

---

## Teknikk 2: Structured Prompts

For mer kontroll, bruk strukturert format:

```
Subject: Growth chart with upward trend line
Style: Modern minimalist, flat design
Colors: Primary blue (#2563EB), accent green (#10B981)
Composition: Centered, clean white background
Mood: Optimistic, professional, tech-forward
Technical: Suitable for OpenGraph 1200x630
```

---

## Teknikk 3: Vibe Library

Bruk kjente estetiske referanser:

### Stilretninger

| Stil | Prompt-ord |
|------|------------|
| **Minimalist** | clean, simple, whitespace, geometric, understated |
| **Bold/Brutalist** | high contrast, stark, raw, industrial, heavy typography |
| **Organic** | flowing, natural, soft curves, earth tones, handcrafted |
| **Tech/Digital** | neon, gradient, futuristic, holographic, circuit |
| **Editorial** | magazine-quality, sophisticated, curated, art-directed |
| **Playful** | colorful, whimsical, rounded, fun, energetic |

### Stemnings-ord

| Stemning | Prompt-ord |
|----------|------------|
| **Profesjonell** | corporate, polished, trustworthy, established |
| **Innovativ** | cutting-edge, forward-thinking, disruptive |
| **Varm/vennlig** | welcoming, approachable, human, caring |
| **Premium** | luxury, exclusive, refined, sophisticated |
| **Energisk** | dynamic, bold, vibrant, action-oriented |

---

## Teknikk 4: Photography Terms

For fotorealistiske bilder, bruk fotografitermer:

### Kamera/linse
```
Shot on Sony A7III with 85mm f/1.4 lens
Wide-angle 24mm perspective
Macro close-up with shallow depth of field
```

### Belysning
```
Soft natural window light from the left
Three-point studio lighting setup
Golden hour warm backlighting
Dramatic rim light with dark background
```

### Komposisjon
```
Rule of thirds composition
Centered symmetrical framing
Low angle looking up
Bird's eye view from above
```

---

## Teknikk 5: Physical Object Framing

Generer bilde AV et fysisk objekt (magasin, poster, etc.):

```
A photo of a glossy magazine cover featuring [innhold].
The magazine is lying on a white marble surface with soft shadows.
Include a barcode and issue number in the corner.
```

Dette gir mer realistiske kontekst-bilder.

---

## Teknikk 6: Perspective Framing

Be om tolkning fra et perspektiv:

```
How a data scientist sees a spreadsheet
How a child sees a hospital
How an architect sees a cityscape
```

Modellen infererer hva dette perspektivet ville fremheve.

---

## Marketing-spesifikke templates

### SaaS / Tech produkt

```
Modern isometric illustration of [produkt/konsept],
using [primary color] and [accent color] palette,
clean tech aesthetic with subtle gradients,
floating UI elements, abstract data visualization,
professional SaaS marketing style
```

### E-commerce

```
Studio product shot of [produkt] on seamless white background,
professional lighting with soft shadows,
high-end e-commerce style, crisp details,
suitable for product page hero image
```

### B2B / Enterprise

```
Abstract geometric composition representing [konsept],
corporate blue and silver color scheme,
professional, trustworthy aesthetic,
subtle grid pattern, clean modern lines,
suitable for enterprise marketing
```

### Startup / Disruptor

```
Bold, energetic illustration of [konsept],
vibrant gradient from [color1] to [color2],
dynamic composition with movement,
modern startup aesthetic, optimistic mood
```

---

## Farger i prompts

### Beste praksis

1. **Bruk hex-koder** for presisjon:
   ```
   using brand blue (#2563EB) and accent coral (#FF6B6B)
   ```

2. **Beskriv fargeforhold:**
   ```
   predominantly white background with blue accents
   gradient from deep purple to vibrant pink
   ```

3. **Referer til kjente paletter:**
   ```
   Apple-inspired minimalist grayscale with single accent color
   Stripe-style gradient with purple and blue
   ```

---

## Negative prompts

Beskriv hva du IKKE vil ha:

```
Create a professional headshot.
Avoid: text, watermarks, logos, cluttered background, harsh shadows
```

Nyttig for å unngå vanlige AI-problemer.

---

## Iterativ forbedring

### Start bredt, bli spesifikk

**Iterasjon 1:**
```
Tech company hero image
```

**Iterasjon 2:**
```
Abstract geometric hero image for a tech company,
modern minimalist style
```

**Iterasjon 3:**
```
Abstract geometric hero image with interconnected nodes and lines,
representing AI and connectivity,
using deep navy (#0F172A) background with cyan (#06B6D4) accents,
modern minimalist style, subtle glow effects,
suitable for SaaS landing page header
```

---

## Vanlige feil å unngå

### ❌ For vagt
```
A nice picture for my website
```

### ✅ Bedre
```
Modern flat illustration of a team collaborating on a project,
using warm coral and teal color palette,
friendly professional style, diverse representation,
suitable for "About Us" page hero image
```

### ❌ For mye tekst-request
```
Create a banner with the text "Welcome to Our Platform"
```

### ✅ Bedre
```
Create an abstract banner background with welcoming, open composition.
Leave space on the left side for text overlay.
Warm gradient from orange to pink, modern SaaS style.
```

### ❌ For komplekst
```
A detailed scene with 15 people in an office building with
computers and coffee cups and plants and windows showing a city...
```

### ✅ Bedre
```
Modern office environment, shallow depth of field,
focus on a laptop screen with abstract UI,
blurred background with warm natural light,
professional, productive atmosphere
```

---

## Sjekkliste før du genererer

- [ ] Stil er definert (minimalist, bold, organic, etc.)
- [ ] Farger er spesifisert (helst hex-koder)
- [ ] Komposisjon er beskrevet
- [ ] Stemning/mood er inkludert
- [ ] Tekniske krav er nevnt (format, bruksområde)
- [ ] Negative elementer er listet (hva å unngå)

---

## Relaterte ressurser

- [OG-IMAGES.md](OG-IMAGES.md) - Spesifikke templates for OpenGraph
- [SOCIAL-GRAPHICS.md](SOCIAL-GRAPHICS.md) - Social media templates
- [MARKETING-ASSETS.md](MARKETING-ASSETS.md) - Bannere og artikkelbilder
