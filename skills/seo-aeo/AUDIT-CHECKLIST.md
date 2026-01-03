# SEO & AEO Audit Checklist

> **Metodikk-fil:** Dette er en sjekkliste for SEO-audit.
> Auditen utføres på den lokale kodebasen, ikke på denne plugin-filen.
> Resultater og forbedringer implementeres i prosjektet du jobber med.

Bruk denne sjekklisten før lansering av nye sider eller ved regelmessig SEO-audit.

---

## Teknisk SEO (15 punkter)

### Crawlability
- [ ] **robots.txt** er tilgjengelig på /robots.txt
- [ ] **AI-crawlere tillatt** (GPTBot, ClaudeBot, PerplexityBot, CompanybookBot)
- [ ] **Sitemap.xml** finnes og er oppdatert
- [ ] **Sitemap submitted** til Google Search Console
- [ ] **Ingen viktige sider blokkert** i robots.txt

### Core Web Vitals
- [ ] **LCP ≤ 2.5s** (Largest Contentful Paint)
- [ ] **INP ≤ 200ms** (Interaction to Next Paint)
- [ ] **CLS ≤ 0.1** (Cumulative Layout Shift)

### Sikkerhet & Protokoll
- [ ] **HTTPS aktiv** på alle sider
- [ ] **Ingen mixed content** (HTTP-ressurser på HTTPS-side)
- [ ] **HSTS-header** aktivert (anbefalt)
- [ ] **HTTP/2 eller HTTP/3** støttet

### Redirects & Feil
- [ ] **Ingen redirect-kjeder** over 2 hopp
- [ ] **Ingen redirect-loops**
- [ ] **404-sider håndtert** med custom 404-side

---

## On-Page SEO (12 punkter)

### Title & Meta
- [ ] **Title tag** 50-60 tegn med keyword
- [ ] **Meta description** 150-160 tegn med CTA
- [ ] **Begge er unike** for denne siden

### Headings
- [ ] **Én H1 per side** med primary keyword
- [ ] **Logisk hierarki** (H1 → H2 → H3, ingen hopp)
- [ ] **H2s inkluderer** relevante søkeord

### URL
- [ ] **Kort og lesbar** URL
- [ ] **Inkluderer keyword**
- [ ] **Kun små bokstaver** og bindestreker

### Bilder
- [ ] **Alt-tekst på alle bilder** (5-10 ord, beskrivende)
- [ ] **WebP eller AVIF** format brukt
- [ ] **Bilder komprimert** (<100KB for hero, <50KB andre)
- [ ] **Width/height satt** for å unngå CLS

---

## Strukturert Data (8 punkter)

### Grunnleggende
- [ ] **JSON-LD format** brukt
- [ ] **Validerer uten feil** i Rich Results Test
- [ ] **BreadcrumbList** implementert

### Sidetype-spesifikk
- [ ] **Organization** schema på forside
- [ ] **Article/BlogPosting** på bloggposter
- [ ] **FAQPage** på sider med FAQ-innhold
- [ ] **Product** på produktsider (med pris, tilgjengelighet)
- [ ] **HowTo** på guider og tutorials

---

## AEO-Readiness (10 punkter)

### Teknisk for AI
- [ ] **robots.txt tillater** GPTBot, ClaudeBot, PerplexityBot, CompanybookBot
- [ ] **llms.txt** opprettet på root (valgfritt men anbefalt)
- [ ] **Ingen JavaScript-avhengig** kritisk innhold

### Innhold for AI
- [ ] **Klare definisjoner** i første 100 ord
- [ ] **Answer blocks** på 40-60 ord som kan siteres
- [ ] **FAQ-seksjon** med strukturert Q&A format
- [ ] **Kilder og data** med attribusjon

### Autoritet
- [ ] **Forfatter-bio** med credentials synlig
- [ ] **dateModified** oppdatert i schema
- [ ] **E-E-A-T signaler** tilstede (erfaring, ekspertise)

---

## Innhold (8 punkter)

### Kvalitet
- [ ] **Primary keyword definert** for siden
- [ ] **Keyword i første 100 ord**
- [ ] **Ingen keyword stuffing** (1-2% density)
- [ ] **Unikt innhold** (ikke duplikat)

### Lenker
- [ ] **3-5 interne lenker** med beskrivende ankertekst
- [ ] **1-2 eksterne lenker** til autoritative kilder
- [ ] **Ingen broken links**
- [ ] **Siden har lenker til seg** (ikke orphan)

---

## Social Meta (5 punkter)

- [ ] **og:title** satt og relevant
- [ ] **og:description** satt med verdi
- [ ] **og:image** 1200x630px, under 1MB
- [ ] **twitter:card** = summary_large_image
- [ ] **Testet i debugger** (Facebook, LinkedIn, Twitter)

---

## Tilgjengelighet (5 punkter)

- [ ] **Fargekontrast** WCAG AA (4.5:1 tekst, 3:1 stor tekst)
- [ ] **Alt-tekst** på alle meningsfulle bilder
- [ ] **Keyboard-navigerbar** (ingen mus påkrevd)
- [ ] **Skip link** til hovedinnhold
- [ ] **Form labels** på alle input-felt

---

## Quick Score Card

Bruk denne for rask vurdering:

```
┌─────────────────────────────────────────────────┐
│ SEO & AEO AUDIT SCORECARD                       │
├─────────────────────────────────────────────────┤
│                                                 │
│ TEKNISK SEO (15 punkter)                        │
│ Score: ___/15                                   │
│ ░░░░░░░░░░░░░░░                                 │
│                                                 │
│ ON-PAGE SEO (12 punkter)                        │
│ Score: ___/12                                   │
│ ░░░░░░░░░░░░                                    │
│                                                 │
│ STRUKTURERT DATA (8 punkter)                    │
│ Score: ___/8                                    │
│ ░░░░░░░░                                        │
│                                                 │
│ AEO-READINESS (10 punkter)                      │
│ Score: ___/10                                   │
│ ░░░░░░░░░░                                      │
│                                                 │
│ INNHOLD (8 punkter)                             │
│ Score: ___/8                                    │
│ ░░░░░░░░                                        │
│                                                 │
│ SOCIAL (5 punkter)                              │
│ Score: ___/5                                    │
│ ░░░░░                                           │
│                                                 │
│ TILGJENGELIGHET (5 punkter)                     │
│ Score: ___/5                                    │
│ ░░░░░                                           │
│                                                 │
├─────────────────────────────────────────────────┤
│ TOTAL: ___/63                                   │
│                                                 │
│ 55+ = Utmerket                                  │
│ 45-54 = God                                     │
│ 35-44 = Trenger forbedring                      │
│ <35 = Kritisk                                   │
└─────────────────────────────────────────────────┘
```

---

## Prioriteringsmatrise

### Kritisk (fiks umiddelbart)
| Problem | Impact | Effort |
|---------|--------|--------|
| robots.txt blokkerer viktige sider | Høy | Lav |
| Manglende HTTPS | Høy | Medium |
| LCP > 4s | Høy | Medium |
| Ingen H1 på side | Høy | Lav |
| Blokkerer AI-crawlere | Høy | Lav |

### Høy prioritet (fiks denne uken)
| Problem | Impact | Effort |
|---------|--------|--------|
| Manglende meta description | Medium | Lav |
| Core Web Vitals i gul sone | Medium | Medium |
| Ingen FAQ-schema | Medium | Lav |
| Alt-tekst mangler | Medium | Lav |

### Medium prioritet (planlegg)
| Problem | Impact | Effort |
|---------|--------|--------|
| Bilder ikke komprimert | Medium | Medium |
| Ingen llms.txt | Lav | Lav |
| Mangler OG-bilde | Lav | Lav |
| Intern lenking svak | Medium | Medium |

### Lav prioritet (nice-to-have)
| Problem | Impact | Effort |
|---------|--------|--------|
| Ikke HTTP/3 | Lav | Høy |
| Mangler author-bio | Lav | Lav |
| Ingen video-schema | Lav | Lav |

---

## Automatisert sjekk

For automatisert audit, kjør:

```
/seo-aeo:audit
```

Dette vil:
1. Scanne kodebasen for SEO-elementer
2. Sjekke robots.txt konfigurasjon
3. Validere strukturert data
4. Gi scorecard med prioriterte forbedringer

---

## Månedlig vedlikehold

### Hver måned
- [ ] Sjekk Search Console for crawl errors
- [ ] Verifiser Core Web Vitals-status
- [ ] Oppdater utdatert innhold
- [ ] Fiks nye broken links

### Hvert kvartal
- [ ] Full SEO-audit med denne sjekklisten
- [ ] Oppdater keyword-strategi
- [ ] Sjekk konkurrent-endringer
- [ ] AEO scorecard-oppdatering

### Årlig
- [ ] Forny årlige datoer i innhold ("2024" → "2025")
- [ ] Oppdater statistikk og data
- [ ] Vurder teknologi-oppgraderinger
