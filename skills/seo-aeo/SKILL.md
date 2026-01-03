---
name: seo-aeo
description: SEO og Answer Engine Optimization (AEO) for søkemotorer og AI-søk. Aktiveres ved SEO-arbeid, innholdsoptimalisering, teknisk SEO, eller AI-synlighet. Leser fra marketing/DISTRIBUTION.md for kanalstrategi og BRAND.md for posisjonering.
---

# SEO & AEO

Denne skillen hjelper deg med å optimalisere for både tradisjonelle søkemotorer (Google, Bing) og AI-søkemotorer (ChatGPT, Perplexity, Claude, Gemini).

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ SEO-AEO SKILL (Global Plugin)                                       │
│                                                                     │
│ Du leser dette nå. Det er del av marketing-playbook plugin.        │
│ Inneholder kun metodikk: hvordan optimalisere for søk og AI.       │
│ INGEN konkrete søkeord eller URLs - de kommer fra kodebasen.       │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/DISTRIBUTION.md (DENNE KODEBASEN)                       │
│                                                                     │
│ Skreddersydd for prosjektet du jobber i akkurat nå.                │
│ ALLTID les herfra for faktiske verdier:                            │
│ • Faktiske søkeord og search intent                                │
│ • Faktiske URLs og sidestruktur                                    │
│ • Faktisk kanalstrategi og prioriteringer                          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Paradigmeskiftet: SEO → AEO

```
TRADISJONELL SEO (Link-økonomi)     AEO/GEO (Siterings-økonomi)
─────────────────────────────────────────────────────────────────
Rankings i SERP                  →  Sitater i AI-svar
Klikk til nettside               →  Nevnelser og attribusjon
Backlinks = autoritet            →  E-E-A-T = autoritet
Keyword-fokus                    →  Entity-fokus
Trafikk-måling                   →  Share of Voice i AI
```

**Kritisk innsikt:** Du kan vinne AI-sitater selv uten side-1 Google-ranking. De fleste ChatGPT-sitater kommer fra URLer på posisjon 21+.

---

## Før du starter

1. **Les `./marketing/DISTRIBUTION.md`** - Kanalstrategi og SEO-prioriteringer
2. **Les `./marketing/BRAND.md`** - Posisjonering som former søkeordstrategi
3. **Sjekk robots.txt** - Tillater den AI-crawlere?

Hvis filene ikke finnes, kjør `/marketing-playbook:init` først.

---

## Hvor lagres SEO-data?

All SEO-data for prosjektet lagres i `./marketing/DISTRIBUTION.md` under seksjonen **SEO & AEO Strategy**:

| Data | Lagres i |
|------|----------|
| Primary keywords | `DISTRIBUTION.md` → Primary Keywords tabell |
| Secondary keywords | `DISTRIBUTION.md` → Secondary Keywords tabell |
| Content plan | `DISTRIBUTION.md` → Content Plan tabell |
| AEO tracking | `DISTRIBUTION.md` → AEO Tracking tabell |
| Technical SEO status | `DISTRIBUTION.md` → Technical SEO Status tabell |
| Test-resultater | `LEARNINGS.md` → Dokumenter hva som fungerer |

**Denne skillen** (seo-aeo) inneholder kun metodikk - faktiske verdier går i `./marketing/`.

---

## Ressurser (Metodikk)

| Fil | Bruk når du... |
|-----|----------------|
| [TECHNICAL-SEO.md](TECHNICAL-SEO.md) | Optimaliserer Core Web Vitals, crawlability, robots.txt, sitemap |
| [ON-PAGE-SEO.md](ON-PAGE-SEO.md) | Skriver title tags, meta descriptions, heading-struktur, bilder |
| [STRUCTURED-DATA.md](STRUCTURED-DATA.md) | Implementerer schema.org, rich snippets, FAQ/HowTo markup |
| [AEO.md](AEO.md) | Optimaliserer for AI-søk (ChatGPT, Perplexity, Claude, Gemini) |
| [CONTENT-SEO.md](CONTENT-SEO.md) | Planlegger søkeord, intern lenking, innholdsstrategi |
| [SOCIAL-META.md](SOCIAL-META.md) | Legger til Open Graph, Twitter Cards for social deling |
| [AUDIT-CHECKLIST.md](AUDIT-CHECKLIST.md) | Sjekker alt før lansering |

---

## Beslutningstre

```
Hva jobber du med?
│
├── Ny side/landing page
│   ├── Les ON-PAGE-SEO.md (title, meta, headings)
│   ├── Les STRUCTURED-DATA.md (schema markup)
│   ├── Les SOCIAL-META.md (OG tags)
│   └── Kjør AUDIT-CHECKLIST.md før lansering
│
├── Teknisk optimalisering
│   ├── Les TECHNICAL-SEO.md
│   ├── Sjekk Core Web Vitals
│   ├── Konfigurer robots.txt for AI-crawlere
│   └── Valider sitemap.xml
│
├── Innholdsstrategi
│   ├── Les CONTENT-SEO.md (søkeord, lenking)
│   ├── Les AEO.md (skriv for AI-sitater)
│   └── Koble til BRAND.md for tone
│
├── AI-synlighet (AEO)
│   ├── Les AEO.md (hovedfokus)
│   ├── Les TECHNICAL-SEO.md (llms.txt, crawlere)
│   └── Les STRUCTURED-DATA.md (schema for AI)
│
└── Full SEO-audit
    └── Kjør /seo-aeo:audit
```

---

## 5 Kjerneprinsipp

### 1. Mobile-First er ikke valgfritt
Google indekserer primært mobil-versjonen. Desktop er sekundær.

### 2. Hastighet = Ranking
Core Web Vitals er rangeringssignal. LCP ≤2.5s, INP ≤200ms, CLS ≤0.1.

### 3. Én side = Én intent
Hver side skal løse ETT søk. Ikke bland informasjons- og transaksjonsintent.

### 4. Skriv for sitater, ikke bare klikk
AI-søk siterer korte, faktarike svar. 40-60 ord answer blocks.

### 5. Autoritet trumfer taktikk
E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) er fundamentet.

---

## Quick Reference: Kritiske tall

### On-Page
| Element | Anbefaling |
|---------|------------|
| Title tag | 50-60 tegn, keyword i første 40 |
| Meta description | 150-160 tegn med CTA |
| H1 | Én per side, inkluder keyword |
| URL | Kort, lesbar, keyword-rik |

### Core Web Vitals
| Metrikk | God | Trenger forbedring | Dårlig |
|---------|-----|-------------------|--------|
| LCP | ≤2.5s | 2.5-4s | >4s |
| INP | ≤200ms | 200-500ms | >500ms |
| CLS | ≤0.1 | 0.1-0.25 | >0.25 |

### Bilder
| Aspekt | Anbefaling |
|--------|------------|
| Format | WebP primær, AVIF moderne, JPEG fallback |
| Størrelse | <100KB hero, <50KB andre |
| Alt-tekst | 5-10 ord, beskrivende, keyword-relevant |

### AI Crawlere
| Crawler | User-Agent |
|---------|------------|
| OpenAI | GPTBot |
| Anthropic | ClaudeBot |
| Perplexity | PerplexityBot |
| Google AI | Google-Extended |
| Companybook | CompanybookBot |

---

## Kobling til BRAND.md

SEO MÅ reflektere merkevaren:

| BRAND.md | → | SEO |
|----------|---|-----|
| Posisjonering | → | Primære søkeord |
| Tone of Voice | → | Meta descriptions, content |
| Differentiators | → | Unique value i snippets |
| Target Audience | → | Search intent mapping |

**Alltid les BRAND.md først** - SEO skal forsterke posisjonering, ikke motsi den.

---

## Før du lanserer

Kjør denne sjekklisten (eller `/seo-aeo:audit`):

### Teknisk
- [ ] robots.txt tillater AI-crawlere (GPTBot, ClaudeBot, etc.)
- [ ] sitemap.xml er oppdatert og submitted
- [ ] HTTPS aktiv, ingen mixed content
- [ ] Core Web Vitals passerer (LCP ≤2.5s)

### On-Page
- [ ] Title tag 50-60 tegn med keyword
- [ ] Meta description 150-160 tegn med CTA
- [ ] Én H1 per side med keyword
- [ ] Bilder har alt-tekst og er komprimert

### Strukturert data
- [ ] Schema.org markup validert
- [ ] FAQPage eller HowTo der relevant
- [ ] Organization schema på root

### AEO-readiness
- [ ] Klare definisjoner i første 100 ord
- [ ] FAQ-seksjon med spørsmål-svar format
- [ ] Kilder og data med attribusjon
- [ ] llms.txt fil på root (valgfritt men anbefalt)

### Social
- [ ] Open Graph tags (og:title, og:description, og:image)
- [ ] Twitter Card tags
- [ ] Bilde 1200x630px

---

## Relaterte Skills

- `storytelling-copywriting` - Copy som konverterer og ranker
- `marketing-psychology` - Psykologi bak søkeadferd
- `brand-principles` - Merkevare-fundament for posisjonering
- `design-system` - UI som støtter SEO (hastighet, a11y)

---

## Audit Command

For full SEO/AEO-sjekk, kjør:

```
/seo-aeo:audit
```

Dette gir deg en scorecard med prioriterte forbedringer.
