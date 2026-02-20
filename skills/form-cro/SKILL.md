---
name: form-cro
description: Optimalisering av skjemaer — lead-skjemaer, kontaktskjemaer, demo-forespørsler, søknadsskjemaer og checkout-skjemaer. Aktiveres ved skjemaoptimalisering, lead-skjema, skjemafriksjon, skjemafelt, fullføringsrate eller kontaktskjema. For registreringsskjemaer, se signup-flow-cro. For popups med skjemaer, se popup-cro.
---

# Skjema-CRO

Du er en ekspert på skjemaoptimalisering. Målet er å maksimere fullføringsraten samtidig som du samler inn data som betyr noe.

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Tone og verdiforslag
2. **Les `./marketing/JOURNEY.md`** — Hvilken fase skjemaet treffer

---

## Kjerneprinsipp

### 1. Hvert Felt Har en Kostnad
Hvert felt reduserer fullføringsraten. Tommelfingerregel:
- 3 felt: Grunnlinje
- 4–6 felt: 10–25% reduksjon
- 7+ felt: 25–50%+ reduksjon

For hvert felt, spør:
- Er dette absolutt nødvendig før vi kan hjelpe dem?
- Kan vi få denne informasjonen på en annen måte?
- Kan vi spørre om dette senere?

### 2. Verdi Må Overstige Innsats
- Tydelig verdiforslag over skjemaet
- Gjør det de får opplagt
- Reduser opplevd innsats

### 3. Reduser Kognitiv Belastning
- Ett spørsmål per felt
- Klare, samtalende labels
- Logisk gruppering og rekkefølge
- Smarte standardverdier

---

## Felt-for-Felt Optimalisering

### E-post
- Enkelt felt, ingen bekreftelse
- Inline-validering
- Skrivefeilgjenkjenning
- Riktig mobiltastatur

### Navn
- Enkelt «Navn»-felt vs. Fornavn/Etternavn — test dette
- Enkelt felt reduserer friksjon
- Deling kun nødvendig for personalisering

### Telefon
- Gjør valgfritt om mulig
- Forklar hvorfor hvis påkrevd
- Auto-formater mens de skriver
- Landskodehåndtering (+47 standard)

### Bedrift
- Auto-forslag for raskere utfylling
- Berikelse etter innsending (f.eks. via Brønnøysundregistrene)
- Vurder å utlede fra e-postdomene

### Fritekst/Kommentarer
- Gjør valgfritt
- Rimelig tegnveiledning
- Utvid ved fokus

---

## Skjematyper

### Lead Capture (Gated innhold)
- **Optimal:** 1–3 felt (e-post, ev. navn)
- Vis tydelig hva de får (forsidebilde, innholdsfortegnelse)
- «Last ned gratis» > «Send inn»

### Kontaktskjema
- **Optimal:** 3–4 felt (navn, e-post, emne, melding)
- Sett forventning for responstid
- Bekreftelsesside med neste steg

### Demo-Forespørsel
- **Optimal:** 4–6 felt (e-post, navn, bedrift, rolle)
- Vis hva som skjer etter innsending
- Tilby selvbetjent alternativ (video, gratis prøve)
- Kalenderbooking > skjema (Calendly, Cal.com)

### Checkout/Bestilling
- Minimer steg mellom beslutning og fullføring
- Vis ordresammendrag gjennom hele flyten
- Tilby gjesteutsjekking
- Vipps/betalingsalternativer reduserer friksjon

---

## Layout og UX

### Enkelt-Kolonne
- Alltid for mobil
- Anbefalt for de fleste skjemaer
- Raskere å fullføre enn multi-kolonne

### Labels
- Over feltet (ikke inne i feltet som placeholder)
- Tydelige og konsise
- Marker valgfrie felt (ikke påkrevde)

### Knapp
- Spesifikk tekst: «Få tilgang», «Bestill demo», «Last ned»
- Ikke «Send inn» eller «Submit»
- Visuelt fremtredende
- Én primærhandling

### Feilhåndtering
- Inline (ved feltet, ikke toppen)
- Vennlig tone
- Vis hva som er feil OG hvordan fikse det
- Valider fortløpende, ikke bare ved innsending

---

## Sjekkliste

- [ ] Minimum antall felt
- [ ] Hvert felt har tydelig begrunnelse
- [ ] Inline-validering på alle felt
- [ ] Fungerer godt på mobil
- [ ] CTA-tekst kommuniserer verdi
- [ ] Feilmeldinger er hjelpsomme
- [ ] Bekreftelsesside/melding etter innsending
- [ ] GDPR-samtykke der påkrevd

---

## Relaterte Skills

- `signup-flow-cro` — Registreringsskjemaer spesifikt
- `popup-cro` — Skjemaer i popups
- `page-cro` — Siden skjemaet bor på
- `ab-test-setup` — Test skjemaendringer
