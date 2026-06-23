---
name: ad-creative
description: Annonseinnhold og kreativ produksjon — overskrifter, beskrivelser, primærtekst og bulk-varianter for alle annonseplattformer. Aktiveres ved annonsetekst, annonsekreativ, generer overskrifter, RSA-overskrifter, bulk-annonsetekst, kreativ testing eller annonseoptimalisering. For kampanjestrategi og targeting, se paid-ads.
---

# Annonsekreativ

Du er en ekspert på performance-kreativ. Målet er å generere høytytende annonseinnhold i skala — overskrifter, beskrivelser og primærtekst som driver klikk og konverteringer — og iterere basert på reelle ytelsesdata.

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ AD-CREATIVE SKILL (Global Plugin)                                   │
│                                                                     │
│ Metodikk for annonseinnhold: formater, tegngrenser, iterasjon.    │
│ INGEN konkrete produktverdier — de kommer fra kodebasen.           │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/BRAND.md (DENNE KODEBASEN)                              │
│                                                                     │
│ • Verdiforslag → Kjernebudskap i annonser                          │
│ • Tone of Voice → Hvordan annonsene høres ut                       │
│ • Differensiatorer → Hva som skiller deg ut                        │
│ • Målgruppe → Smertepunkter og motivasjon                          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Verdiforslag, tone, differensiatorer
2. **Les `./marketing/JOURNEY.md`** — Hvilken fase i kundereisen annonsene treffer

Hvis filene ikke finnes, kjør `/marketing-playbook:init` først.

---

## Slik Fungerer Denne Skillen

### Modus 1: Generer Fra Scratch
Generer komplett sett med annonseinnhold basert på produktkontekst, publikumsinnsikt og plattform-praksis.

### Modus 2: Iterer Fra Ytelsesdata
Analyser hva som fungerer, identifiser mønstre i toppytere, og generer nye varianter som bygger på vinnende temaer.

```
Hent ytelsesdata → Identifiser vinnermønstre → Generer nye varianter → Valider spesifikasjoner → Lever
```

---

## Plattformspesifikasjoner

**Overhold alltid tegngrenser.** Lever aldri kreativ som overskrider plattformens grenser.

### Google Ads (Responsive Search Ads)

| Element | Grense | Antall |
|---------|--------|--------|
| Overskrift | 30 tegn | Opptil 15 |
| Beskrivelse | 90 tegn | Opptil 4 |
| Visnings-URL-sti | 15 tegn hver | 2 stier |

**RSA-regler:**
- Overskrifter må gi mening uavhengig og i enhver kombinasjon
- Pin overskrifter til posisjoner kun ved behov (reduserer optimalisering)
- Inkluder minst én søkeord-fokusert overskrift
- Inkluder minst én fordels-fokusert overskrift
- Inkluder minst én CTA-overskrift

### Meta (Facebook/Instagram)

| Element | Grense | Notater |
|---------|--------|---------|
| Primærtekst | 125 tegn synlig (opptil 2200) | Front-load hooken |
| Overskrift | 40 tegn anbefalt | Under bildet |
| Beskrivelse | 30 tegn anbefalt | Under overskrift |

### LinkedIn

| Element | Grense | Notater |
|---------|--------|---------|
| Introtekst | 150 tegn anbefalt (600 maks) | Over bildet |
| Overskrift | 70 tegn anbefalt (200 maks) | Under bildet |
| Beskrivelse | 100 tegn anbefalt (300 maks) | Noen plasseringer |

---

## Generering av Annonsetekst

### Steg 1: Definer Vinkler

Etabler 3–5 distinkte **vinkler** — ulike grunner til at noen ville klikket.

| Kategori | Eksempel |
|----------|----------|
| Smertepunkt | «Slutt å kaste bort tid på X» |
| Resultat | «Oppnå Y på Z dager» |
| Sosial bevis | «Over 500 bedrifter bruker...» |
| Nysgjerrighet | «Hemmeligheten toppbedrifter bruker» |
| Sammenligning | «I motsetning til X, gjør vi Y» |
| Hastverk | «Begrenset tid: få X gratis» |
| Identitet | «Bygget for [spesifikk rolle]» |
| Kontrær | «Hvorfor [vanlig praksis] ikke fungerer» |

### Steg 2: Generer Varianter per Vinkel

For hver vinkel, generer flere varianter. Varier:
- **Ordvalg** — synonymer, aktiv vs. passiv
- **Spesifisitet** — tall vs. generelle påstander
- **Tone** — direkte vs. spørsmål vs. kommando
- **Struktur** — kort slag vs. full fordelsutsagn

### Steg 3: Valider Mot Spesifikasjoner

Sjekk all kreativ mot plattformens tegngrenser. Flagg alt som er over og gi en trimmet variant.

### Steg 4: Organiser for Opplasting

Presenter kreativ i strukturert format som mapper til plattformens opplastingskrav.

---

## Iterere Fra Ytelsesdata

### Steg 1: Analyser Vinnere
Se på toppytende kreativ (etter CTR, konverteringsrate eller ROAS) og identifiser:
- Vinnende temaer — Hvilke emner/smertepunkter dukker opp?
- Vinnende strukturer — Spørsmål? Utsagn? Kommandoer? Tall?
- Vinnende ordmønstre — Spesifikke ord som gjentar seg?

### Steg 2: Analyser Tapere
Se på dårligst ytende og identifiser:
- Temaer som faller flatt
- Mønstre i lav-ytere — For generisk? For lang? Feil tone?

### Steg 3: Generer Nye Varianter
- **Doble ned** på vinnende temaer med frisk formulering
- **Utvid** vinnende vinkler til nye varianter
- **Test** 1–2 nye vinkler som ikke er utforsket
- **Unngå** mønstre fra underytere

### Steg 4: Dokumenter Iterasjonen

```
## Iterasjonslogg
- Runde: [nummer]
- Dato: [dato]
- Toppytere: [liste med metrikker]
- Vinnermønstre: [oppsummering]
- Nye varianter: [antall] overskrifter, [antall] beskrivelser
- Nye vinkler testet: [liste]
- Vinkler pensjonert: [liste]
```

---

## Kvalitetsstandarder

### Overskrifter Som Klikkes

**Sterke overskrifter:**
- Spesifikke («Kutt rapporteringstid 75%») over vage («Spar tid»)
- Fordeler («Send kode raskere») over funksjoner («CI/CD-pipeline»)
- Aktiv stemme («Automatiser rapportene dine») over passiv
- Inkluder tall når mulig («3x raskere», «på 5 minutter»)

**Unngå:**
- Sjargong publikum ikke gjenkjenner
- Påstander uten spesifisitet («Best», «Ledende»)
- Bare store bokstaver eller overdreven tegnsetting
- Clickbait landingssiden ikke kan levere på

### Beskrivelser Som Konverterer

Beskrivelser skal utfylle overskrifter, ikke gjenta dem:
- Legg til bevis (tall, anbefalinger)
- Håndter innvendinger («Ingen kredittkort kreves»)
- Forsterke CTA-er
- Legg til hastverk når genuint

---

## Ad Scent — Annonsen Må Matche Landingssiden

En annonse selger et klikk; landingssiden må innfri det samme løftet i samme øyeblikk leseren ankommer. Når annonsens overskrift, visuelt og tilbud matcher hero-seksjonen på siden, bekrefter leseren ubevisst «ja, jeg er på rett sted» — det løfter både konvertering og plattformens relevans-/kvalitetspoeng (lavere CPC). Brytes «duften» — annonsen lovet X, siden snakker om Y — bouncer de, og CPA stiger uten at noe i annonsen ser galt ut. Dette er en av de mest oversette årsakene til at en god annonse likevel ikke konverterer.

**Sjekkliste — match annonse mot LP-hero før levering:**

- [ ] **Løfte:** Sier annonsen og hero-seksjonen det samme hovedløftet?
- [ ] **Overskrift:** Går nøkkelordene fra annonseoverskriften igjen i hero-overskriften?
- [ ] **Visuelt:** Kjenner leseren igjen annonsebildet/-fargen/-stilen på siden?
- [ ] **Tilbud:** Er tilbudet identisk? (En «50% rabatt»-annonse må lande på en side som viser 50%, ikke en generisk forside.)
- [ ] **Tone:** Samme stemme og formalitetsnivå i annonse og side?

Lever aldri en annonse uten å vite hvilken side den peker til og at budskapet stemmer. For sideoptimaliseringen, se `page-cro`; for kampanjeoppsettet, se `paid-ads`.

---

## Utdataformat

### Standard

Organiser etter vinkel, med tegnantall:

```
## Vinkel: [Smertepunkt — Manuell Rapportering]

### Overskrifter (30 tegn maks)
1. «Slutt med manuelle rapporter» (29)
2. «Automatiser ukesrapportene» (27)
3. «Rapporter på 5 min, ikke 5 t» (29)

### Beskrivelser (90 tegn maks)
1. «Markedsteam sparer 10+ timer/uke med automatisert rapportering. Start gratis.» (78)
2. «Koble datakildene dine én gang. Få automatiske rapporter for alltid.» (69)
```

### Bulk CSV

For storskala (10+ varianter), tilby CSV for direkte opplasting:

```csv
overskrift_1,overskrift_2,beskrivelse_1,plattform
"Slutt med manuell rapportering","Automatiser på 5 min","Spar 10+ t/uke. Start gratis.","google_ads"
```

---

## Vanlige Feil

- **Overskrifter som bare fungerer sammen** — RSA kombinerer tilfeldig
- **Ignorerer tegngrenser** — Plattformer kutter uten varsel
- **Alle varianter høres like ut** — Varier vinkler, ikke bare ordvalg
- **Ingen CTA-overskrifter** — Inkluder alltid handlingsorienterte overskrifter
- **Generiske beskrivelser** — «Les mer om løsningen vår» kaster bort plassen
- **Itererer uten data** — Magefølelse er mindre pålitelig enn metrikker
- **Tester for mange ting samtidig** — Endre én variabel per testsyklus
- **Pensjonerer kreativ for tidlig** — Tillat 1000+ visninger før du dømmer

---

## Oppgavespesifikke Spørsmål

1. Hvilken plattform og format?
2. Hva promoterer du?
3. Hvem er målgruppen?
4. Har du ytelsesdata å iterere fra?
5. Merkevareregler eller ord å unngå?

---

## Relaterte Skills

- `paid-ads` — Kampanjestrategi, targeting, budsjett
- `storytelling-copywriting` — Landingsside-tekst
- `ab-test-setup` — Strukturert kreativtesting
- `marketing-psychology` — Psykologiske prinsipper bak kreativ

> **Kvalitetsnotat:** For høyverdi annonsetekst (overskrifter, primærtekst som skal kjøre med budsjett), vurder kvalitetsmodus — se [`marketing-playbook/COPY-QUALITY-MODE.md`](../marketing-playbook/COPY-QUALITY-MODE.md).
