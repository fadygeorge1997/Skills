# Acceptance Criteria Template

## Acceptance Criteria Overview

| Attribute | Value |
|-----------|-------|
| **Feature** | [Name] |
| **User Story** | [As a [user], I want [goal] so that [benefit]] |
| **Created** | [Date] |
| **Owner** | [Name] |

---

## Gherkin Format Reference

**Structure:**
```
**Given** [context/precondition]
**When** [action]
**Then** [expected outcome]
```

---

## Core Scenarios

### Scenario 1: [Happy Path Name]

```gherkin
GIVEN [user is logged in]
AND [any preconditions]
WHEN [user performs action]
THEN [expected outcome]
AND [additional outcomes]
```

**Priority:** [P0/P1/P2]
**Status:** [Ready/In Progress/Verified]

---

### Scenario 2: [Alternative Path Name]

```gherkin
GIVEN [context]
AND [preconditions]
WHEN [user performs alternative action]
THEN [expected outcome]
```

**Priority:** [P0/P1/P2]
**Status:** [Ready/In Progress/Verified]

---

### Scenario 3: [Error Handling Name]

```gherkin
GIVEN [error condition exists]
WHEN [user attempts action]
THEN [appropriate error message is displayed]
AND [user can recover from error]
```

**Priority:** [P0/P1/P2]
**Status:** [Ready/In Progress/Verified]

---

## Detailed Acceptance Criteria

### Functional Criteria

| ID | Criterion | Given | When | Then | Status |
|----|-----------|-------|------|------|--------|
| AC1 | [Description] | [Context] | [Action] | [Outcome] | ✓/✗ |
| AC2 | [Description] | [Context] | [Action] | [Outcome] | ✓/✗ |
| AC3 | [Description] | [Context] | [Action] | [Outcome] | ✓/✗ |

### Non-Functional Criteria

| ID | Criterion | Requirement | Verification Method | Status |
|----|-----------|-------------|---------------------|--------|
| NFR1 | Performance | [Load time requirement] | [Test method] | ✓/✗ |
| NFR2 | Accessibility | [WCAG requirement] | [Audit method] | ✓/✗ |
| NFR3 | Security | [Security requirement] | [Test method] | ✓/✗ |

---

## State-Based Criteria

### Default State

```gherkin
GIVEN [component loads with data]
WHEN [no interaction has occurred]
THEN [default state is displayed]
AND [element appears as specified]
```

### Empty State

```gherkin
GIVEN [no data exists]
WHEN [screen/component loads]
THEN [empty state is displayed]
AND [explanation text is shown]
AND [primary CTA is available]
```

### Loading State

```gherkin
GIVEN [data is being fetched]
WHEN [request is in progress]
THEN [loading indicator is displayed]
AND [skeleton/spinner shown as specified]
```

### Error State

```gherkin
GIVEN [an error has occurred]
WHEN [screen/component loads]
THEN [error message is displayed]
AND [message follows error guidelines]
AND [retry option is available]
```

### Success State

```gherkin
GIVEN [action has completed successfully]
WHEN [confirmation is needed]
THEN [success feedback is displayed]
AND [next logical action is clear]
```

### Disabled State

```gherkin
GIVEN [action is not available]
WHEN [condition prevents action]
THEN [element is visually disabled]
AND [reason for disabled state is clear if applicable]
```

---

## Edge Case Criteria

### Data Edge Cases

```gherkin
GIVEN [very long text input]
WHEN [user enters maximum characters]
THEN [text is truncated or handled as specified]
```

```gherkin
GIVEN [special characters in input]
WHEN [user enters emojis or special characters]
THEN [characters are handled correctly]
```

### Timing Edge Cases

```gherkin
GIVEN [slow network connection]
WHEN [request takes longer than [X] seconds]
THEN [appropriate loading state is shown]
AND [user can cancel if applicable]
```

### Permission Edge Cases

```gherkin
GIVEN [user lacks required permission]
WHEN [user attempts restricted action]
THEN [appropriate message is displayed]
AND [option to request access or upgrade is shown]
```

---

## Accessibility Criteria

### Keyboard Navigation

```gherkin
GIVEN user navigates by keyboard
WHEN user tabs through interface
THEN all interactive elements are reachable
AND focus order follows logical sequence
AND focus is visible on all elements
```

### Screen Reader

```gherkin
GIVEN user is using a screen reader
WHEN user navigates interface
THEN all elements have appropriate ARIA labels
AND state changes are announced
AND images have descriptive alt text
```

### Color Contrast

```gherkin
GIVEN interface is displayed
WHEN color contrast is measured
THEN all text meets WCAG 2.1 AA standards
- Normal text: 4.5:1 minimum
- Large text: 3:1 minimum
```

---

## Responsive Criteria

### Mobile Breakpoint

```gherkin
GIVEN viewport width is < [768px]
WHEN interface renders
THEN mobile layout is displayed
AND touch targets are minimum 44x44px
AND content is readable without horizontal scroll
```

### Tablet Breakpoint

```gherkin
GIVEN viewport width is [768px-1024px]
WHEN interface renders
THEN tablet layout is displayed
AND appropriate adaptations are shown
```

### Desktop Breakpoint

```gherkin
GIVEN viewport width is > [1024px]
WHEN interface renders
THEN desktop layout is displayed
AND content uses available space appropriately
```

---

## Integration Criteria

### API Integration

```gherkin
GIVEN [API endpoint is called]
WHEN [specific request is made]
THEN [expected response is handled]
AND [loading states shown appropriately]
AND [errors handled gracefully]
```

### Third-Party Integration

```gherkin
GIVEN [third-party service is integrated]
WHEN [integration is triggered]
THEN [expected behavior occurs]
AND [fallback exists if service is unavailable]
```

---

## Performance Criteria

| Metric | Requirement | Verification |
|--------|-------------|--------------|
| Initial load | < [X] seconds | Lighthouse |
| Time to interactive | < [X] seconds | Lighthouse |
| API response time | < [X] ms | Network monitoring |

---

## Definition of Done

### For Each Scenario

- [ ] Scenario passes automated test
- [ ] Scenario verified manually
- [ ] Edge cases covered
- [ ] Accessibility verified
- [ ] Responsive behavior verified

### For Feature

- [ ] All P0 scenarios pass
- [ ] All P1 scenarios pass
- [ ] Code reviewed
- [ ] Design QA complete
- [ ] Documentation updated

---

## Test Traceability Matrix

| Scenario | Test Case | Automated | Manual | Status |
|----------|-----------|-----------|--------|--------|
| [Scenario 1] | [TC-001] | ✓/✗ | ✓/✗ | [Pass/Fail] |
| [Scenario 2] | [TC-002] | ✓/✗ | ✓/✗ | [Pass/Fail] |

---

## Connected Artifacts

| Artifact | Relationship | Link |
|----------|--------------|------|
| User Story | [Parent requirement] | [Link] |
| State Inventory | [States covered] | [Link] |
| Edge Case Catalog | [Edge cases addressed] | [Link] |
| Handoff Docs | [Design specification] | [Link] |

---

## Metadata

| Field | Value |
|-------|-------|
| Created | [Date] |
| Created By | [Name] |
| Last Updated | [Date] |
| Version | [Version] |
