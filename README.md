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
# 1. Oppdater marketplace-metadata (henter versjonsinformasjon fra GitHub)
claude plugin marketplace update 0-1-plugins

# 2. Reinstaller plugin for å hente ny versjon
claude plugin uninstall marketing-playbook@0-1-plugins
claude plugin install marketing-playbook@0-1-plugins
```

### Sjekk installert versjon

Du kan sjekke hvilken versjon du har installert:

```bash
# Via interaktiv UI
/plugin  # → Installed tab → Se versjonsnummer

# Eller sjekk filen direkte
cat ~/.claude/plugins/installed_plugins.json | grep -A5 "marketing-playbook"
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

Pluginen inkluderer 50 skills som automatisk aktiveres når du jobber med relevant innhold.

> **Viktig:** Skill-filene inneholder metodikk og prinsipper — ikke konkrete verdier.
> Faktiske verdier leses alltid fra `./marketing/`-mappen i prosjektet.

### Fundament

| Skill | Beskrivelse |
|-------|-------------|
| `marketing-playbook` | Hovedskill — ABC-sjekkliste, journey-mapping, switching dynamics |
| `marketing-mindset` | 20 strategiske prinsipper for markedstenkning |
| `brand-principles` | 7 prinsipper for merkevarebygging |
| `distribution-principles` | SOV→SOM, 60:40, Reach>Frequency |
| `customer-principles` | Lojalitet, retention, community |
| `marketing-psychology` | 50+ psykologiske prinsipper, prispsykologi, vekstmodeller |
| `customer-research` | Intervjuer, surveys, JTBD, the Mom Test, syntese → mater BRAND.md |
| `marketing-plan` | Komplett markedsplan-leveranse (situasjon, OKR, kanal-mix, budsjett, roadmap) |

### Innhold og Copy

| Skill | Beskrivelse |
|-------|-------------|
| `blog-writing` | Norske blogginnlegg med SEO/AEO-subagent, konseptforklaringer, image-gen og publiseringspipeline |
| `content-writing` | Artikler, guider, landing pages, content pillars, searchable vs shareable |
| `content-strategy` | Innholdsstrategi med pillar/cluster-arkitektur og 4-faktor topic scoring |
| `storytelling-copywriting` | AIDA, PAS, headlines, CRO-copy, sidestruktur |
| `copy-editing` | Redigerer/forbedrer/refresher eksisterende tekst (motstykke til storytelling-copywriting) |
| `social-content` | LinkedIn, X, Instagram, Facebook — hooks, repurposing |
| `email-sequence` | Velkomst, nurture, re-engasjering, onboarding-sekvenser |
| `sms` | SMS/MMS for nordisk e-handel (samtykke, flyt-typer, korte meldinger) |
| `ad-creative` | Annonseinnhold, bulk-generering, iterasjon |
| `lead-magnets` | 13 lead magnet-formater med stage-matching og konverteringsbenchmarks |
| `free-tool-strategy` | Engineering as marketing med 6 verktøytyper og 8-faktor scorecard |
| `marketing-ideas` | Idébank etter kategori tilpasset norske forhold |

### SEO og Synlighet

| Skill | Beskrivelse |
|-------|-------------|
| `seo-aeo` | SEO + Answer Engine Optimization for AI-søk (7 sub-guider) |
| `ai-seo` | Dedikert AI-siteringsoptimalisering for ChatGPT, Perplexity, Claude, Gemini |
| `programmatic-seo` | Skalerbar SEO med templates og data (10 playbooks) |
| `site-architecture` | Nettstedsarkitektur med 3-click rule, hub-and-spoke, Mermaid sitemap |
| `schema-markup` | JSON-LD strukturert data med 10+ schema-typer og CMS-patterns |
| `competitor-alternatives` | Konkurrent-sammenligningssider for SEO og salg |

### Konvertering (CRO)

| Skill | Beskrivelse |
|-------|-------------|
| `page-cro` | Landingssider, hjemmesider, prissider (7-stegs analyse) |
| `signup-flow-cro` | Registreringsflyt-optimalisering |
| `onboarding-cro` | Post-signup aktivering og aha-øyeblikk |
| `form-cro` | Skjema-optimalisering for leads, kontakt, demo |
| `popup-cro` | Modals, overlays, slide-ins |
| `paywall-upgrade-cro` | In-app paywalls og upgrade moments |

### Strategi og Vekst

| Skill | Beskrivelse |
|-------|-------------|
| `launch-strategy` | Produktlanseringer med ORB-rammeverk |
| `pricing-strategy` | Prisstrategi, packaging, value metrics |
| `paid-ads` | Kampanjestrategi for Google, Meta, LinkedIn, Finn.no |
| `referral-program` | Referral og affiliate tilpasset norsk marked |
| `churn-prevention` | Cancel flows, save offers, dunning, retensjon |
| `ab-test-setup` | A/B-testing med hypotese-rammeverk |
| `analytics-tracking` | Generell tracking (PostHog + GA4 referanser) |
| `offers` | Tilbudsdesign — verdistabel, bundling, garanti, urgency (mellom pris og presentasjon) |
| `community-marketing` | Community-led growth, ambassadør-/superfan-programmer |
| `co-marketing` | Partnervalg, felles kampanjer, delt lead-attribusjon |
| `public-relations` | Earned media, presse, journalist-outreach (nordisk presse) |
| `competitor-profiling` | Research/profilering av konkurrenter (firmografi via Companybook) |

### B2B Salg

| Skill | Beskrivelse |
|-------|-------------|
| `revops` | Revenue operations med MQL-modell, speed-to-lead SLA, pipeline hygiene |
| `cold-email` | B2B cold outreach med 4 formler, deliverability-sjekkliste, norsk juridisk kontekst |
| `sales-enablement` | Pitch deck arc, innvendingshåndtering, battle cards, demo-script |
| `prospecting` | Finn/kvalifiser/bygg prospekt-lister (Companybook, Brønnøysund, GDPR) |

### Design og Bilder

| Skill | Beskrivelse |
|-------|-------------|
| `design-system` | UI/UX metodikk, anti-patterns, estetiske retninger (9 sub-filer) |
| `image-gen` | AI-bildegenerering for OG-bilder, social media, bannere |

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

## Versjonering og Releases

Marketing Playbook følger [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.0.0): Breaking changes i plugin API
- **MINOR** (0.X.0): Ny funksjonalitet, bakoverkompatibel
- **PATCH** (0.0.X): Bugfixes, dokumentasjonsendringer

### Automatisering

Repoet bruker GitHub Actions for:
- **Versjon-synkronisering**: `marketplace.json` synkes automatisk med `plugin.json`
- **Release-tags**: Git tags og GitHub Releases opprettes automatisk

### Pre-commit validering

For å sikre versjonskonsistens lokalt:

```bash
# Aktiver pre-commit hook
git config core.hooksPath .githooks
```

Se [CONTRIBUTING.md](CONTRIBUTING.md) for full release-workflow.

## Lisens

MIT

## Utvikler

[0-1.no](https://0-1.no) - AI-konsulenter for norske bedrifter
