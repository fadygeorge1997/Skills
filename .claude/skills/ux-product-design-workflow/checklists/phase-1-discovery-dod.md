# Phase 1: Discovery & Research — Definition of Done

## Overview

This checklist defines the criteria for completing Phase 1 (Discovery & Research). All items must be checked before advancing to Phase 2 (Define & Problem Framing).

---

## Checklist

### Stakeholder Alignment

- [ ] Business objectives documented with success criteria
- [ ] Constraints identified (timeline, budget, technical, regulatory)
- [ ] Stakeholder assumptions explicitly mapped
- [ ] Target user segments hypothesized (to be validated)
- [ ] Context mode set (MVP/Growth/Enterprise)

#### Verification
- Evidence: stakeholder alignment meeting notes or async approval documented in `ux/research/`

### Research Plan

- [ ] Research methodology selected and documented
- [ ] Research questions prioritized
- [ ] Interview script/questionnaire created
- [ ] Participant screener defined
- [ ] Timeline and resources allocated

### User Research Execution

- [ ] Minimum 5-8 interviews conducted per segment
- [ ] Interviews used JTBD-style questions
- [ ] Active listening and neutral probing applied
- [ ] Sessions recorded (with consent) or detailed notes taken
- [ ] Contextual inquiry performed where possible

### Existing Data Review

- [ ] Analytics reviewed: heatmaps, funnels, user flows
- [ ] Support tickets analyzed for pain points
- [ ] Error logs reviewed for friction points
- [ ] Previous research synthesized (if exists)

### Competitive Analysis

- [ ] 3-5 competitors identified (direct and indirect)
- [ ] Feature comparison matrix created
- [ ] UX teardowns of key flows completed
- [ ] Positioning gaps documented
- [ ] Alternative solutions/workarounds documented

### Synthesis

- [ ] Affinity mapping completed with themed clusters
- [ ] Empathy maps created per segment (all 6 quadrants)
- [ ] All empathy map entries evidence-tagged
- [ ] JTBD statements in canonical format (minimum 3)
- [ ] Job maps created for primary jobs
- [ ] Opportunity backlog built and prioritized

### Four-Risk Gate

- [ ] Value risk assessed (evidence of user demand)
- [ ] Usability risk assessed (complexity considerations)
- [ ] Feasibility risk assessed (technical landscape)
- [ ] Viability risk assessed (business model)
- [ ] Overall gate status documented
- [ ] Validation actions identified for unknowns

### Documentation Quality

- [ ] All claims tagged with evidence sources
- [ ] Assumptions explicitly marked [ASSUMPTION]
- [ ] Contradictions surfaced with resolution approach
- [ ] Research sources cited and accessible

#### Verification
- Evidence: spot-check 5 random claims — each must have an `[EVIDENCE: source]` or `[ASSUMPTION: reason]` tag

### Design Brief

- [ ] Problem summary articulated
- [ ] Target users defined
- [ ] Constraints documented
- [ ] Success criteria established
- [ ] Initial scope outlined

---

## Deliverables Checklist

| Deliverable | Format | Status |
|-------------|--------|--------|
| Research Plan | `templates/research-plan-template.md` | ✓/✗ |
| Interview Scripts | Document | ✓/✗ |
| Competitive Analysis | `templates/competitive-analysis-template.md` | ✓/✗ |
| Empathy Maps | `templates/empathy-map-template.md` | ✓/✗ |
| JTBD Statements | `templates/jtbd-statement-template.md` | ✓/✗ |
| Opportunity Backlog | Prioritized list | ✓/✗ |
| Four-Risk Gate | `templates/four-risk-gate-template.md` | ✓/✗ |
| Design Brief | `templates/design-brief-template.md` | ✓/✗ |

---

## Phase Transition Criteria

**Before advancing to Phase 2, confirm:**

| Criterion | Status |
|-----------|--------|
| Team can articulate who users are | ✓/✗ |
| Team can state what jobs users are hiring solutions for | ✓/✗ |
| Team can identify biggest unmet needs | ✓/✗ |
| All above backed by evidence, not just assumptions | ✓/✗ |
| Four-Risk Gate status is Pass or Conditional Pass | ✓/✗ |
| No catastrophic risks blocking advancement | ✓/✗ |

---

## Warning Signs (Do NOT advance if)

- Research was only done to validate existing beliefs
- Personas created from demographics alone (no behavioral data)
- No actual user contact (only secondary research)
- Stakeholder alignment not achieved
- Major assumptions not identified

---

## Anti-Patterns Avoided

| Anti-Pattern | Avoided? | Notes |
|--------------|----------|-------|
| Confirmation tourism | ✓/✗ | [Evidence of seeking disconfirming data] |
| Persona theater | ✓/✗ | [Personas grounded in research — Evidence: each persona attribute has at least one [EVIDENCE: source] tag] |
| Analysis paralysis | ✓/✗ | [Timeboxed and converged] |
| Skipping to solutions | ✓/✗ | [Focused on understanding, not building] |

---

## Loop-Back Triggers from Later Phases

Return to Phase 1 Discovery when:
- Phase 7 metrics show D7 retention <20% (product-market fit issue)
- Phase 5 testing reveals fundamental misunderstanding of user needs
- Phase 7 analytics discover a new user segment not covered in original research
- Support ticket analysis reveals pain points not captured in empathy maps

---

## Sign-off

| Role | Name | Approved | Date |
|------|------|----------|------|
| Research Lead | | ✓/✗ | |
| Product Manager | | ✓/✗ | |
| Design Lead | | ✓/✗ | |

---

## Next Phase

Upon completion, proceed to:
> `skills/ux-define/SKILL.md` — Phase 2: Define & Problem Framing
