# Marketing Playbook

> ABC-rammeverk for konsistent merkevare-kommunikasjon i Claude Code.

Marketing Playbook hjelper deg med å opprettholde konsistent merkevarestemme i alt markedsinnhold ved å opprette og håndheve marketing-filer i prosjektene dine.

**Mappestruktur:**
```
ditt-prosjekt/
└── marketing/           ← Alt marketing-innhold samlet
    ├── BRAND.md         - Hvem dere er (ABC-rammeverket)
    ├── JOURNEY.md       - Hvordan kunder opplever dere (funnel)
    └── LEARNINGS.md     - Bevis på at det fungerer (BAF)
```

## Installasjon

```bash
claude plugin install 0-1-no/marketing-playbook
```

## ABC-rammeverket

Marketing Playbook er bygget rundt tre kjernepilarer:

### A - Audience (Målgruppe)
- **Hvem** snakker du til?
- Hva er deres **pain points**?
- Hva er deres **mål**?

### B - Brand (Merkevare)
- Hva er din **posisjonering**?
- Hva er dine **verdier**?
- Hva gjør deg **unik**?

### C - Communication (Kommunikasjon)
- Hva er din **tone of voice**?
- Hvilke **ord bruker du**?
- Hvilke **ord unngår du**?

## Kommandoer

| Kommando | Beskrivelse |
|----------|-------------|
| `/marketing-playbook` | Vis status og versjon |
| `/marketing-playbook:init` | Opprett BRAND.md interaktivt |
| `/marketing-playbook:check` | Verifiser innhold mot BRAND.md |
| `/marketing-playbook:audit` | Full prosjekt-audit |

## Filer som opprettes

Når du kjører `/marketing-playbook:init`, opprettes `marketing/`-mappen med tre filer:

| Fil | Innhold |
|-----|---------|
| `marketing/BRAND.md` | ABC-rammeverket (Audience, Brand, Communication) + Validering |
| `marketing/JOURNEY.md` | Kundereise-kart (ToFU → Loyalty) |
| `marketing/LEARNINGS.md` | Brand Audience Fit validering og dokumenterte innsikter |

## marketing/BRAND.md-struktur

BRAND.md definerer hvem dere er:

```markdown
# [Prosjektnavn] Brand

## Audience
**Primary:** [Hvem er hovedmålgruppen?]
**Secondary:** [Andre målgrupper]

### Pain Points
- [Problemer du løser]

### Goals
- [Hva de vil oppnå]

## Brand
**Positioning:** [Én setning som beskriver posisjonen]
**Values:** [Kjerneverdier]
**Differentiators:** [Hva gjør deg unik]

## Communication
**Tone of Voice:** [Adjektiver som beskriver stemmen]
**Words We Use:** [Foretrukket terminologi]
**Words We Avoid:** [Ord å unngå]
```

## Brukseksempler

### Sjekk innhold før publisering
```
/marketing-playbook:check

# Lim inn landing page-tekst, e-post eller annonsetekst
# Sjekker mot marketing/BRAND.md og marketing/JOURNEY.md
# Gir ABC-score og konkrete forbedringer
```

### Auditer hele prosjektet
```
/marketing-playbook:audit

# Leser marketing/BRAND.md, JOURNEY.md og LEARNINGS.md
# Skanner landing pages, oversettelser, meta-tagger
# Analyserer journey coverage (hvilke funnel-steg er dekket?)
# Evaluerer Brand Health (7 prinsipper)
# Sjekker Brand Audience Fit validering
# Returnerer omfattende merkevare-rapport med prioriterte tiltak
```

## Skills

Pluginen inkluderer fire skills som automatisk aktiveres når du jobber med markedsinnhold:

### marketing-playbook
- Leser marketing/BRAND.md, JOURNEY.md og LEARNINGS.md før du skriver
- Følger ABC-sjekklisten
- Identifiserer riktig journey stage
- Bruker riktige ord og tone
- Sjekker BAF-status før skalering

### marketing-mindset
20 tidløse strategiske prinsipper for markedstenkning. Brukes som sparrepartner ved strategiske beslutninger:

| Kategori | Prinsipper |
|----------|------------|
| **Konkurransefordel** | Hvis det er lett å måle er det for sent, Alle taktikker har livssyklus, Vinn ved å ikke konkurrere, First mover overvurdert |
| **Verdi & Posisjonering** | Folk kjøper problemløsning, Pris er signal, Strategi er fravalg |
| **Merkevarebygging** | 60/40 regelen, Brand compounds, SOV→SOM, Mental+Physical availability, Distinctiveness>Differentiation |
| **Distribusjon** | Rule of Seven, Reach>Frequency, 95/5 (B2B) |
| **Kreativitet** | Emotion beats rational, Gjentatt eksponering, Kompleks≠Komplisert |
| **Måling** | Correlation≠causation, Det du måler er det du får |

### marketing-psychology
35+ psykologiske prinsipper for effektiv markedsføring, organisert etter funnel-steg:

| Fase | Prinsipper |
|------|------------|
| **TOFU** (Awareness) | Mere Exposure, Information Gap, Von Restorff, Picture Superiority, Confirmation Bias, m.fl. |
| **MOFU/BOFU** (Conversion) | Anchoring, Halo Effect, Scarcity, Social Proof, Loss Aversion, Decoy Effect, m.fl. |
| **CX** (Retention) | Peak-End Rule, Sunk Cost, IKEA Effect, Nostalgia, Self-Reference, m.fl. |

### brand-principles
7 prinsipper for å bygge en sterk merkevare (brukes i audit):

| Prinsipp | Beskrivelse |
|----------|-------------|
| **Ethos** | Ha et sterkt formål (why), misjon og verdier |
| **Remarkable** | Vær bemerkelsesverdig - ha en tydelig USP |
| **Relatable** | Vær relaterbar - ha en menneskelig stemme |
| **Involved** | Vær involvert - co-create med kunder |
| **Present** | Vær tilstede - i relevante kanaler |
| **Inspirational** | Vær inspirerende - folk rallyer rundt dere |
| **Defensibility** | Vær forsvarbar - vanskelig å kopiere |

Bruk disse som referanse når du bygger og evaluerer merkevarer.

## Brand Audience Fit (BAF)

> "Brand-Audience Fit er når kunder forstår, bruker og hjelper med å promotere produktet ditt som et resultat av verdien de får fra det."

BAF er inspirert av Product-Market Fit, men fokuserer på merkevare-resonans. En merkevare med høy BAF selger seg selv.

### Indikatorer på høy BAF
- Konverteringsrate ≥2%
- Kunder anbefaler aktivt (word-of-mouth)
- Lavere kundeanskaffelseskost (CAC) over tid
- Kort salgssyklus

### marketing/LEARNINGS.md
Dokumenter tester, resultater og innsikter i `marketing/LEARNINGS.md`:
- Hva fungerer og hva fungerer ikke
- Konverteringsrater og metrikker
- Beste kundesegmenter
- Hypoteser å teste videre

**Tips:** Ikke skaler markedsføringen før BAF er validert. Test først, dokumenter, iterer.

## Premium-versjon

For avanserte marketing-funksjoner, besøk [marketing.no](https://marketing.no):
- Utvidede copywriting-rammeverk (AIDA, PAS, etc.)
- SEO-innholdsoptimalisering
- Konkurrentanalyse-verktøy
- Kampanjeplanleggings-agenter

## Lisens

MIT

## Utvikler

[0-1.no](https://0-1.no) - AI-konsulenter for norske bedrifter
