# Agent Coordination Rules

## Agent Invocation Priority

When multiple agents could apply, follow this priority order:

1. **ux-phase-navigator** — Always invoke first to establish context (which phase, what's complete)
2. **Phase-specific agents** — Based on detected phase:
   - Phase 1: ux-researcher → ux-artifact-generator
   - Phase 2: ux-artifact-generator
   - Phase 3-4: Manual design work (agents assist on request)
   - Phase 5: ux-prototype-reviewer → ux-accessibility-auditor
   - Phase 6: ux-handoff-preparer
   - Phase 7: Manual analysis (agents assist on request)

## Inter-Agent Data Flow

```
ux-researcher
  ├─→ ux/research/competitive-analysis.md
  ├─→ ux/research/teardowns/
  └─→ ux/research/accessibility/
        ↓
ux-artifact-generator
  ├─→ ux/define/personas/
  ├─→ ux/define/journey-maps/
  ├─→ ux/define/empathy-maps/
  └─→ ux/define/problem-statements/
        ↓
[Manual Design Work: IA, Prototyping]
        ↓
ux-prototype-reviewer
  └─→ ux/validate/heuristic-evaluation.md
        ↓
ux-accessibility-auditor
  └─→ ux/validate/accessibility-audit.md
        ↓
ux-handoff-preparer
  ├─→ ux/handoff/specs/
  ├─→ ux/handoff/edge-cases/
  └─→ ux/handoff/acceptance-criteria/
```

## Conflict Resolution

When two agents could handle a task:
- **Research vs Artifact generation**: If user has raw data → ux-artifact-generator. If user needs data → ux-researcher.
- **Prototype review vs Accessibility audit**: Always run prototype review first (broader scope), then accessibility audit (specialized depth).
- **Phase navigator vs any other agent**: Phase navigator provides context, not work product. Always pair it with a working agent.

## Error Escalation

When an agent encounters an issue it can't resolve:
1. Document the issue in the agent's output
2. Recommend the appropriate fallback (see Tool Fallback in each agent)
3. If no fallback available, recommend manual intervention with specific guidance
4. Never silently skip a quality gate — always surface the gap

## Phase Transition Triggers

After an agent completes work, check if the current phase's Definition of Done is now met:
- If yes → recommend phase advancement via ux-phase-navigator
- If no → list remaining items and recommend next action
- If loop-back triggered → recommend target phase with evidence (see `rules/iteration-workflows.md`)
