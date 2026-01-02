# Microcopy

De små tekstene som gjør stor forskjell: buttons, labels, errors, empty states.

---

## Hva er Microcopy

Microcopy er de korte tekstbitene i et grensesnitt:
- Button-tekst
- Form labels og hints
- Error messages
- Empty states
- Loading messages
- Confirmation dialogs
- Tooltips

---

## Prinsipper

### 1. Klarhet > Personlighet

Når du må velge, velg alltid klarhet.

| Uklart | Klart |
|--------|-------|
| "Kom i gang!" | "Opprett konto" |
| "La oss gjøre dette" | "Send bestilling" |
| "Hmm, noe gikk galt" | "Betalingen mislyktes" |

### 2. Handling, ikke objekt

Fokuser på hva brukeren gjør, ikke hva de interagerer med.

| Objekt-fokus | Handling-fokus |
|--------------|----------------|
| "Skjema" | "Send" |
| "Abonnement" | "Bli medlem" |
| "Passord" | "Logg inn" |

### 3. Konsistens

Bruk samme ord for samme handling overalt.

- Ikke bytt mellom "Slett", "Fjern", "Ta bort"
- Velg ett og hold deg til det

---

## Button-tekst

### Primær CTA

- Start med verb
- Vær spesifikk
- Indiker resultatet

| Svak | Sterk |
|------|-------|
| "Submit" | "Send søknad" |
| "Next" | "Gå til betaling" |
| "OK" | "Bekreft bestilling" |

### Sekundær CTA

- Tydeliggjør forskjellen fra primær
- Ikke "Avbryt" hvis handlingen er reversibel

| Situasjon | Primær | Sekundær |
|-----------|--------|----------|
| Lagre endringer | "Lagre" | "Forkast endringer" |
| Slette konto | "Slett permanent" | "Behold kontoen" |

---

## Error Messages

### Struktur

1. **Hva skjedde** - Kort beskrivelse
2. **Hvorfor** - Hvis relevant
3. **Hva gjøre** - Løsning eller neste steg

### Eksempler

| Dårlig | Bra |
|--------|-----|
| "Error 500" | "Vi har tekniske problemer. Prøv igjen om noen minutter." |
| "Invalid input" | "E-postadressen ser ikke riktig ut. Sjekk at den inneholder @." |
| "Failed" | "Betalingen ble avvist av banken. Prøv et annet kort." |

### Tone

- Unngå å skylde på brukeren
- Vær hjelpsom, ikke teknisk
- Ved alvorlige feil: vis empati

---

## Empty States

Når det ikke er noe innhold ennå.

### Struktur

1. **Bekreft tilstanden** - "Ingen prosjekter ennå"
2. **Forklar verdien** - Hva vil de se her?
3. **Vis vei videre** - Tydelig CTA

### Eksempel

> **Ingen fakturaer ennå**
>
> Her vil du se alle fakturaer du sender. Når kunder betaler, oppdateres statusen automatisk.
>
> [Opprett din første faktura]

---

## Loading & Progress

### Kort ventetid (<3 sek)

- Enkel spinner eller indikator
- Ingen tekst nødvendig

### Lengre ventetid

- Vis hva som skjer: "Laster inn data..."
- Hvis mulig, vis progresjon: "3 av 5 filer lastet"

### Veldig lang ventetid

- Sett forventning: "Dette kan ta opptil 2 minutter"
- Tillat å gjøre andre ting: "Vi sender e-post når det er ferdig"

---

## Confirmation Dialogs

### Destruktive handlinger

Vær tydelig på konsekvensene.

```
Slett prosjektet "Kundelansering"?

Alt innhold, filer og historikk blir slettet permanent.
Dette kan ikke angres.

[Avbryt]  [Slett permanent]
```

### Viktige handlinger

Bekreft hva som vil skje.

```
Publiser endringer?

Artikkelen blir synlig for alle besøkende.

[Avbryt]  [Publiser nå]
```

---

## Personality vs Klarhet

### Når personlighet fungerer

- Onboarding og velkomst
- Suksessmeldinger
- Ikke-kritiske steder

### Når klarhet må vinne

- Feilmeldinger
- Betalingsflyt
- Destruktive handlinger
- Komplekse oppgaver

---

## Vanlige Feil

- **"Click here"** - Linkteksten bør beskrive destinasjonen
- **"Error"** uten forklaring - Hjelp brukeren
- **Alle caps** - Virker som du roper
- **Dobbel negasjon** - "Ikke avbryt" (forvirrende)
- **Teknisk sjargong** - "Invalid token" (hvem vet hva det betyr?)
