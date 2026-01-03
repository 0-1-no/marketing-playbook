# AEO (Answer Engine Optimization)

> **Metodikk-fil:** Dette er prinsipper for AI-søkeoptimalisering.
> Faktiske søkeord og innholdsstrategi dokumenteres i `./marketing/DISTRIBUTION.md`.
> Arbeid gjøres i den lokale kodebasen, ikke i denne plugin-filen.

Bruk denne filen når du optimaliserer for AI-søkemotorer som ChatGPT, Perplexity, Claude, Gemini og Google AI Overviews.

---

## Paradigmeskiftet

Vi beveger oss fra **link-økonomi** til **siterings-økonomi**.

```
TRADISJONELL SEO                    AEO/GEO
────────────────────────────────────────────────────────────
Rankings i SERP              →      Sitater i AI-svar
Klikk til nettside           →      Nevnelser og attribusjon
Backlinks = autoritet        →      E-E-A-T = autoritet
Keyword-match                →      Entity-match
10 blå lenker                →      Synthesert svar med kilder
Trafikk-måling               →      Share of Voice i AI
```

### Hvorfor dette endrer alt

| Innsikt | Implikasjon |
|---------|-------------|
| ChatGPT har 800M+ ukentlige brukere | Massivt nytt søkevolum |
| Google markedsandel under 90% | Første gang siden 2015 |
| 40%+ søk er zero-click | Svaret gis direkte, ingen klikk |
| AI siterer fra posisjon 21+ | Du trenger ikke side-1 for å bli sitert |

---

## De 4 pilarene for AEO

### Pilar 1: Innholdsarkitektur

AI-systemer prioriterer innhold som er lett å ekstrahere og sitere.

#### Answer Blocks

Skriv i modulære "answer blocks" på 40-60 ord som kan stå alene.

**Dårlig (vanskelig å sitere):**
```
Det er mange ting å tenke på når man jobber med SEO, og det
avhenger veldig av situasjonen, men generelt sett handler det
om å gjøre nettsiden synlig for søkemotorer, noe som kan gjøres
på forskjellige måter avhengig av hva man prøver å oppnå.
```

**Godt (lett å sitere):**
```
SEO (Search Engine Optimization) er prosessen med å optimalisere
nettsider for å rangere høyere i søkeresultater. Dette inkluderer
tre hovedområder: teknisk SEO for crawlability og hastighet,
on-page SEO for innhold og struktur, og off-page SEO for
autoritet gjennom lenker og omtaler.
```

#### Strukturformater AI elsker

| Format | Hvorfor | Eksempel |
|--------|---------|----------|
| Definisjoner | Besvarer "Hva er..." | "[Term] er [definisjon]" |
| Lister | Besvarer "Hvilke..." | "De 5 viktigste..." |
| Steg-for-steg | Besvarer "Hvordan..." | "1. Først... 2. Deretter..." |
| Sammenligninger | Besvarer "vs..." | "A skiller seg fra B ved..." |
| Fakta med kilder | Besvarer "Hvor mye..." | "Ifølge [kilde], er..." |

#### Løs intent i første 100 ord

Ikke bygg opp til svaret. Gi det umiddelbart.

**Dårlig:**
```
Mange lurer på hva som er best. Det finnes flere alternativer.
La oss se på bakgrunnen først...
[500 ord senere]
...så svaret er React.
```

**Godt:**
```
Det beste JavaScript-rammeverket for de fleste prosjekter er React.
Med over 200,000 GitHub-stjerner og brukt av Facebook, Netflix og
Airbnb, tilbyr det fleksibilitet, stort økosystem og sterk
jobbmarked. Her er hvorfor, og når du bør vurdere alternativer:
```

---

### Pilar 2: Autoritet og E-E-A-T

AI-systemer prioriterer innhold fra autoritative kilder.

#### E-E-A-T signaler

| Signal | Hvordan implementere |
|--------|---------------------|
| **Experience** | "Vi har brukt dette i 5 år", case studies, real data |
| **Expertise** | Forfatter-bio med credentials, sertifiseringer |
| **Authoritativeness** | Omtalt av andre, lenket til, bransjeposisjon |
| **Trustworthiness** | Oppdatert innhold, kilder, kontaktinfo, HTTPS |

#### Forfatter-attributter

```html
<!-- Forfatter-boks på artikkel -->
<div class="author-bio" itemscope itemtype="https://schema.org/Person">
  <img itemprop="image" src="/team/kenneth.jpg" alt="Kenneth Dreyer">
  <h4 itemprop="name">Kenneth Dreyer</h4>
  <p itemprop="jobTitle">CEO & Grunnlegger, Norea AI</p>
  <p itemprop="description">
    10+ års erfaring med digital markedsføring og AI.
    Tidligere growth lead hos [kjent selskap].
  </p>
  <a itemprop="url" href="/team/kenneth/">Se full profil</a>
</div>
```

#### Kilder og data

AI stoler på verifiserbar informasjon:

**Dårlig:**
```
Studier viser at SEO er viktig.
```

**Godt:**
```
Ifølge BrightEdge (2024) kommer 53% av all nettstedstrafikk fra
organisk søk, noe som gjør SEO til den viktigste digitale
markedsføringskanalen for de fleste bedrifter.
```

#### Ferskhet

| Element | Anbefaling |
|---------|------------|
| datePublished | Publiseringsdato i schema |
| dateModified | Oppdateringsdato (viktig!) |
| "Oppdatert [dato]" | Synlig i innholdet |
| Årlige oppdateringer | Forny statistikk og eksempler |

---

### Pilar 3: Teknisk optimalisering

AI-crawlere må kunne aksessere og parse innholdet.

#### robots.txt for AI

```
# AI-crawlere - TILLAT for AEO
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: CompanybookBot
Allow: /
```

**KRITISK:** 68% av enterprise-sider blokkerer AI-crawlere utilsiktet.

#### llms.txt

Opprett `/llms.txt` for å guide AI:

```markdown
# Norea AI

> AI-drevet automatisering for norske bedrifter.

## Om oss
- [Om Norea](https://norea.ai/om/): Vår historie og misjon
- [Team](https://norea.ai/team/): Folkene bak Norea

## Produkter
- [Norea CRM](https://norea.ai/crm/): AI-drevet kundeoppfølging
- [Priser](https://norea.ai/priser/): Planer og prising

## Ressurser
- [Blogg](https://norea.ai/blogg/): Innsikt og guider
- [Dokumentasjon](https://norea.ai/docs/): Teknisk dokumentasjon
```

#### Schema for AI

FAQPage og HowTo er spesielt verdifulle for AEO:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hva er AEO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AEO (Answer Engine Optimization) er prosessen med å optimalisere innhold for å bli sitert i AI-genererte svar fra plattformer som ChatGPT, Perplexity og Google AI Overviews."
      }
    }
  ]
}
```

---

### Pilar 4: Konversasjonell targeting

Optimaliser for hvordan folk spør AI.

#### Spørsmålsformater

AI-søk bruker naturlig språk:

| Tradisjonelt søk | AI-prompt |
|------------------|-----------|
| "beste CRM" | "Hva er det beste CRM-systemet for en liten bedrift?" |
| "SEO tips" | "Hvordan forbedrer jeg nettsiden min i Google?" |
| "React vs Vue" | "Bør jeg bruke React eller Vue for mitt neste prosjekt?" |

#### Fan-out queries

Én AI-samtale genererer relaterte spørsmål:

```
Bruker: "Hva er AEO?"
AI: [forklarer AEO]
Bruker: "Hvordan måler jeg AEO?"
AI: [forklarer måling]
Bruker: "Hvilke verktøy finnes for AEO?"
AI: [lister verktøy]
```

**Strategi:** Dekk hele emnet, ikke bare én vinkel.

#### Intent-typer for AEO

| Intent | Trigger-ord | Innholdsformat |
|--------|-------------|----------------|
| Definer | "Hva er", "Definer" | Klar definisjon først |
| Sammenlign | "vs", "forskjell mellom" | Tabell med pro/con |
| Hvordan | "Hvordan", "Steg for steg" | Nummerert liste |
| Anbefal | "Beste", "Anbefalt" | Prioritert liste med begrunnelse |
| Troubleshoot | "Fungerer ikke", "Feilmelding" | Problem → Årsak → Løsning |

---

## Skriv for sitater

### Sitérbar skriving

| Prinsipp | Eksempel |
|----------|----------|
| Spesifikt > Generelt | "42% ROI" > "høy ROI" |
| Fakta > Meninger | "Brukt av 10,000+" > "Populært verktøy" |
| Direkte > Omstendelig | "SEO er X" > "Det kan sies at SEO..." |
| Tall > Ord | "3-6 måneder" > "en stund" |

### Definisjonsformelen

```
[Term] er [kategori] som [funksjon/formål], [unik egenskap].
```

**Eksempel:**
```
Norea CRM er et AI-drevet kundebehandlingssystem som automatiserer
oppfølging og salg, spesielt designet for norske SMB-er.
```

### FAQ-strukturen

```markdown
## Vanlige spørsmål

### Hva er [term]?

[40-60 ord direkte svar som kan stå alene]

### Hvorfor er [term] viktig?

[40-60 ord med konkrete fordeler]

### Hvordan kommer jeg i gang med [term]?

[Nummerert steg-for-steg, 3-5 steg]
```

---

## Plattform-spesifikk optimalisering

### ChatGPT / SearchGPT

| Faktor | Anbefaling |
|--------|------------|
| Crawler | GPTBot, ChatGPT-User |
| Sitats-stil | 2-3 kilder per svar i snitt |
| Favoriserer | LinkedIn, G2, Gartner-style innhold |
| Teknikk | Klare definisjoner, autoritative kilder |

### Perplexity

| Faktor | Anbefaling |
|--------|------------|
| Crawler | PerplexityBot |
| Sitats-stil | 6-7 kilder per svar i snitt |
| Favoriserer | Video, reviews, community-innhold |
| Teknikk | Multimedia, PeerSpot-style anmeldelser |

### Google AI Overviews (SGE)

| Faktor | Anbefaling |
|--------|------------|
| Crawler | Google-Extended |
| Sitats-stil | Integrert med SERP |
| Favoriserer | Eksisterende Google-ranking |
| Teknikk | E-E-A-T, People Also Ask-optimalisering |

### Claude

| Faktor | Anbefaling |
|--------|------------|
| Crawler | ClaudeBot |
| Sitats-stil | Grundig med kilder |
| Favoriserer | Teknisk dokumentasjon, akademisk |
| Teknikk | Strukturert data, code examples |

---

## AEO Scorecard

### 4 nøkkelmetrikker

#### 1. AI Visibility

**Definisjon:** Blir du anbefalt for prioriterte søkeord?

**Måling:**
1. Lag liste over 10-20 prioriterte queries
2. Test i ChatGPT, Perplexity, Claude, Gemini
3. Dokumenter hvilke queries som nevner ditt brand
4. Beregn: (queries med nevnelse / totalt) × 100

**Mål:** 60%+

#### 2. AI Share of Voice

**Definisjon:** Hvor ofte nevnes DU vs konkurrenter?

**Måling:**
1. Kjør samme queries 10 ganger
2. Tell alle merkevare-nevnelser
3. Beregn din andel: (dine nevnelser / totalt) × 100

**Mål:** Match eller overgå SEO-markedsandel

#### 3. AI Citations

**Definisjon:** Hvor ofte er din URL kilden til svaret?

**Måling:**
1. Sjekk AI bot-trafikk i analytics
2. Bruk verktøy som XFunnel for citation tracking
3. Test queries og noter kildeattribusjon

**Mål:** 30%+ av relevante queries

#### 4. Referral Demand

**Definisjon:** Trafikk som oppdaget deg via AI, men besøkte senere.

**Måling:** Post-purchase survey:
```
Hvordan hørte du først om oss?
○ Google-søk
○ Anbefalt av venn
○ AI-assistent (ChatGPT, Perplexity, etc.)
○ Sosiale medier
○ Annet
```

**Mål:** Vekst over tid

---

## Scorecard-template

```
┌─────────────────────────────────────────────────┐
│ AEO SCORECARD - [Dato]                          │
├─────────────────────────────────────────────────┤
│                                                 │
│ AI VISIBILITY                    [X]% → Mål: 60%│
│ ────────────────────────────────                │
│ Queries med brand-tilstedeværelse: X/Y          │
│                                                 │
│ AI SHARE OF VOICE                [X]% → Mål: Match SEO
│ ────────────────────────────────                │
│ Din andel vs konkurrenter                       │
│ Konkurrent A: X% | Konkurrent B: X% | Du: X%    │
│                                                 │
│ AI CITATIONS                     [X]% → Mål: 30%│
│ ────────────────────────────────                │
│ Din URL som kilde i AI-svar                     │
│                                                 │
│ REFERRAL DEMAND                  [X] → Mål: Vekst
│ ────────────────────────────────                │
│ Post-purchase survey: "Fant via AI"             │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## Diagnostikk

### Lavt AI Visibility

| Diagnose | Løsning |
|----------|---------|
| Crawlere blokkert | Oppdater robots.txt |
| Innhold for komplekst | Forenkle, legg til tydelige svar |
| Manglende schema | Implementer FAQPage, HowTo |
| Svake entity-signaler | Styrk topic authority |

### Høy visibility, lave citations

| Diagnose | Løsning |
|----------|---------|
| Manglende autoritet | Legg til data, ekspertkilder |
| Svar ikke direkte | Reskriv med verdi i første avsnitt |
| Ufullstendig schema | Valider og utvid strukturert data |
| Utdatert innhold | Oppdater tall og eksempler |

### Plattform-spesifikke problemer

| Plattform | Problem | Tiltak |
|-----------|---------|--------|
| ChatGPT | Ikke sitert | Fokuser på LinkedIn, autoritativt innhold |
| Perplexity | Ignorert | Legg til video, PeerSpot-style reviews |
| Gemini | Mangler | Optimaliser for Medium, Reddit |
| AI Overviews | Fraværende | Styrk E-E-A-T, forbedre Google-ranking |

---

## Sjekkliste for AEO-readiness

### Teknisk
- [ ] robots.txt tillater GPTBot, ClaudeBot, PerplexityBot, CompanybookBot
- [ ] llms.txt opprettet på root
- [ ] FAQPage schema på relevante sider
- [ ] HowTo schema på guider
- [ ] Ingen JavaScript-avhengig kritisk innhold

### Innhold
- [ ] Klare definisjoner i første 100 ord
- [ ] Answer blocks på 40-60 ord
- [ ] FAQ-seksjon med strukturerte Q&A
- [ ] Kilder og data med attribusjon
- [ ] Oppdatert dateModified

### Autoritet
- [ ] Forfatter-bios med credentials
- [ ] Organization schema på root
- [ ] Ekstern validering (omtaler, lenker)
- [ ] Original data eller research

### Måling
- [ ] Query-liste for tracking
- [ ] AI bot-trafikk i analytics
- [ ] Post-purchase survey implementert
- [ ] Månedlig scorecard-oppdatering

---

## Verktøy

| Verktøy | Bruk | Kostnad |
|---------|------|---------|
| HubSpot AEO Grader | AI visibility audit | Gratis |
| XFunnel | Full AEO tracking | Betalt |
| Manuell testing | Query-by-query | Gratis (tid) |
| Google Analytics | AI bot-trafikk | Gratis |
