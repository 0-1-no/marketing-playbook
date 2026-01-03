# Content SEO

> **Metodikk-fil:** Dette er prinsipper for søkeordstrategi og intern lenking.
> Faktiske søkeord og innholdsplan dokumenteres i `./marketing/DISTRIBUTION.md`.
> Posisjonering og tone hentes fra `./marketing/BRAND.md`.

Bruk denne filen når du planlegger innholdsstrategi, søkeordanalyse, intern lenking og topical authority.

---

## Søkeordanalyse

### Search Intent

Alle søk har en underliggende intent. Match innhold til intent.

| Intent | Trigger-ord | Innholdstype | Eksempel |
|--------|-------------|--------------|----------|
| **Informational** | Hva, hvorfor, hvordan, guide | Blog, guide, tutorial | "Hva er SEO" |
| **Navigational** | [merkenavn], logg inn | Forside, innlogging | "Norea login" |
| **Commercial** | Beste, anmeldelse, vs | Sammenligning, review | "Beste CRM 2025" |
| **Transactional** | Kjøp, pris, bestill | Produktside, prising | "Norea CRM pris" |

### Søkeordsprioritering

| Faktor | Vekt | Hvorfor |
|--------|------|---------|
| Search volume | Høy | Trafikk-potensial |
| Konkurranse | Medium | Realistisk ranking |
| Relevans | Kritisk | Må matche tilbud |
| Intent-match | Kritisk | Må matche innhold |
| Conversion potential | Høy | ROI |

### Søkeordskategorier

```
┌─────────────────────────────────────────────────────────────┐
│ HEAD TERMS (1-2 ord)                                        │
│ Høyt volum, høy konkurranse                                │
│ Eksempel: "CRM", "SEO"                                      │
├─────────────────────────────────────────────────────────────┤
│ BODY TERMS (2-3 ord)                                        │
│ Middels volum, middels konkurranse                         │
│ Eksempel: "CRM for SMB", "SEO-guide"                        │
├─────────────────────────────────────────────────────────────┤
│ LONG-TAIL (4+ ord)                                          │
│ Lavt volum, lav konkurranse, høy konvertering              │
│ Eksempel: "Beste CRM for konsulentbyrå i Norge"            │
└─────────────────────────────────────────────────────────────┘
```

**Strategi:** Start med long-tail for rask ranking, bygg opp til body og head terms.

---

## Én side = Én primary query

Hver side skal optimaliseres for ETT hovedsøkeord.

### Mapping-template

| Side | Primary Query | Secondary Keywords | Intent | Status |
|------|---------------|-------------------|--------|--------|
| /crm/ | beste crm for smb | crm-system, kundeoppfølging | Commercial | Live |
| /blogg/seo-guide/ | seo for nybegynnere | seo-tips, seo-guide | Informational | Live |
| /priser/ | norea pris | norea kostnader, prising | Transactional | Live |

### Optimalisering per side

| Element | Primary keyword |
|---------|-----------------|
| Title tag | I første 40 tegn |
| H1 | Inkludert naturlig |
| URL slug | Inkludert |
| Første 100 ord | Inkludert |
| Meta description | Inkludert |
| Alt-tekst (1+ bilder) | Variasjon |

### Keyword density

**Mål:** 1-2% for primary keyword

**Beregning:**
```
Density = (Antall ganger keyword / Totalt antall ord) × 100
```

**Eksempel:**
- 2000 ord artikkel
- "SEO" nevnt 30 ganger
- Density: 1.5% ✓

**Advarsel:**
- > 3% = Keyword stuffing risiko
- < 0.5% = Underoptimalisert

---

## Intern lenkestruktur

### Pillar/Cluster-modellen

```
                    ┌─────────────────────┐
                    │    PILLAR PAGE      │
                    │  (Hovedtema, 3000+) │
                    │  "Komplett CRM-guide"│
                    └──────────┬──────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
    ┌────▼────┐           ┌────▼────┐           ┌────▼────┐
    │ CLUSTER │           │ CLUSTER │           │ CLUSTER │
    │  (1500) │           │  (1500) │           │  (1500) │
    │ CRM for │           │ CRM vs  │           │ Beste   │
    │   SMB   │           │   ERP   │           │CRM 2025 │
    └─────────┘           └─────────┘           └─────────┘
```

**Lenkestrategi:**
- Cluster → Pillar (alle)
- Pillar → Cluster (alle)
- Cluster → Cluster (der relevant)

### Ankertekst

| Type | Eksempel | Når |
|------|----------|-----|
| Eksakt match | "SEO-guide for nybegynnere" | Sparsomt (1-2 per side) |
| Delvis match | "vår guide til SEO" | Primær bruk |
| Branded | "Les Norea-bloggen" | For merkevare-bygging |
| Generisk | "Les mer" | Unngå - gir ingen kontekst |

**Dårlig:**
```html
For mer info, <a href="/seo-guide/">klikk her</a>.
```

**Godt:**
```html
Lær mer i vår <a href="/seo-guide/">komplette SEO-guide for nybegynnere</a>.
```

### Lenkeregler

| Regel | Anbefaling |
|-------|------------|
| Minimum per side | 3-5 interne lenker |
| Plassering | I brødtekst, ikke bare footer |
| Relevans | Kun til relatert innhold |
| Nye sider | Lenk fra 2-3 eksisterende sider |
| Orphan pages | Ingen sider uten interne lenker |

---

## Ekstern lenking

### Lenk til autoriteter

Ekstern lenking til autoritative kilder styrker troverdighet.

| Gode kilder | Eksempler |
|-------------|-----------|
| Offisiell dokumentasjon | developer.google.com |
| Forskningsstudier | .edu, .gov, peer-reviewed |
| Bransjerapporter | Gartner, Forrester, Statista |
| Anerkjente publikasjoner | HBR, Wired, TechCrunch |

### Lenkeattributter

```html
<!-- Standard ekstern lenke -->
<a href="https://external.com" target="_blank" rel="noopener">
  Ekstern kilde
</a>

<!-- Sponset/betalt lenke -->
<a href="https://partner.com" rel="sponsored noopener">
  Partner
</a>

<!-- Bruker-generert innhold (kommentarer) -->
<a href="https://user-link.com" rel="ugc noopener">
  Brukerlenke
</a>

<!-- Ikke stol på denne kilden -->
<a href="https://untrusted.com" rel="nofollow noopener">
  Usikker kilde
</a>
```

---

## Duplikatinnhold

### Identifiser duplikater

| Type | Problem | Løsning |
|------|---------|---------|
| Eksakt duplikat | To identiske sider | Slett én, 301 redirect |
| Nær-duplikat | Svært likt innhold | Konsolider eller differensier |
| Parameter-duplikat | ?color=red vs ?color=blue | Canonical til hovedside |
| WWW vs non-WWW | Samme innhold | Velg én, 301 redirect |

### Canonical-bruk

```html
<!-- Produktside med parametere -->
<!-- URL: /produkt/?farge=rod&str=m -->
<link rel="canonical" href="https://example.com/produkt/">
```

### Konsolidering vs differensiering

**Konsolider når:**
- Sidene konkurrerer mot hverandre
- Ingen unik verdi i hver side
- Lite trafikk på begge

**Differensier når:**
- Ulike søkeintensjoner
- Ulikt publikum
- Begge har betydelig trafikk

---

## Tynne sider

### Identifisering

| Indikator | Terskel |
|-----------|---------|
| Ordtelling | < 300 ord |
| Bounced rate | > 80% |
| Time on page | < 30 sek |
| Rankings | Ingen top-100 |

### Handlingsalternativer

| Tiltak | Når |
|--------|-----|
| Utvid | Emnet fortjener mer innhold |
| Konsolider | Slå sammen med relatert side |
| Slett | Ingen søkevolum, ingen verdi |
| noindex | Nødvendig, men ikke ranking-verdig |

---

## Skriv naturlig (unngå AI-deteksjon)

Google kan nedgradere åpenbart AI-generert innhold som mangler verdi.

### Signaler på AI-slop

| Signal | Eksempel |
|--------|----------|
| Overgeneralisering | "I dagens digitale verden..." |
| Filler-fraser | "Det er viktig å merke seg at..." |
| Repetitiv struktur | Alle avsnitt starter likt |
| Manglende spesifisitet | Ingen tall, case, eksempler |
| Perfekt grammatikk | Ingen menneskelige variasjoner |

### Skrivetips for autentisitet

| Teknikk | Eksempel |
|---------|----------|
| Personlig erfaring | "Da vi implementerte dette i 2023..." |
| Spesifikke tall | "ROI på 47% over 6 måneder" |
| Navngitte eksempler | "Som Klarna gjorde med sin checkout..." |
| Meninger | "Jeg anbefaler ikke X fordi..." |
| Kontroverser | "Mange er uenige, men..." |

### Redigerings-workflow

1. **AI-draft** (hvis brukt) - Rå første utkast
2. **Fakta-sjekk** - Verifiser alle påstander
3. **Personliggjør** - Legg til erfaringer, meninger
4. **Spesifiser** - Erstatt generelt med konkret
5. **Voice check** - Matcher det merkevaren?
6. **Human touch** - Les høyt, naturlig?

---

## Content refresh

### Når oppdatere

| Trigger | Handling |
|---------|----------|
| Årlige oppdateringer | Oppdater "(2024)" til "(2025)" |
| Trafikknedgang | Analyser og forny |
| Utdaterte fakta | Oppdater statistikk |
| Nye konkurrenter ranker | Utvid og forbedre |
| SERP-endring | Tilpass til nye features |

### Oppdaterings-sjekkliste

- [ ] Oppdater dateModified i schema
- [ ] Oppdater "sist oppdatert" synlig
- [ ] Forny utdaterte tall
- [ ] Legg til nye seksjoner om nødvendig
- [ ] Sjekk og fiks broken links
- [ ] Forbedre interne lenker
- [ ] Oppgrader bilder om nødvendig

---

## Innholdskalender

### Template

| Uke | Innhold | Primary Query | Type | Status | Ansvarlig |
|-----|---------|---------------|------|--------|-----------|
| 1 | SEO-guide | seo for nybegynnere | Pillar | Planlagt | Kenneth |
| 2 | On-page tips | on-page seo tips | Cluster | Planlagt | - |
| 3 | Technical audit | teknisk seo sjekkliste | Cluster | Planlagt | - |
| 4 | Link building | link building strategi | Cluster | Planlagt | - |

### Prioritering

1. **Quick wins** - Long-tail med lav konkurranse
2. **Pillar pages** - Bygger topical authority
3. **Conversion pages** - Høy kommersiell intent
4. **Clusters** - Støtter pillar pages
5. **Updates** - Forbedre eksisterende

---

## Sjekkliste

### Per innhold
- [ ] Primary query definert
- [ ] Intent matcher innholdstype
- [ ] Keyword i title, H1, URL, første 100 ord
- [ ] 3-5 interne lenker med god ankertekst
- [ ] 1-2 eksterne lenker til autoriteter
- [ ] Ingen duplikatinnhold
- [ ] > 300 ord (ideelt 1500+ for konkurransedyktige termer)
- [ ] Lesbart og engasjerende
- [ ] Oppdatert dateModified

### Site-wide
- [ ] Pillar/cluster-struktur definert
- [ ] Alle sider har interne lenker (ingen orphans)
- [ ] Canonical tags på alle sider
- [ ] Keyword-mapping komplett
- [ ] Innholdskalender vedlikeholdt
- [ ] Regelmessig content audit

---

## Verktøy

| Verktøy | Bruk |
|---------|------|
| Google Search Console | Queries, klikkdata |
| Ahrefs / SEMrush | Keyword research, konkurrentanalyse |
| Screaming Frog | Intern lenke-audit |
| Surfer SEO | On-page optimalisering |
| Clearscope | Innholdsoptimalisering |
