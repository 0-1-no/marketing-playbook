# Format Design

Use this before outlining any blog article that should feel distinctive, visual, or highly readable. The goal is to make the post a designed editorial product, not a text dump.

## Format brief

Before drafting, choose:

- **Reader job**: what the reader wants to understand or decide.
- **Editorial shape**: briefing, magazine feature, field guide, case teardown, comparison, checklist, interactive explainer, or opinion essay.
- **First-screen promise**: the one thing that makes a busy reader continue.
- **Visual system**: hero image, diagrams, tables, callouts, cards, screenshots, embedded video, or light interactivity.
- **Concrete proof**: examples, numbers, screenshots, quotes, customer-like scenarios, or source excerpts.

Do not choose a plain essay by default. Use a plain essay only when the argument itself is unusually strong and short.

## Reader rhythm

For busy business readers, prefer this structure:

1. **The move**: what changed, in one sharp paragraph.
2. **Why it matters**: the business consequence, not the technical novelty.
3. **The example**: one concrete workflow or before/after.
4. **The catch**: cost, risk, access, governance, limitations.
5. **The Monday move**: what the reader can do next week.

This can be dressed as a briefing, field guide, or magazine feature. Keep the rhythm even when headings differ.

## Section rule

Every substantive section needs:

- **Claim**: one sentence with a point of view.
- **Concrete**: a specific example, number, workflow, quote, or visual.
- **Action**: what the reader should think, decide, test, or avoid.

If the section only explains background, compress it into a sidebar or remove it.

## Visual modules

Use one visual module roughly every 500-700 words, or sooner if the article becomes abstract. Good modules:

- **Before/after workflow**: old way vs agent way.
- **Access/control table**: system -> agent may do -> human approves.
- **Cost math box**: tokens, hours, salary, or opportunity cost.
- **Scenario cards**: three realistic company situations.
- **Decision tree**: when to use a powerful model vs a cheaper one.
- **Embedded video**: when a launch demo or product video shows what prose cannot.
- **Illustration/infographic**: use `image-gen` or code-native SVG/HTML for diagrams when a list would be dull.

Never leave a thin list as the only representation of an important idea.

## Examples and specificity

Make examples feel like real work:

- weak: "analyse kundedata"
- stronger: "les 200 supportsaker fra siste måned, finn de fem gjentatte klagene, grupper dem etter produktområde, og foreslå hvilke to som bør prioriteres i neste sprint"

Use realistic constraints:

- source data;
- allowed actions;
- output format;
- approval point;
- success metric.

## Voice checks

- Speak directly to the reader. Avoid repeatedly labeling them as "leaders", "marketers", or "professionals".
- Replace superlatives with observable effects. "Programmatisk tilgang er nøkkelen" becomes "Uten API-tilgang må agenten vente på at mennesker kopierer data inn og ut."
- Remove filler transitions such as "det er her", "det betyr ikke at", and repeated "ikke bare X, men Y" when they add rhythm but not meaning.
- Use one sentence a reader could repeat in a meeting.

## Final format QA

Before publishing, scan the rendered article:

- Does the first screen clearly say why this matters?
- Are long lists turned into tables, diagrams, cards, or checklists?
- Is there at least one concrete workflow the reader can picture?
- Is there one number, calculation, or tradeoff where value is discussed?
- Does every visual earn its place?
- Would the article still be useful if the reader skipped the FAQ?
