---
description: Show Marketing Playbook status for this project. Displays BRAND.md and JOURNEY.md info, version, and available commands.
allowed-tools: Read, Glob
---

# Marketing Playbook - Status

Vis status for Marketing Playbook i dette prosjektet.

## Steg 1: Sjekk om filene finnes

Søk etter `marketing/`-mappen med `BRAND.md`, `JOURNEY.md` og `LEARNINGS.md`.

Akseptable plasseringer (i prioritert rekkefølge):
1. `marketing/` (anbefalt)
2. Prosjekt-rot (legacy)

## Steg 2: Vis status

### Hvis BEGGE filer finnes:

```
═══════════════════════════════════════════
        MARKETING PLAYBOOK
═══════════════════════════════════════════

Status: ✅ Fullstendig oppsett

───────────────────────────────────────────
FILER
───────────────────────────────────────────

📁 marketing/
   📋 BRAND.md      Sist oppdatert: [dato]
   🗺️ JOURNEY.md    Sist oppdatert: [dato]
   🧪 LEARNINGS.md  Sist oppdatert: [dato]

───────────────────────────────────────────
OPPSUMMERING
───────────────────────────────────────────

Audience:    [primary audience]
Positioning: [én setning]
Tone:        [adjektiver]

Journey stages definert:
✅ Awareness  ✅ Consideration  ✅ Evaluation
✅ Purchase   ✅ Post-purchase  ✅ Loyalty

───────────────────────────────────────────
KOMMANDOER
───────────────────────────────────────────

/marketing-playbook:check   Sjekk innhold mot ABC + Journey
/marketing-playbook:audit   Full prosjekt-audit
/marketing-playbook:init    Installer på nytt

═══════════════════════════════════════════
```

### Hvis KUN BRAND.md finnes:

```
═══════════════════════════════════════════
        MARKETING PLAYBOOK
═══════════════════════════════════════════

Status: ⚠️ Delvis oppsett

───────────────────────────────────────────
FILER
───────────────────────────────────────────

📁 marketing/
   📋 BRAND.md:      ✅ Funnet
   🗺️ JOURNEY.md:    ❌ Mangler
   🧪 LEARNINGS.md:  ❌ Mangler

───────────────────────────────────────────
ANBEFALING
───────────────────────────────────────────

Du har BRAND.md, men mangler JOURNEY.md og
LEARNINGS.md for komplett oppsett.

Kjør /marketing-playbook:init for å legge til
manglende filer (BRAND.md beholdes).

───────────────────────────────────────────
KOMMANDOER
───────────────────────────────────────────

/marketing-playbook:check   Sjekk innhold mot BRAND.md
/marketing-playbook:audit   Full prosjekt-audit
/marketing-playbook:init    Legg til JOURNEY.md

═══════════════════════════════════════════
```

### Hvis INGEN filer finnes:

```
═══════════════════════════════════════════
        MARKETING PLAYBOOK
═══════════════════════════════════════════

Status: ❌ Ikke installert

Ingen marketing/-mappe funnet.

───────────────────────────────────────────
KOM I GANG
───────────────────────────────────────────

Kjør /marketing-playbook:init for å sette opp.

Dette oppretter:

📁 marketing/
   📋 BRAND.md (ABC-rammeverket)
      • Audience - Hvem snakker vi til?
      • Brand - Hva tilbyr vi?
      • Communication - Hvordan sier vi det?

   🗺️ JOURNEY.md (Kundereisen)
      • Awareness → Consideration → Purchase
      • Post-purchase → Loyalty
      • Psykologi-prinsipper per stage

   🧪 LEARNINGS.md (Validering)
      • Brand Audience Fit status
      • Tester og resultater
      • Hva fungerer / hva fungerer ikke

═══════════════════════════════════════════
```

## Steg 3: Vis tilleggsinformasjon

Hvis filene finnes, vis også:

**Fra BRAND.md:**
- Antall "Words We Avoid" definert
- Antall key messages
- Om Design-seksjon er inkludert

**Fra JOURNEY.md:**
- Hvilke stages som er definert vs "[Under utvikling]"
- Antall touchpoints listet
- Om metrikker er definert
