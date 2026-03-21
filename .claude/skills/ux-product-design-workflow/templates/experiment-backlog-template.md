# Experiment Backlog Template

## Experiment Backlog Overview

| Attribute | Value |
|-----------|-------|
| **Product/Feature** | [Name] |
| **Owner** | [Name] |
| **Last Updated** | [Date] |
| **Active Experiments** | [#] |
| **Backlog Experiments** | [#] |

---

## Experiment Hypothesis Format

> "We believe that **[change]** will **[outcome]** because **[evidence/rationale]**."

---

## Active Experiments

### Experiment 1: [Name]

| Element | Details |
|---------|---------|
| **Hypothesis** | "We believe that [change] will [outcome] because [evidence]." |
| **Success Metric** | [Primary metric this experiment affects] |
| **Guardrail Metrics** | [Metrics that shouldn't degrade] |
| **Minimum Detectable Effect** | [% or absolute value] |
| **Sample Size** | [Calculated sample size] |
| **Duration** | [Weeks] |
| **Traffic Split** | [e.g., 50/50 or 90/10] |
| **Status** | [Running] |
| **Start Date** | [Date] |
| **Target End Date** | [Date] |

---

### Experiment 2: [Name]

| Element | Details |
|---------|---------|
| **Hypothesis** | "We believe that [change] will [outcome] because [evidence]." |
| **Success Metric** | [Primary metric] |
| **Guardrail Metrics** | [Metrics that shouldn't degrade] |
| **Minimum Detectable Effect** | [%] |
| **Sample Size** | [#] |
| **Duration** | [Weeks] |
| **Traffic Split** | [Split] |
| **Status** | [Running] |
| **Start Date** | [Date] |

---

## Prioritized Backlog

### Priority 1: [Experiment Name]

| Element | Details |
|---------|---------|
| **Hypothesis** | "We believe that [change] will [outcome] because [evidence]." |
| **Success Metric** | [Primary metric] |
| **Expected Impact** | [High/Medium/Low] |
| **Implementation Effort** | [High/Medium/Low] |
| **Priority Score** | [Impact/Effort ratio or ICE score] |
| **Status** | [Backlog] |

---

### Priority 2: [Experiment Name]

| Element | Details |
|---------|---------|
| **Hypothesis** | "We believe that [change] will [outcome] because [evidence]." |
| **Success Metric** | [Primary metric] |
| **Expected Impact** | [High/Medium/Low] |
| **Implementation Effort** | [High/Medium/Low] |
| **Priority Score** | [Score] |
| **Status** | [Backlog] |

---

### Priority 3: [Experiment Name]

| Element | Details |
|---------|---------|
| **Hypothesis** | "We believe that [change] will [outcome] because [evidence]." |
| **Success Metric** | [Primary metric] |
| **Expected Impact** | [High/Medium/Low] |
| **Implementation Effort** | [High/Medium/Low] |
| **Priority Score** | [Score] |
| **Status** | [Backlog] |

---

## Completed Experiments

### Experiment: [Name]

| Element | Details |
|---------|---------|
| **Hypothesis** | "We believed that [change] would [outcome] because [evidence]." |
| **Result** | [Win/Loss/Inconclusive] |
| **Impact** | [% change observed] |
| **Statistical Significance** | [% confidence] |
| **Decision** | [Ship/Iterate/Abandon] |
| **Learnings** | [What we learned] |
| **Next Step** | [What we're doing next] |

---

### Experiment: [Name]

| Element | Details |
|---------|---------|
| **Hypothesis** | "We believed that [change] would [outcome] because [evidence]." |
| **Result** | [Win/Loss/Inconclusive] |
| **Impact** | [% change observed] |
| **Statistical Significance** | [% confidence] |
| **Decision** | [Ship/Iterate/Abandon] |
| **Learnings** | [What we learned] |
| **Next Step** | [What we're doing next] |

---

## Experiment Ideas (Unprioritized)

| # | Hypothesis | Source | Impact Guess | Effort Guess |
|---|------------|--------|--------------|--------------|
| 1 | "We believe that [change] will [outcome] because [evidence]." | [Research/Analytics/Feedback] | [H/M/L] | [H/M/L] |
| 2 | [Hypothesis] | [Source] | [H/M/L] | [H/M/L] |

---

## Priority Framework

### ICE Scoring

| Factor | Description | Scale |
|--------|-------------|-------|
| **Impact** | How much will this move the metric? | 1-10 |
| **Confidence** | How sure are we this will work? | 1-10 |
| **Ease** | How easy is this to implement? | 1-10 |

**ICE Score = (Impact × Confidence × Ease) ÷ 10**

### Priority Matrix

| High Impact, Low Effort | High Impact, High Effort |
| ----------------------- | ------------------------ |
| **Do First** | **Plan Carefully** |
| [Experiments] | [Experiments] |

| Low Impact, Low Effort | Low Impact, High Effort |
| ---------------------- | ----------------------- |
| **Fill-in Work** | **Avoid** |
| [Experiments] | [Experiments] |

---

## A/B Test Requirements Checklist

Before launching any experiment:

- [ ] Hypothesis clearly stated in format
- [ ] Success metric defined
- [ ] Guardrail metrics defined
- [ ] Sample size calculated for statistical significance
- [ ] Minimum detectable effect determined
- [ ] Test duration set (minimum 2 weeks)
- [ ] Traffic split decided
- [ ] Segment targeting defined
- [ ] Rollout plan documented
- [ ] Kill switch in place
- [ ] Analytics tracking verified

---

## Learning Log

| Date | Experiment | Key Learning | Implication |
|------|------------|--------------|-------------|
| [Date] | [Experiment name] | [What we learned] | [What this means for future work] |

---

## Connected Artifacts

| Artifact | Relationship | Link |
|----------|--------------|------|
| Goals-Signals-Metrics | [Metrics experiments target] | [Link] |
| North Star Metric | [How experiments support NSM] | [Link] |
| User Research | [Insights that inform hypotheses] | [Link] |

---

## Metadata

| Field | Value |
|-------|-------|
| Created | [Date] |
| Owner | [Name] |
| Last Updated | [Date] |
| Review Cadence | [Weekly] |
