---
description: Initialize Marketing Playbook for this project. Creates BRAND.md, JOURNEY.md, DISTRIBUTION.md, and LEARNINGS.md through interactive deep-dive setup.
disable-model-invocation: true
allowed-tools: Read, Write, Glob, AskUserQuestion
---

# Marketing Playbook - Init

Opprett `BRAND.md`, `JOURNEY.md`, `DISTRIBUTION.md` og `LEARNINGS.md` for dette prosjektet gjennom interaktivt intervju.

> **VIKTIG INSTRUKSJON:** Denne kommandoen oppretter filer UNDERVEIS, ikke på slutten.
> Etter hver DEL skal du umiddelbart opprette den tilhørende filen før du går videre.
> Dette sikrer at alle filer blir opprettet selv om samtalen avbrytes.

---

## Arkitektur-påminnelse

```
┌─────────────────────────────────────────────────────────────────────┐
│ DU ER HER: Kjører init i en spesifikk kodebase                     │
│                                                                     │
│ Marketing Playbook (plugin) = Rammeverk og metodikk                │
│ ./marketing/ (denne kodebasen) = Skreddersydde verdier            │
│                                                                     │
│ Alt du samler inn nå skal handle om DETTE PROSJEKTET.              │
│ Ikke generelle prinsipper - konkrete verdier for denne merkevaren. │
└─────────────────────────────────────────────────────────────────────┘
```

**Fokus:** Spør om og dokumenter verdier som er spesifikke for denne kodebasen og merkevaren den representerer.

---

## Steg 1: Sjekk eksisterende

Sjekk om `marketing/`-mappen finnes med `BRAND.md`, `JOURNEY.md`, `DISTRIBUTION.md` eller `LEARNINGS.md`.

Akseptable plasseringer (i prioritert rekkefølge):
1. `marketing/` (anbefalt)
2. Prosjekt-rot (legacy - migrer til marketing/)

Hvis filer finnes, spør:
```
Eksisterende filer funnet:
- marketing/BRAND.md: [Ja/Nei]
- marketing/JOURNEY.md: [Ja/Nei]
- marketing/DISTRIBUTION.md: [Ja/Nei]
- marketing/LEARNINGS.md: [Ja/Nei]

Vil du:
1. Overskrive alt (starter på nytt)
2. Kun oppdatere BRAND.md
3. Kun oppdatere JOURNEY.md
4. Kun oppdatere DISTRIBUTION.md
5. Kun oppdatere LEARNINGS.md
6. Avbryt
```

Hvis filer finnes i rot (legacy), tilby migrering:
```
Fant filer i prosjekt-rot (legacy plassering):
- BRAND.md
- JOURNEY.md

Vil du migrere til marketing/-mappen? (anbefalt)
```

## Steg 2: Introduksjon

```
═══════════════════════════════════════════════════════════════
                    MARKETING PLAYBOOK - INIT
═══════════════════════════════════════════════════════════════

Velkommen! Jeg skal hjelpe deg med å sette opp Marketing Playbook.

Vi går gjennom fire deler:

📋 DEL 1: BRAND.md (ABC-rammeverket)
   • Audience - Hvem snakker vi til?
   • Brand - Hva tilbyr vi?
   • Communication - Hvordan sier vi det?

🗺️ DEL 2: JOURNEY.md (Kundereisen)
   • Hvordan oppdager kunder deg?
   • Hva vurderer de før kjøp?
   • Hvordan ser opplevelsen ut etterpå?

📡 DEL 3: DISTRIBUTION.md (Kanaler & Stack)
   • Hvilke verktøy bruker dere?
   • Hvor er dere til stede?
   • Hva fungerer best?

🧪 DEL 4: LEARNINGS.md (Validering)
   • Brand Audience Fit - Resonerer det?
   • Tester og resultater
   • Hva fungerer og hva fungerer ikke?

Dette tar ca. 15-20 minutter. Du kan svare "vet ikke" eller
"ikke relevant ennå" på spørsmål du er usikker på.

═══════════════════════════════════════════════════════════════
```

---

## DEL 1: BRAND.md

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
Velg 3-4 som beskriver hvordan dere kommuniserer:
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

## ✅ CHECKPOINT: Opprett BRAND.md

**STOPP HER og opprett filen UMIDDELBART før du fortsetter til DEL 2.**

```
═══════════════════════════════════════════════════════════════
                    ✅ OPPRETTER BRAND.md
═══════════════════════════════════════════════════════════════

[████░░░░░░░░░░░░] 25% - BRAND.md

Basert på svarene i DEL 1, oppretter jeg nå marketing/BRAND.md...

═══════════════════════════════════════════════════════════════
```

1. Opprett `marketing/`-mappen hvis den ikke finnes
2. Opprett `marketing/BRAND.md` basert på svarene fra DEL 1
3. Se `examples/BRAND.md` for struktur
4. Inkluder alle ABC-elementer:
   - Audience: primary, secondary, use cases, pain points, goals
   - Brand: positioning, values, differentiators, competitors
   - Communication: tone, signature story, principles, words we use/avoid
5. Bekreft for brukeren:

```
✅ BRAND.md opprettet!

📁 marketing/BRAND.md

Inneholder:
• Audience-definisjon
• Brand-posisjonering
• Communication-retningslinjer

Fortsetter til DEL 2: JOURNEY.md...
───────────────────────────────────────────────────────────────
```

---

## DEL 2: JOURNEY.md

```
───────────────────────────────────────────────────────────────
                      🗺️ KUNDEREISEN
───────────────────────────────────────────────────────────────

Nå kartlegger vi hvordan kunder opplever dere fra første
kontakt til lojal kunde.

Svar så godt du kan. "Vet ikke ennå" er helt OK for nye merkevarer.
───────────────────────────────────────────────────────────────
```

### Awareness (Oppdagelse)

**Spørsmål 16:** Hvordan oppdager folk dere typisk?
- Eksempler: "Google-søk, sosiale medier, word-of-mouth, annonser"
- Hvilke kanaler er viktigst?

**Spørsmål 17:** Hva er det første inntrykket du vil gi?
- Hva skal de tenke/føle når de først ser dere?

**Spørsmål 18:** Hva er den største barrieren for å få oppmerksomhet?
- Eksempel: "Mange konkurrenter", "Ukjent kategori", "Lav awareness"

### Consideration (Vurdering)

**Spørsmål 19:** Hva vurderer kundene før de bestemmer seg?
- Eksempel: "Pris, funksjoner, reviews, tillit"

**Spørsmål 20:** Hvilke spørsmål stiller de seg?
- Eksempel: "Er dette verdt prisen?", "Passer det for meg?"

**Spørsmål 21:** Hvilke bekymringer har de?
- Eksempel: "For dyrt", "Komplisert å bruke", "Usikker på kvalitet"

**Spørsmål 22:** Hvordan bygger dere tillit?
- Eksempel: "Reviews, case studies, gratis prøve, garantier"

### Purchase (Kjøp)

**Spørsmål 23:** Hvordan kjøper kundene? (kjøpsprosessen)
- Eksempel: "Online checkout", "Kontakt salg", "Freemium → betalt"

**Spørsmål 24:** Hva er de største friksjonspunktene i kjøpet?
- Eksempel: "Komplisert checkout", "Manglende betalingsalternativer"

### Post-purchase (Etter kjøp)

**Spørsmål 25:** Hva skjer rett etter kjøp?
- Eksempel: "Velkomst-e-post, onboarding, levering"

**Spørsmål 26:** Hva kan skape kjøpsanger?
- Eksempel: "Lang leveringstid", "Vanskelig å komme i gang"

**Spørsmål 27:** Hvordan sikrer dere en god opplevelse?
- Eksempel: "Rask support, god dokumentasjon, overraskelser"

### Loyalty (Lojalitet)

**Spørsmål 28:** Hva får kunder til å komme tilbake?
- Eksempel: "Nytt innhold, nye features, lojalitetsprogram"

**Spørsmål 29:** Har dere eller planlegger dere lojalitetsprogram/referrals?
- Beskriv kort hvis ja

**Spørsmål 30:** Hvordan holder dere kontakten med eksisterende kunder?
- Eksempel: "Nyhetsbrev, sosiale medier, community"

### Touchpoints (Kontaktpunkter)

**Spørsmål 31:** Hvilke markedsføringskanaler bruker dere aktivt?
- Eksempler: "Facebook Ads, Google Ads, Instagram, LinkedIn, E-post, SEO"

**Spørsmål 32:** Hvilke kanaler vil dere satse mer på fremover?
- Prioriter gjerne

---

## ✅ CHECKPOINT: Opprett JOURNEY.md

**STOPP HER og opprett filen UMIDDELBART før du fortsetter til DEL 3.**

```
═══════════════════════════════════════════════════════════════
                    ✅ OPPRETTER JOURNEY.md
═══════════════════════════════════════════════════════════════

[████████░░░░░░░░] 50% - JOURNEY.md

Basert på svarene i DEL 2, oppretter jeg nå marketing/JOURNEY.md...

═══════════════════════════════════════════════════════════════
```

1. Opprett `marketing/JOURNEY.md`
2. Se `examples/JOURNEY.md` for struktur
3. Inkluder alle stages fra svarene:
   - Awareness (ToFU)
   - Consideration (MoFU)
   - Evaluation (BoFU)
   - Purchase
   - Post-purchase
   - Loyalty
4. Marker seksjoner som "[Under utvikling]" hvis bruker svarte "vet ikke"
5. Bekreft for brukeren:

```
✅ JOURNEY.md opprettet!

📁 marketing/JOURNEY.md

Inneholder:
• Kundereise-oversikt (6 stages)
• Touchpoints per stage
• Psykologi-prinsipper

Fortsetter til DEL 3: DISTRIBUTION.md...
───────────────────────────────────────────────────────────────
```

---

## DEL 3: DISTRIBUTION.md

```
───────────────────────────────────────────────────────────────
                      📡 KANALER & STACK
───────────────────────────────────────────────────────────────

Nå kartlegger vi hvilke verktøy dere bruker og hvor dere er
til stede.

Nyoppstartede merkevarer: "Ikke satt opp ennå" er helt OK.
Vi inkluderer Quick Start-tips for organic SEO.
───────────────────────────────────────────────────────────────
```

### Marketing Stack

**Spørsmål 40:** Hvilken e-postleverandør bruker dere?
- Eksempler: "Mailchimp", "Klaviyo", "Loops", "ConvertKit", "Ingen ennå"
- Hvis aktiv: hvor stor er listen?

**Spørsmål 41:** Hvilken CMS/website platform bruker dere?
- Eksempler: "WordPress", "Webflow", "Next.js", "Framer", "Shopify"

**Spørsmål 42:** Hvilke analytics-verktøy har dere?
- Eksempler: "GA4", "Plausible", "Fathom", "Ingen"
- Har dere Google Search Console satt opp?

**Spørsmål 43:** Hvilke sosiale medier er aktive?
- Eksempler: "LinkedIn", "Instagram", "TikTok", "X", "Facebook"
- Ca. hvor mange følgere per kanal?

**Spørsmål 44:** Bruker dere betalt annonsering?
- Eksempler: "Google Ads", "Meta Ads", "LinkedIn Ads", "Ingen"
- Hvis ja: ca. månedlig budsjett?

**Spørsmål 45:** Har dere CRM eller salgssystem?
- Eksempler: "HubSpot", "Pipedrive", "Salesforce", "Notion", "Regneark", "Ingen"

### Kanalstrategi

**Spørsmål 46:** Hvilke kanaler gir best resultater i dag?
- Eksempel: "Organic search", "LinkedIn", "Referrals"
- Hvis ny: "Ikke nok data ennå"

**Spørsmål 47:** Hvor vil dere satse mer fremover?
- Prioriter gjerne
- Hva er hypotesen for hvorfor denne kanalen?

---

## ✅ CHECKPOINT: Opprett DISTRIBUTION.md og LEARNINGS.md

**STOPP HER og opprett begge filer UMIDDELBART.**

```
═══════════════════════════════════════════════════════════════
                    ✅ OPPRETTER DISTRIBUTION.md
═══════════════════════════════════════════════════════════════

[████████████░░░░] 75% - DISTRIBUTION.md

Basert på svarene i DEL 3, oppretter jeg nå marketing/DISTRIBUTION.md...

═══════════════════════════════════════════════════════════════
```

### Opprett DISTRIBUTION.md

1. Opprett `marketing/DISTRIBUTION.md`
2. Se `examples/DISTRIBUTION.md` for struktur
3. Inkluder:
   - Marketing Stack (email, CMS, analytics, social, ads, CRM)
   - Current Channels med primary/secondary/experimental
   - Budget Split visualisering
   - SEO & AEO Strategy med tomme tabeller
4. Marker "[Ikke satt opp ennå]" for verktøy som mangler

### Opprett LEARNINGS.md (automatisk template)

```
═══════════════════════════════════════════════════════════════
                    ✅ OPPRETTER LEARNINGS.md
═══════════════════════════════════════════════════════════════

[████████████████] 100% - LEARNINGS.md

Oppretter tom template for å dokumentere tester og innsikter...

═══════════════════════════════════════════════════════════════
```

LEARNINGS.md opprettes som **tom template** - ingen intervju nødvendig:

```markdown
# Learnings

> Dokumentasjon av tester, resultater og innsikter.
> Fyll ut underveis når du kjører markedsføringsaktiviteter.

---

## Oversikt

| Periode | Test | Resultat | BAF Status |
|---------|------|----------|------------|
| [dato] | [test] | [resultat] | [status] |

**Nåværende BAF Status:** ⚠️ Ikke validert ennå

---

## Brand Audience Fit Validering

*[Fyll ut når du kjører første validering]*

### Test 1: [Navn]

**Hypotese:** [Hva tror du?]
**Oppsett:** [Kanal, budsjett, varighet, målgruppe]
**Resultater:** [Metrikker og tall]
**Konklusjon:** [Validert / Ikke validert / Under terskel]

---

## Hva vi har lært

### Hva fungerer ✅

| Innsikt | Bevis | Implementert? |
|---------|-------|---------------|
| [innsikt] | [bevis] | [✅/❌] |

### Hva fungerer ikke ❌

| Innsikt | Bevis | Handling |
|---------|-------|----------|
| [innsikt] | [bevis] | [handling] |

### Åpne spørsmål ❓

- [ ] [spørsmål 1]
- [ ] [spørsmål 2]

---

## Kommende tester

*[Planlagte tester å kjøre]*

---

*Sist oppdatert: [dato]*
```

Bekreft for brukeren:

```
✅ Alle filer opprettet!

📁 marketing/
   ✅ BRAND.md        - Merkevare-retningslinjer
   ✅ JOURNEY.md      - Kundereise-kart
   ✅ DISTRIBUTION.md - Kanaler og stack
   ✅ LEARNINGS.md    - Tom template for tester

───────────────────────────────────────────────────────────────
```

---

## Steg 4: Bekreft og Neste Steg

```
═══════════════════════════════════════════════════════════════
                         ✅ FERDIG!
═══════════════════════════════════════════════════════════════

Marketing Playbook er satt opp:

📁 marketing/
   ✅ BRAND.md        - Merkevare-retningslinjer (ABC)
   ✅ JOURNEY.md      - Kundereise-kart
   ✅ DISTRIBUTION.md - Kanaler og marketing stack
   ✅ LEARNINGS.md    - Tom template for tester

═══════════════════════════════════════════════════════════════
```

### Sjekk andre filer

Sjekk om følgende filer finnes og vis status til brukeren:

```
───────────────────────────────────────────────────────────────
STATUS - MARKETING PLAYBOOK
───────────────────────────────────────────────────────────────

Grunnoppsett:
✅ BRAND.md        - Nettopp opprettet
✅ JOURNEY.md      - Nettopp opprettet
✅ DISTRIBUTION.md - Nettopp opprettet
✅ LEARNINGS.md    - Nettopp opprettet

Valgfrie tillegg:
[✅/❌] DESIGN-SYSTEM.md  - Visuell identitet
[✅/❌] CONTENT-RULES.md  - Innholdsregler

───────────────────────────────────────────────────────────────
```

### Foreslå neste kommandoer

Basert på hva som mangler:

```
───────────────────────────────────────────────────────────────
NESTE STEG
───────────────────────────────────────────────────────────────

1. Review filene og juster detaljer
2. Bruk /marketing-playbook:check før du publiserer innhold
3. Kjør /marketing-playbook:audit for full gjennomgang

[Hvis DESIGN-SYSTEM.md mangler og bruker jobber med UI:]
💡 Kjør /design-system:init for visuell identitet

[Hvis CONTENT-RULES.md mangler og bruker skriver innhold:]
💡 Kjør /content-writer:init for innholdsregler

[Hvis fra scratch:]
🚀 Quick Start: Se DISTRIBUTION.md for organic SEO-guide
   Kjør /seo-aeo:audit for SEO og AI-synlighet-sjekk

───────────────────────────────────────────────────────────────
```

---

## Håndtering av ufullstendige svar

Hvis bruker svarer "vet ikke", "ikke relevant ennå", eller lignende:

1. **Ikke press** - Aksepter svaret
2. **Marker i output** - Bruk `[Under utvikling]` eller `[Ikke definert ennå]`
3. **Gi tips** - "Dette kan du fylle ut senere når du vet mer"

Eksempel i JOURNEY.md:
```markdown
### Loyalty (♻️)

*[Under utvikling - merkevaren er i tidlig fase]*

**Status:** Ikke definert ennå
**Tips:** Vurder lojalitetsprogram når du har etablert kundebase
```

---

## Alternative kommandoer

Hvis brukeren bare vil opprette én fil av gangen, kan de bruke:

- `/marketing-playbook:brand-init` - Kun BRAND.md
- `/marketing-playbook:journey-init` - Kun JOURNEY.md
- `/marketing-playbook:distribution-init` - Kun DISTRIBUTION.md

LEARNINGS.md opprettes automatisk som tom template og fylles ut manuelt underveis.
