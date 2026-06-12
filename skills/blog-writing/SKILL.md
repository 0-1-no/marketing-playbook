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
   - `references/format-design.md` before outlining any article that should be engaging, visual, or distinctive.
   - `references/seo-aeo-reviewer.md` before writing any blog article.
   - `references/norwegian-humanizer.md` before the final edit pass.
   - `references/concept-explainers.md` when the article uses technical concepts or jargon.
   - `references/publishing-0-1.md` when publishing to 0-1.
   - `references/publishing-companybook.md` when publishing to Companybook.
3. Spawn an SEO/AEO reviewer subagent before outline or drafting. Treat a blog-writing request as permission to delegate that specific SEO/AEO brief.
4. Create a format brief before drafting. Decide whether this should be an essay, briefing, magazine feature, field guide, comparison, case-led piece, interactive explainer, or another shape. Do not default to a plain article.
5. Draft for the reader first, then optimize. Do not let SEO turn the article generic.
6. Use `image-gen` for article/OG image planning or generation; do not invent image standards in this skill.
7. Publish and verify through the target repo's normal pipeline.

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
  - a format/visual plan that makes the article easy to skim and worth reading;
  - a "what this means for your company" section or equivalent;
  - FAQ/questions when useful;
  - internal links and a clear CTA;
  - an image/OG plan via `image-gen`.

## Editorial standard

- Speak to the reader, not about the reader. Avoid lazy audience labels such as "norske ledere" unless the geography or role is the point.
- Use a Morning Brew/TLDR-style rhythm when the audience is busy: what happened, why it matters, what to do next, what to watch.
- Every substantive section must have a claim, a concrete example, and a practical implication. If a section cannot pass that test, cut or redesign it.
- No generic noun-list may stand alone. A list like "CRM, documents, email, support" must become a table, scenario, decision tree, graphic, checklist, or case box that adds meaning.
- If the article discusses cost, time, risk, or value, include at least one simple calculation or operational example.
- Do not overstate a feature. If a capability is not unique, say what is actually different. Example: 1M context is not a story by itself if other current models also have 1M context.
- Treat visuals as part of the article, not decoration. Use generated images, diagrams, embedded videos, screenshots, tables, or interactive modules when they make the point faster than prose.
- YouTube/product videos must be embedded inline when the publishing target supports embeds. Do not hide the primary video inside collapsed details, make the user leave the article to watch, or place a custom overlay over the native player. Include a normal fallback link only as secondary support.
- The final read-through must answer: would a busy professional keep reading after the first screen? If not, restructure before publishing.

## Quality gate

Before publishing, the article must pass three checks:

1. **Concept clarity**: important jargon is explained through inline wording, callouts, or target-supported tooltips.
2. **Business value**: the article connects the topic to time, cost, risk, quality, customer experience, or new workflows.
3. **Distribution pack**: include SEO title, meta description, AEO questions, internal link suggestions, image prompt, and 2-3 social teaser drafts in the PR/context notes. Do not auto-publish social posts.
4. **Readability/product gate**: check skimmability, visual breaks, concrete examples, and whether any section feels like filler. Rewrite before publishing if the article is merely correct.
