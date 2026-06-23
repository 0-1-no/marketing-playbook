# GEO-rubrikker — Citability & E-E-A-T-scoring

> **Metodikk-fil for `ai-seo`.** To operative rubrikker for å score innhold før publisering:
> (1) Citability — vil AI faktisk sitere denne passasjen? (2) E-E-A-T — fortjener siden tillit?
> Faktiske søkeord og sider hører hjemme i `./marketing/DISTRIBUTION.md`, ikke her.

AEO-fundamentet (answer blocks, FAQ-struktur, tredjeparts tilstedeværelse) ligger i `seo-aeo/AEO.md`.
Denne filen går dypere på *selve passasjen* og *selve siden*: hva som gjør tekst sitérbar, og hva som gjør en kilde verdt å stole på.

---

## 1. Citability-rubrikk — skriv passasjer AI faktisk siterer

En AI-modell siterer ikke en side. Den siterer en **passasje** — en avgrenset bit tekst som svarer på spørsmålet brukeren stilte. Jobben din er å skrive passasjer som kan løftes rett ut og limes inn i et svar uten redigering. Tenk på det som å skrive sitater modellen *vil* bruke fordi de gjør svaret bedre.

`seo-aeo/AEO.md` lærer deg 40–60-ords answer blocks for korte, faktuelle svar (definisjoner, «hva er X»). Denne rubrikken dekker det **lengre, selvstendige avsnittet** (~130–170 ord) som svarer på et reelt spørsmål med svar + støtte — formatet AI-søk siterer for «hvordan/hvorfor/hvilken»-spørsmål, der et tørt ett-setnings-svar ikke holder.

### De fire egenskapene

| Egenskap | Hva det betyr | Hvorfor det får sitering |
|----------|---------------|--------------------------|
| **Selvstendig** | Passasjen gir mening løsrevet fra resten av siden. Ingen «som nevnt over», «dette», «derfor» som peker utenfor avsnittet. | AI henter ett avsnitt om gangen. Peker det utenfor seg selv, blir det ubrukelig som sitat. |
| **Fakta-tett** | Tall, datoer, navn, prosenter, konkrete eksempler — ikke generelle påstander. | Modellen foretrekker verifiserbart innhold. «42 % i 2024» slår «mange». |
| **Unik** | Egen data, eget førstehånds-funn, eller en vinkel ingen andre har. Ikke en omskriving av det alle andre sier. | Hvis ti sider sier det samme, siterer modellen Wikipedia. Unikt innhold er den eneste grunnen til å sitere *deg*. |
| **Svar-først** | Konklusjonen i første setning, så støtten. Ikke bygg opp til svaret. | AI klipper ofte bare første 1–2 setninger. Ligger svaret sist, mister du siteringen. |

### Lengde: hvorfor ~130–170 ord

For kort (under ~100 ord) → ikke nok substans til å stå alene som et fullverdig svar; modellen må kombinere flere kilder og kan droppe deg.
For langt (over ~200 ord) → modellen må klippe, og klipper den feil sted faller poenget ditt ut.
~130–170 ord treffer sweet spot: svar + nok støtte/kontekst til å være selvstendig, men kompakt nok til å siteres helt.

### Mapping: én passasje = ett spørsmål

Skriv hver passasje mot **ett konkret spørsmål en bruker ville stilt en AI** («Hvor lang tid tar SEO før det virker?»), ikke mot et søkeord («SEO tid»). AI-søk er konversasjonelt. En passasje som prøver å svare på tre spørsmål samtidig siteres for ingen av dem. Én side kan ha mange slike passasjer — én per spørsmål du vil eie.

### Scoringssjekk (kjør på hver passasje før publisering)

```
[ ] Selvstendig?  — Gir avsnittet mening klippet ut alene, uten resten av siden?
[ ] Fakta-tett?   — Minst ett konkret tall/dato/navn/eksempel?
[ ] Unik?         — Sier den noe egne data/innsikt gir som konkurrenter ikke har?
[ ] Svar-først?   — Står konklusjonen i første setning?
```

4/4 = sitérbar. 3/4 = fiks det manglende før publisering. ≤2/4 = skriv om — dette blir ikke sitert.

### Eksempel

**Svakt (0/4 — bygger opp, generisk, peker utenfor seg selv):**
```
Som vi diskuterte tidligere er dette et komplekst spørsmål. Det avhenger
av mange faktorer, og resultater varierer fra bedrift til bedrift. Men
over tid vil de fleste se en effekt hvis de er tålmodige og gjør jobben
riktig.
```

**Sterkt (4/4 — svar-først, fakta-tett, unikt, selvstendig):**
```
SEO tar typisk 4–6 måneder før det gir målbar trafikkvekst for et nytt
domene. I vår analyse av 38 norske SMB-nettsteder (2024) så de som
publiserte minst to artikler i måneden første synlige ranking-løft etter
median 19 uker, mens de som publiserte sporadisk brukte over 30 uker.
Tre faktorer forklarte mesteparten av variasjonen: domenealder,
publiseringsfrekvens og om innholdet svarte på reelle søk. Ferske domener
uten autoritet er den vanligste årsaken til lange tidshorisonter.
```

---

## 2. E-E-A-T-scoring (4 × 25 poeng)

E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) er ikke et rangeringssignal Google leser direkte — det er rammeverket *kvalitetsvurdererne* deres bruker for å bedømme om en side fortjener tillit, og AI-modeller vekter de samme signalene når de velger kilder. Tidligere ble E-E-A-T mest knyttet til YMYL (Your Money or Your Life — helse, finans, jus). **Googles Quality Rater Guidelines anvender det nå bredt på alt innhold** — ikke bare høyrisiko-temaer. Behandle det som en baseline for enhver side du vil ha sitert.

`seo-aeo/AEO.md` har signal-tabellen («hva er E-E-A-T»). Denne rubrikken gjør det til et **scoringsverktøy**: gi siden poeng, finn det svakeste benet, fiks det.

Scoren er en grov selvevaluering, ikke en eksakt vitenskap. Verdien ligger i å tvinge fram det svakeste benet — en side med 25/25 på Expertise men 5/25 på Trustworthiness (ingen kontaktinfo, ingen kilder, gammel dato) blir ikke sitert. AI vekter den svakeste lenken hardt.

### Experience (0–25) — førstehånds erfaring

Har forfatteren *faktisk gjort* det de skriver om? Dette er det nyeste E-et og det som skiller ekte innhold fra AI-generert massevare.

| Poeng | Kjennetegn |
|-------|------------|
| 20–25 | Egen primærdata/undersøkelse, dokumenterte case studies med tall, «vi testet X på Y kunder» |
| 10–19 | Konkrete egne eksempler og anekdoter, men ingen systematisk data |
| 1–9 | Generelle påstander uten førstehånds-belegg |
| 0 | Tydelig rewrite av andres innhold, ingen egen erfaring |

### Expertise (0–25) — fagkompetanse

Har forfatteren kompetansen? Vises den i dybden og metodikken?

| Poeng | Kjennetegn |
|-------|------------|
| 20–25 | Navngitt forfatter med relevante credentials/sertifiseringer + synlig metodikk + faglig dybde |
| 10–19 | Forfatter-bio finnes, innholdet er kompetent men overflatisk på metode |
| 1–9 | Anonymt eller tynt; korrekt men uten dybde |
| 0 | Faktafeil eller misvisende — negativ ekspertise |

### Authoritativeness (0–25) — autoritet i markedet

Anerkjenner *andre* deg som en kilde? Dette bygges utenfor egen side.

| Poeng | Kjennetegn |
|-------|------------|
| 20–25 | Sitert/omtalt av uavhengige kilder, sterk topical authority (eier temaet på tvers av sider), bransjeposisjon |
| 10–19 | Noe ekstern omtale, voksende dekning av temaet |
| 1–9 | Lite ekstern validering, spredt tematikk |
| 0 | Ingen som refererer deg; ny eller ukjent aktør |

> Topical authority = du dekker et tema *uttømmende* på tvers av flere sider, ikke bare én. AI bygger entity-forståelse: behandles du konsekvent som kilden på «X», siteres du for X.

### Trustworthiness (0–25) — tillit

Det viktigste benet ifølge Google. Kan en leser (og en modell) stole på siden?

| Poeng | Kjennetegn |
|-------|------------|
| 20–25 | Synlig kontaktinfo + navngitte kilder/referanser + fersk `dateModified` + transparent om interessekonflikter + HTTPS |
| 10–19 | De fleste tillitssignaler på plass, men hull (f.eks. mangler dato eller kilder) |
| 1–9 | Få tillitssignaler; anonymt, udatert, ukildet |
| 0 | Aktive røde flagg (skjult eierskap, falske påstander, ingen kontaktvei) |

### Scoringssjekk

```
Experience       __ / 25
Expertise        __ / 25
Authoritativeness __ / 25
Trustworthiness  __ / 25
─────────────────────────
TOTAL            __ / 100
```

**Slik bruker du tallet:** ikke jag 100/100. Finn det **laveste** benet og løft det først — det er der du taper sitering. Typisk billigste løft for de fleste sider: Trustworthiness (legg til kontaktinfo, kilder, synlig oppdateringsdato) og Experience (bytt en generisk påstand mot ett konkret egen-tall).

| Total | Tolkning |
|-------|----------|
| 80–100 | Sterk sitering-kandidat |
| 60–79 | Solid, men ett ben drar ned — fiks det |
| 40–59 | Blir sjelden sitert; adresser de to svakeste benene |
| <40 | Lav tillit — strukturell jobb før AEO-taktikk har effekt |
