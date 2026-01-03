---
name: anti-patterns
description: Identifiserer og unngår generisk AI-estetikk ("AI slop"). Bruk før levering av UI.
---

# Anti-Patterns: Unngå AI Slop

> **Metodikk-fil:** Dette er REGLER og sjekklister som MÅ følges.
> Disse prinsippene gjelder alle prosjekter - de er ikke prosjektspesifikke.
> Bruk denne som kvalitetssjekk FØR du leverer UI.

---

## Hva er AI Slop?

Generisk, forutsigbar design som umiddelbart signaliserer "dette er AI-generert":
- Mangel på personlighet
- Trygt og kjedelig
- Ser ut som alt annet
- Kunne vært hvem som helst sin side

**Problemet:** Når alt ser likt ut, er det umulig å bygge merkevare. AI slop dreper differensiering.

---

## Red Flags Sjekkliste

### Typografi

| Red Flag | Hvorfor det er AI slop |
|----------|------------------------|
| Inter som primærfont | Hver AI-side bruker Inter |
| Roboto, Arial, system fonts | Null personlighet |
| Ingen hierarki mellom headlines | Flat, kjedelig |
| Generiske font-størrelser (16px/32px) | Ingen intensjon |
| Kun én font overalt | Mangler kontrast |

**Fix:** Velg minst én karakterfull font. Bruk font-pairing med intensjon. Varier størrelser dramatisk.

### Farger

| Red Flag | Hvorfor det er AI slop |
|----------|------------------------|
| Lilla (#7C3AED) → blå (#3B82F6) gradient | THE AI gradient |
| Hvit bakgrunn + blå CTA | Default Tailwind |
| Ingen semantisk fargebruk | Tilfeldig |
| Kun primærfarge + grå | Kjedelig palett |
| Farger som "bare fungerer" uten mening | Ingen merkevare |

**Fix:** Definer farger med mening. Bruk overraskende aksenter. Ha en dominantfarge som eies.

### Layout

| Red Flag | Hvorfor det er AI slop |
|----------|------------------------|
| Perfekt symmetri overalt | Robotisk |
| Standard 12-column grid uten variasjon | Forutsigbar |
| Hero → Features → Testimonials → CTA | Forventet rekkefølge |
| Ingen overlapping eller asymmetri | Steril |
| Maks bredde 1200px, sentrert | Safe og kjedelig |

**Fix:** Bryt grid med intensjon. Overlap elementer. Asymmetri skaper spenning. Varier seksjonsbredder.

### Komponenter

| Red Flag | Hvorfor det er AI slop |
|----------|------------------------|
| Identisk border-radius på alt (8px) | Uniformt |
| Standard shadcn/Tailwind uten tilpasning | Template-look |
| Ingen custom ikoner | Generic |
| Stock photos "diverse team smiles at laptop" | AI-bilde vibes |
| Kort med ikon + headline + tekst (repetert) | Feature-grid-syndromet |

**Fix:** Varier border-radius. Tilpass komponenter. Bruk egne illustrasjoner. Unngå repetitive mønstre.

### Motion

| Red Flag | Hvorfor det er AI slop |
|----------|------------------------|
| Ingen animasjoner | Dødt |
| Kun fade-in på scroll | Minimum effort |
| Ingen hover states | Ikke interaktivt |
| Ingen mikro-interaksjoner | Sjelløst |
| Alt animerer likt | Uniformt |

**Fix:** Differensier animasjoner per element. Lag overraskende hover-states. Gi feedback på interaksjon.

### Overall Vibe

| Red Flag | Hvorfor det er AI slop |
|----------|------------------------|
| Kunne vært hvem som helst sin side | Ingen merkevare |
| Ingen overraskelser | Kjedelig |
| Følger "best practices" slavisk | Safe |
| Mangel på personlighet | Generisk |
| Ingenting å huske | Forglemmelig |

---

## The AI Slop Starter Pack

Hvis siden din har disse, er det AI slop:

```
□ Inter font
□ Lilla/blå gradient
□ Hvit bakgrunn
□ Hero med headline + subheadline + CTA
□ 3-kolonne feature grid med ikoner
□ Testimonials i kort-format
□ "Start free trial" CTA
□ Standard footer med 4 kolonner
□ 8px border-radius overalt
□ Kun fade-in animasjoner
```

**Hvis du krysser av 5+, redesign.**

---

## Hvordan Fikse

For hvert element, spør:

1. **Hvorfor dette valget?** (Ikke "fordi det er standard")
2. **Hva ville vært overraskende her?**
3. **Hva sier dette om merkevaren?**
4. **Ville konkurrenten gjort dette?** (Hvis ja, gjør noe annet)

---

## Konkret Sjekkliste Før Levering

Før du leverer UI, bekreft:

### Must-haves

- [ ] Minst 1 font som IKKE er Inter/Roboto/Arial/system
- [ ] Fargepalett som skiller seg fra blå/lilla gradient
- [ ] Minst 1 asymmetrisk element eller layout-brudd
- [ ] Minst 1 custom/karakterfull mikro-interaksjon
- [ ] Minst 1 "den ene tingen" som er uforglemmelig
- [ ] Ingen stock photos i generisk stil
- [ ] Border-radius varierer med intensjon

### Nice-to-haves

- [ ] Custom illustrasjoner eller ikoner
- [ ] Uventet seksjon-rekkefølge
- [ ] Modige fargevalg som eies
- [ ] Animasjoner som overrasker
- [ ] Typografi som er signatur

---

## Alternative Approaches

### I stedet for... → Prøv...

| AI Slop | Alternativ |
|---------|------------|
| Inter font | Satoshi, Clash Display, Cabinet Grotesk, Plus Jakarta Sans |
| Lilla→blå gradient | Solid farge med interessant aksent |
| Symmetrisk hero | Off-center headline, overlapping elementer |
| 3-kolonne feature grid | Bento grid, asymmetrisk layout, scrolling list |
| Standard testimonials | Quotes integrert i design, video testimonials |
| Generiske ikoner | Custom illustrasjoner, ingen ikoner, emojis |
| 8px overalt | Variert: 0px, 4px, 16px, 32px, full rounded |
| Fade-in | Scale, slide, stagger, micro-interactions |

---

## Eksempler på Ikke-Slop

### Distinkte nettsider å lære av

- **Linear** - Mørk, dramatisk, custom animasjoner
- **Vercel** - Monokrom med presise detaljer
- **Notion** - Leken, illustrasjoner, karakterfullt
- **Stripe** - Gradient gjort riktig, custom alt
- **Raycast** - Keyboard-first, unikt visuelt språk

**Hva har de til felles?**
1. Tydelig estetisk retning
2. Egne visuelle elementer
3. Overraskende detaljer
4. Konsistent personlighet
5. Umulig å forveksle med andre

---

## Self-Check Spørsmål

Før levering, spør:

1. **Kan jeg identifisere merkevaren uten logo?**
2. **Ville jeg stoppet scrolling hvis jeg så dette?**
3. **Er det noe her jeg aldri har sett før?**
4. **Ville jeg vist dette til en designer jeg respekterer?**
5. **Om 5 minutter, hva husker jeg?**

Hvis svaret er "nei" på 2+, gå tilbake og redesign.

---

## The One Rule

> Hvis det kunne vært generert av å si "lag en landing page" til en AI, er det AI slop.

Distinkt design krever **intensjon** og **valg**. Hvert element skal ha en grunn - og "det er standard" er ikke en grunn.
