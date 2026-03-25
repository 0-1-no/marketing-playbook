---
name: schema-markup
description: JSON-LD strukturert data — schema-typer, rich results, validering og CMS-spesifikke patterns. Aktiveres ved schema, JSON-LD, structured data, rich results, rich snippets, schema.org eller «legg til strukturert data». For bredere SEO, se seo-aeo. For nettstedsstruktur, se site-architecture.
---

# Schema Markup (Strukturert Data)

Du er en ekspert på strukturert data og JSON-LD. Målet er å implementere korrekt schema markup som gir rich results i Google og gjør innhold maskinlesbart for AI.

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Bedriftsnavn, type, posisjonering
2. **Les `./marketing/DISTRIBUTION.md`** — Hvilke sider trenger schema?

---

## Schema-typer etter prioritet

### 1. Organization (alle nettsider)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Firmanavn",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": [
    "https://linkedin.com/company/firmanavn",
    "https://twitter.com/firmanavn"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "hei@example.com",
    "contactType": "customer service"
  }
}
```

### 2. WebSite + SearchAction (hjemmeside)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Firmanavn",
  "url": "https://example.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://example.com/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

### 3. Article / BlogPosting (artikler)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Artikkeltittel",
  "author": {
    "@type": "Person",
    "name": "Forfatternavn",
    "url": "https://example.com/team/navn"
  },
  "datePublished": "2025-01-15",
  "dateModified": "2025-03-20",
  "publisher": {
    "@type": "Organization",
    "name": "Firmanavn"
  },
  "image": "https://example.com/images/artikkel.jpg"
}
```

### 4. FAQPage (FAQ-seksjoner)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Spørsmål her?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Svar her."
      }
    }
  ]
}
```

**Rich result:** FAQ-dropdown i Google SERP. Også verdifullt for AEO.

### 5. HowTo (steg-for-steg guider)

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Hvordan sette opp CRM",
  "step": [
    {"@type": "HowToStep", "name": "Opprett konto", "text": "Gå til..."},
    {"@type": "HowToStep", "name": "Importer data", "text": "Last opp..."}
  ]
}
```

### 6. Product (produktsider)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Produktnavn",
  "description": "Kort beskrivelse",
  "offers": {
    "@type": "Offer",
    "price": "199",
    "priceCurrency": "NOK",
    "availability": "https://schema.org/InStock"
  }
}
```

### 7. SoftwareApplication (SaaS)

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "AppNavn",
  "operatingSystem": "Web",
  "applicationCategory": "BusinessApplication",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "NOK"
  }
}
```

### 8. BreadcrumbList (alle sider med dybde)

Se `site-architecture` for implementering.

### 9. Review / AggregateRating

```json
{
  "@type": "AggregateRating",
  "ratingValue": "4.8",
  "reviewCount": "127",
  "bestRating": "5"
}
```

### 10. LocalBusiness (fysiske lokasjoner)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Firmanavn Oslo",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Gatenavn 1",
    "addressLocality": "Oslo",
    "postalCode": "0123",
    "addressCountry": "NO"
  }
}
```

---

## CMS-spesifikke Patterns

### Next.js (App Router)

Bruk Next.js Metadata API med `generateMetadata` og JSON-LD via `<script>` i layout:

```tsx
// app/layout.tsx — bruk Next.js metadata export
import { Metadata } from 'next'

export const metadata: Metadata = {
  // standard metadata her
}

// For JSON-LD, bruk en utility-komponent
function JsonLd({ data }: { data: Record<string, unknown> }) {
  return (
    <script
      type="application/ld+json"
      // Next.js saniterer innhold i script-tags automatisk
      children={JSON.stringify(data)}
    />
  )
}
```

### Nuxt 3

```vue
<script setup>
useHead({
  script: [{
    type: 'application/ld+json',
    innerHTML: JSON.stringify({
      "@context": "https://schema.org",
      "@type": "Article",
      headline: article.title
    })
  }]
})
</script>
```

### SvelteKit

```svelte
<svelte:head>
  <script type="application/ld+json">
    {JSON.stringify({
      "@context": "https://schema.org",
      "@type": "Article",
      headline: data.title
    })}
  </script>
</svelte:head>
```

---

## Validering

### Pipeline

1. **Utvikle:** Legg til schema i kode
2. **Validere:** Google Rich Results Test (search.google.com/test/rich-results)
3. **Sjekke:** Schema Markup Validator (validator.schema.org)
4. **Deploy:** Push til produksjon
5. **Monitore:** Google Search Console → Forbedringer

### Vanlige feil

| Feil | Løsning |
|------|---------|
| Missing required field | Sjekk required properties for schema-typen |
| Invalid URL format | Bruk absolutte URLer |
| dateModified eldre enn datePublished | Oppdater dateModified |
| Duplicate schema | Fjern dupliserte script-tags |

---

## Sjekkliste

- [ ] Organization schema på alle sider
- [ ] Article/BlogPosting på artikler
- [ ] FAQPage på FAQ-seksjoner
- [ ] BreadcrumbList på sider med dybde
- [ ] Product/SoftwareApplication på produktsider
- [ ] Validert med Google Rich Results Test
- [ ] Ingen feil i Search Console → Forbedringer

---

## Relaterte Skills

- `seo-aeo` — SEO og AI-synlighet
- `site-architecture` — URL-struktur og navigasjon
- `ai-seo` — AI-optimalisering (schema er kritisk for AI)
- `analytics-tracking` — Mål rich result-klikk
