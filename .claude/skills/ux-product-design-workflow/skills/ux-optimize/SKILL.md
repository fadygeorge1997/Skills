---
name: ux-optimize
description: >
  Phase 7 of the UX & Product Design workflow. Guides post-launch optimization
  including HEART/AARRR metrics framework, Goals-Signals-Metrics mapping,
  experiment design, Product Kata cycles, and continuous discovery rhythms.

  Use this skill when: setting up product metrics, planning experiments, running
  A/B tests, analyzing user behavior, optimizing conversion funnels, or establishing
  continuous discovery practices.
---

# Phase 7: Post-Launch Optimization

## Overview

**Goal:** Measure outcomes, iterate continuously, and drive sustainable growth.

**Duration:** Ongoing — continuous process

**When to loop back:** When metrics stall, when new pain points surface in support tickets, or on a regular weekly cadence (continuous discovery).

---

## Input Requirements

From Previous Phases:
- [ ] Live product or feature
- [ ] Problem statements (Phase 2) — for HEART goals
- [ ] User flows (Phase 3) — for funnel analysis
- [ ] Test findings (Phase 5) — for optimization opportunities
- [ ] Acceptance criteria (Phase 6) — for success baseline

---

## Phase Checklist

### 1. Metrics Framework Setup
- [ ] Define HEART framework goals per feature
- [ ] Map AARRR funnel stages
- [ ] Create Goals-Signals-Metrics tables
- [ ] Set up monitoring dashboards
- [ ] Configure automated anomaly alerts

### 2. Baseline Measurement
- [ ] Establish baseline metrics before changes
- [ ] Document current state for comparison
- [ ] Identify key drop-off points in funnels

### 3. Experiment Design
- [ ] Generate hypotheses from data/feedback
- [ ] Prioritize experiments by impact/effort
- [ ] Design A/B tests with proper statistical rigor
- [ ] Define success criteria and guardrail metrics

### 4. Continuous Discovery
- [ ] Schedule weekly customer touchpoints
- [ ] Maintain opportunity backlog
- [ ] Feed learnings back into discovery phase

### 5. Product Kata Cycles
- [ ] Set direction (north-star metric)
- [ ] Document current state
- [ ] Define target condition (2-4 week goal)
- [ ] Run weekly experiments
- [ ] Document learnings

---

## Deliverables

| Artifact | Format | Template |
|----------|--------|----------|
| HEART Framework | Goals/Signals/Metrics table | `templates/goals-signals-metrics-template.md` |
| AARRR Funnel | Funnel analysis document | Generated during phase |
| Experiment Backlog | Prioritized hypothesis list | `templates/experiment-backlog-template.md` |
| Product Kata Plan | Cycle planning document | Generated during phase |
| North Star Metric | NSM definition | `templates/north-star-metric-template.md` |

---

## HEART Framework

### Dimensions

| Dimension | Measures | Example Metrics |
|-----------|---------|-----------------|
| **H**appiness | Subjective satisfaction | CSAT, NPS, SUS, Perceived ease |
| **E**ngagement | Depth/frequency of use | DAU/MAU, Session length, Feature usage depth |
| **A**doption | New user/feature uptake | Signup rate, Feature adoption %, Time to first value |
| **R**etention | Users returning over time | D1/D7/D30 retention, Churn rate, Resurrection rate |
| **T**ask Success | Behavioral efficiency | Completion rate, Error rate, Time-on-task |

### HEART Goals-Signals-Metrics Template

```markdown
# HEART Framework: [Feature/Product Name]

## Happiness
**Goal:** [What user satisfaction outcome?]
**Signals of Success:** [What behaviors indicate happiness?]
**Signals of Failure:** [What behaviors indicate unhappiness?]
**Metrics:**
- [Metric 1] Target: [value]
- [Metric 2] Target: [value]

## Engagement
**Goal:** [What engagement outcome?]
**Signals of Success:** [What behaviors indicate engagement?]
**Signals of Failure:** [What behaviors indicate disengagement?]
**Metrics:**
- [Metric 1] Target: [value]
- [Metric 2] Target: [value]

## Adoption
**Goal:** [What adoption outcome?]
**Signals of Success:** [What behaviors indicate adoption?]
**Signals of Failure:** [What behaviors indicate non-adoption?]
**Metrics:**
- [Metric 1] Target: [value]
- [Metric 2] Target: [value]

## Retention
**Goal:** [What retention outcome?]
**Signals of Success:** [What behaviors indicate retention?]
**Signals of Failure:** [What behaviors indicate churn?]
**Metrics:**
- [Metric 1] Target: [value]
- [Metric 2] Target: [value]

## Task Success
**Goal:** [What task success outcome?]
**Signals of Success:** [What behaviors indicate success?]
**Signals of Failure:** [What behaviors indicate failure?]
**Metrics:**
- [Metric 1] Target: [value]
- [Metric 2] Target: [value]
```

---

## AARRR Pirate Metrics

### Framework

| Stage | Focus | Key Questions | Example Metrics |
|-------|-------|---------------|-----------------|
| **A**cquisition | How users find you | Which channels drive quality users? | Visitors by channel, CAC, Install rate |
| **A**ctivation | First "Aha!" moment | How fast do users experience core value? | Time to first value, Activation rate, First session depth |
| **R**etention | Continued engagement | Do they come back? | D1/D7/D30 retention, Session frequency |
| **R**eferral | Users recommending you | Would they tell a friend? | NPS, Viral coefficient, Share rate |
| **R**evenue | Financial sustainability | Does unit economics work? | ARPU, LTV, Conversion to paid |

### Funnel Analysis Template

```markdown
# AARRR Funnel Analysis: [Product Name]

## Acquisition
| Channel | Visitors | % of Total | Quality Score |
|---------|----------|------------|---------------|
| [Channel 1] | [count] | [%] | [LTV/CAC ratio] |

**Key Insight:** [What's working? What isn't?]

## Activation
| Step | Users | Drop-off | Cumulative Drop-off |
|------|-------|----------|---------------------|
| Landing | 100% | - | - |
| Sign up | [%] | [%] | [%] |
| First action | [%] | [%] | [%] |
| "Aha" moment | [%] | [%] | [%] |

**Key Insight:** [Where's the biggest drop-off? Why?]

## Retention
| Cohort | D1 | D7 | D30 | Trend |
|--------|----|----|-----|-------|
| [Month] | [%] | [%] | [%] | ↑/↓/→ |

**Key Insight:** [Is retention improving?]

## Referral
| Metric | Value | Trend |
|--------|-------|-------|
| NPS | [score] | ↑/↓ |
| Viral coefficient | [value] | ↑/↓ |
| Share rate | [%] | ↑/↓ |

**Key Insight:** [Are users recommending us?]

## Revenue
| Metric | Value | Target |
|--------|-------|--------|
| ARPU | [$] | [$] |
| LTV | [$] | [$] |
| LTV:CAC | [ratio] | 3:1 minimum |

**Key Insight:** [Is the business model working?]
```

---

## Goals-Signals-Metrics Bridge

### The Framework

1. **Goal:** What outcome do you want? (User-focused, not feature-focused)
2. **Signals:** How would you know if you succeeded? (Observable behaviors)
3. **Metrics:** How do you measure those signals? (Quantifiable numbers)

### Example

| Level | Example |
|-------|---------|
| **Goal** | New users feel confident completing their first transaction |
| **Signal (Success)** | Completes transaction, no support contact, returns within 7 days |
| **Signal (Failure)** | Abandons at confirmation, contacts support, uninstalls within 24 hours |
| **Metrics** | First-transaction completion rate >70%, Support ticket rate <5%, D7 return >40% |

### Consolidated GSM Table

```markdown
# Goals-Signals-Metrics: [Feature Name]

| Goal | Signal | Metric | Target | Current |
|------|--------|--------|--------|---------|
| [Goal 1] | [Success signal] | [Metric] | [value] | [value] |
| [Goal 1] | [Failure signal] | [Metric] | [value] | [value] |
| [Goal 2] | ... | ... | ... | ... |
```

---

## Experiment Design

### Hypothesis Format

> "We believe that [change] will [outcome] because [evidence/rationale]."

### Examples

| Good | Bad |
|------|-----|
| "We believe that showing fee estimates before transaction confirmation will reduce abandonment rate by 15% because 43% of drop-offs occur at the fee reveal stage." | "We believe changing the button color will improve conversions." |

### Experiment Backlog Template

```markdown
# Experiment Backlog: [Product Name]

## Priority 1: [Experiment Name]
**Hypothesis:** "We believe that [change] will [outcome] because [evidence]."
**Success Metric:** [Primary metric]
**Guardrail Metrics:** [Metrics that shouldn't degrade]
**Minimum Detectable Effect:** [%]
**Sample Size Required:** [count]
**Duration:** [weeks]
**Status:** [Backlog/Running/Completed]

## Priority 2: [Experiment Name]
...

## Completed Experiments

| Experiment | Result | Learnings |
|------------|--------|-----------|
| [Name] | Win/Loss/Inconclusive | [What we learned] |
```

### A/B Test Requirements

| Element | Requirement |
|---------|-------------|
| Sample size | Calculate for statistical significance (typically 95% confidence) |
| Duration | Minimum 2 weeks to account for day-of-week effects |
| Traffic split | 50/50 for fastest results, or 90/10 for lower risk |
| Success criteria | Defined before test starts |
| Guardrail metrics | Metrics that must not degrade |

---

## Product Kata

### The Pattern

```
Direction (Where are we going?)
    ↓
Current State (Where are we now?)
    ↓
Target Condition (What's our 2-4 week goal?)
    ↓
Experiments (What will we try?)
    ↓
Learn (What did we learn?)
    ↓
[Repeat]
```

### Product Kata Plan Template

```markdown
# Product Kata Plan: [Date Range]

## Direction
**North-Star Metric:** [The ultimate outcome metric]
**Strategic Goal:** [This quarter's goal]

## Current State
**[North-Star Metric]:** [current value]
**Key Input Metrics:**
- [Metric 1]: [value]
- [Metric 2]: [value]

## Target Condition (2-4 weeks)
**Goal:** Move [metric] from [current] to [target]
**By:** [Date]

## Experiments This Cycle

### Week 1
**Hypothesis:** [What we're testing]
**Experiment:** [What we're doing]
**Success Criteria:** [How we'll know]

### Week 2
**Hypothesis:** ...
**Experiment:** ...
**Success Criteria:** ...

## Learnings
| Week | What We Tried | What Happened | Next Step |
|------|---------------|---------------|-----------|
| 1 | [Action] | [Result] | [Decision] |
```

---

## North Star Metric

### Definition

The single metric that best captures the core value your product delivers to customers.

### Criteria
- Expresses value delivered to customers
- Reflects user engagement with the product
- Is a leading indicator of business success
- Is measurable and actionable

### Examples

| Product | North Star Metric | Why |
|---------|-------------------|-----|
| Spotify | Time spent listening | Core value is music enjoyment |
| Airbnb | Nights booked | Core value is accommodation |
| Slack | Messages sent | Core value is communication |
| Facebook | Daily active users | Core value is connection |

### NSM Template

```markdown
# North Star Metric: [Product Name]

## North Star Metric
**[Metric Name]**: [Definition]

## Why This Metric
- [Captures customer value because...]
- [Correlates with business success because...]
- [Is leading indicator because...]

## Input Metrics (What we can influence)
1. [Input 1] → Drives NSM by [mechanism]
2. [Input 2] → Drives NSM by [mechanism]

## Counter-Metrics (What to watch)
- [Counter-metric 1]: [Why it matters]
- [Counter-metric 2]: [Why it matters]

## Target
- Current: [value]
- 3-month target: [value]
- 6-month target: [value]
```

---

## Continuous Discovery Rhythm

### Weekly Cadence

| Activity | Duration | Participants |
|----------|----------|--------------|
| Customer interview | 30-60 min | PM + Designer (rotating) |
| Synthesis session | 30 min | Core team |
| Experiment review | 30 min | Core team + engineering |
| Opportunity backlog grooming | 30 min | PM + Designer |

### Monthly Cadence

| Activity | Duration | Participants |
|----------|----------|--------------|
| Metrics review | 1 hour | Full team |
| Opportunity assessment | 1 hour | PM + Design + Eng leads |
| Strategy check | 1 hour | Leadership |

---

## Cohort Analysis

### Types

| Type | Definition | Use Case |
|------|------------|----------|
| **Acquisition cohorts** | Users grouped by sign-up date | Track retention over time |
| **Behavioral cohorts** | Users grouped by behavior | Compare engaged vs. unengaged |
| **Feature cohorts** | Users grouped by feature usage | Understand feature impact |

### Retention Cohort Table

```
         Week 1  Week 2  Week 3  Week 4  Week 5  Week 6
Jan      100%    40%     35%     32%     30%     28%
Feb      100%    42%     38%     35%     33%     -
Mar      100%    45%     40%     37%     -       -
Apr      100%    48%     43%     -       -       -
May      100%    50%     -       -       -       -
```

**Key Questions:**
- Is retention improving for newer cohorts?
- Where do users drop off?
- Do engaged users behave differently?

---

## Anti-Patterns to Avoid

### Vanity Metrics
- **Problem:** Tracking total signups instead of active users
- **Solution:** Focus on metrics that reflect real value delivery

### Metric Paranoia
- **Problem:** Tracking too many metrics, no focus
- **Solution:** North Star + 3-5 input metrics, HEART for feature health

### A/B Testing Everything
- **Problem:** Slow iteration, statistical noise
- **Solution:** Test strategically, ship obvious improvements

### Ignoring Qualitative Data
- **Problem:** Numbers don't explain "why"
- **Solution:** Pair quantitative analysis with user interviews

### Goal Displacement
- **Problem:** Optimizing for metrics at expense of user experience
- **Solution:** Guardrail metrics + ethical design hierarchy

### Testing Without Baseline
- **Problem:** Running A/B tests without establishing baseline metrics first. Without a baseline, you can't measure real lift — only relative change within the test period.
- **Solution:** Document baseline metrics for at least 2 weeks before launching any experiment. Include seasonality and day-of-week variance.

### Premature Optimization
- **Problem:** Optimizing micro-conversions when macro-level product-market fit is unproven.
- **Solution:** If D7 retention is <20%, don't optimize button colors — go back to Phase 1 and validate you're solving the right problem.

---

## Quality Criteria

Optimization is evidence-driven when: (1) every metric has a clear Goal-Signal-Metric chain, (2) experiments run for minimum 2 weeks with statistical significance calculated, (3) counter-metrics are tracked alongside primary metrics, (4) learnings are documented and fed back into the opportunity backlog, (5) Product Kata cycles produce weekly learnings.

---

## Definition of Done

Phase 7 is ongoing, but you're in a good rhythm when:

- [ ] HEART framework with Goals, Signals, Metrics for all applicable dimensions
- [ ] AARRR funnel analysis with drop-off hypotheses
- [ ] Goals-Signals-Metrics consolidated table
- [ ] Experiment backlog with hypotheses, success criteria, and guardrail metrics
- [ ] Product Kata plan (Direction, Current State, Target Condition, Experiments)
- [ ] North Star Metric defined with input metric tree
- [ ] Metrics are user-facing outcomes (not system internals)
- [ ] Experiment duration >= 2 weeks
- [ ] Weekly continuous discovery rhythm established
- [ ] Cohort analysis set up for retention tracking
- [ ] Anomaly alerts configured

---

## Cross-Phase References

**Input from Earlier Phases:**
- Problem statements (Phase 2) → HEART goals
- User flows (Phase 3) → Funnel stages
- Test findings (Phase 5) → Experiment hypotheses
- Acceptance criteria (Phase 6) → Success baselines

**Output feeds into:**
- Phase 1 (Discovery): New research questions from data
- Phase 2 (Define): Updated personas from behavior data
- Phase 5 (Validate): New features to test

---

## Context-Adaptive Depth

| Mode | Metrics | Experiments | Cadence |
|------|---------|-------------|---------|
| **MVP** | Core metrics only | Fast iteration, low statistical rigor | Ad-hoc |
| **Growth** | HEART + AARRR | Proper A/B testing | Weekly rhythm |
| **Enterprise** | Full framework + compliance | Statistical rigor + documentation | Daily/weekly rituals |

---

## Templates Used

- `templates/goals-signals-metrics-template.md`
- `templates/experiment-backlog-template.md`
- `templates/north-star-metric-template.md`

---

## Looping Back

The product development cycle is continuous. Every optimization insight should feed back into earlier phases.

### Loop-Back Decision Guide

| Condition | Target Phase | Scope |
|-----------|-------------|-------|
| D7 retention <20% | Phase 1 (Discovery) | Re-examine product-market fit |
| 3+ A/B tests with no significant lift | Phase 2 (Define) | Reframe the hypothesis and problem |
| New user segment discovered in analytics | Phase 1 (Discovery) | Targeted research for new segment |
| Support tickets reveal new pain point cluster | Phase 2 (Define) | Update personas and journey maps |
| Funnel drop-off at a specific flow step | Phase 3 (IA) or Phase 4 (Prototype) | Redesign the failing flow |
| Accessibility complaints post-launch | Phase 5 (Validate) | Re-run accessibility audit |

### Loop-Back Protocol
1. Carry all optimization data as evidence into the target phase
2. Narrow the scope to the specific area triggering the loop-back
3. Update the Four-Risk Gate assessment
4. Set clear exit criteria before re-advancing

> Return to: `skills/ux-discover/SKILL.md` — Phase 1: Discovery & Research
