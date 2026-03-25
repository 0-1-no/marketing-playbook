# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Marketing Playbook is a **Claude Code plugin** that provides marketing frameworks and methodology. It has a two-layer architecture:

1. **Global Plugin** (this repo): Contains methodology, principles, checklists, and skills - NO concrete values
2. **Per-Repo `./marketing/` folder**: Created in each project using the plugin, contains actual brand values

## Repository Structure

```
.claude-plugin/               # Plugin metadata (plugin.json, marketplace.json)
commands/                     # Slash commands (/marketing-playbook:init, etc.)
skills/                       # Auto-activated contextual skills (dir/SKILL.md format)
  ├── marketing-playbook/     # Main skill — reference content (user-invocable: false)
  ├── marketing-psychology/   # 50+ psykologiske prinsipper (user-invocable: false)
  ├── brand-principles/       # 7 brand-prinsipper (user-invocable: false)
  ├── customer-principles/    # Lojalitet, retention (user-invocable: false)
  ├── distribution-principles/ # SOV→SOM, 60:40 (user-invocable: false)
  ├── marketing-mindset/      # 20 strategiske prinsipper (user-invocable: false)
  ├── design-system/          # UI/UX methodology (8 sub-files)
  ├── seo-aeo/                # SEO & AEO methodology (8 sub-files)
  ├── storytelling-copywriting/  # Copy frameworks (7 sub-files)
  ├── content-writing/        # Content methodology (7 sub-files)
  ├── image-gen/              # AI image generation (5 sub-files + scripts/)
  │   └── scripts/generate_image.py  # Gemini API (uv run)
  └── [30+ more skill dirs]/  # CRO, strategy, B2B, etc.
scripts/                      # Git hooks og utility scripts (ikke skill-relatert)
examples/                     # Example outputs (BRAND.md, JOURNEY.md, etc.)
```

## Key Architectural Concept

**Skills contain methodology, not values.** When a skill says "consider fonts like Clash Display", it's suggesting an approach. The actual font choice lives in `./marketing/DESIGN-SYSTEM.md` in the target project.

This separation enables:
- One global plugin with reusable frameworks
- Project-specific customization via `./marketing/` files
- Skills that guide decisions without hardcoding values

## Commands

| Command | Purpose |
|---------|---------|
| `/marketing-playbook` | Show status and version |
| `/marketing-playbook:init` | Create BRAND.md, JOURNEY.md, DISTRIBUTION.md, LEARNINGS.md |
| `/marketing-playbook:check` | Verify content against marketing/ files |
| `/marketing-playbook:audit` | Full project audit with Brand Health scoring |
| `/design-system:init` | Create DESIGN-SYSTEM.md through iterative demos |
| `/seo-aeo:audit` | SEO and AEO audit with scorecard |
| `/content-writer:init` | Create CONTENT-RULES.md with voice rules |

## Skills System

Skills auto-activate based on task context:

| Skill | Activates When |
|-------|---------------|
| `marketing-playbook` | Any marketing content work |
| `design-system` | UI/UX, styling, CSS, Tailwind, landing pages |
| `seo-aeo` | SEO work, meta tags, structured data |
| `storytelling-copywriting` | Copy, headlines, CTAs |
| `content-writing` | Articles, guides, website pages |
| `image-gen` | Image generation, OG images, social graphics, marketing assets |

Skills have progressive loading: main SKILL.md provides decision tree, sub-files loaded on demand.

## ABC Framework

Core framework used throughout:

- **A**udience: Who are we talking to?
- **B**rand: What do we offer and why?
- **C**ommunication: How do we say it?

## Files the Plugin Creates (in target projects)

| File | Content |
|------|---------|
| `marketing/BRAND.md` | ABC framework values |
| `marketing/JOURNEY.md` | Customer journey mapping (ToFU→Loyalty) |
| `marketing/DISTRIBUTION.md` | Channels, stack, SEO strategy |
| `marketing/LEARNINGS.md` | Test results, Brand Audience Fit validation |
| `marketing/DESIGN-SYSTEM.md` | Colors, fonts, components |
| `marketing/CONTENT-RULES.md` | Voice dimensions, structure rules |

## Testing Changes

Install plugin locally and test commands:
```bash
# Test in a project that uses the plugin
/marketing-playbook
/marketing-playbook:check
```

## Language

- **Norwegian** for user-facing content (commands, skill descriptions, example outputs)
- **English** for technical/code comments
