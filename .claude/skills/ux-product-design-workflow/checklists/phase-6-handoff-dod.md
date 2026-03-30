# Phase 6: Design-to-Engineering Handoff — Definition of Done

## Overview

This checklist defines the criteria for completing Phase 6 (Design-to-Engineering Handoff). All items must be checked before engineering implementation begins.

---

## Checklist

### Annotated Specifications

- [ ] Component-by-component behavior documented
- [ ] Interaction annotations included (hover, click, focus)
- [ ] Spacing and layout specifications provided
- [ ] Typography references (tokens, not hardcoded)
- [ ] Color references (tokens, not hex values)
- [ ] Animation and transition specifications

### State Documentation

- [ ] All 8 content states documented per screen + 5 interaction states per element
- [ ] State transition triggers defined
- [ ] Content for each state specified
- [ ] Error handling per state documented
- [ ] State inventory references included

### Edge Case Catalog

- [ ] Data edge cases documented (empty, null, overflow, special characters)
- [ ] Timing edge cases documented (race conditions, timeouts)
- [ ] Permission edge cases documented (revoked access, expired sessions)
- [ ] Connectivity edge cases documented (offline, slow network)
- [ ] Minimum 3 scenarios per category

### Accessibility Requirements

- [ ] ARIA labels and roles specified
- [ ] Keyboard navigation paths documented
- [ ] Focus management defined
- [ ] Screen reader announcements written
- [ ] Color contrast ratios verified (4.5:1 text, 3:1 large text)

### Responsive Behavior

- [ ] Breakpoint definitions provided
- [ ] Layout changes per breakpoint specified
- [ ] Touch target sizes verified (44x44px minimum)
- [ ] Content prioritization per breakpoint

### Acceptance Criteria

- [ ] Given/When/Then scenarios written
- [ ] Per-component criteria included
- [ ] Per-flow criteria included
- [ ] Accessibility criteria included
- [ ] Edge case scenarios included

### Content & Copy

- [ ] Final copy provided (no placeholder text)
- [ ] Empty state copy included
- [ ] Error messages follow guidelines
- [ ] Success messages included
- [ ] Help text and tooltips provided

### Error Message Guidelines

- [ ] All error messages follow structure: [What] + [Why matters] + [Next step]
- [ ] No technical jargon
- [ ] No user-blaming language
- [ ] Actionable next step always provided

### QA Collaboration

- [ ] Visual QA checklist provided
- [ ] Test scenarios for QA documented
- [ ] Definition of done for design QA agreed

---

## Deliverables Checklist

| Deliverable | Format | Status |
|-------------|--------|--------|
| Handoff Checklist | `templates/handoff-checklist-template.md` | ✓/✗ |
| State Documentation | `templates/state-inventory-template.md` | ✓/✗ |
| Edge Case Catalog | `templates/edge-case-catalog-template.md` | ✓/✗ |
| Accessibility Spec | Document | ✓/✗ |
| Acceptance Criteria | `templates/acceptance-criteria-template.md` | ✓/✗ |

---

## Cross-Phase References

### From Earlier Phases (Required)

| Artifact | Used In Phase 6 | Status |
|----------|-----------------|--------|
| State inventories (Phase 3) | State documentation | ✓/✗ |
| Heuristic findings (Phase 5) | Issues to address | ✓/✗ |
| Accessibility audit (Phase 5) | Accessibility requirements | ✓/✗ |
| User flows (Phase 3) | Acceptance criteria scenarios | ✓/✗ |

### For Phase 7 (Created)

| Artifact | Will Feed Into |
|----------|----------------|
| Acceptance criteria | Success baseline for metrics |
| Error messages | Quality metrics for support |

---

## Edge Case Coverage

| Category | Scenarios | Coverage |
|----------|-----------|----------|
| Data | [#] scenarios | ✓/✗ |
| Timing | [#] scenarios | ✓/✗ |
| Permission | [#] scenarios | ✓/✗ |
| Connectivity | [#] scenarios | ✓/✗ |

---

## Accessibility Compliance

### ARIA Documentation

| Element | Role | aria-label | Status |
|---------|------|------------|--------|
| [Component] | [role] | [label] | ✓/✗ |

### Keyboard Navigation

| Action | Key | Status |
|--------|-----|--------|
| Navigate forward | Tab | ✓/✗ |
| Navigate backward | Shift+Tab | ✓/✗ |
| Activate | Enter/Space | ✓/✗ |
| Close/Cancel | Escape | ✓/✗ |

### Focus Management

| Scenario | Focus Destination | Status |
|----------|-------------------|--------|
| Modal open | First focusable element | ✓/✗ |
| Modal close | Trigger element | ✓/✗ |
| Error display | Error message or field | ✓/✗ |
| Content load | Maintain position | ✓/✗ |

---

## Responsive Coverage

| Breakpoint | Width | Status |
|------------|-------|--------|
| Mobile | <768px | ✓/✗ |
| Tablet | 768-1024px | ✓/✗ |
| Desktop | >1024px | ✓/✗ |

---

## Phase Transition Criteria

**Before engineering begins, confirm:**

| Criterion | Status |
|-----------|--------|
| Engineering confirms readiness | ✓/✗ |
| All states documented | ✓/✗ |
| Edge cases catalogued | ✓/✗ |
| Accessibility requirements complete | ✓/✗ |
| Acceptance criteria written | ✓/✗ |
| Error messages follow guidelines | ✓/✗ |
| Empty states designed | ✓/✗ |
| Design QA process defined | ✓/✗ |

---

## Quality Assurance

### Specification Quality Check

| Check | Status |
|-------|--------|
| Uses design tokens (not hardcoded values) | ✓/✗ |
| All interactive elements have state docs | ✓/✗ |
| Responsive behavior specified | ✓/✗ |
| Animations have timing/easing | ✓/✗ |

### Accessibility Quality Check

| Check | Status |
|-------|--------|
| ARIA roles/labels specified | ✓/✗ |
| Keyboard paths documented | ✓/✗ |
| Focus management defined | ✓/✗ |
| Contrast ratios verified | ✓/✗ |

### Content Quality Check

| Check | Status |
|-------|--------|
| No Lorem Ipsum | ✓/✗ |
| Error messages actionable | ✓/✗ |
| Empty states have CTA | ✓/✗ |

---

## Engineering Sign-off

| Element | Confirmed | Engineer | Date |
|---------|-----------|----------|------|
| Specifications complete | ✓/✗ | | |
| States understood | ✓/✗ | | |
| Edge cases clear | ✓/✗ | | |
| Accessibility requirements understood | ✓/✗ | | |
| Questions answered | ✓/✗ | | |

---

## Warning Signs (Do NOT begin engineering if)

- Specifications use hardcoded values (not tokens)
- States incomplete
- Edge cases not documented
- No accessibility requirements
- Engineering has unanswered questions
- Lorem Ipsum in copy

---

## Anti-Patterns Avoided

| Anti-Pattern | Avoided? | Notes |
|--------------|----------|-------|
| Handoff and run | ✓/✗ | [Continuous collaboration planned] |
| Incomplete states | ✓/✗ | [All 8 content + 5 interaction states documented] |
| Missing edge cases | ✓/✗ | [4 categories covered] |
| Pixel-pushing | ✓/✗ | [Token-based specs] |

---

## Loop-Back Triggers

- Engineer identifies 3+ undocumented edge cases → loop back to Phase 4 for state design
- Engineering declares core approach infeasible → loop back to Phase 3 for alternative architecture
- Missing accessibility specs → loop back to Phase 5 for audit completion

---

## Sign-off

| Role | Name | Approved | Date |
|------|------|----------|------|
| Design Lead | | ✓/✗ | |
| Engineering Lead | | ✓/✗ | |
| Product Manager | | ✓/✗ | |
| QA Lead | | ✓/✗ | |

---

## Next Phase

Upon completion, proceed to:
> `skills/ux-optimize/SKILL.md` — Phase 7: Post-Launch Optimization
