# Publishing: Companybook

Use this when publishing to the Companybook blog.

## Repo

- Path: `/Users/kennethdreyer/Code/Companybook`
- Blog content: `content/blog/<slug>.mdx`
- Blog route: `/no/blogg/<slug>`

## Frontmatter

Companybook posts use MDX files with frontmatter mapped into the blog system:

```yaml
---
title: "..."
description: "..."
date: "YYYY-MM-DD"
author: "kenneth"
coverImage: "/blog/<slug>.webp"
coverImageAlt: "..."
tags:
  - AI
  - Norske selskaper
draft: false
---
```

Authors are keyed in `src/lib/blog/types.ts`. Use `kenneth` for Kenneth-authored posts and `companybook` for redaksjonen.

## Article patterns

- Companybook readers are more AI-literate than 0-1 readers.
- Still explain technical terms when they are not essential to the reader's job.
- Show concrete questions a user can ask ChatGPT/Claude with Companybook data.
- Every factual business-data claim should be sourceable.
- Avoid hero-level jargon such as MCP, protocol, tool calling, and integration unless the article is specifically technical.

## Concept explainers

The Companybook blog renderer is more markdown-oriented. Do not assume arbitrary MDX components or tooltip components work in posts.

Use:

- short inline definitions;
- blockquotes for important caveats;
- simple callout-style sections using headings and paragraphs.

If a true tooltip is needed, treat it as a separate code task.

## Images

- Read `marketing/DESIGN-SYSTEM.md` and any illustration-style reference in the repo.
- Use `image-gen` for OG/cover image prompts.
- Store final cover images under the repo's existing public blog convention, typically `/public/blog/<slug>.webp`.
- Include `coverImageAlt`.

## Verification

Use the repo's scripts and existing CI expectations. Typical checks are:

```bash
pnpm typecheck
pnpm lint
pnpm build
```

If a script name differs, inspect `package.json` and use the repo's actual command.

Use branch -> PR -> green checks -> merge to `main` -> deploy verification when publishing.
