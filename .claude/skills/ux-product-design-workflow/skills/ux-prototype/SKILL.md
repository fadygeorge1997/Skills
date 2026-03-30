---
name: ux-prototype
description: >
  Phase 4 of the UX & Product Design workflow. Guides high-fidelity prototyping,
  design system integration, Laws of UX application, RTL/MENA patterns, and
  micro-interaction design. Transforms wireframes into polished, testable interfaces.

  Use this skill when: creating high-fidelity designs, applying UX laws, building
  prototypes, designing micro-interactions, implementing design systems, or
  designing for RTL/Arabic markets.
---

# Phase 4: Prototyping & Laws of UX

## Overview

**Goal:** Transform wireframes into polished, testable interfaces using established psychological principles.

**Duration:** 2-4 weeks typically

**When to move on:** The prototype feels real enough that users can give meaningful feedback, and the design system is documented enough that engineers can build from it.

---

## Input Requirements

From Phase 3 (IA):
- [ ] Sitemap with navigation structure
- [ ] User flows with decision points
- [ ] State inventories (all 8 content states from Phase 3)
- [ ] Wireframe descriptions
- [ ] Card sorting validation results (if conducted)

**If Phase 3 artifacts don't exist:** Warn user that prototypes may not address user mental models.

---

## Phase Checklist

### 1. Laws of UX Application
- [ ] Apply Fitts's Law to primary CTAs
- [ ] Apply Hick's Law to navigation and choices
- [ ] Apply Jakob's Law for conventions
- [ ] Apply Doherty Threshold for responsiveness
- [ ] Apply Miller's Law for chunking
- [ ] Apply Peak-End Rule for completion moments
- [ ] Apply Zeigarnik Effect for progress
- [ ] Apply Aesthetic-Usability Effect for trust

### 2. Design System Integration
- [ ] Map primitive tokens (colors, spacing, typography)
- [ ] Define semantic tokens (bg-primary, spacing-section)
- [ ] Document component tokens (button-bg, card-padding)
- [ ] Ensure Figma-code naming consistency

### 3. High-Fidelity Design
- [ ] Create realistic content (no Lorem Ipsum)
- [ ] Design all interaction states (default, hover, active, focus, disabled) per interactive element
- [ ] Refine all 8 content states at high fidelity (default, empty, loading, partial, error, success, offline, permission)
- [ ] Apply micro-interactions purposefully
- [ ] Implement responsive breakpoints
- [ ] Consider RTL/MENA if applicable

### 4. Prototype Creation
- [ ] Build interactive prototype for key flows
- [ ] Include error states and edge cases
- [ ] Add realistic delays and transitions
- [ ] Prepare for user testing

### 5. Self-Review
- [ ] Nielsen's 10 heuristic review
- [ ] Ethical Design Hierarchy check
- [ ] Accessibility self-audit (WCAG 2.1 AA)
- [ ] Performance considerations

---

## Deliverables

| Artifact | Format | Template |
|----------|--------|----------|
| High-Fidelity Designs | Annotated mockups | Design tool output |
| Design Token Documentation | Token definitions | Design system |
| Micro-interaction Specs | Timing + easing docs | Generated during phase |
| Responsive Rules | Breakpoint behavior | Documentation |
| Interactive Prototype | Clickable flow | Prototype tool |
| Heuristic Self-Check | Completed checklist | Generated during phase |

---

## Laws of UX Application Guide

### Fitts's Law
> Bigger + closer = faster to tap

**Application:**
- Primary CTAs: minimum 44x44px touch target
- Place frequently used actions in thumb zone
- Increase hit area beyond visible element

**Example:**
```
✓ "Pay Now" button: 48x48dp minimum, positioned in bottom thumb zone
✗ Small text links clustered at screen top
```

### Hick's Law
> More choices = slower decisions

**Application:**
- Maximum 5-7 navigation items per level
- Progressive disclosure for complex features
- Group related options, hide advanced

**Example:**
```
✓ Primary nav: Home, Send, Pay, History, Profile (5 items)
✗ All 15 features visible in main navigation
```

### Jakob's Law
> Users expect your site to work like others they know

**Application:**
- Use platform conventions (iOS HIG, Material Design)
- Don't reinvent search, navigation, or forms
- Match competitor patterns users already know

**Example:**
```
✓ Standard tab bar navigation on mobile
✗ Custom gesture-based navigation requiring learning
```

### Doherty Threshold
> <300ms response feels instant

**Application:**
- Skeleton screens during loading
- Optimistic UI updates
- Preload predicted next screens
- Progress bars for longer operations

**Example:**
```
✓ Show skeleton cards while data loads, then fade in content
✗ Blank screen for 2 seconds, then content appears
```

### Miller's Law
> Working memory holds ~7 items

**Application:**
- Chunk form fields into groups
- Break long lists into pages
- Use cards to group related information

**Example:**
```
✓ Checkout: Contact (3 fields) → Shipping (4 fields) → Payment (4 fields)
✗ Single form with 15 sequential fields
```

### Peak-End Rule
> Memory = peak moment + final moment

**Application:**
- Design delight at completion
- Never end flows on error states
- Celebrate achievements

**Example:**
```
✓ Transaction success: Confirmation animation + receipt + "You saved 15 minutes!"
✗ Success screen: Dry confirmation with no next step
```

### Zeigarnik Effect
> Incomplete tasks nag the mind

**Application:**
- Progress bars for multi-step flows
- "3 of 5 steps complete" messaging
- Save drafts automatically

**Example:**
```
✓ Profile completion: "Your profile is 70% complete. Add photo to finish."
✗ No indication of profile completeness
```

### Aesthetic-Usability Effect
> Beautiful = perceived as more usable

**Application:**
- Polish builds trust (especially fintech)
- Consistent spacing and typography
- Professional imagery and icons

**Example:**
```
✓ Consistent 8px grid, aligned elements, quality iconography
✗ Misaligned elements, inconsistent spacing, generic icons
```

---

## Design Token Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    COMPONENT TOKENS                         │
│  button-bg-primary: bg-primary                               │
│  button-border-radius: border-radius-md                      │
│  card-padding: spacing-section                               │
├─────────────────────────────────────────────────────────────┤
│                    SEMANTIC TOKENS                           │
│  bg-primary: color-brand-500                                 │
│  text-primary: color-neutral-900                             │
│  spacing-section: spacing-8                                  │
├─────────────────────────────────────────────────────────────┤
│                    PRIMITIVE TOKENS                          │
│  color-brand-500: #3B82F6                                    │
│  spacing-8: 32px                                             │
│  border-radius-md: 8px                                       │
└─────────────────────────────────────────────────────────────┘
```

---

## RTL/MENA Patterns

### Layout Mirroring Rules

| Element | LTR Behavior | RTL Behavior |
|---------|-------------|--------------|
| Navigation | Left-aligned | Right-aligned |
| Back arrow | Points left | Points right |
| Progress bars | Fill left-to-right | Fill right-to-left |
| Checkmarks | Left of text | Right of text |
| Submenus | Open rightward | Open leftward |

### Text Handling
- Arabic text: Right-aligned, larger line-height (1.8-2.0x)
- Numbers: Remain LTR (phone, prices, math)
- Mixed content: Use proper BiDi isolation

### Typography
- **Recommended fonts:** Cairo, Tajawal, IBM Plex Arabic, Noto Sans Arabic
- Arabic renders smaller at same point size — increase by ~10%
- Line height needs adjustment for connected cursive script

### Fintech Trust Patterns

| Pattern | Implementation |
|---------|----------------|
| Intent-based navigation | "Send Money," "Pay Bills" — not "Products" |
| Fee transparency | Show all fees before commitment |
| Receipt confirmation | Downloadable, shareable receipts |
| Biometric auth | Primary, not secondary |
| Security indicators | Visible but not intrusive |
| Transaction status | Clear, real-time updates |

---

## Micro-Interaction Design

### Structure
```
Trigger → Action → Animation → Feedback
```

### Documentation Template

```markdown
# Micro-Interaction: [Name]

## Trigger
- [What initiates the interaction]

## Action
- [What the user does]

## Animation
- Duration: [ms]
- Easing: [ease-out/spring/etc]
- Properties: [opacity, transform, etc]

## Feedback
- [What the user sees/hears/feels]

## Purpose
- [Why this micro-interaction exists]
- [Which Law of UX it supports]
```

---

## Nielsen's 10 Heuristics Self-Check

| # | Heuristic | Status | Notes |
|---|-----------|--------|-------|
| 1 | Visibility of system status | ✓/✗ | [Findings] |
| 2 | Match between system and real world | ✓/✗ | [Findings] |
| 3 | User control and freedom | ✓/✗ | [Findings] |
| 4 | Consistency and standards | ✓/✗ | [Findings] |
| 5 | Error prevention | ✓/✗ | [Findings] |
| 6 | Recognition rather than recall | ✓/✗ | [Findings] |
| 7 | Flexibility and efficiency | ✓/✗ | [Findings] |
| 8 | Aesthetic and minimalist design | ✓/✗ | [Findings] |
| 9 | Help users recognize and recover from errors | ✓/✗ | [Findings] |
| 10 | Help and documentation | ✓/✗ | [Findings] |

---

## Ethical Design Hierarchy Check

| Level | Status | Evidence |
|-------|--------|----------|
| **1. Human Rights** | ✓/✗ | [Accessibility, privacy, security, inclusivity verified] |
| **2. Functionality** | ✓/✗ | [Usability, performance, reliability verified] |
| **3. Delight** | ✓/✗ | [Pursued only when 1-2 are solid] |

**Rule:** Never sacrifice Level 1 for Level 2, or Level 2 for Level 3.

---

## Anti-Patterns to Avoid

### Form Over Function
- **Problem:** Beautiful design that ignores accessibility
- **Solution:** WCAG compliance before aesthetic polish

### Inconsistent Patterns
- **Problem:** Different interactions for same action across screens
- **Solution:** Document patterns, use design system

### Ignoring Platform Conventions
- **Problem:** Custom patterns that fight user expectations
- **Solution:** Follow platform guidelines (iOS HIG, Material Design)

### Over-Animation
- **Problem:** Animations that slow users down or serve no functional purpose
- **Solution:** Every animation must serve one of: guide attention, confirm action, or show state change. All animations should respect `prefers-reduced-motion`.

### Design Tokens Without Semantic Layer
- **Problem:** Going straight from primitive tokens to component tokens skips the semantic layer that enables theming and consistency.
- **Solution:** Always define the 3-layer hierarchy: primitive → semantic → component. Semantic tokens (e.g., `bg-primary`) create the abstraction layer needed for dark mode, theming, and design system evolution.

### Lorem Ipsum in Prototypes
- **Problem:** Placeholder text masks content-driven design issues (truncation, line breaks, localization).
- **Solution:** Use realistic content from actual use cases. For Arabic/RTL, test with real Arabic strings — not transliterated Latin characters.

---

## Quality Criteria

A prototype is testable when: (1) realistic content replaces all placeholder text, (2) all 5 interaction states are designed per interactive element, (3) all 8 content states are refined at high fidelity, (4) at least one core flow is fully interactive end-to-end, (5) Nielsen's 10 heuristic self-check is completed with no severity-4 issues.

---

## Definition of Done

Phase 4 is complete when:

- [ ] Laws of UX applied as concrete design actions (documented)
- [ ] Design system token mapping complete (primitive > semantic > component)
- [ ] High-fidelity designs for all key screens with realistic content
- [ ] All 5 interaction states designed per element (default, hover, active, focus, disabled)
- [ ] All 8 content states refined at high fidelity (from Phase 3 state inventory)
- [ ] Micro-interaction specs documented with timing and purpose
- [ ] Responsive behavior rules per breakpoint documented
- [ ] RTL/MENA patterns applied (if applicable)
- [ ] Nielsen's 10 heuristic self-check completed
- [ ] Ethical Design Hierarchy check passed
- [ ] WCAG 2.1 AA accessibility self-audit completed
- [ ] Interactive prototype ready for testing

---

## Cross-Phase References

**Input from Phase 3:**
- Wireframes → High-fidelity design base
- State inventories → Interaction state designs
- User flows → Prototype flow structure

**Output feeds into:**
- Phase 5 (Validate): Prototype for usability testing
- Phase 5 (Validate): Heuristic evaluation checklist
- Phase 6 (Handoff): Design token documentation

---

## Context-Adaptive Depth

| Mode | Fidelity | Design System | Documentation |
|------|----------|---------------|---------------|
| **MVP** | Key screens only | Basic tokens | Essential annotations |
| **Growth** | All core screens | Standard tokens | Full component docs |
| **Enterprise** | All screens + variants | Complete token system | Comprehensive design system |

---

## Templates Used

- `templates/heuristic-evaluation-template.md` (partial for self-check)
- Design token documentation (design system)

---

## Next Phase

When Definition of Done is complete, proceed to:
> `skills/ux-validate/SKILL.md` — Phase 5: Validation & Usability Testing
