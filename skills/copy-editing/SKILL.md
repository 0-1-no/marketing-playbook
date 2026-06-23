---
name: copy-editing
description: Redigerer, forbedrer og refresher EKSISTERENDE markedstekst — ikke skriving fra bunnen. Aktiveres når du har tekst som skal poleres, strammes inn eller oppdateres: «rediger denne teksten», «vask språket», «korrekturles», «gjør dette skarpere», «kutt fyllord», «denne leser tungt», «for ordrik», «oppdater denne siden», «innholdet er utdatert», «refresh denne artikkelen», «sjekk mot brand voice», eller redaksjonell QA før publisering. Bruk denne når teksten allerede finnes og skal forbedres. For å SKRIVE ny tekst fra bunnen, bruk storytelling-copywriting i stedet.
---

# Copy Editing (Språkvask & Redaksjonell QA)

Denne skillen hjelper deg med å **redigere, forbedre og refreshe tekst som allerede finnes** — ikke skrive ny. Du tar et utkast eller en publisert side og gjør den klarere, strammere, mer på-merke og faktasjekket, uten å miste forfatterens stemme eller kjernebudskap.

---

## Grensen mot storytelling-copywriting (les dette først)

Dette er det viktigste å forstå før du starter:

| Skill | Jobb | Når |
|-------|------|-----|
| **storytelling-copywriting** | SKRIVER ny tekst fra bunnen | Tom side. Du trenger overskrift, struktur, hook, et helt utkast. |
| **copy-editing** (denne) | REDIGERER, FORBEDRER, REFRESHER tekst som finnes | Du har et utkast eller en publisert side som skal poleres eller oppdateres. |

**Tommelfingerregel:** Skriver du noe nytt? → `storytelling-copywriting`. Gjør du noe eksisterende bedre? → her.

I praksis jobber de to sammen: copywriteren leverer førsteutkastet, så tar du editor-passet. Ikke skriv om hele teksten — *forbedre* den. Hvert kutt skal ha en grunn, og du skal kunne forklare hvorfor endringen gjør teksten bedre.

---

## Arkitektur: Global Plugin + Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ COPY-EDITING SKILL (Global Plugin)                                  │
│                                                                     │
│ Du leser dette nå. Det er del av marketing-playbook plugin.        │
│ Inneholder kun metodikk: hvordan redigere, hva du sjekker.         │
│ INGEN konkret voice eller ordliste — de kommer fra kodebasen.      │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/ (DENNE KODEBASEN)                                      │
│                                                                     │
│ Fasiten du redigerer MOT:                                          │
│ • BRAND.md → Tone of Voice, Words We Use/Avoid, Signature Story    │
│ • CONTENT-RULES.md → Voice-dimensjoner, strukturregler, godkjenning│
│ • JOURNEY.md → Hvilken stage er leseren i?                         │
└─────────────────────────────────────────────────────────────────────┘
```

**Poenget:** Skillen sier «sjekk voice-konsistens». *Hva* riktig voice er, står i `./marketing/BRAND.md`. Du redigerer alltid mot prosjektets faktiske fasit, ikke en generell standard.

---

## Før du starter

1. **Les `./marketing/BRAND.md`** (Communication-seksjonen) — Tone of Voice, `Words We Use`, `Words We Avoid`. Dette er fasiten for voice-passet.
2. **Les `./marketing/CONTENT-RULES.md`** — Voice-dimensjoner, strukturregler og «Godkjenning»-flyten (forfatter → editor).
3. **Les `./marketing/JOURNEY.md`** ved tvil — hvilken stage skriver teksten for? En awareness-tekst og en kjøpsside tåler ulik tone.

Hvis filene ikke finnes:
- Kjør `/marketing-playbook:init` for BRAND.md og JOURNEY.md
- Kjør `/content-writer:init` for CONTENT-RULES.md

Mangler fasiten helt, si fra til brukeren — uten BRAND.md gjetter du på voice, og da blir voice-passet svakt.

---

## Tre spørsmål før du redigerer

Still disse (eller utled dem fra konteksten) så du redigerer mot riktig mål:

1. **Hva er målet med teksten?** Kjennskap, konvertering eller retention? Det avgjør hvor hardt du presser på CTA og bevis.
2. **Hvilken handling skal leseren ta?** Hvis det ikke er tydelig i teksten, er det din viktigste rettelse.
3. **Er dette et utkast eller en refresh av publisert innhold?** Et utkast trenger editor-passene. Publisert innhold som har stått en stund trenger i tillegg et refresh-pass (utdaterte tall, døde lenker, foreldede claims — se eget avsnitt).

---

## Editor-passene

Rediger i fokuserte pass, ett hensyn om gangen. Flere skarpe pass slår ett rotete gjennomlesningsforsøk der du prøver å fikse alt samtidig — da overser du ting. Etter hvert pass: sjekk raskt at du ikke har ødelagt et tidligere pass.

Du trenger ikke alltid kjøre alle. For en rask vask holder pass 1–3. For en landingsside eller lanseringsmail som skal konvertere, kjør alle.

### Pass 1 — Klarhet
**Spørsmål:** Forstår leseren umiddelbart hva som menes?

Se etter: forvirrende setningsbygning, uklare pronomen («det», «dette» som peker på ingenting konkret), sjargong uten forklaring, setninger som prøver å si for mye. Vanligste klarhetsdreper: abstrakt språk der konkret ville landet bedre.

Hvordan: les raskt gjennom og marker uklare partier først — ikke fiks ennå. Foreslå så konkrete rettelser. Behold den opprinnelige meningen.

### Pass 2 — Flyt og kutt
**Spørsmål:** Er teksten stram, eller drukner poenget i fyll?

Kutt fyllord («veldig», «egentlig», «faktisk», «i grunnen»), tomme åpninger («I dagens digitale verden …»), og floskler. Varier setningslengde — bland korte og lange så rytmen ikke blir monoton. Korte avsnitt (2–4 setninger for web). Viktigste info først.

Full liste over fyllord og floskler: [references/sprakvask.md](references/sprakvask.md).

### Pass 3 — Aktiv stemme og klart språk
**Spørsmål:** Skriver teksten som folk snakker, eller som et rundskriv?

- **Passiv → aktiv:** «Rapportene blir laget» → «Vi lager rapportene». Aktiv stemme er kortere og tydeligere om hvem som gjør hva.
- **Nominaliseringer → verb:** «foreta en vurdering» → «vurdere», «gi en anbefaling» → «anbefale». Verb gjør teksten levende.
- **Byråkratord → hverdagsord:** «benytte» → «bruke», «tilrettelegge» → «hjelpe», «implementere» → «sette opp».
- **Anglisismer → norsk der norsk finnes:** «leverage» → «bruke», «feedback» → «tilbakemelding», «seamless» → «smidig». MEN: behold engelsk fagterm hvis BRAND.md bevisst bruker den (vanlig i tech/SaaS) — konsistens med definert stemme vinner over norsk-purisme.

Oppslagslister for alle tre: [references/sprakvask.md](references/sprakvask.md).

### Pass 4 — Voice-konsistens (mot BRAND.md + CONTENT-RULES.md)
**Spørsmål:** Høres hele teksten ut som samme merkevare?

Dette er passet som binder skillen til prosjektet. Sjekk mot fasiten:

| Sjekk | Mot |
|-------|-----|
| Toneskift midtveis (starter varm, blir korporativ) | BRAND.md → Tone of Voice |
| Ord som aldri skal brukes | BRAND.md → `Words We Avoid` |
| Konsekvent terminologi | BRAND.md → `Words We Use` |
| Voice-dimensjoner holdt gjennom hele | CONTENT-RULES.md → Voice-dimensjoner |
| Blanding av «vi»/«selskapet»/tredjeperson | CONTENT-RULES.md |

Les gjerne høyt — øret fanger toneskift øyet glir forbi.

### Pass 5 — So what (relevans)
**Spørsmål:** Svarer hver påstand på «hva har jeg som leser igjen for det?»

For hvert utsagn, spør «og så?». Hvis teksten ikke svarer med en fordel for leseren, mangler det en bro.

❌ «Plattformen bruker AI-drevet analyse»
*Og så?*
✅ «AI-analysen fanger innsikt du ville oversett manuelt — så du tar bedre beslutninger på halve tiden»

Vanligste feil: funksjonslister uten å koble til verdi (feature-dumping).

### Pass 6 — Bevis og spesifisitet
**Spørsmål:** Er påstandene konkrete og underbygget, eller vage og tomme?

- **Bevis:** «markedsledende» (etter hvilken måling?), «kundene elsker oss» (vis dem si det), «tusenvis stoler på oss» (hvilke tusenvis?). Legg til tall, kilde, testimonial med navn — eller demp påstanden.
- **Spesifisitet:** bytt vage ord med konkrete.

| Vagt | Spesifikt |
|------|-----------|
| Spar tid | Spar 4 timer i uka |
| Mange kunder | 2 847 team |
| Raske resultater | Resultater på 14 dager |
| Forbedre arbeidsflyten | Halver rapporteringstiden |
| God support | Svar innen 2 timer |

**Aldri fabriker** tall eller testimonials. Mangler du bevis, demp påstanden i stedet — falske tall ødelegger troverdigheten for hele merkevaren.

---

## Refresh av utdatert innhold

Språkvask er ikke bare for nye utkast. Publiserte sider forfaller: utdaterte tall, foreldede eksempler, drevet brand voice, døde lenker. Bruk refresh-passet når trafikken faller, dataen er gammel, eller produktet har endret seg.

**Refresh-sjekkliste:**
1. **Ferskhet** — Oppdater alle årstall, statistikk og eksempler. Bytt «i 2024» med fersk data. Fjern referanser til avviklede funksjoner eller verktøy.
2. **Nøyaktighet** — Stemmer påstandene fortsatt? Sjekk at pris, funksjoner og posisjonering matcher dagens virkelighet. Test at lenker lever.
3. **Voice** — Matcher tonen dagens BRAND.md? Eldre innhold speiler ofte et tidligere stadium av selskapet.
4. **Bevis** — Kan du legge til nyere testimonials, case eller tall som ikke fantes da teksten ble skrevet?
5. **Synlighet** — Har søkeintensjonen flyttet seg? Legg til «Sist oppdatert: [dato]» synlig (utdatert innhold blir sitert mindre i AI-søk — se `ai-seo`).

**Refresh eller skriv om?**

| Signal | Handling |
|--------|----------|
| Kjernebudskap gyldig, detaljer utdatert | Refresh (oppdater fakta, tall, eksempler) |
| Brand voice har endret seg mye | Refresh + voice-omskriving |
| Vinkel eller målgruppe har flyttet seg | Full omskriving → bruk `storytelling-copywriting` |
| Trenger bare ferske tall og lenker | Lett refresh |

**Kadens (utgangspunkt):** Pris-/produktsider hvert kvartal · høytrafikk-blogg hver 6. mnd · sammenligningssider hver 3.–6. mnd (konkurrenter endrer seg fort) · evergreen-guider årlig.

---

## Før/etter-eksempel

Samme avsnitt, før og etter editor-passene. Legg merke til at kjernebudskapet er bevart — det er strammet og spesifisert, ikke skrevet om.

**Før (utkast):**
> I dagens digitale verden er det egentlig veldig viktig for bedrifter å ha en seamless onboarding. Vår innovative og markedsledende plattform muliggjør at nye kunder kan komme raskt i gang, og det blir tilrettelagt for en god kundeopplevelse gjennom hele kundereisen. Mange kunder opplever store fordeler.

**Etter (redigert):**
> Ny kunde skal være i gang på under 10 minutter. Plattformen gir dem et veiledet oppstartsløp — uten support-billett, uten venting. 9 av 10 fullfører oppsettet på første forsøk.

Hva som skjedde, pass for pass:
- **Klarhet/flyt:** Strøk tom åpning («I dagens digitale verden»), fyllord («egentlig», «veldig»).
- **Aktiv + klart språk:** «det blir tilrettelagt» → aktiv; «muliggjør» → «gir»; anglisismen «seamless onboarding» → «oppstartsløp … uten venting».
- **Voice:** «innovative og markedsledende» (buzzword-bingo) strøket.
- **So what + bevis:** «store fordeler» → konkret resultat; «mange kunder» → «9 av 10 fullfører på første forsøk» (forutsetter at tallet er ekte — ellers demp).

---

## Redaksjonell QA-workflow (forfatter → editor)

Tekst skal ikke publiseres rett fra forfatterens tastatur. Editor-passet er en egen rolle, og det fungerer best som en sløyfe — særlig for tekst med høy innsats (landingssider, lanseringsmail, prissider).

1. **Forfatter leverer utkast** — via `storytelling-copywriting` eller `content-writing`.
2. **Kjør et pass og presenter funn** — vis hva du fant og *hvorfor* det er et problem. Ikke bare pek på feil; foreslå konkrete rettelser.
3. **La forfatteren eie sluttvalget** — på substans og stemme. Du foreslår, de bestemmer.
4. **Sjekk tidligere pass på nytt** etter hver runde med endringer, så en rettelse ikke skaper et nytt problem.
5. **Gjenta til et helt pass ikke finner noe nytt.**
6. **Siste kvalitetsport:** kjør den fulle QA-sjekklista ([references/sprakvask.md](references/sprakvask.md)) + `/marketing-playbook:check` for validering mot BRAND.md og CONTENT-RULES.md. For høy-innsats-tekst, sjekk også CONTENT-RULES.md → «Godkjenning» for prosjektets egne porter.

For en rask sluttsjekk uten full sløyfe: bruk QA-sjekklista i [references/sprakvask.md](references/sprakvask.md).

---

## Vanlige problemer og fiks

| Problem | Symptom | Fiks |
|---------|---------|------|
| Funksjonsvegg | Liste over hva produktet gjør, uten hvorfor det betyr noe | Legg til «som betyr …» etter hver funksjon |
| Korporativt språk | «Tilrettelegge for synergier» | «Hvordan ville et menneske sagt dette?» |
| Svak åpning | Starter med selskapets historie eller vage utsagn | Led med leserens problem eller ønsket resultat |
| Begravd CTA | Oppfordringen kommer for sent eller er utydelig | Gjør CTA tydelig, tidlig, gjentatt |
| Ingen bevis | «Kundene elsker oss» uten dokumentasjon | Legg til konkret testimonial, tall eller case |
| Generiske påstander | «Vi hjelper bedrifter å vokse» | Spesifiser hvem, hvordan, og hvor mye |
| Buzzword-bingo | «Revolusjonerende AI-drevet plattform» | Bytt med konkret utsagn leseren kan tro på |

---

## Anti-patterns (unngå)

- **Skrive om i stedet for å redigere** — du skal forbedre teksten, ikke erstatte den med din egen. Behold forfatterens stemme.
- **Fikse alt på én gjennomlesning** — du overser ting. Kjør fokuserte pass.
- **Endre kjernebudskapet** — språkvask polerer budskapet, det bytter det ikke ut.
- **Norsk-purisme mot merkevaren** — ikke bytt ut engelske fagtermer BRAND.md bevisst bruker.
- **Fabrikere bevis** — aldri dikt opp tall eller testimonials for å fylle et «prove it»-hull.
- **Redigere uten fasit** — uten BRAND.md gjetter du på voice. Les den først.

---

## Relaterte Skills

- `storytelling-copywriting` — SKRIVE ny tekst fra bunnen (motstykket til denne). Frameworks, overskrifter, CTAs, persuasjon. Bruk når siden er tom.
- `content-writing` — Lengre formater (artikler, guider, landing pages) og struktur/skannbarhet. Editorer ofte tekst som kom herfra.
- `content-strategy` — Hvilke sider/temaer som finnes og bør refreshes; prioritering av innholdsarbeid.
- `seo-aeo` — Søke- og AI-synlighet. Refresh-passet hekter på her (utdatert innhold siteres mindre — se `ai-seo`).
- `marketing-psychology` — Hvorfor en redigering forbedrer konvertering.
- `brand-principles` — Merkevare-fundamentet bak `Words We Use/Avoid`.

---

## Når bruker jeg hvilken skill?

| Oppgave | Skill |
|---------|-------|
| Skrive ny sidekopi fra bunnen | `storytelling-copywriting` |
| Skrive en lengre artikkel/guide | `content-writing` |
| Forbedre tekst du (eller noen) nettopp skrev | `copy-editing` (denne) |
| Korrekturlese og polere før publisering | `copy-editing` (denne) |
| Oppdatere en publisert side med utdaterte tall/lenker | `copy-editing` (denne) → refresh-passet |
| Strukturell/strategisk endring av en side | `page-cro` / `content-strategy` |

---

## Referanser (les ved behov)

| Fil | Bruk når du … |
|-----|----------------|
| [references/sprakvask.md](references/sprakvask.md) | Trenger oppslagslister: anglisismer→norsk, byråkratord→klart språk, fyllord/floskler å stryke, buzzword-bingo, og den fulle QA-sjekklista før publisering |
