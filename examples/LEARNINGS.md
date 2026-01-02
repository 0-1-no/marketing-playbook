# Learnings

> Dokumentasjon av tester, resultater og innsikter for [Prosjektnavn]. Denne filen er beviset på Brand Audience Fit og grunnlaget for kontinuerlig forbedring.

---

## Oversikt

| Periode | Test | Resultat | BAF Status |
|---------|------|----------|------------|
| Jan 2025 | Venteliste-kampanje | ✅ 340 signups | Validert |
| Feb 2025 | Landing page A/B | ✅ +45% konvertering | Bekreftet |
| Mar 2025 | Ny målgruppe-test | ⚠️ Under terskel | Må iterere |

**Nåværende BAF Status:** ✅ Validert for primær målgruppe

---

## Brand Audience Fit Validering

### Test 1: Venteliste-kampanje (Jan 2025)

**Hypotese:**
Småbedriftseiere vil sette seg opp på venteliste for et automatiseringsverktøy hvis vi kommuniserer tidsbesparelse.

**Oppsett:**
- Kanal: Instagram + Facebook Ads
- Budsjett: 5.000 kr
- Varighet: 4 uker
- Målgruppe: Småbedriftseiere 30-55 år, Norge

**Resultater:**
| Metrikk | Mål | Resultat | Status |
|---------|-----|----------|--------|
| Venteliste-signups | 200 | 340 | ✅ |
| Cost per signup | <50 kr | 14,70 kr | ✅ |
| Konverteringsrate | ≥2% | 2.8% | ✅ |

**Segmentanalyse:**
| Segment | Signups | % av total | Konvertering |
|---------|---------|------------|--------------|
| Konsulenter | 142 | 42% | 3.4% |
| Frilansere | 89 | 26% | 2.9% |
| Småbedrift <5 ans. | 67 | 20% | 2.1% |
| Andre | 42 | 12% | 1.6% |

**Konklusjon:**
✅ Brand Audience Fit bekreftet for primær målgruppe. Konsulenter og frilansere responderer best.

---

### Test 2: Landing Page A/B (Feb 2025)

**Hypotese:**
"Spare tid" som hovedbudskap konverterer bedre enn "Automatiser arbeidet".

**Varianter:**
- A: "Automatiser arbeidet ditt" (kontroll)
- B: "Spar 10 timer i uken" (test)

**Resultater:**
| Variant | Besøk | Konverteringer | Rate |
|---------|-------|----------------|------|
| A (kontroll) | 1.240 | 28 | 2.3% |
| B (test) | 1.180 | 39 | 3.3% |

**Statistisk signifikans:** 94% (akseptabelt)

**Innsikt:**
Konkret tidsbesparelse ("10 timer") slår abstrakt fordel ("automatiser"). Folk vil vite *hva de får*, ikke *hva de gjør*.

**Handling:**
- Oppdatert hovedbudskap til variant B
- Lagt til "Spare tid" i Words We Use (BRAND.md)

---

## Hva vi har lært

### Hva fungerer ✅

| Innsikt | Bevis | Implementert? |
|---------|-------|---------------|
| Konkrete tall slår vage løfter | A/B test +45% | ✅ Ja |
| Video-demo > tekst | 3x konvertering | ✅ Ja |
| Tillit > pris som kjøpsdriver | Survey + data | ✅ Ja |
| Konsulenter er beste segment | Segment-analyse | ✅ Justert targeting |

### Hva fungerer ikke ❌

| Innsikt | Bevis | Handling |
|---------|-------|----------|
| "Automatisering" som ord | Lav respons | Byttet til "spare tid" |
| Lange produktbeskrivelser | Høy bounce rate | Kortet ned |
| Generiske stock photos | Lav CTR | Byttet til produkt-screenshots |

### Åpne spørsmål ❓

- [ ] Fungerer budskapet for enterprise-kunder?
- [ ] Hva er optimal pris-kommunikasjon?
- [ ] Hvilke kanaler fungerer for B2B?

---

## Kommende tester

### Planlagt: Q2 2025

**Test 3: Enterprise-segment**
- Hypotese: Driftsledere i mellomstore bedrifter har lignende behov
- Metode: LinkedIn Ads + dedikert landing page
- Suksesskriterier: ≥1.5% konvertering, ≥50 signups

**Test 4: Prisingsside A/B**
- Hypotese: "Betal etter bruk" kommunisert tydelig øker konvertering
- Metode: A/B test på prisingsside
- Suksesskriterier: +20% til betalt plan

---

## Metrikker over tid

### Konverteringsrate (landing page)

```
Jan: ██████░░░░ 2.3%
Feb: ████████░░ 3.3%  ↑ +43%
Mar: ████████░░ 3.1%  ↓ -6%
Apr: █████████░ 3.5%  ↑ +13%
```

### CAC (Customer Acquisition Cost)

```
Jan: 450 kr
Feb: 380 kr  ↓ -16%
Mar: 340 kr  ↓ -11%
Apr: 290 kr  ↓ -15%
```

### NPS (Net Promoter Score)

```
Lansering: 32
+3 mnd: 45  ↑
+6 mnd: 52  ↑
```

---

## Dokumentasjonslogg

| Dato | Hendelse | Ansvarlig |
|------|----------|-----------|
| 2025-01-15 | LEARNINGS.md opprettet | Kenneth |
| 2025-01-28 | Test 1 fullført, BAF validert | Kenneth |
| 2025-02-20 | Test 2 fullført, budskap oppdatert | Kenneth |
| 2025-03-01 | Kvartalsgjennomgang | Team |

---

*Sist oppdatert: 2025-03-01*
*Status: Aktiv*
