---
name: guides
description: How-to guider, tutorials, steg-for-steg dokumentasjon og troubleshooting
content-type: guide
intent: informational
typical-length: 1500-5000 ord
seo-priority: high
aeo-priority: very high
journey-stages: consideration, post-purchase
---

# Guides & Tutorials

> **Metodikk-fil:** Faktiske verdier (tone, teknisk nivå) hentes fra `./marketing/BRAND.md` og `./marketing/CONTENT-RULES.md`.

Guider har svært høy AEO-verdi. De besvarer "Hvordan gjør jeg X?" spørsmål som AI-søk prioriterer.

---

## Guide-typer

### 1. Quick Start

**Formål:** Få brukeren i gang på kortest mulig tid

| Aspekt | Krav |
|--------|------|
| Lengde | 500-1000 ord |
| Tid | 5-10 minutter |
| Fokus | Kun det essensielle |
| Forutsetninger | Minimale |

**Struktur:**
```markdown
# Quick Start: [Produkt/Funksjon]

Kom i gang med [produkt] på under 10 minutter.

## Før du starter
- [Forutsetning 1]
- [Forutsetning 2]

## Steg 1: [Handling]
[Kort instruks]

## Steg 2: [Handling]
[Kort instruks]

## Steg 3: [Handling]
[Kort instruks]

## Ferdig!
Du har nå [oppnådd resultat]. Neste steg: [lenke til full guide]
```

---

### 2. Tutorial

**Formål:** Komplett gjennomgang av et emne

| Aspekt | Krav |
|--------|------|
| Lengde | 1500-3000 ord |
| Tid | 20-45 minutter |
| Fokus | Komplett prosess |
| Forutsetninger | Tydelig listet |

**Struktur:**
```markdown
# Hvordan [Oppnå Resultat]: Komplett Guide

Lær hvordan du [resultat] steg for steg.

**Estimert tid:** 30 minutter
**Nivå:** Nybegynner/Middels/Avansert

## Oversikt
Hva du vil lære:
- [Læringsmål 1]
- [Læringsmål 2]
- [Læringsmål 3]

## Forutsetninger
- [Hva du trenger]
- [Kunnskap du bør ha]

## Steg 1: [Handling]
### Hva vi gjør
[Forklaring]

### Hvordan
[Detaljerte instrukser]

### Forventet resultat
[Hva de bør se]

## Steg 2: [Handling]
[Samme struktur]

## Verifisering
Hvordan vet du at det fungerer?
- [ ] [Sjekk 1]
- [ ] [Sjekk 2]

## Vanlige problemer

### [Problem 1]
**Symptom:** [Hva de ser]
**Løsning:** [Hva de gjør]

## Neste steg
- [Relatert guide 1]
- [Avansert emne]
```

---

### 3. Reference / Dokumentasjon

**Formål:** Omfattende referanse for pågående bruk

| Aspekt | Krav |
|--------|------|
| Lengde | 3000-5000+ ord |
| Tid | Oppslagsverk |
| Fokus | Komplett dekning |
| Struktur | Alfabetisk eller logisk gruppering |

**Struktur:**
```markdown
# [Emne] Reference

Komplett referanse for [emne].

## Innholdsfortegnelse
- [Seksjon 1](#seksjon-1)
- [Seksjon 2](#seksjon-2)

## Seksjon 1

### [Konsept A]
[Definisjon og bruk]

**Syntaks/Format:**
```
[eksempel]
```

**Parametre:**
| Parameter | Type | Beskrivelse |
|-----------|------|-------------|
| param1 | string | [beskrivelse] |

**Eksempler:**
[Praktiske eksempler]

## Seksjon 2
[Samme struktur]

## Se også
- [Relatert dokumentasjon]
```

---

### 4. Troubleshooting

**Formål:** Løse spesifikke problemer

| Aspekt | Krav |
|--------|------|
| Lengde | 1000-2000 ord |
| Format | Problem → Årsak → Løsning |
| Fokus | Vanlige issues |
| Struktur | Søkbar, scannable |

**Struktur:**
```markdown
# Troubleshooting: [Område]

Løsninger på vanlige problemer med [område].

## Problem: [Beskrivende tittel]

### Symptomer
- [Hva brukeren ser]
- [Feilmelding hvis relevant]

### Mulige årsaker
1. [Årsak 1]
2. [Årsak 2]

### Løsninger

#### Løsning 1: [Tittel]
1. [Steg 1]
2. [Steg 2]

#### Løsning 2: [Tittel]
[Hvis løsning 1 ikke fungerer]

### Fortsatt problemer?
[Kontakt support / eskaleringsvei]
```

---

## Guide-struktur Template

```markdown
# [Tittel med handlingsverb]

[Hook: 1-2 setninger om hva de oppnår]

**Estimert tid:** [X] minutter
**Nivå:** Nybegynner / Middels / Avansert
**Sist oppdatert:** [dato]

## TL;DR

[40-60 ord oppsummering for de som har det travelt]

## Oversikt

Etter denne guiden vil du kunne:
- [Konkret læringsmål 1]
- [Konkret læringsmål 2]
- [Konkret læringsmål 3]

## Forutsetninger

Før du starter, sørg for at du har:
- [ ] [Forutsetning 1]
- [ ] [Forutsetning 2]
- [ ] [Kunnskap/tilgang som trengs]

---

## Steg 1: [Handlingsverb + Hva]

[1-2 setninger kontekst]

### Hva du gjør

[Instruksjon]

```
[Kode/kommando hvis relevant]
```

### Forventet resultat

[Hva de bør se/oppleve]

> **Tips:** [Nyttig hint]

---

## Steg 2: [Handlingsverb + Hva]

[Samme struktur som steg 1]

---

## Steg 3: [Handlingsverb + Hva]

[Samme struktur]

---

## Verifisering

Sjekk at alt fungerer:

- [ ] [Verifikasjonssjekk 1]
- [ ] [Verifikasjonssjekk 2]
- [ ] [Verifikasjonssjekk 3]

**Forventet sluttresultat:**
[Beskrivelse eller skjermbilde]

---

## Troubleshooting

### [Vanlig problem 1]

**Symptom:** [Hva de ser]

**Løsning:**
1. [Steg]
2. [Steg]

### [Vanlig problem 2]

**Symptom:** [Hva de ser]

**Løsning:**
[Løsning]

---

## Neste steg

Du har nå [oppnådd X]. Her er hva du kan gjøre videre:

- [Relatert guide 1] - [kort beskrivelse]
- [Avansert emne] - [kort beskrivelse]
- [Annen ressurs] - [kort beskrivelse]

---

## FAQ

### [Spørsmål 1]?

[40-60 ord svar]

### [Spørsmål 2]?

[40-60 ord svar]

---

*Har du spørsmål? [Kontakt support]*
```

---

## Steg-skrivingsregler

### Én handling per steg

**Dårlig:**
```
## Steg 1: Logg inn og naviger til innstillinger

Logg inn på kontoen din, klikk på profilikonet øverst til høyre,
velg "Innstillinger" fra menyen, og gå til "Integrasjoner".
```

**Godt:**
```
## Steg 1: Logg inn på kontoen din

Gå til [URL] og logg inn med din e-post og passord.

## Steg 2: Åpne Innstillinger

Klikk på profilikonet øverst til høyre → velg "Innstillinger".

## Steg 3: Naviger til Integrasjoner

I sidemenyen, klikk på "Integrasjoner".
```

### Start med handlingsverb

| Godt | Unngå |
|------|-------|
| Klikk på... | Du må klikke på... |
| Åpne... | Det neste steget er å åpne... |
| Skriv inn... | Her skal du skrive inn... |
| Velg... | Nå velger du... |

### Inkluder forventet resultat

```markdown
## Steg 4: Lagre endringene

Klikk på "Lagre" nederst på siden.

**Du bør se:** En grønn bekreftelsesmelding: "Innstillinger lagret"
```

### Vis, ikke bare fortell

- Inkluder skjermbilder for UI-steg
- Bruk kodeblokker for kommandoer
- Vis eksempel-output
- Highlight relevante elementer

---

## AEO-optimalisering for guider

### HowTo Schema

Guider bør ha HowTo schema markup for AI-synlighet.

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "[Tittel]",
  "description": "[Beskrivelse]",
  "totalTime": "PT30M",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Steg 1: [Tittel]",
      "text": "[Instruksjon]",
      "image": "[URL til bilde]"
    }
  ]
}
```

Se [STRUCTURED-DATA.md](../seo-aeo/STRUCTURED-DATA.md) for full implementering.

### Answer blocks i guider

Hver seksjon bør inneholde et 40-60 ord svar som kan siteres.

**I TL;DR:**
```markdown
## TL;DR

For å sette opp [X], trenger du først [A], deretter [B], og
til slutt [C]. Hele prosessen tar ca. 15 minutter. Det viktigste
er å [kritisk punkt] - hopp ikke over dette steget.
```

**I seksjonsintro:**
```markdown
## Steg 3: Konfigurer integrasjonen

Integrasjonskonfigurasjonen kobler [X] med [Y] slik at data
flyter automatisk. Du trenger API-nøkkel fra [kilde] og
tilgang til admin-panelet i [mål]. Dette tar ca. 5 minutter.
```

### FAQ i guider

Alltid inkluder en FAQ-seksjon med vanlige spørsmål.

```markdown
## FAQ

### Hvor lang tid tar dette?

Hele prosessen tar vanligvis 15-30 minutter, avhengig av
kompleksiteten i oppsettet ditt. Quick Start-versjonen
kan gjøres på under 10 minutter.

### Hva om jeg gjør feil?

Du kan alltid angre eller starte på nytt. Alle endringer
kan reverseres i innstillingene under [sti].

### Trenger jeg teknisk erfaring?

Nei, denne guiden er laget for nybegynnere. Alle steg
forklares i detalj med skjermbilder.
```

---

## Skannbarhet for lange guider

### Innholdsfortegnelse

For guider over 1500 ord, inkluder alltid ToC:

```markdown
## Innholdsfortegnelse

- [Oversikt](#oversikt)
- [Forutsetninger](#forutsetninger)
- [Steg 1: Oppsett](#steg-1-oppsett)
- [Steg 2: Konfigurasjon](#steg-2-konfigurasjon)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
```

### Estimert tid

```markdown
**Estimert tid:** 30 minutter
```

Eller per seksjon:
```markdown
## Steg 3: Database-oppsett (10 min)
```

### Sjekkliste-format

For handlingsbaserte guider:

```markdown
## Forutsetninger-sjekkliste

- [ ] Node.js 18+ installert
- [ ] Git konfigurert
- [ ] API-nøkkel fra [tjeneste]
- [ ] Admin-tilgang til prosjektet
```

### Fremdriftsindikatorer

```markdown
## Steg 2 av 5: Konfigurasjon
```

Eller visuelt:
```markdown
Fremgang: ████░░░░░░ 40%
```

---

## Nivåtilpasning

### Nybegynner

- Forklar alle begreper
- Inkluder "Hva er X?" bokser
- Flere skjermbilder
- Detaljerte steg
- Unngå forkortelser

```markdown
> **Hva er en API-nøkkel?**
> En API-nøkkel er en unik kode som identifiserer deg
> når du kobler to systemer sammen. Tenk på det som
> et passord mellom applikasjoner.
```

### Middels

- Anta grunnleggende kunnskap
- Fokuser på prosessen
- Færre forklaringer, mer handling
- Inkluder alternativer

### Avansert

- Anta ekspertise
- Fokuser på edge cases
- Inkluder optimalisering
- Vis avanserte teknikker

---

## Guide-sjekkliste

### Struktur
- [ ] Klar tittel med handlingsverb
- [ ] Estimert tid inkludert
- [ ] Nivå angitt
- [ ] TL;DR/oppsummering
- [ ] Innholdsfortegnelse (hvis >1500 ord)
- [ ] Forutsetninger listet
- [ ] Nummererte steg
- [ ] Verifisering/suksessjekk
- [ ] Troubleshooting-seksjon
- [ ] Neste steg / relaterte guider
- [ ] FAQ-seksjon

### Steg-kvalitet
- [ ] Én handling per steg
- [ ] Starter med handlingsverb
- [ ] Forventet resultat beskrevet
- [ ] Visuell støtte (skjermbilder, kode)
- [ ] Tips/warnings der relevant

### AEO
- [ ] Answer blocks (40-60 ord) i nøkkelseksjoner
- [ ] FAQ med direkte svar
- [ ] HowTo schema implementert
- [ ] Klar definisjon i intro

### Voice
- [ ] Matcher teknisk nivå i CONTENT-RULES.md
- [ ] Konsistent bruk av "du" eller "vi"
- [ ] Ingen jargon uten forklaring (for nybegynnere)

---

## Vanlige feil å unngå

### For lange steg
**Dårlig:** Ett steg med 5 handlinger
**Godt:** 5 separate steg

### Manglende forventet resultat
**Dårlig:** "Klikk Lagre"
**Godt:** "Klikk Lagre. Du ser en grønn bekreftelse."

### Antatt kunnskap
**Dårlig:** "Konfigurer CORS-headerne"
**Godt:** "Legg til CORS-headere (se boks under for forklaring)"

### Ingen troubleshooting
**Dårlig:** Bare "happy path"
**Godt:** Inkluder 3-5 vanlige problemer

### Utdatert informasjon
**Dårlig:** Skjermbilder fra gammel versjon
**Godt:** Oppdaterte skjermbilder med "Sist oppdatert: [dato]"

---

## Integrasjonspunkter

| Trenger du... | Les... |
|---------------|--------|
| AEO-optimalisering | [AEO.md](../seo-aeo/AEO.md) |
| HowTo schema | [STRUCTURED-DATA.md](../seo-aeo/STRUCTURED-DATA.md) |
| Teknisk skriving | CONTENT-RULES.md → Teknisk dybde |
| Research for komplekse guider | [RESEARCH-PROCESS.md](RESEARCH-PROCESS.md) |
| Humanisering | [ANTI-SLOP.md](ANTI-SLOP.md) |
