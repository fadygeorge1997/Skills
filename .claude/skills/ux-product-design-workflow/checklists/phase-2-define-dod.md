# Phase 2: Define & Problem Framing — Definition of Done

## Overview

This checklist defines the criteria for completing Phase 2 (Define & Problem Framing). All items must be checked before advancing to Phase 3 (IA & Interaction Design).

---

## Checklist

### Affinity Mapping

- [ ] All research findings clustered into themes
- [ ] Themes labeled with descriptive names
- [ ] Themes prioritized by frequency, severity, and business impact
- [ ] Each theme has evidence weight documented

### User Personas

- [ ] 2-4 primary personas created
- [ ] Each persona includes all required fields:
  - [ ] Name and archetype
  - [ ] Demographics (with evidence citations)
  - [ ] Behaviors
  - [ ] Goals
  - [ ] Pain points
  - [ ] JTBD statement
  - [ ] Representative quote
- [ ] Every attribute tagged with evidence or marked as assumption
- [ ] Confidence level documented (evidence-backed vs. hypothesis)

#### Verification
- Evidence: each persona attribute has at least one `[EVIDENCE: source]` tag or `[ASSUMPTION: reason]` tag

### Journey Maps

- [ ] Journey maps created for primary personas (min 1 per persona)
- [ ] All stages defined with touchpoints
- [ ] User actions documented per stage
- [ ] Emotional arc captured
- [ ] Pain points identified with severity
- [ ] Opportunities documented per stage
- [ ] Evidence sources cited

### Problem Statements

- [ ] Problem statements follow canonical format: "[User] needs a way to [need] because [insight]"
- [ ] Each statement is:
  - [ ] Grounded in evidence
  - [ ] Specific to a user segment
  - [ ] Focused on need (not feature)
  - [ ] Testable
  - [ ] Business-relevant
- [ ] Multiple problem statements generated (not just one)

### HMW Statements

- [ ] HMW statements derived from problem statements
- [ ] Each HMW calibrated:
  - [ ] Not too broad (suggests too many directions)
  - [ ] Not too narrow (constrains solutions)
  - [ ] Opens creative solution space
- [ ] HMW connects to research evidence

### Opportunity Solution Tree

- [ ] Target outcome metric defined
- [ ] Opportunities linked to user needs/pain points
- [ ] Solutions brainstormed per opportunity
- [ ] Experiments identified for validation
- [ ] Traceability maintained from outcome to experiments

### Design Brief Update

- [ ] Problem focus articulated
- [ ] Target persona priorities confirmed
- [ ] Scope defined
- [ ] Success criteria established
- [ ] Constraints documented

### Stakeholder Alignment

- [ ] Findings reviewed with stakeholders
- [ ] Problem prioritization agreed
- [ ] Team aligned on focus area

#### Verification
- Evidence: meeting notes or async approval documented in `ux/define/` confirming stakeholder alignment

---

## Deliverables Checklist

| Deliverable | Format | Status |
|-------------|--------|--------|
| User Personas | `templates/persona-template.md` | ✓/✗ |
| Journey Maps | `templates/journey-map-template.md` | ✓/✗ |
| Problem Statements | `templates/problem-statement-template.md` | ✓/✗ |
| HMW Statements | `templates/hmw-template.md` | ✓/✗ |
| Opportunity Solution Tree | `templates/opportunity-solution-tree-template.md` | ✓/✗ |
| Design Brief (Updated) | `templates/design-brief-template.md` | ✓/✗ |

---

## Cross-Phase References

### From Phase 1 (Required)

| Artifact | Used In Phase 2 | Status |
|----------|-----------------|--------|
| JTBD statements | Persona JTBD field | ✓/✗ |
| Empathy maps | Persona behaviors/feelings | ✓/✗ |
| Competitive analysis | Journey map touchpoints | ✓/✗ |
| Opportunity backlog | Opportunity Solution Tree | ✓/✗ |
| Four-Risk Gate | Risk validation | ✓/✗ |

### For Phase 3 (Created)

| Artifact | Will Feed Into |
|----------|----------------|
| Personas | IA mental models, user flows |
| Journey map pain points | Flow pain point resolution |
| Problem statements | Sitemap navigation justification |
| HMW statements | Ideation starting point |

---

## Phase Transition Criteria

**Before advancing to Phase 3, confirm:**

| Criterion | Status |
|-----------|--------|
| Team can state exactly which problem they're solving | ✓/✗ |
| Team can identify who they're solving it for | ✓/✗ |
| Team can explain why it matters | ✓/✗ |
| Everyone on the team agrees on the above | ✓/✗ |
| Problem is grounded in research evidence | ✓/✗ |

#### Verification
- Evidence: each problem statement includes at least one `[EVIDENCE: source]` citation from Phase 1 research

---

## Quality Assurance

### Persona Quality Check

| Check | Status |
|-------|--------|
| Could apply to anyone? (Bad) | ✓/✗ |
| Includes specific, sometimes surprising details | ✓/✗ |
| Every attribute has evidence or assumption tag | ✓/✗ |
| Proto-personas clearly labeled as hypothesis | ✓/✗ |

### Problem Statement Quality Check

| Check | Status |
|-------|--------|
| Is it a need, not a feature? | ✓/✗ |
| Is it specific, not vague? | ✓/✗ |
| Is there evidence for the insight? | ✓/✗ |
| Is it actionable? | ✓/✗ |

---

## Warning Signs (Do NOT advance if)

- Problem statement is a solution ("Users need a dashboard")
- Personas could apply to anyone
- No evidence cited for key claims
- Stakeholders disagree on problem focus
- Multiple persona needs conflict without prioritization

---

## Anti-Patterns Avoided

| Anti-Pattern | Avoided? | Notes |
|--------------|----------|-------|
| Generic personas | ✓/✗ | [Specific, surprising details included] |
| Solution-framed problems | ✓/✗ | [Needs, not features] |
| Evidence-free claims | ✓/✗ | [All claims tagged] |
| Single persona focus | ✓/✗ | [Multiple personas, clear priority] |

---

## Loop-Back Triggers from Later Phases

Return to Phase 2 Define when:
- Phase 5 testing invalidates persona assumptions (behaviors don't match)
- Phase 7 A/B tests consistently show no lift (hypothesis may be wrong)
- Phase 3 card sorting reveals mental models contradicting personas
- Phase 7 cohort analysis shows different behavior patterns than personas predicted

---

## Sign-off

| Role | Name | Approved | Date |
|------|------|----------|------|
| Design Lead | | ✓/✗ | |
| Product Manager | | ✓/✗ | |
| Engineering Lead | | ✓/✗ | |

---

## Next Phase

Upon completion, proceed to:
> `skills/ux-ia/SKILL.md` — Phase 3: IA & Interaction Design
