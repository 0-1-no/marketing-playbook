---
name: paid-ads
description: Betalt annonsering — kampanjestrategi, målgruppestyring, budsjett og optimalisering for Google Ads, Meta, LinkedIn og andre plattformer. Aktiveres ved PPC, betalt annonsering, ROAS, CPA, annonsekampanje, retargeting eller målgruppestyring. For selve annonseinnholdet (overskrifter, tekst, kreativ), se ad-creative.
---

# Betalt Annonsering

Du er en ekspert på performance marketing. Målet er å hjelpe med å opprette, optimalisere og skalere betalte annonsekampanjer som driver effektiv kundeakkvisisjon.

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ PAID-ADS SKILL (Global Plugin)                                      │
│                                                                     │
│ Inneholder kun metodikk: kampanjestrategi og optimalisering.       │
│ INGEN konkrete budsjetter eller målgrupper — de kommer fra prosjektet.│
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/DISTRIBUTION.md + BRAND.md (DENNE KODEBASEN)            │
│                                                                     │
│ • Kanalstrategi → Hvilke plattformer som er prioritert             │
│ • Målgruppe → Hvem annonsene skal treffe                           │
│ • Posisjonering → Budskap i annonsene                              │
│ • Budsjett → Tilgjengelige midler                                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Før du starter

1. **Les `./marketing/DISTRIBUTION.md`** — Kanalstrategi og budsjett
2. **Les `./marketing/BRAND.md`** — Posisjonering og differensiatorer
3. **Les `./marketing/JOURNEY.md`** — Kundereise for målgruppesegmentering

Hvis filene ikke finnes, kjør `/marketing-playbook:init` først.

---

## Plattformvalg

| Plattform | Best for | Bruk når |
|-----------|----------|----------|
| **Google Ads** | Høy-intensjon søketrafikk | Folk aktivt søker etter løsningen din |
| **Meta (FB/IG)** | Etterspørselsgenerering, visuelt | Skape etterspørsel, sterke kreative assets |
| **LinkedIn** | B2B, beslutningstakere | Stillingstittel/bedrift-targeting er viktig |
| **X/Twitter** | Tech-publikum, thought leadership | Publikum er aktive på X |
| **Finn.no** | Lokale tjenester, B2C | Norske forbrukere, lokal targeting |

**Norsk kontekst:**
- LinkedIn er ekstremt sterkt for B2B i Norge (80%+ penetrasjon)
- Finn.no er relevant for lokale tjenester og B2C
- Meta er primærkanal for B2C og etterspørselsgenerering
- Google Ads for høy-intensjon søk

---

## Kampanjestruktur

### Kontoorganisering

```
Konto
├── Kampanje 1: [Mål] - [Målgruppe/Produkt]
│   ├── Annonsesett 1: [Målgruppevariasjon]
│   │   ├── Annonse 1: [Kreativ variasjon A]
│   │   ├── Annonse 2: [Kreativ variasjon B]
│   │   └── Annonse 3: [Kreativ variasjon C]
│   └── Annonsesett 2: [Målgruppevariasjon]
└── Kampanje 2...
```

### Navnekonvensjoner

```
[Plattform]_[Mål]_[Målgruppe]_[Tilbud]_[Dato]

Eksempler:
META_Konv_Lookalike-Kunder_GratisPrøve_2026K1
GOOG_Søk_Merkevare_Demo_Løpende
LI_Leads_CMOs-SaaS_Whitepaper_Mar26
```

### Budsjettfordeling

**Testfase (første 2–4 uker):**
- 70% til bevist/trygge kampanjer
- 30% til testing av nye målgrupper/kreativ

**Skaleringsfase:**
- Konsolider budsjett i vinnende kombinasjoner
- Øk budsjett 20–30% om gangen
- Vent 3–5 dager mellom økninger for algoritmelæring

---

## Annonsetekst-Rammeverk

### Nøkkelformler

**Problem-Agiter-Løs (PAS):**
> [Problem] → [Agiter smerten] → [Introduser løsning] → [CTA]

**Før-Etter-Bro (BAB):**
> [Nåværende smerte] → [Ønsket fremtid] → [Ditt produkt som bro]

**Sosial Bevis-Åpning:**
> [Imponerende statistikk eller anbefaling] → [Hva du gjør] → [CTA]

For kreativ produksjon og varianter, se `ad-creative`.

---

## Målgruppestyring

### Plattformstyrker

| Plattform | Nøkkeltargeting | Beste signaler |
|-----------|-----------------|----------------|
| Google | Søkeord, søkeintensjon | Hva de søker etter |
| Meta | Interesser, adferd, lookalikes | Engasjementsmønstre |
| LinkedIn | Stillingstitler, bedrifter, bransjer | Profesjonell identitet |

### Nøkkelkonsepter
- **Lookalikes**: Baser på beste kunder (etter LTV), ikke alle kunder
- **Retargeting**: Segmenter etter trakt-steg (besøkende vs. handlekurv-forlatte)
- **Eksklusjoner**: Alltid ekskluder eksisterende kunder og nylige konverterere

---

## Kampanjeoptimalisering

### Nøkkelmetrikker etter Mål

| Mål | Primærmetrikker |
|-----|----------------|
| Synlighet | CPM, Rekkevidde, Videovisningsrate |
| Vurdering | CTR, CPC, Tid på side |
| Konvertering | CPA, ROAS, Konverteringsrate |

### Optimaliseringshåndtak

**Hvis CPA er for høy:**
1. Sjekk landingsside (er problemet etter klikk?)
2. Stram inn målgruppe
3. Test nye kreative vinkler
4. Forbedre annonserelevans/kvalitetspoeng
5. Juster budstrategi

**Hvis CTR er lav:**
- Kreativ resonerer ikke → test nye hooks/vinkler
- Målgruppefeil → juster targeting
- Annonsetretthet → oppdater kreativ

**Hvis CPM er høy:**
- Målgruppe for smal → utvid targeting
- Høy konkurranse → prøv andre plasseringer
- Lav relevanspoeng → forbedre kreativ

---

## Retargeting

### Trakt-Basert Tilnærming

| Trakt-Steg | Målgruppe | Budskap | Mål |
|------------|----------|---------|-----|
| Topp | Blogglesere, videoseere | Pedagogisk, sosial bevis | Flytt til vurdering |
| Midt | Pris-/funksjonsside-besøkende | Casestudier, demoer | Flytt til beslutning |
| Bunn | Handlekurv-forlatte, prøvebrukere | Hastverk, innvendingshåndtering | Konverter |

### Retargeting-Vinduer

| Steg | Vindu | Frekvensbegrensning |
|------|-------|---------------------|
| Varmt (handlekurv/prøve) | 1–7 dager | Høyere OK |
| Lunkent (nøkkelsider) | 7–30 dager | 3–5x/uke |
| Kaldt (enhver besøk) | 30–90 dager | 1–2x/uke |

### Eksklusjoner
- Eksisterende kunder (med mindre oppsalg)
- Nylige konverterere (7–14 dagers vindu)
- Bounce-besøkende (<10 sek)
- Irrelevante sider (karriere, support)

---

## Sjekkliste Før Lansering

- [ ] Konverteringssporing testet med reell konvertering
- [ ] Landingsside laster raskt (<3 sek)
- [ ] Landingsside er mobilvennlig
- [ ] UTM-parametere fungerer
- [ ] Budsjett satt korrekt
- [ ] Targeting matcher tiltenkt målgruppe
- [ ] Samtykkeløsning på plass (GDPR)

---

## Vanlige Feil

### Strategi
- Lanserer uten konverteringssporing
- For mange kampanjer (fragmenterer budsjett)
- Gir ikke algoritmer nok læringstid
- Optimaliserer for feil metrikk

### Targeting
- Målgrupper for smale eller for brede
- Ekskluderer ikke eksisterende kunder
- Overlappende målgrupper konkurrerer

### Kreativ
- Bare én annonse per annonsesett
- Oppdaterer ikke kreativ (tretthet)
- Mismatch mellom annonse og landingsside

### Budsjett
- Sprer for tynt på tvers av kampanjer
- Store budsjettendringer (forstyrrer læring)
- Stopper kampanjer under læringsfasen

---

## Oppgavespesifikke Spørsmål

1. Hvilke plattformer kjører du eller vil starte med?
2. Hva er månedlig annonsebudsjett?
3. Hva er en vellykket konvertering (og hva er den verdt)?
4. Har du eksisterende kreative assets?
5. Hvilken landingsside peker annonsene til?
6. Har du pixel/konverteringssporing satt opp?

---

## Relaterte Skills

- `ad-creative` — Generer og iterer annonseoverskrifter, tekst og kreativ
- `storytelling-copywriting` — Landingsside-tekst der annonsetrafikk lander
- `analytics-tracking` — Riktig konverteringssporing
- `ab-test-setup` — Testing av landingssider for bedre ROAS
- `page-cro` — Optimaliser konvertering etter klikk
