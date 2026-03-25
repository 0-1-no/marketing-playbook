---
description: Opprett kun DISTRIBUTION.md for dette prosjektet. Kartlegger marketing stack og kanaler.
disable-model-invocation: true
allowed-tools: Read, Write, Glob, AskUserQuestion
---

# Distribution Init

Opprett `DISTRIBUTION.md` for dette prosjektet gjennom fokusert intervju om marketing stack og kanaler.

> **Forutsetning:** BRAND.md bør finnes for kontekst om målgruppe.
> For fullstendig oppsett, bruk `/marketing-playbook:init` istedenfor.

---

## Steg 1: Sjekk eksisterende

Sjekk om `marketing/DISTRIBUTION.md` finnes.

Hvis filen finnes:
```
Eksisterende DISTRIBUTION.md funnet.

Vil du:
1. Overskrive (start på nytt)
2. Oppdatere basert på eksisterende
3. Avbryt
```

Sjekk også om BRAND.md finnes for kontekst.

---

## Steg 2: Introduksjon

```
═══════════════════════════════════════════════════════════════
                     DISTRIBUTION INIT
═══════════════════════════════════════════════════════════════

Jeg skal hjelpe deg med å kartlegge:

📡 Marketing Stack - Hvilke verktøy dere bruker
📡 Kanaler - Hvor dere er til stede
📡 Strategi - Hva fungerer og hva dere satser på

Nyoppstartede merkevarer: "Ikke satt opp ennå" er helt OK.
Jeg inkluderer Quick Start-tips for organic SEO.

═══════════════════════════════════════════════════════════════
```

---

## Steg 3: Intervju

### Marketing Stack

**Spørsmål 1:** Hvilken e-postleverandør bruker dere?
- Eksempler: "Mailchimp", "Klaviyo", "Loops", "ConvertKit", "Ingen ennå"
- Hvis aktiv: hvor stor er listen?

**Spørsmål 2:** Hvilken CMS/website platform bruker dere?
- Eksempler: "WordPress", "Webflow", "Next.js", "Framer", "Shopify"

**Spørsmål 3:** Hvilke analytics-verktøy har dere?
- Eksempler: "GA4", "Plausible", "Fathom", "Ingen"
- Har dere Google Search Console satt opp?

**Spørsmål 4:** Hvilke sosiale medier er aktive?
- Eksempler: "LinkedIn", "Instagram", "TikTok", "X", "Facebook"
- Ca. hvor mange følgere per kanal?

**Spørsmål 5:** Bruker dere betalt annonsering?
- Eksempler: "Google Ads", "Meta Ads", "LinkedIn Ads", "Ingen"
- Hvis ja: ca. månedlig budsjett?

**Spørsmål 6:** Har dere CRM eller salgssystem?
- Eksempler: "HubSpot", "Pipedrive", "Salesforce", "Notion", "Regneark", "Ingen"

### Kanalstrategi

**Spørsmål 7:** Hvilke kanaler gir best resultater i dag?
- Eksempel: "Organic search", "LinkedIn", "Referrals"
- Hvis ny: "Ikke nok data ennå"

**Spørsmål 8:** Hvor vil dere satse mer fremover?
- Prioriter gjerne
- Hva er hypotesen for hvorfor denne kanalen?

---

## Steg 4: Opprett DISTRIBUTION.md og LEARNINGS.md

### DISTRIBUTION.md

1. Opprett `marketing/DISTRIBUTION.md`
2. Se `examples/DISTRIBUTION.md` for struktur
3. Inkluder:
   - Marketing Stack (email, CMS, analytics, social, ads, CRM)
   - Current Channels med primary/secondary/experimental
   - Budget Split visualisering
   - SEO & AEO Strategy med tomme tabeller
4. Marker "[Ikke satt opp ennå]" for verktøy som mangler

### LEARNINGS.md (hvis ikke finnes)

Opprett tom template for LEARNINGS.md:

```markdown
# Learnings

> Dokumentasjon av tester, resultater og innsikter.
> Fyll ut underveis når du kjører markedsføringsaktiviteter.

---

## Oversikt

| Periode | Test | Resultat | BAF Status |
|---------|------|----------|------------|
| [dato] | [test] | [resultat] | [status] |

**Nåværende BAF Status:** ⚠️ Ikke validert ennå

---

## Brand Audience Fit Validering

*[Fyll ut når du kjører første validering]*

---

## Hva vi har lært

### Hva fungerer ✅

| Innsikt | Bevis | Implementert? |
|---------|-------|---------------|
| [innsikt] | [bevis] | [✅/❌] |

### Hva fungerer ikke ❌

| Innsikt | Bevis | Handling |
|---------|-------|----------|
| [innsikt] | [bevis] | [handling] |

---

*Sist oppdatert: [dato]*
```

---

## Steg 5: Bekreft og Neste Steg

```
═══════════════════════════════════════════════════════════════
                  ✅ DISTRIBUTION.md OPPRETTET
═══════════════════════════════════════════════════════════════

📁 marketing/DISTRIBUTION.md
📁 marketing/LEARNINGS.md (tom template)

DISTRIBUTION.md inneholder:
• Marketing Stack-oversikt
• Kanalstrategi (primary/secondary)
• SEO & AEO Strategy (tomme tabeller)
• Quick Start-guide for organic SEO

LEARNINGS.md:
• Tom template for å dokumentere tester
• Fyll ut underveis

───────────────────────────────────────────────────────────────
STATUS
───────────────────────────────────────────────────────────────

[✅/❌] BRAND.md        - Merkevare
[✅/❌] JOURNEY.md      - Kundereise
✅ DISTRIBUTION.md  - Nettopp opprettet
✅ LEARNINGS.md     - Tom template

───────────────────────────────────────────────────────────────
NESTE STEG
───────────────────────────────────────────────────────────────

[Hvis BRAND.md mangler:]
💡 Kjør /marketing-playbook:brand-init for merkevare-grunnlag

[Hvis JOURNEY.md mangler:]
💡 Kjør /marketing-playbook:journey-init for kundereise

[Hvis du har en nettside:]
🚀 Kjør /seo-aeo:audit for SEO og AI-synlighet-sjekk
🚀 Fyll ut keyword-tabellene i DISTRIBUTION.md

═══════════════════════════════════════════════════════════════
```
