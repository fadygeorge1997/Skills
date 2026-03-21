# Tasks: UX & Product Design Agent

**Feature**: `001-ux-design-agent`
**Generated**: 2026-03-17
**Plan**: [plan.md](plan.md) | **Spec**: [spec.md](spec.md)
**Total tasks**: 38 | **User stories**: 8 | **MVP scope**: US1 + US2

---

## Phase 1: Setup & Validation

*Verify all existing assets are in place and correct before enhancement tasks.*

- [ ] T001 Verify installed plugin structure matches plan.md Project Structure (skills/, agents/, references/, templates/, checklists/, integrations/)
- [ ] T002 Validate plugin.json manifest at `.claude-plugin/plugin.json` — version 1.1.0, correct name and description
- [ ] T003 Confirm all 8 SKILL.md files parse correctly (frontmatter has name + description with valid trigger phrases)
- [ ] T004 Confirm all 6 agents parse correctly (frontmatter has name, description with examples, model, color, tools)
- [ ] T005 [P] Confirm all 24 templates exist in `templates/` per plan.md template list
- [ ] T006 [P] Confirm all 7 DoD checklists exist in `checklists/` per plan.md checklist list
- [ ] T007 [P] Confirm all 10 reference docs exist in `references/` per plan.md reference list

---

## Phase 2: Foundational — Missing Templates & Schemas

*Add the two remaining structural artifacts needed by all user stories.*

- [ ] T008 Create `templates/phase-status-template.json` — starter `ux/phase-status.json` schema matching data-model.md entity definition (7 phases, context object, lastUpdated)
- [ ] T009 Create `templates/evidence-tag-guide.md` — inline tagging reference: `[EVIDENCE: source]`, `[ASSUMPTION: reason]`, `[MEASURED: metric]`, `[CONTRADICTION: source1 vs source2]` with examples per FR-005 and FR-023

---

## Phase 3: US1 — Guided Phase Navigation (P1)

*Goal: User invokes agent on any project state and receives accurate phase diagnosis + next step with DoD.*

**Independent test**: Invoke ux-phase-navigator on empty project → gets Phase 1 diagnosis + research plan prompt. Invoke on project with completed personas + journeys → gets Phase 3 diagnosis.

- [ ] T010 [US1] Review `agents/ux-phase-navigator.md` — add explicit handling for `phase-status.json` creation on first invocation (write starter from `templates/phase-status-template.json`)
- [ ] T011 [US1] Verify `skills/ux-discover/SKILL.md` includes: stakeholder alignment output, research plan generation, JTBD template reference, Four-Risk Gate initial assessment step
- [ ] T012 [P] [US1] Verify `checklists/phase-1-discovery-dod.md` has all 9 DoD items from spec.md Appendix A
- [ ] T013 [P] [US1] Verify `checklists/phase-2-define-dod.md` through `phase-7-optimize-dod.md` each have complete DoD items matching spec.md Appendix A
- [ ] T014 [US1] Add context inference rules to `skills/ux-product-design-workflow/SKILL.md` — project signal detection (few deps → MVP, CI/CD + design tokens → Enterprise) per FR-008 and R7
- [ ] T015 [US1] Add Four-Risk Gate enforcement to `agents/ux-phase-navigator.md` — block Phase 3 advancement if `fourRiskGate` has any `"incomplete"` status

---

## Phase 4: US2 — Artifact Generation from Research (P2)

*Goal: User provides raw research data; agent produces evidence-grounded personas, journey maps, empathy maps, problem statements.*

**Independent test**: Provide 3 interview excerpts to ux-artifact-generator → get 2-4 personas with all required fields, each attribute tagged `[EVIDENCE: source]` or `[ASSUMPTION: rationale]`.

- [ ] T016 [US2] Review `agents/ux-artifact-generator.md` — verify persona schema matches data-model.md Persona entity (all 10 required fields including confidence level)
- [ ] T017 [P] [US2] Verify `templates/persona-template.md` has all required fields: name, demographics, behaviors, goals (ranked), pain points (severity-rated), JTBD, representative quote, technical affinity, evidence tags
- [ ] T018 [P] [US2] Verify `templates/journey-map-template.md` has all required columns: Stage, Touchpoints, Actions, Thoughts, Emotions, Pain Points, Opportunities + emotional arc row
- [ ] T019 [P] [US2] Verify `templates/empathy-map-template.md` has all 6 quadrants: Says, Thinks, Does, Feels, Sees, Hears — with Sees/Hears capturing environmental context per FR-023
- [ ] T020 [US2] Add contradiction handling to `agents/ux-artifact-generator.md` — when data contradicts itself, produce structured comparison table + `[CONTRADICTION: source1 vs source2]` tags per edge case spec
- [ ] T021 [US2] Add proto-persona mode to `agents/ux-artifact-generator.md` — when no research exists, all fields marked `[ASSUMPTION]`, template header shows `confidence: hypothesis`, includes 3-5 interview validation plan
- [ ] T022 [US2] Verify `skills/ux-define/SKILL.md` includes OST (Opportunity Solution Tree) instructions referencing `templates/opportunity-solution-tree-template.md`

---

## Phase 5: US3 — IA, Flows & Interaction Design (P3)

*Goal: User describes a feature; agent produces sitemap, user flow with decision points, and state inventory for all 7+ states.*

**Independent test**: Describe "user onboarding for fintech app" → get sitemap (user mental model, not org chart), primary user flow with decision points + error paths, screen-by-screen state inventory (7+ states).

- [ ] T023 [US3] Verify `skills/ux-ia/SKILL.md` mandates all 7+ interaction states: default, empty, loading, partial, error, success, offline, permission — per FR-006
- [ ] T024 [P] [US3] Verify `templates/state-inventory-template.md` has columns for all 8 states with behavioral description + copy fields per component
- [ ] T025 [P] [US3] Verify `templates/user-flow-template.md` has: happy path, decision points, error paths, edge cases, off-ramps per Phase 3 DoD
- [ ] T026 [US3] Add Hick's Law navigation check to `skills/ux-ia/SKILL.md` — ≤7 items per navigation level, validation note per Phase 3 DoD

---

## Phase 7: US4 — Post-Launch Metrics & Optimization (P4)

*Goal: User has live product; agent helps define HEART/AARRR framework, experiment hypotheses, Product Kata cycle.*

**Independent test**: Describe live feature → get Goals-Signals-Metrics table covering all 5 HEART dimensions, AARRR funnel with drop-off hypotheses, Product Kata plan (4-week cycle).

- [ ] T027 [US4] Verify `skills/ux-optimize/SKILL.md` covers: all 5 HEART dimensions with GSM tables, AARRR funnel with drop-off hypotheses, Product Kata cycle (Direction → Current → Target → Experiments)
- [ ] T028 [P] [US4] Verify `templates/north-star-metric-template.md` has: NSM definition, input metric tree, counter-metrics per Phase 7 DoD

---

## Phase 7: US5 — Context-Adaptive Output Depth (P5)

*Goal: MVP mode produces lean artifacts (1-2 pages); Enterprise mode includes compliance, larger samples, audit references.*

**Independent test**: Ask "generate research plan" in MVP mode → under 2 pages, 3-5 interview targets. In Enterprise mode → compliance checkpoints, larger samples, data handling protocols.

- [ ] T029 [US5] Add context mode dispatch table to `skills/ux-product-design-workflow/SKILL.md` — explicit MVP/Growth/Enterprise output rules: field count, sample sizes, compliance flags, artifact depth per FR-008
- [ ] T030 [US5] Add `--mode` argument handling to `skills/ux-discover/SKILL.md`, `skills/ux-define/SKILL.md`, `skills/ux-validate/SKILL.md` — explicit override takes precedence over inference per R7

---

## Phase 8: US6 — Usability Validation & Heuristic Evaluation (P3)

*Goal: Agent produces structured heuristic evaluations (all 10 Nielsen heuristics) + usability test plans with task scenarios and severity-rated findings.*

**Independent test**: Describe 3 checkout screens → heuristic evaluation covering all 10 Nielsen heuristics, severity-rated (0-4), at least 5 usability issues with specific remediation citing Laws of UX. Test plan with 5+ task scenarios.

- [ ] T031 [US6] Verify `agents/ux-prototype-reviewer.md` covers all 10 Nielsen heuristics with severity 0-4 scale per FR-022 — add any missing heuristics to the evaluation process
- [ ] T032 [P] [US6] Verify `templates/heuristic-evaluation-template.md` has: 10 heuristic sections, severity scale (0-4) with definitions, Laws of UX citation field per finding
- [ ] T033 [P] [US6] Verify `templates/test-plan-template.md` has: research objectives, methodology (moderated/unmoderated, remote/in-person), 5+ task scenario slots, success metrics (completion rate, time-on-task, error rate, SUS target), participant criteria with sample size justification

---

## Phase 9: US7 — Design-to-Engineering Handoff (P3)

*Goal: Agent generates complete 4-layer handoff documentation: annotated specs, edge-case catalog, state docs, accessibility spec, acceptance criteria.*

**Independent test**: Describe 5-field form → handoff docs with all 7+ interaction states per field, validation rules, error messages, keyboard navigation path, screen reader announcements, responsive breakpoints, Given/When/Then acceptance criteria.

- [ ] T034 [US7] Verify `agents/ux-handoff-preparer.md` covers all 4 documentation layers and produces 5 output files — confirm edge case catalog includes all 4 categories: data, timing, permission, connectivity per FR-015 and Phase 6 DoD
- [ ] T035 [P] [US7] Verify `templates/acceptance-criteria-template.md` uses Given/When/Then (Gherkin) format with edge case scenario slots per US7 acceptance scenario 3
- [ ] T036 [P] [US7] Verify `templates/edge-case-catalog-template.md` has sections for all 4 edge case categories (data, timing, permission, connectivity) with minimum 3 scenario slots per category per SC-010

---

## Phase 10: US8 — Spec Kit Lifecycle Integration (P4)

*Goal: UX agent reads existing specs/ artifacts, cross-references user scenarios, contributes [UX]-tagged tasks alongside engineering tasks.*

**Independent test**: In project with `specs/feature/spec.md`, invoke `/ux.define` → reads existing spec, cross-references user scenarios, produces personas that align with spec requirements + mapping table.

- [ ] T037 [US8] Add Spec Kit detection to `skills/ux-discover/SKILL.md` and `skills/ux-define/SKILL.md` — if `specs/` directory exists, read and cross-reference existing spec artifacts per FR-021 and R8
- [ ] T038 [US8] Verify `integrations/skill-chaining-guide.md` documents all 3 Spec Kit integration points (speckit.specify → UX problem statements, speckit.plan → IA constraints, speckit.tasks → [UX]-tagged tasks) with concrete invocation examples

---

## Dependencies

```
T001-T007 (Setup) → T008-T009 (Foundational) → T010-T015 (US1) → T016-T022 (US2)
US1 and US2 are the MVP scope — complete before US3+

US3-US8 are independently parallelizable after US2 is complete:
  T023-T026 (US3) can start in parallel with T027-T028 (US4)
  T029-T030 (US5) can start in parallel with T031-T033 (US6)
  T034-T036 (US7) can start in parallel with T037-T038 (US8)
```

## Parallel Execution Examples

**Phase 3 (US1) — run in parallel within the story:**
```
T012, T013 (checklist verification) run in parallel with T014 (context inference)
T011 (skill verification) runs independently of T015 (risk gate enforcement)
```

**Phase 8/9 (US6/US7) — run in parallel across stories:**
```
T031 (ux-prototype-reviewer check) || T034 (ux-handoff-preparer check)
T032, T033 (template verification) || T035, T036 (template verification)
```

## Implementation Strategy

**MVP scope (do first)**: T001-T022 (Setup + Foundational + US1 + US2)
- Covers the two highest-value JTBDs: phase guidance and artifact generation
- Independently testable after T015 and T022

**Growth scope (do second)**: T023-T030 (US3 + US4 + US5)
- Adds IA design, metrics, and context adaptation
- Unlocks the full 7-phase workflow

**Complete scope (do third)**: T031-T038 (US6 + US7 + US8)
- Adds heuristic evaluation, handoff, and Spec Kit integration
- Lower priority but high value for enterprise teams

## Notes

- All tasks are verification/enhancement tasks against existing assets — no new infrastructure needed
- Tasks marked `[P]` can run in parallel (different files, no blocking dependencies)
- This is a skill/prompt system — "implementation" means editing SKILL.md and template files, not writing code
- Each task should take 5-30 minutes depending on the gap between current and required state
