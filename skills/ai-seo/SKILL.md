---
name: ai-seo
description: AI-synlighet og GEO (Generative Engine Optimization) — bli sitert av ChatGPT, Perplexity, Claude, Gemini og Google AI Overviews. Aktiveres ved AI SEO, AI-synlighet, bli sitert av AI, LLM-optimalisering, GEO, citability, E-E-A-T-scoring, brand mentions som AI-signal, eller «hvordan bli nevnt av ChatGPT». For AEO-fundament og tradisjonell SEO, se seo-aeo. For teknisk SEO og llms.txt-spec, se seo-aeo/TECHNICAL-SEO.md.
---

# AI SEO — Bli sitert av AI

Du er en ekspert på AI-synlighet og citation optimization. Målet er å sørge for at merkevaren blir anbefalt og sitert når AI-systemer svarer på relevante spørsmål.

**For dypere dekning av innholdsarkitektur, E-E-A-T-grunnlag, og AEO-scorecards, se `seo-aeo/AEO.md`.**
**For operative scoringsrubrikker (citability + E-E-A-T 4×25), se [references/GEO-RUBRICS.md](references/GEO-RUBRICS.md).**

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

**Score autoriteten din:** Bruk E-E-A-T-rubrikken (4×25 poeng) i [references/GEO-RUBRICS.md](references/GEO-RUBRICS.md) for å finne det svakeste benet og fikse det. AI vekter den svakeste lenken hardt — én manglende kontaktinfo eller gammel dato kan velte en ellers sterk side. Merk: Googles Quality Rater Guidelines anvender nå E-E-A-T bredt på alt innhold, ikke bare YMYL (helse/finans/jus).

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

## Citability — skriv passasjer AI faktisk siterer

AI siterer ikke en side, den siterer en **passasje** — en avgrenset bit tekst den kan løfte rett inn i svaret sitt. Pilar 1 over (40–60-ords answer blocks) dekker korte, faktuelle svar. For lengre «hvordan/hvorfor/hvilken»-spørsmål trenger du **selvstendige passasjer på ~130–170 ord**: svaret først, så støtte, kompakt nok til å siteres helt, men fyldig nok til å stå alene.

Fire egenskaper avgjør om en passasje blir sitert:

| Egenskap | Spørsmål du stiller passasjen |
|----------|-------------------------------|
| **Selvstendig** | Gir den mening klippet ut alene, uten «som nevnt over»? |
| **Fakta-tett** | Minst ett konkret tall, dato, navn eller eksempel? |
| **Unik** | Sier den noe egen data/innsikt gir som konkurrenter ikke har? |
| **Svar-først** | Står konklusjonen i *første* setning (AI klipper ofte bare de første)? |

4/4 = sitérbar. Skriv hver passasje mot **ett konkret spørsmål** en bruker ville stilt en AI, ikke mot et søkeord — én side kan ha mange slike passasjer, én per spørsmål du vil eie.

**For full rubrikk med eksempler og lengde-begrunnelse, se [references/GEO-RUBRICS.md](references/GEO-RUBRICS.md).**

---

## Brand mentions — det sterkeste siterings-signalet nå

Usitert **merkenevnelse** (brand mention uten lenke) er nå et sterkere AI-siterings-signal enn backlinks. Ahrefs-data fra sent 2025 indikerer at omtaler korrelerer **~3× sterkere** med AI-synlighet enn tradisjonelle backlinks gjør. Logikken: AI-modeller bygger forståelse av *entiteter* — hvor ofte og i hvilken kontekst et merke nevnes på tvers av nettet — ikke bare hvem som lenker til hvem.

**Hvorfor dette snur SEO-prioritering:** I link-økonomien jaget du backlinks. I siterings-økonomien jager du **tilstedeværelse der målgruppen og AI-modellene henter fra** — selv uten en eneste lenke tilbake til deg.

| Kilde | Hvorfor den teller for AI |
|-------|---------------------------|
| **Reddit** | Tungt vektet treningsdata + live-henting; genuine tråder i relevante subreddits |
| **YouTube** | Transkripsjoner indekseres; bli nevnt i videoer + egne videoer med god description/CC |
| **Wikipedia** | Høyeste enkelt-andel av ChatGPT-sitater; verifiserbar entitet |
| **LinkedIn** | Thought leadership; bli omtalt som ekspert i ditt felt |
| **Fagfora / nisje-communities** | Ekspertomtale der din målgruppe faktisk diskuterer |

**Konkret tiltak:** Bygg en omtale-strategi, ikke bare en lenke-strategi. Dette er distribusjon, ikke teknisk SEO — koble til `social-content` (organisk tilstedeværelse), `community-marketing` (Reddit/fora), og `public-relations` (omtale i presse og bransjemedier).

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

`/llms.txt` på root er en kuratert markdown-meny som peker AI mot sidene du faktisk vil bli sitert fra — en snarvei forbi støy og treg HTML-parsing. **Siterings-vinkelen:** prioriter dine mest sitérbare sider øverst (sammenligninger, original data, definisjoner) med en presis én-linjes beskrivelse per lenke, så modellen forstår *hva hver side svarer på* uten å crawle den. Dette er ikke et rangeringssignal — det er kuratering: du forteller modellen hvor svarene ligger.

**For format og full struktur-spec, se `seo-aeo/TECHNICAL-SEO.md`** (ikke duplisert her).

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
- [ ] llms.txt opprettet (format: `seo-aeo/TECHNICAL-SEO.md`)
- [ ] Forfatter-profiler med schema
- [ ] Nøkkelsider scorer 4/4 på citability-sjekken (selvstendig, fakta-tett, unik, svar-først)
- [ ] E-E-A-T-score ≥80/100 på nøkkelsider — svakeste ben adressert
- [ ] 5+ sammenligningsartikler publisert
- [ ] Brand mentions-strategi (Reddit/YouTube/fora), ikke bare lenker
- [ ] Tilstedeværelse på 3+ tredjepartsplattformer
- [ ] Månedlig AI visibility-sjekk
- [ ] Viktigste sider er ungated

---

## Relaterte Skills

- `seo-aeo` — AEO-fundament og E-E-A-T-basis (answer blocks, FAQ-struktur, scorecards); denne skillen spisser citation-taktikken oppå
- `content-strategy` — Planlegg innhold for AI-synlighet
- `schema-markup` — Strukturert data for AI-crawlere
- `competitor-alternatives` — Sammenligningssider (høyest siteringsfrekvens)
- `social-content` · `community-marketing` · `public-relations` — Bygg brand mentions der AI henter fra
