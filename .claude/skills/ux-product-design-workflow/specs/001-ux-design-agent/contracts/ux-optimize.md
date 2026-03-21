# Command Contract: /ux.optimize

**Phase**: 7 — Post-Launch Optimization
**Skill**: `skills/ux-optimize/SKILL.md`

## Purpose

Set up measurement frameworks (HEART + AARRR), Goals-Signals-Metrics mappings, experiment backlogs, and Product Kata cycles for continuous post-launch improvement.

## Invocation

```
/ux.optimize [optional: specific metric area, feature to optimize, or experiment to design]
```

## Inputs

- **Required**: Live product or feature description
- **Optional**: Current metrics/analytics data, known drop-off points, hypothesis to test, baseline measurements

## Behavior

1. Check if Phase 6 (Handoff) is complete (warn if not, allow override for already-live products).
2. Present Phase 7 DoD checklist.
3. Generate optimization artifacts:
   - **HEART framework**: all 5 dimensions with Goals, Signals (success + failure), Metrics, Targets
   - **AARRR funnel**: stage-by-stage analysis with drop-off hypotheses
   - **Goals-Signals-Metrics table**: consolidated measurement framework
   - **Experiment backlog**: prioritized list of experiments with hypothesis, success criteria, estimated effort
   - **Product Kata plan**: 4-week cycle with Direction, Current State, Target Condition, and 2-3 experiments
4. If user provides analytics data: analyze for patterns, anomalies, and optimization opportunities.
5. Product Kata is ongoing — this phase loops back to itself weekly.

## Outputs

| Artifact | Path | Template |
|----------|------|----------|
| HEART framework | `ux/metrics/heart-framework.md` | Inline (from data-model schema) |
| AARRR funnel | `ux/metrics/aarrr-funnel.md` | Inline |
| Goals-Signals-Metrics | `ux/metrics/goals-signals-metrics.md` | `templates/goals-signals-metrics-template.md` |
| Experiment backlog | `ux/metrics/experiment-backlog.md` | `templates/experiment-backlog-template.md` |
| Product Kata plan | `ux/metrics/product-kata-[date].md` | Inline |

## Guardrails

- Metrics MUST be user-facing outcomes, not system internals ("users complete checkout in <3 min" not "API responds in <200ms").
- Experiment hypotheses MUST follow: "We believe [change] will [outcome] because [evidence/rationale]."
- MUST NOT auto-run experiments or modify production analytics configs — agent designs, humans execute.
- Minimum experiment duration: 2 weeks (to account for weekly patterns).
- Each experiment MUST have pre-defined success criteria and sample size recommendation.

## Context Adaptation

| Mode | Behavior |
|------|----------|
| MVP | 2-3 HEART dimensions, basic funnel, 2-3 experiments, 2-week kata cycles |
| Growth | All 5 HEART dimensions, full funnel, 5-8 experiments, weekly kata cycles |
| Enterprise | Full HEART + AARRR, segmented analysis, 10+ experiments, weekly kata + quarterly reviews |

## Cross-Phase References (FR-019)

| This Phase Artifact | MUST Reference | From Phase |
|---------------------|----------------|------------|
| HEART framework goals | Problem statements (what user needs we're measuring against) | Phase 2 |
| AARRR funnel | Journey map stages (map funnel to journey) | Phase 2 |
| Experiment hypotheses | Heuristic findings (test remediations) | Phase 5 |
| Product Kata target conditions | Four-Risk Gate (align with value/usability risk areas) | Phase 1 |
| Experiment backlog | Test plan findings (iterate on validated issues) | Phase 5 |

## Tooling Integration (Appendix G)

| Tool/Skill | When to Invoke | What It Provides |
|------------|---------------|------------------|
| `cro-methodology` skill | Primary optimization framework | CRE Methodology, O/CO, hypothesis design, ICE scoring, A/B testing |
| `hooked-ux` skill | When optimizing engagement loops | Hook Model audit, habit testing, Manipulation Matrix |
| `a-b-test-config-creator` skill | When setting up experiments | A/B test configuration |
| `ab-test-analyzer` skill | When interpreting experiment data | A/B test result analysis |
| `statistical-significance-calculator` skill | When evaluating test results | Statistical significance validation |
| `funnel-analysis-builder` skill | When diagnosing drop-off points | Funnel visualization and analysis |
| `cohort-analysis-creator` skill | When measuring retention | Cohort analysis setup |
| `churn-analysis-helper` skill | When investigating user loss | Churn prediction and analysis |
| `retention-calculator` skill | When tracking return rates | Retention metric calculation |
| `kpi-dashboard-template` skill | When building monitoring dashboards | KPI dashboard design |
| `lean-startup` skill | When applying Build-Measure-Learn | MVP definition, pivot criteria |
| `predictable-revenue` skill | When aligning UX with revenue funnels | Revenue funnel alignment |
| `chrome-devtools` MCP | When measuring performance | `performance_start_trace`, `lighthouse_audit` for CWV |
| `playwright` MCP | When automating conversion flow tests | Browser automation for funnel verification |

## Skill Reference Files

This contract is implemented by `skills/ux-optimize/SKILL.md` and draws from:
- `references/metrics-optimization.md` — HEART framework (5 dimensions with detailed metrics), Goals-Signals-Metrics 3-step process, AARRR pirate metrics (per-stage metrics), HEART+AARRR combination matrix, A/B testing methodology (6-step process, common pitfalls), cohort analysis (types, reading tables, what to look for), North Star Metric (concept, examples by product type, input metric tree), metric hierarchy & taxonomy (3 levels: outcome/driver/health), counter-metrics, dashboard design best practices, experiment documentation template (before/after), experiment log, continuous improvement loop (weekly rhythm)
- `references/frameworks.md` — Product Kata (4-step cycle), Lean UX (Think/Make/Check), Continuous Discovery Habits

## North Star Metric

Every optimization engagement MUST define a North Star Metric per `references/metrics-optimization.md`:
- Reflects value delivered to users (not just revenue)
- Is a leading indicator of long-term business success
- Is influenced by the entire product team's work
- Sits atop a tree of input metrics the team can directly influence

| Product Type | Example NSM |
|-------------|-------------|
| Mobile wallet | Weekly active transactors |
| E-commerce | Weekly purchases per active customer |
| SaaS | Weekly active users completing core task |
| Content platform | Total daily reading time |

## Counter-Metrics

Every optimized metric MUST have a counter-metric per `references/metrics-optimization.md`:

| Primary Metric | Risk If Gamed | Counter-Metric |
|---------------|---------------|----------------|
| Sign-up rate | Low-quality users | D7 activation rate |
| Session length | Frustration/endless scrolling | Task completion rate |
| Feature adoption | Forced adoption via dark patterns | Voluntary repeat usage |
| Transaction volume | Micro-transaction inflation | Avg transaction value |

## Metric Hierarchy

Organize metrics into 3 levels per `references/metrics-optimization.md`:
1. **Outcome Metrics (Lagging)**: Revenue, retention, NPS — updated monthly/quarterly, owned by leadership
2. **Driver Metrics (Leading)**: Feature adoption, activation rate — updated weekly, owned by product triads
3. **Health Metrics (Guardrails)**: Error rates, latency, crash rate — monitored continuously, owned by engineering

## Continuous Improvement Cadence

The weekly rhythm per `references/metrics-optimization.md`:
1. **Monday**: Review dashboard metrics from previous week
2. **Tuesday-Wednesday**: Conduct user interviews (continuous discovery)
3. **Thursday**: Triad meets to synthesize insights and prioritize experiments
4. **Friday**: Ship small improvements, set up next week's tests

## When to Loop Back to Discovery

The optimization phase feeds back to discovery when:
- Metrics plateau (incremental experiments stop moving NSM)
- New user segment emerges from cohort analysis
- Support ticket themes shift to new complaint patterns
- Market disruption (competitor launches, regulatory changes)
- Quarterly cadence (schedule deep-discovery cycles regardless)

## Product Kata Cycle Template

Each kata cycle (2-4 weeks) follows this structure:
1. **Direction**: North-star metric and strategic context
2. **Current State**: Baseline measurement + qualitative understanding
3. **Target Condition**: Specific, measurable 2-4 week goal
4. **First Experiment**: Smallest test that could disprove the hypothesis
5. **Reflection**: What did we learn? What's the next experiment?

The cycle loops: Reflection feeds back into Current State for the next iteration.

## Experimentation Anti-Patterns

Avoid these from `references/metrics-optimization.md`:
- **Vanity metric addiction**: Track task success, retention, activation — not total page views
- **Gut-feeling reliance**: Every experiment needs a hypothesis grounded in research or analytics
- **HiPPO-driven experiments**: Use evidence-based prioritization, not highest-paid-person's opinion
- **Metric gaming**: Always pair primary metric with counter-metric
- **Post-hoc rationalization**: Pre-define ship/kill/iterate criteria BEFORE results come in
