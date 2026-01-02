# Marketing Playbook

> ABC framework for consistent brand communication in Claude Code.

Marketing Playbook helps you maintain consistent brand voice across all your marketing content by creating and enforcing `BRAND.md` files in your projects.

## Installation

```bash
claude plugin install 0-1-no/marketing-playbook
```

## The ABC Framework

Marketing Playbook is built around three core pillars:

### A - Audience
- **Who** are you talking to?
- What are their **pain points**?
- What are their **goals**?

### B - Brand
- What's your **positioning**?
- What are your **values**?
- What makes you **different**?

### C - Communication
- What's your **tone of voice**?
- Which **words do you use**?
- Which **words do you avoid**?

## Commands

| Command | Description |
|---------|-------------|
| `/marketing-playbook` | Show status and version |
| `/marketing-playbook:init` | Create BRAND.md interactively |
| `/marketing-playbook:check` | Verify content against BRAND.md |
| `/marketing-playbook:audit` | Full project audit |

## BRAND.md Structure

When you run `/marketing-playbook:init`, a `BRAND.md` file is created with this structure:

```markdown
# [Project Name] Brand

## Audience
**Primary:** [Who is your main target audience?]
**Secondary:** [Other audiences]

### Pain Points
- [Problems you solve]

### Goals
- [What they want to achieve]

## Brand
**Positioning:** [One sentence description]
**Values:** [Core values]
**Differentiators:** [What makes you unique]

## Communication
**Tone of Voice:** [Adjectives describing your voice]
**Words We Use:** [Preferred terminology]
**Words We Avoid:** [Words to skip]
```

## Usage Examples

### Check content before publishing
```
/marketing-playbook:check

# Paste your landing page copy, email, or ad text
# Get ABC score and specific improvements
```

### Audit your entire project
```
/marketing-playbook:audit

# Scans landing pages, translations, meta tags
# Returns comprehensive brand alignment report
```

## Auto-trigger Skill

The plugin includes a skill that automatically activates when you're working on marketing content. It reminds you to:
- Read BRAND.md before writing
- Follow ABC checklist
- Use correct words and tone

## Premium Version

For advanced marketing capabilities, visit [marketing.no](https://marketing.no):
- Extended copywriting frameworks (AIDA, PAS, etc.)
- SEO content optimization
- Competitor analysis tools
- Campaign planning agents

## License

MIT

## Author

[0-1.no](https://0-1.no) - AI consultancy for Norwegian businesses
