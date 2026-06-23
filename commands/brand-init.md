---
description: Opprett kun BRAND.md for dette prosjektet. Bruk denne hvis du bare vil sette opp merkevare-grunnlaget (ABC-rammeverket).
allowed-tools: Read, Write, Glob, AskUserQuestion
---

# Brand Init

Opprett `BRAND.md` for dette prosjektet gjennom fokusert intervju om ABC-rammeverket.

> **Når bruke denne:** Når du bare vil sette opp merkevare-grunnlaget uten kundereise og distribusjon.
> For fullstendig oppsett, bruk `/marketing-playbook:init` istedenfor.

---

## Steg 1: Sjekk eksisterende (seksjons-bevisst, additiv)

**Hvorfor dette steget er additivt:** Brand-init kan kjøres flere ganger — typisk når malen har fått nye seksjoner (f.eks. PMM-dybden: Personas, JTBD, Konkurranse-tiers, Proof points, Kundespråk, Innvendinger). Da skal en bruker som allerede fylte ut BRAND.md trygt kunne kjøre init på nytt og **kun fylle hullene**, uten å miste det de har skrevet. Vi jobber derfor på seksjons-nivå, ikke fil-nivå.

Sjekk om `marketing/BRAND.md` finnes (sjekk også prosjekt-rot for legacy — tilby migrering til `marketing/` hvis funnet der).

**Hvis filen ikke finnes:** hopp rett til Steg 2 og kjør hele intervjuet.

**Hvis filen finnes:** les den, og sammenlign mot dagens mal (`examples/BRAND.md`). Avgjør hvilke seksjoner som er PRESENT vs MISSING.

Forventede seksjoner (overskrift med reelt innhold = PRESENT; tom/`[placeholder]`/`[Under utvikling]` = MISSING):
- **ABC-kjerne:** Audience, Brand, Communication
- **PMM-dybde:** Personas (B2B), Jobs-to-be-done, Konkurranselandskap (tiers), Proof Points, Kundespråk (verbatim), Innvendinger

Vis en sjekkliste og la brukeren velge:
```
marketing/BRAND.md finnes. Seksjons-status:

✅ Du har:   Audience · Brand · Communication
⬜ Mangler:  Personas · Jobs-to-be-done · Konkurranse-tiers · Proof points · Kundespråk · Innvendinger

Hva vil du gjøre?
1. Fyll kun de manglende seksjonene (anbefalt — bevarer alt du har)
2. Velg spesifikke seksjoner å oppdatere
3. Oppdater hele BRAND.md på nytt (intervju alt — eksisterende beholdes om du svarer "behold")
4. Avbryt
```

**Regler for skriving (gjelder hele kommandoen):**
- Intervju **kun** de manglende/valgte seksjonene (spørsmål 1-15 = ABC-kjernen, 16-21 = PMM-dybden). Hopp over det som allerede er fylt.
- **Skriv additivt:** bevar alt eksisterende innhold, fyll kun hull / append manglende seksjoner. Overskriv ALDRI en utfylt seksjon uten at brukeren eksplisitt valgte den.
- Hvis en valgt seksjon allerede har innhold: vis gammelt, foreslå nytt, spør "behold / erstatt / slå sammen" før du skriver.

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

### PMM-dybde (produkt-markedsføring)

Disse seksjonene gir copy, salg og posisjonering mer å jobbe med. For B2C eller tidlig-fase: svar "ikke relevant ennå" der det ikke passer — feltene markeres `[Under utvikling]`.

**Spørsmål 16 — Personas (B2B):** Hvilke kjøpsroller er involvert i en beslutning?
- Roller: Bruker, Champion (intern forkjemper), Beslutningstaker, Økonomisk kjøper, Teknisk påvirker
- For hver relevant rolle: Hva bryr de seg om? Hva er deres utfordring? Hvilken verdi lover vi dem?
- B2C: ofte holder det med "Bruker"

**Spørsmål 17 — Jobs-to-be-done:** Hvilke 2-3 "jobber" ansetter kunden produktet for å få gjort?
- Format: "Når [situasjon], vil jeg [motivasjon], slik at jeg [utfall]"
- Tenk funksjonell + emosjonell + sosial jobb

**Spørsmål 18 — Konkurranselandskap i tiers:** Sorter konkurrentene i tre nivåer (utvider svar 9):
- **Direkte** (samme løsning, samme problem)
- **Sekundær** (annen løsning, samme problem)
- **Indirekte** (motstridende tilnærming, f.eks. "gjøre ingenting")
- For hver: hvor kommer de til kort?

**Spørsmål 19 — Proof points:** Hvilke bevis støtter løftene deres?
- Nøkkeltall/resultater, kunder/logoer, testimonial-snutter
- Koble gjerne verditema → bevis ("sparer tid" → konkret tall)
- Svar "ikke ennå" hvis dere er pre-launch

**Spørsmål 20 — Kundespråk (verbatim):** Hvordan beskriver kundene problemet og løsningen med EGNE ord?
- Sitater er gull — bruk dem ordrett der du har dem
- Bygg gjerne en liten ordliste: kundens ord → vårt begrep
- Dette utfyller "ord vi bruker" (svar 14), ikke dupliser

**Spørsmål 21 — Innvendinger:** Hva er de topp 3 grunnene til å IKKE kjøpe, og hvordan møter dere dem?
- Eksempel: "For dyrt" → regnestykke på ROI; "for komplisert" → 5-min oppsett

---

## Steg 4: Opprett BRAND.md

1. Opprett `marketing/`-mappen hvis den ikke finnes
2. Opprett `marketing/BRAND.md` basert på svarene
3. Se `examples/BRAND.md` for struktur
4. Inkluder alle ABC-elementer
5. Inkluder PMM-seksjonene (svar 16-21), plassert slik:
   - **Personas (B2B)** og **Jobs-to-be-done** under Audience
   - **Konkurranselandskap** (tiers) i Brand-delen
   - **Proof Points** etter Brand
   - **Kundespråk (verbatim)** i Communication (utfyller Words We Use/Avoid)
   - **Innvendinger** etter Konkurranselandskap eller Communication
6. Marker `[Under utvikling]` for seksjoner brukeren ikke kunne svare på

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
