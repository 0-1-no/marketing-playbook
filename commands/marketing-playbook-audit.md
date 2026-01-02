---
description: Full audit of project against BRAND.md. Scans landing pages, copy, meta tags, and marketing content.
allowed-tools: Read, Glob, Grep
---

# Marketing Playbook - Full Audit

Utfør en komplett gjennomgang av prosjektets marketing-innhold mot `BRAND.md`.

## Steg 1: Les BRAND.md

Finn og les `BRAND.md`. Hvis den ikke finnes, anbefal å kjøre `/marketing-playbook` først.

## Steg 2: Skann prosjektet

Søk etter relevante filer:

### Landing pages og UI
```
app/**/page.tsx
app/**/page.jsx
pages/**/*.tsx
pages/**/*.jsx
src/app/**/page.tsx
```

### Oversettelser/Copy
```
messages/**/*.json
locales/**/*.json
i18n/**/*.json
public/locales/**/*.json
```

### Meta og SEO
```
app/layout.tsx (metadata)
public/manifest.json
public/robots.txt
```

### Dokumentasjon
```
README.md
docs/**/*.md
*.md (rot-nivå)
```

### Marketing Assets
```
public/og-*.png
public/images/marketing/**
```

## Steg 3: Analyser hver kategori

### Landing Pages

For hver funnet page.tsx/jsx:
1. Les filen
2. Identifiser bruker-synlig tekst (headings, paragraphs, CTAs)
3. Sjekk mot ABC

Output:
```
📄 app/page.tsx (Landing page)

Funn:
- Heading: "[tekst]" ✅ On-brand
- CTA: "[tekst]" ⚠️ Bruker "enkel" - vurder alternativ

Score: 8/10
```

### Translations (i18n)

For messages/*.json:
1. Les JSON-struktur
2. Identifiser brukervendt tekst
3. Sjekk for "Words We Avoid"

Output:
```
📄 messages/nb-NO.json

Funn:
- 3 forekomster av "beste" (linje 45, 89, 122)
- Key message "finn leads basert på tech stack" mangler
- Tone of voice: Konsistent ✅

Score: 7/10
```

### Meta & SEO

Sjekk:
- Title tags
- Meta descriptions
- OG tags
- JSON-LD

Output:
```
📄 app/layout.tsx (Meta)

Funn:
- Title: "[tekst]" ✅
- Description: "[tekst]" ⚠️ Mangler key message
- OG Image: Finnes ✅

Score: 9/10
```

## Steg 4: "Words We Avoid" Scan

Kjør grep for alle ord i "Words We Avoid" listen:

```
Søker etter forbudte ord...

"beste": 5 funn
  - app/page.tsx:23
  - messages/nb-NO.json:45
  ...

"enkel": 2 funn
  - components/Hero.tsx:12
  ...
```

## Steg 5: Sammendrag

```
═══════════════════════════════════════════
        MARKETING PLAYBOOK AUDIT
═══════════════════════════════════════════

Prosjekt: [navn]
BRAND.md: [dato sist oppdatert]
Skannet: [antall] filer

═══════════════════════════════════════════

TOTAL SCORE: [X/10]

Per kategori:
- Landing pages: 8/10 (3 filer)
- Translations: 7/10 (2 filer)
- Meta/SEO: 9/10 (1 fil)
- Docs: N/A (ingen funnet)

═══════════════════════════════════════════

TOP 5 FORBEDRINGER:

1. [Mest kritisk]
2. [Nest mest kritisk]
3. ...

═══════════════════════════════════════════

FORBUDTE ORD FUNNET:

| Ord | Antall | Filer |
|-----|--------|-------|
| beste | 5 | page.tsx, nb-NO.json |
| ... | ... | ... |

═══════════════════════════════════════════

NESTE STEG:

- [ ] Fiks "Words We Avoid" funn
- [ ] Oppdater meta descriptions
- [ ] Legg til manglende key messages

Kjør `/marketing-playbook:check [fil]` for detaljer om spesifikke filer.
```

## Begrensninger

- Skann kun tekst-baserte filer
- Ignorer node_modules, .next, dist, build
- Fokuser på bruker-synlig innhold
