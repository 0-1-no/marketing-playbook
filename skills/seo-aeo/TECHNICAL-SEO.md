# Technical SEO

> **Metodikk-fil:** Dette er tekniske SEO-prinsipper og konfigurasjoner.
> Implementering gjøres i den lokale kodebasen (robots.txt, sitemap, etc.).
> Kanalstrategi dokumenteres i `./marketing/DISTRIBUTION.md`.

Bruk denne filen når du jobber med teknisk SEO-fundament: Core Web Vitals, crawlability, robots.txt, sitemap, og AI-crawler-konfigurasjon.

---

## Core Web Vitals

Google bruker Core Web Vitals som rangeringssignal. 75% av besøk må være i "god" kategori.

### Terskelverdier

| Metrikk | God | Trenger forbedring | Dårlig |
|---------|-----|-------------------|--------|
| **LCP** (Largest Contentful Paint) | ≤2.5s | 2.5-4s | >4s |
| **INP** (Interaction to Next Paint) | ≤200ms | 200-500ms | >500ms |
| **CLS** (Cumulative Layout Shift) | ≤0.1 | 0.1-0.25 | >0.25 |

### LCP-optimalisering

LCP måler hvor raskt hovedinnholdet lastes.

**Vanlige problemer og løsninger:**

| Problem | Løsning |
|---------|---------|
| Store bilder | Komprimer til WebP, maks 100KB for hero |
| Treg server (TTFB) | CDN, edge caching, optimalisert hosting |
| Render-blocking CSS/JS | Inline kritisk CSS, defer non-critical |
| Tredjepartsscripts | Lazy load eller async |

```html
<!-- Preload LCP-element -->
<link rel="preload" as="image" href="/hero.webp" fetchpriority="high">

<!-- Defer non-critical JS -->
<script defer src="/analytics.js"></script>

<!-- Inline kritisk CSS -->
<style>
  /* Critical above-fold styles */
</style>
```

### INP-optimalisering

INP måler responstid ved interaksjon (erstatter FID).

**Vanlige problemer og løsninger:**

| Problem | Løsning |
|---------|---------|
| Tung JavaScript | Code splitting, tree shaking |
| Lang main thread | Web Workers for tunge operasjoner |
| Blokkerende hydration | Progressive hydration, islands |
| Tredjepartsscripts | Async loading, lazy init |

```html
<!-- Async tredjepartsscripts -->
<script async src="https://third-party.com/script.js"></script>

<!-- Defer non-critical -->
<script defer src="/main.js"></script>
```

### CLS-optimalisering

CLS måler visuell stabilitet (uventede layout-endringer).

**Vanlige problemer og løsninger:**

| Problem | Løsning |
|---------|---------|
| Bilder uten dimensjoner | Alltid sett width/height |
| Dynamisk injisert innhold | Reserver plass på forhånd |
| Webfonts som laster | font-display: swap + preload |
| Annonser uten plass | Faste containere |

```html
<!-- Bilder med dimensjoner -->
<img
  src="/image.webp"
  width="800"
  height="600"
  style="aspect-ratio: 4/3;"
  alt="Beskrivelse"
>

<!-- Font preload -->
<link
  rel="preload"
  href="/fonts/main.woff2"
  as="font"
  type="font/woff2"
  crossorigin
>
```

---

## Mobile-First Indexing

Google bruker primært mobil-versjonen for indeksering og ranking.

### Krav

| Sjekk | Krav |
|-------|------|
| Responsivt design | Viewport meta tag, flytende layout |
| Samme innhold | Mobil og desktop har identisk innhold |
| Samme strukturert data | Schema markup på begge versjoner |
| Samme meta tags | title, description identiske |
| Touch targets | Minimum 48x48px |
| Font størrelse | Minimum 16px for lesbarhet |

```html
<!-- Viewport meta (påkrevd) -->
<meta name="viewport" content="width=device-width, initial-scale=1">
```

### Vanlige feil

- Skjuler innhold på mobil som er synlig på desktop
- Ulike canonical URLs mellom mobile/desktop
- Blokkerer ressurser i robots.txt som mobil trenger
- Lazy-loader bilder som aldri vises på mobil

---

## Hastighetsoptimalisering

### Bildeoptimalisering

```html
<!-- Optimal bildekode -->
<picture>
  <source srcset="/image.avif" type="image/avif">
  <source srcset="/image.webp" type="image/webp">
  <img
    src="/image.jpg"
    loading="lazy"
    decoding="async"
    width="800"
    height="600"
    alt="Beskrivende tekst"
  >
</picture>
```

| Format | Bruk | Støtte |
|--------|------|--------|
| AVIF | Beste komprimering, moderne browsers | Chrome, Firefox, Edge |
| WebP | God komprimering, bred støtte | 95%+ browsers |
| JPEG | Fallback | Alle browsers |

### Lazy Loading

```html
<!-- Native lazy loading (below fold) -->
<img src="/image.webp" loading="lazy" alt="...">

<!-- Eager loading (above fold / LCP) -->
<img src="/hero.webp" loading="eager" fetchpriority="high" alt="...">
```

**Regel:**
- `loading="eager"` + `fetchpriority="high"` for LCP-element
- `loading="lazy"` for alt below-fold

### Komprimering

| Ressurs | Teknikk |
|---------|---------|
| HTML | Minify, Gzip/Brotli |
| CSS | Minify, purge unused, Gzip/Brotli |
| JavaScript | Minify, tree-shake, code-split, Gzip/Brotli |
| Bilder | WebP/AVIF, responsive sizes, compression |
| Fonts | Subset, WOFF2 format, preload |

---

## HTTPS og HTTP/2

### HTTPS (påkrevd)

HTTPS er rangeringssignal og påkrevd for mange moderne features.

**Sjekkliste:**
- [ ] Gyldig SSL-sertifikat
- [ ] Ingen mixed content (HTTP-ressurser på HTTPS-side)
- [ ] HTTP → HTTPS redirect (301)
- [ ] HSTS header aktivert

```
# HSTS Header
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

### HTTP/2 og HTTP/3

HTTP/2 gir betydelig hastighetsøkning via multiplexing.

**Sjekk:**
```bash
curl -I --http2 https://example.com
# Skal returnere "HTTP/2 200"
```

---

## robots.txt

Plassering: `/robots.txt` på root.

### Grunnleggende struktur

```
# Søkemotorer
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Disallow: /private/

# Sitemap
Sitemap: https://example.com/sitemap.xml
```

### AI-crawler konfigurasjon

**KRITISK:** 68% av enterprise-sider blokkerer utilsiktet AI-crawlere. Sjekk dette!

```
# === AI CRAWLERE - TILLAT FOR AEO ===

# OpenAI (ChatGPT, SearchGPT)
User-agent: GPTBot
Allow: /

# Anthropic (Claude)
User-agent: ClaudeBot
Allow: /

# Perplexity
User-agent: PerplexityBot
Allow: /

# Google AI (Gemini, AI Overviews)
User-agent: Google-Extended
Allow: /

# Companybook
User-agent: CompanybookBot
Allow: /

# === SØKEMOTORER ===

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# === BLOKKERTE BOTS ===

User-agent: AhrefsBot
Disallow: /

User-agent: SemrushBot
Disallow: /
```

### User-Agent oversikt

| Bot | Eier | Formål | Anbefaling |
|-----|------|--------|------------|
| GPTBot | OpenAI | ChatGPT trening + søk | Allow |
| OAI-SearchBot | OpenAI | SearchGPT live-henting | Allow |
| ChatGPT-User | OpenAI | Bruker-triggede hentinger | Allow |
| ClaudeBot | Anthropic | Claude trening | Allow |
| Claude-User | Anthropic | Bruker-triggede hentinger | Allow |
| PerplexityBot | Perplexity | AI-søk indeksering | Allow |
| Google-Extended | Google | Gemini/AI Overviews | Allow |
| CompanybookBot | Companybook | B2B data | Allow |
| Googlebot | Google | Søk-indeksering | Allow |
| Bingbot | Microsoft | Søk-indeksering | Allow |

### Verifiser robots.txt

```bash
# Sjekk at filen er tilgjengelig
curl -I https://example.com/robots.txt

# Les innholdet
curl https://example.com/robots.txt
```

---

## XML Sitemap

Plassering: `/sitemap.xml` på root (eller referert i robots.txt).

### Struktur

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2025-01-03</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://example.com/produkter/</loc>
    <lastmod>2025-01-02</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

### Best practices

| Regel | Beskrivelse |
|-------|-------------|
| Kun kanoniske URLs | Ikke inkluder redirects, duplicates |
| Oppdatert lastmod | Faktisk endringsdato, ikke generert |
| Maks 50,000 URLs | Bruk sitemap index for større sider |
| Submit til Search Console | Og Bing Webmaster Tools |
| Dynamisk generering | Oppdater automatisk ved nye sider |

### Sitemap Index (for store sider)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://example.com/sitemap-pages.xml</loc>
    <lastmod>2025-01-03</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap-products.xml</loc>
    <lastmod>2025-01-03</lastmod>
  </sitemap>
</sitemapindex>
```

---

## Canonical Tags

Canonical forteller søkemotorer hvilken URL som er "originalen" ved duplisert innhold.

### Implementering

```html
<!-- Alltid self-referencing canonical -->
<link rel="canonical" href="https://example.com/side/">

<!-- Selv med parametere, pek til ren URL -->
<!-- På: example.com/produkter/?farge=rod&str=m -->
<link rel="canonical" href="https://example.com/produkter/">
```

### Regler

| Situasjon | Canonical |
|-----------|-----------|
| Parametervariasjoner | Pek til ren URL uten parametere |
| HTTP vs HTTPS | Alltid HTTPS |
| www vs non-www | Velg én, vær konsistent |
| Pagineringssider | Hver side sin egen canonical |
| Produktvarianter (farge) | Pek til hovedprodukt eller egen side |

### Vanlige feil

- Canonical til 404-side
- Canonical til redirect
- Inkonsistent www/non-www
- Canonical på noindex-sider
- Chain of canonicals (A→B→C)

---

## Redirects og feilhåndtering

### Redirect-typer

| Kode | Type | Bruk |
|------|------|------|
| 301 | Permanent | URL er flyttet for godt |
| 302 | Temporary | Midlertidig flytting |
| 307 | Temporary (strikt) | Bevar HTTP-metode |
| 308 | Permanent (strikt) | Bevar HTTP-metode |

**Regel:** Bruk 301 for permanente endringer. Det overfører link equity.

### Redirect-kjeder

**Unngå dette:**
```
A → B → C → D  (redirect chain)
```

**Gjør dette:**
```
A → D
B → D
C → D
```

### 404-håndtering

| Handling | Beskrivelse |
|----------|-------------|
| Custom 404-side | Hjelp brukeren videre |
| Soft 404-sjekk | Ikke returner 200 på 404-innhold |
| Logg 404-errors | Finn og fiks broken links |
| 410 for slettede sider | Eksplisitt "gone" |

---

## noindex og nofollow

### Meta robots

```html
<!-- Ikke indekser denne siden -->
<meta name="robots" content="noindex">

<!-- Ikke følg lenker på denne siden -->
<meta name="robots" content="nofollow">

<!-- Kombinert -->
<meta name="robots" content="noindex, nofollow">

<!-- Ingen snippet i søkeresultater -->
<meta name="robots" content="nosnippet">
```

### Bruksområder for noindex

| Sidetyper | Noindex? |
|-----------|----------|
| Admin-sider | Ja |
| Søkeresultatsider internt | Ja |
| Takk-for-bestilling | Ja |
| Filtervisninger (pagination) | Vurder (bruk canonical i stedet) |
| Vilkår og personvern | Nei (indekser) |
| Bloggposter | Nei (indekser) |

---

## Paginering

### Håndtering

**Anbefalt fremgangsmåte:**

```html
<!-- Side 1 -->
<link rel="canonical" href="https://example.com/blogg/">
<link rel="next" href="https://example.com/blogg/?page=2">

<!-- Side 2 -->
<link rel="canonical" href="https://example.com/blogg/?page=2">
<link rel="prev" href="https://example.com/blogg/">
<link rel="next" href="https://example.com/blogg/?page=3">

<!-- Siste side -->
<link rel="canonical" href="https://example.com/blogg/?page=10">
<link rel="prev" href="https://example.com/blogg/?page=9">
```

**Alternativ: Infinite scroll med progressiv URL-oppdatering**

---

## hreflang (flerspråklige sider)

For sider med flere språkversjoner.

```html
<!-- Norsk versjon -->
<link rel="alternate" hreflang="nb" href="https://example.com/">
<link rel="alternate" hreflang="en" href="https://example.com/en/">
<link rel="alternate" hreflang="x-default" href="https://example.com/">

<!-- Engelsk versjon -->
<link rel="alternate" hreflang="nb" href="https://example.com/">
<link rel="alternate" hreflang="en" href="https://example.com/en/">
<link rel="alternate" hreflang="x-default" href="https://example.com/">
```

### Regler

- Bidirectional: Alle språkversjoner må peke til hverandre
- x-default: Fallback for ukjente regioner
- Self-referencing: Inkluder seg selv i listen
- Konsistens: Samme hreflang på alle sider i gruppen

---

## llms.txt

Ny standard for å hjelpe AI-systemer forstå nettstedet ditt.

### Plassering og format

Fil: `/llms.txt` på root
Format: Markdown

### Eksempel

```markdown
# Example Company

> One-line description of what the company does.

## About
- [Company Overview](https://example.com/about): Core mission and history.
- [Team](https://example.com/team): Leadership and key people.

## Products
- [Main Product](https://example.com/products/main): Primary offering.
- [Pricing](https://example.com/pricing): Plans and pricing.

## Documentation
- [API Reference](https://example.com/docs/api): Technical documentation.
- [Guides](https://example.com/docs/guides): How-to guides.

## Blog
- [Latest Posts](https://example.com/blog): Industry insights and updates.
```

### Struktur

| Element | Format | Påkrevd |
|---------|--------|---------|
| H1 | `# Company Name` | Ja |
| Blockquote | `> One-liner` | Valgfritt |
| Seksjoner | `## Section Name` | Ja (minst 1) |
| Lenker | `- [Tittel](URL): Beskrivelse` | Ja i seksjoner |

### Fordeler

- AI-systemer parser raskere enn HTML
- Kuratert innhold fremfor crawling
- Prioritering av viktige sider
- Kontekst via beskrivelser

---

## Teknisk SEO-sjekkliste

### Crawlability
- [ ] robots.txt er tilgjengelig og korrekt
- [ ] AI-crawlere er tillatt (GPTBot, ClaudeBot, PerplexityBot, CompanybookBot)
- [ ] Sitemap.xml er oppdatert og submitted
- [ ] Ingen viktige sider blokkert
- [ ] Ingen redirect-kjeder over 2 hopp

### Indexability
- [ ] Viktige sider er indeksert (site:example.com)
- [ ] Canonical tags er korrekte
- [ ] Ingen utilsiktet noindex
- [ ] Duplicate content håndtert

### Performance
- [ ] LCP ≤2.5s
- [ ] INP ≤200ms
- [ ] CLS ≤0.1
- [ ] TTFB <600ms

### Security
- [ ] HTTPS aktiv
- [ ] Gyldig SSL-sertifikat
- [ ] Ingen mixed content
- [ ] HSTS aktivert

### Mobile
- [ ] Viewport meta tag
- [ ] Responsivt design
- [ ] Touch targets ≥48px
- [ ] Lesbar font (≥16px)

---

## Verktøy

| Verktøy | Bruk |
|---------|------|
| Google Search Console | Indeksering, crawl errors, performance |
| PageSpeed Insights | Core Web Vitals |
| Lighthouse | Teknisk audit |
| Screaming Frog | Crawl-analyse |
| web.dev/measure | Performance testing |
