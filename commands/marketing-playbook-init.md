---
description: Initialize Marketing Playbook for this project. Creates BRAND.md with Audience, Brand, and Communication sections through interactive setup.
allowed-tools: Read, Write, Glob, AskUserQuestion
---

# Marketing Playbook - Init

Opprett `BRAND.md` for dette prosjektet gjennom interaktiv oppsett.

## Steg 1: Sjekk eksisterende

Sjekk om `BRAND.md` allerede finnes.

Hvis ja, spør:
```
BRAND.md finnes allerede.

Vil du:
1. Overskrive helt (starter på nytt)
2. Oppdatere eksisterende (behold struktur)
3. Avbryt
```

## Steg 2: Interaktiv oppsett

```
═══════════════════════════════════════════
   MARKETING PLAYBOOK - INIT
═══════════════════════════════════════════

La oss sette opp BRAND.md for dette prosjektet.
Jeg stiller deg noen spørsmål om ABC:

• Audience - Hvem snakker vi til?
• Brand - Hva tilbyr vi?
• Communication - Hvordan sier vi det?

═══════════════════════════════════════════
```

Still følgende spørsmål (bruk AskUserQuestion):

### A - AUDIENCE

**Spørsmål 1:** Hvem er hovedmålgruppen?
- Eksempel: "Salg og BD som bygger lead-lister"

**Spørsmål 2:** Hvilke problemer løser du for dem? (pain points)
- Eksempel: "Tidkrevende å manuelt sjekke tech stack"

**Spørsmål 3:** Hva er deres mål?
- Eksempel: "Bygge målrettede lead-lister raskt"

### B - BRAND

**Spørsmål 4:** Beskriv posisjoneringen i én setning
- Eksempel: "Norges smarteste bedriftsoversikt"

**Spørsmål 5:** Hva er 3-5 kjerneverdier?
- Eksempel: "Innsikt, Effektivitet, Pålitelighet"

**Spørsmål 6:** Hva gjør dere unike vs konkurrenter?
- Eksempel: "Tech stack crawling, MCP-integrasjon"

### C - COMMUNICATION

**Spørsmål 7:** Beskriv tone of voice (3-4 adjektiver)
- Eksempel: "Profesjonell, pedagogisk, direkte"

**Spørsmål 8:** Hvilke ord/fraser bruker dere ofte?
- Eksempel: "Innsikt, tech stack, leads"

**Spørsmål 9:** Hvilke ord/fraser unngår dere?
- Eksempel: "Beste, revolusjonerende, gratis"

## Steg 3: Generer BRAND.md

Basert på svarene, generer komplett `BRAND.md`:

```markdown
# [Prosjektnavn] Brand

> Marketing Playbook for [prosjektnavn]. Denne filen brukes av Claude for å sikre konsistent kommunikasjon.

---

## Audience

**Primary:** [svar 1]
**Secondary:** [eventuelt utledet]

### Use Cases
- [utledet fra pain points og mål]

### Pain Points
- [svar 2 som liste]

### Goals
- [svar 3 som liste]

---

## Brand

**Positioning:** [svar 4]

**Mission:** [utledet fra kontekst]

**Values:**
1. **[verdi]** - [kort beskrivelse]
...

**Personality:**
- [fra tone of voice]

**Differentiators:**
- **[differentiator]** - [beskrivelse]
...

---

## Communication

### Tone of Voice
- **[adjektiv]** - [hva det betyr i praksis]
...

### Key Messages
1. "[utledet hovedbudskap]"
...

### Words We Use
- [svar 8 som liste]

### Words We Avoid
- [svar 9] (med begrunnelse)
...

---

*Sist oppdatert: [dagens dato]*
```

## Steg 4: Bekreft

```
✅ BRAND.md opprettet!

Fil: ./BRAND.md

───────────────────────────────────────────
NESTE STEG
───────────────────────────────────────────

1. Review BRAND.md og juster detaljer
2. Bruk /marketing-playbook:check før du publiserer innhold
3. Kjør /marketing-playbook:audit for full gjennomgang

───────────────────────────────────────────
```
