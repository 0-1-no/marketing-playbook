---
name: analytics-tracking
description: Sporingsoppsett og måling — event tracking, conversion tracking, UTM-parametere, sporingsplaner og analyse. Aktiveres ved sporing, analytics, conversion tracking, event tracking, UTM, sporingsplan eller «sett opp tracking». For A/B-test-måling, se ab-test-setup.
---

# Analytics og Sporing

Du er en ekspert på analytics-implementering og måling. Målet er å sette opp sporing som gir handlingsbare innsikter for markedsførings- og produktbeslutninger.

---

## Arkitektur: Global Plugin → Lokal Kodebase

```
┌─────────────────────────────────────────────────────────────────────┐
│ ANALYTICS-TRACKING SKILL (Global Plugin)                            │
│                                                                     │
│ Generell sporingsmetodikk for markedsføring og produkt.            │
│ Dekker PostHog, GA4 og andre analytics-verktøy.                    │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ ./marketing/DISTRIBUTION.md (DENNE KODEBASEN)                       │
│                                                                     │
│ • Kanalstrategi → Hvilke kanaler som trenger sporing               │
│ • Konverteringsmål → Hva som skal måles                            │
│ • KPI-er → Metrikker og benchmarks                                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Før du starter

1. **Les `./marketing/DISTRIBUTION.md`** — Kanalstrategi og KPI-er
2. **Les `./marketing/BRAND.md`** — Konverteringsmål knyttet til posisjonering
3. **Forstå teknisk stack** — Påvirker implementeringsmetode

Hvis filene ikke finnes, kjør `/marketing-playbook:init` først.

---

## Kjerneprinsipp

### 1. Spor for Beslutninger, Ikke Data
- Hvert event skal informere en beslutning
- Unngå forfengelighetsmetrikker
- Kvalitet > antall events

### 2. Start med Spørsmålene
- Hva trenger du å vite?
- Hvilke handlinger vil du ta basert på disse dataene?
- Jobb baklengs til hva du trenger å spore

### 3. Navngi Konsistent
- Navnekonvensjoner betyr mye
- Etabler mønstre FØR implementering
- Dokumenter alt

### 4. Vedlikehold Datakvalitet
- Valider implementeringen
- Overvåk for problemer
- Ren data > mer data

---

## Sporingsplan-Rammeverk

### Struktur

```
Event-Navn | Kategori | Egenskaper | Trigger | Notater
---------- | -------- | ---------- | ------- | -------
```

### Event-Typer

| Type | Eksempler |
|------|-----------|
| Sidevisninger | Automatisk, beriket med metadata |
| Brukerhandlinger | Knappeklikk, skjemainnsendinger, funksjonsbruk |
| Systemevents | Registrering fullført, kjøp, abonnement endret |
| Egendefinerte konverteringer | Målfullføringer, trakt-steg |

---

## Event-Navnekonvensjoner

### Anbefalt Format: Objekt-Handling

```
signup_completed
button_clicked
form_submitted
article_read
checkout_payment_completed
```

### Beste Praksis
- Små bokstaver med understrek
- Vær spesifikk: `cta_hero_clicked` vs. `button_clicked`
- Inkluder kontekst i egenskaper, ikke i event-navn
- Unngå mellomrom og spesialtegn
- Dokumenter beslutninger

---

## Essensielle Events

### Markedsføringsside

| Event | Egenskaper |
|-------|------------|
| `cta_clicked` | button_text, location |
| `form_submitted` | form_type |
| `signup_completed` | method, source |
| `demo_requested` | — |

### Produkt/App

| Event | Egenskaper |
|-------|------------|
| `onboarding_step_completed` | step_number, step_name |
| `feature_used` | feature_name |
| `purchase_completed` | plan, value |
| `subscription_cancelled` | reason |

---

## UTM-Parameterstrategi

### Standard Parametere

| Parameter | Formål | Eksempel |
|-----------|--------|----------|
| utm_source | Trafikkilde | google, nyhetsbrev, linkedin |
| utm_medium | Markedsføringskanal | cpc, email, social, organic |
| utm_campaign | Kampanjenavn | vaar_kampanje_2026 |
| utm_content | Differensier versjoner | hero_cta, sidebar_banner |
| utm_term | Betalte søkeord | regnskapsprogram |

### Navnekonvensjoner
- Små bokstaver overalt
- Bruk understrek eller bindestrek konsistent
- Vær spesifikk men konsis: `blogg_footer_cta`, ikke `cta1`
- Dokumenter alle UTM-er i et regneark

---

## Feilsøking og Validering

### Valideringssjekkliste

- [ ] Events utløses på riktige triggere
- [ ] Egenskapsverdier fylles riktig
- [ ] Ingen dupliserte events
- [ ] Fungerer på tvers av nettlesere og mobil
- [ ] Konverteringer registreres korrekt
- [ ] Ingen personopplysninger lekker

### Vanlige Problemer

| Problem | Sjekk |
|---------|-------|
| Events utløses ikke | Trigger-konfigurasjon, er analytics lastet? |
| Feil verdier | Variabelsti, datalayer-struktur |
| Dupliserte events | Flere containere, trigger utløses to ganger |

---

## Personvern og Samtykke

### GDPR-Krav (Norge/EØS)
- Samtykke kreves før sporing (ikke bare informasjon)
- Implementer samtykkeløsning (Cookiebot, Cookie Information, etc.)
- IP-anonymisering
- Datalagringsinnstillinger konfigurert
- Mulighet for brukersletting
- Samle kun det du trenger

### Cookie-Kategorier
| Kategori | Krever samtykke | Eksempler |
|----------|----------------|-----------|
| Nødvendig | Nei | Sesjon, innlogging |
| Analytics | Ja | PostHog, GA4 |
| Markedsføring | Ja | Meta Pixel, LinkedIn Insight |
| Preferanser | Ja | Språk, tema |

---

## Utdataformat

### Sporingsplan-Dokument

```markdown
# [Side/Produkt] Sporingsplan

## Oversikt
- Verktøy: [PostHog/GA4/etc.]
- Sist oppdatert: [Dato]

## Events

| Event-Navn | Beskrivelse | Egenskaper | Trigger |
|------------|-------------|------------|---------|
| signup_completed | Bruker fullfører registrering | method, plan | Suksessside |

## Konverteringer

| Konvertering | Event | Telling |
|--------------|-------|---------|
| Registrering | signup_completed | Én per økt |
```

---

## Verktøyspesifikke Guider

For detaljert implementering per verktøy:

| Verktøy | Best for |
|---------|----------|
| PostHog | Open-source, session replay, feature flags |
| GA4 | Google-økosystem, gratis, bred adopsjon |
| Mixpanel | Produkt-analytics, funnels, kohorter |

---

## Oppgavespesifikke Spørsmål

1. Hvilke verktøy bruker du (PostHog, GA4, Mixpanel, etc.)?
2. Hvilke nøkkelhandlinger vil du spore?
3. Hvilke beslutninger skal dataene informere?
4. Hvem implementerer — utviklere eller markedsføring?
5. Er det personvern-/samtykkekrav?
6. Hva spores allerede?

---

## Relaterte Skills

- `ab-test-setup` — Eksperimentsporing
- `seo-aeo` — Organisk trafikkanalyse
- `page-cro` — Konverteringsoptimalisering (bruker denne dataen)
