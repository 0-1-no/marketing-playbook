---
description: Full audit of project against BRAND.md, JOURNEY.md, and LEARNINGS.md. Includes ABC check, journey coverage, brand health (7 principles), and Brand Audience Fit validation.
allowed-tools: Read, Glob, Grep
---

# Marketing Playbook - Full Audit

Utfør en komplett gjennomgang av prosjektets marketing-innhold mot `BRAND.md`, `JOURNEY.md` og `LEARNINGS.md`.

## Steg 1: Les Marketing Playbook-filer

Finn og les alle filer. Hvis de ikke finnes, anbefal å kjøre `/marketing-playbook:init` først.

```
Laster Marketing Playbook...

✅ BRAND.md funnet
✅ JOURNEY.md funnet
✅ LEARNINGS.md funnet

Starter full audit...
```

Merk: LEARNINGS.md kan være tom for nye merkevarer. Dette er OK - audit vil anbefale å starte BAF-validering.

## Steg 2: Skann prosjektet

Søk etter relevante filer:

### Landing pages og UI
```
app/**/page.tsx
app/**/page.jsx
pages/**/*.tsx
pages/**/*.jsx
src/app/**/page.tsx
```

### Oversettelser/Copy
```
messages/**/*.json
locales/**/*.json
i18n/**/*.json
public/locales/**/*.json
```

### Meta og SEO
```
app/layout.tsx (metadata)
public/manifest.json
public/robots.txt
```

### Dokumentasjon
```
README.md
docs/**/*.md
*.md (rot-nivå)
```

### Marketing Assets
```
public/og-*.png
public/images/marketing/**
```

## Steg 3: Analyser hver kategori

### Landing Pages

For hver funnet page.tsx/jsx:
1. Les filen
2. Identifiser bruker-synlig tekst (headings, paragraphs, CTAs)
3. Sjekk mot ABC

Output:
```
📄 app/page.tsx (Landing page)

Funn:
- Heading: "[tekst]" ✅ On-brand
- CTA: "[tekst]" ⚠️ Bruker "enkel" - vurder alternativ

Score: 8/10
```

### Translations (i18n)

For messages/*.json:
1. Les JSON-struktur
2. Identifiser brukervendt tekst
3. Sjekk for "Words We Avoid"

Output:
```
📄 messages/nb-NO.json

Funn:
- 3 forekomster av "beste" (linje 45, 89, 122)
- Key message "finn leads basert på tech stack" mangler
- Tone of voice: Konsistent ✅

Score: 7/10
```

### Meta & SEO

Sjekk:
- Title tags
- Meta descriptions
- OG tags
- JSON-LD

Output:
```
📄 app/layout.tsx (Meta)

Funn:
- Title: "[tekst]" ✅
- Description: "[tekst]" ⚠️ Mangler key message
- OG Image: Finnes ✅

Score: 9/10
```

## Steg 4: "Words We Avoid" Scan

Kjør grep for alle ord i "Words We Avoid" listen:

```
Søker etter forbudte ord...

"beste": 5 funn
  - app/page.tsx:23
  - messages/nb-NO.json:45
  ...

"enkel": 2 funn
  - components/Hero.tsx:12
  ...
```

## Steg 5: Journey Coverage Analyse

Kartlegg innhold per journey stage:

### Innholdskartlegging

Kategoriser alle marketing-filer etter journey stage:

| Stage | Filer funnet | Dekning |
|-------|--------------|---------|
| Awareness | [antall] | ✅/⚠️/❌ |
| Consideration | [antall] | ✅/⚠️/❌ |
| Evaluation | [antall] | ✅/⚠️/❌ |
| Purchase | [antall] | ✅/⚠️/❌ |
| Post-purchase | [antall] | ✅/⚠️/❌ |
| Loyalty | [antall] | ✅/⚠️/❌ |

### Typisk kategorisering

| Filtype/Innhold | Stage |
|-----------------|-------|
| Annonse-copy, hero-tekst | Awareness |
| Produktsider, features | Consideration |
| Prising, sammenligning | Evaluation |
| Checkout, handlekurv | Purchase |
| Velkomst-e-post, onboarding | Post-purchase |
| Nyhetsbrev, VIP-innhold | Loyalty |

### Journey Gaps

Identifiser mangler:

```
📊 Journey Coverage

Awareness:     ████████░░ 80%  (4 filer)
Consideration: ██████████ 100% (6 filer)
Evaluation:    ██████░░░░ 60%  (3 filer)
Purchase:      ████░░░░░░ 40%  (2 filer)
Post-purchase: ░░░░░░░░░░ 0%   (0 filer) ⚠️
Loyalty:       ░░░░░░░░░░ 0%   (0 filer) ⚠️

Anbefalinger:
- ⚠️ Mangler post-purchase innhold (velkomst, onboarding)
- ⚠️ Mangler loyalty innhold (nyhetsbrev, lojalitetsprogram)
```

### Psykologi-bruk

Sjekk om innhold utnytter anbefalte prinsipper fra JOURNEY.md:

| Stage | Anbefalte prinsipper | Brukt? |
|-------|---------------------|--------|
| Awareness | Mere Exposure, Von Restorff | ✅/❌ |
| Consideration | Social Proof, Authority | ✅/❌ |
| ... | ... | ... |

## Steg 6: Brand Health Evaluering

Evaluer merkevaren mot de 7 brand-prinsippene. Se `skills/brand-principles.md` for detaljer.

### 1. ETHOS (Formål)
Vurder BRAND.md:
- Er "why" tydelig artikulert (utover å tjene penger)?
- Er verdiene spesifikke nok til å utelukke noe?
- Kan verdiene brukes til å ta beslutninger?

**Score:** [0-10]

### 2. REMARKABLE (Bemerkelsesverdig)
Vurder BRAND.md + innhold:
- Er USP/differentiators tydelige og unike?
- Ville kunder naturlig fortelle andre?
- Skiller det seg fra konkurrentene?

**Score:** [0-10]

### 3. RELATABLE (Relaterbar)
Vurder BRAND.md + copy:
- Er tone of voice distinkt og gjenkjennelig?
- Føles kommunikasjonen menneskelig?
- Er personligheten konsistent på tvers av touchpoints?

**Score:** [0-10]

### 4. INVOLVED (Involvert)
Vurder JOURNEY.md + praksis:
- Er det dokumentert feedback-loops?
- Finnes det co-creation eller community-elementer?
- Hvordan håndteres kundeinnspill?

**Score:** [0-10]

### 5. PRESENT (Tilstede)
Vurder JOURNEY.md touchpoints:
- Er merkevaren til stede i relevante kanaler?
- Gir tilstedeværelsen verdi utover salg?
- Er det konsistent på tvers av kanaler?

**Score:** [0-10]

### 6. INSPIRATIONAL (Inspirerende)
Vurder BRAND.md values + mission:
- Er verdiene noe folk kan rallye rundt?
- Representerer merkevaren noe større enn produktet?
- Matcher handlinger ord?

**Score:** [0-10]

### 7. DEFENSIBILITY (Forsvarbarhet)
Vurder BRAND.md differentiators:
- Hva gjør merkevaren vanskelig å kopiere?
- Hvilke typer forsvarbarhet finnes (nettverk, data, kultur)?
- Blir fordelen sterkere over tid?

**Score:** [0-10]

### Brand Health Output

```
───────────────────────────────────────────
BRAND HEALTH (7 Prinsipper)
───────────────────────────────────────────

1. ETHOS          [██████░░░░] 6/10
   ✅ Mission definert
   ⚠️ "Why" kunne vært tydeligere

2. REMARKABLE     [████████░░] 8/10
   ✅ Tydelig USP
   ✅ Differentiators dokumentert

3. RELATABLE      [████████░░] 8/10
   ✅ Tone of voice definert
   ⚠️ Personality kunne vært mer distinkt

4. INVOLVED       [████░░░░░░] 4/10
   ⚠️ Ingen feedback-loops dokumentert
   💡 Vurder community eller NPS

5. PRESENT        [██████░░░░] 6/10
   ✅ Kanaler definert
   ⚠️ Mangler verdi-innhold utover salg

6. INSPIRATIONAL  [██░░░░░░░░] 2/10
   ⚠️ Verdier føles generiske
   💡 Hva vil folk rallye rundt?

7. DEFENSIBILITY  [░░░░░░░░░░] 0/10
   ❌ Ikke adressert
   💡 Hva gjør dere vanskelig å kopiere?

───────────────────────────────────────────
BRAND HEALTH TOTAL: 34/70 (49%)
───────────────────────────────────────────

Prioriterte forbedringer:
1. Definer forsvarbarhet (moat)
2. Styrk inspirerende verdier
3. Etabler feedback-loops
```

## Steg 7: Brand Audience Fit (BAF)

Evaluer om merkevaren resonerer med målgruppen i praksis.

> "Brand-Audience Fit er når kunder forstår, bruker og hjelper med å promotere
> produktet ditt som et resultat av verdien de får fra det."

BAF er inspirert av Product-Market Fit, men fokuserer på merkevare-resonans.

### Sjekk LEARNINGS.md

Les `LEARNINGS.md` for å vurdere BAF-status:

**Indikatorer på høy BAF:**
- Konverteringsrate ≥2%
- Kunder anbefaler aktivt (NPS >50)
- Word-of-mouth driver vekst
- Lavere CAC over tid
- Kort salgssyklus

**Indikatorer på lav BAF:**
- Må "pushe" hardt for salg
- Høy CAC som ikke synker
- Få gjenkjøp/referrals
- Kunder forstår ikke verdien
- Mye priskonkurranse

### BAF Evaluering

| Indikator | Status | Kommentar |
|-----------|--------|-----------|
| Validert med tester? | ✅/⚠️/❌ | [fra LEARNINGS.md] |
| Konverteringsrate ≥2%? | ✅/⚠️/❌ | [faktisk rate] |
| Dokumenterte learnings? | ✅/⚠️/❌ | [antall innsikter] |
| Segmenter identifisert? | ✅/⚠️/❌ | [beste segment] |

### BAF Output

```
───────────────────────────────────────────
BRAND AUDIENCE FIT
───────────────────────────────────────────

Status: [✅ Validert / ⚠️ Under testing / ❌ Ikke validert]

Resonans-nivå: [Høy / Medium / Lav / Ukjent]

Bevis:
- Konverteringsrate: [X%] (benchmark: ≥2%)
- Beste segment: [segment]
- Dokumenterte tester: [antall]
- Learnings: [antall innsikter]

[Hvis ikke validert:]
⚠️ ADVARSEL: Unngå å skalere før BAF er validert.

   Anbefalt:
   1. Kjør test-kampanje mot målgruppe
   2. Sett opp venteliste eller forhåndssalg
   3. Mål konvertering og dokumenter i LEARNINGS.md

   En merkevare med høy BAF selger seg selv.
   En merkevare med lav BAF krever konstant pushing.

───────────────────────────────────────────
```

## Steg 8: Sammendrag

```
═══════════════════════════════════════════
        MARKETING PLAYBOOK AUDIT
═══════════════════════════════════════════

Prosjekt: [navn]
BRAND.md: [dato sist oppdatert]
JOURNEY.md: [dato sist oppdatert]
Skannet: [antall] filer

═══════════════════════════════════════════
TOTAL SCORE
═══════════════════════════════════════════

ABC Score:          [X/10]  (Innhold vs BRAND.md)
Journey Score:      [X/10]  (Funnel-dekning)
Brand Health:       [X/70]  (7 prinsipper)
Brand Audience Fit: [✅/⚠️/❌] (Validering)

TOTAL: [X]%

───────────────────────────────────────────
PER KATEGORI
───────────────────────────────────────────

- Landing pages: 8/10 (3 filer)
- Translations: 7/10 (2 filer)
- Meta/SEO: 9/10 (1 fil)
- Docs: N/A (ingen funnet)

───────────────────────────────────────────
JOURNEY COVERAGE
───────────────────────────────────────────

Awareness:     ████████░░ 80%
Consideration: ██████████ 100%
Evaluation:    ██████░░░░ 60%
Purchase:      ████░░░░░░ 40%
Post-purchase: ░░░░░░░░░░ 0%  ⚠️
Loyalty:       ░░░░░░░░░░ 0%  ⚠️

═══════════════════════════════════════════
TOP 5 FORBEDRINGER
═══════════════════════════════════════════

1. [Mest kritisk]
2. [Nest mest kritisk]
3. ...

═══════════════════════════════════════════
FORBUDTE ORD FUNNET
═══════════════════════════════════════════

| Ord | Antall | Filer |
|-----|--------|-------|
| beste | 5 | page.tsx, nb-NO.json |
| ... | ... | ... |

═══════════════════════════════════════════
JOURNEY GAPS
═══════════════════════════════════════════

⚠️ Manglende stages:
- Post-purchase: Ingen velkomst-e-post eller onboarding
- Loyalty: Ingen nyhetsbrev eller lojalitetsprogram

═══════════════════════════════════════════
BRAND HEALTH HIGHLIGHTS
═══════════════════════════════════════════

Styrker:
- [Prinsipper med høy score]

Forbedringspotensial:
- [Prinsipper med lav score]

═══════════════════════════════════════════
NESTE STEG
═══════════════════════════════════════════

Innhold:
- [ ] Fiks "Words We Avoid" funn
- [ ] Oppdater meta descriptions
- [ ] Legg til manglende key messages

Journey:
- [ ] Fyll journey gaps (post-purchase, loyalty)
- [ ] Oppdater JOURNEY.md med nye learnings

Brand Health:
- [ ] [Laveste prinsipp]: [Konkret tiltak]
- [ ] [Nest laveste]: [Konkret tiltak]
- [ ] [Tredje laveste]: [Konkret tiltak]

───────────────────────────────────────────

Kjør `/marketing-playbook:check [fil]` for detaljer om spesifikke filer.

═══════════════════════════════════════════
```

## Begrensninger

- Skann kun tekst-baserte filer
- Ignorer node_modules, .next, dist, build
- Fokuser på bruker-synlig innhold
