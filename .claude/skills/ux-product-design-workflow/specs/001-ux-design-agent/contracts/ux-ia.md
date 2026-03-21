# Command Contract: /ux.ia

**Phase**: 3 — Information Architecture & Interaction Design
**Skill**: `skills/ux-ia/SKILL.md`

## Purpose

Structure the product's information architecture, user flows, task flows, and interaction state inventories based on defined problem statements and personas.

## Invocation

```
/ux.ia [optional: specific screen/feature or IA focus area]
```

## Inputs

- **Required**: Completed personas and problem statements (Phase 2)
- **Optional**: Specific feature/screen to design IA for, existing navigation structure, content inventory

## Behavior

1. Verify Phase 2 completion (warn if incomplete).
2. Check `ux/ia/` for existing artifacts.
3. Present Phase 3 DoD checklist.
4. Generate artifacts in order:
   - Sitemap / app map organized by user mental model (not org chart)
   - User flows for core scenarios (including decision points, error paths)
   - Task flows for specific interactions
   - State inventories for each primary screen (all 7+ states)
   - Wireframe descriptions (annotated, screen-by-screen)
5. Recommend card sorting approach for IA validation.
6. When all DoD items complete: recommend `/ux.prototype`.

## Outputs

| Artifact | Path | Template |
|----------|------|----------|
| Sitemap | `ux/ia/sitemap.md` | `templates/sitemap-template.md` |
| User flows | `ux/ia/user-flows.md` | `templates/user-flow-template.md` |
| State inventories | `ux/ia/state-inventories.md` | `templates/state-inventory-template.md` |
| Wireframe descriptions | `ux/ia/wireframe-descriptions.md` | Inline |
| Navigation taxonomy | `ux/ia/navigation-taxonomy.md` | Inline |

## Guardrails

- IA MUST be organized by user mental model, not internal org structure.
- Every screen description MUST include all 7+ states (default, empty, loading, partial, error, success, offline, permission).
- User flows MUST include error paths and edge cases, not just happy path.
- Apply Hick's Law: max 5-7 navigation items per level.
- Apply Jakob's Law: recommend platform conventions before custom patterns.
- All user flows MUST reference personas by name (FR-019 cross-phase referencing).
- Sitemap MUST reference problem statements to justify navigation structure.

## Context Adaptation

| Mode | Behavior |
|------|----------|
| MVP | 1 sitemap, 2-3 core user flows, state inventories for primary screens only |
| Growth | Full sitemap with secondary nav, 5-8 user flows including edge cases, state inventories for all screens |
| Enterprise | Sitemap with navigation zones + governance model, comprehensive flows with decision trees, state inventories + compliance states (audit, data-retention) |

## Tooling Integration (Appendix G)

| Tool/Skill | When to Invoke | What It Provides |
|------------|---------------|------------------|
| `ui-design-patterns` skill | When selecting interaction patterns | Navigation, form, data display, feedback patterns |
| `design-principles` skill | When structuring layouts | Gestalt, hierarchy, visual balance, alignment |
| `ux-heuristics` skill | When evaluating IA decisions | Nielsen's 10, Krug's Laws, severity ratings |
| `ui-ux-pro-max` skill | When making style/layout decisions | Style selection, typography, layout rules; run `search.py` |
| `interface-design` skill | When designing screen layouts | Interface design principles |
| `mermaid-flowchart-generator` skill | When creating user flow diagrams | Mermaid flowchart syntax |
| `mermaid-state-diagram-creator` skill | When designing state machines | State diagram generation |
| `shadcn-ui` MCP | When looking up component patterns | Component library lookup, audit checklists |

## Skill Reference Files

This contract is implemented by `skills/ux-ia/SKILL.md` and draws from:
- `references/ideation-prototyping.md` — IA principles, card sorting (4 types: Open, Closed, Hybrid, Tree Testing), user flows & task flows, state design, SCAMPER, Crazy 8s, Design Studio, RICE scoring, feature prioritization
- `references/frameworks.md` — Design Sprint (5-day), convergence & decision techniques
- `references/laws-of-ux.md` — Hick's Law (navigation item limits), Jakob's Law (platform conventions), Gestalt principles (visual grouping for IA)

## Card Sorting Validation

When recommending IA validation, specify the appropriate card sorting type:

| Type | When to Use | Participants | Output |
|------|-------------|-------------|--------|
| **Open** | No existing IA; need to discover user mental models | 15-30 | Category names and groupings |
| **Closed** | Existing categories; testing if users can find items | 15-30 | Findability scores per item |
| **Hybrid** | Existing IA with potential new categories | 15-30 | Validation + new category discovery |
| **Tree Testing** | Validate navigation hierarchy without visual design influence | 50+ | Task completion rates per path |

## Cross-Phase References (FR-019)

| This Phase Artifact | MUST Reference | From Phase |
|---------------------|----------------|------------|
| Sitemap | Problem statements (navigation justification) | Phase 2 |
| User flows | Personas by name (who performs the flow) | Phase 2 |
| User flows | Journey map pain points (where flows must reduce friction) | Phase 2 |
| State inventories | Persona tech comfort level (error message complexity) | Phase 2 |

## Prioritization Framework

When the agent recommends feature or flow prioritization, use RICE scoring from `references/ideation-prototyping.md`:
- **Reach**: How many users will this impact per quarter?
- **Impact**: How much will it move the target metric? (Massive=3x, High=2x, Medium=1x, Low=0.5x, Minimal=0.25x)
- **Confidence**: How certain are we? (High=100%, Medium=80%, Low=50%)
- **Effort**: Person-months to implement
- **Score**: (Reach × Impact × Confidence) ÷ Effort
