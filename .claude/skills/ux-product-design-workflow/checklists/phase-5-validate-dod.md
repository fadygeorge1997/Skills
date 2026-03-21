# Phase 5: Validation & Usability Testing — Definition of Done

## Overview

This checklist defines the criteria for completing Phase 5 (Validation & Usability Testing). All items must be checked before advancing to Phase 6 (Design-to-Engineering Handoff).

---

## Checklist

### Test Planning

- [ ] Research objectives defined and aligned to HMW statements
- [ ] Methodology selected (moderated/unmoderated, remote/in-person)
- [ ] Participant screener created matching personas
- [ ] Task scenarios written from real jobs (not feature tests)
- [ ] Success metrics defined (completion rate, time-on-task, SUS)
- [ ] Test plan documented

### Participant Recruitment

- [ ] 5-8 participants recruited per segment
- [ ] Participants match persona criteria
- [ ] Sessions scheduled with buffer time
- [ ] Consent forms prepared
- [ ] Incentives arranged

### Test Execution

- [ ] Think-aloud protocol used
- [ ] Sessions recorded (with permission)
- [ ] Moderator avoided leading, helping, reacting
- [ ] Critical incidents noted in real-time
- [ ] Follow-up questions asked appropriately

### Heuristic Evaluation

- [ ] 3-5 evaluators reviewed independently
- [ ] All 10 Nielsen heuristics evaluated
- [ ] Severity ratings assigned (0-4 scale)
- [ ] Findings consolidated and deduplicated
- [ ] Recommendations documented

### Accessibility Audit

- [ ] Automated accessibility scan run
- [ ] Manual WCAG 2.1 AA POUR check completed
- [ ] Keyboard navigation tested
- [ ] Screen reader tested (VoiceOver or NVDA)
- [ ] Color contrast verified (4.5:1)

### Human-AI Testing (if applicable)

- [ ] Transparency tested (user understands AI capabilities)
- [ ] Scoping tested (AI communicates uncertainty)
- [ ] Error recovery tested (user can correct AI)
- [ ] Explainability tested (user understands AI reasoning)

### Synthesis

- [ ] Findings affinity mapped across participants
- [ ] All issues severity-rated (0-4 scale)
- [ ] Issues prioritized by impact vs. effort
- [ ] Recommendations documented
- [ ] Patterns across participants identified

### Issue Resolution

- [ ] Critical issues (severity 4) fixed
- [ ] Major issues (severity 3) addressed or documented
- [ ] Retest scheduled for critical fixes

---

## Deliverables Checklist

| Deliverable | Format | Status |
|-------------|--------|--------|
| Test Plan | `templates/test-plan-template.md` | ✓/✗ |
| Participant Screener | `templates/participant-screener-template.md` | ✓/✗ |
| Heuristic Evaluation | `templates/heuristic-evaluation-template.md` | ✓/✗ |
| Accessibility Audit | POUR checklist | ✓/✗ |
| Findings Report | `templates/findings-report-template.md` | ✓/✗ |
| Recommendations | Prioritized action plan | ✓/✗ |

---

## Cross-Phase References

### From Earlier Phases (Required)

| Artifact | Used In Phase 5 | Status |
|----------|-----------------|--------|
| Personas | Participant recruitment | ✓/✗ |
| Journey map pain points | Test focus areas | ✓/✗ |
| State inventories | States to test | ✓/✗ |
| Prototype | What's being tested | ✓/✗ |

### For Phase 6 (Created)

| Artifact | Will Feed Into |
|----------|----------------|
| Findings | Handoff accessibility requirements |
| Severity-rated issues | Handoff edge case documentation |
| Test scenarios | Acceptance criteria |

---

## Metrics Summary

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Task Completion Rate | >80% | | ✓/✗ |
| SUS Score | ≥68 | | ✓/✗ |
| Error Rate | <10% | | ✓/✗ |
| Time on Task | [baseline] | | ✓/✗ |

---

## Severity Rating Summary

| Severity | Count | Fixed | Remaining |
|----------|-------|-------|-----------|
| 4 (Catastrophic) | | | |
| 3 (Major) | | | |
| 2 (Minor) | | | |
| 1 (Cosmetic) | | | |

---

## Accessibility Audit Summary

### WCAG POUR Check

| Principle | Status | Notes |
|-----------|--------|-------|
| **Perceivable** | ✓/✗ | |
| **Operable** | ✓/✗ | |
| **Understandable** | ✓/✗ | |
| **Robust** | ✓/✗ | |

### Specific Checks

| Check | Status | Value |
|-------|--------|-------|
| Color contrast (normal text) | ✓/✗ | [ratio] |
| Color contrast (large text) | ✓/✗ | [ratio] |
| Touch targets | ✓/✗ | [size] |
| Keyboard navigation | ✓/✗ | |
| Screen reader | ✓/✗ | |

---

## Phase Transition Criteria

**Before advancing to Phase 6, confirm:**

| Criterion | Status |
|-----------|--------|
| Task completion rate >80% on core flows | ✓/✗ |
| No catastrophic issues (severity 4) remain | ✓/✗ |
| Accessibility meets WCAG 2.1 AA | ✓/✗ |
| Critical findings addressed or documented | ✓/✗ |
| Retest completed for critical fixes | ✓/✗ |

---

## Quality Assurance

### Test Quality Check

| Check | Status |
|-------|--------|
| 5+ participants per segment | ✓/✗ |
| Real users (not colleagues) | ✓/✗ |
| Task scenarios realistic | ✓/✗ |
| Moderator neutral | ✓/✗ |

### Findings Quality Check

| Check | Status |
|-------|--------|
| All findings severity-rated | ✓/✗ |
| Evidence cited for each finding | ✓/✗ |
| Recommendations actionable | ✓/✗ |
| Impact vs effort prioritization done | ✓/✗ |

---

## Warning Signs (Do NOT advance if)

- Only tested with team members
- Only tested happy path
- Task completion below 80%
- Catastrophic issues unresolved
- No accessibility testing done

---

## Anti-Patterns Avoided

| Anti-Pattern | Avoided? | Notes |
|--------------|----------|-------|
| Testing with colleagues | ✓/✗ | [Real target users recruited] |
| Single participant | ✓/✗ | [5+ per segment] |
| Only happy path | ✓/✗ | [Errors and edge cases tested] |
| Fixing everything at once | ✓/✗ | [Prioritized by severity] |

---

## Sign-off

| Role | Name | Approved | Date |
|------|------|----------|------|
| Research Lead | | ✓/✗ | |
| Design Lead | | ✓/✗ | |
| Product Manager | | ✓/✗ | |

---

## Next Phase

Upon completion, proceed to:
> `skills/ux-handoff/SKILL.md` — Phase 6: Design-to-Engineering Handoff
