# Command Contract: /ux.handoff

**Phase**: 6 — Design-to-Engineering Handoff
**Skill**: `skills/ux-handoff/SKILL.md`

## Purpose

Generate comprehensive handoff documentation: annotated specs, state catalogs, edge-case catalogs, accessibility requirements, responsive rules, and QA checklists for engineering.

## Invocation

```
/ux.handoff [optional: specific feature/screen or handoff focus]
```

## Inputs

- **Required**: Validated design artifacts (Phase 5 complete or in progress)
- **Optional**: Specific feature to hand off, existing engineering constraints, design system token file

## Behavior

1. Verify Phase 5 completion (warn if testing incomplete).
2. Present Phase 6 DoD checklist.
3. Generate handoff package:
   - **Annotated specifications**: screen-by-screen behavioral notes, interaction states, micro-interaction timing
   - **State documentation**: complete state catalog per screen (all 7+ states with behavioral rules)
   - **Edge-case catalog**: boundary conditions, error scenarios, recovery paths
   - **Accessibility requirements**: ARIA labels, keyboard behavior, focus order, color contrast values
   - **Responsive rules**: breakpoint behaviors, layout shifts, touch target sizes
   - **QA checklist**: visual fidelity verification points (target >95% accuracy)
   - **Acceptance criteria**: testable Given/When/Then scenarios per feature
4. Cross-reference with Spec Kit artifacts if available (link to spec.md, plan.md).
5. When complete: recommend `/ux.optimize` for post-launch setup.

## Outputs

| Artifact | Path | Template |
|----------|------|----------|
| Handoff checklist | `ux/handoff/handoff-checklist.md` | `templates/handoff-checklist-template.md` |
| State documentation | `ux/handoff/state-documentation.md` | Reuses state-inventory template |
| Edge-case catalog | `ux/handoff/edge-case-catalog.md` | Inline |
| Accessibility spec | `ux/handoff/accessibility-spec.md` | Inline |
| Acceptance criteria | `ux/handoff/acceptance-criteria.md` | Inline (Given/When/Then) |

## Guardrails

- MUST NOT include implementation-specific instructions (no "use React's useState" — describe behavior, not code).
- State documentation MUST cover all 7+ states for every screen handed off.
- Accessibility spec MUST include specific ARIA roles, keyboard shortcuts, and focus management rules.
- Edge-case catalog MUST address: missing data, network failure, invalid input, concurrent access, permission denial.
- Acceptance criteria MUST be in Given/When/Then format for direct import to issue trackers.
- All handoff docs MUST reference state inventories from Phase 3 and heuristic findings from Phase 5.

## Context Adaptation

| Mode | Behavior |
|------|----------|
| MVP | Annotated flows + core states + basic acceptance criteria, accessibility essentials only |
| Growth | Full spec + all states + edge-case catalog + accessibility spec + acceptance criteria |
| Enterprise | Full spec + states + edge cases + accessibility + responsive rules + compliance requirements + QA checklist + visual fidelity verification points |

## Cross-Phase References (FR-019)

| This Phase Artifact | MUST Reference | From Phase |
|---------------------|----------------|------------|
| State documentation | State inventories (validate coverage) | Phase 3 |
| Accessibility spec | Heuristic evaluation findings (remediation status) | Phase 5 |
| Edge-case catalog | User flow error paths | Phase 3 |
| Acceptance criteria | Test plan task scenarios (align success criteria) | Phase 5 |
| Handoff checklist | Persona names (who each feature serves) | Phase 2 |

## Error Message Writing Guidelines

When handoff includes error states, error messages MUST follow:
- **Tone**: Friendly, blame-free, no technical jargon
- **Structure**: [What happened] + [Why it matters] + [What to do next]
- **Example**: "We couldn't save your changes. Your internet connection dropped. Your work is safe — we'll save automatically when you're back online."
- **Anti-patterns**: "Error 500", "Something went wrong", "Invalid input", "null"

## Empty State Design Principles

When handoff includes empty states, documentation MUST specify:
- **Educational**: Explain what this area will contain once populated
- **Actionable**: Provide a clear CTA to the first action
- **Motivational**: Show the value of completing the action
- **Example-driven**: Use realistic placeholder content, not "Lorem ipsum"

## Tooling Integration (Appendix G)

| Tool/Skill | When to Invoke | What It Provides |
|------------|---------------|------------------|
| `speckit-taskstoissues` skill | When creating engineering work items | Convert tasks to GitHub/Linear issues |
| `figma:implement-design` skill | When translating designs to code | Figma design implementation |
| `figma:code-connect-components` skill | When bridging design-code gap | Figma-to-code component connection |
| `figma:create-design-system-rules` skill | When documenting design system | Design system rule generation from Figma |
| `acceptance-criteria-creator` skill | When writing Given/When/Then criteria | Structured acceptance criteria generation |
| `definition-of-done-generator` skill | When defining completion criteria | DoD checklist generation |
| `design-doc-template` skill | When creating engineering design docs | Technical design document templates |
| `storybook-figma` MCP | When verifying component context | Design-to-code bridging, Storybook integration |
| `accesslint` MCP | When final-checking accessibility | `diff_html` for before/after a11y comparison |

## Skill Reference Files

This contract is implemented by `skills/ux-handoff/SKILL.md` and draws from:
- `references/design-handoff.md` — Staggered sprint pipeline (UX runs 1-2 sprints ahead), handoff documentation standards (4 layers: Context/Flow/Specification/Edge Cases), design QA process (visual/interaction/responsive/content/accessibility checklists), component documentation template, responsive specification format (breakpoint strategy), edge case catalog template, acceptance criteria in Given/When/Then (Gherkin) format, collaboration anti-patterns
- `references/arabic-rtl-mena.md` — RTL responsive considerations, common RTL bugs checklist, Arabic accessibility (screen reader, diacritics, font sizing)
- `references/laws-of-ux.md` — Accessibility connections per UX law (for accessibility spec generation)

## Staggered Sprint Pipeline

Handoff documentation MUST support the staggered sprint model from `references/design-handoff.md`:
- Sprint N-2: UX Research (research insights, validated problems)
- Sprint N-1: UX Design (validated designs ready for handoff)
- Sprint N: Engineering (implement designs, UX attends standups, design QA)
- Sprint N+1: Post-launch monitoring + quick-fix designs

## Handoff Documentation Layers

Every handoff package MUST include these 4 layers per `references/design-handoff.md`:
1. **Context (the "why")**: User story, research findings, success metrics, emotional intent
2. **Flow (the "what")**: User flow diagram (all paths), screen inventory, entry/exit points
3. **Specification (the "how")**: Component list with tokens, spacing/typography/color values, interaction specs, state documentation, responsive rules
4. **Edge Cases (the "what if")**: Empty states, error states, boundary conditions, offline behavior, permission states

## Design QA Checklist

Handoff MUST include a QA verification checklist per `references/design-handoff.md`:
- **Visual fidelity**: Colors, typography, spacing, border radius, shadows, icons match tokens
- **Interaction fidelity**: All states implemented, transitions match specs, keyboard nav works, touch targets meet minimums
- **Responsive fidelity**: Layout adapts at breakpoints, no horizontal scroll, touch/desktop behaviors correct
- **Content fidelity**: Real content renders, long text handled, empty/error states match, RTL mirrors correctly
- **Accessibility**: ARIA labels, screen reader announcements, contrast meets WCAG AA, keyboard-only navigation

## Acceptance Criteria Format

Use Given/When/Then (Gherkin) format per `references/design-handoff.md`:
- Each criterion MUST be independently testable
- Use specific, measurable language (not "loads quickly" → "renders within 400ms")
- Cover: happy path, error paths, edge cases, accessibility, responsive behavior
- Include performance expectations where relevant
- Reference specific design tokens and component names
