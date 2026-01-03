---
name: marketing-playbook
description: Apply Marketing Playbook principles when creating marketing content, landing pages, copy, or brand materials. Reads files from marketing/ folder.
---

# Marketing Playbook Skill

Denne skillen aktiveres automatisk når du jobber med marketing-relatert innhold.

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ MARKETING-PLAYBOOK (Global Plugin)                                  │
│                                                                     │
│ Du leser dette nå. Det er installert GLOBALT for brukeren.         │
│ Inneholder kun metodikk, prosesser og rammeverk.                   │
│ INGEN konkrete verdier - de kommer fra kodebasen du jobber i.      │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/ (DENNE KODEBASEN)                                      │
│                                                                     │
│ Skreddersydd for prosjektet du jobber i akkurat nå.                │
│ ALLTID les herfra for faktiske verdier:                            │
│ • Hvem er målgruppen? → BRAND.md                                   │
│ • Hvilke farger/fonts? → DESIGN-SYSTEM.md                          │
│ • Hvilke kanaler? → DISTRIBUTION.md                                │
└─────────────────────────────────────────────────────────────────────┘
```

**Viktig distinksjon:**
- **Plugin-filer** (denne og andre skills): Guider for HVORDAN jobbe
- **./marketing/-filer** (i denne kodebasen): Kilde til sannhet for faktiske verdier

**Alltid les fra ./marketing/ først** - det er der de prosjektspesifikke verdiene bor.

---

## Før du starter

Les filene fra `marketing/`-mappen (disse er prosjektspesifikke):

**marketing/BRAND.md** for:
- **Audience**: Hvem snakker vi til?
- **Brand**: Hva tilbyr vi og hvorfor?
- **Communication**: Hvordan sier vi det?

**marketing/JOURNEY.md** for:
- **Kundereisen**: Hvilken stage er dette innholdet for?
- **Psykologi**: Hvilke prinsipper er relevante for denne stagen?
- **Touchpoints**: Hvilke kanaler/formater brukes i denne stagen?

**marketing/DISTRIBUTION.md** for:
- **Stack**: Hvilke verktøy brukes (email, CMS, analytics)?
- **Kanaler**: Hvor er merkevaren til stede?
- **Budget**: Hvordan fordeles ressursene (60:40)?
- **SEO & AEO Strategy**: Søkeord, innholdsplan, AI-synlighet

**marketing/LEARNINGS.md** for:
- **BAF-status**: Er merkevaren validert?
- **Hva fungerer**: Dokumenterte innsikter
- **Segmenter**: Hvem konverterer faktisk?

**marketing/DESIGN-SYSTEM.md** for (hvis UI-arbeid):
- **Aesthetic direction**: Visuell retning og vibe
- **Farger**: Faktisk fargepalett med hex-verdier
- **Typografi**: Faktiske fonts og størrelser
- **Komponenter**: Faktiske patterns og kode

Hvis filene ikke finnes:
- Kjør `/marketing-playbook:init` for BRAND, JOURNEY, DISTRIBUTION, LEARNINGS
- Kjør `/design-system:init` for DESIGN-SYSTEM.md

---

## Identifiser Journey Stage

Når du lager innhold, identifiser hvilken stage det tilhører:

| Innholdstype | Typisk Stage |
|--------------|--------------|
| Annonser (Facebook, Google) | Awareness |
| Blogginnlegg, SEO | Awareness / Consideration |
| Landing pages | Consideration / Evaluation |
| Produktsider | Evaluation |
| Checkout, betalingsflow | Purchase |
| Velkomst-e-post, onboarding | Post-purchase |
| Nyhetsbrev, lojalitetsprogram | Loyalty |

**Når du har identifisert stage:**
1. Les relevant seksjon i JOURNEY.md
2. Bruk psykologi-prinsippene listet for den stagen
3. Adresser kundens bekymringer for den stagen
4. Match touchpoints og kanaler

---

## ABC Sjekkliste

Bruk denne sjekklisten før du leverer marketing-innhold:

### A - Audience

- [ ] Er innholdet relevant for målgruppen definert i BRAND.md?
- [ ] Adresserer det deres pain points?
- [ ] Snakker vi deres språk (ikke for teknisk/for simpelt)?
- [ ] Er use cases relevante for dem?

### B - Brand

- [ ] Er innholdet on-brand?
- [ ] Reflekterer det våre kjerneverdier?
- [ ] Forsterker det vår posisjonering?
- [ ] Skiller det oss fra konkurrentene?

### C - Communication

- [ ] Er tone of voice riktig (per BRAND.md)?
- [ ] Bruker vi ord fra "Words We Use"?
- [ ] Unngår vi ord fra "Words We Avoid"?
- [ ] Er budskapet klart og konsist?
- [ ] Inkluderer vi key messages der relevant?

---

## Vanlige Marketing-oppgaver

### Landing Pages

Når du lager landing pages:
1. Start med brukerens problem (pain point)
2. Vis løsningen (vår posisjonering)
3. Bevis verdien (differentiators)
4. CTA som matcher brukerens mål

### Copy/Tekst

Når du skriver copy:
1. Sjekk tone of voice i BRAND.md
2. Bruk "Words We Use" aktivt
3. Unngå "Words We Avoid" strengt
4. Hold det konsist - respekter brukerens tid

### SEO/Meta

Når du lager meta-innhold:
1. Inkluder key messages i title/description
2. Bruk primær målgruppe-språk
3. Unngå buzzwords og oversolgt språk

### Email/Outreach

Når du skriver email:
1. Personaliser til audience segment
2. Lead med verdi, ikke pitch
3. Tydelig CTA
4. Match tone of voice

---

## Quick Reference

### Typiske "Words We Avoid"
- beste, ledende, revolusjonerende
- enkel (kan tolkes som mangelfull)
- billig, rabatt (verdi, ikke pris)
- disrupts, cutting-edge (buzzwords)
- gratis (med mindre det faktisk er gratis)

### God Copy-struktur
1. **Hook**: Fang oppmerksomhet med pain point
2. **Problem**: Utdyp problemet de opplever
3. **Solution**: Introduser løsningen
4. **Proof**: Vis at det fungerer
5. **CTA**: Klar handlingsoppfordring

---

## Journey-basert innholdsskaping

### Awareness-innhold
**Mål:** Fange oppmerksomhet, skape gjenkjennelse
**Psykologi:** Mere Exposure, Von Restorff, Picture Superiority, Information Gap
**Tips:**
- Led med problem/pain point
- Skill deg ut visuelt
- Skap nysgjerrighet, ikke selg ennå

### Consideration-innhold
**Mål:** Bygge tillit, vise verdi
**Psykologi:** Social Proof, Authority, Halo Effect, Confirmation Bias
**Tips:**
- Vis testimonials og case studies
- Demonstrer ekspertise
- Adresser innvendinger proaktivt

### Evaluation-innhold
**Mål:** Hjelpe valget, redusere risiko
**Psykologi:** Anchoring, Decoy Effect, Loss Aversion, Scarcity
**Tips:**
- Sammenlign alternativer tydelig
- Vis hva de går glipp av
- Tilby garantier/trygghet

### Purchase-innhold
**Mål:** Friksjonsfri gjennomføring
**Psykologi:** Goal Gradient, Default Options, Commitment
**Tips:**
- Minimer steg
- Vis progresjon
- Bekreft at de tar riktig valg

### Post-purchase-innhold
**Mål:** Bekrefte valget, starte relasjonen
**Psykologi:** Peak-End Rule, Cognitive Dissonance, Reciprocity
**Tips:**
- Overrask positivt
- Hjelp dem i gang
- Reduser kjøpsanger

### Loyalty-innhold
**Mål:** Bygge tilhørighet, skape ambassadører
**Psykologi:** Sunk Cost, Social Identity, IKEA Effect, Nostalgia
**Tips:**
- Anerkjenn lojalitet
- Involver dem i utviklingen
- Skap felles historie

---

## Vedlikehold av JOURNEY.md

Foreslå oppdatering av JOURNEY.md når:
- Du har sjekket 5+ innhold for samme stage
- Bruker gir feedback om kundeopplevelsen
- Nye kanaler/touchpoints tas i bruk
- Konverteringsdata viser endringer

---

## Relaterte Kommandoer

| Kommando | Output |
|----------|--------|
| `/marketing-playbook:init` | Oppretter BRAND, JOURNEY, DISTRIBUTION, LEARNINGS |
| `/marketing-playbook:check` | Validerer innhold mot ./marketing/ |
| `/marketing-playbook:audit` | Full prosjekt-audit |
| `/design-system:init` | Oppretter DESIGN-SYSTEM.md |
| `/seo-aeo:audit` | SEO og AEO teknisk audit |

## Relaterte Skills

Alle skills inneholder **metodikk og prinsipper** - ikke konkrete verdier:

| Skill | Innhold |
|-------|---------|
| `seo-aeo` | SEO, AEO, søkeord, AI-synlighet |
| `design-system` | UI/UX metodikk, anti-patterns, estetiske retninger |
| `storytelling-copywriting` | Rammeverk for copy (AIDA, PAS, headlines) |
| `marketing-psychology` | 35+ psykologiske prinsipper per funnel-stage |
| `marketing-mindset` | 20 strategiske prinsipper |
| `brand-principles` | 7 prinsipper for merkevarebygging |
| `distribution-principles` | SOV→SOM, 60:40, Reach>Frequency |
| `customer-principles` | Lojalitet, retention, community |

**Husk:** Disse er guider. Faktiske verdier kommer fra `./marketing/`.
