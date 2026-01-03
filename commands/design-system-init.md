---
description: Initialize Design System for this project. Creates DESIGN-SYSTEM.md through iterative demo-driven setup with landing page examples.
allowed-tools: Read, Write, Glob, Bash, AskUserQuestion
---

# Design System - Init

Opprett `marketing/DESIGN-SYSTEM.md` gjennom en iterativ, demo-drevet prosess.

---

## Arkitektur-påminnelse

```
┌─────────────────────────────────────────────────────────────────────┐
│ DU ER HER: Kjører init i en spesifikk kodebase                     │
│                                                                     │
│ Marketing Playbook (plugin) = Rammeverk og metodikk                │
│ ./marketing/ (denne kodebasen) = Skreddersydde verdier            │
│                                                                     │
│ Design systemet du bygger nå skal være for DETTE PROSJEKTET.       │
│ Bruk skills/design-system/* som metodikk-guide, men output skal   │
│ være konkrete verdier (hex-koder, fontnavn, komponenter) for      │
│ denne spesifikke merkevaren.                                       │
└─────────────────────────────────────────────────────────────────────┘
```

**Fokus:** Bygg et design system som er unikt for denne kodebasen og merkevaren den representerer.

---

## Steg 1: Sjekk eksisterende

Sjekk om disse filene finnes:
- `marketing/DESIGN-SYSTEM.md`
- `marketing/BRAND.md` (for Design-seksjon)

### Hvis DESIGN-SYSTEM.md finnes:
```
Eksisterende design system funnet i marketing/DESIGN-SYSTEM.md

Vil du:
1. Overskrive helt (start på nytt)
2. Oppdatere basert på eksisterende
3. Kun bygge demo basert på eksisterende
4. Avbryt
```

### Hvis BRAND.md ikke finnes:
```
⚠️ BRAND.md ikke funnet.

For best resultat, kjør /marketing-playbook:init først for å sette opp
merkevare-grunnlaget. Design systemet bygger på brand-verdier.

Vil du fortsette uten BRAND.md? (ikke anbefalt)
```

---

## Steg 2: Introduksjon

```
═══════════════════════════════════════════════════════════════
                    DESIGN SYSTEM - INIT
═══════════════════════════════════════════════════════════════

Velkommen! Jeg skal hjelpe deg med å skape et unikt design system
som reflekterer merkevaren din og IKKE ser ut som generisk AI-output.

┌─────────────────────────────────────────────────────────────┐
│ Prosessen:                                                  │
│                                                             │
│ 1. Kartlegger hva du har i dag                             │
│ 2. Forstår din visuelle visjon                             │
│ 3. Bygger 1-3 demo-sider                                   │
│ 4. Itererer til du er fornøyd                              │
│ 5. Dokumenterer i DESIGN-SYSTEM.md                         │
│                                                             │
│ Dette er en ITERATIV prosess - du gir feedback, jeg        │
│ justerer, til vi har noe du er stolt av.                   │
└─────────────────────────────────────────────────────────────┘

Estimert tid: 20-40 minutter (avhengig av iterasjoner)

═══════════════════════════════════════════════════════════════
```

---

## Steg 3: Kartlegging

### 3.1 Eksisterende Assets

**Spørsmål 1:** Har du eksisterende design-elementer? Del det du har:
- Logo (filsti eller URL)
- Farger (hex-koder hvis kjent)
- Fonts (navn hvis kjent)
- Eksisterende nettside (URL)
- Mood board / inspirasjonsbilder
- Brand guidelines dokument

*Tips: "Ikke noe ennå" er helt OK - vi starter fra scratch.*

**Spørsmål 2:** Hvilke frontend-frameworks bruker dere?
- [ ] Next.js / React
- [ ] Tailwind CSS
- [ ] shadcn/ui
- [ ] Radix UI
- [ ] CSS Modules
- [ ] styled-components
- [ ] Vue / Nuxt
- [ ] Vanilla CSS/HTML
- [ ] Annet: ___

**Spørsmål 3:** Har dere eksisterende UI-komponenter?
- Del mapper/filer med komponenter
- Eller beskriv hva som finnes
- "Ingenting" er OK

### 3.2 Visuell Visjon

**Spørsmål 4:** Beskriv "viben" du ønsker med 3-5 ord
```
Eksempler:
- "Moderne, leken, fargerikt"
- "Minimalistisk, profesjonell, dempet"
- "Rå, autentisk, jordnær"
- "Premium, eksklusiv, sofistikert"
```

**Spørsmål 5:** Vis meg 2-3 nettsider du LIKER visuelt
- URL + hva du liker ved dem
- Kan være konkurrenter eller helt andre bransjer

**Spørsmål 6:** Vis meg 1-2 nettsider du IKKE liker
- URL + hva som ikke fungerer
- Hjelper meg forstå hva du vil unngå

**Spørsmål 7:** Hvilken aesthetic direction passer best?

```
1. Brutalist/Raw      - Rå, upolert, konfronterende
2. Minimal/Refined    - Elegant, luftig, sofistikert
3. Maximalist/Chaos   - Energisk, fargerikt, leken
4. Organic/Natural    - Jordnær, varm, autentisk
5. Retro/Futuristic   - Nostalgi, neon, tech
6. Editorial/Magazine - Typografi-drevet, autoritet
7. Playful/Toy-like   - Glad, rund, vennlig
8. Annet (beskriv)
```

Se skills/design-system/AESTHETIC-DIRECTION.md for detaljer om hver retning.

### 3.3 Praktiske Behov

**Spørsmål 8:** Hva skal bygges først?
- Landing page
- Dashboard/App
- E-commerce
- Blog/Content site
- Portfolio
- Annet

**Spørsmål 9:** Er du fornøyd med nåværende design, eller vil du løfte det?
```
1. Behold nåværende retning - bare systematiser
2. Evoluer - bedre versjon av det vi har
3. Revolusjon - helt ny retning
```

---

## Steg 4: Demo-valg

```
───────────────────────────────────────────────────────────────
                      DEMO-MODUS
───────────────────────────────────────────────────────────────

Nå demonstrerer jeg forståelsen min ved å bygge noe konkret.

Velg demo-tilnærming:

┌─────────────────────────────────────────────────────────────┐
│ 1. SHOWCASE APP (anbefalt for evaluering)                   │
│    - Egen app med 2-3 demo landing pages                   │
│    - Kan kjøres lokalt for evaluering                      │
│    - Lett å sammenligne alternativer                       │
│    - Best for iterasjon                                    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 2. DIREKTE I PROSJEKT                                       │
│    - Bygger rett i eksisterende kodebase                   │
│    - Raskere til produksjon                                │
│    - Vanskeligere å iterere                                │
│    - Best når retningen er klar                            │
└─────────────────────────────────────────────────────────────┘

───────────────────────────────────────────────────────────────
```

### Hvis Showcase App:

1. Opprett midlertidig prosjekt:
```bash
# Med valgt framework
npx create-next-app@latest design-showcase --typescript --tailwind --app
cd design-showcase
npx shadcn@latest init  # hvis shadcn valgt
```

2. Bygg showcase-struktur:
```
design-showcase/
├── app/
│   ├── page.tsx           # Directory med alle alternativer
│   ├── option-1/page.tsx  # Landing page variant 1
│   ├── option-2/page.tsx  # Landing page variant 2
│   └── option-3/page.tsx  # Landing page variant 3
```

3. Directory-side med oversikt:
```tsx
// Mørk bakgrunn, kort for hver variant
// Klikk for å åpne full-page preview
```

4. Kjør lokalt:
```bash
npm run dev
# Bruker evaluerer i browser på localhost:3000
```

### Hvis Direkte i Prosjekt:

1. Identifiser eksisterende side å redesigne, eller opprett ny
2. Bygg inkrementelt med feedback
3. Bruk git branches for å lett kunne rulle tilbake

---

## Steg 5: Første Demo

### Oppsummering før bygging

```
═══════════════════════════════════════════════════════════════
                      DEMO 1 - OPPSETT
═══════════════════════════════════════════════════════════════

Basert på kartleggingen bygger jeg nå:

📋 OPPSUMMERING
───────────────────────────────────────────────────────────────
Aesthetic Direction: [valgt retning]
Vibe-ord:            [3-5 ord fra bruker]
Inspirasjons-sider:  [URLer bruker delte]
Primær bruk:         [landing page / dashboard / etc]
Framework:           [Next.js + Tailwind + shadcn / etc]

🎨 FOKUSOMRÅDER
───────────────────────────────────────────────────────────────
- Typografi-valg basert på [vibe]
- Fargepalett inspirert av [kilder]
- Layout-stil: [symmetrisk/asymmetrisk/grid]
- Motion: [minimal/moderat/ekspressiv]

⏳ Vennligst vent mens jeg bygger...

═══════════════════════════════════════════════════════════════
```

### Bygg demo

1. Velg fonts som matcher aesthetic direction
2. Definer fargepalett
3. Bygg hero section
4. Bygg 2-3 ekstra seksjoner
5. Legg til mikro-interaksjoner
6. Sjekk mot ANTI-PATTERNS.md

### Etter bygging

```
───────────────────────────────────────────────────────────────
                      DEMO 1 FERDIG
───────────────────────────────────────────────────────────────

🚀 For å se demoen:

cd design-showcase
npm run dev
# Åpne http://localhost:3000

───────────────────────────────────────────────────────────────
GI MEG FEEDBACK
───────────────────────────────────────────────────────────────

1. Hva FUNGERER?
   (Farger, typografi, layout, vibe?)

2. Hva fungerer IKKE?
   (For mye/lite av noe? Feil retning?)

3. Hva MANGLER?
   (Noe du forventet som ikke er der?)

4. Skala 1-10: Hvor nær er dette?
   (10 = perfekt, 1 = helt feil)

Eller skriv "godkjent" for å gå videre til dokumentasjon.

───────────────────────────────────────────────────────────────
```

---

## Steg 6: Iterasjon

Gjenta til bruker gir sign-off:

1. **Motta feedback**
   - Hva fungerer?
   - Hva må endres?
   - Hva mangler?

2. **Identifiser justeringer**
   - Konkrete endringer basert på feedback
   - Prioriter de viktigste

3. **Bygg oppdatert demo**
   - Implementer endringer
   - Test mot ANTI-PATTERNS.md

4. **Be om ny feedback**

### Etter 3 iterasjoner

```
───────────────────────────────────────────────────────────────
Vi har iterert 3 ganger. La oss konkretisere:

1. Hva er de 3 VIKTIGSTE tingene som MÅ endres?
2. Hva kan vi akseptere som "godt nok for nå"?
3. Er vi på riktig spor, eller trenger vi ny retning?
───────────────────────────────────────────────────────────────
```

### Maks 5 iterasjoner

Etter 5 iterasjoner:
```
Vi har nådd 5 iterasjoner. Dette er vanligvis nok for å lande et design.

Alternativer:
1. Godkjenn nåværende versjon
2. Identifiser ÉN kritisk endring, så godkjenner vi
3. Ta en pause og fortsett senere med /design-system:init
```

---

## Steg 7: Sign-off

Når bruker godkjenner:

```
═══════════════════════════════════════════════════════════════
                      ✅ SIGN-OFF
═══════════════════════════════════════════════════════════════

Demo godkjent etter [X] iterasjoner!

Jeg dokumenterer nå design systemet i:
📁 marketing/DESIGN-SYSTEM.md

Inkluderer:
- Aesthetic direction og vibe
- Fargepalett med tokens
- Typografi-system med fonts
- Komponent-eksempler fra demo
- Motion/animation guidelines
- Do's and Don'ts basert på feedback

═══════════════════════════════════════════════════════════════
```

---

## Steg 8: Generer DESIGN-SYSTEM.md

Opprett `marketing/DESIGN-SYSTEM.md` basert på godkjent demo.

Se examples/DESIGN-SYSTEM.md for template-struktur.

Inkluder:
- Alt fra demo som ble godkjent
- Konkrete CSS-variabler
- Font-loading instruksjoner
- Komponent-kode fra demo
- Animasjon-verdier
- Do's and Don'ts fra iterasjonene

---

## Steg 9: Oppdater BRAND.md

Oppdater Design-seksjonen i BRAND.md for å referere til DESIGN-SYSTEM.md:

```markdown
## Design

→ Se [marketing/DESIGN-SYSTEM.md](DESIGN-SYSTEM.md) for komplett design system.

### Quick Reference
**Aesthetic:** [vibe-ord]
**Primary Color:** [hex]
**Display Font:** [font]
**Body Font:** [font]
**Direction:** [valgt retning]
```

---

## Steg 10: Bekreft

```
═══════════════════════════════════════════════════════════════
                         ✅ FERDIG!
═══════════════════════════════════════════════════════════════

Design System er satt opp:

📁 marketing/
   🎨 DESIGN-SYSTEM.md  ← Komplett design system

📝 BRAND.md oppdatert med Design-referanse

📂 design-showcase/     ← Demo-app (kan slettes eller beholdes)

───────────────────────────────────────────────────────────────
NESTE STEG
───────────────────────────────────────────────────────────────

1. Review DESIGN-SYSTEM.md og juster detaljer
2. Implementer komponenter i hovedprosjektet
3. Kjør /design-system for å se status
4. Design system aktiveres automatisk ved UI-arbeid

───────────────────────────────────────────────────────────────
TIPS
───────────────────────────────────────────────────────────────

• Skillen aktiveres når du jobber med UI/UX
• Den sjekker alltid mot DESIGN-SYSTEM.md
• Bruk /marketing-playbook:check for å validere UI mot brand
• Oppdater DESIGN-SYSTEM.md når designet utvikler seg

═══════════════════════════════════════════════════════════════
```

---

## Håndtering av spesielle tilfeller

### Bruker har allerede et design

1. Be om URL eller skjermbilder
2. Analyser eksisterende stil
3. Spør om de vil:
   - Dokumentere eksisterende
   - Forbedre eksisterende
   - Starte på nytt

### Bruker er usikker på retning

1. Vis de 7 aesthetic directions
2. Be om 2-3 nettsider de liker
3. Foreslå retning basert på BRAND.md
4. Bygg 2-3 varianter i demo

### Bruker har begrenset tid

```
Forkortet modus:

1. Gi meg 3 nettsider du liker
2. Velg aesthetic direction (1-7)
3. Jeg bygger én demo
4. Du godkjenner eller gir 3 konkrete endringer
5. Ferdig etter maks 2 iterasjoner
```

### Bruker vil bare dokumentere eksisterende

1. Be om tilgang til eksisterende kodebase
2. Analyser:
   - Fonts i bruk
   - Farger (kjør farge-ekstraksjon)
   - Spacing-mønster
   - Komponent-stiler
3. Generer DESIGN-SYSTEM.md basert på funn
4. Foreslå eventuelle forbedringer
