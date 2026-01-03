---
name: landing-pages
description: Konverteringsfokuserte sider for produkter, features, kampanjer og lead generation
content-type: landing-page
intent: transactional, commercial
typical-length: 500-1500 ord
seo-priority: high
aeo-priority: medium
journey-stages: consideration, evaluation
---

# Landing Pages

> **Metodikk-fil:** Faktiske verdier (tone, keywords, posisjonering) hentes fra `./marketing/BRAND.md` og `./marketing/CONTENT-RULES.md`.

Landing pages har ett mål: konvertering. Alt annet er støy.

---

## Landing Page-typer

### 1. Produkt/Feature Launch

**Formål:** Introdusere nytt produkt eller feature

**Fokus:**
- Hva er det?
- Hvem er det for?
- Hva løser det?
- Hvordan kommer du i gang?

### 2. Kampanje/Promotion

**Formål:** Tidsbegrenset tilbud eller kampanje

**Fokus:**
- Hva er tilbudet?
- Hvorfor nå? (urgency)
- Hva er verdien?
- Hvordan får du det?

### 3. Lead Generation

**Formål:** Samle leads i bytte mot verdi

**Fokus:**
- Hva får de? (lead magnet)
- Hvorfor er det verdifullt?
- Hva trengs? (minimal info)
- Hva skjer etter?

### 4. Sign-up / Trial

**Formål:** Få brukere til å registrere seg

**Fokus:**
- Hva får de tilgang til?
- Hvor enkelt er det å starte?
- Hvilken risiko fjernes? (gratis, ingen kort)
- Hva er neste steg?

### 5. Event Registration

**Formål:** Registrering til webinar, event, etc.

**Fokus:**
- Hva lærer de?
- Hvem er det for?
- Når er det?
- Hvordan melder de seg på?

---

## Den klassiske strukturen

```
┌─────────────────────────────────────────────┐
│ HERO                                         │
│ Hook + Value Proposition + Primær CTA       │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ PROBLEM                                      │
│ Agiter smertepunktet - "Du kjenner dette"   │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ LØSNING                                      │
│ Introduser produktet som løsningen          │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ BEVIS                                        │
│ Social proof - logoer, testimonials, tall   │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ FEATURES → BENEFITS                          │
│ Hva de får + hvorfor det betyr noe          │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ INNVENDINGER                                 │
│ FAQ, garantier, risikoreduksjon             │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ FINAL CTA                                    │
│ Gjenta med urgency                          │
└─────────────────────────────────────────────┘
```

---

## Above the Fold (Hero)

### Hva må være der

```
┌─────────────────────────────────────────────┐
│                                             │
│  [Headline - Én klar verdiproposisjon]     │
│                                             │
│  [Subheadline - Hvem er dette for]         │
│                                             │
│  [Primær CTA Button]  [Sekundær CTA]       │
│                                             │
│  [Supporting Visual]                        │
│                                             │
│  [Social proof snippet - valgfritt]        │
│                                             │
└─────────────────────────────────────────────┘
```

### Regler

| Element | Regel |
|---------|-------|
| Headline | Maks 10 ord, primært keyword inkludert |
| Subheadline | Maks 20 ord, hvem + hva |
| Primær CTA | Én knapp, én handling |
| Sekundær CTA | Kun hvis nødvendig (demo, lær mer) |
| Visual | Produkt i bruk, ikke stock photo |

### Headline-formler

**Value Prop:**
```
[Resultat] for [målgruppe]
"Automatisert bokføring for små bedrifter"
```

**How + Outcome:**
```
[Handling] som [resultat]
"Bygg landingssider som konverterer"
```

**Pain Point:**
```
Slutt å [smerte]. Start å [gevinst].
"Slutt å jage kunder. Start å bli funnet."
```

**Transformation:**
```
Fra [før] til [etter]
"Fra kaos til kontroll på 5 minutter"
```

---

## Problem-seksjon

### Formål
Få leseren til å nikke gjenkjennende. "Ja, det er akkurat sånn det er."

### Teknikker

**Pain Point Liste:**
```markdown
## Kjenner du igjen dette?

- Du bruker timer på manuell dataregistrering
- Informasjon ligger spredt i 10 forskjellige systemer
- Du glemmer oppfølging fordi det ikke er noe system
```

**Scenariobeskrivelse:**
```markdown
## Det starter alltid likt

Du får en ny lead. Du legger den inn i CRM. Så glemmer du
oppfølgingen fordi du har 50 andre ting å gjøre. Tre uker
senere husker du - men da er det for sent.
```

**Konsekvenser:**
```markdown
## Hva det koster deg

- 40% av leads går tapt til konkurrenter
- 10 timer per uke på manuelt arbeid
- Stress og dårlig samvittighet
```

---

## Løsning-seksjon

### Formål
Introduser produktet som svaret på problemet.

### Teknikker

**Direkte kobling:**
```markdown
## Det finnes en enklere måte

[Produktnavn] automatiserer hele prosessen. Fra lead kommer inn
til oppfølging sendes - uten at du løfter en finger.
```

**Før/Etter:**
```markdown
## Slik ser dagen din ut med [Produktnavn]

| Før | Etter |
|-----|-------|
| 2 timer på dataregistrering | 0 timer - alt skjer automatisk |
| Glemte oppfølginger | Automatiske påminnelser |
| 10 systemer | Alt på ett sted |
```

---

## Social Proof

### Typer og plassering

| Type | Plassering | Formål |
|------|------------|--------|
| Logo-stripe | Etter hero eller etter problem | Establish credibility |
| Testimonials | Etter løsning, etter benefits | Build trust |
| Tall/statistikk | I hero eller problem | Prove scale |
| Case studies | Mot slutten | Deep trust |
| Reviews/ratings | Nær CTA | Conversion boost |

### Logo-stripe

```markdown
Brukt av 500+ bedrifter:

[Logo] [Logo] [Logo] [Logo] [Logo]
```

### Testimonial-format

```markdown
> "[Sitat som adresserer en spesifikk innvending eller bekymring]"
>
> **Navn Etternavn**
> Stilling, Selskap
```

**Godt sitat:**
```
"Vi var skeptiske til enda et verktøy. Men etter 2 uker
hadde vi spart 8 timer per uke. Nå lurer vi på hvordan
vi klarte oss uten."
```

**Dårlig sitat:**
```
"Bra produkt, anbefales."
```

### Tall/statistikk

```markdown
## Tallene snakker for seg

- **10,000+** brukere
- **4.8/5** rating på G2
- **34%** økning i konverteringer i snitt
```

---

## Features → Benefits

### Prinsipp
Features er hva produktet gjør. Benefits er hva kunden får.

| Feature | → | Benefit |
|---------|---|---------|
| Automatiske e-postsekvenser | → | Aldri glem en oppfølging |
| Integrasjon med 100+ verktøy | → | Alt snakker sammen |
| Mobilapp | → | Jobb fra hvor som helst |

### Format

```markdown
## Alt du trenger for å [resultat]

### [Feature-navn]
[1-2 setninger om hva det er]

**Hva det betyr for deg:** [Benefit formulert som brukeropplevelse]
```

### Eksempel

```markdown
### Smart oppfølging

Automatiske påminnelser og sekvenser som tilpasser seg
kundens respons.

**Hva det betyr for deg:** Du glemmer aldri en oppfølging,
og kundene føler seg sett - uten at du gjør noe manuelt.
```

---

## Innvendingshåndtering

### Vanlige innvendinger og svar

| Innvending | Løsning på landing page |
|------------|------------------------|
| "For dyrt" | ROI-kalkulator, "Spar X timer" |
| "For komplisert" | "Kom i gang på 5 min", demo |
| "Ikke sikker på om det passer" | "For hvem er dette" seksjon |
| "Hva om det ikke fungerer?" | Garanti, gratis prøve |
| "Trenger jeg virkelig dette?" | Problem-seksjon, social proof |

### FAQ-seksjon

```markdown
## Vanlige spørsmål

### Er dette vanskelig å sette opp?

De fleste er i gang på under 5 minutter. Vi guider deg
gjennom hvert steg, og support er alltid tilgjengelig.

### Hva hvis det ikke passer for oss?

Du har 14 dager til å prøve helt gratis. Ingen binding,
ingen kredittkort nødvendig.

### Fungerer det med [verktøy vi allerede bruker]?

Vi integrerer med 100+ verktøy. [Se full liste]
```

### Garantier

```markdown
## 100% fornøyd-garanti

Prøv i 30 dager. Hvis du ikke er fornøyd, får du
pengene tilbake - ingen spørsmål stilt.
```

---

## CTA-skriving

### Primær CTA

| Regel | Eksempel |
|-------|----------|
| Handlingsverb + Benefit | "Start gratis prøve" |
| Førsteperson fungerer | "Start min gratis prøve" |
| Fjern friksjon | "Gratis", "Ingen kredittkort" |
| Spesifisér | "Få rapporten" > "Last ned" |

### CTA-formler

```
[Handling] + [Hva de får]
"Start gratis prøve"
"Få din gratis guide"
"Book en demo"
"Se priser"
```

### Sekundær CTA

Kun hvis det er et legitimt alternativt neste steg:
- "Se demo først"
- "Sammenlign planer"
- "Les case studies"

### CTA-plassering

| Sted | Type |
|------|------|
| Hero (above fold) | Primær + ev. sekundær |
| Etter social proof | Primær |
| Etter features | Primær |
| I footer | Primær (repeat) |

**Tommelfingerregel:** Minst 2 CTAs, helst 3-4 på en lang side.

---

## Landing Page Sjekkliste

### Hero (Above the Fold)
- [ ] Headline på maks 10 ord
- [ ] Subheadline som forklarer hvem/hva
- [ ] Én tydelig primær CTA
- [ ] Visuelt element (produkt, ikke stock)
- [ ] Ingen navigasjon som distraherer

### Innhold
- [ ] Problem tydelig artikulert
- [ ] Løsning koblet til problem
- [ ] Features presentert som benefits
- [ ] Social proof (logoer, testimonials, tall)
- [ ] FAQ for innvendinger
- [ ] Garanti eller risiko-reduksjon

### CTAs
- [ ] Primær CTA er handlingsverb + benefit
- [ ] CTA gjentas 2-4 ganger
- [ ] Friksjon fjernet (gratis, ingen kort)
- [ ] Tydelig hva som skjer etter klikk

### Teknisk
- [ ] Lastetid under 3 sekunder
- [ ] Mobilvennlig
- [ ] Ingen eksterne lenker (hold dem på siden)
- [ ] Tracking/analytics på plass

### Voice
- [ ] Matcher BRAND.md Tone of Voice
- [ ] Ingen Words We Avoid
- [ ] Følger CONTENT-RULES.md

---

## Vanlige feil å unngå

### For mye tekst
**Dårlig:** 2000+ ord på en landing page
**Godt:** 500-1500 ord, scannable

### Uklar CTA
**Dårlig:** "Send inn"
**Godt:** "Start gratis prøve"

### Ingen social proof
**Dårlig:** Bare påstander uten bevis
**Godt:** Logoer + testimonials + tall

### Feature-fokus over benefit-fokus
**Dårlig:** "AI-drevet automatisering"
**Godt:** "Spar 10 timer i uken"

### For mange CTAs/valg
**Dårlig:** 5 forskjellige handlinger
**Godt:** 1 primær, maks 1 sekundær

### Navigasjon
**Dårlig:** Full header med 10 lenker
**Godt:** Minimal header, fokus på CTA

---

## Templates per type

### Lead Gen Landing Page

```
[Hero: Hva får de + form]
[Problem: Hvorfor de trenger dette]
[Preview: Hva inneholder lead magnet]
[Social proof: Hvem har lastet ned]
[Form repeat med urgency]
```

### SaaS Trial Landing Page

```
[Hero: Value prop + "Start gratis"]
[Social proof: Logos]
[Problem: Pain points]
[Løsning: Produktoversikt]
[Features → Benefits: 3-5 hovedfunksjoner]
[Testimonials: Spesifikke resultater]
[Priser: Hvis relevant]
[FAQ: Vanlige innvendinger]
[Final CTA: Repeat with guarantee]
```

### Event Registration

```
[Hero: Hva lærer de + Dato/tid]
[Speakers/Host: Hvem presenterer]
[Agenda: Hva dekkes]
[Testimonials: Fra tidligere events]
[Registration form]
[FAQ: Opptak, tid, etc.]
```

---

## Integrasjonspunkter

| Trenger du... | Les... |
|---------------|--------|
| AIDA/PAS struktur | [FRAMEWORKS.md](../storytelling-copywriting/FRAMEWORKS.md) |
| Headline-teknikker | [HEADLINES.md](../storytelling-copywriting/HEADLINES.md) |
| Persuasjonsteknikker | [PERSUASION.md](../storytelling-copywriting/PERSUASION.md) |
| Button/CTA tekst | [MICROCOPY.md](../storytelling-copywriting/MICROCOPY.md) |
| SEO-optimalisering | [ON-PAGE-SEO.md](../seo-aeo/ON-PAGE-SEO.md) |
| Schema markup | [STRUCTURED-DATA.md](../seo-aeo/STRUCTURED-DATA.md) |
