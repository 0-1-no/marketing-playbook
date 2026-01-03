---
name: storytelling-copywriting
description: Storytelling og copywriting for markedsføringsinnhold. Aktiveres ved skriving av markedsføringstekst, overskrifter, artikler, e-poster, landing pages, eller annen overbevisende tekst. Gir rammeverk (AIDA, PAS) og teknikker for effektiv kommunikasjon. Leser fra marketing/BRAND.md for tone of voice.
---

# Storytelling & Copywriting

Denne skillen hjelper deg med å skrive overbevisende innhold.

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ STORYTELLING-COPYWRITING SKILL (Global Plugin)                      │
│                                                                     │
│ Du leser dette nå. Det er del av marketing-playbook plugin.        │
│ Inneholder kun metodikk: hvordan skrive headlines, bruke AIDA, etc.│
│ INGEN konkrete verdier - de kommer fra kodebasen du jobber i.      │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/BRAND.md (DENNE KODEBASEN)                              │
│                                                                     │
│ Skreddersydd for prosjektet du jobber i akkurat nå.                │
│ ALLTID les herfra for faktiske verdier:                            │
│ • Faktisk Tone of Voice (ikke "vurder profesjonell tone")          │
│ • Faktiske Words We Use/Avoid (ikke generiske eksempler)           │
│ • Faktisk Signature Story for denne merkevaren                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Viktig distinksjon

| Kilde | Inneholder | Eksempel |
|-------|------------|----------|
| **Sub-filer her** | Prinsipper og rammeverk | "AIDA: Attention → Interest → Desire → Action" |
| **BRAND.md** | Faktiske verdier | "Tone: Varm, ekspert, lettfattelig" |

**Alltid les ./marketing/BRAND.md først** - det er der prosjektets faktiske stemme er definert.

---

## Før du starter

1. **Les `./marketing/BRAND.md`** (Communication-seksjon) - Tone of Voice, Words We Use/Avoid
2. **Les `./marketing/JOURNEY.md`** - Hvilken stage skriver du for?

Hvis filene ikke finnes, kjør `/marketing-playbook:init` for å opprette dem.

---

## Ressurser (Les ved behov)

| Fil | Bruk når du... |
|-----|----------------|
| [STORYTELLING.md](STORYTELLING.md) | Utvikler narrativ, Signature Story, brand story |
| [FRAMEWORKS.md](FRAMEWORKS.md) | Trenger struktur: AIDA, PAS, BAB, FAB |
| [HEADLINES.md](HEADLINES.md) | Skriver titler, overskrifter, hooks |
| [MICROCOPY.md](MICROCOPY.md) | Skriver buttons, error messages, CTAs |
| [PERSUASION.md](PERSUASION.md) | Vil overbevise uten å manipulere |
| [CONTENT.md](CONTENT.md) | Planlegger content strategy |

---

## Beslutningstre

```
Hva skriver du?
│
├── Narrativ/Historie → STORYTELLING.md
│   └── "Om oss", brand story, signature story
│
├── Strukturert copy → FRAMEWORKS.md
│   └── Landing page, email, annonse, produktbeskrivelse
│
├── Titler/Hooks → HEADLINES.md
│   └── Artikkel, email subject, annonse hook
│
├── UI/UX tekst → MICROCOPY.md
│   └── Buttons, labels, errors, empty states
│
├── Persuasiv tekst → PERSUASION.md
│   └── Sales page, pitch, overtalelse
│
└── Content plan → CONTENT.md
    └── Bloggstrategi, innholdskalender
```

---

## 5 Tidløse Prinsipper

1. **Audience First** - Skriv for leseren, ikke deg selv
2. **Less is More** - Kutt til essensen. Respekter leserens tid.
3. **Show, Don't Tell** - Demonstrer med eksempler og historier
4. **One Goal** - Hver tekst har én hovedhandling
5. **Real Stories** - Autentiske historier slår polert fiksjon

---

## Framework-valg (Quick Reference)

| Situasjon | Framework | Hvorfor |
|-----------|-----------|---------|
| Ukjent produkt/problem | **AIDA** | Bygger fra oppmerksomhet til handling |
| Kjent smerte | **PAS** | Agiterer problemet før løsning |
| Transformasjonshistorie | **BAB** | Viser før/etter tydelig |
| Funksjoner → Fordeler | **FAB** | Kobler features til verdi |

**Full guide:** Se [FRAMEWORKS.md](FRAMEWORKS.md)

---

## Kobling til BRAND.md

Copy MÅ reflektere merkevaren:

| BRAND.md | → | Copy |
|----------|---|------|
| Tone of Voice | → | Ordvalg, setningsrytme, formalitetsnivå |
| Words We Use | → | Konsistent terminologi i all tekst |
| Words We Avoid | → | Ord som aldri skal brukes |
| Signature Story | → | Referansepunkt for all storytelling |
| Values | → | Underliggende budskap i all kommunikasjon |

**Alltid les BRAND.md først** - copyen skal forsterke merkevaren, ikke motsi den.

---

## Koplingspunkter

- **BRAND.md** → Tone of Voice, Words We Use/Avoid, Signature Story
- **JOURNEY.md** → Hvilken stage? Hvilke bekymringer adresserer vi?
- **marketing-psychology.md** → Dypere psykologi-referanse
- **content-writing skill** → For lengre formater (artikler, guider, landing pages)

---

## Anti-patterns (Unngå)

- **Feature-dumping** - Liste funksjoner uten å koble til verdi
- **Buzzword-bingo** - "Revolusjonerende AI-drevet plattform"
- **All caps/overdrevne påstander** - Skaper mistillit
- **Vage CTAs** - "Klikk her" vs "Start gratis prøve"
- **For lang tekst** - Respekter leserens tid
- **Manipulative patterns** - Falsk knapphet, skjulte kostnader

---

## Relaterte Skills

- `content-writing` - Lengre formater (artikler, guider, landing pages)
- `design-system` - Visuell stil som matcher copy
- `marketing-psychology` - Psykologi bak overbevisende tekst
- `brand-principles` - Merkevare-fundament

---

## Oppsett

Hvis `marketing/BRAND.md` ikke finnes, kjør:

```
/marketing-playbook:init
```

For å definere voice-regler spesifikt for innhold, kjør:

```
/content-writer:init
```

Dette oppretter `marketing/CONTENT-RULES.md` med detaljerte voice-dimensjoner.
