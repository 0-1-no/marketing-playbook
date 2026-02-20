---
name: ab-test-setup
description: A/B-testing og eksperimentdesign — planlegg, design og implementer tester med statistisk gyldighet. Aktiveres ved A/B-test, splittest, eksperiment, «test denne endringen», variant, multivariat test eller hypotese. For sporingsimplementering, se analytics-tracking.
---

# A/B-Test Oppsett

Du er en ekspert på eksperimentering og A/B-testing. Målet er å hjelpe med å designe tester som gir statistisk gyldige, handlingsbare resultater.

---

## Før du starter

1. **Les `./marketing/DISTRIBUTION.md`** — Trafikkvolum og kanaler
2. **Les `./marketing/LEARNINGS.md`** — Tidligere testresultater

---

## Kjerneprinsipp

### 1. Start med en Hypotese
- Ikke bare «la oss se hva som skjer»
- Spesifikk prediksjon av resultat
- Basert på resonnement eller data

### 2. Test Én Ting
- Én variabel per test
- Ellers vet du ikke hva som virket

### 3. Statistisk Strenghet
- Forhåndsbestemt utvalgsstrørrelse
- Ikke kikk og stopp tidlig
- Forplikt deg til metodikken

### 4. Mål Det Som Betyr Noe
- Primærmetrikk knyttet til forretningsverdi
- Sekundærmetrikker for kontekst
- Sikkerhetsvaktmetrikker for å forhindre skade

---

## Hypoteserammeverk

### Struktur

```
Fordi [observasjon/data],
tror vi at [endring]
vil føre til [forventet resultat]
for [målgruppe].
Vi vet dette er sant når [metrikker].
```

### Eksempel

**Svak:** «Å endre knappefarge kan øke klikk.»

**Sterk:** «Fordi brukere rapporterer vanskeligheter med å finne CTA (per heatmaps), tror vi at å gjøre knappen større og bruke kontrastfarge vil øke CTA-klikk med 15%+ for nye besøkende. Vi måler klikkrate fra sidevisning til registreringsstart.»

---

## Testtyper

| Type | Beskrivelse | Trafikk behov |
|------|-------------|---------------|
| A/B | To versjoner, én endring | Moderat |
| A/B/n | Flere varianter | Høyere |
| MVT | Flere endringer i kombinasjoner | Svært høyt |
| Split URL | Forskjellige URL-er for varianter | Moderat |

---

## Utvalgsstrørrelse

### Estimering

Avhenger av:
- Nåværende konverteringsrate (baseline)
- Minimum detekterbar effekt (MDE) du vil oppdage
- Statistisk signifikans (typisk 95%)
- Statistisk styrke (typisk 80%)

### Tommelfingerregler

| Baseline | Ønsket forbedring | Ca. utvalg per variant |
|----------|-------------------|----------------------|
| 2% | 20% relativ (→ 2.4%) | ~16 000 |
| 5% | 20% relativ (→ 6%) | ~6 000 |
| 10% | 10% relativ (→ 11%) | ~14 000 |

**Viktig:** Lav trafikk = test store endringer. Høy trafikk = kan teste subtile endringer.

---

## Testprioritering

### PIE-Rammeverket

| Faktor | Spørsmål | Skala |
|--------|----------|-------|
| **Potential** | Hvor mye forbedring er mulig? | 1–10 |
| **Importance** | Hvor viktig er denne siden/flyten? | 1–10 |
| **Ease** | Hvor enkelt er det å implementere? | 1–10 |

Gjennomsnitt = Prioritetspoeng. Test høyest poeng først.

---

## Utdataformat

### Testplan
```
Testnavn: [Navn]
Hypotese: [Fordi... tror vi... vil... Vi vet...]
Varianter: [Kontroll + Variant(er)]
Primærmetrikk: [Metrikk]
Sekundærmetrikker: [Metrikker]
Estimert utvalg: [Antall per variant]
Estimert varighet: [Dager]
Verktøy: [PostHog, VWO, Optimizely, etc.]
```

---

## Dokumenter Resultater

Lagre alltid testresultater i `./marketing/LEARNINGS.md`:

```markdown
## Test: [Navn]
- Dato: [Start–Slutt]
- Hypotese: [Hypotese]
- Resultat: [Vinner/Taper/Ingen forskjell]
- Effekt: [+X% på primærmetrikk]
- Konfidensintervall: [95% CI]
- Læring: [Hva lærte vi]
- Neste steg: [Hva tester vi neste]
```

---

## Vanlige Feil

- **Stopper for tidlig** — Vent til utvalgsstrørrelse er nådd
- **Kikker på data** — Bestem regler på forhånd
- **Tester for mange ting** — Én variabel om gangen
- **Ignorerer sesongeffekter** — Kjør over hele uker
- **Ingen dokumentasjon** — Uten dokumentasjon gjentar du feil

---

## Relaterte Skills

- `page-cro` — Identifiser hva som bør testes
- `analytics-tracking` — Sørg for riktig sporing
- `signup-flow-cro` — Test registreringsendringer
- `email-sequence` — Test e-postelementer
