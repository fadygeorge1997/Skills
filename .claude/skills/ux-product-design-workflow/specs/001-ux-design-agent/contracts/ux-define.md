# Command Contract: /ux.define

**Phase**: 2 — Define & Problem Framing
**Skill**: `skills/ux-define/SKILL.md`

## Purpose

Synthesize research into personas, journey maps, problem statements, HMW statements, and Opportunity Solution Trees.

## Invocation

```
/ux.define [optional: specific artifact to generate or research input]
```

## Inputs

- **Required**: Completed Phase 1 artifacts OR raw research data provided inline
- **Optional**: Specific artifact request (e.g., "generate personas"), interview transcripts, survey data, analytics observations

## Behavior

1. Verify Phase 1 completion (warn if incomplete, allow override).
2. Check `ux/personas/`, `ux/journeys/` for existing artifacts.
3. Present Phase 2 DoD checklist.
4. Generate artifacts in priority order:
   - Personas (2-4 primary, grounded in research evidence)
   - Journey maps (one per primary persona or key scenario)
   - Problem statements ("[User] needs [need] because [insight]")
   - HMW statements (calibrated: not too broad, not too narrow)
   - Opportunity Solution Tree outline
5. Each generated artifact cites evidence sources and tags assumptions.
6. When all DoD items complete: announce Phase 2 done, recommend `/ux.ia`.

## Outputs

| Artifact | Path | Template |
|----------|------|----------|
| Personas | `ux/personas/persona-[name].md` | `templates/persona-template.md` |
| Journey maps | `ux/journeys/journey-[name].md` | `templates/journey-map-template.md` |
| Problem statements | `ux/research/problem-statements.md` | `templates/problem-statement-template.md` |
| HMW statements | `ux/research/hmw-statements.md` | `templates/hmw-template.md` |
| Design brief | `ux/research/design-brief.md` | Inline |

## Guardrails

- Personas MUST be grounded in research evidence, not demographics-only.
- If no research exists, generate "proto-personas" labeled as hypotheses.
- Problem statements MUST follow the "[User] needs [need] because [insight]" format.
- Contradictory evidence MUST be surfaced explicitly with resolution recommendations.

## Context Adaptation

| Mode | Behavior |
|------|----------|
| MVP | 2 personas, 1 journey map, 3-5 problem statements, core HMW only |
| Growth | 3-4 personas, 2-3 journey maps, 5-8 problem statements, HMW + OST |
| Enterprise | 4+ personas with segments, 3+ journey maps with sub-journeys, comprehensive problem statements, full OST |

## Cross-Phase References (FR-019)

| This Phase Artifact | MUST Reference | From Phase |
|---------------------|----------------|------------|
| Personas | Research plan findings (evidence base) | Phase 1 |
| Personas | JTBD statements (jobs each persona performs) | Phase 1 |
| Journey maps | Competitive analysis (where competitors fail = our opportunity) | Phase 1 |
| Problem statements | Empathy map contradictions (Says vs Does) | Phase 1 |
| OST | Four-Risk Gate (value risk informs opportunities) | Phase 1 |

## Tooling Integration (Appendix G)

| Tool/Skill | When to Invoke | What It Provides |
|------------|---------------|------------------|
| `user-journey-mapper` skill | When creating journey maps | Journey map visualization and structure |
| `user-story-generator` skill | When translating insights to user stories | Structured user story generation |
| `jobs-to-be-done` skill | When writing problem statements | Job statement refinement, competitive landscape |
| `hooked-ux` skill | When defining engagement models | Trigger mapping, habit zone analysis |
| `design-sprint` skill | When running Tuesday/Wednesday exercises | Sketch, Decide, storyboard exercises |
| `influence-psychology` skill | When framing behavioral insights | Persuasion principles for user motivation |
| `obviously-awesome` skill | When positioning the product | Competitive alternatives framing |
| `mindmap-generator` skill | When synthesizing themes | Mind map creation for affinity mapping |
| `hundred-million-offers` skill | When constructing value propositions | Offer construction, value equation |

## Skill Reference Files

This contract is implemented by `skills/ux-define/SKILL.md` and draws from:
- `references/discovery-synthesis.md` — Persona development guidelines, journey map template with worked example, problem definition frameworks (5W1H, CATWOE, Root Cause Analysis)
- `references/frameworks.md` — Double Diamond (Define phase), Opportunity Solution Trees, Continuous Discovery Habits
- `references/competitive-analysis.md` — Value Proposition Canvas, positioning statement template (for design brief)

## Persona Quality Checklist

Every generated persona MUST pass:
- [ ] Has a JTBD statement grounded in research
- [ ] Pain points cite specific evidence sources
- [ ] Behaviors are observable (not demographic assumptions)
- [ ] Representative quote is a real quote (or clearly marked as constructed)
- [ ] Tech comfort level is justified by behavioral evidence
- [ ] Distinct from other personas (no overlapping archetypes)

## Problem Definition Frameworks

When generating problem statements, the agent MAY apply these frameworks from `references/discovery-synthesis.md`:
- **5W1H**: Who, What, When, Where, Why, How — for comprehensive problem scoping
- **CATWOE**: Clients, Actors, Transformation, Worldview, Owners, Environment — for stakeholder perspective analysis
- **Root Cause (5 Whys)**: Iterative "why" questioning to find underlying causes, not symptoms

## Journey Map Requirements

Journey maps MUST include per `references/discovery-synthesis.md`:
- Emotional arc across stages (not just actions)
- Key Moments of Truth (critical succeed-or-fail points)
- Evidence sources per stage (tagged `[EVIDENCE]` or `[ASSUMPTION]`)
- Opportunities column linked to competitive analysis gaps from Phase 1
