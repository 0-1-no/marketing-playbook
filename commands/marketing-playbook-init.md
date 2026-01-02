---
description: Initialize Marketing Playbook for this project. Creates BRAND.md, JOURNEY.md, and LEARNINGS.md through interactive deep-dive setup.
allowed-tools: Read, Write, Glob, AskUserQuestion
---

# Marketing Playbook - Init

Opprett `BRAND.md`, `JOURNEY.md` og `LEARNINGS.md` for dette prosjektet gjennom interaktivt intervju (39 spørsmål).

## Steg 1: Sjekk eksisterende

Sjekk om `marketing/`-mappen finnes med `BRAND.md`, `JOURNEY.md` eller `LEARNINGS.md`.

Akseptable plasseringer (i prioritert rekkefølge):
1. `marketing/` (anbefalt)
2. Prosjekt-rot (legacy - migrer til marketing/)

Hvis filer finnes, spør:
```
Eksisterende filer funnet:
- marketing/BRAND.md: [Ja/Nei]
- marketing/JOURNEY.md: [Ja/Nei]
- marketing/LEARNINGS.md: [Ja/Nei]

Vil du:
1. Overskrive alt (starter på nytt)
2. Kun oppdatere BRAND.md
3. Kun oppdatere JOURNEY.md
4. Kun oppdatere LEARNINGS.md
5. Avbryt
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

Vi går gjennom tre deler:

📋 DEL 1: BRAND.md (ABC-rammeverket)
   • Audience - Hvem snakker vi til?
   • Brand - Hva tilbyr vi?
   • Communication - Hvordan sier vi det?

🗺️ DEL 2: JOURNEY.md (Kundereisen)
   • Hvordan oppdager kunder deg?
   • Hva vurderer de før kjøp?
   • Hvordan ser opplevelsen ut etterpå?

🧪 DEL 3: LEARNINGS.md (Validering)
   • Brand Audience Fit - Resonerer det?
   • Tester og resultater
   • Hva fungerer og hva fungerer ikke?

Dette tar ca. 10-15 minutter. Du kan svare "vet ikke" eller
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

## DEL 3: LEARNINGS.md

```
───────────────────────────────────────────────────────────────
                      🧪 VALIDERING
───────────────────────────────────────────────────────────────

Nå kartlegger vi Brand Audience Fit - om merkevaren faktisk
resonerer med målgruppen i praksis.

Nyoppstartede merkevarer: Det er helt OK å svare "ikke testet ennå".
Vi setter opp strukturen så du kan dokumentere underveis.
───────────────────────────────────────────────────────────────
```

### Brand Audience Fit

**Spørsmål 33:** Har dere testet om målgruppen responderer på merkevaren?
- Alternativer: "Ja, validert", "Under testing", "Ikke testet ennå"
- Dette er Brand Audience Fit (BAF) - bevis på at det fungerer

**Spørsmål 34:** Hvis testet - hvilke metoder har dere brukt?
- Eksempler: "Venteliste", "Forhåndssalg", "Annonse-test", "Landing page"
- Svar "ikke relevant" hvis ikke testet

**Spørsmål 35:** Hva er konverteringsraten deres? (hvis kjent)
- Eksempel: "2.5% på landing page"
- Benchmark: ≥2% indikerer sunn e-commerce
- Svar "vet ikke" hvis ukjent

**Spørsmål 36:** Hvilke segmenter responderer best?
- Eksempel: "Konsulenter 35-50 år"
- Hvem konverterer faktisk, ikke bare hvem dere tror er målgruppen

### Learnings

**Spørsmål 37:** Hva har dere lært som fungerer?
- Eksempel: "Video konverterer bedre enn tekst"
- List gjerne flere innsikter

**Spørsmål 38:** Hva har dere lært som IKKE fungerer?
- Eksempel: "Lange produktbeskrivelser gir høy bounce rate"
- Like viktig som det som fungerer

**Spørsmål 39:** Hvilke spørsmål vil dere teste fremover?
- Eksempel: "Fungerer budskapet for enterprise-kunder?"
- Åpne hypoteser å validere

---

## Steg 3: Generer filer

Opprett `marketing/`-mappen hvis den ikke finnes, og generer filene der:

```
marketing/
├── BRAND.md
├── JOURNEY.md
└── LEARNINGS.md
```

### marketing/BRAND.md
Se examples/BRAND.md for struktur. Inkluder:
- Audience med pain points, goals, use cases
- Brand med positioning, values, differentiators, competitors
- Communication med tone, Signature Story, Communication Principles, words we use/avoid
- Validation med BAF status (fra DEL 3)

### marketing/JOURNEY.md
Se examples/JOURNEY.md for struktur. Inkluder:
- Oversiktstabell med alle stages
- Per stage: Kundens perspektiv, bekymringer, touchpoints, våre mål
- Kobling til relevante psykologi-prinsipper
- Marker seksjoner som "Under utvikling" hvis bruker svarte "vet ikke"

### marketing/LEARNINGS.md
Se examples/LEARNINGS.md for struktur. Inkluder:
- Oversiktstabell med tester og resultater
- BAF Validering seksjon med status og metoder
- "Hva fungerer" og "Hva fungerer ikke" seksjoner
- Kommende tester / åpne spørsmål
- Marker som "[Ikke testet ennå]" hvis bruker er i tidlig fase

---

## Steg 4: Bekreft

```
═══════════════════════════════════════════════════════════════
                         ✅ FERDIG!
═══════════════════════════════════════════════════════════════

Marketing Playbook er satt opp:

📁 marketing/
   📋 BRAND.md      - Merkevare-retningslinjer (ABC + Validering)
   🗺️ JOURNEY.md    - Kundereise-kart
   🧪 LEARNINGS.md  - Tester og innsikter

───────────────────────────────────────────────────────────────
BRAND AUDIENCE FIT STATUS
───────────────────────────────────────────────────────────────

[✅ Validert / ⚠️ Under testing / ❌ Ikke testet]

[Hvis ikke validert:]
💡 Anbefaling: Test BAF før du skalerer markedsføringen.
   Kjør små tester, dokumenter i LEARNINGS.md.

───────────────────────────────────────────────────────────────
NESTE STEG
───────────────────────────────────────────────────────────────

1. Review filene og juster detaljer
2. Bruk /marketing-playbook:check før du publiserer innhold
3. Kjør /marketing-playbook:audit for full gjennomgang
4. Dokumenter learnings i LEARNINGS.md underveis

TIP: LEARNINGS.md er beviset på at merkevaren fungerer.
     Jo mer du dokumenterer, jo tryggere beslutninger.

═══════════════════════════════════════════════════════════════
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
