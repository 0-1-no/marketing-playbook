---
name: research-process
description: Metodikk for research til komplekst innhold med kilder, data og ekspert-sitater
content-type: meta
---

# Research Process

> **Metodikk-fil:** Dette er prosess-dokumentasjon som gjelder på tvers av alle content types.

Godt innhold krever godt research. Denne filen beskriver hvordan du samler, verifiserer og presenterer kilder.

---

## Når trengs research?

| Situasjon | Research-nivå | Eksempel |
|-----------|---------------|----------|
| Fakta-påstander | Obligatorisk | "73% av bedrifter bruker..." |
| Tall og statistikk | Obligatorisk | "Markedet er verdt $X milliarder" |
| Ekspertmeninger | Høy verdi | "Ifølge [Ekspert]..." |
| Konkurrentanalyse | Ofte nødvendig | "De tre ledende løsningene er..." |
| Teknisk nøyaktighet | Kritisk | API-dokumentasjon, spesifikasjoner |
| Trender og prognoser | Høy verdi | "[Bransje] forventes å vokse..." |
| Historisk kontekst | Ved behov | "Siden 2015 har..." |

### Rød flagg: Trenger research

- [ ] Jeg bruker ord som "mange", "ofte", "vanligvis" uten kilde
- [ ] Jeg påstår noe om markedsstørrelse eller vekst
- [ ] Jeg siterer tall jeg "husker" fra et sted
- [ ] Jeg beskriver en konkurrents produkt
- [ ] Jeg forklarer en teknisk prosess jeg ikke har gjort selv

---

## Research-arbeidsflyt

```
┌─────────────────────────────────────────────┐
│ 1. DEFINER RESEARCH-SPØRSMÅL                │
│    Hva trenger jeg å vite? Hvorfor?         │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 2. IDENTIFISER KILDE-TYPER                  │
│    Primær? Sekundær? Ekspert?               │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 3. SAMLE KILDER                             │
│    Prioriter etter hierarki                 │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 4. VERIFISER OG KRYSSREFERER                │
│    Minst 2 kilder for viktige påstander     │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 5. DOKUMENTER                               │
│    Full URL, dato, relevant sitat           │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 6. SKRIV MED ATTRIBUSJON                    │
│    Inline sitering, ikke bare lenker        │
└─────────────────────────────────────────────┘
```

---

## Kilde-hierarki

### Prioritet 1: Primærdata
Egen forskning, surveys, eksperimenter.

**Eksempler:**
- Egen kundeundersøkelse
- A/B-test resultater
- Analyse av egne data

**Styrke:** Unik, differensierende, høy troverdighet
**Svakhet:** Tidkrevende å samle

---

### Prioritet 2: Offisielle kilder
Myndigheter, akademia, selskapsrapporter.

**Eksempler:**
- SSB (statistikk.no)
- Regjeringen.no
- Universitetsforskining
- Selskapers årsrapporter (børsnoterte)

**Styrke:** Høy troverdighet, verifiserbar
**Svakhet:** Kan være utdatert, tørr presentasjon

---

### Prioritet 3: Bransjeforskning
Analysehus og bransjeorganisasjoner.

**Eksempler:**
- Gartner, Forrester, McKinsey
- Bransjeforeninger (IKT-Norge, etc.)
- Markedsundersøkelser (Statista, etc.)

**Styrke:** Relevant, ofte fersk
**Svakhet:** Kan ha bias, ofte bak paywall

---

### Prioritet 4: Ekspertsitater
Navngitte eksperter med credentials.

**Eksempler:**
- CEO-uttalelser i presse
- Fagfolk i intervjuer
- Konferanseforedrag

**Styrke:** Autoritet, menneskelig vinkel
**Svakhet:** Kan være subjektiv, kontekst kan mangle

---

### Prioritet 5: Anerkjente medier
Store publikasjoner med redaksjonell standard.

**Eksempler:**
- DN, E24, Shifter (Norge)
- TechCrunch, Wired, HBR (internasjonalt)
- Bransjetidsskrifter

**Styrke:** Lett tilgjengelig, aktuelt
**Svakhet:** Sekundærkilde, kan inneholde feil

---

### Prioritet 6: Community-kilder
Reddit, forums, Stack Overflow.

**Eksempler:**
- Reddit-diskusjoner
- Forum-tråder
- Stack Overflow-svar

**Styrke:** Ekte brukeropplevelser
**Svakhet:** Anonym, må verifiseres uavhengig

---

## Sitering i praksis

### Inline attribusjon

**Sterkt:**
```
Ifølge Gartner sin 2024-rapport, vil 75% av bedrifter
bruke AI i kundekommunikasjon innen 2026.
```

**Middels:**
```
En studie fra MIT viser at personaliserte e-poster
har 29% høyere åpningsrate.
```

**Svakt:**
```
Statistikk viser at e-postmarkedsføring fungerer.
```

### Sitering-formler

| Formel | Når bruke |
|--------|----------|
| "Ifølge [Kilde]..." | Autoritative påstander |
| "[Kilde] fant at..." | Research-resultater |
| "Som [Ekspert] påpeker..." | Ekspertmeninger |
| "Data fra [Kilde] viser..." | Statistikk |
| "[Kilde]s rapport fra [år] avdekket..." | Spesifikk forskning |

### Lenking

**Inline lenke (foretrekkes):**
```markdown
[Gartner-rapporten](URL) viser at...
```

**Fotnoter (for akademisk tone):**
```markdown
Markedet forventes å vokse med 15% årlig.¹

---
¹ Kilde: Gartner, "AI Market Report 2024"
```

**Samlet kildeliste:**
```markdown
## Kilder

- Gartner (2024). AI Market Report. [URL]
- McKinsey (2023). State of AI. [URL]
```

---

## Verifisering

### Sjekkliste for hver kilde

- [ ] **Primærkilde:** Kan jeg spore dette til originaldataen?
- [ ] **Aktualitet:** Er kilden fra siste 2 år? (For statistikk)
- [ ] **Konsensus:** Er andre kilder enige?
- [ ] **Kontekst:** Feilrepresenterer jeg noe ved å ta det ut av sammenheng?
- [ ] **Bias:** Har kilden åpenbare interesser?

### Røde flagg

| Tegn | Handling |
|------|----------|
| Ingen dato | Finn nyere kilde |
| "Studier viser" uten spesifikk kilde | Finn original studie |
| Runde tall (50%, 100x) | Verifiser, ofte markedsføringspåstand |
| Kun én kilde | Kryssreferer |
| Veldig gammel (>3 år for tech) | Finn fersk data |
| .com-domene som eneste kilde | Finn offisiell/akademisk kilde |

### Kryssreferering

For viktige påstander, bruk minst 2 uavhengige kilder:

```
Primærkilde: Gartner-rapport
Sekundærkilde: McKinsey-analyse
→ Hvis begge sier det samme, trygg å sitere
```

---

## Research-dokumentasjon

### Underveis: Research-logg

```markdown
## Research-logg: [Artikkel-tittel]

### Spørsmål 1: [Hva leter jeg etter?]

**Kilde 1:** [URL]
- Funnet: [Relevant info]
- Sitat: "[Direkte sitat]"
- Vurdering: [Pålitelig/Må verifisere]

**Kilde 2:** [URL]
- Funnet: [Relevant info]
- Bekrefter kilde 1: [Ja/Nei]

**Konklusjon:** [Hva jeg kan påstå trygt]

---

### Spørsmål 2: [Neste tema]
[Samme struktur]
```

### Etter publisering: Kildearkiv

Hold et arkiv over kilder du bruker ofte:

```markdown
## Ofte brukte kilder

### Markedsstørrelse
- Gartner: [URL til abonnement]
- Statista: [URL]

### Norsk statistikk
- SSB: statistikk.no
- Innovasjon Norge: rapporter

### Bransjeinnsikt
- Shifter: shifter.no
- E24: e24.no

### Teknisk dokumentasjon
- MDN Web Docs
- Official docs per teknologi
```

---

## Spesielle tilfeller

### Konkurrentinformasjon

**Tillatt:**
- Offentlig tilgjengelig prising
- Funksjoner fra deres hjemmeside
- Presseomtaler
- Brukeranmeldelser

**Forsiktig:**
- Sammenligningstabeller (hold oppdatert)
- Påstander om deres svakheter

**Unngå:**
- Interne tall fra lekkasjer
- Spekulasjon som fakta

### Prediksjoner og prognoser

**Godt:**
```
Gartner spår at AI-markedet vil vokse med 15% årlig
frem mot 2028. Andre analytikere, som IDC, anslår
10-20% avhengig av segment.
```

**Dårlig:**
```
AI-markedet vil eksplodere de neste årene.
```

### Egne meninger vs. fakta

**Merk tydelig:**
```
Vår erfaring tilsier at...
Vi mener at...
Dataene viser X, men vi tolker det som...
```

---

## AI-assistert research

### Bruk AI til

- Oppsummere lange rapporter
- Finne relevante søkeord
- Strukturere research-spørsmål
- Oversette utenlandske kilder

### Verifiser alltid

- AI kan "hallusinere" kilder
- Sjekk at URL-er faktisk eksisterer
- Les primærkilden selv
- Bekreft tall mot original

### Siter aldri AI som kilde

**Feil:**
```
Ifølge ChatGPT er markedet verdt $50 milliarder.
```

**Riktig:**
```
[Finn faktisk kilde på tallet]
```

---

## Research-sjekkliste

### Før du starter
- [ ] Definert spesifikke research-spørsmål
- [ ] Identifisert hvilke kildetyper som trengs
- [ ] Satt av nok tid (research tar tid)

### Underveis
- [ ] Dokumenterer alle kilder med URL og dato
- [ ] Lagrer relevante sitater
- [ ] Kryssrefererer viktige påstander
- [ ] Noterer usikkerheter

### Før publisering
- [ ] Alle fakta-påstander har kilder
- [ ] Kilder er fra siste 2 år (for statistikk)
- [ ] Inline attribusjon er brukt
- [ ] Lenker fungerer

### Etter publisering
- [ ] Arkivert research-logg
- [ ] Satt påminnelse for oppdatering (6-12 mnd)

---

## Integrasjonspunkter

| Trenger du... | Les... |
|---------------|--------|
| Skrive artikkel med research | [ARTICLES.md](ARTICLES.md) |
| Case study med kundedata | [ARTICLES.md](ARTICLES.md) → Case Study |
| Teknisk guide | [GUIDES.md](GUIDES.md) |
| Markedsanalyse | [ARTICLES.md](ARTICLES.md) → Industry Analysis |
| E-E-A-T signaler | [WEBSITE-PAGES.md](WEBSITE-PAGES.md) → Team |
