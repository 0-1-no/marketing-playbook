---
description: Show Marketing Playbook status for this project. Displays BRAND.md, JOURNEY.md, DISTRIBUTION.md, and LEARNINGS.md info, version, and available commands.
allowed-tools: Read, Glob
---

# Marketing Playbook - Status

Vis status for Marketing Playbook i dette prosjektet.

## Steg 1: Sjekk om filene finnes

Søk etter `marketing/`-mappen med `BRAND.md`, `JOURNEY.md`, `DISTRIBUTION.md` og `LEARNINGS.md`.

Akseptable plasseringer (i prioritert rekkefølge):
1. `marketing/` (anbefalt)
2. Prosjekt-rot (legacy)

## Steg 2: Vis status

### Hvis ALLE 4 filer finnes:

```
═══════════════════════════════════════════
        MARKETING PLAYBOOK
═══════════════════════════════════════════

Status: ✅ Fullstendig oppsett

───────────────────────────────────────────
FILER
───────────────────────────────────────────

📁 marketing/
   📋 BRAND.md        Sist oppdatert: [dato]
   🗺️ JOURNEY.md      Sist oppdatert: [dato]
   📡 DISTRIBUTION.md Sist oppdatert: [dato]
   🧪 LEARNINGS.md    Sist oppdatert: [dato]

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

### Hvis noen filer mangler:

```
═══════════════════════════════════════════
        MARKETING PLAYBOOK
═══════════════════════════════════════════

Status: ⚠️ Delvis oppsett

───────────────────────────────────────────
FILER
───────────────────────────────────────────

📁 marketing/
   📋 BRAND.md:        [✅ Funnet / ❌ Mangler]
   🗺️ JOURNEY.md:      [✅ Funnet / ❌ Mangler]
   📡 DISTRIBUTION.md: [✅ Funnet / ❌ Mangler]
   🧪 LEARNINGS.md:    [✅ Funnet / ❌ Mangler]

───────────────────────────────────────────
ANBEFALING
───────────────────────────────────────────

Kjør /marketing-playbook:init for å legge til
manglende filer. Eksisterende filer beholdes.

───────────────────────────────────────────
KOMMANDOER
───────────────────────────────────────────

/marketing-playbook:check   Sjekk innhold mot ABC + Journey
/marketing-playbook:audit   Full prosjekt-audit
/marketing-playbook:init    Legg til manglende filer

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

   📡 DISTRIBUTION.md (Kanaler & Stack)
      • Marketing stack (email, CMS, analytics)
      • Aktive kanaler og budget split
      • Quick Start: Organic SEO for nye prosjekter

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

**Fra DISTRIBUTION.md:**
- Marketing stack status (hvilke verktøy er satt opp)
- Aktive kanaler (primary/secondary)
- Owned vs Rented ratio
- Om Quick Start SEO er relevant (nye prosjekter)

**Fra LEARNINGS.md:**
- BAF-status (Validert / Under testing / Ikke testet)
- Antall dokumenterte tester
- Siste oppdatering
