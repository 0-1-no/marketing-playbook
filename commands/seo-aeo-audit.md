---
description: Full SEO og AEO audit av kodebasen med scorecard og prioriterte forbedringer
allowed-tools: Read, Glob, Grep
---

# /seo-aeo:audit

Du er en SEO/AEO-ekspert som utfører en grundig audit av **den lokale kodebasen** brukeren jobber i.

> **Viktig:** Denne kommandoen auditer koden i brukerens prosjekt, ikke plugin-filene.
> Les `./marketing/DISTRIBUTION.md` for eksisterende SEO-strategi hvis den finnes.

---

## Steg 1: Identifiser prosjekttype

Finn ut hva slags prosjekt dette er:

```
Søk etter:
- package.json (Next.js, Astro, Gatsby, etc.)
- index.html (statisk)
- nuxt.config (Nuxt)
- astro.config (Astro)
```

Rapporter:
- Rammeverk/teknologi
- Hosting (Vercel, Netlify, etc. hvis identifiserbart)

---

## Steg 2: robots.txt sjekk

### Finn robots.txt

Søk i:
- `/public/robots.txt`
- `/static/robots.txt`
- `/robots.txt`

### Sjekk AI-crawlere

Verifiser at disse er tillatt (ikke Disallow):

| Crawler | User-Agent | Status |
|---------|------------|--------|
| OpenAI | GPTBot | ✅/❌ |
| Anthropic | ClaudeBot | ✅/❌ |
| Perplexity | PerplexityBot | ✅/❌ |
| Google AI | Google-Extended | ✅/❌ |
| Companybook | CompanybookBot | ✅/❌ |

### Rapporter issues

- Mangler robots.txt
- AI-crawlere blokkert
- Viktige sider blokkert

---

## Steg 3: Sitemap sjekk

### Finn sitemap

Søk etter:
- `/public/sitemap.xml`
- Referanse i robots.txt
- Dynamisk generering (next-sitemap.config.js, etc.)

### Rapporter

- Sitemap finnes/mangler
- Dynamisk eller statisk
- Referert i robots.txt

---

## Steg 4: llms.txt sjekk

Søk etter `/public/llms.txt` eller `/llms.txt`.

Rapporter:
- Finnes/mangler
- Hvis finnes: innhold og struktur

---

## Steg 5: Meta tags audit

### Finn meta-komponenter

Søk etter:
- `<title>` tags
- `<meta name="description"`
- `<meta property="og:`
- `<meta name="twitter:`
- Head-komponenter (Next.js Metadata, etc.)

### Sjekk for issues

| Issue | Hvordan finne |
|-------|---------------|
| Manglende title | Sider uten `<title>` |
| Manglende description | Sider uten `<meta name="description"` |
| Duplikat titles | Samme title på flere sider |
| Manglende OG-tags | Ingen `og:image`, `og:title` |

---

## Steg 6: Heading-struktur

### Søk etter heading-mønstre

```
Søk etter:
- <h1>, <H1>, className="h1"
- Flere H1 på samme side
- H3 uten H2 (hierarki-brudd)
```

### Rapporter

- Sider med 0 eller flere H1
- Brudd på hierarki

---

## Steg 7: Bilde-audit

### Søk etter bilder

```
Søk etter:
- <img> tags uten alt
- <Image> komponenter uten alt
- Store bildefiler (.jpg, .png over 200KB)
- Manglende width/height
```

### Sjekk formater

- Brukes WebP/AVIF?
- Er det lazy loading implementert?

---

## Steg 8: Strukturert data

### Finn JSON-LD

```
Søk etter:
- <script type="application/ld+json">
- @type":"FAQPage
- @type":"HowTo
- @type":"Article
- @type":"Organization
- @type":"Product
```

### Rapporter

| Schema type | Funnet | Status |
|-------------|--------|--------|
| Organization | Ja/Nei | ✅/⚠️ |
| Article/BlogPosting | Ja/Nei | ✅/⚠️ |
| FAQPage | Ja/Nei | ✅/⚠️ |
| BreadcrumbList | Ja/Nei | ✅/⚠️ |

---

## Steg 9: Performance indikatorer

### Søk etter

- Lazy loading (`loading="lazy"`, `lazy`)
- Preload (`<link rel="preload"`)
- Defer/async på scripts
- Viewport meta tag

---

## Steg 10: Generer Scorecard

Basert på funnene, generer scorecard:

```
┌─────────────────────────────────────────────────┐
│ SEO & AEO AUDIT SCORECARD                       │
│ Prosjekt: [navn]                                │
│ Dato: [dato]                                    │
├─────────────────────────────────────────────────┤
│                                                 │
│ TEKNISK SEO            ████████░░  X/10         │
│ • robots.txt:          [status]                 │
│ • AI-crawlere:         [status]                 │
│ • sitemap.xml:         [status]                 │
│ • HTTPS:               [status]                 │
│                                                 │
│ ON-PAGE SEO            ██████░░░░  X/10         │
│ • Title tags:          [status]                 │
│ • Meta descriptions:   [status]                 │
│ • Heading-struktur:    [status]                 │
│ • Bilder (alt):        [status]                 │
│                                                 │
│ STRUKTURERT DATA       █████░░░░░  X/10         │
│ • Organization:        [status]                 │
│ • Article:             [status]                 │
│ • FAQPage:             [status]                 │
│ • BreadcrumbList:      [status]                 │
│                                                 │
│ AEO-READINESS          ███░░░░░░░  X/10         │
│ • AI-crawlere tillatt: [status]                 │
│ • llms.txt:            [status]                 │
│ • FAQ-struktur:        [status]                 │
│ • Answer blocks:       [status]                 │
│                                                 │
│ SOCIAL META            ████░░░░░░  X/10         │
│ • OG tags:             [status]                 │
│ • Twitter cards:       [status]                 │
│ • OG image:            [status]                 │
│                                                 │
├─────────────────────────────────────────────────┤
│ OVERALL SCORE:         ██████░░░░  XX/50        │
│                                                 │
│ 45+  = Utmerket                                 │
│ 35-44 = God                                     │
│ 25-34 = Trenger forbedring                      │
│ <25  = Kritisk                                  │
└─────────────────────────────────────────────────┘
```

---

## Steg 11: Prioriterte forbedringer

List opp konkrete forbedringer i prioritert rekkefølge:

### 🔴 Kritisk (fiks nå)

1. [Issue] - [Fil] - [Løsning]
2. ...

### 🟡 Høy prioritet (denne uken)

1. [Issue] - [Fil] - [Løsning]
2. ...

### 🟢 Medium prioritet (planlegg)

1. [Issue] - [Fil] - [Løsning]
2. ...

---

## Steg 12: Quick Wins

Identifiser og list 3-5 forbedringer som tar under 5 minutter hver:

1. [Quick win 1]
2. [Quick win 2]
3. [Quick win 3]

---

## Output format

Presenter resultatene i denne rekkefølgen:

1. **Prosjektoversikt** - Teknologi, struktur
2. **Scorecard** - Visuell oversikt
3. **Kritiske issues** - Må fikses
4. **Quick wins** - Raske forbedringer
5. **Detaljerte funn** - Per kategori
6. **Neste steg** - Anbefalt handlingsplan

---

## Eksempel på funn-format

### ❌ Kritisk: AI-crawlere blokkert

**Fil:** `/public/robots.txt`
**Problem:** GPTBot og ClaudeBot er blokkert med `Disallow: /`
**Impact:** Innhold vil ikke siteres i ChatGPT, Claude, etc.
**Løsning:**
```
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /
```

---

### ⚠️ Advarsel: Manglende FAQPage schema

**Problem:** FAQ-seksjon funnet, men ingen FAQPage schema
**Fil:** `/src/pages/faq.tsx`
**Impact:** Mister FAQ rich snippets i Google
**Løsning:** Legg til FAQPage JSON-LD (se STRUCTURED-DATA.md)

---

### ✅ OK: OG tags implementert

**Status:** Alle sider har og:title, og:description, og:image
**Merknad:** Vurder å legge til og:image:alt

---

## Notater

- Denne auditen sjekker kun koden, ikke live-performance
- For Core Web Vitals, bruk PageSpeed Insights
- For indekseringsstatus, sjekk Google Search Console
- For AI visibility, test manuelt i ChatGPT/Perplexity

---

## Relaterte ressurser

- `skills/seo-aeo/AUDIT-CHECKLIST.md` - Full manuell sjekkliste
- `skills/seo-aeo/TECHNICAL-SEO.md` - Teknisk SEO-dokumentasjon
- `skills/seo-aeo/AEO.md` - AEO-optimalisering
