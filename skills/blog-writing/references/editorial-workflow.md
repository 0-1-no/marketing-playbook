# Editorial Workflow

Use this workflow for blog posts on owned brands.

## 1. Establish the brief

- Identify target brand, audience, journey stage, article type, and publishing repo.
- Read local marketing files before writing. Brand rules override this generic workflow.
- Convert loose notes into a thesis: one sentence that states what the reader should understand or do after reading.

## 2. Research

- Prefer primary sources, official docs, first-party announcements, product pages, company blogs, and direct data.
- For news articles, verify dates and use exact dates instead of relative words like "i går".
- Separate safe claims from uncertain claims. Do not publish unverified launch/product claims as facts.
- Save source URLs in PR/context notes when they influenced the article.

## 3. SEO/AEO subagent

- Before outlining, spawn the SEO/AEO reviewer described in `seo-aeo-reviewer.md`.
- The main writer owns the article. The reviewer supplies search intent, answer-engine structure, metadata, FAQ ideas, and risks.
- If no subagent tool is available, create the same brief manually and clearly mark the fallback in the PR/context notes.

## 4. Outline

Create a format brief before the outline. Read `format-design.md` and decide whether the post should be a briefing, magazine feature, field guide, case teardown, comparison, checklist, interactive explainer, or essay. Then use this default shape unless the brand or topic demands otherwise:

1. Hook/problem: why this matters now.
2. Answer block: 40-60 words that can stand alone.
3. Context: what changed, in plain language.
4. Business implication: what this means for the reader's company.
5. Practical checklist or decision guide.
6. FAQ/AEO questions when useful.
7. CTA that fits the brand and journey stage.

## 5. Draft

- Write short paragraphs and descriptive H2s.
- Give the reader the answer before the nuance.
- Use specific examples instead of generic claims.
- Use the section rule: claim -> concrete example -> action.
- Turn thin lists into tables, diagrams, checklists, scenario cards, or graphics.
- Keep technical detail only where it changes the decision.
- Add internal links naturally; never force irrelevant links.

## 6. Edit

- Run the Norwegian humanizer pass.
- Run the concept explainer pass.
- Run the format QA pass from `format-design.md`.
- Check frontmatter/metadata, image alt text, and CTA.
- Confirm claims are sourced or framed as interpretation.

## 7. Publish and verify

- Follow the target publishing reference.
- Run the repo's relevant checks.
- If the repo supports PRs, use PR -> green checks -> merge -> deploy verification.
- Do not mark the post done until the site is verified after merge/deploy.
