---
name: content-strategy
description: Innholdsstrategi — pillar/cluster-arkitektur, searchable vs shareable, topic prioritering og innholdskalender. Aktiveres ved innholdsstrategi, content plan, pillar pages, topic clusters, innholdskalender, editorial plan eller «hva skal vi skrive om». For selve skrivingen, se content-writing. For distribusjon, se social-content.
---

# Innholdsstrategi

Du er en ekspert på innholdsstrategi. Målet er å planlegge innhold som bygger topic authority, driver organisk trafikk og konverterer besøkende — ikke bare å produsere artikler.

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Posisjonering, målgruppe, differensiatorer
2. **Les `./marketing/DISTRIBUTION.md`** — SEO-strategi, kanalplan
3. **Les `./marketing/JOURNEY.md`** — Kundereisefaser og innholdsbehov per fase

---

## Searchable vs. Shareable

Alt innhold faller i én av to kategorier:

| Type | Mål | Eksempler | Metrikk |
|------|-----|-----------|---------|
| **Searchable** | Organisk trafikk, SEO | Guider, sammenligninger, «how-to» | Rankings, organisk trafikk |
| **Shareable** | Synlighet, merkevare | Meningsinnhold, originale data, historier | Delinger, mentions, backlinks |

**Balanse:** 60% searchable / 40% shareable for de fleste virksomheter. Justér basert på modenhet:
- Ny virksomhet → 70/30 searchable (bygg grunnlag)
- Etablert → 50/50 (bygg merkevare)
- Markedsleder → 40/60 shareable (thought leadership)

---

## Pillar/Cluster-arkitektur

### Modellen

```
                    ┌──────────────┐
                    │  Pillar Page  │  (Bred oversikt, 2000+ ord)
                    │  /crm-guide/  │
                    └──────┬───────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
     ┌──────┴──────┐ ┌────┴────┐ ┌──────┴──────┐
     │ Cluster 1   │ │ Cluster 2│ │ Cluster 3   │
     │ /crm-for-   │ │ /crm-vs-│ │ /crm-       │
     │  smb/       │ │  excel/ │ │  implement/ │
     └─────────────┘ └─────────┘ └─────────────┘
```

### Pillar Page
- Bred oversikt av et kjernetema
- 2000–3000 ord, dekker alle hovedaspekter
- Lenker til alle cluster-artikler
- Oppdateres jevnlig

### Cluster-artikler
- Dykker dypt inn i ett spesifikt undertema
- 1000–2000 ord
- Lenker tilbake til pillar page + relevante clusters
- Targeting long-tail søkeord

### Intern lenking
- Pillar → alle clusters
- Cluster → pillar
- Cluster → relaterte clusters
- **Bruk beskrivende ankertekst**, ikke «les mer»

---

## Topic Prioritering

### 4-faktor vektet scoring

| Faktor | Vekt | Hvordan vurdere |
|--------|------|-----------------|
| **Søkevolum** | 25% | Antall månedlige søk (Ahrefs/DataForSEO) |
| **Difficulty** | 25% | KD-score vs. ditt domenes DR |
| **Intent-match** | 30% | Matcher søkerens intensjon ditt tilbud? |
| **Business value** | 20% | Hvor nær er søkeren et kjøp? |

**Scoring:** Gi 1–5 på hver faktor, multipliser med vekt. Summer. **25+** = skriv nå. **15–24** = backlog. **<15** = skip.

### Intent-match guide

| Søke-intent | Business value | Eksempel |
|-------------|---------------|----------|
| Informational | Lav | «Hva er CRM?» |
| Navigational | Medium | «[Merke] priser» |
| Commercial | Høy | «Beste CRM for SMB» |
| Transactional | Høyest | «[Merke] gratis prøve» |

---

## Buyer-stage Mapping

| Stage | Innholdstype | Mål |
|-------|-------------|-----|
| **Awareness** | Blogg, guider, lister | Fang oppmerksomhet, utdan |
| **Consideration** | Sammenligninger, case studies | Bygg tillit, vis verdi |
| **Decision** | Produktsider, demo, priser | Konverter |
| **Post-purchase** | Onboarding-guider, tips | Aktiver, behold |

**Sjekk JOURNEY.md** for prosjektspesifikk mapping.

---

## Innholdskalender-template

```markdown
## [Måned] — Innholdsplan

### Uke 1
- [ ] [Tittel] — [Type: searchable/shareable] — [Stage] — [Kanal]

### Uke 2
- [ ] [Tittel] — [Type] — [Stage] — [Kanal]

### Uke 3
- [ ] [Tittel] — [Type] — [Stage] — [Kanal]

### Uke 4
- [ ] [Tittel] — [Type] — [Stage] — [Kanal]

**Balanse denne måneden:** X% searchable / Y% shareable
**Stage-dekning:** Awareness: X | Consideration: X | Decision: X
```

---

## Content Audit-prosess

Når du reviderer eksisterende innhold:

### 1. Inventar
- List alt eksisterende innhold med URL, publiseringsdato, trafikk
- Kategoriser: searchable/shareable, buyer stage, cluster

### 2. Evaluer

| Handling | Kriterier |
|----------|----------|
| **Behold** | God trafikk, on-brand, oppdatert |
| **Oppdater** | God posisjon men utdatert, eller thin content som kan utdypes |
| **Konsolider** | Flere artikler om samme tema → slå sammen |
| **Fjern** | Irrelevant, feil, ingen trafikk, kannibaliserer |

### 3. Gap-analyse
- Sammenlign clusters med konkurrenter
- Identifiser buyer stages uten innhold
- Finn søkeord du rangerer 5–15 for (lavthengende frukt)

---

## Sjekkliste

- [ ] Pillar/cluster-struktur definert
- [ ] Topics scoret og prioritert
- [ ] Innholdskalender for neste 4 uker
- [ ] Searchable/shareable-balanse sjekket
- [ ] Alle buyer stages har innhold
- [ ] Intern lenking planlagt
- [ ] Oppdateringssyklus for eksisterende innhold

---

## Relaterte Skills

- `content-writing` — Selve skrivingen av innhold
- `seo-aeo` — Søkemotor- og AI-optimalisering
- `social-content` — Distribusjon på sosiale medier
- `programmatic-seo` — Skalerbar innholdsproduksjon
- `analytics-tracking` — Mål innholdsytelse
