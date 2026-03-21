# Command Contract: /ux.discover

**Phase**: 1 — Discovery & Research
**Skill**: `skills/ux-discover/SKILL.md`

## Purpose

Guide the user through discovery research: stakeholder alignment, research planning, JTBD mapping, competitive analysis, and empathy mapping.

## Invocation

```
/ux.discover [optional: research focus or domain context]
```

## Inputs

- **Required**: None (agent prompts for context if missing)
- **Optional**: Research focus area, target user segment, domain context, existing research data (pasted or file path)

## Behavior

1. Check `ux/phase-status.json` — if exists, load current state. If not, initialize with Phase 1 in-progress.
2. Check for existing research artifacts in `ux/research/`. If found, offer to build on them.
3. Present Phase 1 DoD checklist with current completion status.
4. Based on what's missing, generate the most impactful next artifact:
   - If no research plan: generate `ux/research/research-plan.md`
   - If no JTBD statements: generate `ux/research/jtbd-statements.md`
   - If no competitive analysis: generate `ux/research/competitive-analysis.md`
   - If no empathy maps: generate `ux/research/empathy-maps.md`
5. If user provides raw research data: synthesize into structured artifact with evidence tagging.
6. After each artifact, update DoD checklist and show remaining items.
7. When all DoD items are done/skipped: announce Phase 1 complete, recommend `/ux.define`.

## Outputs

| Artifact | Path | Template |
|----------|------|----------|
| Research plan | `ux/research/research-plan.md` | `templates/research-plan-template.md` |
| JTBD statements | `ux/research/jtbd-statements.md` | Inline (JTBD format from SKILL.md) |
| Competitive analysis | `ux/research/competitive-analysis.md` | Inline (feature matrix + UX teardown) |
| Empathy maps | `ux/research/empathy-maps.md` | `templates/empathy-map-template.md` |
| Opportunity backlog | `ux/research/opportunity-backlog.md` | Inline (ranked list) |
| Phase status | `ux/phase-status.json` | Schema from data-model.md |

## Guardrails

- All synthesized insights MUST be tagged with evidence level (assumption/observed/measured).
- If user has no raw research data, generate "proto" artifacts clearly labeled as hypotheses.
- MUST NOT advance to Phase 2 if DoD items are pending without explicit user override.
- MUST apply Four-Risk Gate checkpoint at end of Phase 1.

## Context Adaptation

| Mode | Behavior |
|------|----------|
| MVP | 3-5 interview targets, 2-week timeline, 3-5 competitors, essential empathy map fields |
| Growth | 5-8 interview targets, 3-4 week timeline, 5-8 competitors, full empathy maps |
| Enterprise | 8-15 interview targets, 4-6 week timeline, 8+ competitors, empathy maps + data sources + compliance |

## Cross-Phase References (FR-019)

Phase 1 is the origin — its artifacts are referenced by all subsequent phases. Discovery outputs MUST be structured for downstream consumption:
- JTBD statements MUST use the canonical format so Phase 2 can derive personas
- Competitive analysis MUST include UX patterns so Phase 4 can apply Jakob's Law
- Empathy maps MUST tag each entry with source so Phase 5 test plans can trace back
- Four-Risk Gate MUST capture value risk evidence so all phases can check alignment

## Tooling Integration (Appendix G)

| Tool/Skill | When to Invoke | What It Provides |
|------------|---------------|------------------|
| `jobs-to-be-done` skill | When framing user motivation and job statements | Forces of Progress, Big Hire/Little Hire, competitive landscape mapping |
| `competitive-ads-extractor` skill | During competitive analysis | Competitor ad strategy and messaging extraction |
| `lead-research-assistant` skill | When building user segments | Audience research and profiling |
| `survey-creator` skill | When planning primary research instruments | Research survey design |
| `content-research-writer` skill | When gathering secondary research | Structured web-based content research |
| `design-sprint` skill | When running compressed discovery (Monday exercises) | Map, HMW notes, expert interview structure |
| `blue-ocean-strategy` skill | When analyzing competitive landscape | Value innovation canvas, non-customer analysis |
| `Claude in Chrome` MCP | During competitive UX teardowns | Live page inspection, interaction recording |
| `context7` MCP | When looking up framework documentation | Up-to-date library/method docs |
| `google_drive` MCP | When accessing stakeholder briefs | Document search and retrieval |

## Skill Reference Files

This contract is implemented by `skills/ux-discover/SKILL.md` and draws from:
- `references/discovery-synthesis.md` — JTBD framework, empathy mapping (6 quadrants), persona development, journey mapping, affinity mapping, cognitive prompting, bias mitigation, stakeholder interview guide
- `references/competitive-analysis.md` — Direct/indirect/aspirational competitors, SWOT, Porter's Five Forces, feature comparison matrix, UX teardown methodology, value proposition canvas, Blue Ocean strategy
- `references/frameworks.md` — Double Diamond (Discover/Define phases), Continuous Discovery Habits, DIKW Pyramid

## Research Method Selection Guide

| What You Need to Learn | Recommended Method | Minimum Viable Version |
|------------------------|--------------------|----------------------|
| User motivations, mental models | Semi-structured interviews | 5 interviews, 30 min each |
| Real-world behavior in context | Contextual inquiry | 3 observation sessions |
| Quantitative preferences/priorities | Survey | 50+ responses |
| Information architecture expectations | Card sorting (open) | 15 participants |
| Competitor UX patterns | Competitive teardown | 3-5 competitors |
| Market size, segment validation | Desk research + analytics | Available data analysis |
| Longitudinal behavior patterns | Diary study | 5-10 participants, 1-2 weeks |
| Stakeholder alignment | Stakeholder interviews | 3-5 key stakeholders, 45 min each |

## Empathy Map Format

Empathy maps MUST use 6 quadrants (not 4): Says, Thinks, Does, Feels, Sees, Hears. The Sees and Hears quadrants capture environmental context per `references/discovery-synthesis.md`. Each entry MUST be tagged with evidence source.

## Synthesis Methods

When synthesizing research data, the agent MUST offer:
- **Affinity mapping**: Group observations by theme, identify patterns across participants (minimum 3 participants showing same pattern = systemic)
- **DIKW Pyramid**: Transform raw Data → Information → Knowledge → Wisdom
- **Cognitive prompting**: Use structured AI synthesis with bias checks per `references/discovery-synthesis.md`
