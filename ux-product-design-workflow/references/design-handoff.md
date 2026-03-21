# Design Handoff & Development Collaboration

## Table of Contents
1. [The Staggered Sprint Pipeline](#the-staggered-sprint-pipeline)
2. [Handoff Documentation Standards](#handoff-documentation-standards)
3. [Design QA Process](#design-qa-process)
4. [Component Documentation](#component-documentation)
5. [Responsive Specification Format](#responsive-specification-format)
6. [Edge Case Catalog](#edge-case-catalog)
7. [Collaboration Anti-Patterns](#collaboration-anti-patterns)

---

## The Staggered Sprint Pipeline

UX work runs 1-2 sprints ahead of engineering to prevent bottlenecks and ensure designs are validated before development starts.

### Sprint Timeline

```
Sprint N-2 (UX Research)
├── User research for upcoming features
├── Problem validation and concept exploration
├── Initial wireframes and flow exploration
└── Output: Research insights, validated problems, concept directions

Sprint N-1 (UX Design)
├── Detailed high-fidelity design
├── Prototype development
├── Usability testing and iteration
├── Design system updates if needed
└── Output: Validated designs ready for handoff

Sprint N (Engineering)
├── Implement Sprint N-1 designs
├── UX attends standups and reviews
├── Design QA during development
├── Real-time edge case resolution
└── Output: Shipped feature, design QA sign-off

Sprint N+1 (UX next cycle)
├── UX is already 2 sprints ahead on next features
├── Post-launch monitoring of Sprint N feature
└── Quick-fix designs for any issues found in Sprint N
```

### Sprint Ceremony Participation

| Ceremony | UX Role | Why It Matters |
|----------|---------|---------------|
| **Sprint Planning** | Present validated designs, answer questions, scope complexity | Engineers understand context, not just specs |
| **Daily Standup** | Flag design decisions needed, review in-progress implementation | Catch misinterpretations early |
| **Sprint Review** | Demo alongside engineering, present upcoming designs | Stakeholders see design-dev alignment |
| **Retrospective** | Surface collaboration friction, suggest process improvements | Continuous improvement of the handoff itself |

---

## Handoff Documentation Standards

### What to Document

Every handoff package should include these layers, from overview to detail:

**Layer 1: Context (the "why")**
- User story or JTBD this feature addresses
- Key research findings that drove design decisions
- Link to the problem statement and success metrics
- What the user should feel at each step

**Layer 2: Flow (the "what")**
- User flow diagram showing all paths (happy path, errors, edge cases)
- Screen inventory: every unique screen state
- Entry points: how users reach this feature
- Exit points: where they go after

**Layer 3: Specification (the "how")**
- Component list with design token references
- Spacing, typography, and color values using token names (not raw values)
- Interaction specifications: transitions, animations, timing
- State documentation: default, hover, active, focus, disabled, error, loading, success
- Responsive behavior rules per breakpoint

**Layer 4: Edge Cases (the "what if")**
- Empty states: what to show when there's no data
- Error states: what to show when things fail
- Boundary conditions: max character counts, overflow behavior, extreme data
- Offline behavior: cached vs. unavailable
- Permission states: what to show when access is restricted

### Annotation Best Practices

- Annotate directly on the design file (Figma, etc.), not in separate documents
- Use numbered callouts for complex interactions
- Include "why" annotations, not just "what": "This confirmation step exists because user testing showed 43% drop-off without it"
- Link to relevant usability test findings
- Flag decisions that are still open or need engineering input

### Design Specification Template

For each screen/flow in the handoff:

```
## Screen: [Screen Name]

### User Story
As a [persona], I want to [action] so that [outcome].

### Acceptance Criteria
Given [precondition]
When [user action]
Then [expected result]

Example:
Given the user has entered a valid amount and recipient
When they tap "Send Money"
Then:
  - A loading spinner replaces the button text
  - The transaction processes within 5 seconds
  - On success: confirmation screen with receipt number, amount, recipient, timestamp
  - On failure: error message with retry button, amount and recipient preserved
  - The user's balance updates immediately (optimistic UI, reconciled on server response)

### Component Inventory
| Component | Token Reference | Notes |
|-----------|----------------|-------|
| Header bar | nav-header-default | Sticky, elevation-2 |
| Amount input | input-currency-lg | Right-aligned for Arabic, left for LTR |
| Send button | button-primary-lg | Disabled until validation passes |
| Fee disclosure | text-caption-muted | Updates dynamically based on amount |

### Interaction Specs
| Trigger | Animation | Duration | Easing |
|---------|-----------|----------|--------|
| Button tap | Scale down 0.97x | 100ms | ease-out |
| Screen transition | Slide left (LTR) / right (RTL) | 300ms | ease-in-out |
| Success state | Checkmark draw animation | 600ms | spring |
| Error state | Shake + red border | 400ms | ease-out |

### States
- Default: Amount field focused, send button disabled
- Valid: Send button enabled, fee preview visible
- Loading: Button shows spinner, inputs disabled
- Success: Confirmation card with receipt details
- Error: Inline error message, retry button, form data preserved
- Offline: Queue indicator, "Will send when connected" message
```

### Acceptance Criteria Format

Use the **Given-When-Then** (Gherkin) format for testable acceptance criteria:

```
Feature: [Feature Name]

Scenario: Happy path
  Given [user state/precondition]
  When [user performs action]
  Then [observable outcome]
  And [additional outcome]

Scenario: Error path
  Given [user state/precondition]
  When [user performs action incorrectly]
  Then [error handling behavior]
  And [recovery option available]

Scenario: Edge case
  Given [unusual state]
  When [user performs action]
  Then [graceful handling]
```

**Rules for writing good acceptance criteria:**
- Each criterion must be independently testable
- Use specific, measurable language (not "the page loads quickly" → "the page renders within 400ms")
- Cover: happy path, error paths, edge cases, accessibility, and responsive behavior
- Include performance expectations where relevant
- Reference specific design tokens and component names

### Worked Example: Handoff Artifact — Send Money Confirmation Screen

**Screen:** Send Money — Confirmation
**Feature:** P2P Money Transfer
**Designer:** Nour A. | **Sprint:** Sprint 14 | **Last updated:** 2025-02-10

**User Story:**
As Mariam (first-time sender), I want to see a clear confirmation after sending money so I know the transfer succeeded and can show proof to the recipient.

**Acceptance Criteria:**

```
Scenario: Successful transfer
  Given Mariam has entered a valid amount (500 EGP) and recipient (Mama)
  When the transfer completes successfully
  Then:
    - Confirmation screen appears within 200ms of server response
    - Green checkmark animation plays (600ms, spring easing)
    - Receipt shows: amount, recipient name, timestamp, reference number
    - "Share Receipt" button is visible (primary action)
    - "Done" button returns to home screen
    - Push notification sent to Mariam
    - SMS sent to recipient's phone number within 30 seconds

Scenario: Transfer fails after submission
  Given Mariam has tapped "Send 500 EGP to Mama"
  When the server returns an error (timeout, insufficient funds, etc.)
  Then:
    - Error message in Egyptian Arabic explains the problem
    - Amount and recipient are preserved (no re-entry needed)
    - "Try Again" button retries with same parameters
    - If insufficient funds: show current balance and shortfall amount
```

**Component Inventory:**

| Component | Token | Specs |
|-----------|-------|-------|
| Success icon | icon-check-circle | 64px, color: semantic-success, draw animation 600ms |
| Amount display | text-display-lg | Font: Cairo Bold 32px, color: text-primary |
| Recipient name | text-body-lg | Font: Cairo Regular 18px, color: text-secondary |
| Reference number | text-mono-sm | Font: IBM Plex Mono 14px, color: text-muted, tap-to-copy |
| Share Receipt button | button-primary-lg | Full width, height 48px, margin-top: spacing-6 |
| Done button | button-ghost-lg | Full width, height 48px, margin-top: spacing-3 |

**Interaction Specs:**

| Trigger | Animation | Duration | Easing |
|---------|-----------|----------|--------|
| Screen entry | Fade in + slide up 20px | 300ms | ease-out |
| Checkmark | SVG path draw | 600ms | spring(1, 80, 10) |
| Amount | Counter from 0 to final amount | 400ms | ease-out |
| Share button tap | Scale 0.97x → 1x | 100ms | ease-out |
| Tap reference number | Copy toast appears bottom-center | 200ms in, 2000ms visible, 200ms out | ease-in-out |

**Edge Cases:**

| Condition | Behavior |
|-----------|----------|
| Reference number is 20+ chars | Truncate middle with ellipsis, full number in tap-to-copy |
| Recipient has no name saved | Show phone number formatted: +20 1XX XXX XXXX |
| User backgrounds app during transfer | Resume shows confirmation or error, never a blank state |
| Screenshot taken | No restriction; receipt is designed to be screenshot-friendly |
| Amount is 0.50 EGP | Display "0.50 EGP" (always show 2 decimal places) |

---

## Design QA Process

Design QA happens during development, not after. The designer reviews implementation against design specs continuously.

### QA Checklist

**Visual Fidelity**
- [ ] Colors match design tokens (check both light and dark modes if applicable)
- [ ] Typography: font family, size, weight, line-height, letter-spacing
- [ ] Spacing: padding, margins, gaps match token values
- [ ] Border radius, shadows, and elevation match specs
- [ ] Icons: correct icon, correct size, correct color

**Interaction Fidelity**
- [ ] All states implemented: hover, active, focus, disabled, error, loading
- [ ] Transitions and animations match specs (timing, easing)
- [ ] Keyboard navigation works logically
- [ ] Focus indicators are visible
- [ ] Touch targets meet minimum size requirements (44px iOS / 48dp Android)

**Responsive Fidelity**
- [ ] Layout adapts correctly at all breakpoints
- [ ] Content reflows properly (no horizontal scroll)
- [ ] Touch-specific and desktop-specific behaviors work correctly
- [ ] Images and media scale appropriately

**Content Fidelity**
- [ ] Real content (not placeholder text) renders correctly
- [ ] Long text handling: truncation, wrapping, overflow
- [ ] Empty states match designs
- [ ] Error messages match approved copy
- [ ] RTL layout mirrors correctly (if applicable)

**Accessibility**
- [ ] ARIA labels present and accurate
- [ ] Screen reader announces elements correctly
- [ ] Color contrast meets WCAG AA (4.5:1 text, 3:1 large text)
- [ ] Keyboard-only navigation works end-to-end

### Filing Design QA Issues

Format:
```
TITLE: [Screen Name] - [Brief description]
SEVERITY: Critical / Major / Minor / Cosmetic
EXPECTED: [What the design shows — link/screenshot]
ACTUAL: [What the implementation shows — screenshot]
DEVICE/BROWSER: [Where the issue appears]
NOTES: [Why this matters for the user experience]
```

---

## Component Documentation

### Documentation Template

For each component in the design system:

```
## Component: [Name]

### Purpose
When and why to use this component.

### Anatomy
Visual breakdown of sub-elements (label, icon, container, etc.)

### Variants
- Primary: [use case]
- Secondary: [use case]
- Ghost: [use case]
- Destructive: [use case]

### States
| State | Visual | Behavior |
|-------|--------|----------|
| Default | [description] | — |
| Hover | [description] | cursor changes to pointer |
| Active/Pressed | [description] | scale down slightly |
| Focus | [description] | visible focus ring |
| Disabled | [description] | pointer-events: none |
| Loading | [description] | spinner replaces label |

### Sizes
- Small: height 32px, font-size 14px
- Medium: height 40px, font-size 16px (default)
- Large: height 48px, font-size 18px

### Tokens Used
- Background: button-bg-primary
- Text: button-text-primary
- Border-radius: button-radius
- Padding: button-padding-x, button-padding-y

### Accessibility
- Role: button
- aria-label: required when icon-only
- Keyboard: Enter/Space to activate
- Focus: visible focus ring, 2px offset

### Do's and Don'ts
DO: Use primary for the single most important action per screen
DON'T: Use multiple primary buttons in the same context
DO: Include a clear, action-oriented label ("Save changes")
DON'T: Use vague labels ("Submit", "OK")
```

---

## Responsive Specification Format

### Breakpoint Strategy

Define breakpoints based on content, not devices:

| Breakpoint | Width | Typical Use |
|-----------|-------|-------------|
| **Mobile** | 320-767px | Single column, bottom navigation, stacked layout |
| **Tablet** | 768-1023px | Two columns, sidebar navigation possible |
| **Desktop** | 1024-1439px | Multi-column, full navigation, hover states |
| **Wide** | 1440px+ | Max-width container, increased whitespace |

### Per-Component Responsive Rules

Document how each component adapts:

```
## Navigation
- Mobile: Bottom tab bar (5 items max), hamburger for secondary nav
- Tablet: Side rail (collapsed icons), expand on hover/tap
- Desktop: Full sidebar with labels

## Card Grid
- Mobile: Single column, full width
- Tablet: 2 columns, 16px gap
- Desktop: 3-4 columns, 24px gap
- Wide: 4 columns, max-width 1200px centered

## Data Table
- Mobile: Card view (each row becomes a stacked card)
- Tablet: Horizontal scroll with pinned first column
- Desktop: Full table view
```

### RTL Responsive Considerations

When designing responsive + RTL:
- Column order reverses at all breakpoints
- Bottom navigation item order reverses
- Swipe direction reverses (swipe right = forward in RTL)
- Text alignment flips; numbers stay LTR
- Touch zones shift for right-handed RTL interaction

---

## Edge Case Catalog

### Template for Documenting Edge Cases

| Category | Edge Case | Design Decision | Fallback |
|----------|-----------|----------------|----------|
| **Data** | User has 0 transactions | Show empty state with CTA to first action | — |
| **Data** | User has 1,000+ transactions | Paginate, 20 per page, infinite scroll | Show "Load more" button |
| **Data** | Transaction amount is 0.001 EGP | Display 2 decimal places minimum | Round to nearest piaster |
| **Text** | Username is 50+ characters | Truncate with ellipsis after 30 chars | Tooltip shows full name |
| **Network** | API timeout after 10 seconds | Show retry button with error message | Cache last-known-good data |
| **Network** | Complete offline | Show cached data with "offline" banner | Queue actions for sync |
| **Permission** | Camera access denied | Show explanation + settings deep-link | Fall back to manual input |
| **Device** | Screen too small for content | Stack horizontally-laid elements | Scrollable container |
| **Locale** | Mixed LTR/RTL content | BiDi algorithm handles, test thoroughly | Manual dir attributes |
| **Security** | Session expires mid-task | Save draft state, redirect to login | Restore draft after re-auth |

---

## Collaboration Anti-Patterns

### What Goes Wrong

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| **"Over the wall" handoff** | Designer finishes, emails a link, moves on | Designer stays involved through development |
| **Pixel-perfect from screenshots** | Dev eyeballs spacing from a screenshot | Use design tokens; dev references spec, not image |
| **Undocumented states** | Dev invents error/empty states | Designer documents ALL states explicitly |
| **Late engineering input** | "This is technically impossible" after design is final | Include engineers in design reviews from wireframe stage |
| **Design drift** | Implementation slowly diverges from spec | Regular design QA sessions during sprints |
| **Assumption cascade** | Dev assumes behavior for edge cases | Edge case catalog provided upfront; unknowns flagged for discussion |
| **Token drift** | Figma tokens diverge from code tokens | Single source of truth; automated token sync |
