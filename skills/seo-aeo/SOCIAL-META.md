# Social Meta Tags

> **Metodikk-fil:** Dette er templates og spesifikasjoner for social meta.
> Faktiske verdier (titler, beskrivelser, bilder) skrives i den lokale kodebasen.
> Tone og merkevare hentes fra `./marketing/BRAND.md`.

Bruk denne filen når du implementerer Open Graph (Facebook, LinkedIn) og Twitter Cards for optimal deling på sosiale medier.

---

## Hvorfor social meta?

Når en URL deles på sosiale medier, vises en forhåndsvisning med bilde, tittel og beskrivelse. Uten riktige meta tags får du:

- Feil eller manglende bilde
- Avkuttet eller uklar tittel
- Generisk eller tom beskrivelse
- Dårligere CTR på delinger

---

## Open Graph (Facebook, LinkedIn)

Open Graph brukes av Facebook, LinkedIn, Pinterest, og mange andre plattformer.

### Påkrevde tags

```html
<meta property="og:title" content="SEO-guide for nybegynnere | Norea">
<meta property="og:description" content="Lær SEO fra bunnen. Komplett guide med sjekklister og maler.">
<meta property="og:image" content="https://example.com/images/seo-guide-og.jpg">
<meta property="og:url" content="https://example.com/seo-guide/">
<meta property="og:type" content="article">
```

### Anbefalte tags

```html
<!-- Site name -->
<meta property="og:site_name" content="Norea AI">

<!-- Locale -->
<meta property="og:locale" content="nb_NO">

<!-- Image dimensjoner -->
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Illustrasjon av SEO-konsepter">

<!-- For artikler -->
<meta property="article:published_time" content="2025-01-03T08:00:00+01:00">
<meta property="article:modified_time" content="2025-01-03T10:00:00+01:00">
<meta property="article:author" content="https://example.com/team/kenneth/">
<meta property="article:section" content="Marketing">
<meta property="article:tag" content="SEO">
<meta property="article:tag" content="Digital markedsføring">
```

### og:type verdier

| Type | Bruk |
|------|------|
| `website` | Forsider, generelle sider |
| `article` | Bloggposter, artikler |
| `product` | Produktsider |
| `profile` | Personsider |
| `video.other` | Videosider |

---

## Twitter Cards

Twitter (X) bruker egne tags, men faller tilbake til Open Graph hvis Twitter-tags mangler.

### Summary Card (standard)

For artikler og generelt innhold:

```html
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="SEO-guide for nybegynnere">
<meta name="twitter:description" content="Lær SEO fra bunnen. Komplett guide.">
<meta name="twitter:image" content="https://example.com/images/seo-guide.jpg">
```

### Summary Card with Large Image

For visuelt innhold, større bilde:

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="SEO-guide for nybegynnere">
<meta name="twitter:description" content="Lær SEO fra bunnen. Komplett guide.">
<meta name="twitter:image" content="https://example.com/images/seo-guide-large.jpg">
<meta name="twitter:image:alt" content="SEO-guide infografikk">
```

### Tilleggsinfo

```html
<!-- Twitter-konto for siden -->
<meta name="twitter:site" content="@norea_ai">

<!-- Forfatterens Twitter-konto -->
<meta name="twitter:creator" content="@kennethdreyer">
```

---

## Bildespesifikasjoner

### Anbefalte dimensjoner

| Plattform | Optimal størrelse | Min. størrelse | Aspekt |
|-----------|-------------------|----------------|--------|
| Facebook | 1200 × 630 | 600 × 315 | 1.91:1 |
| LinkedIn | 1200 × 627 | 1200 × 627 | 1.91:1 |
| Twitter (large) | 1200 × 628 | 300 × 157 | 2:1 |
| Twitter (summary) | 144 × 144 | 144 × 144 | 1:1 |
| Pinterest | 1000 × 1500 | 600 × 900 | 2:3 |

### Universell anbefaling

**Bruk 1200 × 630 px** for de fleste bruksområder. Dette fungerer på alle plattformer.

### Bildeformat

| Format | Anbefaling |
|--------|------------|
| JPEG | Standard for foto |
| PNG | For grafikk med tekst |
| WebP | Støttes ikke alle steder |
| GIF | Kun for animasjon |

**Filstørrelse:** Maks 8MB, ideelt under 1MB.

### Bilde-innhold

| Gjør | Unngå |
|------|-------|
| Tydelig tittel/tekst | For mye tekst |
| Merkevarefarger | Generiske stockbilder |
| Ansikter (øker engagement) | Bilde uten kontekst |
| Call-to-action | Avkuttet viktig innhold |

---

## Komplett eksempel

```html
<!DOCTYPE html>
<html lang="nb">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Primære meta -->
  <title>SEO-guide for nybegynnere - Lær å ranke i Google | Norea</title>
  <meta name="description" content="Lær SEO fra bunnen med vår komplette guide. Inkluderer sjekklister, eksempler og maler. Start gratis.">
  <link rel="canonical" href="https://norea.ai/blogg/seo-guide/">

  <!-- Open Graph / Facebook / LinkedIn -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://norea.ai/blogg/seo-guide/">
  <meta property="og:title" content="SEO-guide for nybegynnere - Lær å ranke i Google">
  <meta property="og:description" content="Lær SEO fra bunnen med vår komplette guide. Inkluderer sjekklister, eksempler og maler.">
  <meta property="og:image" content="https://norea.ai/images/seo-guide-og.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="SEO-guide illustrasjon med søkemotor-ikoner">
  <meta property="og:site_name" content="Norea AI">
  <meta property="og:locale" content="nb_NO">

  <!-- Article-spesifikk -->
  <meta property="article:published_time" content="2025-01-03T08:00:00+01:00">
  <meta property="article:author" content="https://norea.ai/team/kenneth/">
  <meta property="article:section" content="Marketing">
  <meta property="article:tag" content="SEO">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@norea_ai">
  <meta name="twitter:creator" content="@kennethdreyer">
  <meta name="twitter:title" content="SEO-guide for nybegynnere - Lær å ranke i Google">
  <meta name="twitter:description" content="Lær SEO fra bunnen med vår komplette guide. Inkluderer sjekklister.">
  <meta name="twitter:image" content="https://norea.ai/images/seo-guide-og.jpg">
  <meta name="twitter:image:alt" content="SEO-guide illustrasjon">
</head>
<body>
  <!-- Innhold -->
</body>
</html>
```

---

## Dynamisk generering

### Next.js / React

```tsx
// app/blogg/[slug]/page.tsx
import { Metadata } from 'next'

export async function generateMetadata({ params }): Promise<Metadata> {
  const post = await getPost(params.slug)

  return {
    title: post.title,
    description: post.excerpt,
    openGraph: {
      title: post.title,
      description: post.excerpt,
      url: `https://example.com/blogg/${params.slug}`,
      siteName: 'Norea AI',
      images: [
        {
          url: post.ogImage,
          width: 1200,
          height: 630,
          alt: post.title,
        },
      ],
      locale: 'nb_NO',
      type: 'article',
      publishedTime: post.publishedAt,
      authors: [post.author.name],
    },
    twitter: {
      card: 'summary_large_image',
      title: post.title,
      description: post.excerpt,
      images: [post.ogImage],
    },
  }
}
```

### HTML template (statisk)

```html
<!-- Erstatt variabler med faktiske verdier -->
<meta property="og:title" content="{{title}}">
<meta property="og:description" content="{{description}}">
<meta property="og:image" content="{{siteUrl}}/images/{{slug}}-og.jpg">
<meta property="og:url" content="{{siteUrl}}/{{slug}}/">
```

---

## Testing og debugging

### Verktøy

| Plattform | Debugger URL |
|-----------|--------------|
| Facebook | developers.facebook.com/tools/debug/ |
| LinkedIn | linkedin.com/post-inspector/ |
| Twitter | cards-dev.twitter.com/validator |

### Vanlige problemer

| Problem | Årsak | Løsning |
|---------|-------|---------|
| Gammelt bilde vises | Cache | Bruk Facebook Debugger "Scrape Again" |
| Bilde kuttes | Feil dimensjoner | Bruk 1200x630 |
| Beskrivelse mangler | Tag mangler | Legg til og test |
| Feil bilde | Ikke absolutt URL | Bruk full URL med https:// |

### Cache-busting

Når du oppdaterer OG-bilde:

1. **Facebook:** Bruk debugger, klikk "Scrape Again"
2. **LinkedIn:** Legg til ?v=2 på bilde-URL midlertidig
3. **Twitter:** Vent, eller bruk validator

---

## Sjekkliste

### Alle sider
- [ ] `og:title` - Unik, engasjerende
- [ ] `og:description` - Komplett, med CTA
- [ ] `og:image` - 1200x630, under 1MB
- [ ] `og:url` - Canonical URL
- [ ] `og:type` - Riktig type

### For delingsoptimalisering
- [ ] `og:image:alt` - Beskrivende alt-tekst
- [ ] `twitter:card` - summary_large_image for viktige sider
- [ ] Testet i debuggere

### Før lansering
- [ ] Alle URLs er absolutte (https://...)
- [ ] Bilder er publisert og tilgjengelige
- [ ] Ingen Lorem Ipsum i tags
