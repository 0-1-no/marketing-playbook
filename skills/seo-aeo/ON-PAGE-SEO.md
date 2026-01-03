# On-Page SEO

> **Metodikk-fil:** Dette er prinsipper for on-page optimalisering.
> Faktiske verdier (titler, beskrivelser) skrives i den lokale kodebasen.
> Tone og ordvalg hentes fra `./marketing/BRAND.md`.

Bruk denne filen når du optimaliserer innhold på en side: title tags, meta descriptions, headings, bilder, URLs og tilgjengelighet.

---

## Title Tag

Title tag er det viktigste on-page elementet for SEO og CTR.

### Spesifikasjoner

| Aspekt | Anbefaling |
|--------|------------|
| Lengde | 50-60 tegn (maks ~580px) |
| Keyword | I første 40 tegn |
| Struktur | [Keyword] + [Benefit] \| [Brand] |
| Unikhet | Hver side må ha unik title |

### Formater som fungerer

```
[Primært søkeord] - [Fordel/utfall] | [Merkenavn]
[Tall] [Adjektiv] [Søkeord] for [Målgruppe] (2025)
Hvordan [Handling] - [Resultat] | [Merkenavn]
[Søkeord] vs [Alternativ]: Hvilken er best?
```

### Eksempler

**Godt:**
```html
<title>SEO-guide for nybegynnere - Lær å ranke i Google | Norea</title>
<!-- 58 tegn, keyword først, benefit, brand -->

<title>15 beste CRM-systemer for små bedrifter (2025)</title>
<!-- 48 tegn, tall, keyword, målgruppe, år -->
```

**Dårlig:**
```html
<title>Velkommen til vår nettside</title>
<!-- Ingen keyword, ingen verdi -->

<title>CRM CRM-system CRM-løsning beste CRM gratis CRM</title>
<!-- Keyword stuffing -->

<title>Les vår fantastiske guide om de mange fordelene ved å bruke moderne CRM-systemer for din bedrift i dag</title>
<!-- For langt, 105 tegn -->
```

### CTR-optimalisering

| Teknikk | Eksempel |
|---------|----------|
| Tall | "7 måter...", "15 beste..." |
| År | "(2025)", "[Oppdatert 2025]" |
| Power words | "Ultimate", "Komplett", "Gratis" |
| Spørsmål | "Hvordan...", "Hva er..." |
| Brackets | "[Guide]", "(Gratis mal)" |

---

## Meta Description

Meta description påvirker CTR, ikke ranking direkte. Det er salgsargumentet ditt i SERP.

### Spesifikasjoner

| Aspekt | Anbefaling |
|--------|------------|
| Lengde | 150-160 tegn |
| Keyword | Inkluder naturlig (blir boldet) |
| CTA | Avslutt med handling |
| Unikhet | Hver side må ha unik description |

### Struktur

```
[Hva siden handler om] + [Unik verdi/fordel] + [CTA]
```

### Eksempler

**Godt:**
```html
<meta name="description" content="Lær SEO fra bunnen med vår komplette guide for nybegynnere. Inkluderer sjekklister, eksempler og maler. Start gratis i dag.">
<!-- 147 tegn, keyword, fordel, CTA -->
```

**Dårlig:**
```html
<meta name="description" content="Vi er et selskap som tilbyr tjenester.">
<!-- For kort, ingen verdi, ingen keyword -->

<meta name="description" content="SEO SEO-guide SEO-tips SEO-hjelp SEO-ekspert SEO-byrå">
<!-- Keyword stuffing, ingen mening -->
```

### CTA-eksempler

- "Les mer og kom i gang i dag."
- "Få gratis tilgang nå."
- "Sammenlign og velg riktig løsning."
- "Last ned malen gratis."
- "Se priser og bestill demo."

---

## Heading-struktur

Headings (H1-H6) strukturerer innholdet og signaliserer viktighet til søkemotorer.

### Regler

| Regel | Beskrivelse |
|-------|-------------|
| Én H1 per side | Hovedtittel, inkluder primær keyword |
| Hierarki | H1 → H2 → H3 (ikke hopp over nivåer) |
| Keywords i H2 | Sekundære søkeord i underseksjoner |
| Beskrivende | Headings skal gi mening isolert |

### Eksempel på god struktur

```html
<h1>Komplett SEO-guide for nybegynnere</h1>

  <h2>Hva er SEO?</h2>
    <h3>On-page SEO</h3>
    <h3>Off-page SEO</h3>
    <h3>Teknisk SEO</h3>

  <h2>Hvordan komme i gang med SEO</h2>
    <h3>Steg 1: Keyword research</h3>
    <h3>Steg 2: Optimaliser innhold</h3>
    <h3>Steg 3: Bygg lenker</h3>

  <h2>Vanlige SEO-feil å unngå</h2>

  <h2>Oppsummering</h2>
```

### Vanlige feil

| Feil | Problem |
|------|---------|
| Flere H1 | Forvirrer søkemotorer |
| H1 → H3 (hopper H2) | Bryter hierarki |
| Styling-headings | Bruk CSS, ikke H-tags for styling |
| Keyword stuffing i headings | Unaturlig, skader UX |

---

## URL-struktur

Gode URLs er lesbare, korte og keyword-rike.

### Regler

| Regel | Anbefaling |
|-------|------------|
| Lengde | Maks 60-75 tegn |
| Format | Små bokstaver, bindestrek som separator |
| Keywords | Inkluder primær keyword |
| Lesbarhet | Brukeren skal forstå innholdet fra URL |

### Eksempler

**Godt:**
```
/seo-guide-nybegynnere/
/produkter/crm-system/
/blogg/email-marketing-tips/
```

**Dårlig:**
```
/page?id=12345&cat=7
/produkter/kat1/subkat2/item999/variant-a/
/Dette-Er-En-Veldig-Lang-URL-Som-Inneholder-Alt-For-Mange-Ord
```

### URL-endringer

Ved URL-endringer:
1. Implementer 301 redirect fra gammel til ny
2. Oppdater interne lenker
3. Oppdater sitemap
4. Overvåk i Search Console

---

## Bildeoptimalisering

Bilder påvirker hastighet, tilgjengelighet og kan ranke i bildesøk.

### Format-valg

| Format | Bruk | Komprimering |
|--------|------|--------------|
| WebP | Standard for web | 25-35% mindre enn JPEG |
| AVIF | Moderne browsers | 50% mindre enn JPEG |
| JPEG | Fallback | Baseline |
| PNG | Transparens nødvendig | Bruk WebP i stedet |
| SVG | Ikoner, logoer | Vektor, skalerbar |

### Størrelsesanbefalinger

| Bildetype | Maks filstørrelse | Maks dimensjon |
|-----------|-------------------|----------------|
| Hero/Banner | 100KB | 1920px bredde |
| Artikkelbilder | 50KB | 1200px bredde |
| Thumbnails | 20KB | 400px bredde |
| Ikoner | 5KB | 64px |

### Alt-tekst

Alt-tekst er kritisk for tilgjengelighet og bilde-SEO.

**Regler:**
- 5-10 ord, beskrivende
- Inkluder keyword naturlig (ikke stuff)
- Beskriv hva bildet viser
- Ingen "Bilde av..." prefix

**Eksempler:**

```html
<!-- Godt -->
<img src="/team.webp" alt="Norea-teamet jobber sammen på kontoret i Oslo">

<!-- Dårlig -->
<img src="/team.webp" alt="bilde foto team mennesker kontor arbeid">

<!-- Også dårlig -->
<img src="/team.webp" alt="">
```

### Komplett bildekode

```html
<picture>
  <source
    srcset="/hero-800.avif 800w, /hero-1200.avif 1200w, /hero-1920.avif 1920w"
    type="image/avif"
    sizes="100vw"
  >
  <source
    srcset="/hero-800.webp 800w, /hero-1200.webp 1200w, /hero-1920.webp 1920w"
    type="image/webp"
    sizes="100vw"
  >
  <img
    src="/hero-1200.jpg"
    alt="Beskrivende alt-tekst med keyword"
    width="1920"
    height="1080"
    loading="eager"
    fetchpriority="high"
    decoding="async"
  >
</picture>
```

### Bildekomprimering

| Verktøy | Type |
|---------|------|
| Squoosh (app.squoosh.com) | Manuell, god kontroll |
| Sharp (Node.js) | Programmatisk |
| Next.js Image | Automatisk |
| Cloudinary | CDN med transformasjon |

---

## Breadcrumbs

Breadcrumbs hjelper navigasjon og kan vises i søkeresultater.

### Implementering

```html
<nav aria-label="Breadcrumb">
  <ol itemscope itemtype="https://schema.org/BreadcrumbList">
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/">
        <span itemprop="name">Hjem</span>
      </a>
      <meta itemprop="position" content="1">
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/produkter/">
        <span itemprop="name">Produkter</span>
      </a>
      <meta itemprop="position" content="2">
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <span itemprop="name">CRM-system</span>
      <meta itemprop="position" content="3">
    </li>
  </ol>
</nav>
```

Se [STRUCTURED-DATA.md](STRUCTURED-DATA.md) for JSON-LD versjon.

---

## Tilgjengelighet (a11y)

10-20% av befolkningen har funksjonshemninger. God tilgjengelighet = bedre SEO.

### WCAG AA-krav

| Krav | Spesifikasjon |
|------|---------------|
| Fargekontrast | 4.5:1 for vanlig tekst, 3:1 for stor tekst |
| Fokusindikatorer | Synlig focus state |
| Alt-tekst | Alle bilder med innhold |
| Keyboard-navigasjon | Alt fungerer uten mus |
| Skip links | Hopp til hovedinnhold |
| Form labels | Alle input-felt har labels |
| Heading-hierarki | Logisk rekkefølge |

### Kontrast-sjekk

```css
/* Minimum 4.5:1 for vanlig tekst */
color: #1a1a1a; /* på hvit bakgrunn = 12.6:1 ✓ */

/* Minimum 3:1 for stor tekst (18px+ eller 14px bold) */
color: #666666; /* på hvit bakgrunn = 5.7:1 ✓ */
```

### Skip link

```html
<a href="#main" class="skip-link">Hopp til hovedinnhold</a>

<style>
.skip-link {
  position: absolute;
  left: -9999px;
}
.skip-link:focus {
  position: static;
}
</style>
```

### Verktøy

| Verktøy | Bruk |
|---------|------|
| axe DevTools | Chrome extension |
| WAVE | Web accessibility evaluator |
| Lighthouse | Audit i Chrome DevTools |
| WebAIM Contrast Checker | Kontrast-testing |

---

## Intern lenking

Interne lenker distribuerer "link equity" og hjelper crawling.

### Regler

| Regel | Beskrivelse |
|-------|-------------|
| 3-5 interne lenker per side | Minimum for viktige sider |
| Beskrivende ankertekst | "Les SEO-guiden", ikke "klikk her" |
| Relevans | Lenk til relatert innhold |
| Kontekstuell plassering | I brødtekst, ikke bare footer |
| Ingen broken links | Regelmessig sjekk |

### Ankertekst

**Godt:**
```html
<a href="/seo-guide/">Les vår komplette SEO-guide for nybegynnere</a>
```

**Dårlig:**
```html
<a href="/seo-guide/">Klikk her</a>
<a href="/seo-guide/">Les mer</a>
```

### Pillar/Cluster-modell

```
                    ┌─────────────────┐
                    │   Pillar Page   │
                    │ (Hovedtema SEO) │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────▼────┐         ┌────▼────┐         ┌────▼────┐
    │ Cluster │         │ Cluster │         │ Cluster │
    │On-page  │         │Technical│         │ Lenke-  │
    │  SEO    │         │   SEO   │         │building │
    └─────────┘         └─────────┘         └─────────┘
```

Cluster-artikler lenker til Pillar, Pillar lenker til clusters.

---

## On-Page SEO Sjekkliste

### Title & Meta
- [ ] Title tag 50-60 tegn med keyword først
- [ ] Meta description 150-160 tegn med CTA
- [ ] Begge er unike for denne siden

### Headings
- [ ] Én H1 per side med primary keyword
- [ ] H2s dekker hovedseksjoner
- [ ] Logisk hierarki (ingen hopp)

### Innhold
- [ ] Keyword i første 100 ord
- [ ] 3-5 interne lenker
- [ ] 1-2 eksterne lenker til autoriteter
- [ ] Lesbar, scanbar tekst

### Bilder
- [ ] Alle bilder har beskrivende alt-tekst
- [ ] WebP-format (eller AVIF med fallback)
- [ ] Komprimert under 100KB
- [ ] Width/height attributter satt
- [ ] Lazy loading på below-fold bilder

### URL
- [ ] Kort, lesbar URL
- [ ] Inneholder keyword
- [ ] Kun små bokstaver og bindestreker

### Tilgjengelighet
- [ ] WCAG AA kontrast
- [ ] Keyboard-navigerbar
- [ ] Skip link til main
- [ ] Form labels på alle inputs

---

## Vanlige feil

| Feil | Konsekvens | Løsning |
|------|------------|---------|
| Duplikat titles | Forvirrer Google | Unik title per side |
| Manglende alt-tekst | Dårlig a11y + bilde-SEO | Beskriv alle bilder |
| Keyword stuffing | Penalty-risiko | Skriv naturlig |
| Tynne sider | Lav ranking | Utvid eller konsolider |
| Broken links | Dårlig UX + crawl waste | Regelmessig sjekk |
| Manglende H1 | Uklar sidestruktur | Én H1 på toppen |
| Store bilder | Treg side | Komprimer til <100KB |
