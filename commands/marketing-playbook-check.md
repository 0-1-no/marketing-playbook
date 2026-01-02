---
description: Check if content aligns with BRAND.md and JOURNEY.md. Use before publishing landing pages, copy, or marketing materials.
allowed-tools: Read, Glob, AskUserQuestion
---

# Marketing Playbook - Sjekk Innhold

Verifiser at innhold samsvarer med prosjektets `BRAND.md` og `JOURNEY.md`.

## Steg 1: Les BRAND.md og JOURNEY.md

Finn og les filene fra `marketing/`-mappen:

```
marketing/BRAND.md
marketing/JOURNEY.md
```

Akseptable plasseringer (i prioritert rekkefølge):
1. `marketing/` (anbefalt)
2. Prosjekt-rot (legacy)

Hvis filene ikke finnes:
```
⚠️ Marketing Playbook ikke satt opp.

Mangler:
- marketing/BRAND.md: [Ja/Nei]
- marketing/JOURNEY.md: [Ja/Nei]

Kjør `/marketing-playbook:init` for å sette opp.
```

## Steg 2: Identifiser innhold og journey stage

Spør brukeren:

```
Hvilket innhold skal sjekkes?
- Lim inn tekst eller oppgi filnavn

Hvilken del av kundereisen er dette for?
1. Awareness (annonser, førsteinntrykk)
2. Consideration (vurdering, sammenligning)
3. Evaluation (produktvalg, detaljer)
4. Purchase (checkout, betaling)
5. Post-purchase (velkomst, onboarding)
6. Loyalty (nyhetsbrev, lojalitet)
```

Bruk kontekst hvis innholdstype er åpenbar (f.eks. checkout-tekst = Purchase).

## Steg 3: ABC Sjekkliste

Evaluer innholdet mot hver seksjon:

### A - AUDIENCE

| Sjekk | Status | Kommentar |
|-------|--------|-----------|
| Relevant for målgruppen? | ✅/⚠️/❌ | [detaljer] |
| Adresserer pain points? | ✅/⚠️/❌ | [detaljer] |
| Snakker deres språk? | ✅/⚠️/❌ | [detaljer] |

### B - BRAND

| Sjekk | Status | Kommentar |
|-------|--------|-----------|
| On-brand? | ✅/⚠️/❌ | [detaljer] |
| Reflekterer verdier? | ✅/⚠️/❌ | [detaljer] |
| Forsterker posisjonering? | ✅/⚠️/❌ | [detaljer] |

### C - COMMUNICATION

| Sjekk | Status | Kommentar |
|-------|--------|-----------|
| Riktig tone of voice? | ✅/⚠️/❌ | [detaljer] |
| Bruker riktige ord? | ✅/⚠️/❌ | [detaljer] |
| Unngår forbudte ord? | ✅/⚠️/❌ | [detaljer] |
| Budskap klart? | ✅/⚠️/❌ | [detaljer] |

## Steg 4: Journey Stage Sjekk

Basert på valgt stage, verifiser mot JOURNEY.md:

### J - JOURNEY

| Sjekk | Status | Kommentar |
|-------|--------|-----------|
| Matcher kundens mål for stagen? | ✅/⚠️/❌ | [detaljer] |
| Adresserer bekymringer for stagen? | ✅/⚠️/❌ | [detaljer] |
| Bruker relevant psykologi? | ✅/⚠️/❌ | [prinsipper brukt] |
| Riktig kanal/touchpoint? | ✅/⚠️/❌ | [detaljer] |

### Stage-spesifikke sjekker

**Awareness:**
- [ ] Fanger oppmerksomhet raskt?
- [ ] Skiller seg ut visuelt?
- [ ] Skaper nysgjerrighet uten å overselge?

**Consideration:**
- [ ] Bygger tillit (social proof, autoritet)?
- [ ] Adresserer vanlige innvendinger?
- [ ] Viser verdi tydelig?

**Evaluation:**
- [ ] Hjelper med valget?
- [ ] Reduserer opplevd risiko?
- [ ] Viser sammenligninger/alternativer?

**Purchase:**
- [ ] Minimerer friksjon?
- [ ] Bekrefter at de tar riktig valg?
- [ ] Tydelig progresjon?

**Post-purchase:**
- [ ] Reduserer kjøpsanger?
- [ ] Hjelper i gang med bruk?
- [ ] Overrasker positivt?

**Loyalty:**
- [ ] Anerkjenner lojalitet?
- [ ] Gir eksklusiv verdi?
- [ ] Inviterer til engasjement?

## Steg 5: Spesifikke funn

### Ord som bør endres
List opp ord fra "Words We Avoid" som ble funnet:

| Funnet | Anbefalt endring |
|--------|------------------|
| "beste" | "pålitelig" / "effektiv" |

### Manglende elementer
List opp ting fra "Words We Use" eller "Key Messages" som kunne vært inkludert.

### Psykologi-muligheter
Basert på journey stage, foreslå prinsipper som kunne styrket innholdet:

| Prinsipp | Hvordan bruke |
|----------|---------------|
| [fra JOURNEY.md] | [konkret forslag] |

## Steg 6: Sammendrag

```
═══════════════════════════════════════════
     MARKETING PLAYBOOK - SJEKK
═══════════════════════════════════════════

Innhold: [filnavn/beskrivelse]
Journey Stage: [valgt stage]

───────────────────────────────────────────
SCORE
───────────────────────────────────────────

ABC Score: [X/10]
Journey Score: [X/10]
Total: [X/10]

───────────────────────────────────────────
FUNN
───────────────────────────────────────────

✅ Styrker:
- [liste]

⚠️ Forbedringer:
- [liste med konkrete forslag]

❌ Kritisk:
- [hvis noe bryter sterkt med brand/journey]

───────────────────────────────────────────
PSYKOLOGI-TIPS
───────────────────────────────────────────

For [stage] anbefales:
- [prinsipp]: [hvordan bruke]

═══════════════════════════════════════════
```

## Steg 7: Journey-oppdatering (valgfritt)

Etter sjekken, vurder om JOURNEY.md bør oppdateres:

```
💡 Journey-innsikt

Basert på dette innholdet, vurder å oppdatere JOURNEY.md:
- [Ny bekymring identifisert?]
- [Nytt touchpoint i bruk?]
- [Ny psykologi som fungerer?]

Vil du oppdatere JOURNEY.md nå? (ja/nei)
```

## Output-format

Vær konstruktiv og gi konkrete forbedringsforslag. Ikke bare påpek problemer - forklar hvordan det kan fikses.
