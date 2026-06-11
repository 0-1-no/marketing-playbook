# Publishing: 0-1

Use this when publishing to the 0-1 website.

## Repo

- Path: `/Users/kennethdreyer/Code/0-1/0-1-web`
- Blog content: `src/content/blog/<slug>.mdx`
- Blog route: `/blogg/<slug>`
- Public site: `https://0-1.no`

## Frontmatter

0-1 blog posts use MDX frontmatter:

```yaml
---
title: "..."
description: "..."
date: "YYYY-MM-DD"
author: "Kenneth Dreyer"
category: "AI"
tags:
  - AI
  - Strategi
readingTime: "8 min"
image: "/images/blog/<slug>.<ext>"
---
```

`image` is optional. If omitted, the app generates an OG image through `/api/og`.

## Article patterns

- 0-1 writes for Norwegian SMB leaders who want clarity, not hype.
- Use everyday language. Explain technical words when they matter.
- Prefer the StoryBrand pattern in local `marketing/CONTENT-RULES.md`: problem first, then guide, then plan/action.
- Third person "0-1" is the default. Use "jeg" only when the article is explicitly Kenneth's viewpoint.

## Concept explainers

The 0-1 blog currently supports MDX and existing prose callouts. Use this pattern for important concepts:

```mdx
<aside className="prose-callout">
  <strong>Kort forklart:</strong> Programmatisk tilgang betyr at et system kan gjøre handlinger via kode eller API, uten at et menneske klikker rundt manuelt.
</aside>
```

Do not add a tooltip component unless the user asks for a code enhancement. For now, use inline explanations and callouts.

## Images

- Read `marketing/DESIGN-SYSTEM.md` before generating or selecting images.
- Use `image-gen` for article hero/OG image prompts.
- Store final blog images under the repo's existing public image convention, typically `public/images/blog/`.
- Keep alt text concrete and short.

## Verification

Run the repo's relevant checks before publishing:

```bash
npm run type-check
npm run build
```

Run lint if the repo's lint script is known to work. If lint is broken due to toolchain drift, record it and rely on type/build plus the repo's verify/CI.

Use branch -> PR -> green checks -> merge to `main` -> deploy verification when publishing.
