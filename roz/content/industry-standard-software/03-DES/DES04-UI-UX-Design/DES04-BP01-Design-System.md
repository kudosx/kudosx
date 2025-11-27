# DES04-BP01: Design System

Xây dựng design system để đảm bảo consistency và tăng tốc development.

## Design System Structure

```
Design System
├── Foundations
│   ├── Colors
│   ├── Typography
│   ├── Spacing
│   ├── Icons
│   └── Grid
├── Components
│   ├── Buttons
│   ├── Forms
│   ├── Cards
│   ├── Navigation
│   └── Modals
└── Patterns
    ├── Forms
    ├── Tables
    ├── Notifications
    └── Authentication
```

## Color System

```css
/* Primary Colors */
--color-primary-50: #eff6ff;
--color-primary-500: #3b82f6;
--color-primary-900: #1e3a8a;

/* Semantic Colors */
--color-success: #10b981;
--color-warning: #f59e0b;
--color-error: #ef4444;
--color-info: #3b82f6;

/* Neutral Colors */
--color-gray-50: #f9fafb;
--color-gray-500: #6b7280;
--color-gray-900: #111827;
```

## Typography Scale

```css
/* Font Sizes */
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */

/* Font Weights */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

## Spacing System

```css
/* 4px base unit */
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-12: 3rem;     /* 48px */
```

## Component Example: Button

```tsx
// Button variants
<Button variant="primary">Primary</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="outline">Outline</Button>
<Button variant="ghost">Ghost</Button>

// Button sizes
<Button size="sm">Small</Button>
<Button size="md">Medium</Button>
<Button size="lg">Large</Button>

// Button states
<Button disabled>Disabled</Button>
<Button loading>Loading</Button>
```

## Documentation Requirements

| Component | Required Docs |
|-----------|---------------|
| All | Description, props, examples |
| Interactive | States (hover, focus, disabled) |
| Forms | Validation states, error messages |
| Layout | Responsive behavior |

## Tools

| Tool | Purpose |
|------|---------|
| **Figma** | Design & prototyping |
| **Storybook** | Component documentation |
| **Chromatic** | Visual regression testing |
| **Zeroheight** | Design system documentation |

## Checklist

- [ ] Color palette defined
- [ ] Typography scale defined
- [ ] Spacing system defined
- [ ] Core components documented
- [ ] Usage guidelines written
- [ ] Storybook setup
- [ ] Accessibility guidelines
