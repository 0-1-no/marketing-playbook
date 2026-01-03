# Structured Data (Schema.org)

> **Metodikk-fil:** Dette er schema.org templates og prinsipper.
> Faktiske verdier (firmanavn, URLs, etc.) hentes fra den lokale kodebasen.
> Organisasjonsinfo kan dokumenteres i `./marketing/BRAND.md`.

Bruk denne filen når du implementerer strukturert data for rich snippets i Google og bedre AI-forståelse.

---

## Hva er strukturert data?

Strukturert data er et standardisert format (Schema.org) som hjelper søkemotorer og AI-systemer forstå innholdet på en side.

### Fordeler

| Fordel | Beskrivelse |
|--------|-------------|
| Rich snippets | FAQ, reviews, produktinfo i søkeresultater |
| AI-forståelse | LLM-er parser strukturert data bedre enn HTML |
| Knowledge Graph | Bidrar til Googles kunnskapsbase |
| Voice search | Strukturert data brukes i voice assistants |

---

## Format: JSON-LD

Google anbefaler JSON-LD. Plasseres i `<head>` eller `<body>`.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "SEO-guide for nybegynnere",
  "author": {
    "@type": "Person",
    "name": "Kenneth Dreyer"
  }
}
</script>
```

---

## Viktige Schema-typer

### 1. Organization

**Bruk på:** Hovedside / Om oss
**Rich snippet:** Logo, kontaktinfo i Knowledge Panel

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Norea AI",
  "url": "https://norea.ai",
  "logo": "https://norea.ai/logo.png",
  "description": "AI-drevet automatisering for norske bedrifter.",
  "foundingDate": "2023",
  "founders": [
    {
      "@type": "Person",
      "name": "Kenneth Dreyer"
    }
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "hei@norea.ai",
    "contactType": "customer service"
  },
  "sameAs": [
    "https://linkedin.com/company/norea-ai",
    "https://twitter.com/norea_ai"
  ]
}
```

---

### 2. Article / BlogPosting

**Bruk på:** Bloggposter, artikler
**Rich snippet:** Forfatter, dato, bilde

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Komplett SEO-guide for nybegynnere",
  "description": "Lær SEO fra bunnen med vår komplette guide.",
  "image": "https://example.com/seo-guide.jpg",
  "datePublished": "2025-01-03",
  "dateModified": "2025-01-03",
  "author": {
    "@type": "Person",
    "name": "Kenneth Dreyer",
    "url": "https://example.com/team/kenneth"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Norea AI",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/seo-guide/"
  }
}
```

---

### 3. FAQPage

**Bruk på:** FAQ-seksjoner, spørsmål-svar innhold
**Rich snippet:** Accordion med Q&A i søkeresultater
**AEO-verdi:** Høy - AI siterer FAQ-struktur ofte

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hva er SEO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SEO (Search Engine Optimization) er prosessen med å optimalisere nettsider for å rangere høyere i søkemotorer som Google. Dette inkluderer teknisk optimalisering, innholdsforbedring og lenkebygging."
      }
    },
    {
      "@type": "Question",
      "name": "Hvor lang tid tar det å se SEO-resultater?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Det tar vanligvis 3-6 måneder å se betydelige resultater fra SEO-arbeid. Tidsrammen avhenger av konkurranse, nettsidens alder og kvaliteten på optimaliseringen."
      }
    },
    {
      "@type": "Question",
      "name": "Trenger jeg SEO hvis jeg bruker betalt annonsering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, SEO og betalt annonsering utfyller hverandre. SEO gir langsiktig, kostnadseffektiv trafikk, mens betalt annonsering gir umiddelbare resultater. De fleste vellykkede bedrifter bruker begge."
      }
    }
  ]
}
```

---

### 4. HowTo

**Bruk på:** Guider, tutorials, oppskrifter
**Rich snippet:** Steg-for-steg i søkeresultater
**AEO-verdi:** Høy - AI elsker strukturerte instruksjoner

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Hvordan sette opp Google Search Console",
  "description": "En enkel guide til å verifisere og sette opp Google Search Console for nettstedet ditt.",
  "totalTime": "PT10M",
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "NOK",
    "value": "0"
  },
  "step": [
    {
      "@type": "HowToStep",
      "name": "Gå til Search Console",
      "text": "Åpne search.google.com/search-console og logg inn med Google-kontoen din.",
      "url": "https://example.com/guide#steg-1"
    },
    {
      "@type": "HowToStep",
      "name": "Legg til eiendom",
      "text": "Klikk på 'Legg til eiendom' og skriv inn nettadressen din.",
      "url": "https://example.com/guide#steg-2"
    },
    {
      "@type": "HowToStep",
      "name": "Verifiser eierskap",
      "text": "Velg verifiseringsmetode (DNS, HTML-fil eller meta-tag) og følg instruksjonene.",
      "url": "https://example.com/guide#steg-3"
    }
  ]
}
```

---

### 5. Product

**Bruk på:** Produktsider, e-commerce
**Rich snippet:** Pris, tilgjengelighet, vurderinger

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Norea CRM Pro",
  "image": "https://example.com/crm-pro.jpg",
  "description": "AI-drevet CRM for små og mellomstore bedrifter.",
  "brand": {
    "@type": "Brand",
    "name": "Norea"
  },
  "sku": "CRM-PRO-001",
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/produkter/crm-pro/",
    "priceCurrency": "NOK",
    "price": "499",
    "priceValidUntil": "2025-12-31",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "Norea AI"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "127"
  }
}
```

---

### 6. BreadcrumbList

**Bruk på:** Alle sider med hierarkisk navigasjon
**Rich snippet:** Breadcrumb-sti i søkeresultater

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Hjem",
      "item": "https://example.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Produkter",
      "item": "https://example.com/produkter/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "CRM Pro",
      "item": "https://example.com/produkter/crm-pro/"
    }
  ]
}
```

---

### 7. VideoObject

**Bruk på:** Sider med video
**Rich snippet:** Video-thumbnail, varighet i søkeresultater

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "SEO for nybegynnere - Komplett tutorial",
  "description": "Lær grunnleggende SEO på 15 minutter.",
  "thumbnailUrl": [
    "https://example.com/video-thumb-1x1.jpg",
    "https://example.com/video-thumb-4x3.jpg",
    "https://example.com/video-thumb-16x9.jpg"
  ],
  "uploadDate": "2025-01-03T08:00:00+01:00",
  "duration": "PT15M30S",
  "contentUrl": "https://example.com/videos/seo-tutorial.mp4",
  "embedUrl": "https://www.youtube.com/embed/xyz123",
  "interactionStatistic": {
    "@type": "InteractionCounter",
    "interactionType": { "@type": "WatchAction" },
    "userInteractionCount": 12500
  }
}
```

### Video med Key Moments (Clip)

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "SEO Tutorial",
  "hasPart": [
    {
      "@type": "Clip",
      "name": "Hva er SEO?",
      "startOffset": 0,
      "endOffset": 120,
      "url": "https://example.com/video#t=0"
    },
    {
      "@type": "Clip",
      "name": "Keyword research",
      "startOffset": 120,
      "endOffset": 300,
      "url": "https://example.com/video#t=120"
    },
    {
      "@type": "Clip",
      "name": "On-page optimalisering",
      "startOffset": 300,
      "endOffset": 600,
      "url": "https://example.com/video#t=300"
    }
  ]
}
```

---

### 8. Review / AggregateRating

**Bruk på:** Produkter, tjenester, programvare
**Rich snippet:** Stjerner i søkeresultater

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Norea CRM",
  "review": {
    "@type": "Review",
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": "5",
      "bestRating": "5"
    },
    "author": {
      "@type": "Person",
      "name": "Ola Nordmann"
    },
    "reviewBody": "Fantastisk CRM som har forenklet hele salgsprosessen vår."
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "127"
  }
}
```

---

### 9. LocalBusiness

**Bruk på:** Fysiske butikker, kontorer
**Rich snippet:** Kart, åpningstider, kontaktinfo

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Norea AI",
  "image": "https://example.com/kontor.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Storgata 1",
    "addressLocality": "Oslo",
    "postalCode": "0150",
    "addressCountry": "NO"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 59.9139,
    "longitude": 10.7522
  },
  "telephone": "+47 22 33 44 55",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "17:00"
    }
  ]
}
```

---

### 10. WebSite med SearchAction

**Bruk på:** Forsiden
**Rich snippet:** Søkeboks i Google

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Norea AI",
  "url": "https://norea.ai",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://norea.ai/sok?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

---

## Kombinere flere schemas

Du kan ha flere schema-typer på én side:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Norea AI",
      "url": "https://example.com"
    },
    {
      "@type": "WebPage",
      "@id": "https://example.com/seo-guide/#webpage",
      "url": "https://example.com/seo-guide/",
      "name": "SEO-guide for nybegynnere",
      "isPartOf": {
        "@id": "https://example.com/#website"
      }
    },
    {
      "@type": "Article",
      "@id": "https://example.com/seo-guide/#article",
      "mainEntityOfPage": {
        "@id": "https://example.com/seo-guide/#webpage"
      },
      "headline": "SEO-guide for nybegynnere",
      "author": {
        "@id": "https://example.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Hjem",
          "item": "https://example.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "SEO-guide",
          "item": "https://example.com/seo-guide/"
        }
      ]
    }
  ]
}
```

---

## Validering og testing

### Verktøy

| Verktøy | URL | Bruk |
|---------|-----|------|
| Rich Results Test | search.google.com/test/rich-results | Test om schema gir rich snippets |
| Schema Validator | validator.schema.org | Valider JSON-LD syntax |
| Google Search Console | search.google.com/search-console | Se faktiske rich results |

### Vanlige feil

| Feil | Løsning |
|------|---------|
| Manglende påkrevde felt | Sjekk schema.org dokumentasjon |
| Ugyldig JSON | Valider med jsonlint.com |
| URL-mismatch | URL i schema må matche canonical |
| Utdatert data | Hold priser, datoer oppdatert |
| Invisible markup | Schema må matche synlig innhold |

---

## AEO-optimalisering med Schema

Schema hjelper AI-systemer forstå innholdet:

### Høy AEO-verdi

| Schema type | AEO-verdi | Hvorfor |
|-------------|-----------|---------|
| FAQPage | Høy | Spørsmål-svar format AI elsker |
| HowTo | Høy | Strukturerte instruksjoner |
| Article med author | Høy | E-E-A-T signaler |
| Product med reviews | Medium | Konkrete data |
| Organization | Medium | Entitets-klarhet |

### Best practices for AEO

1. **Bruk FAQPage** på alle sider med Q&A-innhold
2. **Inkluder author** med credentials
3. **Hold data oppdatert** - dateModified er viktig
4. **Vær spesifikk** - jo mer data, jo bedre

---

## Sjekkliste

### Alle sider
- [ ] BreadcrumbList implementert
- [ ] WebPage eller spesifikk type

### Artikler/blogg
- [ ] Article eller BlogPosting
- [ ] author med navn og URL
- [ ] datePublished og dateModified
- [ ] publisher (Organization)

### Produktsider
- [ ] Product med offers
- [ ] Pris, valuta, tilgjengelighet
- [ ] aggregateRating hvis reviews finnes

### FAQ-innhold
- [ ] FAQPage med alle Q&As
- [ ] Svar er komplette og informative

### Forside
- [ ] Organization schema
- [ ] WebSite med SearchAction (valgfritt)

### Validering
- [ ] Rich Results Test passerer
- [ ] Ingen errors i Search Console
