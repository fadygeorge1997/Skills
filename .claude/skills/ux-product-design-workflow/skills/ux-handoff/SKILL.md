---
name: ux-handoff
description: >
  Phase 6 of the UX & Product Design workflow. Guides design-to-engineering handoff
  including annotated specifications, state documentation, edge-case catalogs,
  accessibility requirements, and acceptance criteria. Ensures engineering can build
  with minimal ambiguity and rework.

  Use this skill when: preparing designs for engineering, creating handoff documentation,
  writing acceptance criteria, documenting edge cases, or specifying accessibility requirements.
---

# Phase 6: Design-to-Engineering Handoff

## Overview

**Goal:** Create comprehensive handoff documentation that engineering can build from without ambiguity.

**Duration:** 1-2 weeks overlapping with engineering sprints

**When to move on:** Engineering confirms they have everything needed to implement, and design QA process is defined.

---

## The Staggered Sprint Pipeline

UX work runs ahead of engineering:
- **Sprint N-2:** Research, problem validation, concept exploration
- **Sprint N-1:** Detailed design, prototyping, user testing
- **Sprint N:** Engineering builds Sprint N-1 designs while UX works on Sprint N+1

UX attends ALL sprint ceremonies: planning, standups, reviews, retros.

---

## Input Requirements

From Phase 5 (Validate):
- [ ] Validated high-fidelity designs
- [ ] Heuristic evaluation findings (resolved)
- [ ] Accessibility audit results
- [ ] User flow documentation

From Earlier Phases:
- [ ] State inventories (Phase 3)
- [ ] Design tokens (Phase 4)
- [ ] User personas (Phase 2)

---

## Phase Checklist

### 1. Annotated Specifications
- [ ] Component-by-component behavior documentation
- [ ] Interaction annotations (hover, click, focus, etc.)
- [ ] Spacing and layout specifications
- [ ] Typography and color references
- [ ] Animation and transition specs

### 2. State Documentation
- [ ] All 8 content states per screen + 5 interaction states per interactive element
- [ ] State transition triggers
- [ ] Content for each state
- [ ] Error handling per state

### 3. Edge Case Catalog
- [ ] Data edge cases (empty, null, overflow, special characters)
- [ ] Timing edge cases (race conditions, timeouts)
- [ ] Permission edge cases (revoked access, expired sessions)
- [ ] Connectivity edge cases (offline, slow network)

### 4. Accessibility Requirements
- [ ] ARIA labels and roles
- [ ] Keyboard navigation paths
- [ ] Focus management
- [ ] Screen reader announcements
- [ ] Color contrast ratios

### 5. Responsive Behavior
- [ ] Breakpoint definitions
- [ ] Layout changes per breakpoint
- [ ] Touch target sizes
- [ ] Content prioritization

### 6. Acceptance Criteria
- [ ] Given/When/Then scenarios
- [ ] Per-component criteria
- [ ] Per-flow criteria
- [ ] Accessibility criteria

### 7. QA Collaboration
- [ ] Visual QA checklist
- [ ] Test scenarios for QA
- [ ] Definition of done for design QA

---

## Deliverables

| Artifact | Format | Template |
|----------|--------|----------|
| Handoff Checklist | Comprehensive checklist | `templates/handoff-checklist-template.md` |
| State Documentation | Element-state matrix | `templates/state-inventory-template.md` |
| Edge Case Catalog | Scenario catalog | `templates/edge-case-catalog-template.md` |
| Accessibility Spec | WCAG requirements | Generated during phase |
| Acceptance Criteria | Gherkin format | `templates/acceptance-criteria-template.md` |

---

## Handoff Checklist Template

```markdown
# Design Handoff Checklist: [Feature Name]

## Context
- **Designer:** [Name]
- **Feature:** [Description]
- **Target Sprint:** [Sprint number]
- **Engineering Lead:** [Name]

## Design Artifacts
- [ ] High-fidelity mockups (all screens)
- [ ] Interactive prototype (key flows)
- [ ] Design system components used
- [ ] Asset export (icons, images)

## Component Specifications
- [ ] Spacing documented (8px grid)
- [ ] Typography (font, size, weight, line-height)
- [ ] Colors (token names, not hex)
- [ ] Border radius, shadows
- [ ] States documented (8 content + 5 interaction)

## Interaction Documentation
- [ ] Hover states
- [ ] Active/pressed states
- [ ] Focus states (keyboard)
- [ ] Disabled states
- [ ] Loading states
- [ ] Error states
- [ ] Success states
- [ ] Transitions and animations

## Content
- [ ] Final copy provided (no Lorem Ipsum)
- [ ] Empty state copy
- [ ] Error messages
- [ ] Help text and tooltips

## Edge Cases
- [ ] Empty state handling
- [ ] Long text truncation
- [ ] Network failure handling
- [ ] Permission denied handling
- [ ] Offline behavior

## Accessibility
- [ ] ARIA labels specified
- [ ] Keyboard navigation documented
- [ ] Focus order defined
- [ ] Screen reader text
- [ ] Color contrast verified (4.5:1)

## Responsive
- [ ] Mobile breakpoint
- [ ] Tablet breakpoint
- [ ] Desktop breakpoint
- [ ] Touch targets (44x44px)

## Acceptance Criteria
- [ ] Gherkin scenarios written
- [ ] Edge case scenarios included
- [ ] Accessibility test scenarios

## Sign-off
- [ ] Engineering review completed
- [ ] Questions resolved
- [ ] Ready for implementation
```

---

## State Documentation Format

```markdown
# State Documentation: [Component/Screen Name]

## Element: [Name]

| State | Visual | Behavior | Content | Trigger |
|-------|--------|----------|---------|---------|
| Default | [Description] | [Interaction] | [Text] | Initial load |
| Empty | [Empty state visual] | [CTA behavior] | [Headline + description + CTA] | No data |
| Loading | [Skeleton/spinner] | [Wait behavior] | [Optional: "Loading..."] | Data fetch start |
| Partial | [Partial visual] | [What's interactive] | [Available content] | Some data loaded |
| Error | [Error visual] | [Retry options] | [Error message + retry CTA] | Fetch failure |
| Success | [Success visual] | [Next step] | [Confirmation + next action] | Action complete |
| Offline | [Offline indicator] | [Retry when online] | [Offline message] | Network loss |
| Permission | [Permission request] | [Request flow] | [Why needed + allow/deny] | Access required |

## State Transitions
```
Default → Loading → Success/Error
Default → Loading → Error → Retry → Loading
Empty → Loading → Partial → Success
Offline → (queued) → Online → Sync
```

## Content Reference
- Empty state headline: "[Copy]"
- Empty state description: "[Copy]"
- Error message: "[Copy]"
- Success message: "[Copy]"
```

---

## Edge Case Catalog

### Categories

#### Data Edge Cases
| Scenario | Handling | Notes |
|----------|----------|-------|
| Empty data | [Empty state design] | Show CTA |
| Null values | [Fallback display] | Don't show "null" |
| Very long text | [Truncation rule] | Ellipsis + tooltip |
| Special characters | [Sanitization/escaping] | Security + display |
| Negative numbers | [Display format] | Parentheses vs minus |
| Zero values | [Display format] | Show "0" or "-"? |

#### Timing Edge Cases
| Scenario | Handling | Notes |
|----------|----------|-------|
| Slow network | [Loading state + timeout] | 30s timeout? |
| Race conditions | [Cancellation/debounce] | Last request wins |
| Concurrent edits | [Conflict resolution] | Merge or notify? |
| Session timeout | [Preserve data + re-auth] | Don't lose work |

#### Permission Edge Cases
| Scenario | Handling | Notes |
|----------|----------|-------|
| Not logged in | [Login prompt + return] | Deep link preserved |
| Insufficient permissions | [Explanation + request] | Graceful degradation |
| Permission revoked mid-session | [Re-auth prompt] | Data preservation |

#### Connectivity Edge Cases
| Scenario | Handling | Notes |
|----------|----------|-------|
| Offline | [Cached content + indicator] | Queue actions |
| Intermittent connection | [Retry logic + indicator] | Exponential backoff |
| Slow network | [Optimistic UI + sync] | Progressive loading |

---

## Accessibility Requirements Format

```markdown
# Accessibility Requirements: [Component/Screen]

## ARIA Roles and Labels
| Element | Role | aria-label | aria-describedby |
|---------|------|------------|------------------|
| [Button] | button | "Submit payment" | - |
| [Input] | textbox | - | [error-id] |

## Keyboard Navigation
| Key | Action |
|-----|--------|
| Tab | Move to next interactive element |
| Shift+Tab | Move to previous |
| Enter/Space | Activate button/link |
| Escape | Close modal/cancel |

## Focus Management
- Initial focus: [Element]
- After action: [Element]
- Error focus: [Error message or field]
- Modal focus trap: [First focusable element]

## Screen Reader Announcements
| Event | Announcement |
|-------|--------------|
| Loading | "Loading content" |
| Error | "Error: [message]" |
| Success | "[Action] completed successfully" |
| Validation | "[Field] error: [message]" |

## Color Contrast
| Element | Foreground | Background | Ratio | Status |
|---------|------------|------------|-------|--------|
| Body text | #1F2937 | #FFFFFF | 12.6:1 | ✓ Pass |
| Secondary text | #6B7280 | #FFFFFF | 5.0:1 | ✓ Pass |
```

---

## Acceptance Criteria (Gherkin Format)

```markdown
# Acceptance Criteria: [Feature Name]

## Scenario: [Scenario Name]
**Given** [context/precondition]
**When** [action]
**Then** [expected outcome]

## Example: Successful Payment
**Given** user is logged in
**And** user has sufficient balance
**When** user initiates payment of EGP 100
**Then** payment is processed successfully
**And** user sees success confirmation
**And** transaction appears in history

## Example: Payment Error
**Given** user is logged in
**And** network is unreliable
**When** user initiates payment
**And** network request fails
**Then** user sees error message with retry option
**And** no partial transaction is recorded
**And** user can retry payment

## Example: Empty State
**Given** user is logged in
**And** user has no transaction history
**When** user views transaction list
**Then** user sees empty state message
**And** user sees primary CTA to make first transaction

## Accessibility Criteria
**Given** user navigates by keyboard
**When** user tabs through interface
**Then** all interactive elements are reachable
**And** focus order follows logical sequence
**And** focus is visible on all elements
```

---

## Error Message Guidelines

### Structure
`[What happened]` + `[Why it matters]` + `[What to do next]`

### Rules
- Never blame the user ("You entered..." → "That format didn't work")
- Never use technical jargon ("Error 500" → "Something went wrong on our end")
- Always provide a next step
- Use the user's vocabulary (match persona language)

### Examples

| Bad | Good |
|-----|------|
| "Invalid input" | "That email format didn't work. Try something like name@example.com" |
| "Error 500" | "Something went wrong on our end. Please try again in a moment." |
| "User not found" | "We couldn't find an account with that email. Want to sign up?" |

---

## Empty State Guidelines

### Required Elements
| Element | Purpose | Example |
|---------|---------|---------|
| Illustration/Icon | Visual context | Relevant, not generic |
| Headline | What this area is for | "Your transactions will appear here" |
| Description | Why it's valuable | "Track spending, spot patterns, stay on budget" |
| Primary CTA | First action | "Make your first transfer" |
| Secondary Info | Reduce anxiety | "It takes less than 2 minutes" |

---

## Anti-Patterns to Avoid

### Handoff and Run
- **Problem:** Throwing designs over the wall
- **Solution:** Continuous collaboration, design QA during implementation

### Incomplete States
- **Problem:** Only documenting happy path
- **Solution:** Every screen needs all 8 content states; every interactive element needs all 5 interaction states

### Missing Edge Cases
- **Problem:** Edge cases discovered during development
- **Solution:** Systematic edge case catalog before handoff

### Pixel-Pushing
- **Problem:** Debating exact pixels from screenshots
- **Solution:** Use design tokens, reference shared system

### Screenshot-Based Handoff
- **Problem:** Handing off screenshots instead of specs with tokens, states, and edge cases leads to interpretation errors and rework.
- **Solution:** Every handoff document must include: design token references, all state transitions, edge case handling rules. Screenshots supplement specs, they don't replace them.

### Missing Copy
- **Problem:** Lorem Ipsum in handoff docs. Copy is a design material — placeholder text masks truncation, localization, and comprehension issues.
- **Solution:** Final copy must be present in all handoff docs. If product copy doesn't exist yet, create draft copy that demonstrates realistic content length and tone, and flag it for copywriter review.

---

## Quality Criteria

A handoff package is engineering-ready when: (1) every component has all 8 content states + 5 interaction states documented, (2) acceptance criteria are independently testable (Given/When/Then), (3) edge case catalog covers data, timing, permission, and connectivity scenarios, (4) all design tokens are named (no raw hex/px values), (5) engineering confirms zero open questions.

---

## Definition of Done

Phase 6 is complete when:

- [ ] Annotated specifications (component-by-component behavior)
- [ ] State catalog covering all 8 content states per screen + 5 interaction states per element
- [ ] Edge case catalog with 4 categories (data, timing, permission, connectivity)
- [ ] Accessibility requirements (ARIA, keyboard, focus, contrast, screen reader)
- [ ] Responsive behavior rules with touch targets
- [ ] Acceptance criteria in Given/When/Then format
- [ ] Error messages follow guidelines (friendly, actionable, no jargon)
- [ ] Empty states include education, CTA, and motivation
- [ ] All handoff docs reference state inventories from Phase 3
- [ ] Engineering confirms readiness
- [ ] Design QA process defined

---

## Cross-Phase References

**Input from Earlier Phases:**
- State inventories (Phase 3) → State documentation
- Heuristic findings (Phase 5) → Issues to address
- Accessibility audit (Phase 5) → Accessibility requirements
- User flows (Phase 3) → Acceptance criteria scenarios

**Output feeds into:**
- Phase 7 (Optimize): Metrics for success tracking
- Development: Implementation specification
- QA: Test scenarios

---

## Context-Adaptive Depth

| Mode | Documentation Depth | Edge Cases | Accessibility |
|------|---------------------|------------|---------------|
| **MVP** | Core screens + key states | Critical only | Basic WCAG |
| **Growth** | Standard handoff | 4 categories | WCAG 2.1 AA |
| **Enterprise** | Comprehensive + audit trail | All scenarios | Full compliance docs |

---

## Templates Used

- `templates/handoff-checklist-template.md`
- `templates/state-inventory-template.md`
- `templates/edge-case-catalog-template.md`
- `templates/acceptance-criteria-template.md`

---

## Next Phase

When Definition of Done is complete, proceed to:
> `skills/ux-optimize/SKILL.md` — Phase 7: Post-Launch Optimization
