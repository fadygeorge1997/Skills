# State Inventory Template

## Inventory Overview

| Attribute | Value |
|-----------|-------|
| **Screen/Component** | [Name] |
| **Created** | [Date] |
| **Owner** | [Name] |
| **Total Elements** | [#] |
| **Total States** | [#] |

---

## State Reference

### The 7+ Essential States

| State | Definition | When It Occurs |
|-------|------------|----------------|
| **Default** | Normal resting state | Initial load, after actions |
| **Empty** | No data available | New user, cleared data |
| **Loading** | Data being fetched | API call in progress |
| **Partial** | Some data available | Progressive loading |
| **Error** | Operation failed | API error, validation error |
| **Success** | Action completed | After successful action |
| **Offline** | No network | Network unavailable |
| **Permission** | Access required | Feature needs authorization |

---

## Element State Inventory

### Element: [Element Name]

**Type:** [Button/Input/Card/List/etc.]

| State | Visual | Behavior | Content | Trigger | Notes |
|-------|--------|----------|---------|---------|-------|
| **Default** | [Description] | [Interaction] | [Text shown] | Initial load | [Notes] |
| **Hover** | [Visual change] | [Cursor/Tooltip] | [Text] | Mouse over | [Notes] |
| **Focus** | [Focus ring] | [Keyboard nav] | [Text] | Tab to element | [Notes] |
| **Active** | [Pressed look] | [Click feedback] | [Text] | Mouse down | [Notes] |
| **Disabled** | [Grayed out] | No interaction | [Text] | [Condition] | [Notes] |
| **Loading** | [Spinner/skeleton] | Wait state | [Loading text] | API call | [Notes] |
| **Error** | [Error style] | [Error message] | [Error text] | Validation fail | [Notes] |
| **Success** | [Success style] | [Checkmark, etc.] | [Success text] | Action complete | [Notes] |

---

### Element: [Element Name]

**Type:** [Type]

| State | Visual | Behavior | Content | Trigger | Notes |
|-------|--------|----------|---------|---------|-------|
| **Default** | [Description] | [Interaction] | [Text] | Initial | [Notes] |
| **Empty** | [Empty state] | [CTA shown] | [Headline + description] | No data | [Notes] |
| **Loading** | [Skeleton] | [Wait] | [Optional text] | Loading | [Notes] |
| **Partial** | [Partial data] | [What's interactive] | [Available content] | Some data | [Notes] |
| **Error** | [Error state] | [Retry option] | [Error message] | Failure | [Notes] |
| **Success** | [Success state] | [Next action] | [Confirmation] | Complete | [Notes] |
| **Offline** | [Offline indicator] | [Cached content] | [Offline message] | No network | [Notes] |

---

### Element: [Element Name]

**Type:** [Type]

| State | Visual | Behavior | Content | Trigger | Notes |
|-------|--------|----------|---------|---------|-------|
| **Default** | [Description] | [Interaction] | [Text] | [Trigger] | [Notes] |
| **Permission** | [Locked state] | [Upgrade prompt] | [Why needed] | Access denied | [Notes] |

---

## Screen-Level States

### Screen: [Screen Name]

| State | Layout | Key Components | User Message | Actions Available |
|-------|--------|----------------|--------------|-------------------|
| **Default** | [Layout description] | [What's visible] | — | [Available actions] |
| **Empty** | [Empty layout] | [Empty state components] | "[Headline]" | [Primary CTA] |
| **Loading** | [Skeleton layout] | [Skeleton components] | "Loading..." | [Cancel if available] |
| **Partial** | [Partial layout] | [Loaded components] | — | [Actions for loaded data] |
| **Error** | [Error layout] | [Error components] | "[Error message]" | [Retry, Contact support] |
| **Success** | [Success layout] | [Success components] | "[Success message]" | [Next action] |
| **Offline** | [Offline layout] | [Cached components] | "You're offline" | [Retry when online] |

---

## State Transition Matrix

### [Element Name] Transitions

| From State | Trigger | To State | Transition Effect |
|------------|---------|----------|-------------------|
| Default | Click | Loading | [Fade/Spin/etc.] |
| Loading | Success | Success | [Transition] |
| Loading | Error | Error | [Transition] |
| Error | Retry | Loading | [Transition] |
| Success | Timeout | Default | [Transition] |

---

## Loading States Detail

### Loading Strategy

| Content Type | Loading Pattern | Skeleton | Progressive Load |
|--------------|-----------------|----------|------------------|
| [Text content] | [Skeleton/Spinner] | [Skeleton style] | [Order of load] |
| [Images] | [Blur-up/Placeholder] | [Placeholder] | [Priority] |
| [Lists] | [Skeleton rows] | [Row skeleton] | [Pagination] |

### Loading Timing

| Duration | Indicator | User Feedback |
|----------|-----------|---------------|
| < 400ms | None needed | Instant feel (Doherty Threshold) |
| 400ms - 2s | Spinner/skeleton | Loading indication |
| > 2s | Progress bar | "This may take a moment" |
| > 10s | Progress + cancel | Offer to cancel |

---

## Error States Detail

### Error Types

| Error Type | Example | User Message | Recovery |
|------------|---------|--------------|----------|
| **Validation** | Invalid email | "That format didn't work. Try name@example.com" | Correct input |
| **Network** | Timeout | "Connection timed out. Try again?" | Retry |
| **Server** | 500 error | "Something went wrong on our end. Please try again." | Retry |
| **Auth** | Not logged in | "Log in to continue" | Login |
| **Permission** | Access denied | "You need [X] permission for this" | Request access |
| **Business** | Insufficient funds | "Not enough balance for this transaction" | Add funds |

### Error Message Guidelines

**Structure:** `[What happened]` + `[Why it matters]` + `[What to do next]`

| Good | Bad |
|------|-----|
| "That email format didn't work. Try something like name@example.com" | "Invalid email" |
| "Something went wrong on our end. Please try again in a moment." | "Error 500" |

---

## Empty States Detail

### Empty State Components

| Component | Purpose | Example |
|-----------|---------|---------|
| **Illustration/Icon** | Visual context | Relevant, not generic |
| **Headline** | What this area is for | "Your transactions will appear here" |
| **Description** | Why it's valuable | "Track spending, spot patterns" |
| **Primary CTA** | First action | "Make your first transfer" |
| **Secondary Info** | Reduce anxiety | "It takes less than 2 minutes" |

### Empty State Template

```markdown
**Empty State: [Scenario]**

**Illustration:** [Description of visual]

**Headline:** "[Headline text]"

**Description:** "[Description of value]"

**Primary CTA:** [Button text] → [Action]

**Secondary:** [Additional context or reassurance]
```

---

## Accessibility for States

| State | Accessibility Consideration |
|-------|----------------------------|
| **Loading** | aria-busy="true", announce "Loading" |
| **Error** | aria-invalid="true", aria-describedby for message |
| **Success** | aria-live region announcement |
| **Disabled** | aria-disabled="true", explain why |
| **Offline** | Status message in aria-live region |

---

## Checklist

### Per Interactive Element

- [ ] Default state defined
- [ ] Hover state defined (if applicable)
- [ ] Focus state defined
- [ ] Active/pressed state defined
- [ ] Disabled state defined
- [ ] Loading state defined
- [ ] Error state defined
- [ ] Success state defined
- [ ] Empty state defined (if applicable)
- [ ] Offline state defined (if applicable)
- [ ] Permission state defined (if applicable)

### Per Screen

- [ ] All screen-level states defined
- [ ] State transitions documented
- [ ] Loading strategy defined
- [ ] Error handling documented
- [ ] Empty states designed
- [ ] Accessibility considered

---

## Connected Artifacts

| Artifact | Relationship | Link |
|----------|--------------|------|
| User Flows | [Where states appear] | [Link] |
| Handoff Docs | [State specifications] | [Link] |
| Edge Case Catalog | [Edge case states] | [Link] |
| Acceptance Criteria | [State criteria] | [Link] |

---

## Metadata

| Field | Value |
|-------|-------|
| Created | [Date] |
| Created By | [Name] |
| Last Updated | [Date] |
| Version | [Version] |
