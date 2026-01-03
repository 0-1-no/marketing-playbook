---
name: aesthetic-direction
description: Definerer visuell retning og "vibe" for merkevaren. Les denne først ved nytt design-arbeid.
---

# Aesthetic Direction

> **Metodikk-fil:** Dette er en guide for å VELGE visuell retning.
> Faktisk valgt retning dokumenteres i `./marketing/DESIGN-SYSTEM.md`.

---

## Velg Din Vibe

Før du designer, **commit til en retning**. Ikke prøv å være alt for alle.

---

## 7 Aesthetic Directions

### 1. Brutalist / Raw

| Egenskap | Beskrivelse |
|----------|-------------|
| **Vibe** | Rå, upolert, ærlig, konfronterende |
| **Typografi** | Monospace, tunge weights, store størrelser |
| **Farger** | Høy kontrast, svart/hvitt, én aksent |
| **Layout** | Asymmetrisk, grid-brudd, overlapping |
| **Borders** | Skarpe, tykke, synlige |
| **Motion** | Minimal eller glitchy |

**Passer for:** Tech startups, indie brands, avant-garde, dev tools

**Eksempler:** Balenciaga, Bloomberg, brutalist.one

```css
:root {
  --aesthetic: brutalist;
  --density: dense;
  --contrast: dramatic;
  --motion: minimal;
  --edges: sharp;
  --texture: raw;
}
```

---

### 2. Minimal / Refined

| Egenskap | Beskrivelse |
|----------|-------------|
| **Vibe** | Elegant, presist, luftig, sofistikert |
| **Typografi** | Thin weights, mye whitespace, presise linjer |
| **Farger** | Monokrom, subtile nyanser, én aksent |
| **Layout** | Perfekt grid, balansert, romslig |
| **Borders** | Tynne eller ingen, subtile dividers |
| **Motion** | Raffinert, sakte, elegant |

**Passer for:** Luksus, SaaS, profesjonelle tjenester, finans

**Eksempler:** Apple, Aesop, Muji

```css
:root {
  --aesthetic: minimal;
  --density: spacious;
  --contrast: subtle;
  --motion: restrained;
  --edges: sharp;
  --texture: smooth;
}
```

---

### 3. Maximalist / Chaos

| Egenskap | Beskrivelse |
|----------|-------------|
| **Vibe** | Energisk, overveldende, leken, disruptiv |
| **Typografi** | Mixed weights, variert størrelse, overlay |
| **Farger** | Mange farger, gradienter, clash |
| **Layout** | Kaotisk men kontrollert, lag på lag |
| **Borders** | Variert, dekorativt |
| **Motion** | Ekspressiv, overraskende, mye |

**Passer for:** Kreative byrå, underholdning, unge merkevarer, kunst

**Eksempler:** Spotify Wrapped, Nike SNKRS, Mailchimp old

```css
:root {
  --aesthetic: maximalist;
  --density: dense;
  --contrast: dramatic;
  --motion: expressive;
  --edges: varied;
  --texture: layered;
}
```

---

### 4. Organic / Natural

| Egenskap | Beskrivelse |
|----------|-------------|
| **Vibe** | Varm, jordnær, bærekraftig, autentisk |
| **Typografi** | Serif eller håndskrift-inspirert, mykt |
| **Farger** | Jordfarger, grønt, beige, dempet |
| **Layout** | Flytende, organiske former, asymmetri |
| **Borders** | Myke, avrundede, naturlige |
| **Motion** | Flytende, naturlig, behagelig |

**Passer for:** Wellness, mat, bærekraft, livsstil, håndverk

**Eksempler:** Patagonia, Oatly, Aesop

```css
:root {
  --aesthetic: organic;
  --density: balanced;
  --contrast: balanced;
  --motion: flowing;
  --edges: rounded;
  --texture: textured;
}
```

---

### 5. Retro / Futuristic

| Egenskap | Beskrivelse |
|----------|-------------|
| **Vibe** | Nostalgisk, neon, sci-fi, gaming |
| **Typografi** | 80s/90s fonter, pixelated, display |
| **Farger** | Neon på mørk, cyan/magenta, synth |
| **Layout** | Grid-basert, skjermer, panels |
| **Borders** | Glødende, outlined, tech |
| **Motion** | Glitch, scanlines, pulserende |

**Passer for:** Gaming, tech, underholdning, festivaler, crypto

**Eksempler:** Figma, Discord, Steam

```css
:root {
  --aesthetic: retro-future;
  --density: balanced;
  --contrast: dramatic;
  --motion: expressive;
  --edges: sharp;
  --texture: digital;
}
```

---

### 6. Editorial / Magazine

| Egenskap | Beskrivelse |
|----------|-------------|
| **Vibe** | Sofistikert, lesbar, innholdsrik, autoritet |
| **Typografi** | Serif headlines, streng hierarki, spalter |
| **Farger** | Begrenset palett, mye svart/hvitt |
| **Layout** | Kolonne-grid, stramt, typografi-drevet |
| **Borders** | Linjer som dividers, strenge |
| **Motion** | Minimal, tekst-fokus |

**Passer for:** Media, innhold, thought leadership, publikasjoner

**Eksempler:** NYT, Medium, Substack

```css
:root {
  --aesthetic: editorial;
  --density: balanced;
  --contrast: balanced;
  --motion: minimal;
  --edges: sharp;
  --texture: print;
}
```

---

### 7. Playful / Toy-like

| Egenskap | Beskrivelse |
|----------|-------------|
| **Vibe** | Glad, vennlig, leken, tilgjengelig |
| **Typografi** | Runde fonter, bold, store størrelser |
| **Farger** | Primærfarger, pasteller, glad palett |
| **Layout** | Avrundet, ikoner, illustrasjoner |
| **Borders** | Tykke, runde, lekne |
| **Motion** | Bouncy, overshoot, karakter |

**Passer for:** B2C, barn, edtech, community, spill

**Eksempler:** Duolingo, Notion, Figma

```css
:root {
  --aesthetic: playful;
  --density: balanced;
  --contrast: balanced;
  --motion: bouncy;
  --edges: rounded;
  --texture: smooth;
}
```

---

## Hvordan Velge

### Steg 1: Les BRAND.md

Se på:
- **Tone of Voice** - Formell? Leken? Autoritær?
- **Personality** - Hvilke adjektiver beskriver merkevaren?
- **Values** - Hva står dere for?

### Steg 2: Se på målgruppen

- Hva forventer de?
- Hvilke nettsider bruker de?
- Hva er deres referansepunkter?

### Steg 3: Se på konkurrentene

- Hva gjør de?
- Hvordan kan du skille deg ut?
- **Gjør det motsatte** hvis alle gjør det samme

### Steg 4: Test på 3 personer

Vis dem et moodboard eller en quick mockup:
- "Hvordan føles dette?"
- "Hvem tror du dette er for?"
- "Hva husker du?"

---

## Den Ene Tingen

Hvert design må ha **én ting folk husker**:

| Type | Eksempler |
|------|-----------|
| **Uvanlig animasjon** | Cursor trails, liquid transitions, 3D |
| **Overraskende farge** | Neon på mørk, uventet aksent, gradient twist |
| **Distinkt typografi** | Custom font, dramatisk størrelse, unikt hierarki |
| **Layout som bryter** | Overlapping, asymmetri, scroll-hijack |
| **Signatur-element** | Maskot, ikon, form som repeteres |

**Spørsmål:** Hva vil folk huske 5 minutter etter de forlot siden?

---

## Aesthetic Tokens

Når retning er valgt, definer tokens:

```css
:root {
  /* Velg din aesthetic */
  --aesthetic: [brutalist|minimal|maximalist|organic|retro-future|editorial|playful];

  /* Density: Hvor tett er elementene? */
  --density: [compact|balanced|spacious];

  /* Contrast: Hvor dramatisk er forskjellene? */
  --contrast: [dramatic|balanced|subtle];

  /* Motion: Hvor mye bevegelse? */
  --motion: [expressive|balanced|restrained|minimal];

  /* Edges: Skarpe eller runde kanter? */
  --edges: [sharp|balanced|rounded];

  /* Texture: Glatt eller teksturert? */
  --texture: [raw|textured|organic|smooth|digital|print|layered];
}
```

Disse tokens informerer alle designbeslutninger og sikrer konsistens.

---

## Mapping: BRAND.md → Aesthetic

| Hvis BRAND.md sier... | Vurder denne retningen |
|----------------------|------------------------|
| "Profesjonell, tillitvekkende" | Minimal, Editorial |
| "Leken, vennlig, morsom" | Playful, Maximalist |
| "Innovativ, cutting-edge" | Brutalist, Retro-future |
| "Autentisk, ærlig, jordnær" | Organic, Editorial |
| "Ung, energisk, disruptiv" | Maximalist, Retro-future |
| "Premium, eksklusiv, luksuriøs" | Minimal, Editorial |
| "Kreativ, kunstnerisk, unik" | Brutalist, Maximalist |

---

## Blanding

Du kan mikse retninger, men vær forsiktig:

**Fungerer:**
- Minimal + Brutalist (clean men med edge)
- Playful + Organic (vennlig og jordnær)
- Editorial + Minimal (innholdsfokus med eleganse)

**Fungerer IKKE:**
- Alt på en gang (ingen retning)
- Motsetninger uten intensjon (maximalist + minimal)
- "Litt av alt" (AI slop)

**Regel:** Velg én primær retning, tillat én sekundær påvirkning.

---

## Eksempler på Vellykkede Retninger

| Merkevare | Primær | Sekundær | Resultat |
|-----------|--------|----------|----------|
| Linear | Minimal | Brutalist | Dark, dramatisk, presis |
| Notion | Playful | Minimal | Vennlig men ren |
| Stripe | Minimal | Maximalist | Elegant med gradient-twist |
| Discord | Retro-future | Playful | Gaming-vibe men tilgjengelig |
| Oatly | Organic | Brutalist | Jordnær men edgy |

---

## Neste steg

1. Velg din retning
2. Definer aesthetic tokens
3. Se [TYPOGRAPHY.md](TYPOGRAPHY.md) for font-valg
4. Se [COLOR-THEORY.md](COLOR-THEORY.md) for palett
5. Sjekk mot [ANTI-PATTERNS.md](ANTI-PATTERNS.md) før levering
