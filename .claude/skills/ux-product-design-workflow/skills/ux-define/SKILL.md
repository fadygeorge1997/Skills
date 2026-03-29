---
name: ux-define
description: >
  Phase 2 of the UX & Product Design workflow. Guides Define & Problem Framing
  activities including persona creation, journey mapping, problem statement writing,
  HMW statements, and Opportunity Solution Trees. Transforms research into actionable
  problem definitions.

  Use this skill when: synthesizing research data, creating personas, building journey
  maps, writing problem statements, crafting HMW questions, or prioritizing opportunities.
---

# Phase 2: Define & Problem Framing

## Overview

**Goal:** Converge raw research into specific, actionable problem statements.

**Duration:** 1-2 weeks typically

**When to move on:** The team can state exactly which user problem they're solving, for whom, and why it matters — and everyone agrees.

---

## Input Requirements

From Phase 1 (Discovery):
- [ ] Research synthesis with themed insights
- [ ] Empathy maps per segment
- [ ] JTBD statements and job maps
- [ ] Competitive analysis findings
- [ ] Opportunity backlog
- [ ] Four-Risk Gate assessment
- [ ] Design brief with constraints

**If Phase 1 artifacts don't exist:** Warn user that outputs will be assumption-based proto-artifacts requiring validation.

---

## Phase Checklist

### 1. Affinity Mapping
- [ ] Cluster all research findings into thematic groups
- [ ] Label themes with descriptive names
- [ ] Prioritize themes by frequency, severity, and business impact
- [ ] Document theme evidence weights

### 2. Persona Creation
- [ ] Identify 2-4 primary personas from research
- [ ] Document demographics with evidence citations
- [ ] List behaviors, goals, and pain points
- [ ] Include JTBD statement per persona
- [ ] Add representative quote from research

### 3. Journey Mapping
- [ ] Define journey stages for each primary persona
- [ ] Map touchpoints per stage
- [ ] Document actions and emotional arc
- [ ] Identify pain points with severity
- [ ] Add opportunities per stage

### 4. Problem Framing
- [ ] Write problem statements in canonical format
- [ ] Calibrate HMW statements (not too broad, not too narrow)
- [ ] Build Opportunity Solution Tree
- [ ] Validate against research data

### 5. Alignment
- [ ] Create design brief with problem focus
- [ ] Review with stakeholders
- [ ] Confirm target persona priorities

---

## Deliverables

| Artifact | Format | Template |
|----------|--------|----------|
| User Personas | Profile cards (2-4) | `templates/persona-template.md` |
| Journey Maps | Stage-based tables | `templates/journey-map-template.md` |
| Problem Statements | Structured format | `templates/problem-statement-template.md` |
| HMW Statements | Scoped questions | `templates/hmw-template.md` |
| Opportunity Solution Tree | Hierarchical diagram | `templates/opportunity-solution-tree-template.md` |
| Design Brief | 1-2 page summary | `templates/design-brief-template.md` |

### Quality Criteria

A persona is complete when: (1) behaviors are grounded in observed research data (not assumed), (2) JTBD statement follows the 4-part format, (3) at least 3 evidence citations support key attributes.

---

## Persona Template

```markdown
# [NAME]: The [Archetype]

## Demographics
- **Age:** [age] [EVIDENCE: interview-X]
- **Location:** [location] [EVIDENCE: survey-Y]
- **Occupation:** [job title]
- **Tech Comfort:** [Low/Medium/High]

## Behaviors
- [Behavior 1] [EVIDENCE: observation-Z]
- [Behavior 2]
- [Behavior 3]

## Goals
- [Primary goal] [EVIDENCE: interview-A]
- [Secondary goal]

## Pain Points
- [Pain point 1] — Severity: [H/M/L] [EVIDENCE: support-ticket-B]
- [Pain point 2]

## JTBD Statement
"When [situation], I want to [motivation], so I can [outcome] without [pain point]."

## Representative Quote
> "[Direct quote from research]" — [Interview participant X]

## Confidence Level
- [ ] Evidence-backed (research data supports all fields)
- [ ] Hypothesis (proto-persona requiring validation)
```

---

## Problem Statement Format

**Canonical Structure:**
> "[User] needs a way to [need] because [insight]."

**Quality Checklist:**
- [ ] Specific user segment named
- [ ] Real need (not feature request)
- [ ] Evidence-backed insight
- [ ] Business relevance clear
- [ ] Testable

**Examples:**

| Good | Bad |
|------|-----|
| "First-time mobile wallet users in Egypt need a way to understand transaction fees upfront because hidden costs at checkout cause 43% abandonment and erode trust in digital payments." | "Users need a better checkout experience." |
| "Small business owners managing inventory need a way to quickly identify low-stock items because 67% report missing sales due to unexpected stockouts." | "We need a dashboard." |

---

## HMW Calibration Guide

**The Goldilocks Zone:**

| Too Broad | Too Narrow | Just Right |
|-----------|------------|------------|
| "HMW make the app better?" | "HMW add a blue notification badge?" | "HMW help new users feel confident completing their first transaction within 5 minutes?" |
| "HMW improve onboarding?" | "HMW reduce the form to 3 fields?" | "HMW reduce the anxiety that first-time digital payment users feel when committing money?" |

**Calibration Test:**
1. Does it suggest multiple solution directions? (Not too narrow)
2. Is it specific enough to act on? (Not too broad)
3. Does it connect to user research? (Evidence-based)

---

## Journey Map Structure

```markdown
# Journey Map: [Persona Name] - [Journey Name]

## Stage: [Stage Name]

| Touchpoint | Action | Emotion | Pain Points | Opportunities |
|------------|--------|---------|-------------|---------------|
| [Where] | [What] | [😊😐😟] | [Friction] | [Improvement] |

## Emotional Arc
[Description of how emotions change across stages]

## Key Insights
- [Insight 1] [EVIDENCE: source]
- [Insight 2]

## References
- Persona: [Link to persona]
- JTBD: [Link to JTBD statement]
- Research: [Link to empathy map]
```

---

## Opportunity Solution Tree

```markdown
# Opportunity Solution Tree

## Target Outcome
[The metric you're trying to move]

## Opportunities (User Needs/Pain Points)
1. [Opportunity 1] [EVIDENCE: research source]
   - Solutions:
     - a. [Solution idea]
     - b. [Solution idea]
   - Experiments:
     - [How to validate]
2. [Opportunity 2]
   - Solutions: ...
```

---

## Anti-Patterns to Avoid

### Generic Personas
- **Problem:** Personas that could apply to anyone
- **Solution:** Include specific, sometimes surprising details from research

### Solution-Framed Problems
- **Problem:** "Users need a dashboard" (solution, not problem)
- **Solution:** "Users need to quickly understand their data status" (need)

### Evidence-Free Claims
- **Problem:** Stating assumptions as facts
- **Solution:** Every claim tagged with evidence or marked as assumption

### Single Persona Focus
- **Problem:** Designing for one user type when multiple exist
- **Solution:** Create 2-4 personas, prioritize primary for this initiative

### Feature-Framed Problems
- **Problem:** Writing problem statements that are disguised feature requests ("Users need a dropdown" vs "Users need to quickly select their bank").
- **Solution:** Apply the "so that" test — if the statement names a UI element instead of a user outcome, reframe it.

### Personas Without Behaviors
- **Problem:** Demographics without behavioral patterns are marketing segments, not design tools.
- **Solution:** Every persona must include observed behaviors with evidence citations. If you only have demographics, label it a proto-persona and schedule validation research.

---

## Definition of Done

Phase 2 is complete when:

- [ ] Affinity mapping completed with themed clusters
- [ ] 2-4 personas created with all required fields, evidence-tagged
- [ ] Journey maps for primary personas (minimum 1 per persona)
- [ ] Problem statements in canonical format with evidence
- [ ] HMW statements calibrated and validated
- [ ] Opportunity Solution Tree linking outcomes to opportunities
- [ ] All personas reference JTBD from Phase 1
- [ ] Contradictory evidence surfaced with resolution plan
- [ ] Design brief updated with problem focus
- [ ] Stakeholder alignment confirmed

---

## Cross-Phase References

**Required input from Phase 1 (Discovery):**
- Research synthesis with themed insights
- Empathy maps per segment → Persona behaviors and feelings
- JTBD statements and job maps → Persona JTBD field
- Competitive analysis findings → Journey map touchpoints
- Opportunity backlog → Opportunity Solution Tree
- Four-Risk Gate assessment
- Design brief with constraints

**Artifacts this phase produces for the next phase (Phase 3):**
- User personas (2-4) with behaviors, goals, and JTBD statements
- Journey maps with pain points and opportunities
- Problem statements in canonical format
- HMW statements (calibrated)
- Opportunity Solution Tree
- Updated design brief with problem focus

**Output feeds into:**
- Phase 3 (IA): Sitemap structure from persona mental models
- Phase 3 (IA): User flows reference personas by name
- Phase 4 (Design): Laws of UX application based on persona behaviors
- Phase 5 (Validate): Test plan participants match persona segments

**Loop-back triggers:** Return to Phase 1 (Discovery) when persona validation reveals significant gaps in research, when contradictory evidence cannot be resolved with existing data, or when new user segments are identified that were not covered in initial research.

---

## Context-Adaptive Depth

| Mode | Personas | Journey Maps | Documentation |
|------|----------|--------------|---------------|
| **MVP** | 1-2 primary only | Core journey only | Essential fields |
| **Growth** | 2-3 personas | Primary + secondary journeys | Standard templates |
| **Enterprise** | 3-4+ personas | All key journeys with edge cases | Full documentation + stakeholder sign-off |

---

## Templates Used

- `templates/persona-template.md`
- `templates/journey-map-template.md`
- `templates/problem-statement-template.md`
- `templates/hmw-template.md`
- `templates/opportunity-solution-tree-template.md`
- `templates/design-brief-template.md`

---

## Next Phase

When Definition of Done is complete, proceed to:
> `skills/ux-ia/SKILL.md` — Phase 3: IA & Interaction Design
