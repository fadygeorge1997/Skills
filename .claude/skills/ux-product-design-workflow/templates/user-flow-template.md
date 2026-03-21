# User Flow Template

## Flow Overview

| Attribute | Value |
|-----------|-------|
| **Flow Name** | [Name] |
| **Persona** | [Persona Name] |
| **Goal** | [What user is trying to accomplish] |
| **Entry Point** | [Where user starts] |
| **Exit Point** | [Where user ends] |
| **Created** | [Date] |

---

## Flow Diagram

```
┌─────────────┐
│   START     │
│ [Entry Pt]  │
└──────┬──────┘
       │
       ▼
┌─────────────┐     No    ┌─────────────┐
│  Decision?  │───────────▶│  Alt Path   │
└──────┬──────┘            └─────────────┘
       │ Yes
       ▼
┌─────────────┐
│   Screen    │
│   [Name]    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    END      │
│ [Exit Pt]   │
└─────────────┘
```

---

## Flow Steps

### Step 1: [Step Name]

| Element | Details |
|---------|---------|
| **Screen** | [Screen/component name] |
| **URL** | [Path] |
| **User Action** | [What user does] |
| **System Response** | [What system does] |
| **State** | [Default/Loading/Error/etc.] |
| **Decision** | [Yes/No branch if applicable] |

**Annotations:**
- [Additional context or notes]

**References:**
- Persona: [Link]
- JTBD: [Link]
- Pain Point: [Link]

---

### Step 2: [Step Name]

| Element | Details |
|---------|---------|
| **Screen** | [Screen/component name] |
| **URL** | [Path] |
| **User Action** | [What user does] |
| **System Response** | [What system does] |
| **State** | [State] |
| **Decision** | [Branch if applicable] |

**Annotations:**
- [Additional context]

---

### Step 3: [Step Name]

| Element | Details |
|---------|---------|
| **Screen** | [Screen/component name] |
| **URL** | [Path] |
| **User Action** | [What user does] |
| **System Response** | [What system does] |
| **State** | [State] |
| **Decision** | [Branch if applicable] |

---

## Decision Points

### Decision 1: [Decision Name]

| Branch | Condition | Next Step | Notes |
|--------|-----------|-----------|-------|
| **Yes** | [Condition for yes] | [Step #] | [Context] |
| **No** | [Condition for no] | [Step #] | [Context] |

---

## Error Paths

### Error Path 1: [Error Name]

```
[Normal Step] ──▶ [Error State] ──▶ [Recovery Action] ──▶ [Resume Flow]
```

| Element | Details |
|---------|---------|
| **Trigger** | [What causes the error] |
| **Error Screen** | [Where user sees error] |
| **Error Message** | [What user sees] |
| **Recovery Options** | [How user can proceed] |
| **Resume Point** | [Where flow continues] |

### Error Path 2: [Error Name]

| Element | Details |
|---------|---------|
| **Trigger** | [Cause] |
| **Error Screen** | [Screen] |
| **Error Message** | [Message] |
| **Recovery Options** | [Options] |
| **Resume Point** | [Resume point] |

---

## Edge Cases

### Edge Case 1: [Edge Case Name]

| Element | Details |
|---------|---------|
| **Scenario** | [What unusual situation occurs] |
| **Impact on Flow** | [How flow is affected] |
| **Handling** | [How it's addressed] |
| **Alternative Path** | [What user does instead] |

### Edge Case 2: [Edge Case Name]

| Element | Details |
|---------|---------|
| **Scenario** | [Description] |
| **Impact on Flow** | [Impact] |
| **Handling** | [Handling] |
| **Alternative Path** | [Path] |

---

## Flow Variations

### Variation A: [Variation Name]

| Trigger | Divergence Point | Different Steps | Rejoin Point |
|---------|------------------|-----------------|--------------|
| [What triggers this variation] | [Step where it branches] | [What's different] | [Where it rejoins main flow] |

### Variation B: [Variation Name]

| Trigger | Divergence Point | Different Steps | Rejoin Point |
|---------|------------------|-----------------|--------------|
| [Trigger] | [Branch point] | [Differences] | [Rejoin] |

---

## State Transitions

| From State | Trigger | To State | User Feedback |
|------------|---------|----------|---------------|
| [State 1] | [Action/Event] | [State 2] | [What user sees] |
| [State 2] | [Action] | [State 3] | [Feedback] |

---

## Micro-Interactions

| Step | Interaction | Timing | Purpose | Law of UX |
|------|-------------|--------|---------|-----------|
| [Step #] | [Animation/Transition] | [ms] | [Why it exists] | [Which law applies] |

---

## Flow Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Completion Rate | >80% | [Completed / Started] |
| Time to Complete | [baseline] | [Average duration] |
| Error Rate | <10% | [Errors / Actions] |
| Drop-off Point | [Step with lowest continuation] | [Analytics] |

---

## Accessibility Considerations

| Element | Consideration | Implementation |
|---------|--------------|----------------|
| Navigation | [How to navigate by keyboard] | [Implementation notes] |
| Screen Reader | [Announcements needed] | [ARIA implementation] |
| Focus Management | [Focus after actions] | [Focus handling] |

---

## Connected Artifacts

| Artifact | Relationship | Link |
|----------|--------------|------|
| Persona | [Who this flow is for] | [Link] |
| Sitemap | [Pages in this flow] | [Link] |
| State Inventory | [States in this flow] | [Link] |
| Test Plan | [How to test this flow] | [Link] |

---

## Metadata

| Field | Value |
|-------|-------|
| Created | [Date] |
| Created By | [Name] |
| Last Updated | [Date] |
| Version | [Version] |
