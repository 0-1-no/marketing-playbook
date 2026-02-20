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

---

## CRO-fokusert Sidestruktur

### Above the Fold

| Element | Retningslinjer |
|---------|---------------|
| **Overskrift** | Ditt viktigste budskap. Kommuniser kjerneverdi. Spesifikt > generisk. |
| **Underoverskrift** | Utvider overskriften. Legger til spesifisitet. 1–2 setninger maks. |
| **Primær CTA** | Handlingsorientert. Kommuniser hva de får: «Start gratis prøve» > «Registrer deg» |

**Overskrift-formler:**
- «{Oppnå resultat} uten {smertepunkt}»
- «{Kategori} for {målgruppe}»
- «Aldri {ubehagelig hendelse} igjen»
- «{Spørsmål som adresserer hovedsmerte}»

### Kjerneseksjoner

| Seksjon | Formål |
|---------|--------|
| Sosialt bevis | Bygg troverdighet (logoer, tall, testimonials) |
| Problem/Smerte | Vis at du forstår situasjonen |
| Løsning/Fordeler | Koble til resultater (3–5 nøkkelfordeler) |
| Hvordan det fungerer | Reduser opplevd kompleksitet (3–4 steg) |
| Innvendingshåndtering | FAQ, sammenligninger, garantier |
| Siste CTA | Oppsummer verdi, gjenta CTA, risikoreversering |

---

## CTA-Retningslinjer

### Svake CTAs (unngå)
- Send inn, Registrer deg, Les mer, Klikk her, Kom i gang

### Sterke CTAs (bruk)
- Start gratis prøve
- Få [spesifikk ting]
- Se [Produkt] i aksjon
- Lag din første [ting]
- Last ned guiden

**Formel:** [Handlingsverb] + [Hva de får] + [Kvalifisering om nødvendig]

---

## Sidetype-Spesifikk Veiledning

### Hjemmeside
- Server flere målgrupper uten å bli generisk
- Led med bredeste verdiforslag
- Gi tydelige stier for ulike besøksintenter

### Landing Page
- Én melding, én CTA
- Match overskrift til annonse/trafikkilde
- Komplett argument på én side

### Prisside
- Hjelp besøkende velge riktig plan
- Adresser «hvilken passer for meg?»-angst
- Gjør anbefalt plan tydelig

### Funksjonsside
- Koble funksjon → fordel → resultat
- Vis brukstilfeller og eksempler
- Tydelig sti til å prøve eller kjøpe

### Om oss-side
- Fortell historien om hvorfor dere finnes
- Koble misjon til kundefordel
- Inkluder fortsatt en CTA

---

## Skriveregler for Konvertering

1. **Enkelt over komplekst** — «Bruk» ikke «benytt», «hjelp» ikke «tilrettelegg»
2. **Spesifikt over vagt** — Unngå «effektivisere», «optimalisere», «innovativt»
3. **Aktivt over passivt** — «Vi lager rapporter» ikke «Rapporter blir lagd»
4. **Trygt over kvalifisert** — Fjern «nesten», «veldig», «egentlig»
5. **Vis over fortell** — Beskriv resultatet i stedet for å bruke adjektiver
6. **Ærlig over sensasjonelt** — Aldri fabriker statistikk eller testimonials
