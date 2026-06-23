---
name: page-cro
description: Konverteringsoptimalisering (CRO) for nettsider — landingssider, hjemmesider, prisingsider, produktsider og blogginnlegg. Aktiveres ved CRO, konverteringsoptimalisering, «denne siden konverterer ikke», «forbedre konverteringer» eller «hvorfor fungerer ikke denne siden». For registreringsflyt, se signup-flow-cro. For skjemaer, se form-cro. For popups, se popup-cro.
---

# Konverteringsoptimalisering (CRO)

Du er en ekspert på konverteringsoptimalisering. Målet er å analysere nettsider og gi konkrete anbefalinger som forbedrer konverteringsraten.

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ PAGE-CRO SKILL (Global Plugin)                                      │
│                                                                     │
│ Inneholder kun metodikk: hvordan analysere og forbedre sider.      │
│ INGEN konkrete sider eller URL-er — de kommer fra kodebasen.       │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/BRAND.md + JOURNEY.md (DENNE KODEBASEN)                 │
│                                                                     │
│ • Posisjonering → Verdiforslag og overskrifter                     │
│ • Målgruppe → Smertepunkter og motivasjon                          │
│ • Kundereise → Hvilken fase besøkende er i                         │
│ • Tone of Voice → Hvordan CTA-er og tekst formuleres               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Posisjonering, målgruppe, differensiatorer
2. **Les `./marketing/JOURNEY.md`** — Hvilken fase i kundereisen siden treffer
3. **Les `./marketing/DISTRIBUTION.md`** — Trafikkilder til siden

Hvis filene ikke finnes, kjør `/marketing-playbook:init` først.

---

## Analysemetode

Analyser siden i rekkefølge etter påvirkning:

### 1. Verdiforslag (Høyest påvirkning)

**Sjekk:**
- Kan en besøkende forstå hva dette er og hvorfor det er relevant innen 5 sekunder?
- Er hovedfordelen klar, spesifikk og differensiert?
- Er det skrevet i kundens språk (ikke bedriftsjargong)?

**Vanlige problemer:**
- Funksjonsfokusert i stedet for fordelsfokusert
- For vagt eller for kreativt (ofrer klarhet)
- Prøver å si alt i stedet for det viktigste

**Kobling til BRAND.md:** Verdiforslaget MÅ reflektere posisjonering og differensiatorer fra BRAND.md.

### 2. Overskrift

**Vurder:**
- Kommuniserer den kjerneverdien?
- Er den spesifikk nok til å bety noe?
- **Ad scent:** Matcher hero-overskrift, visuelt og tilbud annonsen som sendte dem hit? (samme løfte, samme nøkkelord, samme bilde). Brudd på «duften» = høy bounce og stigende CPA. Se `ad-creative` og `paid-ads` for annonsesiden.

**Sterke mønster:**
- Resultatfokusert: «Oppnå [ønsket resultat] uten [smertepunkt]»
- Spesifisitet: Inkluder tall, tidsrammer eller konkrete detaljer
- Sosial bevis: «Over 500 norske bedrifter bruker...»

### 3. CTA — Plassering, Tekst og Hierarki

**Primær CTA:**
- Er det én klar hovedhandling?
- Er den synlig uten å scrolle?
- Kommuniserer knappeteksten verdi, ikke bare handling?
  - Svak: «Send inn», «Registrer», «Les mer»
  - Sterk: «Start gratis prøveperiode», «Se priser», «Bestill demo»

**CTA-hierarki:**
- Finnes det en logisk primær vs. sekundær CTA?
- Gjentas CTA-er ved viktige beslutningspunkter?

### 4. Visuelt Hierarki og Skannbarhet

**Sjekk:**
- Kan noen som skanner forstå hovedbudskapet?
- Er de viktigste elementene visuelt fremtredende?
- Er det nok luft/whitespace?
- Støtter bildene budskapet eller distraherer de?

### 5. Tillitssignaler og Sosial Bevis

**Typer:**
- Kundelogoer (spesielt gjenkjennelige norske merker)
- Anmeldelser (spesifikke, med navn og bilde)
- Casestudier med reelle tall
- Vurderingspoeng (Trustpilot, Google anmeldelser)
- Sertifiseringer og medlemskap (bransjeforbund)

**Plassering:** Nær CTA-er og etter fordels-påstander.

### 6. Innvendingshåndtering

**Vanlige innvendinger:**
- Pris/verdi-bekymringer
- «Vil dette fungere for min situasjon?»
- Hvor vanskelig er det å komme i gang?
- «Hva hvis det ikke fungerer?»

**Håndter gjennom:** FAQ-seksjoner, garantier, sammenligning med alternativer, åpenhet om prosessen.

### 7. Friksjonspunkter

**Se etter:**
- For mange skjemafelt
- Uklare neste steg
- Forvirrende navigasjon
- Påkrevd informasjon som ikke burde være påkrevd
- Dårlig mobilopplevelse
- Treg lastetid

---

## Awareness-stadier og landingsside-format

En landingsside konverterer best når den møter den besøkende der de er. Eugene Schwartz' innsikt: hvor mye den besøkende allerede vet om problemet og løsningen — deres **awareness-nivå** — avgjør hvilket argument som trengs. Sender du kald trafikk til en ren produktside, hopper de av: de skjønner ikke engang hvorfor de skulle bry seg ennå. Sender du brand-søk-trafikk til en lang historie-side, irriterer du dem som var klare til å kjøpe.

> **Ikke det samme som funnel-stadiet.** Marketing Playbook bruker en kundereise (Awareness → Consideration → ... → Loyalty, se `JOURNEY.md`) som beskriver *hvor i kjøpsreisen* noen er. Schwartz' awareness-stige er en **separat, ortogonal akse**: *hvor klar over problemet/løsningen* de er akkurat nå. De utfyller hverandre — en person kan være «Solution Aware» i Schwartz-forstand mens de fortsatt er i Consideration-fasen i reisen. Bruk reisen til å forstå intensjon; bruk awareness-stigen til å velge sideformat.

Stigen, fra minst til mest aware, med anbefalt sideformat og typisk trafikk-kilde:

- **Unaware** (kjenner ikke problemet) → **story-drevet advertorial**. Du må først vekke problembevisstheten via en historie eller observasjon før du nevner produktet. Trafikk: kald social/discovery (folk som ikke leter).
- **Problem Aware** (kjenner problemet, ikke løsningen) → **listicle/edukativ side**. Lær dem hva som finnes; posisjoner kategorien din som svaret. Trafikk: Google-søk på problemet eller kategorien.
- **Solution Aware** (vurderer alternativer) → **proof-drevet side**: sammenligning, testimonials, verifisering, demo. De vet løsningstypen finnes — de trenger bevis på at *din* er best. Trafikk: comparison-research.
- **Most/Product Aware** (klar til å kjøpe) → **ren produktside**, minimal chrome, tydelig CTA. Ikke selg på nytt — gjør det enkelt å handle. Trafikk: direkte, retur-besøk, brand-søk.

| Awareness | Trafikk-kilde | Hva de trenger | Sideformat |
|-----------|---------------|----------------|------------|
| Unaware | Kald social/discovery | Vekke problemet | Story-drevet advertorial |
| Problem Aware | Google-søk (problem/kategori) | Forstå løsningskategorien | Listicle/edukativ side |
| Solution Aware | Comparison-research | Bevis på at du er best | Proof-drevet (sammenligning, demo, testimonials) |
| Most/Product Aware | Direkte, retur, brand-søk | Lav friksjon til kjøp | Ren produktside, tydelig CTA |

**Copy-vinkel per stadie:**
- Unaware: «Visste du at [skjult problem]?» — start i leserens verden, ikke i produktet.
- Problem Aware: «[Antall] måter å løse [problem] på» — kategoriser og posisjoner.
- Solution Aware: «[Ditt produkt] vs. [alternativ]: her er forskjellen» — direkte, bevisbasert.
- Most/Product Aware: «Kom i gang med [produkt]» — pris, CTA, ferdig.

**Rut etter awareness.** Du kan vise riktig format basert på `referrer` eller `UTM`-parametere: kald social-annonse → advertorial-variant, brand-søk → produktside. Samme tilbud, ulik inngang. Awareness-nivået forteller deg *hvilket argument*; trafikk-kilden er ofte proxyen som lar deg gjette det automatisk.

For overskrift- og vinkel-skifte per awareness-nivå (copy-siden av dette), se `storytelling-copywriting`.

---

## Sidespesifikke Rammeverk

### Hjemmeside
- Klar posisjonering for nye besøkende
- Rask vei til vanligste konvertering
- Håndter både «klar til å kjøpe» og «undersøker fortsatt»

### Landingsside
- **Sidestruktur:** Bruk ATIDCOA-sekvensen fra `storytelling-copywriting` → [FRAMEWORKS.md](../storytelling-copywriting/FRAMEWORKS.md) for optimal seksjonering
- Budskapsamsvar med trafikkilde (annonse → side)
- Én CTA (fjern navigasjon om mulig)
- Komplett argument på én side
- Tilpass budskap til kundereise-fase (fra JOURNEY.md)

### Prisingside
- Tydelig plansammenligning
- Anbefalt plan markert
- Håndter «hvilken plan passer for meg?»-angst
- Vis verdien, ikke bare funksjoner per plan

### Produktside / Funksjonsside
- Koble funksjon til fordel
- Brukstilfeller og eksempler
- Klar vei til å prøve/kjøpe

### Blogginnlegg
- Kontekstuelle CTA-er som matcher innholdets tema
- Inline CTA-er ved naturlige stoppunkter
- Ikke avbryt leseopplevelsen

---

## Utdataformat

Strukturer anbefalingene slik:

### Raske Gevinster (Implementer nå)
Enkle endringer med sannsynlig umiddelbar effekt.

### Høy-Påvirkning (Prioriter)
Større endringer som krever mer arbeid, men gir betydelig forbedring.

### Testideer
Hypoteser verdt å A/B-teste i stedet for å anta.

### Tekstalternativer
For nøkkelelementer (overskrifter, CTA-er), gi 2–3 alternativer med begrunnelse.

---

## Eksperimentideer

Når du anbefaler eksperimenter:

| Område | Hva å teste |
|--------|-------------|
| Hero-seksjon | Overskrift, visuelt, CTA |
| Sosial bevis | Type og plassering |
| Prispresentasjon | Layout, ankring, årlig vs. månedlig |
| Skjema | Antall felt, flersteg vs. ett steg |
| Navigasjon | Forenklet vs. full |

For testing-metodikk, se `ab-test-setup`.

---

## Oppgavespesifikke Spørsmål

1. Hva er nåværende konverteringsrate og mål?
2. Hvor kommer trafikken fra?
3. Hvordan ser registrerings-/kjøpsflyten ut etter denne siden?
4. Har du brukerdata, heatmaps eller session recordings?
5. Hva har du allerede prøvd?

---

## Relaterte Skills

- `signup-flow-cro` — Registreringsflyt-optimalisering
- `form-cro` — Skjema-optimalisering
- `popup-cro` — Popups og modals
- `storytelling-copywriting` — Komplett copy-omskriving
- `ab-test-setup` — Strukturert testing av endringer
- `analytics-tracking` — Sporingsoppsett for å måle forbedringer
