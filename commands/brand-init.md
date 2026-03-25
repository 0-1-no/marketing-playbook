---
description: Opprett kun BRAND.md for dette prosjektet. Bruk denne hvis du bare vil sette opp merkevare-grunnlaget (ABC-rammeverket).
disable-model-invocation: true
allowed-tools: Read, Write, Glob, AskUserQuestion
---

# Brand Init

Opprett `BRAND.md` for dette prosjektet gjennom fokusert intervju om ABC-rammeverket.

> **Når bruke denne:** Når du bare vil sette opp merkevare-grunnlaget uten kundereise og distribusjon.
> For fullstendig oppsett, bruk `/marketing-playbook:init` istedenfor.

---

## Steg 1: Sjekk eksisterende

Sjekk om `marketing/BRAND.md` finnes.

Hvis filen finnes:
```
Eksisterende BRAND.md funnet.

Vil du:
1. Overskrive (start på nytt)
2. Oppdatere basert på eksisterende
3. Avbryt
```

---

## Steg 2: Introduksjon

```
═══════════════════════════════════════════════════════════════
                       BRAND INIT
═══════════════════════════════════════════════════════════════

Jeg skal hjelpe deg med å definere merkevaren din gjennom
ABC-rammeverket:

📋 A - AUDIENCE (Hvem snakker vi til?)
📋 B - BRAND (Hva tilbyr vi?)
📋 C - COMMUNICATION (Hvordan sier vi det?)

Dette tar ca. 5-10 minutter. Du kan svare "vet ikke" på
spørsmål du er usikker på.

═══════════════════════════════════════════════════════════════
```

---

## Steg 3: Intervju

### A - AUDIENCE (Målgruppe)

**Spørsmål 1:** Hvem er hovedmålgruppen din?
- Eksempel: "Salg og BD som bygger lead-lister"
- Tips: Tenk på den personen som får mest verdi av produktet

**Spørsmål 2:** Finnes det sekundære målgrupper?
- Eksempel: "Investorer, journalister, HR"
- Svar "nei" hvis ikke relevant

**Spørsmål 3:** Hvilke problemer løser du for dem? (pain points)
- Eksempel: "Tidkrevende å manuelt sjekke tech stack"
- List gjerne flere

**Spørsmål 4:** Hva er målgruppens mål?
- Eksempel: "Bygge målrettede lead-lister raskt"
- Hva prøver de å oppnå?

**Spørsmål 5:** Hvordan ser en typisk brukssituasjon ut? (use case)
- Eksempel: "Finn alle Shopify-butikker i Norge med over 5 ansatte"
- Konkret scenario

### B - BRAND (Merkevare)

**Spørsmål 6:** Beskriv posisjoneringen i én setning
- Eksempel: "Norges smarteste bedriftsoversikt"
- Hva er dere, kort fortalt?

**Spørsmål 7:** Hva er 3-5 kjerneverdier?
- Eksempel: "Innsikt, Effektivitet, Pålitelighet"
- Hva står dere for?

**Spørsmål 8:** Hva gjør dere unike vs konkurrenter?
- Eksempel: "Tech stack crawling som ingen andre har"
- Hvorfor skal de velge dere?

**Spørsmål 9:** Hvem er hovedkonkurrentene?
- Eksempel: "Proff.no, 1881, BuiltWith"
- Og hva er deres styrker/svakheter?

### C - COMMUNICATION (Kommunikasjon)

**Spørsmål 10:** Beskriv tone of voice med 3-4 adjektiver
- Eksempel: "Profesjonell, pedagogisk, direkte, norsk"

**Spørsmål 11:** Hva er Signature Story? (Hvorfor startet dere?)
- Eksempel: "Vi så småbedriftseiere bruke søndagene på regneark..."
- Tips: Det konkrete problemet som fikk dere til å starte
- Svar "ikke definert ennå" hvis ukjent

**Spørsmål 12:** Hvilken transformasjon tilbyr dere kunden?
- Eksempel: "Fra 'jeg rekker ikke alt' til 'systemene snakker sammen av seg selv'"
- Tips: Før → Etter i kundens liv

**Spørsmål 13:** Hvilke kommunikasjonsprinsipper er viktigst for dere?
Velg 3-4:
- **Audience First** - Fokus på leser, ikke avsender
- **Less is More** - Kort og tydelig
- **Use Stories** - Fortell, ikke forklar
- **Have Opinions** - Tør å ta tydelige standpunkt
- **Adjust to Medium** - Tilpass til kanal
- **Clear Goal** - Alltid vite hva kommunikasjonen skal oppnå

**Spørsmål 14:** Hvilke ord/fraser bruker dere ofte?
- Eksempel: "Innsikt, tech stack, leads, crawlet"

**Spørsmål 15:** Hvilke ord/fraser unngår dere?
- Eksempel: "Beste, revolusjonerende, gratis, billig"
- Og hvorfor?

---

## Steg 4: Opprett BRAND.md

1. Opprett `marketing/`-mappen hvis den ikke finnes
2. Opprett `marketing/BRAND.md` basert på svarene
3. Se `examples/BRAND.md` for struktur
4. Inkluder alle ABC-elementer

---

## Steg 5: Bekreft og Neste Steg

```
═══════════════════════════════════════════════════════════════
                      ✅ BRAND.md OPPRETTET
═══════════════════════════════════════════════════════════════

📁 marketing/BRAND.md

Inneholder:
• Audience-definisjon (primary, secondary, use cases, pain points)
• Brand-posisjonering (values, differentiators, competitors)
• Communication-retningslinjer (tone, signature story, words)

───────────────────────────────────────────────────────────────
STATUS
───────────────────────────────────────────────────────────────

✅ BRAND.md      - Nettopp opprettet
[✅/❌] JOURNEY.md      - Kundereise
[✅/❌] DISTRIBUTION.md - Kanaler og stack
[✅/❌] LEARNINGS.md    - Tester og innsikter

───────────────────────────────────────────────────────────────
NESTE STEG
───────────────────────────────────────────────────────────────

[Hvis JOURNEY.md mangler:]
💡 Kjør /marketing-playbook:journey-init for kundereise

[Hvis DISTRIBUTION.md mangler:]
💡 Kjør /marketing-playbook:distribution-init for kanaler

[For fullstendig oppsett:]
💡 Kjør /marketing-playbook:init for alt på én gang

═══════════════════════════════════════════════════════════════
```
