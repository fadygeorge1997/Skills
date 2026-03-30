# Phase 3: IA & Interaction Design — Definition of Done

## Overview

This checklist defines the criteria for completing Phase 3 (IA & Interaction Design). All items must be checked before advancing to Phase 4 (Prototyping & Laws of UX).

---

## Checklist

### Ideation

- [ ] Structured ideation session conducted (SCAMPER, Crazy 8s, Design Studio)
- [ ] Minimum 3 distinct solution concepts generated per problem
- [ ] Concepts evaluated against:
  - [ ] Desirability (users want it)
  - [ ] Feasibility (can build it)
  - [ ] Viability (makes business sense)
- [ ] Top concepts selected for further development

### Information Architecture

- [ ] Card sorting conducted (open, closed, or hybrid)
- [ ] Results analyzed for user mental model alignment

#### Verification
- Evidence: card sorting results documented with agreement matrix or dendrograms in `ux/ia/`
- [ ] Sitemap created organized by user needs (not org chart)
- [ ] Navigation hierarchy validated with Hick's Law (≤7 items per level)
- [ ] Tree testing validation approach defined

### Sitemap

- [ ] All pages/screens included
- [ ] Navigation zones defined (primary, secondary, footer)
- [ ] URL structure defined
- [ ] Mental model alignment documented
- [ ] Hick's Law check passed

### User Flows

- [ ] Primary user flows mapped for core scenarios
- [ ] Decision points and branching documented
- [ ] Error paths and recovery documented
- [ ] Edge cases identified and handled
- [ ] Flows annotated with persona context
- [ ] Flows reference personas by name

### State Inventory

- [ ] All interactive elements identified
- [ ] All 8 content states documented per screen:
  - [ ] Default
  - [ ] Empty
  - [ ] Loading
  - [ ] Partial (if applicable)
  - [ ] Error
  - [ ] Success
  - [ ] Offline (if applicable)
  - [ ] Permission (if applicable)
- [ ] State transitions documented
- [ ] Content defined for each state

### Wireframes

- [ ] Low-fidelity wireframes created for key screens
- [ ] Focus on layout, hierarchy, and flow
- [ ] Behavioral annotations included
- [ ] Wireframes tested (hallway testing minimum)

#### Verification
- Evidence: hallway test feedback documented with at least 3 participant observations in `ux/ia/`

### Design Patterns

- [ ] Common interaction patterns defined (CRUD, search, filter, navigate)
- [ ] Patterns align with platform conventions
- [ ] Pattern deviations documented with rationale

---

## Deliverables Checklist

| Deliverable | Format | Status |
|-------------|--------|--------|
| Ideation Output | Documented concepts | ✓/✗ |
| Sitemap | `templates/sitemap-template.md` | ✓/✗ |
| User Flows | `templates/user-flow-template.md` | ✓/✗ |
| State Inventory | `templates/state-inventory-template.md` | ✓/✗ |
| Wireframes | Annotated descriptions | ✓/✗ |

---

## Cross-Phase References

### From Phase 2 (Required)

| Artifact | Used In Phase 3 | Status |
|----------|-----------------|--------|
| Personas | User flow persona context | ✓/✗ |
| Journey map pain points | Flow pain point resolution | ✓/✗ |
| Problem statements | Sitemap navigation justification | ✓/✗ |
| HMW statements | Ideation starting point | ✓/✗ |

### For Phase 4 (Created)

| Artifact | Will Feed Into |
|----------|----------------|
| Wireframes | High-fidelity design base |
| State inventories | Interaction state designs |
| User flows | Prototype flow structure |

---

## Hick's Law Validation

| Navigation Level | Item Count | Target | Status |
|------------------|------------|--------|--------|
| Primary navigation | | ≤7 | ✓/✗ |
| Secondary navigation | | ≤7 | ✓/✗ |
| Per screen choices | | ≤7 | ✓/✗ |

---

## State Inventory Completeness

| Element | 7+ States Documented | Notes |
|---------|---------------------|-------|
| [Element 1] | ✓/✗ | |
| [Element 2] | ✓/✗ | |
| [Element 3] | ✓/✗ | |

---

## Phase Transition Criteria

**Before advancing to Phase 4, confirm:**

| Criterion | Status |
|-----------|--------|
| 2-3 strong concepts selected | ✓/✗ |
| IA validated (card sorting or tree testing planned) — Evidence: validation results documented in `ux/ia/` | ✓/✗ |
| Wireframes team-ready for refinement | ✓/✗ |
| All core flows mapped with error paths | ✓/✗ |
| All interactive elements have state documentation | ✓/✗ |

---

## Quality Assurance

### IA Quality Check

| Check | Status |
|-------|--------|
| Organized by user mental model, not org chart | ✓/✗ |
| Navigation items within Hick's Law limits | ✓/✗ |
| Card sorting informed structure | ✓/✗ |

### Flow Quality Check

| Check | Status |
|-------|--------|
| Flows reference personas by name | ✓/✗ |
| Error paths documented | ✓/✗ |
| Edge cases identified | ✓/✗ |
| Happy path + alternative paths included | ✓/✗ |

### State Quality Check

| Check | Status |
|-------|--------|
| All interactive elements inventoried | ✓/✗ |
| All 8 content states covered | ✓/✗ |
| Empty state has CTA | ✓/✗ |
| Error state has recovery path | ✓/✗ |

---

## Warning Signs (Do NOT advance if)

- IA structured around internal departments
- Only happy path designed (no error/edge cases)
- Wireframes not tested at all
- First idea accepted without alternatives
- States missing for key interactive elements

---

## Anti-Patterns Avoided

| Anti-Pattern | Avoided? | Notes |
|--------------|----------|-------|
| IA by org chart | ✓/✗ | [User mental model used] |
| Premature convergence | ✓/✗ | [3+ concepts explored] |
| Wireframe theater | ✓/✗ | [Hallway testing done] |
| Missing states | ✓/✗ | [All 8 content states documented] |

---

## Loop-Back Triggers from Later Phases

Return to Phase 3 IA when:
- Phase 5 task completion <60% on a core flow (IA may be wrong)
- Phase 6 engineering review reveals infeasible flow architecture
- Phase 5 tree testing shows <60% findability on primary tasks
- Phase 7 funnel analysis shows unexpected drop-off at navigation decision points

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
> `skills/ux-prototype/SKILL.md` — Phase 4: Prototyping & Laws of UX
