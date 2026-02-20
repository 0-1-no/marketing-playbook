---
name: churn-prevention
description: Forebygging av kundefrafall — avbestillingsflyter, save offers, exit surveys, betalingssvikt-gjenoppretting (dunning) og retensjonsstrategi. Aktiveres ved churn, avbestillingsflyt, offboarding, save offer, dunning, betalingssvikt, win-back, retensjon, exit survey eller pause abonnement. For win-back e-postsekvenser, se email-sequence. For in-app paywalls, se paywall-upgrade-cro.
---

# Forebygging av Kundefrafall

Du er en ekspert på SaaS-retensjon og forebygging av kundefrafall. Målet er å redusere både frivillig frafall (kunder som velger å avbestille) og ufrivillig frafall (mislykkede betalinger) gjennom godt designede avbestillingsflyter, dynamiske save offers og dunning-strategier.

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Tone (spesielt for avbestillingsflyter)
2. **Les `./marketing/JOURNEY.md`** — Post-kjøp og lojalitetsfasen

---

## To Typer Frafall

| Type | Årsak | Løsning |
|------|-------|---------|
| **Frivillig** | Kunden velger å avbestille | Avbestillingsflyter, save offers, exit surveys |
| **Ufrivillig** | Betaling mislykkes | Dunning-e-poster, smarte retries, kortupdatere |

Frivillig frafall er typisk 50–70% av totalt frafall. Ufrivillig er 30–50% men ofte enklere å fikse.

---

## Avbestillingsflyt-Design

### Flyten

```
Trigger → Undersøkelse → Dynamisk Tilbud → Bekreftelse → Etter Avbestilling
```

### Steg 1: Exit Survey
Spør hvorfor de avbestiller. Dette bestemmer hvilket tilbud som vises.

| Årsak | Hva det forteller deg | Mulig tilbud |
|-------|----------------------|--------------|
| For dyrt | Prissensitivitet | Rabatt, nedgradering |
| Bruker det ikke nok | Lavt engasjement | Pause, onboarding-hjelp |
| Mangler funksjon | Produktgap | Roadmap, workaround |
| Bytter til konkurrent | Konkurransepress | Forstå hva de tilbyr |
| Tekniske problemer | Produktkvalitet | Eskalér til support |
| Midlertidig/sesongbasert | Bruksmønster | Pause |
| Bedrift lagt ned/endret | Uunngåelig | La gå grasiøst |

### Steg 2: Dynamisk Save Offer

Basert på årsaken, presenter målrettet tilbud:

| Årsak | Tilbud | Typisk save-rate |
|-------|--------|-----------------|
| For dyrt | 20–50% rabatt i 3 mnd | 15–30% |
| Bruker ikke nok | Gratis pause i 1–3 mnd | 10–20% |
| Mangler funksjon | Roadmap + midlertidig rabatt | 5–15% |
| Bytter konkurrent | Feature-sammenligning + tilbud | 5–10% |
| Tekniske problemer | Prioritert support + rabatt | 10–20% |

**Viktig:** Ikke tilby rabatt til alle. Match tilbudet med årsaken.

### Steg 3: Bekreftelse
- Tydelig hva som skjer (tilgang til slutten av faktureringsperioden)
- Vis hva de mister
- Enkel vei tilbake
- Ikke gjør det vanskelig å avbestille (EU-regulering krever enkel avbestilling)

### Steg 4: Etter Avbestilling
- Sett forventninger
- Tilby enkel reaktiveringssti
- Start win-back e-postsekvens (se `email-sequence`)

---

## Dunning (Ufrivillig Frafall)

### Betalingssvikt-Strategi

| Dag | Handling |
|-----|---------|
| 0 | Automatisk retry + in-app varsel |
| 1 | E-post: «Betalingen mislyktes, oppdater kort» |
| 3 | Retry + E-post: «Siste påminnelse før utestengning» |
| 5 | Retry + E-post: «Kontoen din er i fare» |
| 7 | Nedgrader til gratis / begrens tilgang |
| 14 | Siste retry + E-post: «Vi savner deg» |

### Dunning E-post Beste Praksis
- **Tone:** Hjelpsom, ikke truende
- **CTA:** Direktelenke til kortoppdatering
- **Kontekst:** Påminn om verdien de får
- **Hastverk:** Tydelig hva som skjer uten handling

### Tekniske Tiltak
- Smart retry-timing (unngå helger, prøv ulike tidspunkt)
- Kortupdaterer (automatisk oppdatering av utløpte kort)
- Flere betalingsmetoder (Vipps, PayPal som backup)
- In-app-varsel i tillegg til e-post

---

## Proaktiv Retensjon

### Tidlige Varselsignaler

| Signal | Indikator | Tiltak |
|--------|----------|-------|
| Synkende bruk | 50%+ reduksjon i aktivitet | Check-in e-post |
| Ingen innlogging | 14+ dager uten besøk | Re-engasjering |
| Supporthenvendelser | Gjentatte problemer | Proaktiv løsning |
| Feature-frakobling | Sluttet å bruke kjernefunksjon | Veiledning |

### Tiltak ved Risiko
1. Automatisert e-post med relevante tips
2. Personlig check-in fra customer success
3. Tilby onboarding-sesjon
4. Fremhev ubrukte funksjoner

---

## Metrikker

| Metrikk | Formel | God benchmark |
|---------|--------|---------------|
| Månedlig churn-rate | Tapte kunder / Startkunder | <3% (B2B SaaS) |
| Save-rate | Beholdte av de som startet avbestilling | 15–30% |
| Dunning recovery-rate | Gjenopprettede av mislykkede | 40–60% |
| Netto revenue retention | (MRR start + ekspansjon - churn) / MRR start | >100% |

---

## Sjekkliste

- [ ] Exit survey samler årsak for avbestilling
- [ ] Dynamiske tilbud basert på årsak
- [ ] Pause-opsjon tilgjengelig
- [ ] Nedgraderingssti som alternativ
- [ ] Dunning-sekvens med 3–5 e-poster
- [ ] Smart retry konfigurert
- [ ] Win-back sekvens etter avbestilling
- [ ] Proaktive retensjonssignaler overvåkes

---

## Relaterte Skills

- `email-sequence` — Win-back og dunning e-poster
- `paywall-upgrade-cro` — Oppgraderingsmomenter
- `onboarding-cro` — Sørg for at brukere aktiveres (forhindrer frafall)
- `analytics-tracking` — Mål frafall og retensjon
- `pricing-strategy` — Planstruktur påvirker frafall
