---
description: Show Marketing Playbook status for this project. Displays BRAND.md info, version, and available commands.
allowed-tools: Read, Glob
---

# Marketing Playbook - Status

Vis status for Marketing Playbook i dette prosjektet.

## Steg 1: Sjekk om BRAND.md finnes

Søk etter `BRAND.md` i prosjekt-rot og undermapper.

## Steg 2: Vis status

### Hvis BRAND.md FINNES:

```
═══════════════════════════════════════════
        MARKETING PLAYBOOK
═══════════════════════════════════════════

Status: ✅ Installert

Fil: ./BRAND.md
Sist oppdatert: [dato fra fil]

───────────────────────────────────────────
OPPSUMMERING
───────────────────────────────────────────

Audience:    [primary audience]
Positioning: [én setning]
Tone:        [adjektiver]

───────────────────────────────────────────
KOMMANDOER
───────────────────────────────────────────

/marketing-playbook:check   Sjekk innhold mot BRAND.md
/marketing-playbook:audit   Full prosjekt-audit
/marketing-playbook:init    Installer på nytt

═══════════════════════════════════════════
```

### Hvis BRAND.md IKKE finnes:

```
═══════════════════════════════════════════
        MARKETING PLAYBOOK
═══════════════════════════════════════════

Status: ❌ Ikke installert

Ingen BRAND.md funnet i prosjektet.

───────────────────────────────────────────
KOM I GANG
───────────────────────────────────────────

Kjør /marketing-playbook:init for å sette opp.

Dette oppretter BRAND.md med:
• Audience - Hvem snakker vi til?
• Brand - Hva tilbyr vi?
• Communication - Hvordan sier vi det?

═══════════════════════════════════════════
```

## Steg 3: Vis tilleggsinformasjon

Hvis BRAND.md finnes, vis også:
- Antall "Words We Avoid" definert
- Antall key messages
- Om Design-seksjon er inkludert
