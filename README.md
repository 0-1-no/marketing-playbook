# Marketing Playbook

> Komplett marketing-rammeverk for Claude Code - fra merkevare til distribusjon til kundelojalitet.

Marketing Playbook hjelper deg med å bygge og opprettholde en konsistent merkevare gjennom hele kundereisen - fra første kontakt til lojal ambassadør.

---

## Arkitektur

Marketing Playbook har en **to-lags arkitektur**:

```
┌─────────────────────────────────────────────────────────────────────┐
│ MARKETING-PLAYBOOK (Global Plugin)                                  │
│                                                                     │
│ Installeres globalt for brukeren. Inneholder:                      │
│ • Metodikk og prinsipper                                           │
│ • Prosesser for å opprette ./marketing/                            │
│ • Sjekklister og best practices                                    │
│ • Guider for hvordan Claude skal jobbe                             │
│                                                                     │
│ INGEN konkrete verdier - kun rammeverk og arkitektur               │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/ (Per-Repo Innhold)                                     │
│                                                                     │
│ Opprettes i hver kodebase. Inneholder:                             │
│ • BRAND.md      - Faktiske brand-verdier, tone of voice            │
│ • JOURNEY.md    - Faktisk kundereise, touchpoints                  │
│ • DISTRIBUTION.md - Faktisk stack, kanaler, budsjett               │
│ • LEARNINGS.md  - Faktiske tester og resultater                    │
│ • DESIGN-SYSTEM.md - Faktiske farger, fonts, komponenter           │
│                                                                     │
│ SKREDDERSYDD for hver kodebase - dette er kildene til sannhet     │
└─────────────────────────────────────────────────────────────────────┘
```

### Hvordan det fungerer

1. **Plugin installeres globalt** - Gir Claude tilgang til metodikk og prosesser
2. **Claude kjører init** - Oppretter `./marketing/` med brukerens verdier
3. **Claude leser fra ./marketing/** - Alltid kilde til sannhet for faktiske verdier
4. **Plugin-skills guider arbeidet** - Prinsipper og sjekklister, ikke verdier

### Fleksibilitet

`./marketing/` tilpasses hver kodebase:
- **Full-stack nettside**: Alle filer inkludert DESIGN-SYSTEM.md
- **API/Backend**: Kanskje bare BRAND.md for dokumentasjon
- **Social media bot**: BRAND.md + DISTRIBUTION.md
- **Landing page**: Alt fokusert på konvertering

---

## Mappestruktur

```
ditt-prosjekt/
└── marketing/                 ← Skreddersydd for dette prosjektet
    ├── BRAND.md               - Hvem dere er (ABC-rammeverket)
    ├── JOURNEY.md             - Hvordan kunder opplever dere (funnel)
    ├── DISTRIBUTION.md        - Hvor dere viser dere (kanaler & stack)
    ├── LEARNINGS.md           - Bevis på at det fungerer (BAF)
    └── DESIGN-SYSTEM.md       - Visuell identitet (farger, fonts, komponenter)
```

## Installasjon

```bash
# 1. Legg til marketplace
claude plugin marketplace add 0-1-no/marketing-playbook

# 2. Installer plugin
claude plugin install marketing-playbook
```

### Verifiser installasjon
```bash
claude plugins list
```

## Oppdatering

Når det kommer nye versjoner av pluginen:

```bash
# Oppdater til nyeste versjon
claude plugin update marketing-playbook

# Eller med marketplace-navn
claude plugin update marketing-playbook@0-1-no
```

### Sjekk tilgjengelige oppdateringer
```bash
# Oppdater marketplace-metadata først
claude plugin marketplace update

# Deretter kjør update
claude plugin update marketing-playbook
```

> **Tips:** Se [CHANGELOG.md](CHANGELOG.md) for oversikt over hva som er nytt i hver versjon.

## De 6 Kategoriene

Marketing Playbook dekker seks fundamentale kategorier:

| # | Kategori | Spørsmål | Dekker |
|---|----------|----------|--------|
| 1 | **Audience** | Hvem snakker vi til? | Målgruppe, psykologi, kundereise |
| 2 | **Brand** | Hva tilbyr vi? | Posisjonering, verdier, differensiering |
| 3 | **Communication** | Hva forteller vi? | Storytelling, copywriting, innhold |
| 4 | **Distribution** | Hvordan når vi ut? | Kanaler, reach, budsjett |
| 5 | **Customer** | Hvordan bygger vi superfans? | Lojalitet, referrals, community |
| 6 | **Management** | Hvordan blir vi bedre? | Prinsipper, analyse, kampanjer |

---

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
- Hva er din **Signature Story**?
- Hvilke **kommunikasjonsprinsipper** følger dere?
- Hvilke **ord bruker du**?
- Hvilke **ord unngår du**?

## Kommandoer

### Hovedkommandoer

| Kommando | Beskrivelse |
|----------|-------------|
| `/marketing-playbook` | Vis status og versjon |
| `/marketing-playbook:init` | Opprett alle filer med checkpoint-basert generering |
| `/marketing-playbook:check` | Verifiser innhold mot marketing/-filene |
| `/marketing-playbook:audit` | Full prosjekt-audit med Brand Health og BAF |
| `/design-system:init` | Opprett DESIGN-SYSTEM.md med iterativ demo (bevarer alle versjoner) |
| `/content-writer:init` | Opprett CONTENT-RULES.md med valgfri showcase-app |
| `/seo-aeo:audit` | SEO og AEO audit med scorecard og prioriterte forbedringer |

### Separate init-kommandoer

For fleksibilitet kan du også kjøre hver del separat:

| Kommando | Beskrivelse |
|----------|-------------|
| `/marketing-playbook:brand-init` | Opprett kun BRAND.md (ABC-rammeverket) |
| `/marketing-playbook:journey-init` | Opprett kun JOURNEY.md (kundereise) |
| `/marketing-playbook:distribution-init` | Opprett DISTRIBUTION.md + LEARNINGS.md (kanaler og stack) |

## Filer som opprettes

Når du kjører `/marketing-playbook:init`, opprettes `marketing/`-mappen med fire filer:

| Fil | Innhold |
|-----|---------|
| `marketing/BRAND.md` | ABC-rammeverket (Audience, Brand, Communication) |
| `marketing/JOURNEY.md` | Kundereise-kart (ToFU → Loyalty) |
| `marketing/DISTRIBUTION.md` | Marketing stack, kanaler, og Quick Start SEO |
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

## marketing/JOURNEY.md-struktur

JOURNEY.md kartlegger kundereisen:

```markdown
# [Prosjektnavn] Journey

## Oversikt
| Stage | Mål | Bekymringer | Touchpoints |
|-------|-----|-------------|-------------|
| Awareness | Fange oppmerksomhet | "Trenger jeg dette?" | Ads, Social |
| Consideration | Bygge tillit | "Er dette troverdig?" | Landing, Blog |
| Evaluation | Hjelpe valget | "Er det verdt prisen?" | Pricing, Demo |
| Purchase | Friksjonsfritt kjøp | "Gjør jeg rett?" | Checkout |
| Post-purchase | Bekrefte valget | "Hva nå?" | Onboarding |
| Loyalty | Skape ambassadører | "Vil jeg fortsette?" | Email, Community |

## [Stage]
**Kundens mål:** [Hva de prøver å oppnå]
**Bekymringer:** [Hva de lurer på]
**Psykologi:** [Relevante prinsipper]
**Touchpoints:** [Kanaler og formater]
**Våre mål:** [Hva vi vil oppnå]
```

## marketing/DISTRIBUTION.md-struktur

DISTRIBUTION.md kartlegger hvor dere er til stede og SEO-strategi:

```markdown
# [Prosjektnavn] Distribution

## Marketing Stack
- **Email:** [Provider, liste-størrelse]
- **CMS:** [Platform, hosting]
- **Analytics:** [Verktøy]
- **Social:** [Aktive kanaler]
- **Ads:** [Plattformer, budsjett]
- **CRM:** [System]

## Current Channels
**Primary:** [Kanaler med mest ressurser]
**Secondary:** [Vedlikeholdes]
**Experimental:** [Testes]

## SEO & AEO Strategy
### Primary Keywords
| Keyword | Volume | Difficulty | Intent | Target Page | Status |

### Content Plan
| Tittel | Primary Query | Type | Status |

### AEO Tracking
| AI Engine | Testet query | Sitert? | Sist sjekket |

## Quick Start: Organic SEO
*For nye prosjekter uten etablert stack*
1. Keyword research → dokumenter i Primary Keywords
2. Cornerstone content → planlegg i Content Plan
3. Technical basics
4. Google Business Profile
5. Answer "People Also Ask" + AI → spor i AEO Tracking
```

## Brukseksempler

### Sjekk innhold før publisering
```
/marketing-playbook:check

# Lim inn landing page-tekst, e-post eller annonsetekst
# Sjekker mot alle 4 marketing/-filer
# Gir ABC-score, Distribution-score og konkrete forbedringer
```

### Auditer hele prosjektet
```
/marketing-playbook:audit

# Leser alle 4 marketing/-filer
# Skanner landing pages, oversettelser, meta-tagger
# Analyserer journey coverage og distribution stack
# Evaluerer Brand Health (7 prinsipper)
# Sjekker Brand Audience Fit validering
# Returnerer omfattende rapport med prioriterte tiltak
```

## Skills

Pluginen inkluderer skills som automatisk aktiveres når du jobber med relevant innhold.

> **Viktig:** Skill-filene inneholder metodikk og prinsipper - ikke konkrete verdier.
> Faktiske verdier leses alltid fra `./marketing/`-mappen i prosjektet.

### design-system
Aktiveres ved UI/UX-arbeid, styling, komponenter, landing pages.

| Fil | Innhold |
|-----|---------|
| `SKILL.md` | Decision tree og quick reference |
| `AESTHETIC-DIRECTION.md` | 7 visuelle retninger (Brutalist→Playful) |
| `ANTI-PATTERNS.md` | AI slop detection, sjekklister |
| `TYPOGRAPHY.md` | Font-valg prinsipper, pairing |
| `COLOR-THEORY.md` | Fargepalett-strategier, kontrast |
| `COMPONENTS.md` | Komponent-patterns, states |
| `MICRO-INTERACTIONS.md` | Animasjon-prinsipper, timing |
| `RESPONSIVE.md` | Mobile-first, breakpoints |
| `ACCESSIBILITY.md` | WCAG, keyboard-nav, kontrast |

**Output:** Oppretter/leser `marketing/DESIGN-SYSTEM.md` med faktiske verdier.

### seo-aeo
Aktiveres ved SEO-arbeid, meta-tagger, strukturert data, og AI-søkeoptimalisering (AEO).

| Fil | Innhold |
|-----|---------|
| `SKILL.md` | Decision tree og quick reference |
| `TECHNICAL-SEO.md` | Core Web Vitals, robots.txt, sitemap, AI-crawlere |
| `ON-PAGE-SEO.md` | Title tags, meta, headings, bilder, URLs |
| `STRUCTURED-DATA.md` | Schema.org, JSON-LD, rich snippets |
| `AEO.md` | Answer Engine Optimization for AI-søk |
| `CONTENT-SEO.md` | Søkeord, intern lenking, innholdsstrategi |
| `SOCIAL-META.md` | Open Graph, Twitter Cards |
| `AUDIT-CHECKLIST.md` | Pre-launch sjekkliste (63 punkter) |

**Kjør:** `/seo-aeo:audit` for full SEO/AEO-audit med scorecard.

### marketing-playbook
- Leser alle 4 marketing/-filer før du skriver
- Følger ABC-sjekklisten + Distribution-sjekk
- Identifiserer riktig journey stage
- Bruker riktige ord og tone
- Sjekker BAF-status før skalering

### storytelling-copywriting
Guide for storytelling og copywriting med progressiv loading. Hovedfilen gir oversikt, sub-filer lastes ved behov:

| Fil | Innhold |
|-----|---------|
| `SKILL.md` | Beslutningstre og quick reference |
| `STORYTELLING.md` | Signature Story, narrativ, StoryBrand |
| `FRAMEWORKS.md` | AIDA, PAS, BAB, FAB med anti-patterns |
| `HEADLINES.md` | Curiosity gap, numbers, "How to" |
| `MICROCOPY.md` | Buttons, errors, CTAs, empty states |
| `PERSUASION.md` | Conversational copy, rhythm, etikk |
| `CONTENT.md` | Evergreen, library vs publication |

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

### distribution-principles
14 tidløse prinsipper for å få budskapet ut:

| Kategori | Prinsipper |
|----------|------------|
| **Brand Building** | Cultural Imprinting, SOV→SOM, 60:40 Split, How Advertising Works |
| **Reach & Frequency** | Reach>Frequency, Rule of 7, 95/5 Rule (B2B) |
| **Channel Strategy** | Distribution follows attention, Owned>Rented, Compounding Touchpoints, Content-Channel Fit |
| **Consistency** | Consistency Compounds, Earn Attention, Dark Social |

### customer-principles
Tidløse prinsipper for kundelojalitet og community:

| Kategori | Prinsipper |
|----------|------------|
| **The Loyalty Loop** | Purchase → Experience → Loyalty → Advocacy → (ny kunde via WOM) |
| **Loyalty Myths** | 77/23 Rule (de fleste vil ikke ha "relasjon"), Shared Values > Interaksjoner, Mer ≠ Bedre |
| **Retention Economics** | 5-7x Rule, Leaky Bucket, Behavior ≠ Loyalty |
| **Experience & Memory** | Peak-End Rule, Moments of Truth, Recovery Paradox |
| **Word of Mouth** | Referrals are Earned, Negative Spreads Faster, Make it Easy to Share |
| **Customer Service** | Service as Marketing, Underpromise/Overdeliver, Solve the Problem |
| **Onboarding** | First 90 Days, Churn is Lagging, Value Lock-in > Contractual |
| **Community Building** | Crowd→Community progression, Learn from Religion, Sacrifice, Us vs Them |

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

## Lisens

MIT

## Utvikler

[0-1.no](https://0-1.no) - AI-konsulenter for norske bedrifter
