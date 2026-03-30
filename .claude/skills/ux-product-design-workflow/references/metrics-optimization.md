# Post-Launch Metrics & Optimization

## Table of Contents
1. [HEART Framework (UX Quality)](#heart-framework)
2. [Goals-Signals-Metrics Process](#goals-signals-metrics-process)
3. [AARRR Pirate Metrics (Growth)](#aarrr-pirate-metrics)
4. [Combining HEART and AARRR](#combining-heart-and-aarrr)
5. [A/B Testing Methodology](#ab-testing-methodology)
6. [Cohort Analysis](#cohort-analysis)
7. [AI-Driven Optimization](#ai-driven-optimization)
8. [Continuous Improvement Loop](#continuous-improvement-loop)

---

## HEART Framework

Developed by Google's UX research team (Kerry Rodden et al.), HEART shifts focus from basic traffic metrics to nuanced experience quality.

### The Five Dimensions

**Happiness** — Subjective user attitudes and satisfaction
- CSAT (Customer Satisfaction Score)
- NPS (Net Promoter Score)
- Perceived ease of use
- Post-task satisfaction surveys
- App store ratings and sentiment

**Engagement** — Depth, frequency, and intensity of involvement
- Session length and depth
- Frequency of visits (daily, weekly, monthly)
- Feature-specific usage metrics
- Content interaction rates (likes, shares, saves)
- Return visit patterns

**Adoption** — Acquisition of new users for product or feature
- New user signups over time
- Feature adoption rates after launch
- Percentage of users trying new payment methods
- Upgrade/conversion rates
- First-time feature usage

**Retention** — Rate at which existing users return
- Day 1, 7, 30 retention rates
- Cohort retention curves
- Churn rate and churn reasons
- Reactivation rates
- Subscription renewal rates

**Task Success** — Behavioral efficiency and effectiveness
- Task completion rates
- Time-on-task (benchmark against industry standards)
- Error rates (slips and mistakes per task)
- Drop-off points in critical flows
- Number of steps to complete core tasks

---

## Goals-Signals-Metrics Process

The bridge between HEART dimensions and actionable dashboards:

### Step 1: Articulate the Goal
What user experience outcome does the team care about for this feature?

Example: "New users should feel confident completing their first financial transaction."

### Step 2: Identify Signals
What user behavior would indicate success or failure of this goal?

Signals of success:
- User completes first transaction
- User completes transaction without contacting support
- User returns to make a second transaction within 7 days

Signals of failure:
- User abandons at payment confirmation screen
- User contacts support during first transaction
- User uninstalls within 24 hours of first transaction attempt

### Step 3: Build Specific Metrics
Transform signals into trackable, measurable numbers.

| Signal | Metric | Target |
|--------|--------|--------|
| Completes first transaction | First transaction completion rate | >70% within 48 hours |
| No support contact needed | Support ticket rate for first-timers | <5% |
| Returns for second transaction | D7 transaction retention | >40% |
| Abandons at confirmation | Confirmation screen drop-off rate | <15% |

### Dashboard Design

- Group metrics by HEART dimension
- Show trends over time, not just current values
- Include cohort breakdowns (new vs. returning, by segment)
- Set up automated alerts for metric degradation
- Review dashboards weekly as a Triad

---

## AARRR Pirate Metrics

Ensures the product drives sustainable business growth by tracking the customer lifecycle funnel.

### Acquisition — How people discover you
- Cost Per Acquisition (CPA)
- Customer Acquisition Cost (CAC)
- Conversion rates by source/channel
- Organic vs. paid traffic ratios
- App store ranking and visibility

### Activation — The "Aha!" moment
- Time to value (how quickly users experience core benefit)
- Onboarding completion rate
- Activation rate (% completing key first action)
- First session depth and engagement
- Setup completion percentage

### Retention — Continued engagement
- Monthly Active Users (MAU) / Daily Active Users (DAU)
- Cohort retention curves (D1, D7, D30, D90)
- Feature stickiness (DAU/MAU ratio)
- Churn rate and prediction models
- Re-engagement campaign effectiveness

### Referral — Users recommending you
- Viral coefficient (K-factor)
- Referral link click-through rates
- Invite conversion rates
- NPS (promoter score correlates with referral behavior)
- Social sharing frequency

### Revenue — Financial value generated
- Average Revenue Per User (ARPU)
- Monthly Recurring Revenue (MRR) growth
- Customer Lifetime Value (CLV)
- Break-even revenue metrics
- Revenue per cohort

---

## Combining HEART and AARRR

These frameworks are complementary:

- **HEART** ensures the product is usable and loved (UX quality)
- **AARRR** ensures the product is viable and growing (business health)

| AARRR Stage | Relevant HEART Dimensions |
|-------------|--------------------------|
| Acquisition | Adoption (how many new users) |
| Activation | Task Success (can they complete setup?), Happiness (first impression) |
| Retention | Retention (do they come back?), Engagement (how deeply?) |
| Referral | Happiness (would they recommend?), Engagement (how invested?) |
| Revenue | All dimensions contribute to willingness to pay |

A balanced approach ensures the team neither sacrifices UX for short-term revenue nor ignores financial viability.

---

## A/B Testing Methodology

### When to A/B Test

- You have a specific, measurable hypothesis
- You have sufficient traffic for statistical significance
- The change is isolated enough to attribute results
- The risk of the variant is acceptable

### Running Effective Tests

**1. Formulate hypothesis:**
"Changing the CTA from 'Sign Up' to 'Start Free' will increase activation rate by 15% because it reduces perceived commitment."

**2. Determine sample size:**
- Use statistical power calculators
- Minimum detectable effect: what's the smallest improvement worth detecting?
- Typical: 95% confidence level, 80% statistical power

**3. Randomize and segment:**
- Random assignment to control vs. variant
- Segment by relevant factors (new vs. returning, device, geography)
- Ensure groups are balanced

**4. Run for adequate duration:**
- Minimum 1-2 full business cycles (usually 2 weeks)
- Account for day-of-week effects
- Don't peek at results early and make decisions

**5. Analyze results:**
- Primary metric: the one you hypothesized about
- Secondary metrics: guard rails (ensure you didn't hurt other metrics)
- Segment analysis: did it work better for some groups?

**6. Document and share:**
- What was tested, why, results, decision made
- Build institutional knowledge of what works

### Common Pitfalls

- Testing too many things at once (can't attribute results)
- Stopping tests too early based on initial trends
- Ignoring novelty effects (users may engage more with anything new)
- Not considering long-term effects on retention
- Testing cosmetic changes when structural changes are needed

---

## Cohort Analysis

### Purpose
Track how specific groups of users behave over time, rather than looking at aggregate metrics that can mask important trends.

### Common Cohort Types

- **Acquisition cohort:** Users who signed up in the same week/month
- **Behavioral cohort:** Users who performed a specific action (e.g., first purchase)
- **Feature cohort:** Users who adopted a specific feature

### Reading Cohort Tables

```
              Week 0   Week 1   Week 2   Week 3   Week 4
Jan cohort    100%     45%      32%      28%      25%
Feb cohort    100%     52%      38%      33%      --
Mar cohort    100%     58%      42%      --       --
```

Interpretation: Later cohorts are retaining better, suggesting product improvements are working.

### What to Look For

- **Retention curves:** Are they flattening (good) or declining (bad)?
- **Cohort comparison:** Are newer cohorts performing better than older ones?
- **Feature impact:** Do cohorts who use feature X retain better?
- **Seasonal effects:** Are patterns consistent or cyclical?

---

## AI-Driven Optimization

### Automated Monitoring

Deploy AI agents to continuously monitor product analytics dashboards:
- Background anomaly detection: automatically flag unexpected drops in task success or spikes in churn
- Pattern recognition across segments: identify which user groups are affected
- Root cause hypothesis generation: suggest potential causes based on correlating metrics
- Alert prioritization: distinguish signal from noise

### Agentic Experimentation

Bounded AI agents can propose and run micro-optimizations under human governance:
- Dynamically adjust CTA copy based on user segment
- Optimize email send times based on engagement patterns
- Personalize onboarding flows based on user characteristics
- Suggest feature flag rollout strategies

Critical constraint: all AI-driven changes must remain under human review and approval. The AI proposes, the Triad decides.

### Predictive Analytics

- Churn prediction models: identify at-risk users before they leave
- LTV prediction: estimate customer lifetime value for acquisition optimization
- Feature impact forecasting: predict how changes will affect key metrics
- Anomaly forecasting: distinguish expected seasonal changes from actual problems

---

## Continuous Improvement Loop

### The Weekly Rhythm

1. **Monday:** Review dashboard metrics from previous week
2. **Tuesday-Wednesday:** Conduct user interviews (continuous discovery)
3. **Thursday:** Triad meets to synthesize insights and prioritize experiments
4. **Friday:** Ship small improvements, set up next week's tests

### Product Kata Application

Apply the four-step cycle continuously:

1. **Direction:** "Become the most trusted digital wallet" (stable)
2. **Current:** "First-transaction completion is 62%, target is 80%"
3. **Target:** "Reach 70% completion by end of month"
4. **Experiment:** "Hypothesis: adding a fee preview screen before confirmation will reduce drop-off by 10%. Test duration: 2 weeks."

After each experiment: What did we expect? What happened? What did we learn? What's our next experiment?

### Feeding Back into Discovery

Post-launch data feeds directly back into the discovery phase:
- Analytics anomalies become research questions
- Support ticket themes become interview topics
- Cohort analysis reveals underserved segments
- A/B test results inform the opportunity backlog

The cycle is continuous: Discover > Define > Develop > Deliver > Measure > Discover again.

---

## North Star Metric

### Concept

A North Star Metric (NSM) is the single metric that best captures the core value your product delivers to customers. It aligns the entire organization around one measurable outcome. The North Star Metric concept was popularized by Amplitude and Reforge.

**Characteristics of a good NSM:**
- Reflects value delivered to users (not just revenue)
- Is a leading indicator of long-term business success
- Is influenced by the entire product team's work
- Is understandable by everyone in the organization
- Moves incrementally with product improvements

### Examples by Product Type

| Product Type | North Star Metric | Why |
|-------------|------------------|-----|
| **Mobile wallet** | Weekly active transactors | Reflects habitual value delivery |
| **E-commerce** | Weekly purchases per active customer | Shows repeat engagement |
| **SaaS** | Weekly active users completing core task | Captures activation + retention |
| **Content platform** | Total daily reading time | Indicates engagement depth |
| **Messaging** | Messages sent per day | Core loop usage |

### NSM + Input Metrics

The NSM sits atop a tree of input metrics that the team can directly influence:

```
        [North Star: Weekly Active Transactors]
                    │
     ┌──────────────┼──────────────┐
     │              │              │
[New users    [Returning      [Transactions
 activated]    users]          per user]
     │              │              │
┌────┴────┐    ┌───┴───┐     ┌───┴───┐
[Sign-up  [Onboarding [D7    [D30   [Avg    [Failed
 rate]     complete]  retain] retain] txns]   txn %]
```

Each input metric is owned by a specific squad or initiative. Improvements to input metrics compound into NSM growth.

---

## Metric Hierarchy & Taxonomy

### Three Levels

**Level 1: Outcome Metrics (Lagging)**
- Business results: revenue, profit, market share
- User outcomes: retention, satisfaction, NPS
- Updated monthly or quarterly
- Owned by leadership and PM

**Level 2: Driver Metrics (Leading)**
- Behavioral indicators that predict outcomes
- Feature adoption, activation rate, frequency
- Updated weekly
- Owned by product triads

**Level 3: Health Metrics (Guardrails)**
- System and experience quality indicators
- Error rates, latency, crash rate, support ticket volume
- Monitored continuously
- Owned by engineering and design

### Counter-Metrics

Every metric you optimize for should have a counter-metric that guards against gaming:

| Primary Metric | Risk If Gamed | Counter-Metric |
|---------------|---------------|----------------|
| Sign-up rate | Low-quality users | D7 activation rate |
| Session length | Endless scrolling, frustration | Task completion rate |
| Feature adoption | Forced adoption via dark patterns | Voluntary repeat usage |
| Support ticket reduction | Hiding support channels | CSAT, app store rating |
| Transaction volume | Micro-transactions inflating count | Avg transaction value |

---

## Dashboard Design Best Practices

### Layout Principles

1. **Hierarchy first:** Most important metric (NSM) at the top, largest
2. **Context always:** Show trends over time, not just current values
3. **Comparison built in:** Period-over-period, cohort-over-cohort, target vs. actual
4. **Segmentation available:** Filterable by user segment, platform, geography
5. **Alerts visible:** Red/yellow/green status indicators for metric health

### Dashboard Types

| Type | Audience | Refresh | Content |
|------|----------|---------|---------|
| **Executive** | Leadership | Weekly | NSM, revenue, growth, 3-5 key metrics |
| **Product** | Triad | Daily | Feature metrics, funnel conversion, experiment results |
| **Engineering** | Dev team | Real-time | Error rates, latency, crash rate, deploy status |
| **Support** | CS team | Real-time | Ticket volume, response time, top issues |

### Common Dashboard Mistakes

- **Too many metrics:** If everything is highlighted, nothing is. Limit to 7-10 metrics per dashboard
- **No context:** A number without trend, target, or comparison is meaningless
- **Vanity metrics only:** Total users, total pageviews — these only go up and tell you nothing
- **No actionability:** If the team can't change a metric, it doesn't belong on their dashboard
- **Stale data:** Dashboards with week-old data become ignored

---

## Experiment Documentation Template

### Before Running

```
## Experiment: [Descriptive Name]

### Hypothesis
We believe that [change] for [user segment]
will result in [measurable outcome]
because [reasoning based on research/data].

### Metrics
- Primary: [the one metric this tests]
- Secondary: [1-2 guardrail metrics]
- Counter-metric: [what we monitor to prevent gaming]

### Design
- Type: [A/B test / multivariate / feature flag rollout]
- Control: [current experience]
- Variant(s): [description of change(s)]
- Sample size needed: [calculated via power analysis]
- Duration: [minimum run time, accounting for business cycles]
- Audience: [all users / segment / % rollout]

### Risks
- What could go wrong?
- What's the rollback plan?
- Are there regulatory considerations?
```

### After Running

```
### Results
- Primary metric: [control vs. variant, with confidence interval]
- Secondary metrics: [any unexpected movement]
- Segment breakdowns: [did it work differently for subgroups?]

### Statistical Validity
- Sample size achieved: [actual vs. planned]
- Confidence level: [%]
- Duration: [actual run time]
- Any anomalies: [novelty effects, external events, data quality issues]

### Decision
- [ ] Ship variant (statistically significant positive result)
- [ ] Iterate (promising but needs refinement)
- [ ] Kill variant (negative or inconclusive result)
- [ ] Extend test (insufficient data)

### Learnings
What did we learn about our users that applies beyond this experiment?
[Document the insight, not just the result]

### Next Experiment
Based on these learnings, our next hypothesis is:
[Link to next experiment doc]
```

### Anti-Patterns in Experimentation

| Anti-Pattern | Why It's Dangerous | Fix |
|-------------|-------------------|-----|
| **Vanity metric addiction** | Total page views, total downloads — these only go up and tell you nothing actionable | Track task success, retention, and activation instead |
| **Ignoring negative feedback loops** | Post-launch complaints or churn signals get dismissed as "edge cases" | Set up automated alerts for metric degradation; treat every churn spike as a research signal |
| **Gut-feeling reliance** | "I think this CTA color will work better" without data | Every experiment needs a hypothesis grounded in research or analytics |
| **HiPPO-driven experiments** | Highest Paid Person's Opinion dictates what gets tested | Use opportunity scoring and evidence-based prioritization |
| **Metric gaming** | Optimizing sign-up rate by reducing friction so much that unqualified users flood in | Always pair a primary metric with a counter-metric (see Counter-Metrics table above) |
| **Post-hoc rationalization** | Test fails, team finds reasons to ship anyway | Pre-register decisions: define "ship/kill/iterate" criteria BEFORE results come in |

### Experiment Log

Maintain a running log of all experiments for institutional memory:

| # | Date | Name | Hypothesis | Primary Metric | Result | Decision | Learning |
|---|------|------|-----------|----------------|--------|----------|----------|
| 1 | Jan | Fee preview | Showing fees reduces drop-off | Confirmation drop-off | -23% drop-off | Ship | Users need cost certainty before committing |
| 2 | Feb | Social proof | Showing user count builds trust | Sign-up rate | +4% (not sig.) | Kill | Trust signals need to be more specific |
| 3 | Mar | Arabic onboarding | Dialect copy > formal | Onboarding completion | +18% completion | Ship | Egyptian dialect dramatically outperforms Fusha in casual flows |

---

## Phase Transition Signals

### Definition of Done for Metrics & Optimization Phase

Before claiming this phase is complete and looping back to Discovery:

- [ ] Analytics dashboards configured for specific HEART and AARRR metrics
- [ ] Baseline metrics established for all tracked dimensions
- [ ] North Star Metric defined and agreed upon by the Triad
- [ ] Counter-metrics established for every primary optimization target
- [ ] At least one complete experiment cycle documented (hypothesis → test → result → learning)
- [ ] Next iteration hypothesis drafted based on live data
- [ ] Continuous discovery cadence established (weekly customer touchpoints)
- [ ] Cohort analysis run comparing at least two acquisition cohorts
- [ ] Anomaly alerting set up for critical metrics (task success, retention, error rate)

### When to Loop Back to Discovery

The optimization phase feeds directly back into the discovery phase. Loop back when:

- **Metrics plateau:** Incremental experiments stop moving the NSM — you need new insights
- **New user segment emerges:** Cohort analysis reveals an underserved group you didn't design for
- **Support ticket themes shift:** New complaint patterns indicate unmet needs
- **Market disruption:** Competitor launches or regulatory changes invalidate assumptions
- **Quarterly cadence:** Even without crisis signals, schedule quarterly deep-discovery cycles

The workflow is a continuous cycle: **Discover → Define → Develop → Deliver → Measure → Discover again.**

---

### Cross-References
- For UX law compliance metrics → `laws-of-ux.md` (Doherty Threshold → response time metrics)
- For competitive benchmark metrics → `competitive-analysis.md`
- For state design impact on task success → `ideation-prototyping.md`
- For A/B test UX considerations → `usability-testing.md`
- For AI-driven optimization patterns → `agentic-ai-design.md`
- For MENA-specific market benchmarks → `arabic-rtl-mena.md`
