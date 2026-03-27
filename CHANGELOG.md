# Changelog

All notable changes to Marketing Playbook will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.2] - 2026-03-27

### Fixed — Skill routing and discoverability

- **Command names**: CLAUDE.md dokumenterte feil command-format (`/design-system:init`). Claude Code bruker `plugin-name:command-filename`, altså `/marketing-playbook:design-system-init`. Alle 10 kommandoer korrekt dokumentert.
- **Removed `disable-model-invocation: true`** fra 6 init-commands (brand-init, marketing-playbook-init, design-system-init, content-writer-init, journey-init, distribution-init). Init-kommandoer oppretter filer og er ikke destruktive — per Claude Code docs bør flagget kun brukes for irreversible operasjoner. Agenter kan nå kalle init-commands programmatisk via Skill tool.
- **Version synlig i CLAUDE.md** — versjon vises nå øverst i filen for raskere agent-oppdagelse.

---

## [0.6.1] - 2026-03-25

### Fixed — Skill structure compliance

6 standalone `.md`-filer i `skills/` fulgte ikke Claude Code sin `dir/SKILL.md`-oppdagelse og ble aldri lastet:

- `marketing-playbook.md` → `marketing-playbook/SKILL.md`
- `marketing-psychology.md` → `marketing-psychology/SKILL.md`
- `brand-principles.md` → `brand-principles/SKILL.md`
- `customer-principles.md` → `customer-principles/SKILL.md`
- `distribution-principles.md` → `distribution-principles/SKILL.md`
- `marketing-mindset.md` → `marketing-mindset/SKILL.md`

### Changed

- Alle 6 referanse-skills markert `user-invocable: false` (bakgrunnsreferanse, ikke manuelt invokable)
- 6 init-commands markert `disable-model-invocation: true` (brand-init, marketing-playbook-init, design-system-init, content-writer-init, journey-init, distribution-init) — forhindrer at Claude trigger dem automatisk
- CLAUDE.md oppdatert med korrekt `dir/SKILL.md`-struktur

### Technical
- Version bump til 0.6.1

---

## [0.6.0] - 2026-03-25

### Added — 9 nye skills

**Content & SEO (Tier 1.5)**
- `content-strategy` — Innholdsstrategi med pillar/cluster-arkitektur, searchable vs shareable rammeverk, 4-faktor topic scoring
- `ai-seo` — Dedikert AI-siteringsoptimalisering for ChatGPT, Perplexity, Claude, Gemini. 3-pilar rammeverk (Structure, Authority, Presence), bot-blocking sjekkliste, citation-share data
- `site-architecture` — Nettstedsarkitektur med 3-click rule, 6 navigasjonstyper, 12 URL-mønstre, hub-and-spoke intern lenking, Mermaid sitemap output
- `schema-markup` — JSON-LD strukturert data med 10+ schema-typer, CMS-spesifikke patterns (Next.js, Nuxt, SvelteKit), valideringspipeline
- `free-tool-strategy` — Engineering as marketing med 6 verktøytyper, 8-faktor scorecard (25+ = go), MVP scope-sjekkliste, norske eksempler
- `lead-magnets` — 13 lead magnet-formater med stage-matching, gating-matrise, konverteringsbenchmarks

**B2B Salg (Tier 4)**
- `revops` — Revenue operations med dual-criteria MQL-modell, 4t/48t speed-to-lead SLA, 8-metrikk dashboard, pipeline hygiene, marketing→sales handoff
- `cold-email` — B2B cold outreach med 4 formler, 3-tier voice, angle rotation, breakup email, deliverability-sjekkliste (SPF/DKIM/DMARC), norsk juridisk kontekst
- `sales-enablement` — 11-slide pitch deck arc, 6 innvendingskategorier med svar-templates, persona value prop matrix, battle cards, demo-script rammeverk

### Changed — Eksisterende skills oppdatert

- **pricing-strategy** — Ny seksjon «Prisingsresearch-metoder» med Van Westendorp Price Sensitivity Meter (4-spørsmåls metode), MaxDiff-analyse for feature-prioritering, og konkrete prisøkningstriggers (>40% konvertering, <3% churn)
- **churn-prevention** — Nye nøkkel-benchmarks (soft decline recovery 50-60%, hard decline 20-30%, pause-reaktivering 60-80%) og rabatt sweet spot-analyse (20-30% i 2-3 mnd er optimalt, høyere trener avbestillingsadferd)
- **seo-aeo/AEO.md** — Ny Pilar 5: Tredjeparts tilstedeværelse (brands 6,5x mer sannsynlig å bli sitert via tredjepart). Princeton GEO-studie (+40% sitater, +37% statistikk, -10% keyword stuffing). Innholdstyper sortert etter siteringsfrekvens (sammenligninger ~33%). Nye verktøy: Otterly AI, Peec AI, ZipTie, LLMrefs
- **marketing-playbook.md** — Oppdatert Relaterte Skills-tabell med alle 9 nye skills og ny B2B Salg-kategori

### Technical
- Version bump til 0.6.0

---

## [0.5.1] - 2026-02-21

### Added
- **ATIDCOA-rammeverket** i storytelling-copywriting/FRAMEWORKS.md — 7-stegs landing page-modell som utvider klassisk AIDA med Transformation, Compare og Objections
  - Komplett strukturbeskrivelse med alle steg
  - AIDA vs. ATIDCOA sammenligningstabell
  - Vanlige feil
  - Bransjespesifikke tilpasninger (B2B/SaaS + E-commerce/DTC)
  - Kilde-attribusjon til Oliver Kenyon

### Changed
- storytelling-copywriting/SKILL.md — ATIDCOA lagt til i description, arkitektur-boks, ressurstabell, framework quick reference og landing page-seksjon
- page-cro/SKILL.md — ATIDCOA-referanse under landingsside-rammeverket
- competitor-alternatives/SKILL.md — Kryss-referanse til ATIDCOA Compare-steget
- Beslutningsmatrisen i FRAMEWORKS.md oppdatert: AIDA → kort format, ATIDCOA → landing pages
- Kombinasjoner-seksjonen utvidet med ATIDCOA + FAB og PAS → ATIDCOA

### Technical
- Version bump til 0.5.1

## [0.5.0] - 2026-02-20

### Added — 19 nye skills

**Tier 1 — Kjerneverdier (7 stk)**
- `page-cro` — Konverteringsoptimalisering for nettsider (7-stegs analyse, sidespesifikke rammeverk)
- `programmatic-seo` — Skalerbar SEO med templates og data (10 playbooks, norske datakilder)
- `social-content` — LinkedIn, X, Instagram, Facebook innholdsstrategi (hooks, repurposing)
- `email-sequence` — E-postsekvenser og automatisering (velkomst, nurture, re-engasjering, onboarding)
- `analytics-tracking` — Generell tracking-metodikk (PostHog + GA4 som referanser)
- `paid-ads` — Kampanjestrategi for Google, Meta, LinkedIn, Finn.no
- `ad-creative` — Annonseinnhold, bulk-generering, iterasjon fra performance data

**Tier 2 — CRO-pakke (6 stk)**
- `signup-flow-cro` — Registreringsflyt-optimalisering (felt-for-felt, friksjonskart)
- `onboarding-cro` — Post-signup aktivering (aha-øyeblikk, progressiv onboarding)
- `form-cro` — Skjema-optimalisering for leads, kontakt, demo, checkout
- `popup-cro` — Modals, overlays, slide-ins (triggere, frekvensregler)
- `paywall-upgrade-cro` — In-app paywalls og upgrade moments
- `churn-prevention` — Cancel flows, save offers, dunning, proaktiv retensjon

**Tier 3 — Strategi (6 stk)**
- `launch-strategy` — Produktlanseringer med ORB-rammeverk (Owned/Rented/Borrowed)
- `competitor-alternatives` — Konkurrent-sammenligningssider for SEO og salg
- `ab-test-setup` — A/B-testing med hypotese-rammeverk og PIE-prioritering
- `pricing-strategy` — Prisstrategi, packaging, value metrics (NOK/MVA)
- `referral-program` — Referral og affiliate tilpasset norsk marked
- `marketing-ideas` — Idébank etter kategori, filtrert etter modenhet og ressurser

### Changed — 5 berikede skills

- `content-writing` — Lagt til searchable vs shareable, content pillars, idékilder, prioritering
- `storytelling-copywriting` — Lagt til CRO sidestruktur, CTA-retningslinjer, sidetype-veiledning
- `seo-aeo` — Lagt til audit-prioritering (5-stegs hierarki), oppdatert relaterte skills
- `marketing-psychology` — Lagt til strategiske tenkningsmodeller, prispsykologi, design/delivery-modeller, vekstmodeller, quick reference-tabell
- `marketing-playbook` — Lagt til switching dynamics, anti-persona, komplett skills-katalog (30 skills)

### Technical
- Version bump til 0.5.0
- Oppdatert plugin.json og marketplace.json descriptions
- Utvidet keywords med CRO, konvertering, e-post, sosiale-medier, annonser, prising, lansering

## [0.4.1] - 2026-01-13

### Changed
- Flyttet `generate_image.py` til `skills/image-gen/scripts/` (følger Claude Code skill best practice)
- Scripts tilhørende en skill skal ligge inne i skill-mappen, ikke på plugin rot-nivå

### Fixed
- Script ikke funnet når skill kjøres fra plugin-cache (feil working directory)

## [0.4.0] - 2026-01-12

### Added
- AI-bildegenerering med Gemini API (Nano Banana Pro)
- Ny skill: `image-gen` for marketing-bilder
  - SKILL.md - Hovedskill med beslutningstre
  - PROMPT-GUIDE.md - Prompting best practices
  - OG-IMAGES.md - OpenGraph templates
  - SOCIAL-GRAPHICS.md - Social media templates
  - MARKETING-ASSETS.md - Bannere og artikkelbilder
- Python script: `scripts/generate_image.py` med uv-støtte
  - Marketing presets: og, twitter, instagram, story, linkedin, banner, etc.
  - Støtte for 1K/2K/4K oppløsning
  - Image editing med --input flag
- `.gitignore` for å beskytte API-nøkler og secrets

### Changed
- Plugin description oppdatert til å inkludere bildegenerering
- Keywords utvidet med "image-gen" og "gemini"

### Technical
- Bruker `gemini-3-pro-image-preview` (Nano Banana Pro) som default modell
- PEP 723 inline dependencies (ingen separat requirements.txt)
- Krever `GEMINI_API_KEY` miljøvariabel

## [0.3.0] - 2026-01-05

### Added
- Dark mode CSS variables i DESIGN-SYSTEM.md template (light + dark default)
- Dark Mode Strategy seksjon i template med mapping-tabell og toggle-implementasjon
- DECISIONS.md beslutningslogg i showcase-struktur (kortfattet format)
- Component Gallery side (`/gallery`) med alle komponenter i light/dark mode
- Showcase som permanent visuell referanse under `marketing/design-showcase/`
- Dark mode toggle-krav i demo builds med next-themes
- Lenker mellom DESIGN-SYSTEM.md og showcase
- Visual Reference seksjon i template

### Changed
- design-system-init krever nå light + dark mode fra Steg 5
- Showcase opprettes under `marketing/` (samlet med andre marketing-filer)
- Iterasjonsfeedback inkluderer dark mode check
- Steg 8 ekstraksjon bruker strukturert beslutningslogg
- Gallery genereres automatisk ved sign-off

### Fixed
- Dark mode mistes ikke lenger under iterasjoner
- Visuelle beslutninger bevares i DECISIONS.md
- Showcase integrert som pågående referanse (ikke kastet etter godkjenning)

## [0.2.0] - 2026-01-04

### Added
- Separate init-kommandoer: `brand-init`, `journey-init`, `distribution-init`
- Design-system showcase versjonering (v1/v2/v3 i stedet for option-1/2/3)
- Content-writer showcase-app alternativ
- "Neste steg"-seksjon i alle init-kommandoer
- Tidlig-fase deteksjon i marketing-playbook-audit
- Maturity-phase håndtering (tidlig vs etablert fase)

### Changed
- `marketing-playbook:init` bruker nå checkpoint-basert fil-generering
- LEARNINGS.md opprettes som tom template (ingen egen intervju)
- Audit gir mildere tilbakemelding for tidlig-fase prosjekter
- Design-showcase bevarer alle iterasjoner for progresjonsvisning

### Fixed
- Init fullførte bare BRAND.md - nå opprettes alle filer via checkpoints etter hver seksjon

## [0.1.0] - 2026-01-02

### Added
- Initial release
- ABC-rammeverk (Audience, Brand, Communication)
- Kommandoer:
  - `marketing-playbook:init` - Opprett marketing/-filer
  - `marketing-playbook:check` - Verifiser innhold
  - `marketing-playbook:audit` - Full prosjekt-audit
  - `design-system:init` - Opprett DESIGN-SYSTEM.md
  - `content-writer:init` - Opprett CONTENT-RULES.md
  - `seo-aeo:audit` - SEO og AEO audit
- Skills:
  - marketing-playbook - Hovedskill for merkevare-arbeid
  - design-system - UI/UX metodikk
  - seo-aeo - Søkemotor og AI-optimalisering
  - storytelling-copywriting - Tekstforfatter-rammeverk
  - content-writing - Innholdsproduksjon
  - marketing-mindset - 20 strategiske prinsipper
  - marketing-psychology - 35+ psykologiske prinsipper
  - brand-principles - 7 merkevare-prinsipper
  - distribution-principles - 14 distribusjons-prinsipper
  - customer-principles - Kundelojalitet og community
- Eksempelfiler: BRAND.md, JOURNEY.md, DISTRIBUTION.md, LEARNINGS.md
