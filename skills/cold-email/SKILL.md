---
name: cold-email
description: B2B cold outreach — e-postformler, deliverability, personalisering og angle rotation. Aktiveres ved cold email, kald e-post, outbound, prospektering, lead generation eller «nå ut til potensielle kunder». For e-postsekvenser (varme leads), se email-sequence. For lead scoring, se revops.
---

# Cold Email

Du er en ekspert på B2B cold email outreach. Målet er å skrive e-poster som åpnes, leses og besvares — uten å havne i spam.

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Posisjonering og differensiatorer
2. **Les `./marketing/JOURNEY.md`** — Awareness-fasen

---

## 4 Cold Email-formler

### 1. Problem-Solution

```
Hei [Fornavn],

[Problem de har — spesifikt og gjenkjennelig].

Vi hjelper [type bedrift] med å [løsning], noe som typisk gir [konkret resultat].

[Sosial bevis: "Vi hjalp [lignende bedrift] med å [resultat]."]

Er dette relevant for [bedriftsnavn]?

[Signatur]
```

### 2. Question-Led

```
Hei [Fornavn],

Har [bedriftsnavn] vurdert å [handling relatert til ditt produkt]?

Spør fordi [grunn — gjerne en observasjon om deres bedrift].

[Kort pitch — 1-2 setninger].

Verdt en kort samtale?

[Signatur]
```

### 3. Insight-Led

```
Hei [Fornavn],

Jeg la merke til [spesifikk observasjon om deres bedrift/nettside/produkt].

[Innsikt: Hva dette betyr / mulighet de går glipp av].

Vi har hjulpet [lignende bedrift] med akkurat dette — [kort resultat].

Åpen for en 15-minutters prat?

[Signatur]
```

### 4. Social Proof-Led

```
Hei [Fornavn],

[Referansebedrift] begynte å bruke [ditt produkt] i [måned] og oppnådde [konkret resultat].

De hadde lignende utfordringer som [bedriftsnavn]: [1-2 spesifikke paralleller].

Er [dag] eller [dag] mulig for en kort intro?

[Signatur]
```

---

## 3-tier Voice

| Tier | Tone | Best for | Eksempel åpning |
|------|------|----------|-----------------|
| **Formal** | Profesjonell, respektfull | Enterprise, C-suite | «Jeg tar kontakt angående...» |
| **Conversational** | Uformell, personlig | SMB, mellomledere | «Hei [Navn], jeg la merke til at...» |
| **Bold** | Direkte, utfordrende | Startup, innovative | «[Bedriftsnavn] kaster penger ut vinduet på [ting].» |

**Norsk kontekst:** Conversational fungerer best i Norge. Nordmenn er generelt uformelle i forretningskommunikasjon.

---

## Angle Rotation

Ikke send samme vinkel til hele listen. Rotér mellom 3–5 angles:

| Angle | Eksempel |
|-------|----------|
| **Pain point** | «Sliter dere med [problem]?» |
| **Trigger event** | «Gratulerer med [hendelse] — dette betyr ofte at...» |
| **Competitor** | «Mange som bruker [konkurrent] bytter fordi...» |
| **Industry insight** | «I [bransje] ser vi at [trend]...» |
| **Mutual connection** | «[Felles kontakt] foreslo at vi burde snakke.» |

---

## Breakup Email

Siste e-post i sekvensen. Signaliserer at du gir opp (men ofte den med høyest reply-rate):

```
Hei [Fornavn],

Jeg har sendt et par e-poster uten svar, så jeg antar at timing
ikke er riktig akkurat nå.

Ingen problem — jeg legger deg ikke til igjen.

Hvis [smertepunkt] blir aktuelt senere, er det bare å svare
på denne e-posten.

Lykke til videre!

[Signatur]
```

---

## Deliverability-sjekkliste

### Teknisk oppsett

- [ ] **SPF** — Sett opp i DNS
- [ ] **DKIM** — Signer e-poster
- [ ] **DMARC** — Policy konfigurert
- [ ] **Custom tracking domain** — Ikke bruk default fra e-postverktøy
- [ ] **Dedikert sending-domene** — Ikke bruk primærdomene for cold email

### Domain Warmup

| Uke | Volum | Mål |
|-----|-------|-----|
| 1 | 10–20/dag | Etabler avsenderrykte |
| 2 | 20–40/dag | Bygg volum gradvis |
| 3 | 40–60/dag | Monitorer bounce/spam |
| 4+ | 60–100/dag | Full kapasitet |

### Innholdsregler

- [ ] Ingen bilder i cold emails
- [ ] Maks 1 lenke (signatur teller ikke)
- [ ] Unngå spam-trigger-ord (gratis, tilbud, rabatt, 100%)
- [ ] Personalisering i emnelinje og/eller åpning
- [ ] Kort — under 150 ord

---

## Sekvensstruktur

| E-post | Dag | Vinkel |
|--------|-----|--------|
| 1 | 0 | Hovedpitch (Problem-Solution eller Insight) |
| 2 | 3 | Sosial bevis |
| 3 | 7 | Ny vinkel (angle rotation) |
| 4 | 12 | Verdi-tillegg (relevant innhold/innsikt) |
| 5 | 18 | Breakup email |

---

## Reply-rate Benchmarks

| Metrikk | Dårlig | OK | Bra |
|---------|--------|-----|-----|
| Open rate | <30% | 30–50% | 50%+ |
| Reply rate | <2% | 2–5% | 5%+ |
| Positive reply rate | <1% | 1–3% | 3%+ |
| Bounce rate | >5% | 2–5% | <2% |
| Unsubscribe rate | >1% | 0.5–1% | <0.5% |

---

## Norsk Cold Email-kontekst

- **GDPR:** Legitim interesse (B2B) kan brukes, men dokumenter grunnlag
- **Markedsføringsloven § 15:** E-post til bedrifter er tillatt (B2B), men ikke B2C uten samtykke
- **Tone:** Uformell og direkte. «Du» er standard, ikke «De»
- **Timing:** Tirsdag–torsdag 09:00–11:00 er best

---

## Sjekkliste

- [ ] SPF/DKIM/DMARC konfigurert
- [ ] Dedikert sending-domene
- [ ] Domain warmup gjennomført
- [ ] 3+ angles forberedt
- [ ] 5-e-post sekvens med breakup
- [ ] Personalisering per mottaker
- [ ] Under 150 ord per e-post
- [ ] Benchmarks satt for open/reply rate

---

## Relaterte Skills

- `revops` — Lead scoring og pipeline-håndtering
- `email-sequence` — Varme lead-sekvenser (ikke cold)
- `sales-enablement` — Støttemateriell for salgsprosessen
- `analytics-tracking` — Mål kampanjeytelse
