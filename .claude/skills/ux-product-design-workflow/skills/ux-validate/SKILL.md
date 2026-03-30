---
name: ux-validate
description: >
  Phase 5 of the UX & Product Design workflow. Guides validation and usability
  testing activities including test planning, heuristic evaluation, accessibility
  audits, Human-AI interaction testing, and findings synthesis. Ensures designs
  work for real users before engineering commitment.

  Use this skill when: planning usability tests, running heuristic evaluations,
  conducting accessibility audits, testing AI features, or synthesizing test findings.
---

# Phase 5: Validation & Usability Testing

## Overview

**Goal:** Rigorously test with real users and fix critical issues before engineering commitment.

**Duration:** 1-2 weeks typically

**When to move on:** Task completion rate >80% on core flows, no catastrophic usability issues remain, and accessibility meets WCAG AA.

---

## Input Requirements

From Phase 4 (Prototype):
- [ ] High-fidelity designs or interactive prototype
- [ ] Design system documentation
- [ ] User flows to test
- [ ] State documentation

From Earlier Phases:
- [ ] Personas (for participant recruitment)
- [ ] Journey maps (for pain point focus)
- [ ] HMW statements (for test objectives)

---

## Phase Checklist

### 1. Test Planning
- [ ] Define research objectives aligned to HMW statements
- [ ] Select methodology (moderated/unmoderated, remote/in-person)
- [ ] Create participant screener matching personas
- [ ] Write task scenarios from real jobs (not feature tests)
- [ ] Define success metrics (completion rate, time-on-task, SUS)

### 2. Participant Recruitment
- [ ] Recruit 5-8 participants per segment
- [ ] Screen for target persona match
- [ ] Schedule sessions with buffer time
- [ ] Prepare consent forms and incentives

### 3. Test Execution
- [ ] Conduct sessions with think-aloud protocol
- [ ] Don't lead, don't help, don't react visibly
- [ ] Record sessions (with permission)
- [ ] Take notes on critical incidents

### 4. Heuristic Evaluation
- [ ] Have 3-5 evaluators review independently
- [ ] Evaluate against Nielsen's 10 heuristics
- [ ] Rate severity for each finding (0-4 scale)
- [ ] Consolidate and deduplicate findings

### 5. Accessibility Audit
- [ ] Run automated accessibility scan
- [ ] Manual WCAG 2.1 AA POUR check
- [ ] Keyboard navigation testing
- [ ] Screen reader testing (VoiceOver, NVDA)

### 6. Human-AI Testing (if applicable)
- [ ] Test transparency of AI capabilities
- [ ] Test scoping and uncertainty handling
- [ ] Test error recovery mechanisms
- [ ] Test explainability

### 7. Synthesis
- [ ] Affinity map findings across participants
- [ ] Severity-rate all issues
- [ ] Prioritize by impact vs. effort
- [ ] Document recommendations

---

## Deliverables

| Artifact | Format | Template |
|----------|--------|----------|
| Test Plan | Structured document | `templates/test-plan-template.md` |
| Participant Screener | Screening questions | `templates/participant-screener-template.md` |
| Heuristic Evaluation | Findings matrix | `templates/heuristic-evaluation-template.md` |
| Accessibility Audit | POUR checklist | Generated during phase |
| Findings Report | Prioritized report | `templates/findings-report-template.md` |
| Recommendations | Action plan | Generated during phase |

---

## Test Plan Template

```markdown
# Usability Test Plan: [Feature/Product Name]

## Research Objectives
1. [Primary objective linked to HMW statement]
2. [Secondary objective]
3. [Tertiary objective]

## Methodology
- **Type:** [Remote moderated / Unmoderated / In-person]
- **Duration:** [minutes per session]
- **Tools:** [Testing platform]

## Participants

| Segment | Count | Criteria |
|---------|-------|----------|
| [Segment 1] | 5-8 | [Screening criteria] |
| [Segment 2] | 5-8 | [Screening criteria] |

## Task Scenarios

### Task 1: [Name]
**Scenario:** "You are [context]. You want to [goal]."
**Starting Point:** [Where they begin]
**Success Path:** [Expected steps]
**Success Criteria:** [What counts as completion]

### Task 2: [Name]
...

## Metrics
- Task completion rate (target: >80%)
- Time-on-task (target: [baseline])
- Error rate (target: <10%)
- SUS score (target: ≥68)
- Single Ease Question (SEQ) per task

## Schedule
- [Date range for sessions]
- [Analysis time]
- [Report delivery]
```

---

## Task Scenario Guidelines

### Good Task Scenarios
- Written from user's perspective
- Based on real jobs (not features)
- Don't reveal the interface solution
- Have clear success criteria

### Examples

| Good | Bad |
|------|-----|
| "You just had dinner with friends. The bill is EGP 600 and you want to split it 4 ways. Send your portion to Ahmed." | "Test the split bill feature" |
| "You received a notification that your phone bill is due tomorrow. Pay it before the deadline." | "Click on Pay Bills and complete a payment" |

---

## Think-Aloud Protocol

### Instructions to Participants
"We're interested in what you're thinking, not just what you're doing. As you work through these tasks, please say everything you're thinking — your impressions, what you're looking for, what confuses you, what you expect to happen."

### Verbalization Levels

| Level | Description | When to Use |
|-------|-------------|-------------|
| **Concurrent** | Think aloud while doing | Standard usability testing |
| **Retrospective** | Think aloud after watching recording | When concurrent affects performance |
| **Coaching** | Ask "What are you trying to do?" | When participant goes quiet |

### Moderator Rules
1. Don't lead: Avoid "What would you click to..."
2. Don't help: Let them struggle (that's the data)
3. Don't react: Neutral facial expressions
4. Do probe: "What are you looking for?" "What did you expect?"

---

## Heuristic Evaluation Framework

### Nielsen's 10 Heuristics

| # | Heuristic | Common Issues to Check |
|---|-----------|----------------------|
| 1 | Visibility of system status | Loading indicators, progress feedback, confirmation |
| 2 | Match between system and real world | Jargon, mental model mismatches |
| 3 | User control and freedom | Back buttons, undo, cancel options |
| 4 | Consistency and standards | Pattern inconsistencies across screens |
| 5 | Error prevention | Confirmation dialogs, input validation |
| 6 | Recognition rather than recall | Hidden options, unlabeled icons |
| 7 | Flexibility and efficiency | Shortcuts, personalization |
| 8 | Aesthetic and minimalist design | Clutter, unnecessary elements |
| 9 | Help users recover from errors | Error message quality, recovery paths |
| 10 | Help and documentation | Onboarding, tooltips, help access |

### Severity Rating Scale

| Rating | Level | Description | Action |
|--------|-------|-------------|--------|
| 0 | Not a problem | No usability issue | None |
| 1 | Cosmetic | Minor polish issue | Fix if time allows |
| 2 | Minor | Inconvenience, easy workaround | Fix when possible |
| 3 | Major | Significant friction, difficult workaround | High priority fix |
| 4 | Catastrophic | Blocks task completion | Must fix before launch |

---

## Accessibility Audit (WCAG 2.1 AA POUR)

### Perceivable
- [ ] Text alternatives for non-text content
- [ ] Captions for multimedia
- [ ] Content adaptable to different presentations
- [ ] Color contrast: 4.5:1 (normal text), 3:1 (large text)

### Operable
- [ ] All functionality keyboard accessible
- [ ] No keyboard traps
- [ ] Skip navigation links
- [ ] Focus visible
- [ ] Touch targets: 44x44px minimum

### Understandable
- [ ] Readable text (language specified)
- [ ] Predictable behavior (no surprises)
- [ ] Input assistance (labels, instructions, error prevention)

### Robust
- [ ] Valid HTML
- [ ] Name, Role, Value for custom components
- [ ] Status messages programmatically determinable

---

## Human-AI Interaction Testing

When products include AI features, test these additional dimensions:

| Principle | Test Questions | Red Flags |
|-----------|---------------|-----------|
| **Transparency** | Does user understand AI capabilities and limitations? | Blind trust or total distrust |
| **Scoping** | Does AI communicate uncertainty appropriately? | AI guesses wrong without asking |
| **Error Recovery** | Can user easily correct AI mistakes? | Must start over to correct |
| **Explainability** | Can user understand why AI made a recommendation? | User can't explain AI's reasoning |

---

## Findings Report Template

```markdown
# Usability Findings Report: [Feature/Product]

## Executive Summary
[2-3 sentences: overall assessment, key issues, go/no-go recommendation]

## Methodology Summary
- Participants: [count] per segment
- Method: [methodology]
- Tasks tested: [list]

## Key Findings (Prioritized)

### Critical (Severity 4)
| Finding | Location | Evidence | Recommendation |
|---------|----------|----------|----------------|
| [Issue] | [Screen] | [Quote/observation] | [Fix] |

### Major (Severity 3)
| Finding | Location | Evidence | Recommendation |
|---------|----------|----------|----------------|
| ... | ... | ... | ... |

### Minor (Severity 2)
...

### Cosmetic (Severity 1)
...

## Metrics Summary

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Task completion | >80% | [%] | ✓/✗ |
| SUS score | ≥68 | [score] | ✓/✗ |
| Error rate | <10% | [%] | ✓/✗ |

## Recommendations (Impact vs. Effort)

| Recommendation | Impact | Effort | Priority |
|----------------|--------|--------|----------|
| [Fix] | High | Low | 1 |
| ... | ... | ... | ... |

## Next Steps
- [ ] Fix critical issues
- [ ] Retest before handoff
- [ ] Document remaining minor issues for backlog
```

---

## Anti-Patterns to Avoid

### Testing with Colleagues
- **Problem:** They know too much about the product
- **Solution:** Recruit real target users matching personas

### Single Participant
- **Problem:** One user is an anecdote, not data
- **Solution:** 5 users find ~85% of issues

### Only Testing Happy Path
- **Problem:** Edge cases and errors are where products break
- **Solution:** Include error recovery, empty states, edge cases in tasks

### Fixing Everything at Once
- **Problem:** Scope creep, delayed launch
- **Solution:** Prioritize by severity + impact, iterate

### Leading Participants
- **Problem:** Moderator biases results
- **Solution:** Use neutral language, don't react, probe without suggesting

### Accessibility as Afterthought
- **Problem:** Running accessibility audit only after visual design is locked. Retrofitting accessibility is 3-5x more expensive than designing for it from the start.
- **Solution:** Integrate WCAG checks from Phase 3 onward. Run automated scans during prototyping, not just validation.

### Only Testing Desktop
- **Problem:** Testing only on desktop when 80%+ of users are mobile (especially in emerging markets).
- **Solution:** Test on the primary device of your target personas. For MENA markets, test on mid-range Android devices first.

---

## Quality Criteria

Validation is rigorous when: (1) 5+ users per segment tested, (2) task completion rate measured for all core flows, (3) severity ratings assigned to every finding, (4) critical issues have proposed fixes with effort estimates, (5) accessibility audit covers all 4 POUR dimensions, (6) findings report includes quantitative metrics AND qualitative insights.

---

## Definition of Done

Phase 5 is complete when:

- [ ] Test plan with JTBD-based task scenarios created
- [ ] 5-8 participants per segment tested
- [ ] Think-aloud sessions conducted with proper protocol
- [ ] Heuristic evaluation by 3-5 evaluators covering all 10 heuristics
- [ ] All findings severity-rated (0-4 scale)
- [ ] Accessibility audit (WCAG 2.1 AA POUR) completed
- [ ] Human-AI interaction checks completed (if applicable)
- [ ] Test plan references journey map pain points
- [ ] Participant criteria match persona segments
- [ ] Findings report with prioritized recommendations delivered
- [ ] Critical issues fixed and retested

---

## Cross-Phase References

**Input from Earlier Phases:**
- Personas → Participant recruitment criteria
- Journey map pain points → Test focus areas
- State inventories → States to test (especially edge cases)
- Heuristic findings → Handoff documentation

**Output feeds into:**
- Phase 6 (Handoff): Accessibility requirements
- Phase 6 (Handoff): Edge case documentation
- Phase 7 (Optimize): HEART metrics baseline

---

## Context-Adaptive Depth

| Mode | Participants | Methods | Documentation |
|------|--------------|---------|---------------|
| **MVP** | 3-5 per segment | Guerrilla + unmoderated | Critical issues only |
| **Growth** | 5-8 per segment | Moderated + heuristic | Standard report |
| **Enterprise** | 8-12 per segment | Full suite + accessibility audit | Comprehensive + compliance |

---

## Templates Used

- `templates/test-plan-template.md`
- `templates/participant-screener-template.md`
- `templates/heuristic-evaluation-template.md`
- `templates/findings-report-template.md`

---

## Next Phase

When Definition of Done is complete, proceed to:
> `skills/ux-handoff/SKILL.md` — Phase 6: Design-to-Engineering Handoff
