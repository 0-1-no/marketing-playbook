---
description: Omfattende oppsett for content voice og regler. Oppretter CONTENT-RULES.md i marketing/-mappen med voice-dimensjoner, strukturregler og kvalitetsporter.
disable-model-invocation: true
allowed-tools: Read, Write, Glob, AskUserQuestion
---

# Content Writer Init

Denne kommandoen guider brukeren gjennom å definere innholdsspesifikke regler som komplementerer BRAND.md. Resultatet er en `./marketing/CONTENT-RULES.md` fil.

---

## Forutsetninger

**Påkrevd:** `./marketing/BRAND.md` må eksistere med Tone of Voice og Words We Use/Avoid.

Hvis BRAND.md mangler:
```
Jeg finner ingen BRAND.md i ./marketing/.

For å opprette innholdsregler trenger jeg først merkevare-fundamentet.
Kjør `/marketing-playbook:init` først, så kan vi fortsette med content-reglene.
```

---

## Arbeidsflyt

### Fase 0: Les eksisterende kontekst

1. Les `./marketing/BRAND.md`
2. Trekk ut:
   - Tone of Voice
   - Words We Use
   - Words We Avoid
   - Communication Principles
3. Bekreft for brukeren hva som allerede finnes

```
Jeg har lest BRAND.md. Her er det jeg fant:

**Tone of Voice:** [oppsummering]
**Words We Use:** [liste]
**Words We Avoid:** [liste]

Nå skal vi bygge videre på dette med spesifikke innholdsregler.
```

---

### Fase 1: Voice-dimensjoner (Spørsmål 1-8)

Introduser konseptet:

```
Vi skal definere din content voice på tvers av 4 dimensjoner.
For hver dimensjon, velg et punkt på spekteret som føles riktig.
```

#### Spørsmål 1: Formalitet

```
## Dimensjon 1: Formalitet

Hvor formell er kommunikasjonen deres?

Spekter:
├── 1: Casual ("Hei der! Klar for å rocke?")
├── 2: Uformell ("Hei! Fint at du er her.")
├── 3: Balansert ("Velkommen. La oss komme i gang.")
├── 4: Profesjonell ("Velkommen til [Selskap].")
└── 5: Formell ("Kjære kunde, vi takker for din henvendelse.")

Velg 1-5:
```

#### Spørsmål 2: Formalitet "This but not that"

```
Hva betyr dette nivået i praksis for dere?

Gi meg ett eksempel på:
- "This": Noe som høres riktig ut
- "Not that": Noe som går for langt / ikke langt nok
```

#### Spørsmål 3: Entusiasme

```
## Dimensjon 2: Entusiasme

Hvor energisk er dere?

Spekter:
├── 1: Reservert ("Her er informasjonen du trenger.")
├── 2: Rolig ("Gode nyheter: Funksjonen er klar.")
├── 3: Vennlig ("Vi er glade for å dele dette med deg!")
├── 4: Entusiastisk ("Dette er kjempespennende nyheter!")
└── 5: Euforisk ("VI ER SÅ HYPE! 🚀🎉")

Velg 1-5:
```

#### Spørsmål 4: Entusiasme "This but not that"

```
Eksempel på dette nivået:
- "This": [Be om eksempel]
- "Not that": [Be om eksempel]
```

#### Spørsmål 5: Teknisk dybde

```
## Dimensjon 3: Teknisk dybde

Hvor faglig/teknisk er språket?

Spekter:
├── 1: Hverdagsspråk ("Gjør nettsiden raskere")
├── 2: Enkelt fagspråk ("Optimaliserer lastetider")
├── 3: Bransjespråk ("Forbedrer Core Web Vitals")
├── 4: Teknisk ("Reduserer TTFB via edge caching")
└── 5: Ekspertnivå ("Implementerer Stale-While-Revalidate med ISR")

Velg 1-5:

Merk: Dette kan variere per content type (guide vs. landing page).
```

#### Spørsmål 6: Teknisk dybde "This but not that"

```
Eksempel på dette nivået:
- "This": [Be om eksempel]
- "Not that": [Be om eksempel]
```

#### Spørsmål 7: Personlighet

```
## Dimensjon 4: Personlighet

Hvor distinkt er merkevare-personligheten?

Spekter:
├── 1: Nøytral ("Vi tilbyr løsninger for...")
├── 2: Profesjonell med hint ("Vi mener sterkt at...")
├── 3: Tydelig personlighet ("Kall oss perfeksjonister, men...")
├── 4: Distinkt voice ("La oss være ærlige: De fleste byråer...")
└── 5: Unik karakter ("*sukk* Nok en rapport om AI...")

Velg 1-5:
```

#### Spørsmål 8: Personlighet "This but not that"

```
Eksempel på dette nivået:
- "This": [Be om eksempel]
- "Not that": [Be om eksempel]
```

---

### Fase 2: Strukturelle regler (Spørsmål 9-14)

```
Nå skal vi definere strukturelle regler for innholdet.
```

#### Spørsmål 9: Person

```
## Person

Hvilken person bruker dere oftest?

- A: Første person flertall ("Vi hjelper deg med...")
- B: Første person entall ("Jeg guider deg gjennom...")
- C: Tredjeperson ("[Selskapsnavn] tilbyr...")
- D: Blanding (varierer per kontekst)

Velg A-D:
```

#### Spørsmål 10: Sammentrekninger

```
## Sammentrekninger

Bruker dere sammentrekninger?

- A: Ja, alltid ("Vi kan ikke", "Det er ikke")
- B: Noen ganger (uformelt innhold ja, formelt nei)
- C: Sjelden (kun i sitater eller dialog)
- D: Aldri ("Vi kan ikke" → "Vi kan ikke")

Velg A-D:

(Engelsk: "can't" vs "cannot", "we're" vs "we are")
```

#### Spørsmål 11: Spørsmål til leseren

```
## Spørsmål til leseren

Stiller dere direkte spørsmål til leseren?

- A: Ofte ("Har du opplevd dette? Lurer du på hvorfor?")
- B: Noen ganger (i introer og avslutninger)
- C: Sjelden (kun i FAQ-seksjoner)
- D: Aldri (kun påstander og fakta)

Velg A-D:
```

#### Spørsmål 12: Emoji-policy

```
## Emojis

Hvordan bruker dere emojis i innhold?

- A: Aldri (rent profesjonelt)
- B: Kun i overskrifter/titler (✅ i lister OK)
- C: Sparsomt (1-2 per side, kun for vekt)
- D: Fritt (del av merkevare-personligheten)

Velg A-D:
```

#### Spørsmål 13: Standard innholdsformat

```
## Standard elementer

Hvilke elementer bør alltid/aldri inkluderes i artikler?

**Alltid inkluder (velg alle som gjelder):**
- [ ] TL;DR / Key Takeaways
- [ ] Innholdsfortegnelse
- [ ] Estimert lesetid
- [ ] FAQ-seksjon
- [ ] CTA i konklusjon
- [ ] Forfatter-byline
- [ ] "Sist oppdatert" dato

**Aldri inkluder:**
- [ ] [Be bruker om input]
```

#### Spørsmål 14: Lenke-krav

```
## Interne lenker

Minimum antall interne lenker per artikkel?

- A: Ingen krav
- B: 2-3 lenker
- C: 4-5 lenker
- D: 5+ lenker

Velg A-D:
```

---

### Fase 3: Kvalitetsporter (Spørsmål 15-17)

```
Til slutt: Hva må være på plass før innhold publiseres?
```

#### Spørsmål 15: Minimum ordtelling

```
## Lengdekrav

Har dere minimum ordtelling per type?

**Artikler/Blogg:**
- A: Ingen minimum
- B: 500+ ord
- C: 1000+ ord
- D: 1500+ ord

**Landing pages:**
- A: Ingen minimum
- B: 300+ ord
- C: 500+ ord
- D: 800+ ord

Velg for hver:
```

#### Spørsmål 16: Review-prosess

```
## Review-sjekkliste

Hva må sjekkes før publisering?

**Obligatoriske sjekker (velg alle som gjelder):**
- [ ] Stavekontroll
- [ ] Faktasjekk / kilder verifisert
- [ ] SEO-optimalisering (title, meta, H-tags)
- [ ] Merkevare-alignment (tone, words)
- [ ] Mobil-preview
- [ ] Lenker fungerer
- [ ] Bilder har alt-tekst
- [ ] CTA fungerer
```

#### Spørsmål 17: Sign-off

```
## Publiserings-godkjenning

Hvem godkjenner før publisering?

- A: Forfatter selv (ingen ekstern review)
- B: Peer review (kollega)
- C: Editor/markedssjef
- D: Kunde/ekstern godkjenning

Velg A-D:
```

---

### Fase 4: Content Showcase (Valgfritt)

```
───────────────────────────────────────────────────────────────
                    CONTENT SHOWCASE
───────────────────────────────────────────────────────────────

Vil du se eksempler i en visuell showcase-app?

┌─────────────────────────────────────────────────────────────┐
│ 1. SHOWCASE APP (anbefalt)                                   │
│    - Visuell demo av voice i ulike kontekster               │
│    - Lett å sammenligne og iterere                          │
│    - Kan deles med team                                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 2. INLINE EKSEMPLER                                          │
│    - Raskere, ingen app å sette opp                         │
│    - Eksempler rett i samtalen                              │
└─────────────────────────────────────────────────────────────┘

───────────────────────────────────────────────────────────────
```

#### Hvis Showcase App:

1. Opprett prosjekt:
```bash
npx create-next-app@latest content-showcase --typescript --tailwind --app
cd content-showcase
```

2. Bygg showcase-struktur:
```
content-showcase/
├── app/
│   ├── page.tsx              # Oversikt med alle eksempler
│   ├── article-intro/page.tsx
│   ├── landing-hero/page.tsx
│   ├── faq-answer/page.tsx
│   ├── error-message/page.tsx
│   ├── email-subject/page.tsx
│   ├── cta-button/page.tsx
│   └── compare/page.tsx      # Før/etter sammenligning
```

3. Hver side viser:
   - Eksempeltekst i din voice
   - Voice-dimensjoner som ble brukt
   - "This" vs "Not that" sammenligning
   - Redigerbar versjon for tweaking

4. Kjør lokalt:
```bash
npm run dev
# Bruker evaluerer i browser på localhost:3000
```

#### Hvis Inline Eksempler:

Generer 6 eksempler i ulike kontekster:

```
Basert på dine svar, her er eksempler i din voice:

───────────────────────────────────────────────────────────────

**1. Artikkel-intro:**
> [Generert eksempel]

**2. Landing page hero:**
> [Generert eksempel]

**3. FAQ-svar:**
> [Generert eksempel]

**4. Error-melding:**
> [Generert eksempel]

**5. Email subject line:**
> [Generert eksempel]

**6. CTA-tekst:**
> [Generert eksempel]

───────────────────────────────────────────────────────────────

Høres disse ut som merkevaren din? Hva ville du endret?
```

### Fase 4b: Iterasjon

**Iterer til bruker bekrefter.**

Ved iterasjon (hvis showcase):
- Opprett ny versjon, IKKE overskriv
- Behold alle versjoner for sammenligning

---

### Fase 5: Opprett CONTENT-RULES.md

Generer filen basert på svarene:

```markdown
# [Brand] Content Rules

> Innholdsspesifikke regler for denne merkevaren. Les sammen med BRAND.md.
> Opprettet: [dato]

---

## Voice-dimensjoner

| Dimensjon | Nivå (1-5) | Beskrivelse |
|-----------|------------|-------------|
| Formalitet | [X] | [Beskrivelse fra "This but not that"] |
| Entusiasme | [X] | [Beskrivelse] |
| Teknisk dybde | [X] | [Beskrivelse] |
| Personlighet | [X] | [Beskrivelse] |

### "This but not that"

**Formalitet:**
- ✅ This: [eksempel]
- ❌ Not that: [eksempel]

**Entusiasme:**
- ✅ This: [eksempel]
- ❌ Not that: [eksempel]

**Teknisk dybde:**
- ✅ This: [eksempel]
- ❌ Not that: [eksempel]

**Personlighet:**
- ✅ This: [eksempel]
- ❌ Not that: [eksempel]

---

## Strukturelle regler

### Generelt
- **Person:** [Første person flertall / etc.]
- **Sammentrekninger:** [Policy]
- **Spørsmål til leser:** [Policy]
- **Emojis:** [Policy]

### Artikler/Blogg
- **Minimum lengde:** [X] ord
- **Alltid inkluder:** [liste]
- **Interne lenker:** Minimum [X]

### Landing Pages
- **Minimum lengde:** [X] ord
- **Alltid inkluder:** [liste]

### Guider
- **Forutsetninger-seksjon:** [Alltid/Ved behov]
- **Verifisering:** [Påkrevd/Valgfritt]

---

## Kvalitetsporter

### Før publisering
- [ ] [Obligatorisk sjekk 1]
- [ ] [Obligatorisk sjekk 2]
- [ ] [Obligatorisk sjekk 3]

### Godkjenning
[Godkjenningsprosess]

---

## Eksempel-voice

### Educational
> [Generert eksempel som ble godkjent]

### Persuasive
> [Generert eksempel som ble godkjent]

### Helpful
> [Generert eksempel som ble godkjent]

---

*Refererer til: BRAND.md for Tone of Voice og Words We Use/Avoid*
```

---

## Avslutning

```
═══════════════════════════════════════════════════════════════
                  ✅ CONTENT-RULES.md OPPRETTET
═══════════════════════════════════════════════════════════════

📁 marketing/CONTENT-RULES.md

Inneholder:
• Voice-dimensjoner (formalitet, entusiasme, teknisk dybde, personlighet)
• "This but not that"-eksempler
• Strukturelle regler
• Kvalitetsporter

[Hvis showcase-app:]
📂 content-showcase/    ← Demo-app med alle eksempler bevart

───────────────────────────────────────────────────────────────
STATUS - MARKETING PLAYBOOK
───────────────────────────────────────────────────────────────

[✅/❌] BRAND.md        - Merkevare
[✅/❌] JOURNEY.md      - Kundereise
[✅/❌] DISTRIBUTION.md - Kanaler og stack
[✅/❌] LEARNINGS.md    - Tester og innsikter
[✅/❌] DESIGN-SYSTEM.md - Visuell identitet
✅ CONTENT-RULES.md - Nettopp opprettet

───────────────────────────────────────────────────────────────
NESTE STEG
───────────────────────────────────────────────────────────────

1. Når du skriver innhold, refererer Claude til:
   - BRAND.md for merkevare-fundament
   - CONTENT-RULES.md for voice-dimensjoner og struktur

2. Bruk /marketing-playbook:check for å validere innhold

[Hvis DESIGN-SYSTEM.md mangler:]
💡 Kjør /design-system:init for visuell identitet

[Hvis BRAND.md mangler:]
💡 Kjør /marketing-playbook:brand-init for merkevare-grunnlag

═══════════════════════════════════════════════════════════════
```

---

## Integrasjon med andre kommandoer

- Etter `/marketing-playbook:init` - naturlig neste steg
- Før `/marketing-playbook:check` - reglene brukes til validering
- Med content-writing skill - refererer til CONTENT-RULES.md automatisk
