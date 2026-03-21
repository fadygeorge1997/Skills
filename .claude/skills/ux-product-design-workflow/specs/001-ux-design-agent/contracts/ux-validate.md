# Command Contract: /ux.validate

**Phase**: 5 — Validation & Usability Testing
**Skill**: `skills/ux-validate/SKILL.md`

## Purpose

Plan and structure usability testing, heuristic evaluations, accessibility audits, and Human-AI interaction checks. Produce test plans, severity-rated findings, and prioritized recommendations.

## Invocation

```
/ux.validate [optional: test type or specific flow to validate]
```

## Inputs

- **Required**: Prototype or design artifacts from Phase 4
- **Optional**: Test type (usability, heuristic, accessibility, AI-interaction), specific flow/screen to test, existing test results to analyze

## Behavior

1. Verify Phase 4 completion.
2. Present Phase 5 DoD checklist.
3. Generate appropriate test artifacts:
   - **Usability test plan**: objectives, methodology (moderated/unmoderated/guerrilla), task scenarios (JTBD-based, not feature-based), metrics (completion rate, SUS, error rate, time-on-task), participant criteria, schedule
   - **Heuristic evaluation**: Nielsen's 10 applied to each core screen, severity-rated (1-4)
   - **Accessibility audit**: WCAG 2.1 AA POUR checklist, color contrast, focus states, keyboard paths, screen reader compatibility
   - **Human-AI checks** (if applicable): transparency, scoping, error recovery, explainability
4. If user provides test results: synthesize into findings report with severity ratings and impact-effort prioritization.
5. When complete: recommend `/ux.handoff`.

## Outputs

| Artifact | Path | Template |
|----------|------|----------|
| Usability test plan | `ux/validation/test-plan.md` | `templates/test-plan-template.md` |
| Heuristic evaluation | `ux/validation/heuristic-evaluation.md` | `templates/heuristic-evaluation-template.md` |
| Accessibility audit | `ux/validation/accessibility-audit.md` | Inline (POUR framework) |
| Findings report | `ux/validation/findings-report.md` | Inline (severity-rated) |
| Recommendations | `ux/validation/recommendations.md` | Inline (impact-effort matrix) |

## Guardrails

- Test scenarios MUST be task-based from real jobs, NOT feature-based ("Send EGP 200 to Ahmed" not "Click Send Money").
- MUST NOT execute tests autonomously — agent drafts plans, humans execute.
- Severity ratings MUST use the 4-level scale (catastrophic, major, minor, cosmetic).
- Accessibility checks MUST cover POUR: Perceivable, Operable, Understandable, Robust.
- Minimum recommendation: 5 participants per segment (cite Nielsen's research).

## Context Adaptation

| Mode | Behavior |
|------|----------|
| MVP | Guerrilla/hallway testing, 3-5 participants, essential heuristics, basic a11y |
| Growth | Remote moderated, 5-8 participants, full heuristics, WCAG AA audit |
| Enterprise | Moderated + unmoderated + expert review, 8-15 participants, full WCAG + compliance |

## Cross-Phase References (FR-019)

| This Phase Artifact | MUST Reference | From Phase |
|---------------------|----------------|------------|
| Test plan task scenarios | Journey map pain points (test the moments that matter) | Phase 2 |
| Test plan participant criteria | Persona segments (recruit matching users) | Phase 2 |
| Heuristic evaluation | State inventories (evaluate all states, not just happy path) | Phase 3 |
| Heuristic evaluation | Laws of UX from prototype phase (verify application) | Phase 4 |
| Findings report | Problem statements (do solutions actually solve the problems?) | Phase 2 |

## Tooling Integration (Appendix G)

| Tool/Skill | When to Invoke | What It Provides |
|------------|---------------|------------------|
| `ux-heuristics` skill | When performing expert review | Nielsen's 10 + Krug's Laws with severity ratings |
| `accessibility` skill | When auditing WCAG compliance | WCAG 2.2, semantic HTML, ARIA, keyboard nav |
| `fixing-accessibility` skill | When remediating a11y issues | Automated fix suggestions |
| `cro-methodology` skill | When validating conversion flows | O/CO framework, persuasion assets audit |
| `color-contrast-checker` skill | When verifying color choices | WCAG contrast ratio validation |
| `keyboard-navigation-tester` skill | When testing keyboard paths | Keyboard navigation verification |
| `scanning-accessibility` skill | When running automated a11y scans | Automated accessibility scanning |
| `e2e-testing-patterns` skill | When designing test automation | End-to-end testing patterns |
| `accesslint` MCP | When auditing live URLs or HTML | `audit_url`, `audit_html`, `audit_file` for WCAG violations |
| `playwright` MCP | When automating interaction tests | Browser automation for flow verification |
| `chrome-devtools` MCP | When running Lighthouse audits | `lighthouse_audit` for performance/a11y/SEO scores |
| `Claude Preview` MCP | When testing prototypes interactively | Live preview with click/fill/screenshot |

## Skill Reference Files

This contract is implemented by `skills/ux-validate/SKILL.md` and draws from:
- `references/usability-testing.md` — Testing methods (4 types), session structure (5-part), think-aloud protocol (3 levels), facilitator discipline, heuristic evaluation process, WCAG POUR framework, participant recruitment (screener template, compensation, channels), consent & ethics, inclusive testing checklist, remote testing tools, moderation script, observer notes, validation anti-patterns
- `references/laws-of-ux.md` — Nielsen's 10 heuristics (detailed criteria), application checklist
- `references/agentic-ai-design.md` — AI error pattern catalog, trust calibration, design checklist for AI features

## Think-Aloud Protocol Levels

When specifying usability test methodology, reference levels from `references/usability-testing.md`:
- **Level 1-2 (Classic)**: Users narrate immediate thoughts — sufficient for most cases
- **Level 3 (Deep Insight)**: Extract causal explanations, problem formulations, and recommendations through probes — use for high-stakes interfaces (financial, health)

## Participant Recruitment Guide

Test plans MUST include recruitment details per `references/usability-testing.md`:
- **Screener**: Demographics + behavioral filters + disqualification criteria + scoring rubric
- **Channels**: User panel services, own user base, social media, in-app intercept, professional recruiters
- **Compensation**: Fair payment adjusted for local purchasing power (30 min = $30-50 USD equivalent)
- **Consent**: Informed consent covering purpose, recording, data handling, voluntary participation

## Inclusive Testing Checklist

Beyond standard usability, verify per `references/usability-testing.md`:
- [ ] Screen reader users (VoiceOver, TalkBack, NVDA)
- [ ] Keyboard-only users
- [ ] Low vision users (200% zoom, contrast ratios)
- [ ] Motor impairment (switch access, target sizes ≥44x44px)
- [ ] Cognitive accessibility (varying literacy levels)
- [ ] Low bandwidth / constrained devices (3G, budget phones)
- [ ] Multilingual / RTL content
- [ ] New-to-digital users (minimal smartphone experience)

## Validation Anti-Patterns

Avoid these from `references/usability-testing.md`:
- **White/able-bodied default**: Test with diverse abilities and backgrounds
- **"Research takes too long"**: Even 3 guerrilla tests reveal blockers
- **Confirmation bias**: Have someone outside the design team review findings
- **Testing ideal conditions only**: Test on constrained devices, slow networks, empty accounts
- **Stakeholder-only testing**: Internal demos are alignment, not validation

## Severity Rating Guide

| Level | Label | Definition | Example |
|-------|-------|------------|---------|
| 4 | Catastrophic | Users cannot complete core task; data loss risk | Submit button non-functional; payment fails silently |
| 3 | Major | Users complete task but with significant difficulty or errors | 40% of users miss required field due to poor visibility |
| 2 | Minor | Users notice issue but work around it without help | Help text unclear but users infer correct action |
| 1 | Cosmetic | Noticed only by experts; no impact on task completion | Icon slightly misaligned; inconsistent capitalization |
| 0 | Not a problem | Evaluator disagreement — included for discussion only | Subjective preference, not usability issue |

## Iteration Process

After findings are prioritized, follow the Lean UX Think/Make/Check loop:
1. **Think**: Formulate hypotheses about which changes will improve the experience
2. **Make**: Create the minimum prototype needed to test the hypothesis
3. **Check**: Test with users, measure against hypothesis, learn

Start with Quick Wins (high-impact, low-effort). Track improvements using same metrics across iterations.
