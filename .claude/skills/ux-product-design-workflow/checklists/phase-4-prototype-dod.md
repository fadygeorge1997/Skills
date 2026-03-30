# Phase 4: Prototyping & Laws of UX — Definition of Done

## Overview

This checklist defines the criteria for completing Phase 4 (Prototyping & Laws of UX). All items must be checked before advancing to Phase 5 (Validation & Usability Testing).

---

## Checklist

### Laws of UX Application

- [ ] **Fitts's Law:** Primary CTAs sized and positioned (44x44px minimum, thumb zone)
- [ ] **Hick's Law:** Navigation and choices limited (≤7 items, progressive disclosure)
- [ ] **Jakob's Law:** Platform conventions followed, familiar patterns used
- [ ] **Doherty Threshold:** Response time addressed (<400ms, skeleton screens, optimistic UI)
- [ ] **Miller's Law:** Content chunked, forms grouped, lists paginated
- [ ] **Peak-End Rule:** Completion moments designed for delight
- [ ] **Zeigarnik Effect:** Progress indicators for multi-step flows
- [ ] **Aesthetic-Usability Effect:** Polish applied for trust and perceived usability

### Design System Integration

- [ ] Primitive tokens defined (colors, spacing, typography)
- [ ] Semantic tokens created (bg-primary, text-primary, spacing-section)
- [ ] Component tokens mapped (button-bg, card-padding)
- [ ] Token naming consistent between design and code
- [ ] Component library referenced/extended

### High-Fidelity Designs

- [ ] All key screens designed at high fidelity
- [ ] Realistic content used (no Lorem Ipsum)
- [ ] All interaction states designed:
  - [ ] Default
  - [ ] Hover (where applicable)
  - [ ] Focus
  - [ ] Active/Pressed
  - [ ] Disabled
  - [ ] Loading
  - [ ] Error
  - [ ] Empty
  - [ ] Success
- [ ] Responsive behavior documented per breakpoint

### Micro-interactions

- [ ] Transitions documented with timing and easing
- [ ] Animations have stated purpose
- [ ] Animations respect prefers-reduced-motion
- [ ] Feedback animations designed for key actions

### RTL/MENA (if applicable)

- [ ] Layout mirroring applied
- [ ] Text direction handled correctly
- [ ] Typography adjusted for Arabic (line-height, font size)
- [ ] Iconography checked for cultural appropriateness
- [ ] Fintech trust patterns applied (if fintech)

### Self-Review

- [ ] Nielsen's 10 heuristic self-check completed
- [ ] Ethical Design Hierarchy check passed
- [ ] Accessibility self-audit completed (WCAG 2.1 AA)

#### Verification
- Evidence: completed Nielsen heuristic self-check table with notes for each heuristic documented below
- Evidence: WCAG 2.1 AA self-audit results documented in the Accessibility Self-Audit section of this checklist

### Prototype

- [ ] Interactive prototype created for key flows
- [ ] Prototype includes error states and edge cases
- [ ] Realistic delays and transitions included
- [ ] Prototype ready for user testing

---

## Deliverables Checklist

| Deliverable | Format | Status |
|-------------|--------|--------|
| High-Fidelity Designs | Annotated mockups | ✓/✗ |
| Design Token Documentation | Token definitions | ✓/✗ |
| Micro-interaction Specs | Timing + easing docs | ✓/✗ |
| Responsive Rules | Breakpoint behavior | ✓/✗ |
| Interactive Prototype | Clickable flow | ✓/✗ |
| Heuristic Self-Check | Completed checklist | ✓/✗ |

---

## Cross-Phase References

### From Phase 3 (Required)

| Artifact | Used In Phase 4 | Status |
|----------|-----------------|--------|
| Wireframes | High-fidelity design base | ✓/✗ |
| State inventories | Interaction state designs | ✓/✗ |
| User flows | Prototype flow structure | ✓/✗ |

### For Phase 5 (Created)

| Artifact | Will Feed Into |
|----------|----------------|
| High-fidelity designs | Prototype for testing |
| Prototype | Usability testing sessions |
| Heuristic self-check | Formal heuristic evaluation |

---

## Laws of UX Application Log

| Law | How Applied | Where | Status |
|-----|-------------|-------|--------|
| Fitts's Law | [Application] | [Screen/Component] | ✓/✗ |
| Hick's Law | [Application] | [Screen/Component] | ✓/✗ |
| Jakob's Law | [Application] | [Screen/Component] | ✓/✗ |
| Doherty Threshold | [Application] | [Screen/Component] | ✓/✗ |
| Miller's Law | [Application] | [Screen/Component] | ✓/✗ |
| Peak-End Rule | [Application] | [Screen/Component] | ✓/✗ |
| Zeigarnik Effect | [Application] | [Screen/Component] | ✓/✗ |
| Aesthetic-Usability | [Application] | [Screen/Component] | ✓/✗ |

---

## Nielsen's Heuristic Self-Check

| # | Heuristic | Status | Notes |
|---|-----------|--------|-------|
| 1 | Visibility of system status | ✓/✗ | |
| 2 | Match between system and real world | ✓/✗ | |
| 3 | User control and freedom | ✓/✗ | |
| 4 | Consistency and standards | ✓/✗ | |
| 5 | Error prevention | ✓/✗ | |
| 6 | Recognition rather than recall | ✓/✗ | |
| 7 | Flexibility and efficiency | ✓/✗ | |
| 8 | Aesthetic and minimalist design | ✓/✗ | |
| 9 | Help users recover from errors | ✓/✗ | |
| 10 | Help and documentation | ✓/✗ | |

---

## Ethical Design Hierarchy Check

| Level | Status | Evidence |
|-------|--------|----------|
| **1. Human Rights** | ✓/✗ | [Accessibility, privacy, security verified] |
| **2. Functionality** | ✓/✗ | [Usability, performance verified] |
| **3. Delight** | ✓/✗ | [Pursued only when 1-2 solid] |

---

## Accessibility Self-Audit

| WCAG Principle | Status | Notes |
|----------------|--------|-------|
| **Perceivable** | ✓/✗ | |
| **Operable** | ✓/✗ | |
| **Understandable** | ✓/✗ | |
| **Robust** | ✓/✗ | |

### Specific Checks

| Check | Status |
|-------|--------|
| Color contrast 4.5:1 (text) | ✓/✗ |
| Touch targets 44x44px | ✓/✗ |
| Keyboard navigation works | ✓/✗ |
| Focus visible | ✓/✗ |

---

## Phase Transition Criteria

**Before advancing to Phase 5, confirm:**

| Criterion | Status |
|-----------|--------|
| Prototype realistic enough for meaningful feedback — Evidence: prototype URL or file path documented | ✓/✗ |
| Design system documented enough for engineering | ✓/✗ |
| Laws of UX systematically applied | ✓/✗ |
| Nielsen heuristic self-check passed | ✓/✗ |
| Ethical Design Hierarchy check passed | ✓/✗ |

---

## Quality Assurance

### Design Quality Check

| Check | Status |
|-------|--------|
| All states designed (not just default) | ✓/✗ |
| Realistic content (no Lorem Ipsum) | ✓/✗ |
| Consistent spacing (8px grid) | ✓/✗ |
| Token usage (not hardcoded values) | ✓/✗ |

### Prototype Quality Check

| Check | Status |
|-------|--------|
| Covers key flows | ✓/✗ |
| Includes error states | ✓/✗ |
| Realistic timing | ✓/✗ |
| Ready for testing | ✓/✗ |

---

## Warning Signs (Do NOT advance if)

- Only happy path designed
- Lorem Ipsum placeholder content
- Laws of UX mentioned but not applied
- No accessibility consideration
- Form over function (aesthetics over usability)

---

## Anti-Patterns Avoided

| Anti-Pattern | Avoided? | Notes |
|--------------|----------|-------|
| Form over function | ✓/✗ | [Accessibility before aesthetics] |
| Inconsistent patterns | ✓/✗ | [Pattern library followed] |
| Ignoring conventions | ✓/✗ | [Platform conventions used] |
| Over-animation | ✓/✗ | [Animations purposeful, skippable] |

---

## Loop-Back Triggers from Later Phases

Return to Phase 4 Prototype when:
- Phase 5 severity-4 issues in prototype require redesign
- Phase 6 handoff reveals 3+ undocumented states per component
- Phase 5 accessibility audit fails WCAG AA on core flows
- Phase 5 SUS score <68 (below average usability)

---

## Sign-off

| Role | Name | Approved | Date |
|------|------|----------|------|
| Design Lead | | ✓/✗ | |
| Product Manager | | ✓/✗ | |
| Accessibility Lead | | ✓/✗ | |

---

## Next Phase

Upon completion, proceed to:
> `skills/ux-validate/SKILL.md` — Phase 5: Validation & Usability Testing
