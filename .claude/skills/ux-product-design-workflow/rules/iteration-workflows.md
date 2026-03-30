# Iteration Workflow Rules

## Loop-Back Triggers

Phase progression is not strictly linear. These conditions trigger mandatory loop-backs:

### Catastrophic Loop-Backs (must loop back)
| Condition | From Phase | To Phase | Scope |
|-----------|-----------|----------|-------|
| Task completion rate <50% on any core flow | 5 (Validate) | 3 (IA) or 4 (Prototype) | Redesign the failing flow |
| Severity-4 issue in >2 core flows | 5 (Validate) | 3 (IA) | Reconsider information architecture |
| Engineering declares core concept infeasible | 6 (Handoff) | 3 (IA) | Explore alternative solutions |
| D7 retention <15% post-launch | 7 (Optimize) | 1 (Discovery) | Re-examine product-market fit |
| Accessibility fails WCAG AA on core flows | 5 (Validate) | 4 (Prototype) | Redesign with accessibility-first |

### Advisory Loop-Backs (recommended but not mandatory)
| Condition | From Phase | To Phase | Scope |
|-----------|-----------|----------|-------|
| Task completion 50-80% on core flows | 5 (Validate) | 4 (Prototype) | Refine interaction design |
| 3+ undocumented edge cases found in handoff | 6 (Handoff) | 4 (Prototype) | Design missing states |
| A/B test shows no significant lift after 3 tests | 7 (Optimize) | 2 (Define) | Re-examine problem hypothesis |
| User interviews reveal new unmet need | 7 (Optimize) | 1 (Discovery) | Investigate new opportunity |
| SUS score <68 | 5 (Validate) | 4 (Prototype) | Improve usability of weakest flows |

## Loop-Back Protocol

When looping back:
1. **Preserve evidence**: Carry all findings from the triggering phase. Don't restart from scratch.
2. **Narrow scope**: Only revisit the specific area that triggered the loop-back.
3. **Update risk gate**: Re-evaluate the Four-Risk Gate for the affected scope.
4. **Update phase-status.json**: Record the loop-back with timestamp, reason, and scope.
5. **Set exit criteria**: Define specific, measurable criteria for when to re-advance.

## Phase-Status JSON Schema

```json
{
  "currentPhase": 4,
  "phaseHistory": [
    { "phase": 1, "status": "complete", "completedAt": "2025-03-15" },
    { "phase": 2, "status": "complete", "completedAt": "2025-03-20" },
    { "phase": 3, "status": "complete", "completedAt": "2025-03-25" },
    { "phase": 4, "status": "in-progress", "startedAt": "2025-03-26" },
    { "phase": 5, "status": "loop-back", "reason": "Task completion <60% on onboarding flow", "loopBackTo": 4, "scope": "Redesign onboarding interaction", "triggeredAt": "2025-04-01" }
  ],
  "fourRiskGate": {
    "value": { "status": "validated", "evidence": "User interviews confirm need" },
    "usability": { "status": "at-risk", "evidence": "Phase 5 testing showed 55% completion" },
    "feasibility": { "status": "validated", "evidence": "Engineering spike completed" },
    "viability": { "status": "validated", "evidence": "Business model approved" }
  },
  "contextMode": "mvp"
}
```

## Forward-Only Conditions

Some situations should NOT trigger a loop-back:
- Cosmetic (severity 1) findings → fix in current phase, don't loop back
- Minor (severity 2) findings with known workarounds → document and proceed
- Feature requests from test participants → add to opportunity backlog, don't redesign
- Metrics slightly below target (within 10%) → optimize in Phase 7, don't loop back
- Stakeholder opinions without user evidence → note in assumptions, don't change course
