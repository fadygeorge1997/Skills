# Command Contract: /ux.prototype

**Phase**: 4 — Prototyping & Interaction Design Refinement
**Skill**: `skills/ux-prototype/SKILL.md`

## Purpose

Guide high-fidelity design by systematically applying Laws of UX, design system integration, RTL/MENA patterns, and micro-interaction specifications.

## Invocation

```
/ux.prototype [optional: specific screen/component or design concern]
```

## Inputs

- **Required**: Completed IA and wireframe descriptions (Phase 3)
- **Optional**: Design system token file, Figma references, RTL/Arabic requirements, specific Laws of UX to apply

## Behavior

1. Verify Phase 3 completion.
2. Present Phase 4 DoD checklist.
3. For each screen/component:
   - Apply Laws of UX systematically (Fitts's, Hick's, Jakob's, Miller's, Doherty, Peak-End, Zeigarnik, Aesthetic-Usability)
   - Specify micro-interactions with purpose (not decorative)
   - Map to design system tokens (primitive > semantic > component)
   - Generate responsive behavior rules per breakpoint
   - If RTL: apply Arabic mirroring rules from `references/arabic-rtl-mena.md`
4. Produce annotation documentation for each screen.
5. Run Nielsen's 10 heuristics self-check before recommending user testing.
6. When complete: recommend `/ux.validate`.

## Outputs

| Artifact | Path | Template |
|----------|------|----------|
| UX audit per screen | `ux/ia/ux-audit-[screen].md` | Inline |
| Design system mapping | `ux/ia/design-system-mapping.md` | Inline |
| Responsive rules | `ux/ia/responsive-rules.md` | Inline |
| Heuristic self-check | `ux/validation/heuristic-self-check.md` | `templates/heuristic-evaluation-template.md` |

## Guardrails

- MUST NOT generate visual designs or pixel-level specifications — describe patterns, tokens, and behavioral rules.
- Laws of UX MUST be applied as concrete design actions, not abstract principles.
- RTL mirroring: phone numbers, math, and LTR content MUST stay LTR.
- Design system tokens MUST use 3-tier hierarchy (primitive > semantic > component).
- Micro-interaction timing MUST follow Doherty Threshold (<400ms for feedback).
- All design recommendations MUST reference the persona they serve (FR-019).

## Context Adaptation

| Mode | Behavior |
|------|----------|
| MVP | Core Laws of UX only (Fitts's, Hick's, Jakob's), basic responsive rules, no design system mapping |
| Growth | Full Laws of UX application, responsive rules with breakpoints, design system token mapping |
| Enterprise | Full Laws of UX + RTL/MENA patterns, responsive + platform-specific (iOS HIG, Material), comprehensive design system mapping + accessibility token layer |

## Cross-Phase References (FR-019)

| This Phase Artifact | MUST Reference | From Phase |
|---------------------|----------------|------------|
| UX audit per screen | State inventories (verify all states styled) | Phase 3 |
| Design system mapping | User flow decision points (interaction patterns) | Phase 3 |
| Responsive rules | Persona device preferences | Phase 2 |
| Heuristic self-check | Journey map pain points (verify addressed) | Phase 2 |

## Tooling Integration (Appendix G)

| Tool/Skill | When to Invoke | What It Provides |
|------------|---------------|------------------|
| `all-in-one-ui-ux-design` skill | Primary design execution | End-to-end design system: build/redesign/audit/design-system/flow modes |
| `design-system-creation` skill | When building component libraries | Component docs, governance, foundation layer |
| `design-engineer-mindset` skill | When optimizing prototype performance | Rendering pipeline, GPU acceleration, design tokens as code |
| `ui-ux-pro-max` skill | When selecting styles/colors/fonts | Run `search.py --design-system` for recommendations |
| `baseline-ui` skill | When bootstrapping component sets | Baseline UI component templates |
| `artifacts-builder` skill | When building clickable prototypes | Interactive artifact generation |
| `theme-factory` skill | When exploring visual directions | Design theme generation |
| `refactoring-ui` skill | When improving existing designs | UI refactoring principles |
| `web-typography` skill | When defining type hierarchy | Typography systems and font pairing |
| `design-movements` skill | When selecting aesthetic direction | Design movement references |
| `made-to-stick` skill | When crafting UI copy | Message stickiness principles |
| `storybrand-messaging` skill | When structuring narrative flow | Narrative framework for UI copy |
| `shadcn-ui` MCP | When integrating components | Component library lookup |
| `shadcn-community` MCP | When exploring themes | Community themes and components |
| `storybook-figma` MCP | When bridging design-code | Figma integration, component context |
| `Claude Preview` MCP | When previewing HTML prototypes | Live preview and interactive testing |

## Skill Reference Files

This contract is implemented by `skills/ux-prototype/SKILL.md` and draws from:
- `references/laws-of-ux.md` — Predictive models (Fitts's, Hick's, Jakob's, Doherty, Postel's), cognitive bias & memory (Miller's, Peak-End, Zeigarnik, Serial Position, Von Restorff, Aesthetic-Usability), Gestalt principles (6 laws), Nielsen's 10 heuristics, dark patterns awareness, accessibility connections per law
- `references/ideation-prototyping.md` — Prototyping fidelity progression (Low→Mid→High), design systems & tokens (3-tier hierarchy), Design Sprint methodology
- `references/arabic-rtl-mena.md` — RTL layout mirroring rules, BiDi text handling, Arabic typography, cultural localization, trust-building UI patterns, mobile-first heuristics for constrained devices
- `references/agentic-ai-design.md` — Human-AI interaction guidelines, confidence scoring, progressive disclosure for AI, conversational UX patterns (if product includes AI features)

## Prototyping Fidelity Progression

The agent MUST recommend the appropriate fidelity level per `references/ideation-prototyping.md`:

| Fidelity | Tools | When to Use | What to Test |
|----------|-------|-------------|-------------|
| **Low-fi** | Paper, whiteboard, basic wireframes | Early exploration, multiple concepts | Layout, flow, information hierarchy |
| **Mid-fi** | Grayscale digital wireframes | IA validation, flow testing | Navigation, task completion, content structure |
| **High-fi** | Full visual design with interactions | Pre-launch validation | Visual design, micro-interactions, emotional response |

Selection criteria: Use lowest fidelity that answers the current question. Never high-fi before flow validation.

## Gestalt Principles Application

When auditing screens, verify Gestalt principles from `references/laws-of-ux.md`:
- **Proximity**: Related elements grouped by spacing (not just lines/boxes)
- **Common Region**: Cards/containers for semantically related content
- **Similarity**: Consistent styling for same-type elements
- **Continuity**: Elements aligned on clear visual lines
- **Closure**: Truncated lists suggest continuation; partial cards suggest scrollability
- **Figure-Ground**: Modal overlays, active states, shadow/elevation hierarchy

## Dark Patterns Check

Before recommending any interaction pattern, verify it does NOT match dark patterns from `references/laws-of-ux.md`:
- No confirmshaming, roach motels, hidden costs, forced continuity
- No misdirection via Von Restorff Effect abuse
- No pre-checked consent or misleading button sizing
- Especially critical for fintech/MENA markets where digital trust is fragile

## Micro-Interaction Specification Guide

When specifying micro-interactions, include:
- **Trigger**: What user action initiates the animation
- **Duration**: 100-300ms for UI feedback, 300-500ms for transitions, never >1000ms
- **Easing**: ease-out for entrances, ease-in for exits, spring for playful interactions
- **Purpose**: Must serve one of: feedback, guidance, continuity, or delight (in that priority order per Ethical Design Hierarchy)

## Human-AI Interaction Checks

If the product includes AI features, apply checks from `references/agentic-ai-design.md`:
- **Transparency**: AI capabilities and limitations clearly communicated
- **Confidence display**: Tiered indicators (High/Moderate/Low), never false-precision percentages
- **Error recovery**: Users can easily undo/edit AI actions
- **Progressive disclosure**: Action summary → Supporting rationale → Detailed analysis
- **Trust calibration**: Design for appropriate trust level (prevent both over-trust and under-trust)
