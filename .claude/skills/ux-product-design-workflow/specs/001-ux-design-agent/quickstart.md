# Quickstart: UX & Product Design Agent

## Prerequisites

- Claude Code (or compatible agentic IDE) installed
- The `ux-product-design-workflow` skill installed (via `.claude/skills/` or equivalent)
- A project directory where you want UX artifacts generated

## 1. First Invocation (< 2 minutes)

Start by telling the agent about your project:

```
/ux.discover I'm building a mobile fintech app for first-time
digital payment users in Egypt
```

The agent will:
1. Detect you're starting fresh (no `ux/` directory exists)
2. Initialize `ux/phase-status.json` in MVP mode
3. Generate a research plan at `ux/research/research-plan.md`
4. Show the Phase 1 Definition of Done checklist

## 2. Generate Your First Artifact (< 15 minutes)

If you have interview notes or research, paste them:

```
/ux.define Here are my interview notes:
- User A (28, accountant): "I'd rather wait in line than lose
  money to a glitch." Pays bills at bank branch.
- User B (34, teacher): Tried mobile banking once, got confused
  by fees. Went back to cash.
- User C (22, student): Uses InstaPay daily but doesn't trust
  it for large amounts.
```

The agent produces:
- 2-3 personas grounded in your interview data
- Problem statements in "[User] needs [need] because [insight]" format
- Each insight tagged as `[EVIDENCE: interview]` or `[ASSUMPTION]`

## 3. Navigate Phases

The agent always tells you which phase you're in and what's next:

| Command | Phase | What You Get |
|---------|-------|-------------|
| `/ux.discover` | 1. Discovery | Research plans, JTBD, competitive analysis, empathy maps |
| `/ux.define` | 2. Define | Personas, journey maps, problem statements, HMW |
| `/ux.ia` | 3. IA & Interaction | Sitemaps, user flows, state inventories, wireframe descriptions |
| `/ux.prototype` | 4. Prototyping | Laws of UX application, design system mapping, RTL patterns |
| `/ux.validate` | 5. Validation | Test plans, heuristic evaluations, accessibility audits |
| `/ux.handoff` | 6. Handoff | Annotated specs, edge-case catalogs, acceptance criteria |
| `/ux.optimize` | 7. Optimize | HEART/AARRR metrics, experiment backlogs, Product Kata |

## 4. Context Modes

Set your context explicitly or let the agent infer it:

```
/ux.discover --mode mvp       # Lean, scrappy output
/ux.discover --mode enterprise # Full rigor + compliance
```

If you don't set a mode, the agent infers from your project:
- Few files, no CI → MVP mode
- Design tokens, CI/CD, compliance docs → Enterprise mode

## 5. Output Structure

All artifacts are saved under `ux/` in your project:

```
ux/
├── personas/           # Persona profiles
├── journeys/           # Journey maps
├── research/           # Research plans, JTBD, competitive analysis
├── ia/                 # Sitemaps, flows, state inventories
├── validation/         # Test plans, findings, accessibility
├── handoff/            # Engineering handoff docs
├── metrics/            # HEART, AARRR, experiments
├── risk-assessments/   # Four-Risk Gate evaluations
└── phase-status.json   # Phase tracking
```

## 6. Spec Kit Integration

The UX agent works alongside Spec Kit commands:

- During `/speckit.specify`: invoke `/ux.define` to generate problem statements and user segments that feed into the spec.
- During `/speckit.plan`: invoke `/ux.ia` to get IA constraints and flow requirements for the implementation plan.
- During `/speckit.tasks`: UX work items (research, design, testing, handoff) appear alongside engineering tasks.

## 7. Cross-Phase Referencing (FR-019)

Each phase's artifacts MUST reference earlier phase outputs. The agent enforces this automatically:

| Phase | Must Reference |
|-------|---------------|
| Define (2) | Discovery research findings, competitive gaps |
| IA (3) | Personas, journey map stages, problem statements |
| Prototype (4) | State inventories, IA decisions, Laws of UX |
| Validate (5) | Journey map pain points, persona segments, state inventories |
| Handoff (6) | State inventories, heuristic findings, test plan scenarios |
| Optimize (7) | Problem statements, journey map stages, heuristic findings |

## 8. Key Phase Features

Each phase skill includes specialized capabilities:

- **Discovery**: Empathy maps (6 quadrants), JTBD statements, synthesis methods (affinity mapping, DIKW Pyramid)
- **Define**: Problem definition frameworks (5W1H, CATWOE, Root Cause), journey map emotional arcs
- **IA**: Card sorting validation (Open/Closed/Hybrid/Tree Testing), RICE prioritization scoring
- **Prototype**: Fidelity progression (Low/Mid/High-fi), Gestalt principles checklist, dark patterns check
- **Validate**: Think-aloud protocol (3 levels), participant recruitment guide, inclusive testing checklist
- **Handoff**: Staggered sprint pipeline (N-2 → N+1), 4-layer documentation, Given/When/Then acceptance criteria
- **Optimize**: North Star Metric + input metric tree, counter-metrics, weekly improvement cadence

## 9. Tooling Integration

The agent automatically detects and leverages connected MCP servers and complementary skills:

### MCP Servers (auto-detected when connected)

| Server | What It Adds | Phase |
|--------|-------------|-------|
| **AccessLint** | Automated WCAG auditing of HTML/URLs | Validate, Handoff |
| **Playwright** | Browser-automated interaction testing | Prototype, Validate |
| **Chrome DevTools** | Lighthouse audits, performance tracing | Validate, Optimize |
| **Claude Preview** | Live HTML prototype preview and testing | Prototype, Validate |
| **shadcn-ui** | Component library lookup and audit checklists | IA, Prototype |
| **Storybook-Figma** | Design-to-code bridging, Figma integration | Prototype, Handoff |
| **Context7** | Up-to-date library documentation | All phases |

### Complementary Skills (invoked automatically when relevant)

The agent chains 50+ skills across phases. Key examples:

- **Discovery**: `jobs-to-be-done` for job statements, `competitive-ads-extractor` for competitive intel
- **Define**: `user-journey-mapper` for journey maps, `hooked-ux` for engagement models
- **IA**: `ui-design-patterns` for interaction patterns, `ux-heuristics` for expert review
- **Prototype**: `all-in-one-ui-ux-design` for design execution, `design-system-creation` for component libraries
- **Validate**: `accessibility` for WCAG compliance, `cro-methodology` for conversion optimization
- **Handoff**: `figma:implement-design` for Figma-to-code, `acceptance-criteria-creator` for Given/When/Then
- **Optimize**: `ab-test-analyzer` for experiment analysis, `funnel-analysis-builder` for drop-off diagnosis

> Full mapping: see spec.md Appendix G (Tooling Ecosystem) and Appendix H (Skills Matrix)

## 10. Validation

To verify the agent is working correctly:

1. Run `/ux.discover` on an empty project → should get a research plan with evidence tags
2. Run `/ux.define` with sample interview data → should get personas with `[EVIDENCE: interview]` or `[ASSUMPTION]` tags
3. Run `/ux.ia` for a simple feature → should get state inventory with all 7+ states and RICE-scored priorities
4. Run `/ux.validate` → should get task-based test scenarios (not feature-based) with severity ratings (0-4)
5. Check that `ux/phase-status.json` tracks progress correctly
6. Verify the agent warns when trying to skip phases
7. Verify cross-phase references: e.g., handoff docs reference Phase 3 state inventories and Phase 5 heuristic findings
