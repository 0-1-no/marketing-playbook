# Marketing Playbook

> ABC-rammeverk for konsistent merkevare-kommunikasjon i Claude Code.

Marketing Playbook hjelper deg med å opprettholde konsistent merkevarestemme i alt markedsinnhold ved å opprette og håndheve `BRAND.md`-filer i prosjektene dine.

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

Når du kjører `/marketing-playbook:init`, opprettes to filer:

| Fil | Innhold |
|-----|---------|
| `BRAND.md` | ABC-rammeverket (Audience, Brand, Communication) |
| `JOURNEY.md` | Kundereise-kart (ToFU → Loyalty) |

## BRAND.md-struktur

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
# Få ABC-score og konkrete forbedringer
```

### Auditer hele prosjektet
```
/marketing-playbook:audit

# Skanner landing pages, oversettelser, meta-tagger
# Returnerer omfattende merkevare-rapport
```

## Skills

Pluginen inkluderer to skills som automatisk aktiveres når du jobber med markedsinnhold:

### marketing-playbook
- Leser BRAND.md før du skriver
- Følger ABC-sjekklisten
- Bruker riktige ord og tone

### marketing-psychology
35+ psykologiske prinsipper for effektiv markedsføring, organisert etter funnel-steg:

| Fase | Prinsipper |
|------|------------|
| **TOFU** (Awareness) | Mere Exposure, Information Gap, Von Restorff, Picture Superiority, Confirmation Bias, m.fl. |
| **MOFU/BOFU** (Conversion) | Anchoring, Halo Effect, Scarcity, Social Proof, Loss Aversion, Decoy Effect, m.fl. |
| **CX** (Retention) | Peak-End Rule, Sunk Cost, IKEA Effect, Nostalgia, Self-Reference, m.fl. |

Bruk denne som referanse når du lager landingssider, e-poster eller annonser.

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
