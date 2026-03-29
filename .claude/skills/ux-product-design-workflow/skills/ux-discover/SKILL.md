---
name: ux-discover
description: >
  Phase 1 of the UX & Product Design workflow. Guides Discovery & Research activities
  including stakeholder alignment, user interviews, competitive analysis, JTBD mapping,
  and empathy mapping. Produces research synthesis, opportunity backlog, and Four-Risk
  Gate initial assessment.

  Use this skill when: starting a new product, conducting user research, running
  competitive analysis, creating empathy maps, documenting JTBD statements, or
  building an opportunity backlog.
---

# Phase 1: Discovery & Research

## Overview

**Goal:** Deeply understand users, context, behaviors, and pain points *before* proposing solutions.

**Duration:** 2-4 weeks typically

**When to move on:** You can articulate who the users are, what jobs they're hiring solutions for, and where the biggest unmet needs live — backed by evidence, not assumptions.

---

## Input Requirements

Before starting this phase, gather or request:

- [ ] Business objectives and constraints from stakeholders
- [ ] Any existing user research or analytics data
- [ ] Market context and competitive landscape awareness
- [ ] Product vision or problem hypothesis (if exists)
- [ ] Timeline and resource constraints

**If no inputs exist:** Start with stakeholder alignment session to define objectives.

---

## Phase Checklist

### 1. Stakeholder Alignment
- [ ] Document business objectives and success criteria
- [ ] Identify constraints (timeline, budget, technical, regulatory)
- [ ] Map stakeholder assumptions explicitly
- [ ] Align on target user segments (hypotheses to validate)

### 2. User Research
- [ ] Design research plan with methodology selection
- [ ] Create interview scripts using JTBD-style questions
- [ ] Recruit participants (minimum 5-8 per segment)
- [ ] Conduct interviews with active listening
- [ ] Perform contextual inquiry where possible
- [ ] Review existing analytics: heatmaps, funnels, support tickets

### 3. Competitive Analysis
- [ ] Identify 3-5 direct and indirect competitors
- [ ] Build feature comparison matrix
- [ ] Conduct UX teardowns of key flows
- [ ] Document positioning gaps and opportunities

### 4. Synthesis
- [ ] Create empathy maps (6 quadrants) per segment
- [ ] Document JTBD job statements and job maps
- [ ] Affinity cluster findings into themes
- [ ] Build opportunity backlog with evidence weights

### 5. Risk Assessment
- [ ] Complete Four-Risk Gate initial assessment
- [ ] Document assumptions requiring validation
- [ ] Identify highest-uncertainty risk areas

---

## Deliverables

| Artifact | Format | Template |
|----------|--------|----------|
| Research Plan | Structured markdown | `templates/research-plan-template.md` |
| Interview Scripts | Question guide per segment | Generated during phase |
| Competitive Analysis | Matrix + teardown | `templates/competitive-analysis-template.md` |
| Empathy Maps | 6-quadrant canvas | `templates/empathy-map-template.md` |
| JTBD Statements | Structured format | `templates/jtbd-statement-template.md` |
| Opportunity Backlog | Prioritized list | Generated during phase |
| Four-Risk Gate | Assessment document | `templates/four-risk-gate-template.md` |
| Design Brief | 1-2 page summary | `templates/design-brief-template.md` |

### Quality Criteria

A research synthesis is complete when: (1) every finding cites at least one evidence source, (2) themes are tagged with frequency count, (3) assumptions are explicitly separated from evidence.

---

## JTBD Interview Questions

### Situation Questions
- "Tell me about the last time you [situation]. What happened?"
- "Walk me through how you currently handle [task]."
- "What were you trying to accomplish when you [action]?"

### Motivation Questions
- "What was going through your mind when you decided to [action]?"
- "What did you hope would happen?"
- "What were you worried might happen?"

### Outcome Questions
- "How did it turn out compared to what you expected?"
- "What would have made it better?"
- "What's the biggest frustration you still have with [domain]?"

### Behavioral Questions
- "How do you currently solve this problem?"
- "What workarounds have you tried?"
- "What's the hardest part about [activity]?"

---

## Empathy Map Structure (6 Quadrants)

```
┌─────────────────────────────────────────────────────┐
│                    SAYS                             │
│  Direct quotes from interviews and observations     │
├─────────────────────┬───────────────────────────────┤
│        SEES         │          HEARS                │
│  What they see in   │  What they hear from others,  │
│  their environment, │  friends, colleagues, media   │
│  competitors, market│                               │
├─────────────────────┼───────────────────────────────┤
│      THINKS         │          DOES                 │
│  What they think    │  What they actually do,       │
│  but don't say,     │  behaviors, actions taken     │
│  concerns, hopes    │                               │
├─────────────────────┴───────────────────────────────┤
│                   FEELS                             │
│  Emotions, fears, anxieties, joys, frustrations     │
└─────────────────────────────────────────────────────┘
```

Each entry must be tagged with evidence:
- `[EVIDENCE: interview-3]` — Direct observation
- `[ASSUMPTION: inferred]` — Educated guess requiring validation

---

## Four-Risk Gate Template

For each initiative, assess all four risks:

| Risk | Status | Evidence | Action Needed |
|------|--------|----------|---------------|
| **Value** | Pass/Fail/Incomplete | [Research findings] | [What to validate] |
| **Usability** | Pass/Fail/Incomplete | [User behavior data] | [What to test] |
| **Feasibility** | Pass/Fail/Incomplete | [Tech assessment] | [What to spike] |
| **Viability** | Pass/Fail/Incomplete | [Business model] | [What to model] |

**Gate Status:** Advance only when all risks are addressed (not necessarily passed, but understood).

---

## Anti-Patterns to Avoid

### Confirmation Tourism
- **Problem:** Interviewing only to validate existing beliefs
- **Solution:** Actively seek disconfirming evidence. Ask "What would prove me wrong?"

### Persona Theater
- **Problem:** Creating personas from demographics and guesses
- **Solution:** Every persona attribute must cite specific research evidence

### Analysis Paralysis
- **Problem:** Researching endlessly without converging
- **Solution:** Set a timebox. 2-4 weeks is usually enough for initial discovery.

### Skipping to Solutions
- **Problem:** "I already know what to build"
- **Solution:** Document assumptions explicitly. Test them. Most will be wrong.

### Solo Research
- **Problem:** Conducting research without stakeholder involvement. Insights not shared don't drive decisions.
- **Solution:** Include at least one stakeholder in synthesis sessions. Share findings early and often.

### Data Hoarding
- **Problem:** Collecting data without documenting in retrievable format.
- **Solution:** Every interview, observation, and data point goes into a structured artifact (empathy map, JTBD statement, or opportunity backlog) within 48 hours of collection.

---

## Definition of Done

Phase 1 is complete when:

- [ ] Stakeholder alignment documented with objectives and constraints
- [ ] Research plan executed with minimum 5-8 interviews per segment
- [ ] Competitive analysis of 3-5 competitors with UX teardown
- [ ] Empathy maps created with evidence-tagged entries (all 6 quadrants)
- [ ] JTBD statements (minimum 3) in canonical format
- [ ] Opportunity backlog prioritized by impact and evidence weight
- [ ] Four-Risk Gate initial assessment completed
- [ ] All assumptions explicitly tagged `[ASSUMPTION]`
- [ ] Context mode set (MVP/Growth/Enterprise)
- [ ] Design brief created with scope and success criteria

---

## Cross-Phase References

**Required input from previous phase:** None (Phase 1 is the entry point). However, Phase 7 (Optimize) feeds new research questions and behavior data back into Discovery when looping.

**Output feeds into:**
- Phase 2 (Define): Personas reference JTBD statements and empathy maps
- Phase 2 (Define): Problem statements reference opportunity backlog
- Phase 3 (IA): User flows reference JTBD job maps

**Artifacts this phase produces for the next phase (Phase 2):**
- Research synthesis with themed insights
- Empathy maps per segment
- JTBD statements and job maps
- Competitive analysis findings
- Opportunity backlog
- Four-Risk Gate assessment
- Design brief with constraints

**Loop-back triggers:** Return to Discovery when Phase 7 metrics stall, when new user segments emerge, when market conditions shift significantly, or when assumptions tagged in later phases prove invalid.

**Reference artifacts in outputs:**
- Persona → "Based on JTBD statement: [reference]"
- Journey map → "Pain point identified in empathy map: [reference]"

---

## Context-Adaptive Depth

| Mode | Research Depth | Participants | Documentation |
|------|---------------|--------------|---------------|
| **MVP** | Lean, focused on top 2 segments | 3-5 per segment | 1-2 page synthesis |
| **Growth** | Balanced across segments | 5-8 per segment | Standard templates |
| **Enterprise** | Comprehensive with compliance review | 8-12 per segment | Full documentation + audit trail |

---

## Templates Used

- `templates/research-plan-template.md`
- `templates/competitive-analysis-template.md`
- `templates/empathy-map-template.md`
- `templates/jtbd-statement-template.md`
- `templates/four-risk-gate-template.md`
- `templates/design-brief-template.md`
- `templates/participant-screener-template.md`

---

## Next Phase

When Definition of Done is complete, proceed to:
> `skills/ux-define/SKILL.md` — Phase 2: Define & Problem Framing
