# Plan-mal — 9-seksjons strukturen

Kanonisk mal for hver markedsplan skillen lager. Hver seksjon har et formål, en struktur og hva du henter fra `./marketing/`-filene. Alle faktiske tall, kanaler og posisjonering kommer fra prosjektets filer — aldri hardkodet her.

**Rekkefølge:** Skriv seksjon 2→9 i numerisk rekkefølge, deretter seksjon 1 (sammendrag) til slutt. Det ferdige dokumentet presenteres alltid i rekkefølge 1→9.

---

## Tittelblokk

```markdown
# {Virksomhet} — Markedsplan v1

**Utarbeidet av:** {navn / rolle}
**For:** {ledelse / styre / klient}
**Dato:** ÅÅÅÅ-MM-DD
**Status:** Utkast v1 — til gjennomgang
```

---

## Seksjon 1 — Sammendrag

**Formål:** Løft-og-del. En markedssjef skal kunne lime dette inn i en styre-oppdatering uten redigering.

**Lengde:** 300–600 ord. Stramt. **Skrives sist, presenteres først.**

**Struktur:**
1. **Én-setnings ramme.** Hva optimaliserer planen for? Ikke «mer omsetning» — noe spesifikt for denne virksomheten på dette stadiet.
2. **Tre store veddemål, rangert etter løftekraft.** Hvert er et avsnitt. Et veddemål = en høy-overbevisning tese om hvor teamet bør fokusere kapital og oppmerksomhet. (Spar med `marketing-mindset` — «strategi er hva du IKKE gjør».)
3. **Hva 12 måneder plausibelt ser ut som.** Punktliste. Utfallstilstand ved planhorisontens slutt. Styre-lesbart.
4. **90-dagers prioriteringer.** Nummerert liste — de ~6 trekkene som shippes i Q1.

**Tone:** Match BRAND.md. Direkte, leder-lesbart, ingen markedssjargong. Navn og tall (konkrete kanaler, konkrete metrikker), ikke abstraksjoner. Trade-offs navngitt eksplisitt.

---

## Seksjon 2 — Situasjonsanalyse

**Formål:** Forankre planen i virkeligheten — marked, konkurranse, hva som fungerer, hva som er fastlåst i dag.

**Henter fra:** LEARNINGS.md (hva fungerer, BAF-status, segmenter), BRAND.md (push/pull/vane/angst), live-data (PostHog/GA4/Stripe/Ahrefs).

**Struktur:**

### Markedet & konkurransen
Switching-kreftene fra BRAND.md i tabell:

| Kraft | Retning | Hva det betyr for oss |
|-------|---------|------------------------|
| Push | Bort fra dagens løsning | |
| Pull | Mot oss | |
| Vane | Holder dem igjen | |
| Angst | Hindrer bytte | |

### Funnel-tilstand i dag
Nåværende tall (besøk → signups → aktivering → betalende → retention). Funnel-*formen*: hvor er den største lekkasjen — topp, midt eller bunn? Vær ærlig om dårlige tall.

### Hva fungerer (fra LEARNINGS.md)
Dokumenterte innsikter, hvilke segmenter som faktisk konverterer, BAF-status (er merkevaren validert?).

### Hva er fastlåst
| Problem | Kostnad av passivitet | Tiltak |
|---------|------------------------|--------|

Fastlåste ting er de mest løftepositive stedene å fokusere de første ukene av roadmapen.

---

## Seksjon 3 — Mål & OKR

**Formål:** Definere hva suksess er, tallfestet.

**Struktur:**

### North star-metrikk (foreslått)
Én metrikk som fanger forretningsmodell-tesen. B2B SaaS: NRR × NPS. Forbruker: blended LTV/CAC. Markedsplass: take-rate × månedlige transaherende brukere. Gjør den spesifikk — ikke generisk «ARR-vekst».

### Resultater (KPI-er)
3–5 målbare resultater med tallfestet target og tidsfrist:

| Resultat (KPI) | Baseline i dag | Target (12 mnd) |
|----------------|----------------|------------------|

---

## Seksjon 4 — Målgruppe & posisjonering

**Formål:** Destillere ICP, anti-persona og posisjonering til én side enhver i teamet kan lese for å orientere seg.

**Henter fra:** BRAND.md (ABC-rammeverket).

**Struktur:**
- **Hva {virksomhet} er, i én setning** — fra posisjoneringen i BRAND.md
- **Kategorien vi hevder** — ny kategori, redefinerer en, eller konkurrerer i en definert? Navngi den.
- **Hvem vi er for (ICP, destillert)** — demografi/firmografi + uttalt problem vs. ekte problem + hva de *egentlig* kjøper. 4–6 punkter.
- **Anti-persona** — hvem vi IKKE vil nå (høy churn, lav NPS, mye support). Like viktig som ICP.
- **Tone of voice (ikke-forhandlebar)** — «Words We Use/Avoid», CTA-regler, tone fra BRAND.md. Hver annen seksjon må respektere dette.

Hvis posisjoneringen er uklar eller selvmotsigende på tvers av materialet — flagg det i seksjon 9.

---

## Seksjon 5 — Kanal-mix (60:40)

**Formål:** Svare «hvordan blir fremmede klar over oss, og hvordan konverterer/beholder/utvider vi dem?» Mappe hver kanal: nåtilstand, planlagte trekk, droppet (med begrunnelse).

**Henter fra:** DISTRIBUTION.md (aktive kanaler, stack, SEO/AEO), JOURNEY.md (touchpoints per stadie).

**Struktur — organisert per AARRR-stadie:**

For hvert stadie (Acquisition / Activation / Retention / Referral / Revenue):
- **Nåtilstand** — kort. Hva fungerer i dag, hva ikke.
- **Trekkene** — nummererte «Trekk». Hvert trekk er et avsnitt (3–6 setninger): kanalen, tesen, det konkrete arbeidet. **Hvert trekk tagges med AARRR-stadie og navngir skillen + verktøyet som eksekverer det.**

Vanlige trekk per stadie:
- **Acquisition** — SEO/innhold (`seo-aeo`), grunnlegger-drevne kanaler (LinkedIn for B2B), PR-forsterkning, betalt lag når budsjett låses opp (`paid-ads`)
- **Activation** — fiks ødelagt signup/onboarding, onboarding-test/ombygging, landingssider, paywall-review
- **Retention** — lifecycle-email (`email-sequence`), churn-forsoning (`churn-prevention`), win-back
- **Referral** — ambassadør/affiliate-program (`referral-program`), del-etter-verdi-øyeblikk
- **Revenue** — pris-audit (`pricing-strategy`), årsplan-default-test, B2B case studies

### Drop-liste
Hva dere bevisst IKKE gjør, med begrunnelse. En drop-liste uten begrunnelse er bare fravær.

### Eide > leide (ORB)
Driv trafikk til eide kanaler (e-postliste, community, blogg). Leide kanaler (LinkedIn, IG, app stores) er distribusjon, ikke fundament. Se `launch-strategy`.

---

## Seksjon 6 — Budsjett-allokering

**Formål:** Vise budsjettet utledet vitenskapelig, fordelt på stadier og 60:40.

**Henter fra:** DISTRIBUTION.md (budsjettlinjer), intervju (CAC, ARPC, churn).

**Struktur:**

### Nåværende budsjett (brutt ned)
| Linje | Kr/mnd | Note |
|-------|--------|------|
| Betalt akkvisisjon | | |
| Verktøy / stack | | |
| Byrå / retainere | | |
| Bemanning | | |

Blended CAC (inkl. lønn, innhold, verktøy — ikke bare annonsekroner). Andel av ARR i dag (sammenlign mot 5–40 %).

### Enhetsøkonomi
| Metrikk | Verdi | Note |
|---------|-------|------|
| ARPC (snitt mnd-inntekt/kunde) | | |
| Blended CAC | | |
| Årlig retention | | 1 − churn |
| LTV (grov) | | ARPC × 12 / churn |
| LTV / CAC | | Sunt: > 3 |

Er noen av disse ukjent — flagg i seksjon 9 som høyest-rangerte åpne beslutning.

### Budsjett-metode (vis regnestykket)
Metode 1 (inntektsbasert 5–40 % av ARR) ELLER Metode 2 (målbasert formel). Vis de fire stegene. Legg på 10–20 % eksperiment-budsjett. Resulterende 12-måneders mål (ærlig prognose, ikke garanti).

### Fordeling
På AARRR-stadier + 60:40 brand/aktivering. Hva som vokser når neste finansieringstrinn låses opp.

---

## Seksjon 7 — Kvartals-roadmap (12 mnd)

**Formål:** Eksekveringslaget. Kvartalsvise milepæler + 90-dagers nedbrytning med eier.

**Struktur:**

### 12-måneders ramme
Per kvartal (~150–250 ord):

#### Q{N} — Måned {X}–{Y}
- **Finansieringstilstand:** {trinn}
- **Fokus:** Én-setnings tema
- **Utfall ved slutt av Q{N}:** 5–8 punkter
- **KPI-targets:** 3–5 tallfestede targets

### 90-dagers nedbrytning (Q1)
Fire 2–3-ukers sprinter, hver rad med **eier**:

| Trekk | AARRR-stadie | Eier |
|-------|--------------|------|

- **Uke 1–2 — Fjern blokkering** — høyest-konfidens, lavest-kostnad. Fiks det som er ødelagt.
- **Uke 3–4 — Fundament** — pillar-arbeid, første innhold, første flows, første tester live.
- **Uke 5–8 — Fart** — renters-rente-arbeid begynner. Innholds-kadens, repeterte tester, kanal-skalering.
- **Uke 9–12 — Renters rente** — andre-ordens trekk, lagdelte taktikker, 90-dagers review-prep.

---

## Seksjon 8 — Måling & KPI-er

**Formål:** Definere hvordan planen måles og hvem som eier hva.

**Henter fra:** JOURNEY.md (touchpoints), `analytics-tracking` (sporingsplan).

**Struktur:**

### Ledende indikatorer per AARRR-stadie
| Stadie | Ledende indikatorer |
|--------|---------------------|
| Acquisition | |
| Activation | |
| Retention | |
| Referral | |
| Revenue | |

### Review-kadens
- Ukentlig: hvem synker med hvem, om hva
- Månedlig: hvem reviewer hva
- Kvartalsvis: når planen rekalibreres

### RACI
| Område | Ansvarlig (R) | Beslutter (A) | Konsultert (C) | Informert (I) |
|--------|---------------|----------------|-----------------|----------------|

Vanlige områder: strategisk plan, brand voice, SEO/innhold, betalt, lifecycle, ambassadører, prising, ansettelser.

> **Måle-advarsel** (`marketing-mindset`): det du måler er det du får. Mål det som faktisk betyr noe — vanity metrics er farlige. Vær skeptisk til attribusjonsmodeller; test med holdout-grupper når mulig.

---

## Seksjon 9 — Risiko & åpne beslutninger

**Formål:** Operasjonell avslutning. Hva er fortsatt TBD, og hva blokkerer det?

**Struktur:**

### Åpne beslutninger (rangert etter effekt)
Hver: navn + effekt + hva som blokkeres.

1. (høyest effekt) — **CAC ukjent** er nesten alltid #1: hvert inntektsestimat avhenger av den.
2. ...

### Risiko
| Risiko | Sannsynlighet | Konsekvens | Mottiltak |
|--------|---------------|------------|-----------|

### Avhengigheter
Hva planen forutsetter som ikke er bekreftet (kapitalrunde, ansettelse, produkt-GA, partnerskap).

---

## Avslutningslinje

```markdown
*{Virksomhet} markedsplan v1. Utarbeidet av {navn}, {dato}. Til gjennomgang og diskusjon.*
```

---

## Per-seksjon heuristikk: «er denne seksjonen ferdig?»

- **Seksjon 1** — En utenforstående forstår vekst-tesen fra denne alene.
- **Seksjon 2** — Dårlige tall er navngitt, ikke skjult.
- **Seksjon 3** — North star er spesifikk for denne virksomheten, ikke generisk.
- **Seksjon 4** — Tone-reglene er eksplisitte nok til at en ny tekstforfatter kan følge dem.
- **Seksjon 5** — Hvert trekk navngir en skill og et verktøy. Drop-listen har begrunnelse.
- **Seksjon 6** — Budsjettet er utledet med Metode 1 eller 2, regnestykket er vist.
- **Seksjon 7** — Hver Q1-rad har eier. Hvert kvartal navngir finansieringstrinnet.
- **Seksjon 8** — North star og ledende indikatorer er koblet til faktiske flater.
- **Seksjon 9** — CAC-status er adressert. Hver TBD fra intervjuet er her, ikke i brødteksten.
