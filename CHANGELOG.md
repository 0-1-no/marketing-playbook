# Changelog

All notable changes to Marketing Playbook will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
