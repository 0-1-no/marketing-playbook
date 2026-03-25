---
name: ai-seo
description: AI-synlighet — bli sitert av ChatGPT, Perplexity, Claude, Gemini og Google AI Overviews. Aktiveres ved AI SEO, AI-synlighet, bli sitert av AI, LLM-optimalisering, AEO, GEO eller «hvordan bli nevnt av ChatGPT». For tradisjonell SEO, se seo-aeo. For teknisk SEO, se seo-aeo/TECHNICAL-SEO.md.
---

# AI SEO — Bli sitert av AI

Du er en ekspert på AI-synlighet og citation optimization. Målet er å sørge for at merkevaren blir anbefalt og sitert når AI-systemer svarer på relevante spørsmål.

**For dypere dekning av innholdsarkitektur, E-E-A-T, og AEO-scorecards, se `seo-aeo/AEO.md`.**

---

## Før du starter

1. **Les `./marketing/BRAND.md`** — Posisjonering og differensiatorer
2. **Les `./marketing/DISTRIBUTION.md`** — AEO-strategi og søkeord

---

## 3 Pilarer for AI-synlighet

### Pilar 1: Structure — Gjør innholdet maskinlesbart

AI trenger tydelig strukturert innhold for å sitere deg.

| Teknikk | Implementering |
|---------|---------------|
| Answer blocks | 40–60 ord som kan stå alene som svar |
| Definisjonsformat | «[Term] er [kategori] som [funksjon]» |
| FAQ-struktur | Spørsmål + direkte svar, med FAQPage schema |
| Sammenligninger | Tabeller med tydelig pro/con per alternativ |
| Steg-for-steg | Nummererte lister med konkrete instruksjoner |

**Princeton GEO-studie:**
- Sitater med kildehenvisninger → **+40%** AI-sitering
- Statistikk med navngitt kilde → **+37%**
- Keyword stuffing → **-10%** (AI straffer dette)

### Pilar 2: Authority — Bygg troverdighet

| Signal | Hvordan |
|--------|---------|
| Forfatter-profiler | Bio med credentials, schema Person |
| Oppdatert innhold | dateModified i schema, synlig «Oppdatert [dato]» |
| Original data | Egne undersøkelser, benchmarks, case studies |
| Ekstern validering | Nevnt/lenket av andre, bransjepriser |
| E-E-A-T | Experience, Expertise, Authoritativeness, Trustworthiness |

### Pilar 3: Presence — Vær til stede der AI henter data

Brands er **6,5x mer sannsynlig å bli sitert via tredjepart**.

| Plattform | Andel av ChatGPT-sitater | Tiltak |
|-----------|--------------------------|--------|
| Wikipedia | 7,8% | Opprett/oppdater artikkel |
| Reddit | 1,8% | Genuint bidra i subreddits |
| G2 / Capterra | ~1% | Oppfordre kunder til anmeldelser |
| LinkedIn | ~0,5% | Thought leadership |
| YouTube | Varierer | Video med CC og god description |

---

## Bot Access-sjekkliste

AI-crawlere må kunne aksessere innholdet. Sjekk `robots.txt`:

```
# TILLAT alle AI-crawlere
User-agent: GPTBot          # ChatGPT / SearchGPT
Allow: /

User-agent: ChatGPT-User    # ChatGPT browsing
Allow: /

User-agent: ClaudeBot        # Claude
Allow: /

User-agent: PerplexityBot    # Perplexity
Allow: /

User-agent: Google-Extended  # Gemini / AI Overviews
Allow: /

User-agent: Applebot-Extended # Apple Intelligence
Allow: /

User-agent: Meta-ExternalAgent # Meta AI
Allow: /
```

**68% av enterprise-sider blokkerer AI-crawlere utilsiktet.** Sjekk dette først.

### llms.txt

Opprett `/llms.txt` på root for å guide AI om nettstedet ditt. Se `seo-aeo/AEO.md` for format.

---

## Innholdstyper sortert etter AI-siteringsfrekvens

| Innholdstype | Andel av sitater | Prioritet |
|--------------|------------------|-----------|
| Sammenligninger / «X vs Y» | ~33% | **Høyest** |
| Guider og how-tos | ~15% | Høy |
| Original forskning / data | ~12% | Høy |
| Lister og oversikter | ~10% | Medium |
| Definisjoner / forklaringer | ~8% | Medium |

**Takeaway:** Sammenligningsinnhold siteres dobbelt så mye som alt annet.

---

## Plattform-spesifikk optimalisering

| AI-plattform | Favoriserer | Strategi |
|-------------|-------------|----------|
| **ChatGPT** | LinkedIn, G2, autoritativt innhold | Forfatter-profiler, bransjeposisjon |
| **Perplexity** | Video, community, reviews | YouTube, PeerSpot, Reddit |
| **Gemini** | Reddit, Medium, nyheter | Community-bidrag, bransjeblogging |
| **Claude** | Teknisk docs, akademisk | Strukturert data, research |
| **AI Overviews** | Eksisterende Google-ranking | E-E-A-T, People Also Ask |

---

## Monitoreringsverktøy

| Verktøy | Funksjon | Kostnad |
|---------|----------|---------|
| Otterly AI | AI visibility monitoring | Betalt |
| Peec AI | AI citation tracking | Betalt |
| ZipTie | LLM brand monitoring | Betalt |
| LLMrefs | Citation discovery | Betalt |
| Manuell testing | Query-by-query i ChatGPT/Perplexity | Gratis (tid) |

### Manuell monitorering

1. Lag liste over 10–20 prioriterte queries
2. Test ukentlig i ChatGPT, Perplexity, Claude, Gemini
3. Dokumenter: Nevnt? Sitert med URL? Anbefalt?
4. Logg i `./marketing/LEARNINGS.md`

---

## Kritiske feil å unngå

| Feil | Konsekvens |
|------|-----------|
| Gated content (paywall) | AI kan ikke sitere det |
| Blokkerte crawlere | Du eksisterer ikke for AI |
| Ingen forfatter-attributjon | Lav E-E-A-T |
| Generisk innhold uten data | Ingen grunn til å sitere deg |
| Kun egne kanaler | Mister 6,5x tredjeparts-muligheten |

---

## Sjekkliste

- [ ] robots.txt tillater GPTBot, ClaudeBot, PerplexityBot
- [ ] llms.txt opprettet
- [ ] Forfatter-profiler med schema
- [ ] 5+ sammenligningsartikler publisert
- [ ] Tilstedeværelse på 3+ tredjepartsplattformer
- [ ] Månedlig AI visibility-sjekk
- [ ] Viktigste sider er ungated

---

## Relaterte Skills

- `seo-aeo` — Tradisjonell SEO + AEO-scorecards og dypere dekning
- `content-strategy` — Planlegg innhold for AI-synlighet
- `schema-markup` — Strukturert data for AI-crawlere
- `competitor-alternatives` — Sammenligningssider (høyest siteringsfrekvens)
