---
name: accessibility
description: WCAG compliance, kontrast og keyboard-navigasjon. Bruk for a11y.
---

# Accessibility (a11y)

> **Metodikk-fil:** Dette er REGLER og krav som MÅ følges.
> A11y er ikke prosjektspesifikt - WCAG-kravene gjelder alle prosjekter.
> Kontrast-verdiene under er MINIMUMSKRAV, ikke forslag.

---

## Hvorfor Accessibility?

1. **Etisk** - Alle fortjener tilgang
2. **Juridisk** - Krav i mange land (WCAG)
3. **Business** - 15-20% av befolkningen har funksjonsnedsettelse
4. **SEO** - God a11y = bedre SEO
5. **UX** - A11y-forbedringer hjelper alle

---

## WCAG 2.1 Nivåer

| Nivå | Beskrivelse | Mål |
|------|-------------|-----|
| A | Minimum | Kritiske barrierer fjernet |
| AA | Standard | **Anbefalt minimum** |
| AAA | Optimal | Høyeste tilgjengelighet |

**Mål for de fleste prosjekter: WCAG 2.1 AA**

---

## Kontrast

### Krav

| Element | Minimum kontrast |
|---------|-----------------|
| Normal tekst (under 18px) | 4.5:1 |
| Stor tekst (18px+ eller 14px bold) | 3:1 |
| UI-komponenter og grafikk | 3:1 |

### Sjekk Kontrast

**Verktøy:**
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Stark](https://www.getstark.co/) (Figma plugin)
- axe DevTools (Chrome extension)

### Vanlige Feil

| Problem | Løsning |
|---------|---------|
| Lys grå tekst på hvit | Mørk opp til minst #767676 |
| Placeholder tekst for lys | Bruk #767676 eller mørkere |
| Disabled state usynlig | Behold lesbar kontrast |
| Link ikke synlig i tekst | Understrek eller tydelig farge |

### Eksempel

```css
/* Dårlig - 2.5:1 kontrast */
.text-muted { color: #BBBBBB; }

/* Bra - 4.6:1 kontrast */
.text-muted { color: #767676; }
```

---

## Keyboard Navigation

### Alle Interaktive Elementer

Må være tilgjengelige med keyboard:
- Tab: Flytt fokus fremover
- Shift+Tab: Flytt fokus bakover
- Enter/Space: Aktiver
- Arrow keys: Naviger i lister/menyer
- Escape: Lukk modaler/dropdowns

### Focus States

```css
/* Aldri gjør dette */
*:focus { outline: none; }

/* Gjør dette i stedet */
*:focus-visible {
  outline: 2px solid var(--brand-500);
  outline-offset: 2px;
}

/* Skjul for mus, vis for keyboard */
button:focus:not(:focus-visible) {
  outline: none;
}
```

### Tab Order

```tsx
// Naturlig tab-order følger DOM
<header>
  <nav>
    <a href="/">Logo</a>           {/* Tab 1 */}
    <a href="/features">Features</a> {/* Tab 2 */}
    <a href="/pricing">Pricing</a>   {/* Tab 3 */}
  </nav>
</header>

// Bruk tabindex sparsomt
<div tabIndex={0}>Fokusbar div</div>  // Kun når nødvendig
<div tabIndex={-1}>Programmatisk fokus</div>  // For modaler etc.
```

### Skip Links

```tsx
// Første element på siden
<a
  href="#main-content"
  className="
    sr-only focus:not-sr-only
    focus:absolute focus:top-4 focus:left-4
    focus:z-50 focus:bg-white focus:p-4
  "
>
  Hopp til hovedinnhold
</a>

// ...header og nav...

<main id="main-content">
  {content}
</main>
```

---

## Semantisk HTML

### Bruk Riktige Elementer

| Feil | Riktig |
|------|--------|
| `<div onClick>` | `<button>` |
| `<div class="link">` | `<a href>` |
| `<div class="header">` | `<header>` |
| `<div class="nav">` | `<nav>` |
| `<div class="main">` | `<main>` |
| `<div class="list">` | `<ul>/<ol>` |

### Landmarks

```html
<body>
  <header>Logo + Nav</header>
  <nav>Hovednavigasjon</nav>
  <main>
    <article>Hovedinnhold</article>
    <aside>Sidebar</aside>
  </main>
  <footer>Footer</footer>
</body>
```

### Headings

```html
<!-- Riktig hierarki -->
<h1>Sidetittel</h1>
  <h2>Seksjon 1</h2>
    <h3>Underseksjon</h3>
  <h2>Seksjon 2</h2>

<!-- Feil - hopper over nivåer -->
<h1>Tittel</h1>
<h3>Underseksjon</h3>  <!-- Mangler h2! -->
```

---

## ARIA

### Når Bruke ARIA

> "No ARIA is better than bad ARIA"

Bruk kun når semantisk HTML ikke er nok.

### Vanlige ARIA-attributter

```tsx
// Beskrivelse
<button aria-label="Lukk modal">×</button>

// Utvidet tilstand
<button aria-expanded={isOpen}>
  Meny
</button>

// Kontroller annet element
<button aria-controls="menu-id" aria-expanded={isOpen}>
  Toggle
</button>
<nav id="menu-id" aria-hidden={!isOpen}>
  {menuItems}
</nav>

// Live regions for dynamisk innhold
<div aria-live="polite" aria-atomic="true">
  {statusMessage}
</div>

// Rolle når HTML ikke er nok
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Modal tittel</h2>
</div>
```

### ARIA for Vanlige Patterns

#### Tabs

```tsx
<div role="tablist">
  <button
    role="tab"
    aria-selected={activeTab === 0}
    aria-controls="panel-0"
  >
    Tab 1
  </button>
</div>
<div
  role="tabpanel"
  id="panel-0"
  aria-labelledby="tab-0"
>
  Innhold
</div>
```

#### Modal

```tsx
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-title"
  aria-describedby="modal-desc"
>
  <h2 id="modal-title">Tittel</h2>
  <p id="modal-desc">Beskrivelse</p>
</div>
```

---

## Bilder

### Alt-tekst

```tsx
// Informative bilder - beskriv innholdet
<img src="/chart.png" alt="Salg økte 25% fra Q1 til Q2 2024" />

// Dekorative bilder - tom alt
<img src="/decorative-blob.svg" alt="" role="presentation" />

// Komplekse bilder - lang beskrivelse
<figure>
  <img src="/infographic.png" alt="Oversikt over brukerreisen" />
  <figcaption>
    Detaljert beskrivelse av infografikken...
  </figcaption>
</figure>
```

### Ikoner

```tsx
// Ikon med tekst - skjul ikonet
<button>
  <Icon aria-hidden="true" />
  Lukk
</button>

// Kun ikon - legg til label
<button aria-label="Lukk">
  <Icon aria-hidden="true" />
</button>
```

---

## Forms

### Labels

```tsx
// Alltid koble label til input
<label htmlFor="email">E-post</label>
<input id="email" type="email" />

// Visuelt skjult label
<label htmlFor="search" className="sr-only">Søk</label>
<input id="search" type="search" placeholder="Søk..." />
```

### Error Messages

```tsx
<div>
  <label htmlFor="email">E-post</label>
  <input
    id="email"
    type="email"
    aria-invalid={hasError}
    aria-describedby={hasError ? "email-error" : undefined}
  />
  {hasError && (
    <p id="email-error" role="alert" className="text-red-500">
      Ugyldig e-postadresse
    </p>
  )}
</div>
```

### Required Fields

```tsx
<label htmlFor="name">
  Navn
  <span aria-hidden="true" className="text-red-500">*</span>
</label>
<input
  id="name"
  required
  aria-required="true"
/>
```

---

## Motion

### Respekter Preferanser

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

```tsx
// React hook
const prefersReducedMotion = window.matchMedia(
  '(prefers-reduced-motion: reduce)'
).matches;

<motion.div
  animate={{ x: 100 }}
  transition={{
    duration: prefersReducedMotion ? 0 : 0.3
  }}
/>
```

---

## Testing

### Automatisk Testing

```bash
# axe-core i tester
npm install @axe-core/react

# eslint-plugin-jsx-a11y
npm install eslint-plugin-jsx-a11y
```

### Manuell Testing

1. **Keyboard-only:** Naviger hele siden med kun tastatur
2. **Screen reader:** Test med VoiceOver (Mac) eller NVDA (Windows)
3. **Zoom:** Test ved 200% zoom
4. **Fargeblindhet:** Bruk Chrome extension som simulerer
5. **Kontrast:** Sjekk alle tekst/bakgrunn-kombinasjoner

### Screen Reader Testing

| OS | Screen Reader | Shortcut |
|-----|--------------|----------|
| Mac | VoiceOver | Cmd + F5 |
| Windows | NVDA | Ctrl + Alt + N |
| Windows | Narrator | Win + Ctrl + Enter |

---

## Tailwind Utility Classes

```tsx
// Screen reader only
<span className="sr-only">Kun for skjermlesere</span>

// Not screen reader only (show again)
<span className="not-sr-only">Synlig igjen</span>
```

---

## Sjekkliste

Før levering, bekreft:

- [ ] Alle tekst/bakgrunn har 4.5:1+ kontrast
- [ ] UI-elementer har 3:1+ kontrast
- [ ] Alle interaktive elementer er keyboard-tilgjengelige
- [ ] Focus-states er synlige
- [ ] Semantisk HTML brukes (button, a, nav, main, etc.)
- [ ] Alle bilder har passende alt-tekst
- [ ] Forms har labels koblet til inputs
- [ ] Error messages er tilgjengelige
- [ ] Skip-link til hovedinnhold
- [ ] prefers-reduced-motion respekteres
- [ ] Testet med screen reader
- [ ] Testet med kun keyboard
