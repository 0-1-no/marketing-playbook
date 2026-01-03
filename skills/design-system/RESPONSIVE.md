---
name: responsive
description: Breakpoints, mobile-first og responsive patterns. Bruk ved responsivt design.
---

# Responsive Design

> **Metodikk-fil:** Dette er prinsipper for responsivt design.
> Prosjektspesifikke breakpoints dokumenteres i `./marketing/DESIGN-SYSTEM.md`.
> Verdiene under er STANDARD TAILWIND - tilpass om prosjektet bruker andre.

---

## Mobile-First Approach

**Start alltid med mobil, utvid til desktop.**

```css
/* Mobile first */
.component {
  padding: 1rem;           /* Mobil default */
}

@media (min-width: 768px) {
  .component {
    padding: 2rem;         /* Tablet+ */
  }
}

@media (min-width: 1024px) {
  .component {
    padding: 3rem;         /* Desktop */
  }
}
```

**Hvorfor mobile-first?**
1. Tvinger deg til å prioritere innhold
2. Lettere å legge til enn å fjerne
3. Bedre performance på mobil
4. Flertallet av trafikk er mobil

---

## Breakpoints

### Standard Breakpoints

| Navn | Min-width | Typisk enhet |
|------|-----------|--------------|
| sm | 640px | Store mobiler |
| md | 768px | Tablets |
| lg | 1024px | Små laptops |
| xl | 1280px | Laptops |
| 2xl | 1536px | Desktops |

### Tailwind

```tsx
<div className="
  p-4          /* default (mobil) */
  sm:p-6       /* 640px+ */
  md:p-8       /* 768px+ */
  lg:p-12      /* 1024px+ */
  xl:p-16      /* 1280px+ */
">
```

### CSS Variables

```css
:root {
  --container-padding: 1rem;
}

@media (min-width: 768px) {
  :root {
    --container-padding: 2rem;
  }
}

@media (min-width: 1024px) {
  :root {
    --container-padding: 4rem;
  }
}
```

---

## Container Strategy

### Max-Width Container

```tsx
<div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  {children}
</div>
```

### Full-Bleed Sections

```tsx
// Bakgrunn full bredde, innhold begrenset
<section className="bg-gray-50">
  <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-24">
    {content}
  </div>
</section>
```

### Narrow Container for Tekst

```tsx
// Optimal lesbarhet: ~65-75 tegn per linje
<article className="max-w-prose mx-auto px-4">
  {longFormContent}
</article>
```

---

## Grid Patterns

### Responsiv Grid

```tsx
// 1 kolonne → 2 kolonner → 3 kolonner
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  {cards.map(card => <Card key={card.id} {...card} />)}
</div>
```

### Asymmetrisk Grid

```tsx
// Bilde + tekst som flipper på mobil
<div className="grid lg:grid-cols-2 gap-8 lg:gap-16 items-center">
  <div className="order-2 lg:order-1">
    <h2>Tittel</h2>
    <p>Beskrivelse</p>
  </div>
  <div className="order-1 lg:order-2">
    <Image />
  </div>
</div>
```

### Bento Grid

```tsx
<div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
  {/* Stor featured - full bredde på mobil */}
  <div className="col-span-2 row-span-2 lg:col-span-2">
    <FeaturedCard />
  </div>

  {/* Mindre kort */}
  <div className="col-span-1"><SmallCard /></div>
  <div className="col-span-1"><SmallCard /></div>

  {/* Full bredde på mobil, halv på desktop */}
  <div className="col-span-2 lg:col-span-2"><WideCard /></div>
</div>
```

---

## Typography Scaling

### Fluid Typography

```css
/* Skalerer smoothly mellom breakpoints */
h1 {
  font-size: clamp(2rem, 5vw + 1rem, 4rem);
}

h2 {
  font-size: clamp(1.5rem, 3vw + 0.5rem, 2.5rem);
}
```

### Tailwind Responsive Text

```tsx
<h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl">
  Stor overskrift
</h1>
```

### Body Text

```css
body {
  font-size: 16px;  /* Aldri mindre enn dette på mobil */
}

@media (min-width: 1024px) {
  body {
    font-size: 18px;  /* Litt større på desktop */
  }
}
```

---

## Touch Targets

### Minimum Størrelse

```
Minimum touch target: 44x44px (Apple) eller 48x48px (Google)
```

```tsx
// Selv om ikonet er 24px, er touch-området 48px
<button className="p-3">  {/* 12px padding rundt 24px ikon = 48px total */}
  <Icon className="w-6 h-6" />
</button>
```

### Spacing Mellom Targets

```tsx
// Minimum 8px mellom klikkbare elementer
<nav className="flex gap-2">  {/* 8px gap */}
  <NavLink>Link 1</NavLink>
  <NavLink>Link 2</NavLink>
</nav>
```

---

## Navigation Patterns

### Desktop → Mobile Menu

```tsx
<header>
  {/* Desktop nav - skjult på mobil */}
  <nav className="hidden md:flex gap-6">
    <NavLink>Features</NavLink>
    <NavLink>Pricing</NavLink>
    <NavLink>About</NavLink>
  </nav>

  {/* Mobile hamburger - skjult på desktop */}
  <button className="md:hidden p-2">
    <MenuIcon />
  </button>
</header>
```

### Mobile Menu Slide

```tsx
<Sheet>
  <SheetTrigger asChild>
    <button className="md:hidden">
      <MenuIcon />
    </button>
  </SheetTrigger>
  <SheetContent side="right" className="w-80">
    <nav className="flex flex-col gap-4 mt-8">
      <NavLink>Features</NavLink>
      <NavLink>Pricing</NavLink>
      <NavLink>About</NavLink>
    </nav>
  </SheetContent>
</Sheet>
```

---

## Image Handling

### Responsive Images

```tsx
<Image
  src="/hero.jpg"
  alt="Hero"
  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
  fill
  className="object-cover"
/>
```

### Art Direction

```tsx
<picture>
  <source media="(min-width: 1024px)" srcSet="/hero-desktop.jpg" />
  <source media="(min-width: 768px)" srcSet="/hero-tablet.jpg" />
  <img src="/hero-mobile.jpg" alt="Hero" />
</picture>
```

### Aspect Ratio

```tsx
// Konsistent aspect ratio på alle skjermstørrelser
<div className="aspect-video relative">
  <Image src="/video-thumb.jpg" alt="" fill className="object-cover" />
</div>

// Kvadrat
<div className="aspect-square">
  <Image />
</div>
```

---

## Spacing Scaling

### Konsistent Spacing-skala

```css
:root {
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-24: 6rem;     /* 96px */
  --space-32: 8rem;     /* 128px */
}
```

### Section Spacing

```tsx
// Responsive vertikal spacing
<section className="py-16 md:py-24 lg:py-32">
  {content}
</section>
```

---

## Testing

### Enheter å Teste

| Bredde | Enhet |
|--------|-------|
| 320px | iPhone SE |
| 375px | iPhone 12/13 |
| 390px | iPhone 14 |
| 768px | iPad |
| 1024px | iPad Pro / Laptop |
| 1280px | Desktop |
| 1536px | Large desktop |

### Chrome DevTools

1. Åpne DevTools (F12)
2. Toggle device toolbar (Ctrl/Cmd + Shift + M)
3. Test ulike enheter
4. Test landscape vs portrait

---

## Sjekkliste

Før levering, bekreft:

- [ ] Fungerer på 320px bredde (minste iPhone)
- [ ] Touch targets er minst 44x44px
- [ ] Tekst er minst 16px på mobil
- [ ] Bilder skalerer riktig
- [ ] Navigation er tilgjengelig på mobil
- [ ] Ingen horisontal scroll
- [ ] Forms er brukbare på mobil (input-typer, tastatur)
- [ ] Spacing føles riktig på alle størrelser
- [ ] Testet på ekte enhet (ikke bare simulator)
