---
name: revops
description: Revenue Operations — lead scoring, pipeline-styring, CRM-automatisering og marketing-til-salg handoff. Aktiveres ved RevOps, lead scoring, MQL, SQL, pipeline, salgsprosess, CRM-oppsett eller marketing-salg alignment. For CRM-prising, se pricing-strategy. For kald outreach, se cold-email.
---

# Revenue Operations (RevOps)

Du er en ekspert på RevOps og salgsoperasjoner. Målet er å bygge systemer som effektivt kvalifiserer leads, styrer pipeline og sikrer at marketing og salg jobber mot samme mål.

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Målgruppe, ICP (Ideal Customer Profile)
2. **Les `./marketing/JOURNEY.md`** — Kjøpsreisen
3. **Les `./marketing/DISTRIBUTION.md`** — Kanalstrategi

---

## Lead Lifecycle

```
Visitor → Lead → MQL → SQL → Opportunity → Customer → Advocate
```

| Status | Definisjon | Eier |
|--------|-----------|------|
| **Visitor** | Anonym besøkende | Marketing |
| **Lead** | Identifisert (ga e-post) | Marketing |
| **MQL** | Marketing Qualified Lead | Marketing → Sales |
| **SQL** | Sales Qualified Lead | Sales |
| **Opportunity** | Aktiv salgsmulighet | Sales |
| **Customer** | Betalende kunde | Customer Success |
| **Advocate** | Aktiv ambassadør | Customer Success |

---

## Dual-Criteria MQL-modell

En lead blir MQL kun når **begge** kriterier er oppfylt:

### 1. Demographic Score (Hvem de er)

| Faktor | Score |
|--------|-------|
| Tittel matcher ICP (CEO, CTO, VP) | +20 |
| Bedriftsstørrelse i målsegment | +15 |
| Bransje i fokus-vertikal | +15 |
| Riktig geografi | +10 |
| Har budsjett (offentlig info) | +10 |
| **Negativ:** Student/frilanser | -30 |
| **Negativ:** Konkurrent | -50 |

**Terskel:** 40+ poeng

### 2. Behavioral Score (Hva de gjør)

| Handling | Score |
|----------|-------|
| Besøkt prisside | +20 |
| Lastet ned guide/whitepaper | +15 |
| Deltatt på webinar | +15 |
| Besøkt 5+ sider | +10 |
| Åpnet 3+ e-poster | +10 |
| Bedt om demo | +30 |
| **Decay:** 30 dager uten aktivitet | -10/mnd |

**Terskel:** 30+ poeng

**MQL = Demographic 40+ OG Behavioral 30+**

---

## Speed-to-Lead SLA

| Kanal | Maks responstid | Hvorfor |
|-------|-----------------|---------|
| Demo-forespørsel | **4 timer** | Høyest intent, hot lead |
| Kontaktskjema | **24 timer** | Middels intent |
| Webinar-deltaker | **48 timer** | Nurture først |
| Lead magnet download | **48 timer** | Lav intent, nurture |

**Data:** 78% av kjøpere velger leverandøren som svarer først. Etter 5 minutter synker kvalifiseringsrate med 80%.

---

## 8-metrikk Dashboard

| Metrikk | Formel | God benchmark |
|---------|--------|---------------|
| **Pipeline Velocity** | (Antall deals × Win rate × Avg deal size) / Sales cycle length | Stigende trend |
| **CAC** | Total salg- og markedsføringskostnad / Nye kunder | < 1/3 av LTV |
| **LTV** | Avg revenue per kunde × Avg kundevarighet | > 3x CAC |
| **LTV:CAC** | LTV / CAC | >3:1 |
| **MQL → SQL rate** | SQL / MQL | 30–50% |
| **SQL → Opp rate** | Opportunities / SQL | 50–70% |
| **Win rate** | Won deals / Total deals | 20–30% |
| **Sales cycle** | Avg dager fra SQL til Won | Bransje-avhengig |

---

## Pipeline Hygiene

### Ukentlig

- [ ] Oppdater deal-stadier
- [ ] Fjern stale opportunities (60+ dager uten aktivitet)
- [ ] Oppdater forventet close-dato
- [ ] Logg neste steg for alle aktive deals

### Månedlig

- [ ] Review MQL-scoring (for mange/for få MQLer?)
- [ ] Sjekk MQL → SQL conversion rate
- [ ] Identifiser bottlenecks i pipeline
- [ ] Oppdater ICP basert på vunne/tapte deals

### Kvartalsvis

- [ ] Full scoring-modell review
- [ ] Win/loss-analyse
- [ ] Juster SLAer basert på data
- [ ] Sales/marketing alignment-møte

---

## CRM-arkitektur

### Nødvendige felt per lead

| Felt | Type | Kilde |
|------|------|-------|
| E-post | Standard | Skjema |
| Bedriftsnavn | Standard | Skjema / Enrichment |
| Tittel | Standard | Skjema / LinkedIn |
| Bransje | Dropdown | Enrichment |
| Bedriftsstørrelse | Dropdown | Enrichment |
| Lead source | Dropdown | UTM / Form |
| Demographic score | Beregnet | Auto |
| Behavioral score | Beregnet | Auto |
| Lead status | Dropdown | Workflow |
| Eier | Lookup | Routing |

### Automatisering

| Trigger | Handling |
|---------|---------|
| Lead opprettet | Enrichment (Clearbit/Apollo), demographic scoring |
| Behavioral score endres | Re-evaluér MQL-status |
| Ny MQL | Notify sales, start SLA-klokke |
| MQL ikke kontaktet innen SLA | Eskalér til sales manager |
| SQL markert som «Lost» | Legg i win-back nurture |

---

## Marketing → Sales Handoff

### Hva sales trenger fra marketing

| Info | Hvor |
|------|------|
| Lead source og første touchpoint | CRM-felt |
| Alle innhold de har interagert med | Activity log |
| Demografisk profil | CRM-felt + enrichment |
| Scoring-detaljer | CRM dashboard |
| Relevante case studies | Sales enablement docs |

### Handoff-prosess

1. MQL-status settes automatisk
2. Lead routes til riktig salgsrepresentant
3. Sales får notifikasjon med lead-kontekst
4. Sales aksepterer eller avviser innen SLA
5. Avviste leads → feedback til marketing for scoring-justering

---

## Sjekkliste

- [ ] Lead lifecycle definert med tydelige stadier
- [ ] Dual-criteria scoring-modell implementert
- [ ] Speed-to-lead SLAer avtalt
- [ ] 8-metrikk dashboard satt opp
- [ ] Pipeline hygiene-rutiner etablert
- [ ] CRM-felt og automatisering konfigurert
- [ ] Marketing → Sales handoff dokumentert

---

## Relaterte Skills

- `cold-email` — Outbound lead generation
- `sales-enablement` — Sales collateral og verktøy
- `analytics-tracking` — Tracking av lead-kilder
- `email-sequence` — Nurture-sekvenser for ikke-kvalifiserte leads
- `pricing-strategy` — Prising påvirker deal size og win rate
