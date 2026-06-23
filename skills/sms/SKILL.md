---
name: sms
description: SMS- og MMS-markedsføring for nordisk e-handel — velkomst-SMS, forlatt-handlekurv, ordrebekreftelse, restock-varsler, vinn-tilbake og tidsbegrensede tilbud. Aktiveres ved SMS-markedsføring, tekstmelding-kampanjer, SMS-flyt, MMS, forlatt handlekurv på SMS, transaksjonell SMS, samtykke til SMS, avsender-ID, alfanumerisk avsender, Link Mobility, Sveve, Vianett, eller «bør vi sende SMS». Bruk også når noen spør om SMS vs e-post. For e-postsekvenser, se email-sequence. For SMS-tekst og rammeverk, se storytelling-copywriting.
---

# SMS-markedsføring

Du er en ekspert på SMS- og MMS-markedsføring for nordisk e-handel. Målet er å bygge SMS-program som driver målbar omsetning eller aktivering — uten å brenne ned listen eller bryte markedsføringsloven. SMS er den dyreste, mest påtrengende kanalen du har. Den fortjener retten til å avbryte fordi mottakeren har sagt ja. Bruk den der umiddelbarhet faktisk vinner, ikke som «enda en e-post».

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ SMS SKILL (Global Plugin)                                           │
│                                                                     │
│ Inneholder kun metodikk: når SMS gir mening, hvordan flyter        │
│ bygges, hvordan korte meldinger skrives, hvordan det måles.        │
│ INGEN konkrete produktverdier — de kommer fra kodebasen.           │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/BRAND.md + JOURNEY.md (DENNE KODEBASEN)                 │
│                                                                     │
│ • Tone of Voice → Hvordan meldingene skrives                       │
│ • Kundereise → Hvilken fase mottakeren er i                        │
│ • Posisjonering → Hvilket løfte SMS-en bærer                       │
│ • Avsendernavn → Hvilken avsender-ID som vises                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Tone, posisjonering, avsendernavn (alfanumerisk avsender-ID henter merkenavnet herfra)
2. **Les `./marketing/JOURNEY.md`** — Kundereisefaser, så du vet hvilken fase en SMS-flyt skal treffe
3. **Les `./marketing/DISTRIBUTION.md`** — Kanalmiks (om den finnes); SMS er nesten alltid et lag *oppå* e-post, ikke en erstatning

Hvis filene ikke finnes, kjør `/marketing-playbook:init` først.

---

## Samtykke først — les dette før alt annet

**Samtykke er fundamentet, ikke en ettertanke.** Uten gyldig samtykke har du ikke et SMS-program — du har et tilsynsregulert problem. I Norge styres dette av markedsføringsloven, ikke amerikansk TCPA. Reglene er strengere på samtykke og enklere på avsender.

### Markedsføringsloven § 15 — forhåndssamtykke

§ 15 krever **forhåndssamtykke** for elektronisk markedsføring til fysiske personer — det inkluderer SMS, MMS, e-post og automatiske oppringningssystemer. Det betyr:

1. **Aktivt, uttrykkelig ja.** Mottakeren må aktivt ha samtykket til markedsføring på SMS. Forhåndskryssede avkrysningsbokser teller ikke. «Du fikk en e-post fra oss» eller «du er kunde» er ikke samtykke.
2. **Samtykket må være spesifikt.** Ja til nyhetsbrev på e-post er *ikke* ja til SMS. Be om SMS-samtykke eksplisitt, gjerne med eget felt eller egen avkrysning.
3. **Frivillig.** Samtykke kan ikke være et vilkår for kjøp eller for å fullføre bestillingen.
4. **Dokumenterbart.** Logg tidspunkt, kilde (hvilket skjema/popup), og nøyaktig samtykketekst som ble vist. Forbrukertilsynet kan be om dette.

**Unntak — eksisterende kundeforhold:** § 15 åpner for at du *kan* markedsføre tilsvarende egne varer/tjenester til en eksisterende kunde uten forhåndssamtykke, men kun hvis kunden fikk en enkel og gratis mulighet til å reservere seg ved innsamling av kontaktinfo *og* i hver senere melding. Dette unntaket er smalt og lett å trå feil på — for SMS er det tryggest å alltid hente eksplisitt samtykke. Behandle unntaket som en nødløsning, ikke en strategi.

### Reservasjonsregisteret

Reservasjonsregisteret (drevet av Brønnøysundregistrene) lar privatpersoner reservere seg mot direktemarkedsføring. For *adressert post og telefonsalg* plikter du å vaske mot det. For SMS basert på eget samtykke er ditt eget opt-in/opt-out-register det primære — men har du kjøpt eller fått lister fra tredjepart, må disse vaskes mot Reservasjonsregisteret før første utsendelse. Tommelfingerregel: send aldri SMS til noen du ikke selv har et dokumentert ja fra.

### GDPR

Telefonnummer er personopplysning. Samtykke til SMS-markedsføring er behandlingsgrunnlaget (GDPR art. 6(1)(a)). Det betyr:

- **Like enkelt å trekke tilbake som å gi.** Avmelding må fungere i hver melding.
- **Innsyn og sletting.** Mottakeren kan be om innsyn (DSAR) og sletting. Ha en rutine.
- **Oppbevaring.** Behold samtykkebevis så lenge du behandler nummeret + rimelig tid etter avmelding for å kunne dokumentere lovlighet.

### Hver melding må ha

- **Tydelig avsender** — merkenavnet skal være synlig (alfanumerisk avsender-ID, se under). Mottakeren ser ikke et «fra»-felt slik som i e-post; navnet må fremgå.
- **Enkel avmelding** — «Svar STOPP for å melde av» eller en avmeldingslenke. Skal være gratis og umiddelbar.

**For en revisjonsklar samtykke- og avmeldingssjekkliste, opt-in-tekst og STOPP-håndtering, se [references/samtykke.md](references/samtykke.md).**

---

## Avsender-ID i Norge

Norske SMS-leverandører lar deg sende fra to typer avsender:

| Type | Eksempel | Egenskap | Brukstilfelle |
|------|----------|----------|---------------|
| **Alfanumerisk avsender** | `Merkenavn` (inntil 11 tegn) | Mottaker kan **ikke** svare | Markedsføring, varsler, ordrebekreftelse |
| **Virtuelt/dedikert nummer** | `+47 …` | Mottaker **kan** svare (toveis) | Kundedialog, STOPP-håndtering, support |

**Konsekvens for tekst:** Med alfanumerisk avsender kan mottakeren ikke svare STOPP til avsenderen — derfor må avmeldingen være en **lenke** eller et eget kortnummer. Med virtuelt nummer kan du bruke «Svar STOPP». Velg avsendertype *før* du skriver tekst, fordi det avgjør hvordan avmeldingen formuleres.

Avsendernavnet hentes fra `./marketing/BRAND.md`. Hold deg innenfor 11 tegn, og bruk samme avsender konsekvent — gjenkjennelse driver åpningsrate og reduserer at meldingen oppleves som spam.

---

## Når SMS slår e-post

SMS er ikke «en e-post til». Bruk den der kanalens egenskaper vinner — høy, umiddelbar åpningsrate — og hold deg unna der den bare blir dyr støy.

| Brukstilfelle | SMS eller e-post? | Hvorfor |
|---------------|-------------------|---------|
| Forlatt handlekurv | **SMS først** | Åpnes innen minutter; e-post leses kanskje neste dag |
| Ordre-/leveringsvarsel | **SMS** | Kunden vil ha det nå, på telefonen |
| Tidsbegrenset tilbud / drop | **SMS** | Hastekanal — leses umiddelbart |
| Restock / «tilbake på lager» | **SMS** | Tidssensitivt; den som varsles først, kjøper |
| Velkomst | **E-post primært, SMS som lag** | E-posten bærer det lange innholdet |
| Pedagogisk nurture | **E-post** | For mye tekst for SMS, og hver SMS koster penger |
| Nyhetsbrev | **E-post** | Feil kanal for SMS |
| Vinn-tilbake | **Begge** | SMS for det harde dyttet, e-post for detaljene i tilbudet |

**Hovedregel:** Hvis meldingen kan vente 24 timer, send den på e-post. SMS reserveres for det som faktisk tjener på umiddelbarhet. Hver gang du er i tvil, er svaret e-post — SMS koster per melding og tærer på listens tålmodighet.

---

## Kjerneprinsipper

### 1. Hver utsendelse koster penger
SMS er ikke gratis. Med pris per melding (typisk noen øre til ~1 kr per SMS i NOK, avhengig av leverandør og volum) tvinger kostnaden frem relevans. Du kan ikke «blaste». Segmenter hardt.

### 2. Samtykket er din mest verdifulle ressurs
Andelen e-postabonnenter som også sier ja til SMS er typisk lav (ofte 5–25 %). En liten liste med ekte ja slår en stor liste med tvilsomt grunnlag. Optimaliser kvaliteten på samtykket, ikke antallet.

### 3. Hver melding må forsvare seg selv
Mottakeren ga deg nummeret sitt. Hver utsendelse skal bestå testen: «Ville jeg vært glad for å få denne meldingen?» Hvis nei — ikke send.

### 4. Korthet og klarhet
Én norsk SMS = 160 tegn (GSM-7-koding). 161+ tegn deles i flere meldinger, og du betaler per del. **Norske tegn (æ, ø, å) finnes i GSM-7 og koster ikke ekstra** — men emojier og enkelte spesialtegn tvinger frem UCS-2-koding, som kutter grensen til 70 tegn per del og dobler kostnaden. Planlegg for antall meldingsdeler.

### 5. Én CTA, én lenke
Kortlenke er obligatorisk (egen merket kortdomene eller leverandørens). Legg UTM-parametere på hver lenke. Én handling, én URL.

### 6. Tydelig avsender i hver melding
Merkenavnet skal frem (alfanumerisk avsender-ID), også i automatiske flyter. Mottakeren har ikke et «fra»-felt å lese — navnet må være synlig.

### 7. Frekvenstak og stilletid
Sett et hardt frekvenstak (f.eks. maks 4–6 markedsførings-SMS per uke per mottaker, lavere for ferske abonnenter). Send i våken tid — norsk praksis er 09–20, aldri tidlig morgen eller sen kveld. Helger fungerer for B2C-tilbud; B2B holder seg til hverdager.

---

## SMS-flyttyper

Hver flyt under angir trigger, forsinkelse og formål. Tekstene er korte og norske; juster tone etter `./marketing/BRAND.md`.

### Velkomst / bekreftelse av samtykke (umiddelbart)

**Trigger:** Mottaker sier ja til SMS. **Mål:** Bekreft, lever lovet verdi, sett tonen.

| SMS | Timing | Formål |
|-----|--------|--------|
| 1 | 0 (umiddelbart) | Bekreftelse + lovet rabatt/verdi + avmeldingsinfo (påkrevd på første melding) |
| 2 | 24 t (valgfri) | Påminnelse + bestselgere, om ingen kjøp |

> `Merkenavn: Velkommen! Her er 10 % rabatt: VELKOMMEN10. Handle: [kortlenke]. Avmelding: [lenke]`

### Forlatt handlekurv (høyest avkastning for e-handel)

**Trigger:** Påbegynt, ikke fullført kjøp. **Mål:** Hente kjøpet hjem.

| SMS | Timing | Formål |
|-----|--------|--------|
| 1 | 30 min etter | «Du glemte noe» + lenke til kurven |
| 2 | 4 t etter (om ingen kjøp) | Myk hast + sosialt bevis |
| 3 | 24 t etter (om ingen kjøp, hvis margin tillater) | Rabatt for å lukke |

**Merk:** Rabatt allerede i SMS 1 lærer kundene å forlate kurven med vilje. Reserver rabatten til SMS 2 eller 3. Stopp flyten ved kjøp, avmelding eller etter 48 t.

### Ordrebekreftelse / transaksjonelt (umiddelbart)

**Trigger:** Fullført kjøp eller forsendelse. **Mål:** Informere — ikke selge.

Transaksjonell SMS (ordrebekreftelse, «pakken er sendt», leveringsvarsel, verifiseringskode) er knyttet til noe kunden selv satte i gang, og er informasjon snarere enn markedsføring. Ikke pakk inn salg i en transaksjonell melding — det gjør den til markedsføring og krever da samtykke etter § 15. Hold det rent: status, sporing, ferdig.

> `Merkenavn: Ordre #12345 bekreftet. Vi sender sporingsoppdatering hit. Spor: [kortlenke]`

### Restock / tilbake på lager (umiddelbart ved hendelse)

**Trigger:** Mottaker meldte interesse for et utsolgt produkt, og det er tilbake. **Mål:** Konvertere på knapphet.

> `Merkenavn: [Produkt] er tilbake på lager — begrenset antall. Sikre din nå: [kortlenke]`

Send kun til de som faktisk ba om varsel. Dette er en av de mest velkomne SMS-ene du kan sende, fordi mottakeren har bedt om den.

### Vinn-tilbake (sovende kunder)

**Trigger:** 60–90 dager uten kjøp. **Mål:** Vinn tilbake eller rens listen.

| SMS | Timing | Formål |
|-----|--------|--------|
| 1 | 60–90 dager etter siste kjøp | «Vi savner deg» + kuraterte forslag |
| 2 | +14 dager (om ingen kjøp) | Rabattilbud med utløp |
| 3 | +14 dager (siste, om ingen kjøp) | Siste sjanse + tilbud om å melde av |

Etter SMS 3 uten respons: hvil nummeret i minst 90 dager. Etter to fulle vinn-tilbake-sykluser uten engasjement: ta nummeret ut av aktiv liste (det beskytter avmeldingsraten og kutter bortkastet spend). Koordiner med `churn-prevention`.

### Tidsbegrensede tilbud / kampanje (enkeltutsendelse)

**Trigger:** Kampanje, drop, salg. **Mål:** Hast → handling.

- 1–2 utsendelser maks per kampanje
- Koordiner mot e-postplanen så du ikke dobbel-tapper samme dag
- Reelt utløp — falsk hast brukt for ofte dreper troverdigheten

> `Merkenavn: 24-TIMERS SALG: 25 % på alt med BLITS25. Slutter midnatt: [kortlenke]`

**For komplette tekstmaler med tegntelling og segmenteringslogikk per flyt, se [references/flyt-maler.md](references/flyt-maler.md).**

---

## Retningslinjer for SMS-tekst

### Struktur
1. **Avsender** — merkenavnet synlig (alfanumerisk avsender-ID)
2. **Hook** — de første ordene avgjør om de leser videre
3. **Verdi** — hva de får, konkret
4. **CTA + kortlenke** — én handling, én URL
5. **Avmelding** — «Avmelding: [lenke]» (eller «Svar STOPP» ved toveis nummer). Påkrevd på velkomst/bekreftelse, anbefalt på hver markedsførings-SMS.

### Lengde
- **160 tegn (GSM-7)** = 1 melding. Sikt hit. Norske æ/ø/å koster ingenting ekstra her.
- **70 tegn (UCS-2)** hvis du bruker emoji eller enkelte spesialtegn — da betaler du for flere deler.
- **161–306 tegn** = 2 meldinger (du betaler dobbelt). Greit for rikere budskap, men vit at det koster.
- **MMS** (bilde + lengre tekst) = flere ganger SMS-prisen. Bruk sparsomt, til høy-impact-øyeblikk (drop, lookbook).

### Tone
- Samtalende, ikke korporativ. SMS føles personlig — skriv som en melding til en venn, ikke en pressemelding.
- Ingen emnelinje, ingen formatering, ingen salgssjargong.
- Emoji i moderasjon (én, situasjonsbestemt) — men husk kostnaden i tegn.
- VERSALER leses som roping. Unngå, bortsett fra rabattkoder (f.eks. «Bruk VELKOMMEN10»).
- Hold deg til norsk med mindre målgruppen er internasjonal. Nordmenn foretrekker direkte og uformelt.

### Personalisering
- Fornavn-token om tilgjengelig (løfter klikkrate)
- Basert på nylig kjøp/kategori/browse
- Ikke fake intimitet («Hei kompis!») — det slår tilbake

### Timing og frekvens
- **Stilletid:** Send 09–20. Aldri tidlig morgen eller sen kveld — det gir avmeldinger og klager.
- **Frekvenstak:** Maks 4–6 markedsførings-SMS per uke per mottaker; lavere for nye abonnenter.
- **Avkjøling:** Etter et rabattdrevet kjøp, hold markedsførings-SMS tilbake i ~14 dager.
- **Ikke dobbel-tapp:** Undertrykk mottakere som er i en aktiv flyt fra kampanjeutsendelser.

---

## Måling

### Nøkkeltall

| Metrikk | Hva den forteller | Sunt nivå (e-handel) |
|---------|-------------------|----------------------|
| **Opt-in-rate** | Helse i toppen av trakten | 5–25 % av e-postabonnenter |
| **Klikkrate (CTR)** | Relevans i meldingen | 8–15 % (mot ~3 % e-post) |
| **Konvertering per utsendelse** | Omsetningseffekt | 1–5 % per kampanje-SMS |
| **Omsetning per melding** | Kanaløkonomi | Mål den i NOK mot kostnad per SMS |
| **Avmeldingsrate per utsendelse** | Slitasje på publikum | < 2 % per utsendelse, < 0,5 % for kampanjer |
| **Kostnad per melding** | Kostnadsdisiplin | Følg per leverandøravtale i NOK |
| **Listevekst** | Momentum i publikum | 5–15 %/mnd tidlig, 1–3 % stabilt |

### Hva du sporer
- **UTM på hver lenke:** `utm_source=sms&utm_medium=sms&utm_campaign=[kampanjenavn]`
- **Attribusjon:** SMS-drevne økter, sisteklikk-omsetning, assisterte konverteringer
- **LTV-effekt:** SMS-abonnenter mot kun-e-post — SMS-ja har ofte høyere livstidsverdi

### Hva du A/B-tester
- Sendetidspunkt (ettermiddag mot kveld)
- Tekstlengde (kort SMS mot MMS med bilde)
- Rabattnivå og utløser (umiddelbar mot forsinket)
- Personalisering (med fornavn mot uten)
- CTA-tekst («Handle nå» mot «Se den» mot «Siste sjanse»)

Kryssreferer `analytics-tracking` for attribusjonsoppsett og `ab-test-setup` for testdesign.

---

## Leverandørvalg (Norden)

Velg en nordisk leverandør med dokumentert leveranse til norske operatører, støtte for alfanumerisk avsender, og avmeldingshåndtering.

| Leverandør | Egnet for | Notat |
|------------|-----------|-------|
| **Link Mobility** | Mellomstor–stor e-handel, nordisk dekning | Bred operatørintegrasjon, API + plattform |
| **Sveve** | SMB, enkel oppstart, norsk fokus | Greit API, rask i gang |
| **Vianett** | SMB–mellomstor, norsk | API + webgrensesnitt, toveis SMS |

Mange e-handelsplattformer (f.eks. Klaviyo) tilbyr SMS, men sjekk alltid at de leverer til norske operatører og støtter alfanumerisk avsender før du binder deg. Velg ut fra: listestørrelse, behov for toveis dialog, og om du allerede har e-postverktøyet samme sted.

---

## Utdataformat

Når noen ber om en SMS-plan, returner:

1. **Samtykkesjekk:** Har de gyldig § 15-samtykke for SMS spesifikt? Er opt-in-mekanismen lovlig og dokumentert? Flagg blokkere først — uten samtykke stopper alt annet.
2. **Strategi:** Hvilke SMS-flyter de bør bygge først, rangert etter avkastning for deres forretningsmodell.
3. **Flytdesign:** For hver prioritert flyt — trigger, forsinkelse, tekst med tegntelling, CTA, segmentering.
4. **Avsender- og leverandøranbefaling:** Alfanumerisk vs. toveis nummer, og hvilken nordisk leverandør.
5. **Måleplan:** Nøkkeltall, referansenivåer, A/B-testkø.
6. **Avmelding:** Hvordan avmelding håndteres gitt valgt avsendertype.

Vær konkret. Ikke skriv «send SMS til rett tid» — skriv «send 30 min etter forlatt kurv, igjen etter 4 t hvis ingen kjøp, og etter 24 t med rabatt hvis margin tillater».

---

## Oppgavespesifikke spørsmål

1. Har dere dokumentert, SMS-spesifikt samtykke etter markedsføringsloven § 15?
2. Hvilken leverandør bruker eller vurderer dere (Link Mobility, Sveve, Vianett, annet)?
3. Alfanumerisk avsender (ingen svar) eller toveis nummer (kundedialog)?
4. Hvor stor er e-postlisten, og hva er SMS-opt-in-raten (om noen)?
5. Hvilke flyter kjører dere allerede?
6. Er dere ren e-handel, app, eller tjeneste?
7. Hva er hovedmålet: omsetning, aktivering, retensjon eller transaksjonelt?

---

## Vanlige feil

1. **Bygge på e-postsamtykke.** Ja til nyhetsbrev er ikke ja til SMS. § 15 krever spesifikt samtykke — ellers er hele programmet ulovlig.
2. **Behandle SMS som e-post.** Daglige kampanje-blast → avmeldingsraten spiker, listen dør.
3. **Rabatt i første forlatt-kurv-melding.** Lærer kundene å forlate kurven for å få avslag. Reserver til SMS 2 eller 3.
4. **Avsender uten merkenavn.** Mottakeren ser ikke et «fra»-felt — navnet må stå i meldingen (alfanumerisk avsender-ID).
5. **Glemme stilletid.** SMS kl. 06 gir avmeldinger og klager. Hold 09–20.
6. **Manglende avmelding.** Avmelding må fungere i hver melding — lenke ved alfanumerisk avsender, «Svar STOPP» ved toveis. Ikke valgfritt.
7. **Emoji overalt.** Tvinger frem UCS-2, halverer tegngrensen, dobler kostnaden.
8. **Salg i transaksjonell SMS.** Pakker du inn et tilbud i en ordrebekreftelse, blir den markedsføring og krever samtykke.
9. **Ingen attribusjon.** Uten UTM og sporing kan du ikke forsvare kanalens kostnad.
10. **Ingen frekvenstak.** Uten tak slites listen ut og avmeldingsraten eksploderer.

---

## Relaterte Skills

- `email-sequence` — Søsterkanalen. Kjøres nesten alltid sammen: e-post bærer det lange innholdet, SMS bærer det haste-pregede dyttet.
- `churn-prevention` — Vinn-tilbake- og save-flyter som kombinerer SMS + e-post.
- `analytics-tracking` — Attribusjon, UTM og måling av omsetning per melding.
- `storytelling-copywriting` — Tekst og rammeverk for korte, overbevisende meldinger.
- `popup-cro` — Innsamling av telefonnummer og SMS-samtykke via popups.
- `lead-magnets` — Insentiv for opt-in (rabatten du gir for å si ja).
- `ab-test-setup` — Testdesign for SMS-elementer.
- `offers` — Tilbudet (rabatt/bonus/urgency) du faktisk sender i SMS-en.
