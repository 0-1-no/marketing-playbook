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
- Matcher den trafikkildens budskap? (Annonse → Landing page konsistens)

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
