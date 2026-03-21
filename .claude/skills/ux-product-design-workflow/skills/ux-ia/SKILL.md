---
name: ux-ia
description: >
  Phase 3 of the UX & Product Design workflow. Guides Information Architecture,
  ideation, and interaction design activities including sitemap creation, user flow
  mapping, state inventories, wireframing, and card sorting validation.

  Use this skill when: structuring app navigation, designing user flows, creating
  sitemaps, planning information architecture, designing interaction states, or
  running ideation sessions.
---

# Phase 3: IA & Interaction Design

## Overview

**Goal:** Explore solutions widely, then structure the product's content and navigation.

**Duration:** 1-3 weeks typically

**When to move on:** You have 2-3 strong concepts, a validated information architecture, and wireframes that the team agrees are worth refining.

---

## Input Requirements

From Phase 2 (Define):
- [ ] User personas with behaviors and goals
- [ ] Journey maps with pain points and opportunities
- [ ] Problem statements
- [ ] HMW statements
- [ ] Opportunity Solution Tree
- [ ] Design brief with constraints

**If Phase 2 artifacts don't exist:** Warn user that IA may not reflect user mental models.

---

## Phase Checklist

### 1. Ideation
- [ ] Run structured ideation (SCAMPER, Crazy 8s, Design Studio)
- [ ] Generate 3+ distinct solution concepts per problem
- [ ] Evaluate concepts against desirability, feasibility, viability
- [ ] Select top concepts for further development

### 2. Information Architecture
- [ ] Conduct card sorting (open, closed, or hybrid)
- [ ] Analyze results for user mental model alignment
- [ ] Create sitemap organized by user needs (not org chart)
- [ ] Validate navigation hierarchy (≤7 items per level)
- [ ] Plan tree testing validation

### 3. User Flows
- [ ] Map primary user flows for core scenarios
- [ ] Include decision points and branching
- [ ] Document error paths and recovery
- [ ] Add edge case handling
- [ ] Annotate with persona context

### 4. State Inventory
- [ ] Identify all interactive elements
- [ ] Document all states per element (7+ states)
- [ ] Define state transition triggers
- [ ] Plan loading and error handling

### 5. Wireframes
- [ ] Create low-fidelity wireframes for key screens
- [ ] Focus on layout, hierarchy, and flow
- [ ] Annotate behavior and interactions
- [ ] Plan for hallway testing

---

## Deliverables

| Artifact | Format | Template |
|----------|--------|----------|
| Ideation Output | Documented concepts | Generated during phase |
| Sitemap | Hierarchical diagram | `templates/sitemap-template.md` |
| User Flows | Annotated diagrams | `templates/user-flow-template.md` |
| State Inventory | Element-state matrix | `templates/state-inventory-template.md` |
| Wireframes | Annotated descriptions | Generated during phase |

---

## Ideation Techniques

### SCAMPER Method
For each existing solution or assumption:
- **S**ubstitute: What can be replaced?
- **C**ombine: What can be merged?
- **A**dapt: What else is like this?
- **M**odify: What can be changed?
- **P**ut to other use: New applications?
- **E**liminate: What's unnecessary?
- **R**everse: What can be rearranged?

### Crazy 8s
- 8 ideas in 8 minutes
- Focus on quantity over quality
- Build on each other's ideas in groups

### Concept Evaluation Matrix

| Concept | Desirability | Feasibility | Viability | Total |
|---------|-------------|-------------|-----------|-------|
| [Name] | 1-5 | 1-5 | 1-5 | Sum |
| ... | ... | ... | ... | ... |

---

## Sitemap Structure

```markdown
# Sitemap: [Product Name]

## Navigation Zones

### Primary Navigation
- **Home** (/)
- **[Section 1]** (/[section])
  - [Subsection A]
  - [Subsection B]
- **[Section 2]** (/[section])

### Secondary Navigation
- [Utility items]

### Footer Navigation
- [Footer items]

## Hick's Law Validation
- Primary nav items: [count] (target: ≤7)
- Secondary nav items: [count]
- Total first-level items: [count]

## Mental Model Alignment
- [How this structure maps to persona mental models]
- [Evidence from card sorting]

## References
- Primary Persona: [Persona name]
- Supporting Research: [Link to card sorting results]
```

---

## User Flow Template

```markdown
# User Flow: [Flow Name]

## Persona: [Name]
## Goal: [What they're trying to accomplish]
## Entry Point: [Where they start]

## Flow Steps

### Step 1: [Name]
- **Screen:** [Description]
- **Action:** [What user does]
- **Decision:** [Yes/No branch if applicable]
- **State:** [Default/Loading/Error/Empty]

### Step 2: [Name]
...

## Error Paths
- [Error scenario 1] → [Recovery path]
- [Error scenario 2] → [Recovery path]

## Edge Cases
- [Edge case 1] → [Handling]
- [Edge case 2] → [Handling]

## References
- Persona: [Link]
- Journey Map Pain Point: [Link]
```

---

## State Inventory (7+ States)

Every interactive element must account for these states:

| State | Description | Design Question |
|-------|-------------|-----------------|
| **Default** | Normal resting state | What does the user see initially? |
| **Empty** | No data/content | How do we motivate first action? |
| **Loading** | Data being fetched | Skeleton, spinner, or progress bar? |
| **Partial** | Some data available | What loads first? What's deferred? |
| **Error** | Something failed | Can they retry? Is data preserved? |
| **Success** | Action completed | What's next? Delight moment? |
| **Offline** | No network | What's cached? What's queued? |
| **Permission** | Access required | Why do we need this? Refusal handling? |

### State Inventory Template

```markdown
# State Inventory: [Screen/Component Name]

## Element: [Name]

| State | Visual | Behavior | Content | Edge Case |
|-------|--------|----------|---------|-----------|
| Default | [Description] | [Interaction] | [Text] | [Handler] |
| Empty | ... | ... | ... | ... |
| Loading | ... | ... | ... | ... |
| Partial | ... | ... | ... | ... |
| Error | ... | ... | ... | ... |
| Success | ... | ... | ... | ... |
| Offline | ... | ... | ... | ... |
| Permission | ... | ... | ... | ... |
```

---

## Card Sorting Methodology

### Types
- **Open:** Users create and label categories (discovery)
- **Closed:** Users sort into predefined categories (validation)
- **Hybrid:** Open first, then closed (best of both)

### Participant Guidelines
- 15-30 participants for meaningful results
- Mix of persona segments
- Remote tools: Optimal Workshop, UserTesting, Maze

### Analysis
- Similarity matrix for category patterns
- Dendrogram for hierarchy visualization
- Look for consensus and outliers

---

## Anti-Patterns to Avoid

### IA by Org Chart
- **Problem:** Navigation structured around internal teams
- **Solution:** Structure around user mental models from research

### Premature Convergence
- **Problem:** Falling in love with first idea
- **Solution:** Generate 3+ alternatives before selecting

### Wireframe Theater
- **Problem:** Creating wireframes no one tests
- **Solution:** Even 5 minutes of hallway testing beats zero

### Missing States
- **Problem:** Only designing happy path
- **Solution:** Every interactive element needs all 7+ states

---

## Definition of Done

Phase 3 is complete when:

- [ ] Structured ideation completed with 3+ concepts evaluated
- [ ] Sitemap organized by user mental model (not org chart)
- [ ] Card sorting conducted (or planned for validation)
- [ ] Navigation validated with Hick's Law (≤7 items per level)
- [ ] User flows for core scenarios with error paths and edge cases
- [ ] State inventories for all primary screens (all 7+ states)
- [ ] Wireframe descriptions with behavioral annotations
- [ ] All flows reference personas by name
- [ ] Tree testing validation approach defined (if IA is critical)

---

## Cross-Phase References

**Input from Phase 2:**
- Personas → User flow persona context
- Journey map pain points → Flow pain point resolution
- Problem statements → Sitemap navigation justification

**Output feeds into:**
- Phase 4 (Prototype): High-fidelity designs based on wireframes
- Phase 5 (Validate): Test scenarios from user flows
- Phase 6 (Handoff): State documentation for engineering

---

## Context-Adaptive Depth

| Mode | Ideation | IA Depth | Wireframes |
|------|----------|----------|------------|
| **MVP** | 1-2 concepts | Core screens only | Key screens only |
| **Growth** | 3 concepts | Standard hierarchy | Core + key secondary |
| **Enterprise** | 3-5 concepts | Full hierarchy with validation | All screens with states |

---

## Templates Used

- `templates/sitemap-template.md`
- `templates/user-flow-template.md`
- `templates/state-inventory-template.md`

---

## Next Phase

When Definition of Done is complete, proceed to:
> `skills/ux-prototype/SKILL.md` — Phase 4: Prototyping & Laws of UX
