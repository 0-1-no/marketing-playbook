---
name: blog-writing
description: Reusable workflow for researching, writing, optimizing, publishing, and verifying high-quality Norwegian blog articles for owned company blogs such as 0-1.no and Companybook. Use for blog posts, editorial articles, news comments, thought leadership, SEO/AEO blog work, and autonomous blog publishing pipelines.
---

# Blog Writing

Use this skill when the user asks for a blog post or article for an owned brand. The job is not just drafting text: research the topic, write a useful article, optimize it for readers/search/AI answers, create an image plan, publish through the target repo, and verify the result.

## Core workflow

1. Read the local marketing files in the target repo:
   - `marketing/BRAND.md`
   - `marketing/CONTENT-RULES.md`
   - `marketing/JOURNEY.md`
   - `marketing/DISTRIBUTION.md`
   - `marketing/DESIGN-SYSTEM.md` when images or visual assets are needed
2. Load the relevant references:
   - `references/editorial-workflow.md` for the end-to-end article process.
   - `references/seo-aeo-reviewer.md` before writing any blog article.
   - `references/norwegian-humanizer.md` before the final edit pass.
   - `references/concept-explainers.md` when the article uses technical concepts or jargon.
   - `references/publishing-0-1.md` when publishing to 0-1.
   - `references/publishing-companybook.md` when publishing to Companybook.
3. Spawn an SEO/AEO reviewer subagent before outline or drafting. Treat a blog-writing request as permission to delegate that specific SEO/AEO brief.
4. Draft for the reader first, then optimize. Do not let SEO turn the article generic.
5. Use `image-gen` for article/OG image planning or generation; do not invent image standards in this skill.
6. Publish and verify through the target repo's normal pipeline.

## Autonomy

For owned company blogs, a user request to write/publish a blog post is standing approval to:

- create a branch, commit, push, open a PR, merge to `main`, and complete the deploy/verify pipeline;
- update article files, images, metadata, and small supporting assets required for the post;
- run formatters, type checks, builds, and repo-specific ship/watch commands.

Do not ask for extra permission for routine blog pipeline steps.

Still require explicit approval before:

- sending email, publishing social posts, or contacting anyone on Kenneth's behalf;
- changing foundational brand files such as `BRAND.md`;
- deleting data/files, rotating secrets, spending money, or making broad architecture changes;
- publishing sensitive legal, medical, financial, or personal claims that cannot be verified.

## Writing standard

- Primary language is Norwegian unless the target brand says otherwise.
- Write for a busy business reader. Explain the practical consequence before the technical detail.
- Avoid buzzwords unless the article explains them in plain language.
- Benchmarks are background context, not the story, unless they directly explain business value.
- Every article must include:
  - a clear reader promise early;
  - one short answer block suitable for AEO;
  - concrete examples or scenarios;
  - a "what this means for your company" section or equivalent;
  - FAQ/questions when useful;
  - internal links and a clear CTA;
  - an image/OG plan via `image-gen`.

## Quality gate

Before publishing, the article must pass three checks:

1. **Concept clarity**: important jargon is explained through inline wording, callouts, or target-supported tooltips.
2. **Business value**: the article connects the topic to time, cost, risk, quality, customer experience, or new workflows.
3. **Distribution pack**: include SEO title, meta description, AEO questions, internal link suggestions, image prompt, and 2-3 social teaser drafts in the PR/context notes. Do not auto-publish social posts.
