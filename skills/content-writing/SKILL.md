---
name: content-writing
description: Guide for å skrive markedsføringsinnhold - artikler, landing pages, website copy og guider. Aktiveres ved skriving av blogg, artikler, sidekopi eller dokumentasjon. Refererer ./marketing/BRAND.md for tone og ./marketing/CONTENT-RULES.md for innholdsregler.
---

# Content Writing

Denne skillen hjelper deg med å skrive forskjellige typer markedsføringsinnhold. Den dekker struktur, skannbarhet, hooks, og AEO-optimalisering for ulike innholdsformater.

---

## Arkitektur: Global Plugin + Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ CONTENT-WRITING SKILL (Global Plugin)                               │
│                                                                     │
│ Du leser dette nå. Det er del av marketing-playbook plugin.        │
│ Inneholder kun metodikk: hvordan strukturere og skrive innhold.    │
│ INGEN konkret tone eller regler - de kommer fra kodebasen.         │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/ (DENNE KODEBASEN)                                      │
│                                                                     │
│ Skreddersydd for prosjektet du jobber i akkurat nå:                │
│ • BRAND.md → Tone of Voice, Words We Use/Avoid                     │
│ • CONTENT-RULES.md → Strukturregler, voice-dimensjoner             │
│ • JOURNEY.md → Hvilken stage er leseren i?                         │
│ • DISTRIBUTION.md → SEO keywords, content plan                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Før du starter

1. **Les `./marketing/BRAND.md`** - Tone of Voice, ord å bruke/unngå
2. **Les `./marketing/CONTENT-RULES.md`** - Strukturregler og voice-dimensjoner
3. **Les `./marketing/JOURNEY.md`** - Hvilken stage er leseren i?

Hvis filene ikke finnes:
- Kjør `/marketing-playbook:init` for BRAND.md og JOURNEY.md
- Kjør `/content-writer:init` for CONTENT-RULES.md

---

## Ressurser (Les ved behov)

| Fil | Bruk når du... |
|-----|----------------|
| [ARTICLES.md](ARTICLES.md) | Skriver bloggpost, thought leadership, case study |
| [LANDING-PAGES.md](LANDING-PAGES.md) | Skriver konverteringsfokusert side |
| [WEBSITE-PAGES.md](WEBSITE-PAGES.md) | Skriver Om oss, Tjenester, Team, Kontakt |
| [GUIDES.md](GUIDES.md) | Skriver how-to, tutorial, dokumentasjon |
| [RESEARCH-PROCESS.md](RESEARCH-PROCESS.md) | Trenger kilder, data, ekspert-sitater |
| [ANTI-SLOP.md](ANTI-SLOP.md) | Vil humanisere AI-generert innhold |

---

## Beslutningstre

```
Hva skriver du?
│
├── Blog/Artikkel → ARTICLES.md
│   ├── Thought leadership (Mening + Bevis + Implikasjoner)
│   ├── How-To (Problem + Steg + Resultat)
│   ├── Nyhetskommentar (Event + Analyse + Takeaway)
│   ├── Listicle (Hook + Kuraterte punkter + Oppsummering)
│   ├── Case Study (Utfordring + Løsning + Resultater)
│   └── Sammenligning (Alternativer + Kriterier + Anbefaling)
│
├── Landing Page → LANDING-PAGES.md
│   ├── Produkt/Feature launch
│   ├── Kampanje/Promotion
│   ├── Lead generation
│   ├── Sign-up/Trial
│   └── Event registration
│
├── Website Page → WEBSITE-PAGES.md
│   ├── Om oss (Signature Story + Verdier)
│   ├── Tjenester (Hva + Hvem + Hvordan + Resultater)
│   ├── Team (Profiler + E-E-A-T signaler)
│   ├── Kontakt (Metoder + Forventninger)
│   └── Karriere (Kultur + Stillinger)
│
├── Guide/How-to → GUIDES.md
│   ├── Quick Start (5 min, kun essensielt)
│   ├── Tutorial (30 min, komplett gjennomgang)
│   ├── Reference (pågående, omfattende)
│   └── Troubleshooting (problem → løsning)
│
├── Research-tungt innhold → RESEARCH-PROCESS.md først
│   └── Så relevant content type
│
└── Kvalitetssjekk → ANTI-SLOP.md
    └── Humaniser og valider mot BRAND.md
```

---

## Content Types Quick Reference

| Type | Intent | Lengde | SEO | AEO | Journey Stage |
|------|--------|--------|-----|-----|---------------|
| Artikkel | Informational | 1000-3000 ord | Høy | Høy | Awareness, Consideration |
| Landing Page | Commercial | 500-1500 ord | Høy | Medium | Consideration, Evaluation |
| Website Page | Navigational | Varierer | Medium | Lav | Awareness, Consideration |
| Guide | Informational | 1500-5000 ord | Høy | Svært høy | Consideration, Post-purchase |

---

## 5 Kjerneprinsipp for Content Writing

### 1. Løs intent i første 100 ord

Ikke bygg opp til svaret. Gi det umiddelbart.

**Dårlig:**
```
Mange lurer på hva som er best. Det finnes flere alternativer.
La oss se på bakgrunnen først...
[500 ord senere]
...så svaret er X.
```

**Godt:**
```
Det beste alternativet for de fleste er X. Her er hvorfor,
og når du bør vurdere Y i stedet.
```

### 2. Skriv i answer blocks (40-60 ord)

AI-systemer siterer modulære blokker som kan stå alene.

**Godt eksempel:**
```
SEO (Search Engine Optimization) er prosessen med å optimalisere
nettsider for å rangere høyere i søkeresultater. Dette inkluderer
tre hovedområder: teknisk SEO for crawlability og hastighet,
on-page SEO for innhold og struktur, og off-page SEO for
autoritet gjennom lenker og omtaler.
```

### 3. Skannbarhet over alt annet

- H2/H3 hierarki (aldri hopp over nivåer)
- Korte avsnitt (2-4 setninger)
- Bullet points for lister (maks 7 punkter)
- Bold for nøkkelbegreper (sparsomt)
- Visuelle breaks (bilder, callouts, kodeblokker)

### 4. Én side = Én intent

Hver side skal løse ETT søk eller oppnå ETT mål. Ikke bland informasjons- og transaksjonsintent på samme side.

### 5. Autentisk voice > Perfekt grammatikk

Innhold som høres ut som en ekspert som forklarer til en kollega slår polert bedriftsspråk.

---

## Integrasjonspunkter

### Med storytelling-copywriting

| Når du... | Bruk... |
|-----------|---------|
| Trenger tittel/hook | [HEADLINES.md](../storytelling-copywriting/HEADLINES.md) |
| Strukturerer persuasivt | [FRAMEWORKS.md](../storytelling-copywriting/FRAMEWORKS.md) (AIDA, PAS) |
| Skriver UI-tekst | [MICROCOPY.md](../storytelling-copywriting/MICROCOPY.md) |
| Vil overbevise etisk | [PERSUASION.md](../storytelling-copywriting/PERSUASION.md) |

### Med seo-aeo

| Når du... | Bruk... |
|-----------|---------|
| Optimaliserer for AI-sitater | [AEO.md](../seo-aeo/AEO.md) |
| Legger til schema markup | [STRUCTURED-DATA.md](../seo-aeo/STRUCTURED-DATA.md) |
| Planlegger søkeord | [CONTENT-SEO.md](../seo-aeo/CONTENT-SEO.md) |
| Sjekker før lansering | [AUDIT-CHECKLIST.md](../seo-aeo/AUDIT-CHECKLIST.md) |

### Med lokale filer

| Fil | Hentes fra |
|-----|------------|
| Tone of Voice | `./marketing/BRAND.md` → Communication |
| Words We Use/Avoid | `./marketing/BRAND.md` → Communication |
| Voice-dimensjoner | `./marketing/CONTENT-RULES.md` |
| Strukturregler | `./marketing/CONTENT-RULES.md` |
| Journey stage | `./marketing/JOURNEY.md` |
| Keywords | `./marketing/DISTRIBUTION.md` → SEO Strategy |

---

## Anti-patterns (Unngå)

### Generiske åpninger
- "I dagens digitale verden..."
- "Det er viktig å merke seg at..."
- "Mange bedrifter opplever at..."

### Filler-fraser
- "Som nevnt tidligere..."
- "Det skal sies at..."
- "For å oppsummere kort..."

### Struktur-feil
- Hoppe over heading-nivåer (H2 → H4)
- Lange avsnitt (5+ setninger)
- Ingen visuelle breaks
- "Klikk her" som ankertekst

### Voice-feil
- Blande førsteperson og tredjeperson
- Overgenerell (ingen spesifikke tall/eksempler)
- Buzzwords fra Words We Avoid

---

## Sjekkliste før publisering

### Struktur
- [ ] Intent løst i første 100 ord
- [ ] H2/H3 hierarki korrekt (ingen hopp)
- [ ] Avsnitt 2-4 setninger
- [ ] Bullet lists maks 7 punkter
- [ ] 3-5 interne lenker inkludert

### Voice
- [ ] Matcher BRAND.md Tone of Voice
- [ ] Ingen Words We Avoid
- [ ] Spesifikke tall og eksempler
- [ ] Leses naturlig høyt

### SEO/AEO
- [ ] Primary keyword i title, H1, første 100 ord
- [ ] Answer blocks på 40-60 ord der relevant
- [ ] FAQ-seksjon med schema-ready format
- [ ] Kilder med attribusjon

### Kvalitet
- [ ] "Ville jeg lest dette selv?"-test
- [ ] "Er dette bedre enn topp 3 Google?"-test
- [ ] Ingen ANTI-SLOP mønstre

---

## Relaterte Skills

- `storytelling-copywriting` - Frameworks, headlines, persuasjon
- `seo-aeo` - Søkeoptimalisering og AI-synlighet
- `marketing-psychology` - Psykologi per journey stage
- `brand-principles` - Merkevare-fundament

---

## Commands

### Oppsett
```
/content-writer:init
```
Interaktiv setup for voice-dimensjoner og innholdsregler. Oppretter `./marketing/CONTENT-RULES.md`.

### Validering
```
/marketing-playbook:check
```
Sjekker innhold mot BRAND.md og CONTENT-RULES.md.
