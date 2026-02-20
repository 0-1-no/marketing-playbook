---
name: signup-flow-cro
description: Optimalisering av registreringsflyt — registrering, kontoopprettelse, prøveperiode-aktivering og påmelding. Aktiveres ved registreringskonvertering, registreringsfriksjon, skjemaoptimalisering for registrering, «brukere dropper av ved registrering» eller kontoopprettelse. For post-registrering onboarding, se onboarding-cro. For lead-skjemaer, se form-cro.
---

# Registreringsflyt CRO

Du er en ekspert på optimalisering av registrerings- og påmeldingsflyter. Målet er å redusere friksjon, øke fullføringsrate og sette brukere opp for vellykket aktivering.

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Tone og posisjonering
2. **Les `./marketing/JOURNEY.md`** — Evaluerings- og kjøpsfasen

---

## Kjerneprinsipp

### 1. Minimer Påkrevde Felt
Hvert felt reduserer konvertering. For hvert felt, spør:
- Trenger vi dette FØR de kan bruke produktet?
- Kan vi samle dette senere (progressiv profilering)?
- Kan vi utlede det fra annen data?

**Typisk feltprioritet:**
- Essensielt: E-post, Passord
- Ofte nødvendig: Navn
- Vanligvis utsettbart: Bedrift, Rolle, Teamstørrelse, Telefon

### 2. Vis Verdi Før Forpliktelse
- Hva kan du vise/gi før registrering kreves?
- Kan de oppleve produktet før kontoopprettelse?
- Reverser rekkefølgen: verdi først, registrering etterpå

### 3. Reduser Opplevd Innsats
- Vis fremdrift ved flersteg
- Grupper relaterte felt
- Bruk smarte standardverdier
- Forhåndsfyll når mulig

### 4. Fjern Usikkerhet
- Tydelige forventninger («Tar 30 sekunder»)
- Vis hva som skjer etter registrering
- Ingen overraskelser (skjulte krav, uventede steg)

---

## Felt-for-Felt Optimalisering

### E-postfelt
- Enkelt felt (ingen bekreftelse)
- Inline-validering for format
- Sjekk for vanlige skrivefeil (gmial.com → gmail.com)
- Tydelige feilmeldinger

### Passordfelt
- Vis passord-toggle (øye-ikon)
- Vis krav på forhånd, ikke etter feil
- Oppdater kravsindikatorer i sanntid
- Tillat liming (ikke deaktiver)
- Vurder passordløse alternativer (magic link)

### Navnfelt
- Enkelt «Fullt navn»-felt vs. Fornavn/Etternavn (test dette)
- Krev kun hvis umiddelbart brukt (personalisering)
- Vurder å gjøre valgfritt

### Sosial Innlogging
- Plasser fremtredende (ofte høyere konvertering enn e-post)
- Vis mest relevante alternativer:
  - B2C: Google, Apple
  - B2B: Google, Microsoft, SSO
- Tydelig visuelt skille fra e-postregistrering
- Vurder «Registrer med Google» som primær

---

## Flytmønstre

### Enkeltsteg vs. Flersteg

**Enkeltsteg:**
- Best for: Enkel registrering (2–3 felt)
- Fordel: Lavest friksjon
- Ulempe: Kan virke overveldende med mange felt

**Flersteg:**
- Best for: Kompleks registrering (4+ felt)
- Fordel: Redusert opplevd kompleksitet
- Ulempe: Kan miste brukere mellom steg

**Flersteg beste praksis:**
- Vis fremdriftsindikator
- Start med enkleste steg (e-post først)
- Lagre data mellom steg
- La brukere gå tilbake

### Gratisversjon vs. Prøveperiode

| Modell | Registreringsfokus |
|--------|-------------------|
| Gratis (freemium) | Minimer friksjon, aktiver raskt |
| Prøveperiode | Sett forventninger om tidsbegrensning |
| Kredittkort-krav | Høyere kvalitet, lavere volum |
| Uten kredittkort | Høyere volum, lavere kvalitet |

---

## E-postverifisering

**Beste praksis:**
- La brukere starte umiddelbart (verifiser i bakgrunnen)
- Påminnelse om verifisering i produktet
- Ikke blokker kjerneopplevelsen
- Begrens kun sensitive handlinger til verifiserte brukere

---

## Sjekkliste

- [ ] Minimum antall felt for å starte
- [ ] Sosial innlogging tilgjengelig
- [ ] Inline-validering på alle felt
- [ ] Tydelig CTA-tekst (ikke «Send inn»)
- [ ] Fungerer på mobil
- [ ] Lastetid under 2 sekunder
- [ ] Personvernlenke synlig
- [ ] Tydelig verdiforslag ved skjemaet

---

## Relaterte Skills

- `onboarding-cro` — Hva som skjer etter registrering
- `form-cro` — Skjemaoptimalisering generelt
- `page-cro` — Siden som leder til registrering
- `ab-test-setup` — Test registreringsendringer
