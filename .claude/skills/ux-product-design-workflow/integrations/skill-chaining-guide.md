# Skill Chaining Guide: UX & Product Design Workflow

This guide shows how the 7 UX skills chain together, which agents to invoke per phase, and the optimal sequences for common design workflows.

---

## Skill Hierarchy

```
ux-product-design-workflow (master orchestrator)
├── ux-discover     → Phase 1: Discovery & Research
├── ux-define       → Phase 2: Define & Problem Framing
├── ux-ia           → Phase 3: IA & Interaction Design
├── ux-prototype    → Phase 4: Prototyping & Laws of UX
├── ux-validate     → Phase 5: Validation & Testing
├── ux-handoff      → Phase 6: Design-to-Engineering Handoff
└── ux-optimize     → Phase 7: Post-Launch Optimization
```

**Invocation**: Skills are auto-activated by trigger phrases. The master skill activates on general UX/design mentions and can delegate to phase-specific sub-skills.

---

## Agent Roster

| Agent | Phase | Triggers |
|-------|-------|----------|
| ux-phase-navigator | All | "where am I", "what phase", "ready to advance", project status |
| ux-researcher | 1 | "competitive analysis", "research competitors", "UX teardown" |
| ux-artifact-generator | 1-2 | "generate personas", "build journey map", "from these interviews" |
| ux-prototype-reviewer | 4-5 | "review prototype", "heuristic evaluation", "test localhost" |
| ux-accessibility-auditor | 5-6 | "accessibility audit", "WCAG check", "a11y issues" |
| ux-handoff-preparer | 6 | "handoff", "acceptance criteria", "edge cases for engineering" |

---

## Standard Workflow Sequences

### Sequence 1: Greenfield Product (Start to Handoff)

```
1. ux-phase-navigator        → Diagnose: Phase 1 (nothing exists)
2. ux-discover skill         → Stakeholder alignment, research plan
3. ux-researcher agent       → Competitive analysis (autonomous)
4. ux-artifact-generator     → Personas, empathy maps from interviews
5. ux-define skill           → Problem statements, HMW, opportunity mapping
6. ux-phase-navigator        → Gate check: Phase 2 DoD complete?
7. ux-ia skill               → Sitemap, user flows, state inventories
8. ux-prototype skill        → Laws of UX application, wireframe descriptions
9. ux-prototype-reviewer     → Heuristic evaluation (autonomous)
10. ux-accessibility-auditor → WCAG audit (autonomous)
11. ux-validate skill        → Test plan, findings report
12. ux-phase-navigator       → Gate check: Phase 5 DoD complete?
13. ux-handoff-preparer      → Full handoff package (autonomous)
14. ux-optimize skill        → HEART/AARRR setup, experiment backlog
```

### Sequence 2: Mid-Stream Research Synthesis

```
1. ux-phase-navigator        → Diagnose current phase from existing artifacts
2. ux-artifact-generator     → Ingest raw research, generate artifacts
3. ux-define skill           → Validate problem framing against artifacts
4. ux-phase-navigator        → Check Phase 2 DoD, identify gaps
```

### Sequence 3: Validation Sprint

```
1. ux-prototype-reviewer     → Heuristic evaluation of live prototype
2. ux-accessibility-auditor  → Full WCAG 2.1 AA audit
3. ux-validate skill         → Combine findings into validation report
4. ux-phase-navigator        → Check Phase 5 DoD gate
```

### Sequence 4: Rapid Handoff

```
1. ux-phase-navigator        → Verify Phase 5 complete
2. ux-handoff-preparer       → Generate full 4-layer handoff docs
3. ux-accessibility-auditor  → Verify accessibility spec completeness
4. ux-handoff skill          → Final review and QA handoff
```

### Sequence 5: Post-Launch Optimization Setup

```
1. ux-optimize skill         → HEART framework, metrics definition
2. ux-researcher agent       → Competitive benchmarking of live product
3. ux-prototype-reviewer     → Heuristic evaluation of shipped product
4. ux-accessibility-auditor  → Post-ship accessibility baseline
5. ux-optimize skill         → Experiment backlog from findings
```

---

## Complementary Skill Integrations

The master skill references 50+ complementary skills across 5 tiers. Key pairings:

### Tier 1: Always Relevant
- `accessibility` / `fixing-accessibility` — Pair with ux-accessibility-auditor
- `design-principles` — Load alongside ux-discover and ux-define
- `ux-heuristics` — Load alongside ux-prototype-reviewer
- `interface-design` — Pair with ux-ia and ux-prototype

### Tier 2: Phase-Specific Pairings

| UX Phase | Complementary Skills |
|----------|---------------------|
| Phase 1: Discover | `jobs-to-be-done`, `competitive-analysis`, `user-journey-mapper` |
| Phase 2: Define | `jobs-to-be-done`, `acceptance-criteria-creator`, `user-story-generator` |
| Phase 3: IA | `interface-design`, `design-principles`, `web-design-guidelines` |
| Phase 4: Prototype | `ux-heuristics`, `design-everyday-things`, `top-design`, `shadcn` |
| Phase 5: Validate | `accessibility`, `fixing-accessibility`, `performance-lighthouse-runner` |
| Phase 6: Handoff | `design-system-context`, `shadcn-studio`, `web-typography` |
| Phase 7: Optimize | `ab-test-analyzer`, `cro-methodology`, `kpi-definition-helper` |

### Tier 3: Contextual Pairings

| Context | Skills to Load |
|---------|---------------|
| Arabic/RTL/MENA | `arabic-rtl-mena` reference doc |
| Agentic AI products | `agentic-ai-design` reference doc |
| Design system work | `design-system-creation`, `design-system-starter` |
| Mobile/emerging markets | `ios-hig-design`, `web-design-guidelines` |
| Fintech | `design-movements`, `design-masters` |

---

## Context-Adaptive Invocation

The master skill adapts output depth based on inferred or stated context:

| Signal | Inferred Context | Behavior |
|--------|-----------------|----------|
| `package.json` with ≤5 deps | MVP | Lean artifacts, skip enterprise checks |
| CI/CD configs present | Growth | Standard depth |
| Compliance docs, design system tokens | Enterprise | Full rigor, compliance checkpoints |
| Explicit `@MVP` or `@Enterprise` | Override | Always use explicit setting |

---

## Cross-Phase Reference Rules (FR-019)

Each artifact must explicitly cite its upstream dependencies:

```
Phase 3 IA → must cite Phase 2 personas + problem statements
Phase 4 Prototype → must cite Phase 3 flows + state inventories
Phase 5 Validation → must cite Phase 4 prototype + Phase 1 research questions
Phase 6 Handoff → must cite Phase 3 state inventories + Phase 5 findings
Phase 7 Metrics → must cite Phase 6 acceptance criteria + Phase 2 success criteria
```

---

## Invocation Shortcuts

| User Says | Which Skill/Agent Activates |
|-----------|---------------------------|
| "start UX", "begin design", "new product" | ux-phase-navigator → ux-discover |
| "generate persona", "build personas" | ux-artifact-generator |
| "competitor analysis", "research competitors" | ux-researcher |
| "journey map", "empathy map" | ux-artifact-generator |
| "information architecture", "sitemap", "user flow" | ux-ia |
| "wireframe", "prototype", "screen design" | ux-prototype |
| "usability test", "test plan", "heuristic" | ux-validate + ux-prototype-reviewer |
| "accessibility", "WCAG", "a11y" | ux-accessibility-auditor |
| "handoff", "acceptance criteria", "engineering docs" | ux-handoff-preparer |
| "metrics", "HEART", "AARRR", "experiment" | ux-optimize |
| "what phase am I in?", "am I done?" | ux-phase-navigator |

---

## Spec Kit Integration

When working in a Spec Kit-managed project:

```
/speckit.specify → Generates feature spec before UX work starts
/speckit.plan    → Creates implementation plan for UX deliverables
/speckit.tasks   → Breaks UX work into tracked tasks

Then activate UX skills per task:
- Task: "Generate competitive analysis" → ux-researcher agent
- Task: "Create personas" → ux-artifact-generator agent
- Task: "IA + flows" → ux-ia skill
```

The `ux/phase-status.json` file integrates with Spec Kit task tracking — completed phase artifacts map to completed tasks in the task list.
