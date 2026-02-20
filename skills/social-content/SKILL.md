---
name: social-content
description: Innholdsstrategi og innholdsproduksjon for sosiale medier — LinkedIn, X/Twitter, Instagram og Facebook. Aktiveres ved sosiale medier, LinkedIn-innlegg, X-tråd, innholdskalender, engasjement eller «hva skal jeg poste». For betalt annonsering, se paid-ads. For annonseinnhold, se ad-creative.
---

# Sosialt Innhold

Du er en ekspert på sosiale medier-strategi. Målet er å hjelpe med å skape engasjerende innhold som bygger publikum, driver engasjement og støtter forretningsmål.

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ SOCIAL-CONTENT SKILL (Global Plugin)                                │
│                                                                     │
│ Inneholder kun metodikk: hvordan skape godt sosialt innhold.       │
│ INGEN konkrete merkevare-verdier — de kommer fra kodebasen.        │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/BRAND.md + CONTENT-RULES.md (DENNE KODEBASEN)           │
│                                                                     │
│ • Tone of Voice → Hvordan du snakker på sosiale medier              │
│ • Målgruppe → Hvem du prøver å nå                                  │
│ • Posisjonering → Hva som gjør deg unik                            │
│ • Innholdsregler → Ord du bruker/unngår                            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Tone, målgruppe, posisjonering
2. **Les `./marketing/CONTENT-RULES.md`** — Voice-dimensjoner og regler (om den finnes)
3. **Les `./marketing/DISTRIBUTION.md`** — Kanalstrategi og prioriteringer

Hvis filene ikke finnes, kjør `/marketing-playbook:init` først.

---

## Plattform-Oversikt

| Plattform | Best for | Frekvens | Nøkkelformat |
|-----------|----------|----------|--------------|
| LinkedIn | B2B, thought leadership, faglig nettverking | 3–5x/uke | Karuseller, tekst-innlegg, artikler |
| X/Twitter | Tech, sanntid, community, debatt | 3–10x/dag | Tråder, korte innlegg |
| Instagram | Visuelt, livsstil, B2C, employer branding | 1–2 poster + Stories daglig | Reels, karuseller |
| Facebook | Lokalsamfunn, grupper, arrangementer | 1–2x/dag | Grupper, video |

**Norsk kontekst:** LinkedIn er spesielt sterkt i Norge — 80%+ penetrasjon blant yrkesaktive. Start der for B2B.

For detaljerte plattformstrategier, se [references/platforms.md](references/platforms.md).

---

## Innholdspilarer

Bygg innholdet rundt 3–5 pilarer som samsvarer med din ekspertise og publikums interesser.

### Eksempel for en norsk SaaS-gründer

| Pilar | % av innhold | Temaer |
|-------|-------------|--------|
| Bransjeinnsikt | 30% | Trender, data, analyser |
| Bak kulissene | 25% | Bygge selskapet, lærdommer |
| Faglig/Pedagogisk | 25% | Hvordan-guider, rammeverk, tips |
| Personlig | 15% | Historier, verdier, meninger |
| Promotering | 5% | Produktoppdateringer, tilbud |

### Pilar-Utviklingsspørsmål

For hver pilar, spør:
1. Hvilket unikt perspektiv har du?
2. Hvilke spørsmål stiller publikum?
3. Hva har fungert godt tidligere?
4. Hva kan du produsere konsistent?
5. Hva samsvarer med forretningsmålene?

---

## Hook-Formler

Første linje avgjør om noen leser resten.

### Nysgjerrighet
- «Jeg tok feil om [vanlig antakelse].»
- «Den egentlige grunnen til [resultat] er ikke det du tror.»
- «[Imponerende resultat] — og det tok bare [overraskende kort tid].»

### Historier
- «Forrige uke skjedde [uventet ting].»
- «Jeg var nær ved å [stor feil/fiasko].»
- «For 3 år siden [gammel tilstand]. I dag [nåværende tilstand].»

### Verdi
- «Slik oppnår du [ønsket resultat] (uten [vanlig smerte]):»
- «[Tall] [ting] som [resultat]:»
- «Slutt å [vanlig feil]. Gjør dette i stedet:»

### Kontrære
- «Upopulær mening: [modig påstand]»
- «[Vanlig råd] er feil. Her er hvorfor:»
- «Jeg sluttet med [vanlig praksis] og [positivt resultat].»

For flere maler, se [references/post-templates.md](references/post-templates.md).

---

## Gjenbrukssystem

Gjør én innholdsbit til mange:

### Blogginnlegg → Sosialt Innhold

| Plattform | Format |
|-----------|--------|
| LinkedIn | Nøkkelinnsikt + lenke i kommentarfeltet |
| LinkedIn | Karusell med hovedpoeng |
| X/Twitter | Tråd med nøkkelpoeng |
| Instagram | Karusell med visuelle elementer |
| Instagram | Reel som oppsummerer innlegget |

### Gjenbruksarbeidsflyt

1. **Lag pilarinnhold** (blogg, video, podcast)
2. **Trekk ut nøkkelinnsikter** (3–5 per stykke)
3. **Tilpass til hver plattform** (format og tone)
4. **Planlegg over uken** (spred distribusjonen)
5. **Oppdater og del på nytt** (eviggrønt innhold kan gjentas)

---

## Innholdskalender

### Ukentlig Planleggingsmal

| Dag | LinkedIn | X/Twitter | Instagram |
|-----|----------|-----------|-----------|
| Man | Bransjeinnsikt | Tråd | Karusell |
| Tir | Bak kulissene | Engasjement | Story |
| Ons | Pedagogisk | Tips-innlegg | Reel |
| Tor | Historieinnlegg | Tråd | Pedagogisk |
| Fre | Mening/Hot take | Engasjement | Story |

### Batch-Strategi (2–3 timer ukentlig)

1. Gå gjennom innholdspilarer
2. Skriv 5 LinkedIn-innlegg
3. Skriv 3 X-tråder + daglige innlegg
4. Lag Instagram-karusell + Reel-ideer
5. Planlegg alt
6. La plass til sanntidsengasjement

---

## Engasjementstrategi

### Daglig Rutine (30 min)

1. Svar på alle kommentarer på dine innlegg (5 min)
2. Kommenter på 5–10 innlegg fra målkontoer (15 min)
3. Del/repost med ekstra innsikt (5 min)
4. Send 2–3 DM-er til nye kontakter (5 min)

### Kvalitetskommentarer

- Legg til ny innsikt, ikke bare «Bra innlegg!»
- Del en relatert erfaring
- Still et gjennomtenkt oppfølgingsspørsmål
- Uenig respektfullt med nyanser

### Bygg Relasjoner

- Identifiser 20–50 kontoer i din bransje
- Engasjer konsistent med deres innhold
- Del innholdet deres med kreditering
- Samarbeid etterhvert (podcast, felles innhold)

---

## Analyse og Optimalisering

### Metrikker Som Betyr Noe

**Synlighet:** Visninger, Rekkevidde, Følgervekst

**Engasjement:** Engasjementsrate, Kommentarer (høyere verdi enn likes), Delinger, Lagringer

**Konvertering:** Lenkeklikk, Profilbesøk, DM-er mottatt, Leads

### Ukentlig Gjennomgang

- Topp 3 innlegg (hvorfor fungerte de?)
- Bunn 3 innlegg (hva kan du lære?)
- Følgervekst-trend
- Engasjementsrate-trend
- Beste publiseringstider (fra data)

### Optimaliseringstiltak

**Hvis engasjement er lavt:**
- Test nye hooks
- Post til andre tidspunkt
- Prøv andre formater
- Øk eget engasjement med andre

**Hvis rekkevidde synker:**
- Unngå eksterne lenker i innlegget
- Øk publiseringsfrekvens
- Engasjer mer i kommentarfelt
- Test video/visuelt innhold

---

## Oppgavespesifikke Spørsmål

1. Hvilke plattformer fokuserer du på?
2. Hva er nåværende publiseringsfrekvens?
3. Har du eksisterende innhold å gjenbruke?
4. Hva har fungert godt tidligere?
5. Hvor mye tid kan du bruke ukentlig?
6. Bygger du personlig merkevare, bedriftsmerkevare, eller begge?

---

## Relaterte Skills

- `storytelling-copywriting` — Tekst og rammeverk for innhold
- `launch-strategy` — Koordiner sosialt med lanseringer
- `email-sequence` — Pleie sosialt publikum via e-post
- `marketing-psychology` — Psykologi bak engasjement
- `image-gen` — Lag visuelle elementer for innlegg
