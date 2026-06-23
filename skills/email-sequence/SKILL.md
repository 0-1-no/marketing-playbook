---
name: email-sequence
description: E-postsekvenser og automatisering — velkomstsekvenser, drip-kampanjer, nurture-sekvenser, onboarding-e-poster, re-engasjering og livssyklus-e-poster. Aktiveres ved e-postsekvens, drip-kampanje, nurture-sekvens, velkomst-e-poster, e-postautomatisering eller livssyklus-e-poster. For in-app onboarding, se onboarding-cro.
---

# E-postsekvenser

Du er en ekspert på e-postmarkedsføring og automatisering. Målet er å lage e-postsekvenser som bygger relasjoner, driver handling og fører folk mot konvertering.

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ EMAIL-SEQUENCE SKILL (Global Plugin)                                │
│                                                                     │
│ Inneholder kun metodikk: hvordan lage effektive e-postsekvenser.   │
│ INGEN konkrete produktverdier — de kommer fra kodebasen.           │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/BRAND.md + JOURNEY.md (DENNE KODEBASEN)                 │
│                                                                     │
│ • Tone of Voice → Hvordan e-poster skrives                         │
│ • Kundereise → Hvilken fase mottakerne er i                        │
│ • Posisjonering → Verdiforslag i e-poster                          │
│ • Differensiatorer → Hva som skiller deg fra alternativer          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Tone, posisjonering, differensiatorer
2. **Les `./marketing/JOURNEY.md`** — Kundereisefaser og touchpoints
3. **Les `./marketing/CONTENT-RULES.md`** — Innholdsregler (om den finnes)

Hvis filene ikke finnes, kjør `/marketing-playbook:init` først.

---

## Kjerneprinsipp

### 1. Én E-post, Én Jobb
- Hver e-post har ett primært formål
- Én hoved-CTA per e-post
- Ikke prøv å gjøre alt på en gang

### 2. Verdi Før Forespørsel
- Led med nytte
- Bygg tillit gjennom innhold
- Fortjen retten til å selge

### 3. Relevans Over Volum
- Færre, bedre e-poster vinner
- Segmenter for relevans
- Kvalitet > frekvens

### 4. Tydelig Vei Videre
- Hver e-post beveger mottakeren et sted
- Lenker skal gjøre noe nyttig
- Gjør neste steg opplagt

---

## Sekvenstyper

### Velkomstsekvens (Etter Registrering)
**Lengde:** 5–7 e-poster over 12–14 dager
**Mål:** Aktiver, bygg tillit, konverter

| E-post | Dag | Formål |
|--------|-----|--------|
| 1 | 0 (umiddelbart) | Velkommen + lever lovet verdi |
| 2 | 1–2 | Rask gevinst — første suksess |
| 3 | 3–4 | Historien din — hvorfor du bygger dette |
| 4 | 5–6 | Sosial bevis — kundereferanse |
| 5 | 7–8 | Overkom innvending |
| 6 | 9–11 | Kjernefunksjon fremhevet |
| 7 | 12–14 | Konvertering — tydelig CTA |

### Nurture-Sekvens (Før Salg)
**Lengde:** 6–8 e-poster over 2–3 uker
**Mål:** Bygg tillit, demonstrer ekspertise, konverter

| E-post | Dag | Formål |
|--------|-----|--------|
| 1 | 0 | Lever lead magnet + introduksjon |
| 2 | 2–3 | Utdyp temaet |
| 3 | 4–5 | Dykk inn i problemet |
| 4 | 6–8 | Løsningsrammeverk |
| 5 | 9–11 | Casestudie |
| 6 | 12–14 | Differensiering |
| 7 | 15–18 | Innvendingshåndtering |
| 8 | 19–21 | Direkte tilbud |

### Re-engasjering
**Lengde:** 3–4 e-poster over 2 uker
**Trigger:** 30–60 dager uten aktivitet
**Mål:** Vinn tilbake eller rens listen

| E-post | Formål |
|--------|--------|
| 1 | Innsjekking (genuint bryr seg) |
| 2 | Verdi-påminnelse (hva er nytt) |
| 3 | Insentiv (spesialtilbud) |
| 4 | Siste sjanse (bli eller avslutt abonnement) |

### Onboarding-Sekvens (Produktbrukere)
**Lengde:** 5–7 e-poster over 14 dager
**Mål:** Aktiver, driv til aha-øyeblikk, oppgrader

| E-post | Dag | Formål |
|--------|-----|--------|
| 1 | 0 | Velkommen + første steg |
| 2 | 1 | Kom-i-gang-hjelp |
| 3 | 2–3 | Funksjon fremhevet |
| 4 | 4–5 | Suksesshistorie |
| 5 | 7 | Innsjekking |
| 6 | 10–12 | Avansert tips |
| 7 | 14+ | Oppgrader/utvid |

**Koordiner med in-app onboarding** — e-post støtter, ikke dupliserer.

---

## Emnelinjestrategi

### Prinsipper
- Tydelig > Kreativt
- Spesifikt > Vagt
- Fordels- eller nysgjerrighetsdrevet
- 40–60 tegn ideelt

### Mønster som fungerer

| Type | Eksempel |
|------|----------|
| Spørsmål | «Sliter du fortsatt med [problem]?» |
| Hvordan | «Slik oppnår du [resultat] på [tid]» |
| Tall | «3 måter å [fordel] på» |
| Direkte | «[Fornavn], din [ting] er klar» |
| Historie | «Feilen jeg gjorde med [tema]» |

### Forhåndsvisningstekst
- Utvider emnelinjen
- ~90–140 tegn
- Ikke gjenta emnelinjen
- Fullfør tanken eller legg til nysgjerrighet

---

## Retningslinjer for E-posttekst

### Struktur
1. **Hook** — Første linje fanger oppmerksomhet
2. **Kontekst** — Hvorfor dette betyr noe for dem
3. **Verdi** — Det nyttige innholdet
4. **CTA** — Hva de skal gjøre nå
5. **Avslutning** — Menneskelig, varm signatur

### Formatering
- Korte avsnitt (1–3 setninger)
- Luft mellom seksjoner
- Punktlister for skannbarhet
- Fet tekst for utheving (sparsomt)
- Mobil-først (de fleste leser på telefon)

### Tone
- Samtalende, ikke formell
- Førsteperson (jeg/vi) og andreperson (du)
- Aktiv stemme
- Les høyt — høres det menneskelig ut?

### Lengde
- 50–125 ord for transaksjonelle
- 150–300 ord for pedagogiske
- 300–500 ord for historiedrevne

### CTA-Retningslinjer
- Knapper for primærhandlinger
- Lenker for sekundærhandlinger
- Én tydelig primær CTA per e-post
- Knappetekst: Handling + resultat

---

## Utdataformat

### Sekvensoversikt
```
Sekvensnavn: [Navn]
Trigger: [Hva starter sekvensen]
Mål: [Primært konverteringsmål]
Lengde: [Antall e-poster]
Timing: [Forsinkelse mellom e-poster]
Avslutningsbetingelser: [Når de forlater sekvensen]
```

### For Hver E-post
```
E-post [#]: [Navn/Formål]
Send: [Timing]
Emnelinje: [Emnelinje]
Forhåndsvisning: [Forhåndsvisningstekst]
Innhold: [Komplett tekst]
CTA: [Knappetekst] → [Lenkedestinasjon]
Segment/Betingelser: [Om aktuelt]
```

---

## Norsk E-post-Kontekst

- **GDPR:** Samtykke kreves for markedsføring. Dokumenter samtykke.
- **Markedsføringsloven:** Tydelig avsender, enkelt å avslutte abonnement.
- **Tone:** Nordmenn foretrekker direkte, uformell kommunikasjon. Unngå overdreven salgstekst.
- **Timing:** Norsk arbeidstid er 08–16. Tirsdag–torsdag er typisk best for B2B.
- **Språk:** Skriv på norsk med mindre målgruppen er internasjonal.

---

## Oppgavespesifikke Spørsmål

1. Hva trigger inngang til denne sekvensen?
2. Hva er primærmålet/konverteringshandlingen?
3. Hva vet mottakerne allerede om deg?
4. Hvilke andre e-poster mottar de?
5. Hva er nåværende e-postytelse?

---

## Relaterte Skills

- `churn-prevention` — Cancel flows og save offers (e-post støtter dette)
- `onboarding-cro` — In-app onboarding (e-post støtter dette)
- `storytelling-copywriting` — Tekst og rammeverk
- `ab-test-setup` — Test e-postelementer
- `popup-cro` — E-post-innsamling via popups

> **Kvalitetsnotat:** For høyverdi tekst (emnelinjer på store utsendelser), vurder kvalitetsmodus — se [`marketing-playbook/COPY-QUALITY-MODE.md`](../marketing-playbook/COPY-QUALITY-MODE.md).
