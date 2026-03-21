# Design Handoff Checklist Template

## Handoff Overview

| Attribute | Value |
|-----------|-------|
| **Feature** | [Name] |
| **Designer** | [Name] |
| **Engineering Lead** | [Name] |
| **Target Sprint** | [Sprint #] |
| **Handoff Date** | [Date] |
| **Status** | [Draft/Ready/Approved] |

---

## Design Artifacts

### Mockups & Prototypes

| Artifact | Status | Location | Notes |
|----------|--------|----------|-------|
| High-fidelity mockups | ✓/✗ | [Link] | [Notes] |
| Interactive prototype | ✓/✗ | [Link] | [Notes] |
| Responsive variations | ✓/✗ | [Link] | [Notes] |
| Dark mode (if applicable) | ✓/✗ | [Link] | [Notes] |
| RTL version (if applicable) | ✓/✗ | [Link] | [Notes] |

### Design System

| Component | Status | Notes |
|-----------|--------|-------|
| Uses existing tokens | ✓/✗ | [Which tokens] |
| New components needed | ✓/✗ | [List] |
| Component specs documented | ✓/✗ | [Location] |

---

## Component Specifications

### Layout & Spacing

| Element | Status | Details |
|---------|--------|---------|
| Grid/alignment documented | ✓/✗ | [8px grid, etc.] |
| Spacing values specified | ✓/✗ | [Token references] |
| Responsive breakpoints | ✓/✗ | [Mobile/Tablet/Desktop] |
| Safe areas accounted | ✓/✗ | [Notch, home indicator] |

### Typography

| Element | Status | Details |
|---------|--------|---------|
| Font families specified | ✓/✗ | [Font names/tokens] |
| Font sizes documented | ✓/✗ | [Size scale] |
| Line heights specified | ✓/✗ | [Values] |
| Font weights documented | ✓/✗ | [Weights used] |

### Colors

| Element | Status | Details |
|---------|--------|---------|
| Color tokens referenced | ✓/✗ | [Semantic tokens only] |
| Color contrast verified | ✓/✗ | [WCAG AA: 4.5:1 text] |
| Focus states colored | ✓/✗ | [Visible focus] |
| Error/success colors | ✓/✗ | [Semantic tokens] |

### Borders & Effects

| Element | Status | Details |
|---------|--------|---------|
| Border radius specified | ✓/✗ | [Values/tokens] |
| Shadows documented | ✓/✗ | [Shadow tokens] |
| Opacity values | ✓/✗ | [For overlays, etc.] |

---

## Interaction States

### Per Interactive Element

| Element | Default | Hover | Focus | Active | Disabled | Loading | Error |
|---------|---------|-------|-------|--------|----------|---------|-------|
| [Button 1] | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | N/A |
| [Input 1] | ✓/✗ | N/A | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| [Card 1] | ✓/✗ | ✓/✗ | ✓/✗ | N/A | N/A | N/A | N/A |

### State Inventory

| Item | Status | Location |
|------|--------|----------|
| All states documented | ✓/✗ | [Link to state inventory] |
| Empty states included | ✓/✗ | [Notes] |
| Error states included | ✓/✗ | [Notes] |

---

## Content & Copy

| Element | Status | Details |
|---------|--------|---------|
| Final copy provided | ✓/✗ | [No Lorem Ipsum] |
| Empty state copy | ✓/✗ | [Headline + description + CTA] |
| Error messages | ✓/✗ | [Following guidelines] |
| Success messages | ✓/✗ | [Confirmation copy] |
| Help text/tooltips | ✓/✗ | [If applicable] |
| Placeholder text | ✓/✗ | [Input placeholders] |

---

## Edge Cases

| Category | Status | Documentation |
|----------|--------|---------------|
| Data edge cases | ✓/✗ | [Empty, long text, null, special chars] |
| Timing edge cases | ✓/✗ | [Slow network, timeout, concurrent actions] |
| Permission edge cases | ✓/✗ | [Not logged in, access denied] |
| Connectivity edge cases | ✓/✗ | [Offline, intermittent connection] |

**Edge Case Catalog:** [Link]

---

## Accessibility

### WCAG Requirements

| Requirement | Status | Notes |
|-------------|--------|-------|
| Color contrast 4.5:1 (text) | ✓/✗ | [Verified] |
| Color contrast 3:1 (large text) | ✓/✗ | [Verified] |
| Touch targets 44x44px | ✓/✗ | [Mobile] |
| Focus visible | ✓/✗ | [For all interactive] |
| Keyboard navigation | ✓/✗ | [All reachable by keyboard] |

### ARIA & Screen Reader

| Element | Status | Notes |
|---------|--------|-------|
| ARIA labels specified | ✓/✗ | [For icons, dynamic content] |
| Screen reader text | ✓/✗ | [For visual-only elements] |
| Live regions defined | ✓/✗ | [For dynamic updates] |
| Alt text for images | ✓/✗ | [All images] |

### Accessibility Spec Document

[Link to full accessibility specification]

---

## Responsive Behavior

| Breakpoint | Status | Notes |
|------------|--------|-------|
| Mobile (<768px) | ✓/✗ | [Layout details] |
| Tablet (768-1024px) | ✓/✗ | [Layout details] |
| Desktop (>1024px) | ✓/✗ | [Layout details] |

### Responsive Rules

| Element | Mobile | Tablet | Desktop |
|---------|--------|--------|---------|
| [Navigation] | [Behavior] | [Behavior] | [Behavior] |
| [Cards] | [Layout] | [Layout] | [Layout] |
| [Forms] | [Layout] | [Layout] | [Layout] |

---

## Animations & Micro-interactions

| Interaction | Timing | Easing | Purpose | Status |
|-------------|--------|--------|---------|--------|
| [Transition] | [ms] | [ease-out/etc.] | [Why] | ✓/✗ |
| [Animation] | [ms] | [easing] | [Why] | ✓/✗ |

**Animation Principles:**
- [ ] All animations have purpose
- [ ] Animations can be disabled (prefers-reduced-motion)
- [ ] Timing under 300ms for UI feedback

---

## Assets

| Asset Type | Status | Format | Location |
|------------|--------|--------|----------|
| Icons | ✓/✗ | [SVG/PNG] | [Location] |
| Images | ✓/✗ | [WebP/PNG] | [Location] |
| Illustrations | ✓/✗ | [SVG/PNG] | [Location] |
| Fonts | ✓/✗ | [WOFF2] | [Location] |

---

## Developer Notes

### Technical Considerations

| Item | Details |
|------|---------|
| API dependencies | [What APIs needed] |
| Third-party integrations | [External services] |
| Platform-specific behavior | [iOS/Android differences] |
| Performance considerations | [Lazy loading, etc.] |

### Questions & Answers

| # | Question | Answer | Answered By |
|---|----------|--------|-------------|
| 1 | [Question from dev] | [Answer] | [Name] |

---

## Acceptance Criteria

| # | Scenario | Given/When/Then | Status |
|---|----------|-----------------|--------|
| 1 | [Scenario name] | [Gherkin format] | ✓/✗ |
| 2 | [Scenario name] | [Gherkin format] | ✓/✗ |

**Full Acceptance Criteria:** [Link]

---

## QA Checklist

### Visual QA

| Item | Status | Notes |
|------|--------|-------|
| Matches design specs | ✓/✗ | [Compare to Figma] |
| Spacing correct | ✓/✗ | [8px grid verification] |
| Typography correct | ✓/✗ | [Font sizes, weights] |
| Colors correct | ✓/✗ | [Token usage] |
| Responsive correct | ✓/✗ | [All breakpoints] |

### Functional QA

| Item | Status | Notes |
|------|--------|-------|
| All states work | ✓/✗ | [Test each state] |
| Animations smooth | ✓/✗ | [No jank] |
| Error handling works | ✓/✗ | [Test error states] |
| Empty states display | ✓/✗ | [Test with no data] |

---

## Sign-off

### Engineering Review

| Reviewer | Status | Date | Notes |
|----------|--------|------|-------|
| [Name] | [Approved/Changes needed] | [Date] | [Notes] |

### Design Review

| Reviewer | Status | Date | Notes |
|----------|--------|------|-------|
| [Name] | [Approved/Changes needed] | [Date] | [Notes] |

---

## Ready for Development

**All items checked?** ✓ Ready for development / ✗ Needs completion

| Blocker | Resolution | Owner |
|---------|------------|-------|
| [Any blockers] | [How resolved] | [Name] |

---

## Metadata

| Field | Value |
|-------|-------|
| Created | [Date] |
| Created By | [Name] |
| Last Updated | [Date] |
| Version | [Version] |
