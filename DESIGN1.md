# Design System Inspired by GitHub

## 1. Visual Theme & Atmosphere

GitHub's design system embodies a modern, developer-centric aesthetic that prioritizes clarity and efficiency in a dark-first environment. The visual language combines deep navy and black backgrounds with crisp white typography and vibrant accent colors, creating a professional yet approachable interface. The design favors minimal ornamentation, with subtle gradients and glowing elements (like animated orbs) providing visual interest without distraction. This system supports both light and dark themes, with careful attention to contrast and readability for extended coding sessions. The overall mood is forward-thinking, collaborative, and technically confident—reflecting GitHub's position as the platform where global development happens.

**Key Characteristics**
- Dark-first theme with high contrast for accessibility
- Minimal, spacious layouts with generous whitespace
- Semantic color usage for status and interactive states
- Smooth, subtle animations and transitions
- Developer-focused typography with monospace support
- Modular component structure for scalability
- Glassmorphic elements with soft shadows and borders
- Emphasis on code visibility and syntax clarity

## 2. Color Palette & Roles

### Primary
- **GitHub Dark Navy** (`#010409`): Primary background for dark theme layouts, hero sections, and full-page backgrounds
- **GitHub Charcoal** (`#1F2328`): Secondary dark background for nested containers and elevated surfaces
- **GitHub Mid-Dark** (`#25292E`): Tertiary dark background for further nesting and component backgrounds

### Accent Colors
- **GitHub Success Green** (`#1A7F37`): Primary call-to-action buttons, success states, and positive confirmations (inferred from sign-up button)
- **GitHub Blue** (`#1F6FEB`): Links, interactive elements, and secondary CTAs
- **GitHub Danger Red** (`#CF222E`): Error states, deletions, and destructive actions

### Interactive
- **GitHub Border Light** (`#D1D9E0`): Input borders, dividers, and subtle separators in light contexts
- **GitHub Border Medium** (`#B7BDC8`): Secondary borders and less prominent dividers
- **GitHub Ghost Transparent** (`#FFF0`): Transparent white overlay for hover states and subtle backgrounds

### Neutral Scale
- **Pure White** (`#FFFFFF`): Primary text, body content, and high-contrast elements (used 483 times)
- **Pure Black** (`#000000`): Text on light backgrounds and semantic dark elements (used 403 times)
- **Light Neutral** (`#F0F6FC`): Light theme background, code backgrounds, and low-emphasis surfaces
- **Subtle Gray** (`#59636E`): Secondary text, metadata, and disabled states
- **Medium Gray** (`#656C76`): Tertiary text and less prominent UI elements
- **Dark Gray** (`#58635B`): Used for dark theme secondary text and borders

### Surface & Borders
- **GitHub Surface Light** (`#E4EBE6`): Light theme card backgrounds and elevated surfaces
- **GitHub Surface Dark** (`#25292E`): Dark theme elevated surfaces above the base background

### Semantic / Status
- **Error State** (`#CF222E`): Validation errors, warnings, and destructive confirmations
- **Success State** (`#1A7F37`): Positive confirmations, successful operations (inferred)

## 3. Typography Rules

### Font Family
**Primary:** Mona Sans VF (variable font)
Fallback stack: `ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`

**Secondary:** Mona Sans (non-variable)
Fallback stack: `ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`

**Code:** `Menlo, monospace` (inferred for syntax highlighting contexts)

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display / H1 | Mona Sans VF | 32px | 600 | 48px | -0.02em | Hero headlines, page titles |
| Heading / H2 | Mona Sans VF | 24px | 600 | 36px | -0.01em | Section headings, major dividers |
| Subheading / H3 | Mona Sans VF | 12px | 600 | 19.5px | 0em | Small headings, labels, badges |
| Body Text | Mona Sans VF | 14px | 400 | 21px | 0em | Primary content, descriptions |
| Body List | Mona Sans | 16px | 400 | 24px | 0em | List items, narrative content |
| Button Text | Mona Sans VF | 16px | 400 | 24px | 0em | Button labels, actions |
| Button Label Weight | Mona Sans VF | 16px | 500 | 24px | 0em | Emphasized button states |
| Form Label | Mona Sans VF | 14px | 600 | 21px | 0em | Input labels, form fields |
| Caption / Small | Mona Sans VF | 12px | 400 | 18px | 0em | Metadata, helper text, timestamps |
| Code / Monospace | Menlo | 14px | 400 | 21px | 0em | Inline code, code blocks |

### Principles
- **Hierarchy by weight and size:** Use bold (600) weights for headings to establish visual priority
- **Line height comfort:** Generous line heights (1.5x–2x) support readability in long-form content
- **Monospace for code:** Developer-focused contexts use monospace typeface for syntax clarity
- **Font-size consistency:** Maintain specific px values for predictable scaling across breakpoints
- **Letter spacing restraint:** Avoid excessive tracking; use tight spacing for dense information

## 4. Component Stylings

### Buttons

**Primary Button (CTA)**
- Background: `#1A7F37`
- Text Color: `#FFFFFF`
- Font Size: `16px`
- Font Weight: `500`
- Font Family: `Mona Sans VF`
- Padding: `12px 24px`
- Border Radius: `6px`
- Border: `1px solid #1A7F37`
- Box Shadow: `none`
- Line Height: `24px`
- Hover State: Background `#228D41`, Box Shadow `rgba(37, 41, 46, 0.1) 0px 4px 8px -2px`
- Active State: Background `#0F5F2C`, Box Shadow `inset rgba(0, 0, 0, 0.2) 0px 2px 4px`

**Secondary Button**
- Background: `rgba(209, 217, 224, 0.1)`
- Text Color: `#FFFFFF`
- Font Size: `16px`
- Font Weight: `500`
- Font Family: `Mona Sans VF`
- Padding: `12px 24px`
- Border Radius: `6px`
- Border: `1px solid #D1D9E0`
- Box Shadow: `none`
- Line Height: `24px`
- Hover State: Background `rgba(209, 217, 224, 0.15)`, Border `#FFFFFF`
- Active State: Background `rgba(209, 217, 224, 0.25)`

**Ghost Button**
- Background: `rgba(0, 0, 0, 0)`
- Text Color: `#FFFFFF`
- Font Size: `16px`
- Font Weight: `400`
- Font Family: `Mona Sans VF`
- Padding: `8px 16px`
- Border Radius: `6px`
- Border: `1px solid #656C76`
- Box Shadow: `none`
- Line Height: `24px`
- Hover State: Background `rgba(255, 255, 255, 0.1)`, Border `#FFFFFF`
- Active State: Background `rgba(255, 255, 255, 0.2)`

**Small Icon Button**
- Background: `rgba(0, 0, 0, 0)`
- Text Color: `#FFFFFF`
- Font Size: `16px`
- Font Weight: `500`
- Font Family: `Mona Sans VF`
- Padding: `4px 4px`
- Border Radius: `6px`
- Border: `0px none`
- Box Shadow: `none`
- Line Height: `24px`
- Hover State: Background `rgba(255, 255, 255, 0.1)`

### Cards & Containers

**Standard Card (Dark)**
- Background: `#1F2328`
- Text Color: `#FFFFFF`
- Font Size: `14px`
- Font Weight: `400`
- Font Family: `Mona Sans VF`
- Padding: `16px`
- Border Radius: `6px`
- Border: `1px solid #656C76`
- Box Shadow: `rgba(209, 217, 224, 0.25) 0px 0px 0px 1px, rgba(37, 41, 46, 0.04) 0px 6px 12px -3px, rgba(37, 41, 46, 0.12) 0px 6px 18px 0px`
- Line Height: `21px`

**Elevated Card**
- Background: `#25292E`
- Text Color: `#FFFFFF`
- Font Size: `14px`
- Font Weight: `400`
- Font Family: `Mona Sans VF`
- Padding: `24px`
- Border Radius: `8px`
- Border: `1px solid rgba(209, 217, 224, 0.1)`
- Box Shadow: `rgba(209, 217, 224, 0) 0px 0px 0px 1px, rgba(37, 41, 46, 0.24) 0px 40px 80px 0px`
- Line Height: `21px`

**Code Block Container**
- Background: `#0F1419`
- Text Color: `#C5CED1`
- Font Size: `14px`
- Font Weight: `400`
- Font Family: `Menlo, monospace`
- Padding: `16px`
- Border Radius: `6px`
- Border: `1px solid #656C76`
- Box Shadow: `rgba(37, 41, 46, 0.04) 0px 1px 0px 0px inset`
- Line Height: `21px`

### Inputs & Forms

**Text Input**
- Background: `#0F1419`
- Text Color: `#FFFFFF`
- Font Size: `14px`
- Font Weight: `400`
- Font Family: `Mona Sans VF`
- Padding: `8px 12px`
- Border Radius: `6px`
- Border: `1px solid #656C76`
- Box Shadow: `rgba(31, 35, 40, 0.04) 0px 1px 0px 0px inset`
- Height: `32px`
- Line Height: `21px`
- Placeholder Color: `#59636E`
- Focus State: Border `#1F6FEB`, Box Shadow `0px 0px 0px 3px rgba(31, 111, 235, 0.3)`

**Text Area**
- Background: `#FFFFFF`
- Text Color: `#1F2328`
- Font Size: `14px`
- Font Weight: `400`
- Font Family: `Mona Sans VF`
- Padding: `8px 12px`
- Border Radius: `6px`
- Border: `1px solid #D1D9E0`
- Box Shadow: `rgba(31, 35, 40, 0.04) 0px 1px 0px 0px inset`
- Height: `auto` (minimum 120px)
- Line Height: `21px`
- Resize: `vertical`
- Focus State: Border `#1F6FEB`, Box Shadow `0px 0px 0px 3px rgba(31, 111, 235, 0.2)`

**Search Input**
- Background: `#0F1419`
- Text Color: `#FFFFFF`
- Font Size: `14px`
- Font Weight: `400`
- Font Family: `Mona Sans VF`
- Padding: `5px 12px`
- Border Radius: `6px`
- Border: `1px solid #656C76`
- Box Shadow: `rgba(31, 35, 40, 0.04) 0px 1px 0px 0px inset`
- Height: `32px`
- Width: `300px` (responsive)
- Line Height: `20px`
- Placeholder Color: `#59636E`

**Form Label**
- Color: `#E4EBE6`
- Font Size: `12px`
- Font Weight: `600`
- Font Family: `Mona Sans VF`
- Margin Bottom: `6px`
- Line Height: `18px`

### Navigation

**Primary Navigation**
- Background: `rgba(1, 4, 9, 0.8)` (semi-transparent dark)
- Text Color: `#FFFFFF`
- Font Size: `16px`
- Font Weight: `400`
- Font Family: `Mona Sans`
- Padding: `0px` (inline items spaced)
- Gap Between Items: `24px`
- Height: `64px`
- Line Height: `24px`
- Border Bottom: `1px solid rgba(209, 217, 224, 0.1)`
- Item Hover State: Text Color `#FFFFFF`, Background `rgba(255, 255, 255, 0.1)`
- Item Active State: Text Color `#1F6FEB`, Border Bottom `2px solid #1F6FEB`

**Nav Item Link**
- Background: `rgba(0, 0, 0, 0)`
- Text Color: `#FFFFFF`
- Font Size: `14px`
- Font Weight: `400`
- Font Family: `Mona Sans VF`
- Padding: `8px 12px`
- Border Radius: `6px`
- Border: `1px solid transparent`
- Line Height: `21px`
- Hover State: Background `rgba(209, 217, 224, 0.1)`, Border `1px solid #D1D9E0`

### Badges & Labels

**Badge / Tag (Default)**
- Background: `rgba(209, 217, 224, 0.15)`
- Text Color: `#FFFFFF`
- Font Size: `12px`
- Font Weight: `600`
- Font Family: `Mona Sans VF`
- Padding: `4px 8px`
- Border Radius: `20px`
- Border: `1px solid rgba(209, 217, 224, 0.3)`
- Line Height: `16px`

**Badge / Status Green**
- Background: `rgba(26, 127, 55, 0.15)`
- Text Color: `#58E84D`
- Font Size: `12px`
- Font Weight: `600`
- Font Family: `Mona Sans VF`
- Padding: `4px 8px`
- Border Radius: `20px`
- Border: `1px solid rgba(26, 127, 55, 0.3)`
- Line Height: `16px`

**Badge / Status Red**
- Background: `rgba(207, 34, 46, 0.15)`
- Text Color: `#F85149`
- Font Size: `12px`
- Font Weight: `600`
- Font Family: `Mona Sans VF`
- Padding: `4px 8px`
- Border Radius: `20px`
- Border: `1px solid rgba(207, 34, 46, 0.3)`
- Line Height: `16px`

### Tabs

**Tab Container**
- Background: `rgba(0, 0, 0, 0)`
- Border Bottom: `1px solid #656C76`
- Height: `auto`

**Tab Item (Inactive)**
- Background: `rgba(0, 0, 0, 0)`
- Text Color: `#59636E`
- Font Size: `14px`
- Font Weight: `500`
- Font Family: `Mona Sans VF`
- Padding: `12px 16px`
- Border Bottom: `2px solid transparent`
- Line Height: `21px`
- Hover State: Text Color `#FFFFFF`

**Tab Item (Active)**
- Background: `rgba(0, 0, 0, 0)`
- Text Color: `#FFFFFF`
- Font Size: `14px`
- Font Weight: `500`
- Font Family: `Mona Sans VF`
- Padding: `12px 16px`
- Border Bottom: `2px solid #1F6FEB`
- Line Height: `21px`

## 5. Layout Principles

### Spacing System
**Base Unit:** `4px`

**Spacing Scale:**
- `4px` — Micro spacing within components, icon-text gaps
- `8px` — Small gaps between related elements, tight component padding
- `12px` — Form field padding, button interior spacing
- `16px` — Default padding, section separators
- `20px` — Medium gaps between content blocks
- `24px` — Gap between major sections, card spacing
- `32px` — Large padding for prominent containers
- `40px` — Vertical spacing between sections
- `48px` — Extra-large vertical rhythm
- `64px` — Full section padding, hero spacing
- `80px` — Large feature block spacing
- `96px` — Maximum spacing between unrelated sections

**Usage Context:**
- Micro (4px–8px): Icon and button internals
- Standard (12px–16px): Default padding, form inputs
- Medium (20px–32px): Card and component spacing
- Large (40px–80px): Section and page-level spacing

### Grid & Container
**Max Width:** `1280px` for primary content, `100%` for edge-to-edge sections

**Column Strategy:**
- Desktop (1280px+): 12-column grid, `96px` columns with `24px` gutters
- Tablet (768px–1024px): 8-column grid, `72px` columns with `16px` gutters
- Mobile (<768px): Single column, `100%` width with `16px` side margins

**Section Patterns:**
- Hero section: Full viewport width, centered content max-width with `80px` vertical padding
- Feature section: Alternating layout (50/50 split on desktop, stacked on mobile)
- Card grid: 3-column on desktop, 2 on tablet, 1 on mobile, with `24px` gap
- Sidebar layout: 70/30 split with `32px` gap

### Whitespace Philosophy
GitHub prioritizes breathing room and visual clarity through generous whitespace. The design avoids clustering; related elements are grouped with `16px–24px` spacing, while unrelated sections use `40px–80px` separation. This creates natural visual hierarchy and reduces cognitive load for users scanning long pages or reading code. Dark backgrounds amplify the effect of whitespace, making content feel more spacious and less overwhelming.

### Border Radius Scale
- `3px` — Minimal rounding for compact buttons and badges
- `6px` — Standard radius for inputs, cards, and interactive elements
- `8px` — Elevated cards and larger containers
- `16px` — Feature images, large asset elements, hero overlays
- `20px` — Pill-shaped buttons and tag containers
- `60px` — Full-circle avatars, fully rounded badges

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Base (0) | No shadow, `background-color` only | Page backgrounds, content areas |
| Raised (1) | `rgba(209, 217, 224, 0.25) 0px 0px 0px 1px, rgba(37, 41, 46, 0.04) 0px 6px 12px -3px, rgba(37, 41, 46, 0.12) 0px 6px 18px 0px` | Dropdown menus, hover cards, tooltips |
| Lifted (2) | `rgba(209, 217, 224, 0) 0px 0px 0px 1px, rgba(37, 41, 46, 0.24) 0px 40px 80px 0px` | Modal dialogs, popovers, overlay cards |
| Floating (3) | Custom: `0px 20px 60px rgba(37, 41, 46, 0.35), 0px 0px 0px 1px rgba(209, 217, 224, 0.2)` | Toast notifications, floating action buttons |

**Shadow Philosophy:**
GitHub's shadow system balances subtlety with clarity. Shadows are used sparingly to indicate elevation and focus, never applied to base backgrounds. The color palette—using dark gray overlaid on the background—ensures shadows remain visible in dark mode without appearing jarring. Blur and spread values increase proportionally with elevation, creating depth without harshness. Borders (1px light or semi-transparent) complement shadows to ensure contrast against dark backgrounds.

## 7. Do's and Don'ts

### Do
- Use the semantic color palette for status (green for success, red for error, blue for links)
- Apply shadows only to interactive or elevated components, never to base surfaces
- Maintain at least `44px` height for interactive touch targets on mobile
- Use Mona Sans VF for interface text and Menlo for code blocks
- Provide at least 3:1 contrast ratio for body text (`#FFFFFF` on `#1F2328` achieves 11:1)
- Group related inputs with `12px` vertical spacing
- Place form labels above inputs, not inside placeholders
- Use the `6px` border radius for standard buttons and inputs
- Combine hover, active, and focus states for all interactive elements
- Reserve the success green (`#1A7F37`) exclusively for primary CTAs and confirmations

### Don't
- Avoid applying multiple shadow levels to a single element
- Don't use red (`#CF222E`) for neutral feedback; reserve it for errors and destructive actions
- Avoid thin fonts (weight <400) for body text; maintain 400 or 600 weights
- Don't truncate text without providing a tooltip or expansion mechanism
- Avoid nesting dark containers more than 3 levels deep (`#010409` → `#1F2328` → `#25292E`)
- Don't place text smaller than `12px` without explicit accessibility review
- Avoid using the full `#000000` black on dark backgrounds; use neutrals from the scale instead
- Don't disable form fields without explanation; use a disabled state with helper text
- Avoid mixing dark and light theme colors in the same component
- Don't apply more than `2px` borders; use `1px` as the standard

## 8. Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|------------|
| Mobile | <576px | Single-column layout, full-width containers, `16px` side margin, stacked navigation, `14px` body text |
| Tablet | 576px–768px | Two-column layout for grids, `20px` side padding, condensed navigation, `16px` line height |
| Small Desktop | 768px–1024px | Three-column grids, `32px` side padding, sidebar layouts enabled, standard typography |
| Desktop | 1024px–1280px | Four-column grids, `48px` side padding, full navigation, max-width containers |
| Large Desktop | >1280px | Full 12-column grid, `64px` side padding, multi-section layouts, max-width `1280px` for content |

### Touch Targets
- **Minimum Height:** `44px` for buttons, links, and form controls
- **Minimum Width:** `44px` for circular buttons and icon buttons
- **Tap Spacing:** `8px` minimum gap between adjacent touch targets on mobile
- **Hover Targets on Desktop:** `40px` height acceptable for non-critical actions (secondary buttons, navigation items)
- **Form Fields:** Minimum `32px` height for inputs, minimum `12px` padding on all sides

### Collapsing Strategy
- **Hero sections:** Full viewport width on all breakpoints; padding reduces from `80px` (desktop) to `48px` (tablet) to `32px` (mobile)
- **Grids:** 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile), maintaining `24px` gap
- **Navigation:** Horizontal bar (desktop/tablet) → hamburger menu (mobile, `<768px`)
- **Sidebars:** Side-by-side 70/30 (desktop) → stacked full-width (tablet/mobile)
- **Cards:** Two-column on desktop → single column on mobile, width `100%` in narrow viewports
- **Typography:** `32px` H1 (desktop) → `24px` (tablet) → `20px` (mobile)
- **Padding:** `32px` horizontal (desktop) → `24px` (tablet) → `16px` (mobile)
- **Images:** Max-width `100%`, scale proportionally, border-radius `16px` maintained across breakpoints

## 9. Agent Prompt Guide

### Quick Color Reference
- **Primary CTA:** Success Green (`#1A7F37`)
- **Secondary CTA:** GitHub Blue (`#1F6FEB`)
- **Destructive Action:** Danger Red (`#CF222E`)
- **Page Background:** GitHub Dark Navy (`#010409`)
- **Card Background:** GitHub Charcoal (`#1F2328`)
- **Body Text:** Pure White (`#FFFFFF`)
- **Secondary Text:** Subtle Gray (`#59636E`)
- **Input Background:** GitHub Dark Navy variant (`#0F1419`)
- **Border Color:** GitHub Border Light (`#D1D9E0`) or Medium Gray (`#656C76`)
- **Hover State Overlay:** `rgba(255, 255, 255, 0.1)` on dark backgrounds

### Iteration Guide
1. **Always use semantic colors first:** Map button/status intent to the color palette (CTA = green, link = blue, error = red) before applying custom values
2. **Maintain contrast compliance:** Ensure minimum 3:1 ratio for secondary text; 4.5:1 for body; test all text on both dark (`#1F2328`) and light (`#FFFFFF`) backgrounds
3. **Apply shadows consistently:** Use the three shadow levels (Raised, Lifted, Floating) only; never create custom shadows without documented purpose
4. **Establish rhythm with spacing:** Use the `4px` base unit; gaps between elements should always be multiples of 4 (8px, 12px, 16px, 20px, 24px, etc.)
5. **Border radius depends on intent:** `6px` for standard UI (buttons, inputs, cards); `20px` for pills/tags; `16px` for images; `3px` for minimal/compact elements
6. **Prioritize touch accessibility:** Every interactive element must be at least `44px` height/width on mobile; maintain `8px` minimum gap between targets
7. **Font hierarchy by weight:** Use `600` weight for all headings (H1–H3); use `400` for body and `500` for button labels; never use weights outside 400–600 range for primary text
8. **Dark theme default:** Design for dark backgrounds first; ensure light theme variants have sufficient contrast with `#FFFFFF` or `#F0F6FC` backgrounds
9. **Responsive collapse order:** Hero → grid collapse → navigation hamburger → sidebar stack; test at 576px, 768px, 1024px, and 1280px breakpoints
10. **Code context uses monospace:** Any content representing code (inline code, code blocks, file trees) must use Menlo or monospace fallback, never Mona Sans, with `14px` size minimum