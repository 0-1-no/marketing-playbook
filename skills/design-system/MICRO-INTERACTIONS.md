---
name: micro-interactions
description: Animasjoner, hover-states og transitions. Bruk for å gi liv til UI.
---

# Micro-Interactions

> **Metodikk-fil:** Dette er prinsipper for animasjoner og timing.
> Prosjektspesifikke motion-verdier dokumenteres i `./marketing/DESIGN-SYSTEM.md`.
> Timing-verdiene under er GENERELLE GUIDELINES - tilpass til prosjektets estetikk.

---

## Hvorfor Micro-Interactions?

Animasjoner gjør forskjellen mellom "fungerer" og "føles bra":

| Uten | Med |
|------|-----|
| Statisk, dødt | Levende, responsivt |
| Usikker på hva som skjedde | Tydelig feedback |
| Kjedelig | Minneverdig |
| AI slop | Håndverk |

---

## Timing Guidelines

### Duration

| Interaksjon | Varighet | Hvorfor |
|-------------|----------|---------|
| Hover states | 150-200ms | Rask respons |
| Button clicks | 100-150ms | Umiddelbar feedback |
| Fade transitions | 200-300ms | Smooth men rask |
| Page transitions | 300-500ms | Rom til å lese |
| Complex animations | 500-1000ms | Gir oppmerksomhet |

**Regel:** Raskere = snappier, saktere = mer elegant

### Easing

| Easing | Bruk for | CSS |
|--------|----------|-----|
| ease-out | Elementer som kommer inn | `cubic-bezier(0, 0, 0.2, 1)` |
| ease-in | Elementer som går ut | `cubic-bezier(0.4, 0, 1, 1)` |
| ease-in-out | State-endringer | `cubic-bezier(0.4, 0, 0.2, 1)` |
| spring | Lekne, bouncy | Krever JS/Framer Motion |

```css
:root {
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

---

## Hover States

### Button Hover

```css
/* Simpel men effektiv */
.button {
  transition: all 200ms var(--ease-out);
}
.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
.button:active {
  transform: translateY(0);
}

/* Med bakgrunns-effekt */
.button-glow:hover {
  box-shadow: 0 0 20px var(--brand-500);
}

/* Med scale */
.button-grow:hover {
  transform: scale(1.05);
}
```

### Card Hover

```css
.card {
  transition: all 300ms var(--ease-out);
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
}

/* Med border-effekt */
.card-border:hover {
  border-color: var(--brand-500);
}

/* Med gradient-reveal */
.card-gradient {
  background: linear-gradient(to bottom right, transparent, transparent);
}
.card-gradient:hover {
  background: linear-gradient(to bottom right, var(--brand-50), transparent);
}
```

### Link Hover

```css
/* Underline animation */
.link {
  position: relative;
}
.link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: currentColor;
  transform: scaleX(0);
  transform-origin: right;
  transition: transform 300ms var(--ease-out);
}
.link:hover::after {
  transform: scaleX(1);
  transform-origin: left;
}
```

---

## Loading States

### Skeleton Loading

```tsx
<div className="animate-pulse">
  <div className="h-4 bg-gray-200 rounded w-3/4 mb-2"></div>
  <div className="h-4 bg-gray-200 rounded w-1/2"></div>
</div>
```

### Button Loading

```tsx
<button disabled className="relative">
  <span className="opacity-0">Send inn</span>
  <span className="absolute inset-0 flex items-center justify-center">
    <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
      <circle
        className="opacity-25"
        cx="12" cy="12" r="10"
        stroke="currentColor"
        strokeWidth="4"
        fill="none"
      />
      <path
        className="opacity-75"
        fill="currentColor"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
      />
    </svg>
  </span>
</button>
```

### Progress Indicator

```css
.progress-bar {
  width: 0%;
  height: 4px;
  background: var(--brand-500);
  transition: width 300ms var(--ease-out);
}
```

---

## Page Transitions

### Fade + Slide

```tsx
// Med Framer Motion
import { motion } from 'framer-motion';

const pageVariants = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -20 }
};

<motion.div
  variants={pageVariants}
  initial="initial"
  animate="animate"
  exit="exit"
  transition={{ duration: 0.3, ease: [0, 0, 0.2, 1] }}
>
  {children}
</motion.div>
```

### Staggered Children

```tsx
const containerVariants = {
  animate: {
    transition: {
      staggerChildren: 0.1
    }
  }
};

const itemVariants = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0 }
};

<motion.ul variants={containerVariants} initial="initial" animate="animate">
  {items.map(item => (
    <motion.li key={item.id} variants={itemVariants}>
      {item.content}
    </motion.li>
  ))}
</motion.ul>
```

---

## Scroll-baserte Animasjoner

### Fade In On Scroll

```tsx
// Med Intersection Observer
import { useInView } from 'framer-motion';

function FadeIn({ children }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-100px" });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 40 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.6, ease: [0, 0, 0.2, 1] }}
    >
      {children}
    </motion.div>
  );
}
```

### Parallax

```tsx
import { useScroll, useTransform } from 'framer-motion';

function Parallax({ children, speed = 0.5 }) {
  const { scrollYProgress } = useScroll();
  const y = useTransform(scrollYProgress, [0, 1], ['0%', `${speed * 100}%`]);

  return (
    <motion.div style={{ y }}>
      {children}
    </motion.div>
  );
}
```

---

## Feedback Animations

### Success State

```tsx
// Checkmark animation
<motion.svg
  initial={{ pathLength: 0 }}
  animate={{ pathLength: 1 }}
  transition={{ duration: 0.5, ease: "easeOut" }}
>
  <motion.path d="M5 13l4 4L19 7" />
</motion.svg>
```

### Error Shake

```css
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-8px); }
  75% { transform: translateX(8px); }
}

.error-shake {
  animation: shake 0.4s ease-in-out;
}
```

### Toast Notification

```tsx
const toastVariants = {
  initial: { opacity: 0, y: 50, scale: 0.9 },
  animate: { opacity: 1, y: 0, scale: 1 },
  exit: { opacity: 0, y: 20, scale: 0.9 }
};

<motion.div
  variants={toastVariants}
  initial="initial"
  animate="animate"
  exit="exit"
  transition={{ type: "spring", stiffness: 500, damping: 30 }}
>
  Handling utført!
</motion.div>
```

---

## Performance

### Optimaliser for 60fps

```css
/* Bruk transform og opacity - de er GPU-akselerert */
.fast {
  transition: transform 200ms, opacity 200ms;
}

/* Unngå å animere disse */
.slow {
  transition: width 200ms;     /* Trigger layout */
  transition: height 200ms;    /* Trigger layout */
  transition: top 200ms;       /* Trigger layout */
  transition: box-shadow 200ms; /* Trigger paint */
}
```

### will-change

```css
/* Bruk sparsomt - kun på elementer som SKAL animeres */
.will-animate {
  will-change: transform;
}
```

### Reduser motion for brukere som foretrekker det

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Tailwind Animasjoner

### Innebygde

```tsx
<div className="animate-spin">Loading...</div>
<div className="animate-ping">Notification dot</div>
<div className="animate-pulse">Skeleton</div>
<div className="animate-bounce">Scroll indicator</div>
```

### Egendefinerte

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out',
        'slide-up': 'slideUp 0.5s ease-out',
        'scale-in': 'scaleIn 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        scaleIn: {
          '0%': { opacity: '0', transform: 'scale(0.95)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
      },
    },
  },
};
```

---

## Sjekkliste

Før levering, bekreft:

- [ ] Buttons har hover OG active states
- [ ] Cards har hover-effekt
- [ ] Loading states er implementert
- [ ] Timings føles responsive (ikke for sakte)
- [ ] Bruker GPU-akselererte properties (transform, opacity)
- [ ] prefers-reduced-motion er respektert
- [ ] Animasjoner tilfører verdi, ikke bare pynt
- [ ] Minst én "signature" animasjon som er unik
