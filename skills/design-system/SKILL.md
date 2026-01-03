---
name: design-system
description: Design system og visuell identitet for merkevaren. Aktiveres automatisk ved UI/UX-arbeid, landing pages, komponentutvikling, styling, CSS, Tailwind, eller visuelt design. Sikrer konsistent, distinkt design som unngår generisk AI-estetikk. Leser fra marketing/DESIGN-SYSTEM.md og BRAND.md.
---

# Design System

Denne skillen hjelper deg med å skape distinkt, merkevare-riktig UI.

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ DESIGN-SYSTEM SKILL (Global Plugin)                                 │
│                                                                     │
│ Du leser dette nå. Det er del av marketing-playbook plugin.        │
│ Inneholder kun metodikk: hvordan velge fonts, farger, komponenter. │
│ INGEN konkrete verdier - de kommer fra kodebasen du jobber i.      │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/DESIGN-SYSTEM.md (DENNE KODEBASEN)                      │
│                                                                     │
│ Skreddersydd for prosjektet du jobber i akkurat nå.                │
│ ALLTID les herfra for faktiske verdier:                            │
│ • Faktiske hex-koder (ikke "#7C3AED fra eksempel")                 │
│ • Faktiske fontnavn (ikke "vurder Clash Display")                  │
│ • Faktisk komponentkode for dette prosjektet                       │
└─────────────────────────────────────────────────────────────────────┘
```

### Viktig distinksjon

| Kilde | Inneholder | Eksempel |
|-------|------------|----------|
| **Sub-filer her** | Prinsipper og forslag | "Vurder fonts som Clash Display eller Satoshi" |
| **DESIGN-SYSTEM.md** | Faktiske verdier | "Display font: Space Grotesk 700" |

**Alltid les ./marketing/ først** - det er der de prosjektspesifikke verdiene bor.

Sub-filene i denne skillen (TYPOGRAPHY.md, COLOR-THEORY.md, etc.) er **guider for å ta beslutninger**, ikke kilder til konkrete verdier.

---

## Før du starter

1. **Les `./marketing/DESIGN-SYSTEM.md`** - Faktiske farger, fonts, komponenter
2. **Les `./marketing/BRAND.md`** (Design-seksjon) - Brand-kontekst

Hvis filene ikke finnes, kjør `/design-system:init` for å opprette dem.

---

## Ressurser (Metodikk - les ved behov)

| Fil | Bruk når du... |
|-----|----------------|
| [AESTHETIC-DIRECTION.md](AESTHETIC-DIRECTION.md) | Definerer visuell retning, vibe, stil |
| [ANTI-PATTERNS.md](ANTI-PATTERNS.md) | Sjekker mot generisk AI-look |
| [COMPONENTS.md](COMPONENTS.md) | Bygger buttons, forms, cards, layouts |
| [TYPOGRAPHY.md](TYPOGRAPHY.md) | Velger fonts, pairing, hierarki |
| [COLOR-THEORY.md](COLOR-THEORY.md) | Velger fargepaletter, kontrast |
| [MICRO-INTERACTIONS.md](MICRO-INTERACTIONS.md) | Legger til animasjoner, hover, transitions |
| [RESPONSIVE.md](RESPONSIVE.md) | Tilpasser til mobile, tablet, desktop |
| [ACCESSIBILITY.md](ACCESSIBILITY.md) | Sikrer a11y compliance |

---

## Beslutningstre

```
Hva bygger du?
│
├── Ny landing page
│   ├── Les AESTHETIC-DIRECTION.md først
│   ├── Bruk COMPONENTS.md for struktur
│   └── Sjekk ANTI-PATTERNS.md før levering
│
├── UI-komponent
│   ├── Les COMPONENTS.md
│   ├── Bruk MICRO-INTERACTIONS.md for states
│   └── Valider mot ACCESSIBILITY.md
│
├── Typografi-system
│   ├── Les TYPOGRAPHY.md
│   └── Koble til BRAND.md farger
│
├── Fargepalett
│   ├── Les COLOR-THEORY.md
│   └── Test mot ACCESSIBILITY.md (kontrast)
│
├── Responsivt design
│   ├── Les RESPONSIVE.md
│   └── Test alle breakpoints
│
└── Generelt UI-arbeid
    ├── Start med AESTHETIC-DIRECTION.md
    └── Avslutt med ANTI-PATTERNS.md sjekk
```

---

## Kjerneprinsipp: Vibe over System

Et design system er ikke bare komponenter og tokens - det er en **vibe**.

**Spør deg selv:**
1. Hva føler brukeren når de ser dette?
2. Ville dette skilt seg ut i konkurrentens feed?
3. Er dette **uforglemmelig** eller bare "pent"?

**Den Ene Tingen:** Hvert design må ha ett element folk husker - en uvanlig animasjon, en overraskende farge, et distinkt typografi-valg.

---

## Kobling til BRAND.md

Design system MÅ reflektere merkevaren:

| BRAND.md | → | Design System |
|----------|---|---------------|
| Tone of Voice | → | Visuell tone (leken = runde former, profesjonell = skarpe linjer) |
| Brand Personality | → | Fargevalg, typografi-stil |
| Values | → | Mikro-interaksjoner, detaljer |
| Differentiators | → | Unike visuelle elementer |

**Alltid les BRAND.md først** - designet skal forsterke merkevaren, ikke motsi den.

---

## Quick Reference: AI Slop Deteksjon

### UNNGÅ disse
- Inter, Roboto, Arial som primærfont
- Lilla/blå gradient på hvit bakgrunn
- Perfekt symmetriske layouts
- Stock-photo i "diverse team smiles at laptop"-stil
- Identiske border-radius overalt (8px på alt)
- Ingen mikro-interaksjoner
- "Safe" fargevalg som ikke sier noe

### GJØR dette
- Velg distinkte, karakterfulle fonts
- Ha en tydelig estetisk retning
- Bruk asymmetri og overraskende layout
- Custom illustrasjoner/ikoner
- Varierte border-radius med intensjon
- Animasjoner som føles naturlige
- Modige fargevalg som skiller seg ut

**Full sjekkliste:** Se [ANTI-PATTERNS.md](ANTI-PATTERNS.md)

---

## Før du leverer UI

Kjør denne sjekklisten:

- [ ] Lest BRAND.md Design-seksjon?
- [ ] Lest marketing/DESIGN-SYSTEM.md?
- [ ] Følger valgt aesthetic direction?
- [ ] Minst 1 font som IKKE er Inter/Roboto/Arial?
- [ ] Fargepalett som skiller seg fra blå/lilla gradient?
- [ ] Minst 1 asymmetrisk element?
- [ ] Minst 1 karakterfull mikro-interaksjon?
- [ ] Minst 1 "den ene tingen" som er uforglemmelig?
- [ ] WCAG AA kontrast på tekst?
- [ ] Testet på mobile?

---

## Relaterte Skills

- `storytelling-copywriting` - Copy som matcher visuell stil
- `marketing-psychology` - Psykologi bak visuelle valg
- `brand-principles` - Merkevare-fundament

---

## Oppsett

Hvis `marketing/DESIGN-SYSTEM.md` ikke finnes, kjør:

```
/design-system:init
```

Dette starter en iterativ prosess hvor du bygger demo-sider og får feedback til design systemet er definert.
