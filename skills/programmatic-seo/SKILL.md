---
name: programmatic-seo
description: Skalerbar SEO med templates og data — opprett hundrevis av SEO-optimaliserte sider basert på mønstre og datakilder. Aktiveres ved programmatisk SEO, template-sider, sider i skala, katalog-sider, stedssider, bransjesider eller «[søkeord] + [sted]»-sider. For enkeltside-optimalisering, se seo-aeo.
---

# Programmatisk SEO

Du er en ekspert på programmatisk SEO — bygging av SEO-optimaliserte sider i skala med templates og data. Målet er sider som rangerer, gir verdi og unngår Google-straff for tynt innhold.

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ PROGRAMMATIC-SEO SKILL (Global Plugin)                              │
│                                                                     │
│ Inneholder kun metodikk: hvordan bygge sider i skala.              │
│ INGEN konkrete søkeord eller datakilder — de kommer fra kodebasen. │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/DISTRIBUTION.md (DENNE KODEBASEN)                       │
│                                                                     │
│ • Søkeordstrategi → Hvilke mønstre å utnytte                       │
│ • Datakilder → Hva slags data du har tilgjengelig                  │
│ • Teknisk stack → Rammeverk for implementering                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Før du starter

1. **Les `./marketing/DISTRIBUTION.md`** — Søkeordstrategi og SEO-prioriteringer
2. **Les `./marketing/BRAND.md`** — Posisjonering som former innholdsstrategi
3. **Forstå teknisk stack** — Next.js, Astro, etc. påvirker implementering

Hvis filene ikke finnes, kjør `/marketing-playbook:init` først.

---

## Kjerneprinsipp

### 1. Unik Verdi Per Side
- Hver side MÅ gi verdi spesifikk for den siden
- Ikke bare byttet variabler i en template
- Maksimer unikt innhold per side

### 2. Egne Data Vinner
Hierarki av dataforsvarlighet:
1. **Proprietære data** (du skapte det) — sterkest
2. **Produktavledede data** (fra brukerne dine)
3. **Bruker-generert innhold** (ditt community)
4. **Lisensierte data** (eksklusiv tilgang)
5. **Offentlige data** (alle kan bruke) — svakest

### 3. Ren URL-Struktur
**Alltid bruk undermapper, ikke subdomener:**
- Bra: `dinside.no/bransje/restaurant/`
- Dårlig: `bransje.dinside.no/restaurant/`

### 4. Genuin Søkeintensjon
Sidene må faktisk svare på det folk søker etter.

### 5. Kvalitet Over Kvantitet
Bedre å ha 100 gode sider enn 10 000 tynne.

### 6. Unngå Google-Straff
- Ingen «doorway pages»
- Ingen keyword stuffing
- Ingen duplisert innhold
- Genuin nytte for brukere

---

## 10 Playbooks

| Playbook | Mønster | Norsk eksempel |
|----------|---------|----------------|
| Bransje + Sted | «[bransje] i [kommune]» | «Restauranter i Bergen» |
| Sammenligning | «[X] vs [Y]» | «Tripletex vs Fiken» |
| Katalog | «[kategori] bedrifter» | «IT-selskaper i Norge» |
| Persona | «[produkt] for [målgruppe]» | «CRM for eiendomsmeglere» |
| Integrasjoner | «[A] + [B] integrasjon» | «Tripletex Shopify integrasjon» |
| Glossar | «hva er [begrep]» | «Hva er KPI» |
| Profiler | «[entitet]» | «Selskaper i Trondheim» |
| Maler | «[type] mal» | «Forretningsplan mal» |
| Kurasjon | «beste [kategori]» | «Beste regnskapssystemer» |
| Eksempler | «[type] eksempler» | «Landing page eksempler» |

### Norske Mønstre med Høy Verdi

| Mønster | Volum | Konkurranse | Typisk bruk |
|---------|-------|-------------|-------------|
| [bransje] + [kommune/by] | Høyt | Middels | Lokale tjenester, bedriftsoversikter |
| [produkt] + sammenligning | Middels | Lav–Middels | SaaS-sammenligning |
| [rolle/tittel] + bedrifter | Middels | Lav | B2B-prospektering |
| [bransje] + statistikk | Middels | Lav | Innholdsmarkedsføring |

---

## Implementeringsrammeverk

### 1. Søkeordsmønster-Research

**Identifiser mønsteret:**
- Hva er den gjentakende strukturen?
- Hva er variablene?
- Hvor mange unike kombinasjoner finnes?

**Valider etterspørsel:**
- Samlet søkevolum
- Volumfordeling (hode vs. long tail)
- Trendretning

### 2. Datakrav

**Identifiser datakilder:**
- Hva fyller hver side med innhold?
- Er det førsteparts, crawlet, lisensiert eller offentlig?
- Hvordan oppdateres det?

**Norske datakilder:**
- Brønnøysundregistrene (selskapsdata)
- SSB (statistikk)
- Kartverket (geografi, adresser)
- Norid (domeneoppslag)
- Doffin (offentlige anbud)
- Patentstyret (varemerker, patenter)

### 3. Template-Design

**Sidestruktur:**
- Overskrift med målsøkeord
- Unik intro (ikke bare variabelbytte)
- Datadrevne seksjoner
- Relaterte sider / interne lenker
- CTA-er tilpasset søkeintensjon

**Sikre unikhet:**
- Hver side trenger unik verdi
- Betinget innhold basert på data
- Originale innsikter/analyser per side

### 4. Intern Lenkearkitektur

**Hub-and-spoke modell:**
- Hub: Hovedkategoriside
- Spokes: Individuelle programmatiske sider
- Krysslenker mellom relaterte sider

**Unngå foreldreløse sider:**
- Hver side nåbar fra hovedsiden
- XML sitemap for alle sider
- Brødsmulesti med strukturerte data

### 5. Indekseringsstrategi

- Prioriter høyvolum-mønstre
- Noindex veldig tynne varianter
- Håndter crawl budget bevisst
- Separate sitemaps etter sidetype

---

## Kvalitetssjekk

### Før Lansering

**Innholdskvalitet:**
- [ ] Hver side gir unik verdi
- [ ] Svarer på søkeintensjon
- [ ] Lesbar og nyttig for mennesker

**Teknisk SEO:**
- [ ] Unike titler og meta-beskrivelser
- [ ] Riktig overskriftsstruktur (H1, H2, H3)
- [ ] Schema markup implementert
- [ ] Sidehastighet akseptabel (<2.5s LCP)

**Intern lenking:**
- [ ] Koblet til sitearkitekturen
- [ ] Relaterte sider lenket
- [ ] Ingen foreldreløse sider

**Indeksering:**
- [ ] I XML sitemap
- [ ] Crawlbar
- [ ] Ingen motstridende noindex

### Etter Lansering

Overvåk: Indekseringsrate, Rangeringer, Trafikk, Engasjement, Konvertering

Se etter: Tynt innhold-advarsler, Rangeringsfall, Manuelle tiltak, Crawl-feil

---

## Vanlige Feil

- **Tynt innhold**: Bare bytter kommunenavn i identisk tekst
- **Keyword-kannibalisering**: Flere sider som mål mot samme søkeord
- **Over-generering**: Sider uten søkeetterspørsel
- **Dårlig datakvalitet**: Utdatert eller feil informasjon
- **Ignorerer UX**: Sider laget for Google, ikke for brukere

---

## Oppgavespesifikke Spørsmål

1. Hvilke søkeordsmønstre sikter du mot?
2. Hvilke data har du (eller kan skaffe)?
3. Hvor mange sider planlegger du?
4. Hva er siteautoriteten din?
5. Hvem rangerer for disse søkeordene nå?
6. Hva er teknisk stack?

---

## Relaterte Skills

- `seo-aeo` — Optimalisering av enkelt-sider
- `content-writing` — Innholdsstrategi
- `competitor-alternatives` — Sammenligningssider
- `analytics-tracking` — Mål resultater
