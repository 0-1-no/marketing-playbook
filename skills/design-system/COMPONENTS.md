---
name: components
description: Komponentbibliotek-guide. Bruk ved bygging av buttons, forms, cards, layouts.
---

# Components

> **Metodikk-fil:** Dette er patterns og prinsipper for komponenter.
> Faktiske komponent-stiler dokumenteres i `./marketing/DESIGN-SYSTEM.md`.
> Kode-eksemplene viser STRUKTUR - bruk farger/fonts/spacing fra prosjektets design system.

---

## Prinsipper

### 1. Konsistens med Karakter

Komponenter skal være konsistente, men ha personlighet:
- Konsistent padding, spacing, border-radius
- Men: unike hover-states, animasjoner, detaljer

### 2. States er Kritiske

Hver komponent trenger:
- Default
- Hover
- Active/Pressed
- Focus
- Disabled
- Loading (der relevant)

### 3. Tilgjengelighet Bygget Inn

- Keyboard-navigerbar
- Focus-visible states
- ARIA-labels der nødvendig
- Kontrast på alle states

---

## Buttons

### Varianter

```tsx
// Primary - hovedhandlinger
<Button variant="primary">Start gratis</Button>

// Secondary - sekundære handlinger
<Button variant="secondary">Les mer</Button>

// Ghost - tertiære handlinger
<Button variant="ghost">Avbryt</Button>

// Destructive - destruktive handlinger
<Button variant="destructive">Slett</Button>
```

### Størrelser

```tsx
<Button size="sm">Small</Button>   // h-8, text-sm
<Button size="md">Medium</Button>  // h-10, text-base
<Button size="lg">Large</Button>   // h-12, text-lg
```

### Anti-Patterns

| Unngå | Hvorfor |
|-------|---------|
| Identiske buttons overalt | Ingen visuelt hierarki |
| Kun tekst-endring mellom varianter | Vanskelig å skille |
| Manglende hover-state | Føles dødt |
| Samme border-radius som alt annet | Uniform |

### Eksempel: Karakterfull Button

```tsx
// I stedet for standard shadcn button
<button className="
  relative overflow-hidden
  bg-black text-white
  px-6 py-3 rounded-full
  font-medium
  transition-all duration-300
  hover:scale-105
  hover:shadow-[0_0_30px_rgba(0,0,0,0.3)]
  active:scale-95
  group
">
  <span className="relative z-10">Kom i gang</span>
  <span className="
    absolute inset-0 bg-gradient-to-r from-brand-500 to-brand-600
    opacity-0 group-hover:opacity-100
    transition-opacity duration-300
  "/>
</button>
```

---

## Forms

### Input Fields

```tsx
<div className="space-y-2">
  <Label htmlFor="email">E-post</Label>
  <Input
    id="email"
    type="email"
    placeholder="din@epost.no"
    className="
      h-12 px-4
      border-2 border-gray-200
      rounded-lg
      focus:border-brand-500 focus:ring-2 focus:ring-brand-500/20
      transition-all duration-200
    "
  />
  <p className="text-sm text-muted-foreground">
    Vi sender aldri spam.
  </p>
</div>
```

### Form Groups

```tsx
<form className="space-y-6">
  {/* Grupper relaterte felt */}
  <div className="grid grid-cols-2 gap-4">
    <FormField label="Fornavn" />
    <FormField label="Etternavn" />
  </div>

  {/* Enkelt-felt med full bredde */}
  <FormField label="E-post" type="email" />

  {/* Submit med tydelig hierarki */}
  <div className="flex gap-3">
    <Button variant="primary" type="submit">Send inn</Button>
    <Button variant="ghost" type="reset">Nullstill</Button>
  </div>
</form>
```

### Validation States

```tsx
// Error state
<Input
  className="border-red-500 focus:border-red-500 focus:ring-red-500/20"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<p id="email-error" className="text-sm text-red-500">
  Ugyldig e-postadresse
</p>

// Success state
<Input
  className="border-green-500 focus:border-green-500"
  aria-invalid="false"
/>
```

---

## Cards

### Standard Card

```tsx
<div className="
  bg-white dark:bg-gray-900
  border border-gray-200 dark:border-gray-800
  rounded-2xl
  p-6
  transition-all duration-300
  hover:shadow-lg hover:border-gray-300
  hover:-translate-y-1
">
  <h3 className="font-semibold text-lg">Tittel</h3>
  <p className="text-muted-foreground mt-2">Beskrivelse</p>
</div>
```

### Feature Card

```tsx
<div className="
  group
  bg-gradient-to-br from-gray-50 to-gray-100
  dark:from-gray-900 dark:to-gray-800
  rounded-3xl
  p-8
  border border-transparent
  hover:border-brand-500/50
  transition-all duration-500
">
  <div className="
    w-12 h-12 rounded-xl
    bg-brand-500 text-white
    flex items-center justify-center
    group-hover:scale-110
    transition-transform duration-300
  ">
    <Icon />
  </div>
  <h3 className="font-bold text-xl mt-6">Feature navn</h3>
  <p className="text-muted-foreground mt-2">
    Feature beskrivelse som forklarer verdien.
  </p>
</div>
```

### Bento Grid

```tsx
<div className="grid grid-cols-4 gap-4">
  {/* Stor featured card */}
  <div className="col-span-2 row-span-2 rounded-3xl bg-brand-500 p-8">
    <h2 className="text-2xl font-bold text-white">Hovedfeature</h2>
  </div>

  {/* Mindre cards */}
  <div className="rounded-2xl bg-gray-100 p-6">Card 2</div>
  <div className="rounded-2xl bg-gray-100 p-6">Card 3</div>
  <div className="col-span-2 rounded-2xl bg-gray-100 p-6">Card 4</div>
</div>
```

---

## Navigation

### Header

```tsx
<header className="
  fixed top-0 inset-x-0 z-50
  backdrop-blur-md bg-white/80 dark:bg-black/80
  border-b border-gray-200/50 dark:border-gray-800/50
">
  <nav className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
    <Logo />
    <div className="hidden md:flex items-center gap-8">
      <NavLink href="/features">Features</NavLink>
      <NavLink href="/pricing">Priser</NavLink>
      <NavLink href="/about">Om oss</NavLink>
    </div>
    <div className="flex items-center gap-4">
      <Button variant="ghost">Logg inn</Button>
      <Button variant="primary">Kom i gang</Button>
    </div>
  </nav>
</header>
```

### Nav Links med Indicator

```tsx
<NavLink
  href="/features"
  className="
    relative py-2
    text-gray-600 hover:text-gray-900
    transition-colors
    group
  "
>
  Features
  <span className="
    absolute bottom-0 left-0 right-0 h-0.5
    bg-brand-500
    scale-x-0 group-hover:scale-x-100
    transition-transform origin-left
  "/>
</NavLink>
```

---

## Layout Patterns

### Container

```tsx
// Standard container
<div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  {children}
</div>

// Narrow container (for text)
<div className="max-w-3xl mx-auto px-4">
  {children}
</div>

// Full-bleed with padded content
<section className="bg-gray-50">
  <div className="max-w-7xl mx-auto px-4 py-24">
    {children}
  </div>
</section>
```

### Section Spacing

```tsx
// Konsistent vertikal spacing mellom seksjoner
<section className="py-16 sm:py-24 lg:py-32">
  {/* Innhold */}
</section>
```

### Grid Systems

```tsx
// 2-column
<div className="grid md:grid-cols-2 gap-8 lg:gap-16">

// 3-column
<div className="grid md:grid-cols-3 gap-6 lg:gap-8">

// Asymmetrisk
<div className="grid md:grid-cols-5 gap-8">
  <div className="md:col-span-3">{/* Større */}</div>
  <div className="md:col-span-2">{/* Mindre */}</div>
</div>
```

---

## Border Radius Strategi

**Unngå:** Samme radius på alt (8px overalt)

**Gjør:** Skaler radius basert på element-størrelse

```css
:root {
  --radius-sm: 0.25rem;   /* 4px - small elements, badges */
  --radius-md: 0.5rem;    /* 8px - inputs, small cards */
  --radius-lg: 0.75rem;   /* 12px - buttons, medium cards */
  --radius-xl: 1rem;      /* 16px - large cards */
  --radius-2xl: 1.5rem;   /* 24px - hero sections, modals */
  --radius-full: 9999px;  /* Pills, avatars */
}
```

| Element | Anbefalt Radius |
|---------|----------------|
| Badges, tags | sm (4px) |
| Inputs | md (8px) |
| Buttons | lg (12px) eller full |
| Cards | xl-2xl (16-24px) |
| Hero images | 2xl+ (24px+) |
| Avatars | full |

---

## Sjekkliste

Før levering, bekreft:

- [ ] Alle komponenter har alle states (hover, active, focus, disabled)
- [ ] Border-radius varierer med intensjon
- [ ] Spacing er konsistent (bruker spacing-skala)
- [ ] Buttons har tydelig visuelt hierarki
- [ ] Forms har tydelig validation feedback
- [ ] Keyboard-navigasjon fungerer
- [ ] Focus-states er synlige
