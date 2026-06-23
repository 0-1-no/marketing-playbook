---
description: Initialize Marketing Playbook for this project. Creates BRAND.md, JOURNEY.md, DISTRIBUTION.md, and LEARNINGS.md through interactive deep-dive setup.
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

## Steg 1: Sjekk eksisterende (seksjons-bevisst, additiv)

**Hvorfor dette steget er additivt:** Init kan kjøres flere ganger — typisk når malen har fått nye seksjoner (f.eks. PMM-dybden: Personas, JTBD, Konkurranse-tiers, Proof points, Kundespråk, Innvendinger). Da skal en bruker som allerede fylte ut BRAND.md trygt kunne kjøre init på nytt og **kun fylle hullene**, uten å miste eller overskrive det de har skrevet. Vi jobber derfor på seksjons-nivå, ikke fil-nivå.

Sjekk om `marketing/`-mappen finnes med `BRAND.md`, `JOURNEY.md`, `DISTRIBUTION.md` eller `LEARNINGS.md`.

Akseptable plasseringer (i prioritert rekkefølge):
1. `marketing/` (anbefalt)
2. Prosjekt-rot (legacy - migrer til marketing/)

### 1a. Legacy-migrering (uendret)

Hvis filer finnes i rot (legacy), tilby migrering FØRST:
```
Fant filer i prosjekt-rot (legacy plassering):
- BRAND.md
- JOURNEY.md

Vil du migrere til marketing/-mappen? (anbefalt)
```

### 1b. Seksjons-diff per fil

For hver fil som finnes: **les den**, og sammenlign mot dagens mal (`examples/`-strukturen). Avgjør hvilke seksjoner som er PRESENT vs MISSING.

For BRAND.md er forventede seksjoner (overskrift = present-signal):
- **ABC-kjerne:** Audience, Brand, Communication
- **PMM-dybde:** Personas (B2B), Jobs-to-be-done, Konkurranselandskap (tiers), Proof Points, Kundespråk (verbatim), Innvendinger

> En seksjon teller som PRESENT hvis overskriften finnes OG har reelt innhold (ikke bare `[placeholder]`/`[Under utvikling]`). Tom/placeholder = MISSING (kan fylles).

Vis brukeren en sjekkliste, f.eks.:
```
marketing/BRAND.md finnes. Seksjons-status:

✅ Du har:   Audience · Brand · Communication
⬜ Mangler:  Personas · Jobs-to-be-done · Konkurranse-tiers · Proof points · Kundespråk · Innvendinger

Hva vil du gjøre?
1. Fyll kun de manglende seksjonene (anbefalt — bevarer alt du har)
2. Velg spesifikke seksjoner å oppdatere
3. Oppdater hele BRAND.md på nytt (intervju alt — eksisterende innhold beholdes om du svarer "behold")
4. Hopp over BRAND.md
```

Gjør tilsvarende kort sjekkliste for JOURNEY.md, DISTRIBUTION.md og LEARNINGS.md (present/missing på fil-nivå holder for disse — seksjons-diff er viktigst for BRAND.md).

### 1c. Intervju kun det som mangler/velges

- Still **kun** spørsmålene som hører til de manglende/valgte seksjonene. Hopp over alt brukeren allerede har fylt ut.
- For BRAND.md: spørsmål 1-15 dekker ABC-kjernen, 15a-15f dekker PMM-dybden. Kjør bare de relevante.

### 1d. Skriv additivt (aldri stille overskriving)

- **Bevar alt eksisterende innhold.** Append nye seksjoner / fyll tomme felt — overskriv ALDRI en utfylt seksjon uten at brukeren eksplisitt valgte den.
- Behold brukerens egen rekkefølge og formuleringer; sett nye seksjoner inn på riktig plass (se plasserings-listen i CHECKPOINT under).
- Hvis en valgt seksjon allerede har innhold: vis det gamle, foreslå det nye, og spør "behold / erstatt / slå sammen" før du skriver.

**For en helt fersk fil (ingen `marketing/`-filer finnes):** hopp over diffen og kjør hele intervjuet (DEL 1-4) som normalt.

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

### PMM-dybde (produkt-markedsføring)

Disse seksjonene gir copy, salg og posisjonering mer å jobbe med. For B2C eller tidlig-fase: svar "ikke relevant ennå" der det ikke passer — feltene markeres `[Under utvikling]`.

**Spørsmål 15a — Personas (B2B):** Hvilke kjøpsroller er involvert i en beslutning?
- Roller: Bruker, Champion (intern forkjemper), Beslutningstaker, Økonomisk kjøper, Teknisk påvirker
- For hver relevant rolle: Hva bryr de seg om? Hva er deres utfordring? Hvilken verdi lover vi dem?
- B2C: ofte holder det med "Bruker"

**Spørsmål 15b — Jobs-to-be-done:** Hvilke 2-3 "jobber" ansetter kunden produktet for å få gjort?
- Format: "Når [situasjon], vil jeg [motivasjon], slik at jeg [utfall]"
- Tenk funksjonell + emosjonell + sosial jobb

**Spørsmål 15c — Konkurranselandskap i tiers:** Sorter konkurrentene i tre nivåer (utvider svar 9):
- **Direkte** (samme løsning, samme problem)
- **Sekundær** (annen løsning, samme problem)
- **Indirekte** (motstridende tilnærming, f.eks. "gjøre ingenting")
- For hver: hvor kommer de til kort?

**Spørsmål 15d — Proof points:** Hvilke bevis støtter løftene deres?
- Nøkkeltall/resultater, kunder/logoer, testimonial-snutter
- Koble gjerne verditema → bevis ("sparer tid" → konkret tall)
- Svar "ikke ennå" hvis dere er pre-launch

**Spørsmål 15e — Kundespråk (verbatim):** Hvordan beskriver kundene problemet og løsningen med EGNE ord?
- Sitater er gull — bruk dem ordrett der du har dem
- Bygg gjerne en liten ordliste: kundens ord → vårt begrep
- Dette utfyller "ord vi bruker" (svar 14), ikke dupliser

**Spørsmål 15f — Innvendinger:** Hva er de topp 3 grunnene til å IKKE kjøpe, og hvordan møter dere dem?
- Eksempel: "For dyrt" → regnestykke på ROI; "for komplisert" → 5-min oppsett

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
5. Inkluder PMM-seksjonene (svar 15a-15f), plassert slik:
   - **Personas (B2B)** og **Jobs-to-be-done** under Audience
   - **Konkurranselandskap** (tiers) i Brand-delen
   - **Proof Points** etter Brand
   - **Kundespråk (verbatim)** i Communication (utfyller Words We Use/Avoid)
   - **Innvendinger** etter Konkurranselandskap eller Communication
   - Marker `[Under utvikling]` for seksjoner brukeren ikke kunne svare på
6. Bekreft for brukeren:

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
