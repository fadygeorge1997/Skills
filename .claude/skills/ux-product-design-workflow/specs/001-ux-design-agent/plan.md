# Implementation Plan: UX & Product Design Agent

**Branch**: `001-ux-design-agent` | **Date**: 2026-03-13 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-ux-design-agent/spec.md`

## Summary

Build an AI-powered UX & Product Design Agent implemented as a set of Spec Kit-integrated skill files and slash commands. The agent guides product teams through a 7-phase UX workflow (Discovery through Post-Launch Optimization), generating concrete artifacts (personas, journey maps, IA, test plans, metrics frameworks) from user input and repository context. It enforces phase progression with Definition of Done gates, applies the Ethical Design Hierarchy and Four-Risk Gate, and adapts output depth to team context (MVP vs Enterprise).

The implementation uses markdown-based skill files with reference documents, slash commands per phase, and a structured `ux/` directory for persisted artifacts — no custom backend, no standalone application.

## Technical Context

**Language/Version**: Markdown + Bash/PowerShell scripting (skill files, templates, automation scripts)
**Primary Dependencies**: Claude Code skill system (SKILL.md format), Spec Kit workflow (.specify/), optional @anthropic-ai/claude-agent-sdk for MCP tool exposure
**Tooling Ecosystem**: 9 MCP servers (AccessLint, Playwright, Chrome DevTools, Claude Preview, shadcn-ui, shadcn-community, Storybook-Figma, Context7, Google Drive), 50+ complementary skills across 5 tiers (see spec.md Appendix G), browser automation agents (Claude in Chrome, Playwright, Chrome DevTools)
**Storage**: File-based markdown in `ux/` directory tree, version-controlled alongside code
**Testing**: Manual validation via Definition of Done checklists per phase; automated checklist validation via PowerShell scripts
**Target Platform**: Claude Code (primary), any agentic IDE supporting SKILL.md conventions (Gemini CLI, Windsurf, Cursor)
**Project Type**: AI agent skill system (collection of prompt-based skills + reference docs + templates + automation)
**Performance Goals**: First valuable artifact (persona, problem statement, or research plan) in <15 minutes from first invocation
**Constraints**: No production backend code generation; all outputs are markdown/JSON artifacts; no autonomous research execution
**Scale/Scope**: 7 phase-specific skills, 10 reference documents, 24 templates, 7 DoD checklists, 1 master SKILL.md orchestrator, 21 artifact types, 50+ complementary skill integrations, 9 MCP server integrations

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Ethical Design Hierarchy | PASS | Agent enforces safety > function > delight in all recommendations. FR-009 requires Four-Risk Gate. FR-012 requires WCAG 2.1 AA. |
| II. Four-Risk Gate | PASS | FR-009 explicitly requires value/usability/feasibility/viability checks before advancing past discovery. Each phase skill includes risk checkpoint. |
| III. Product Triad Collaboration | PASS | Artifacts designed for shared consumption by PM, Design, and Engineering. Handoff phase (Phase 6) explicitly bridges Design-Engineering. |
| IV. UX Quality & Interaction Standards | PASS | FR-011 requires Laws of UX application. FR-006 requires all 7+ interaction states. FR-012 requires WCAG 2.1 AA. |
| V. Evidence Over Assumption | PASS | FR-005 requires explicit evidence vs assumption tagging. Edge case handles contradictory data. Proto-personas labeled as hypotheses. |
| VI. AI as Co-Pilot | PASS | FR-010 refuses production code generation. Agent generates artifacts for human review, not autonomous decisions. Guardrails require clarifying questions over hallucination. |
| Workflow Frameworks | PASS | FR-013 implements all 7 phases (Double Diamond macro + Lean UX loops). FR-007 implements Product Kata for post-launch. JTBD is the core mental model throughout. |
| Operating Rules | PASS | FR-003 enforces consistent output formats. FR-008 implements context-adaptive depth. Progressive disclosure via phase gating (FR-004). |

**Gate result: PASS** — All 6 principles and 2 sections satisfied. No violations.

## Project Structure

### Documentation (this feature)

```text
specs/001-ux-design-agent/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (slash command contracts)
│   ├── ux-discover.md
│   ├── ux-define.md
│   ├── ux-ia.md
│   ├── ux-prototype.md
│   ├── ux-validate.md
│   ├── ux-handoff.md
│   └── ux-optimize.md
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Phase 2 output (/speckit.tasks - NOT created here)
```

### Source Code (repository root)

```text
ux-product-design-workflow/
├── SKILL.md                          # Master orchestrator skill (already exists)
├── references/                       # Deep-dive reference docs (already exist)
│   ├── frameworks.md
│   ├── discovery-synthesis.md
│   ├── competitive-analysis.md
│   ├── ideation-prototyping.md
│   ├── laws-of-ux.md
│   ├── arabic-rtl-mena.md
│   ├── usability-testing.md
│   ├── metrics-optimization.md
│   ├── agentic-ai-design.md
│   └── design-handoff.md
├── skills/                           # NEW: Phase-specific sub-skills
│   ├── ux-discover/
│   │   └── SKILL.md                  # Phase 1: Discovery & Research
│   ├── ux-define/
│   │   └── SKILL.md                  # Phase 2: Define & Problem Framing
│   ├── ux-ia/
│   │   └── SKILL.md                  # Phase 3: IA & Interaction Design
│   ├── ux-prototype/
│   │   └── SKILL.md                  # Phase 4: Prototyping & Laws of UX
│   ├── ux-validate/
│   │   └── SKILL.md                  # Phase 5: Validation & Testing
│   ├── ux-handoff/
│   │   └── SKILL.md                  # Phase 6: Design-to-Eng Handoff
│   └── ux-optimize/
│       └── SKILL.md                  # Phase 7: Post-Launch Optimization
├── templates/                        # NEW: Reusable artifact templates
│   ├── persona-template.md
│   ├── journey-map-template.md
│   ├── empathy-map-template.md        # 6 quadrants: Says, Thinks, Does, Feels, Sees, Hears
│   ├── problem-statement-template.md
│   ├── hmw-template.md
│   ├── research-plan-template.md
│   ├── sitemap-template.md
│   ├── user-flow-template.md
│   ├── state-inventory-template.md
│   ├── test-plan-template.md
│   ├── heuristic-evaluation-template.md
│   ├── handoff-checklist-template.md
│   ├── goals-signals-metrics-template.md
│   ├── experiment-backlog-template.md
│   ├── four-risk-gate-template.md
│   ├── competitive-analysis-template.md
│   ├── opportunity-solution-tree-template.md
│   ├── jtbd-statement-template.md
│   ├── findings-report-template.md
│   ├── edge-case-catalog-template.md
│   ├── participant-screener-template.md  # Screener for usability test recruitment
│   ├── north-star-metric-template.md     # NSM definition + input metric tree
│   ├── design-brief-template.md          # Problem summary + constraints + risk gate
│   └── acceptance-criteria-template.md   # Given/When/Then (Gherkin) format
├── checklists/                       # NEW: Phase DoD checklists
│   ├── phase-1-discovery-dod.md
│   ├── phase-2-define-dod.md
│   ├── phase-3-ia-dod.md
│   ├── phase-4-prototype-dod.md
│   ├── phase-5-validate-dod.md
│   ├── phase-6-handoff-dod.md
│   └── phase-7-optimize-dod.md
├── integrations/                     # NEW: Tooling integration guides
│   ├── mcp-tools-guide.md           # MCP server tool usage per phase
│   └── skill-chaining-guide.md      # Skill invocation sequences per workflow
└── .specify/                         # Spec Kit integration
    ├── memory/
    │   └── constitution.md           # Already created
    └── templates/
        ├── plan-template.md
        ├── spec-template.md
        └── tasks-template.md
```

### User Project Output (generated in consuming repos)

```text
ux/                                   # Created in user's project by agent
├── personas/
│   ├── persona-1-name.md
│   └── persona-2-name.md
├── journeys/
│   ├── journey-1-name.md
│   └── journey-2-name.md
├── research/
│   ├── research-plan.md
│   ├── competitive-analysis.md
│   ├── empathy-maps.md               # 6 quadrants per map
│   ├── jtbd-statements.md
│   ├── participant-screener.md       # Recruitment screener for usability tests
│   └── design-brief.md              # Problem summary + four-risk gate summary
├── ia/
│   ├── sitemap.md                    # Navigation zones + Hick's Law check
│   ├── user-flows.md                 # Happy path + error paths + edge cases
│   └── state-inventories.md          # All 7+ states per interactive element
├── validation/
│   ├── test-plan.md                  # Task-based scenarios, not feature-based
│   ├── heuristic-evaluation.md       # Nielsen's 10, severity-rated (0-4)
│   ├── accessibility-audit.md        # WCAG 2.1 AA POUR checklist
│   ├── findings-report.md            # Severity-rated with impact-effort matrix
│   └── recommendations.md           # Prioritized by impact-effort
├── handoff/
│   ├── handoff-checklist.md          # 4-layer documentation (Context/Flow/Spec/Edge)
│   ├── edge-case-catalog.md
│   ├── state-documentation.md
│   ├── accessibility-spec.md         # ARIA roles, keyboard shortcuts, focus management
│   └── acceptance-criteria.md        # Given/When/Then (Gherkin) format
├── metrics/
│   ├── heart-framework.md            # 5 dimensions with Goals/Signals/Metrics/Targets
│   ├── aarrr-funnel.md              # Stage-by-stage with drop-off hypotheses
│   ├── goals-signals-metrics.md
│   ├── experiment-backlog.md         # Prioritized with hypothesis + success criteria
│   ├── north-star-metric.md          # NSM + input metric tree + counter-metrics
│   └── product-kata-[date].md        # 2-4 week cycle plans (ongoing)
├── risk-assessments/
│   └── four-risk-gate.md
└── phase-status.json                 # Phase tracking metadata
```

**Structure Decision**: This is a skill-system project (not a traditional app). The primary deliverables are SKILL.md files, markdown templates, reference docs, and checklists. The `ux/` directory structure is what the agent *creates in consuming projects* — it's documented here as a contract but not pre-created in this repo.

## Constitution Check — Post-Design Re-evaluation

*Re-check after Phase 1 design completion (data-model.md, contracts/, quickstart.md).*

| Principle | Status | Post-Design Evidence |
|-----------|--------|---------------------|
| I. Ethical Design Hierarchy | PASS | All 7 contracts enforce safety > function > delight ordering. `ux-prototype` contract requires Ethical Design Hierarchy check before Laws of UX application. `ux-handoff` contract requires accessibility requirements (WCAG 2.1 AA) in every handoff doc. FR-012 expanded to cover all design-phase outputs. |
| II. Four-Risk Gate | PASS | `four-risk-gate-template.md` defined in data-model.md with pass/fail/incomplete per risk dimension. `ux-discover` contract includes risk gate as step 6. All phase transitions check risk status in `phase-status.json`. |
| III. Product Triad Collaboration | PASS | Artifact schemas designed for shared consumption: persona templates include engineering-relevant fields (technical constraints, API touchpoints). Handoff contract produces acceptance criteria in Given/When/Then format for engineering. Metrics contract produces GSM tables consumable by PM, Design, and Engineering. |
| IV. UX Quality & Interaction Standards | PASS | `ux-ia` contract mandates all 7+ states per interactive element. `ux-prototype` contract requires Laws of UX application with citations. State inventory template in data-model.md covers: default, empty, loading, partial, error, success, offline, permission. FR-020 adds RTL/MENA patterns. |
| V. Evidence Over Assumption | PASS | Evidence tagging system defined in data-model.md: `[EVIDENCE]`, `[ASSUMPTION]`, `[MEASURED]`, `[CONTRADICTION]`. All artifact schemas include `confidence` field (evidence-backed/assumption/hypothesis). Proto-persona handling explicitly defined in edge cases. FR-023 requires empathy map entries to be traceable. |
| VI. AI as Co-Pilot | PASS | All contracts include guardrails section preventing autonomous decisions. `ux-discover` refuses to fabricate research data. `ux-validate` generates test plans for humans to execute. `ux-handoff` produces documentation for engineering review, not auto-generated code. FR-010 explicitly refuses production code. |
| Workflow Frameworks | PASS | 7 contracts map 1:1 to the 7 phases. Context-adaptive output rules defined in data-model.md with MVP/Growth/Enterprise mode impact table covering all 7 behavioral aspects. Product Kata explicitly implemented in `ux-optimize` contract. |
| Operating Rules | PASS | All contracts produce artifacts (not theory). Context depth adapts per data-model.md inference rules. Progressive disclosure enforced via DoD gating in `phase-status.json`. Cross-phase referencing mandated by FR-019. Spec Kit integration defined in FR-021 and US8. |

**Post-design gate result: PASS** — All 6 principles and 2 sections remain satisfied after Phase 1 design. Enhanced spec adds FR-016 through FR-023, US6-US8, and 4 additional edge cases — all consistent with constitution principles.

## Complexity Tracking

No violations detected. No complexity justifications needed.
