---
name: ux-product-design-workflow
description: >
  Complete UX and Product Design workflow system integrating Double Diamond, Lean UX, Product Kata,
  JTBD, Laws of UX, HEART/AARRR metrics, ethical design hierarchy, four product risks, confidence
  scoring, and agentic AI design patterns. Guides teams through the full product lifecycle:
  Discovery, Define, IA & Interaction Design, Prototype, Validate, Handoff, and Optimize
  with phase transition signals.

  Use this skill whenever the user is working on product design, UX workflows, user research,
  usability testing, design systems, information architecture, interaction design, prototyping,
  user journey mapping, persona creation, design handoff, post-launch optimization, or building
  digital products. Also use when the user mentions Arabic RTL interfaces, MENA/Egyptian fintech
  design, mobile-first design for emerging markets, or Human-AI interaction design patterns.

  Trigger on any mention of: product design process, UX workflow, design thinking, user research
  planning, journey mapping, persona development, wireframing workflow, prototype testing plan,
  heuristic evaluation, accessibility audit planning, design sprint, JTBD analysis, opportunity
  mapping, design-to-code handoff, HEART metrics, pirate metrics, A/B testing strategy, RTL
  design, fintech UX, agentic UI patterns, competitive analysis, card sorting, empathy mapping,
  problem statement writing, How Might We statements, usability report, design tokens, or
  component library planning. Even if the user says "help me design a feature" or "plan a new
  app" — this skill applies.
---

# UX & Product Design Workflow

## How to Use This Skill

This skill is an operating system for product design, not a rigid recipe. Adapt it to the user's context:

**Identify where they are.** Use the Quick Decision Guide (bottom of this file) to figure out which phase applies. Most users aren't starting from scratch — they're mid-stream. Meet them there.

**Produce actionable artifacts, not lectures.** When a user asks for help with personas, produce a persona — don't just explain what one is. When they need a journey map, draft one. Reference the checklists to ensure completeness, but the output should be a working deliverable they can use immediately.

**Scale to their context.** A solo founder building an MVP needs a 2-page research summary, not a 40-page report. A design system team at a bank needs rigor and compliance. Read the room.

**Be opinionated with reasons.** Don't present 5 options without a recommendation. State what you'd do and why, then let them adjust. The frameworks here are guidelines — the user's judgment and context always take precedence.

**Output format defaults:**
- Research plans → structured markdown with timeline, methods, and participant criteria
- Personas → name, photo placeholder, demographics, behaviors, goals, pain points, JTBD, representative quote
- Journey maps → stage-based table with touchpoints, actions, emotions, pain points, opportunities
- Problem statements → "[User] needs a way to [need] because [insight]"
- Wireframe descriptions → annotated screen-by-screen flow descriptions (since you can't draw)
- Test plans → objectives, methodology, tasks, metrics, participant criteria, schedule
- Reports → executive summary, key findings (prioritized), recommendations, metrics

---

## Framework Foundation

Three frameworks power this workflow. You don't need to explain them unless the user asks — just apply their principles.

| Framework | Core Loop | When It Applies |
|-----------|-----------|-----------------|
| **Double Diamond** | Discover > Define > Develop > Deliver | Macro structure: diverge first, then converge. Twice. |
| **Lean UX** | Think > Make > Check | Within each phase: form a hypothesis, build the minimum artifact to test it, measure. |
| **Product Kata** | Direction > Current > Target > Experiment | Post-launch: set a target, run experiments, learn, repeat weekly. |

> Deep dive: `references/frameworks.md` — includes the Opportunity Solution Tree, Continuous Discovery Habits, and Product Triad operating model.

---

## Ethical Design Hierarchy

Non-negotiable baseline. Lower levels must be satisfied before pursuing higher ones:

| Level | Focus | Rule |
|-------|-------|------|
| **1. Human Rights** | Accessibility, privacy, security, inclusivity | Never ship anything that compromises safety, access, or dignity |
| **2. Functionality** | Usability, performance, reliability | The product must work well for its intended purpose |
| **3. Delight** | Emotional resonance, surprise, joy | Only pursue when Levels 1-2 are solid |

Never sacrifice accessibility for aesthetics. Never sacrifice privacy for personalization. Never sacrifice safety for speed-to-market.

---

## The Four Product Risks

Every product initiative faces four risks that the Triad must address together:

| Risk | Question | Owner |
|------|----------|-------|
| **Value risk** | Will users want this? | PM + Design (validated through research) |
| **Usability risk** | Can users figure it out? | Design (validated through testing) |
| **Feasibility risk** | Can engineering build it? | Engineering (validated through spikes/prototypes) |
| **Viability risk** | Does it work for the business? | PM (validated through business modeling) |

If any one risk is unaddressed, the product fails. The Triad model exists to ensure all four are covered.

---

## The Product Triad

Every phase works best when three disciplines collaborate as equals:

| Role | Owns | Asks |
|------|------|------|
| **Product Management** (Viability) | Business goals, roadmap priorities, success criteria | "Does this make business sense?" |
| **UX Design** (Desirability) | User needs, experience quality, research insights | "Does this solve a real user problem?" |
| **Engineering** (Feasibility) | Technical architecture, performance, scalability | "Can we build and maintain this?" |

The tension between these three perspectives is productive. No single discipline should dominate. When all three agree on shared outcome metrics (activation rate, retention, NPS), the product wins.

---

## Phase Map

```
     DIAMOND 1: Right Problem              DIAMOND 2: Right Solution
  ┌──────────────────────────────┐     ┌──────────────────────────────┐
  │ Phase 1       Phase 2        │     │ Phase 3       Phase 4        │
  │ DISCOVER      DEFINE         │     │ IA & INTERACT PROTOTYPE      │
  │ (Diverge)     (Converge)     │     │ (Diverge)     (Converge)     │
  │                              │     │                              │
  │ Understand    Synthesize     │     │ Structure &   Build &        │
  │ users &       into focus     │     │ map flows     refine         │
  │ problem                      │     │               the best       │
  └──────────────────────────────┘     └──────────────────────────────┘

  Phase 5: VALIDATE        Phase 6: HANDOFF          Phase 7: OPTIMIZE
  Test with real users     Ship to engineering       Measure, learn, iterate
  ────────────────────     ────────────────────      ────────────────────
  Usability testing        Annotated specs           HEART + AARRR metrics
  Heuristic evaluation     State documentation       A/B experiments
  Accessibility audit      Edge case catalogs        Continuous discovery
  Human-AI checks          Acceptance criteria       Product Kata cycles
```

**Phase Transition Signals:** Each phase has a "Definition of Done" checklist. Don't advance until you've met the transition criteria — they're documented in each phase's reference file. Moving forward prematurely is the most common cause of product failure.

### Non-Linear Workflows & Iteration

Real product work is not a straight line. Phases loop back when new evidence surfaces:

| Trigger | Loop-Back Target | Action |
|---------|-----------------|--------|
| Phase 5 testing reveals users don't understand core concept | Phase 2 (Define) | Revisit problem statements and personas with new evidence |
| Phase 5 task completion <60% on a core flow | Phase 3 (IA) or Phase 4 (Prototype) | Restructure flow or redesign interaction |
| Phase 7 metrics show D7 retention <20% | Phase 1 (Discovery) | Re-examine whether you're solving the right problem |
| Phase 4 engineering review reveals infeasibility | Phase 3 (IA) | Explore alternative solution architecture |
| Phase 6 handoff reveals undocumented edge cases | Phase 4 (Prototype) | Design missing states, update prototype |
| Phase 7 A/B test shows no significant lift | Phase 2 (Define) | Reframe the hypothesis, re-examine assumptions |

**Loop-back rules:**
1. Always carry forward the evidence that triggered the loop-back — don't restart from scratch
2. Update the Four-Risk Gate assessment when looping back
3. Only revisit the minimum scope needed — don't re-do entire phases
4. Document the loop-back reason in the project's phase-status.json

### Sample Size Guide

Different methods need different participant counts — here's why:

| Method | Recommended N | Rationale |
|--------|--------------|-----------|
| User interviews (Phase 1) | 5-8 per segment | Qualitative saturation: ~85% of themes emerge by user 5 (Nielsen/Landauer) |
| Card sorting (Phase 3) | 15-30 | Statistical: need enough data for dendrogram clustering and agreement metrics |
| Usability testing (Phase 5) | 5-8 per segment | Diminishing returns: 5 users find ~85% of usability issues |
| A/B testing (Phase 7) | Calculate per-test | Statistical power: depends on baseline conversion, MDE, and significance level |
| Tree testing (Phase 3) | 30-50 | Quantitative: need statistical confidence in path success rates |

---

## Phase 1: Discovery & Research

**Goal:** Deeply understand users, context, behaviors, and pain points *before* proposing solutions.

**When to move on:** You can articulate who the users are, what jobs they're hiring solutions for, and where the biggest unmet needs live — backed by evidence, not assumptions.

### Checklist

- [ ] Align stakeholders on business objectives, constraints, and desired outcomes
- [ ] Map existing assumptions explicitly (so you can test them, not just confirm them)
- [ ] Conduct user interviews (minimum 5-8 per segment) using JTBD-style questions
- [ ] Perform contextual inquiry / field studies where possible
- [ ] Run competitive analysis: feature matrix, UX teardowns, positioning gaps
- [ ] Review existing analytics: heatmaps, funnels, support tickets, error logs
- [ ] Create empathy maps (Says, Thinks, Does, Feels, Sees, Hears) per segment
- [ ] Document JTBD job statements and job maps
- [ ] Build initial opportunity backlog

### JTBD Quick Reference

Users hire products to make progress. Map their chronological steps:

**Define > Locate > Prepare > Confirm > Execute > Monitor > Modify**

At each step, identify: **underserved** (opportunity) or **overserved** (simplify).

**Enhanced JTBD Statement Format:**

> "When [circumstance], I want to [job], so I can [need/outcome] without [pain point]."

Example: "When I receive my monthly salary, I want to pay all my bills in one session, so I can feel financially organized without worrying I've missed a payment or been overcharged."

This format captures context (when), motivation (want), desired outcome (so I can), and friction (without) — giving designers richer material than simple job statements.

### Deliverables

| Artifact | Purpose | Format |
|----------|---------|--------|
| Research synthesis | Distill raw data into themes | Themed insight cards with evidence |
| Empathy maps | Capture user psychology | 6-quadrant canvas per segment |
| JTBD job map | Map the user's job chronologically | Step-by-step with service gaps |
| Competitive landscape | Position against alternatives | Feature matrix + UX teardown |
| Opportunity backlog | Prioritize unmet needs | Ranked list with evidence weight |

### Anti-Patterns

- **Confirmation tourism:** Interviewing only to validate what you already believe. Actively seek disconfirming evidence.
- **Persona theater:** Creating personas from demographics and guesses instead of behavioral research data.
- **Analysis paralysis:** Researching endlessly without converging. Set a timebox. 2-4 weeks is usually enough.
- **Skipping to solutions:** "I already know what to build" — the most expensive assumption in product development.
- **Solo research:** Conducting research without stakeholder involvement. Insights that aren't shared don't drive decisions.
- **Data hoarding:** Collecting data without documenting it in a retrievable format. Raw notes decay; tagged evidence compounds.

> Deep dive: `references/discovery-synthesis.md` — JTBD interview questions, empathy mapping, 5W1H, CATWOE, cognitive prompting for AI synthesis, bias mitigation.
> Deep dive: `references/competitive-analysis.md` — competitive analysis frameworks, UX teardown methodology, positioning strategy.

---

## Phase 2: Define & Problem Framing

**Goal:** Converge raw research into specific, actionable problem statements.

**When to move on:** The team can state exactly which user problem they're solving, for whom, and why it matters — and everyone agrees.

### Checklist

- [ ] Affinity map all findings into thematic clusters
- [ ] Prioritize themes by frequency, severity, and business impact
- [ ] Create user personas (2-4 primary) grounded in research evidence
- [ ] Build user journey maps: stages, touchpoints, actions, emotions, pain points, opportunities
- [ ] Formulate problem statements: "[User] needs a way to [need] because [insight]"
- [ ] Write "How Might We" statements — not too broad, not too narrow
- [ ] Build Opportunity Solution Tree: Outcome Metric > Opportunities > Solutions > Experiments
- [ ] Validate definitions against user data (not assumptions)
- [ ] Create design brief with scope, constraints, and success criteria

### Problem Statement Quality Check

Good: "First-time mobile wallet users in Egypt need a way to understand transaction fees upfront because hidden costs at checkout cause 43% abandonment and erode trust in digital payments."

Bad: "Users need a better checkout experience." (Vague, no evidence, no specific user, no why.)

Test your statement: Is it grounded in evidence? Specific user? Real need (not feature)? Testable? Business-relevant?

### HMW Calibration

| Too Broad | Too Narrow | Just Right |
|-----------|------------|------------|
| "HMW make the app better?" | "HMW add a blue notification badge?" | "HMW help new users feel confident completing their first transaction within 5 minutes?" |
| "HMW improve onboarding?" | "HMW reduce the form to 3 fields?" | "HMW reduce the anxiety that first-time digital payment users feel when committing money?" |

### Deliverables

| Artifact | Purpose | Format |
|----------|---------|--------|
| User personas | Compress audience into empathic models | Profile card: demographics, behaviors, goals, pains, JTBD, quote |
| Journey map | Visualize the end-to-end experience | Stage-based table with emotional arc |
| Problem statements | Focus the team on what to solve | Structured "[User] needs [need] because [insight]" |
| HMW statements | Bridge problems to solution space | Scoped question format |
| Design brief | Align team on scope and constraints | 1-2 page document |

### Example: Persona Template

```
NAME: Mariam, The Cautious First-Timer
AGE: 28 | LOCATION: Cairo | OCCUPATION: Accountant
TECH COMFORT: Medium (uses WhatsApp, Instagram daily; avoids new apps)

BEHAVIORS:
- Pays bills through bank branch visits (30-min commute each way)
- Asked a colleague to demonstrate mobile banking before trying it
- Keeps a paper backup of every transaction

GOALS: Save time on routine payments, feel confident money went to the right place
PAIN POINTS: Fears hidden fees, unclear if transaction succeeded, no receipt she can keep

JTBD: "When I need to pay my electricity bill, I want to do it from my phone
so I don't waste half a Saturday at the bank, but I need to feel 100% sure
it went through and know exactly what I was charged."

QUOTE: "I'd rather spend an hour in line than lose money to a glitch."
```

> Deep dive: `references/discovery-synthesis.md` — DIKW pyramid, cognitive prompting workflow, bias mitigation strategies.

---

## Phase 3: Ideation & Information Architecture

**Goal:** Explore solutions widely, then structure the product's content and navigation.

**When to move on:** You have 2-3 strong concepts, a validated information architecture, and wireframes that the team agrees are worth refining.

### Checklist

- [ ] Run structured ideation: SCAMPER, Crazy 8s, Design Studio, or Lateral Thinking
- [ ] Generate 3+ distinct solution concepts per problem
- [ ] Evaluate concepts against desirability, feasibility, and viability
- [ ] Define information architecture through card sorting (open, closed, or hybrid)
- [ ] Create sitemap / app map reflecting user mental models
- [ ] Map user flows and task flows for core scenarios
- [ ] Define interaction patterns for common actions (CRUD, search, filter, navigate)
- [ ] Design all 8 content states per screen: default, empty, loading, partial, error, success, offline, permission
- [ ] Create low-fidelity wireframes focused on layout, hierarchy, and flow
- [ ] Validate IA with tree testing (target >80% on primary paths)

### State Design — The 8 Content States + Interaction States

Every screen has content states and interaction states. Both must be designed explicitly.

**8 Content States** (design these per screen/component in Phase 3):

| State | What the user sees | Design question |
|-------|-------------------|----------------|
| **Default** | Normal data displayed | Is the hierarchy clear? Is the primary action obvious? |
| **Empty** | No data yet | How do we explain and motivate first action? |
| **Loading** | Data being fetched | Skeleton, spinner, or progress bar? |
| **Partial** | Some data available | What loads first? What's deferred? |
| **Error** | Something broke | Can they retry? Is data preserved? What's the error message? |
| **Success** | Action completed | What's the next logical step? Delight moment? |
| **Offline** | No network | What's cached? What's queued for sync? |
| **Permission** | Access needed | Why do we need this? What if they refuse? |

**Interaction States** (design these per interactive element in Phase 4):
- **Default**, **Hover**, **Active/Pressed**, **Focus** (keyboard), **Disabled**

The two categories are orthogonal: a button can be in its "hover" interaction state while the screen shows the "loading" content state.

### Anti-Patterns

- **Premature convergence:** Falling in love with the first idea. Force yourself to generate alternatives.
- **IA by org chart:** Structuring navigation around internal departments instead of user mental models.
- **Wireframe theater:** Creating wireframes no one tests. Even 5 minutes of hallway testing beats zero.
- **Skipping state design:** Only designing the happy path. Empty, error, and offline states are where trust is built or broken.
- **Ignoring feasibility:** Designing flows without engineering input. Check feasibility before investing in detailed wireframes.

> Deep dive: `references/ideation-prototyping.md` — SCAMPER details, card sorting methodology, Design Sprint (5-day), prototyping fidelity guide, design token architecture.

---

## Phase 4: Interaction Design & High-Fidelity Prototyping

**Goal:** Transform wireframes into polished, testable interfaces using established psychological principles.

**When to move on:** The prototype feels real enough that users can give meaningful feedback, and the design system is documented enough that engineers can build from it.

### Laws of UX — Apply Systematically

These aren't suggestions; they're how human brains process interfaces:

| Law | What It Means | Design Action |
|-----|--------------|---------------|
| **Fitts's Law** | Bigger + closer = faster to tap | Primary CTAs: large, thumb-zone, high contrast |
| **Hick's Law** | More choices = slower decisions | Max 5-7 nav items; progressive disclosure |
| **Jakob's Law** | Users expect your site to work like others | Use platform conventions; don't reinvent search |
| **Doherty Threshold** | <300ms response feels instant | Skeleton screens, optimistic UI, preloading |
| **Miller's Law** | Working memory holds ~7 items | Chunk form fields; group related info |
| **Peak-End Rule** | Memory = peak moment + final moment | Design delight at completion; never end on an error |
| **Zeigarnik Effect** | Incomplete tasks nag the mind | Progress bars; "3 of 5 steps complete" |
| **Aesthetic-Usability** | Beautiful = perceived as more usable | Polish builds trust, especially in fintech |
| **Tesler's Law** | Complexity can't be destroyed, only moved | Push complexity to the system, not the user |
| **Postel's Law** | Be liberal in what you accept, strict in output | Flexible input parsing; consistent, predictable output |

### Design System Integration

Build from tokens, not pixels:

```
Primitive:    color-blue-500: #3B82F6    spacing-4: 16px
     ↓
Semantic:     bg-primary: color-blue-500  spacing-section: spacing-8
     ↓
Component:    button-bg: bg-primary       card-padding: spacing-section
```

Designers and developers must speak the same language. Same token names in Figma and code. Same component names. Document the mapping.

### Arabic RTL & MENA Patterns

This is not translation — it's a complete layout and cultural rethink:

**Layout:** Everything mirrors. Navigation right-to-left, progress bars fill right-to-left, back arrows point right, submenus open leftward. Phone numbers and math stay LTR.

**Fintech trust:** Intent-based navigation ("Send Money," "Pay Bills" — not "Products"). Fee previews before commitment. Transaction receipts (downloadable). Biometric auth as primary. Visible security indicators without being intrusive.

**Typography:** Arabic needs larger line-height (1.8-2.0x), renders smaller at same point size as Latin, and uses connected cursive script. Use Cairo, Tajawal, or IBM Plex Arabic.

> Deep dive: `references/arabic-rtl-mena.md` — complete RTL mirroring rules, Egyptian fintech patterns, InstaPay context, trust-building UI, BiDi text handling, mobile-first heuristics for constrained devices.

### Checklist

- [ ] Apply Laws of UX systematically to all core flows
- [ ] Build high-fidelity prototypes with realistic content (not Lorem Ipsum)
- [ ] Integrate design system tokens and components
- [ ] Handle all interaction states per element: default, hover, active, focus, disabled
- [ ] Verify all 8 content states from Phase 3 are refined at high fidelity
- [ ] Apply RTL mirroring and localization patterns (if applicable)
- [ ] Verify responsive behavior across breakpoints (mobile-first)
- [ ] Design micro-interactions purposefully (transitions, feedback animations)
- [ ] Prepare annotation documentation for developer handoff
- [ ] Review against Nielsen's 10 heuristics before user testing

> Deep dive: `references/laws-of-ux.md` — complete Gestalt principles, Postel's Law, Serial Position Effect, Von Restorff Effect, Nielsen's 10 heuristics with application checklist.

---

## Phase 5: Validation & Usability Testing

**Goal:** Rigorously test with real users and fix critical issues before engineering commitment.

**When to move on:** Task completion rate >80% on core flows, no catastrophic usability issues remain, and accessibility meets WCAG AA.

### Checklist

- [ ] Select methodology: remote moderated (deep insight), unmoderated (scale), guerrilla (speed)
- [ ] Recruit 5-8 participants per segment matching your personas
- [ ] Write task scenarios from real jobs: "You want to send EGP 200 to Ahmed for dinner" NOT "Click Send Money"
- [ ] Conduct tests with think-aloud protocol (don't lead, don't help, don't react)
- [ ] Perform heuristic evaluation with 3-5 evaluators against Nielsen's 10 heuristics
- [ ] Run accessibility audit: WCAG 2.1 Level AA minimum (POUR framework)
- [ ] Test Human-AI interaction patterns if AI features are present
- [ ] Measure: task completion (>80%), SUS score (>68), error rate, time-on-task
- [ ] Prioritize findings: impact vs. effort matrix
- [ ] Fix critical/major issues and retest before handoff

### Human-AI Interaction Standards

When your product includes AI features, validate these additional dimensions:

| Principle | What to Test | Red Flag |
|-----------|-------------|----------|
| **Transparency** | Does the user know what AI can/can't do? | User trusts AI blindly or distrusts it entirely |
| **Scoping** | Does AI clarify when it's uncertain? | AI guesses wrong without asking |
| **Error Recovery** | Can users easily correct AI mistakes? | Corrections require starting over |
| **Explainability** | Does the user understand AI's reasoning? | User can't explain why AI recommended X |

### Severity Rating Scale

| Rating | Level | Action |
|--------|-------|--------|
| 4 | **Catastrophic** | Blocks task completion. Must fix before launch. |
| 3 | **Major** | Significant friction. High priority fix. |
| 2 | **Minor** | Inconvenience. Fix when possible. |
| 1 | **Cosmetic** | Polish issue. Fix if time allows. |

### Anti-Patterns

- **Testing with colleagues:** They know too much. Test with real target users.
- **Testing one person:** 5 users find ~85% of issues. One user is an anecdote.
- **Only testing the happy path:** Errors, edge cases, and recovery flows are where products break.
- **Fixing everything at once:** Prioritize. Ship the critical fixes, iterate on the rest.

> Deep dive: `references/usability-testing.md` — testing methodologies, think-aloud verbalization levels, heuristic evaluation process, WCAG POUR audit, reporting templates, iteration prioritization.
> Deep dive: `references/agentic-ai-design.md` — Plan-Act-Reflect pattern, multi-agent UX, XAI design, Human-AI collaboration architecture.

---

## Phase 6: Design Handoff & Development Collaboration

**This is not a single moment — it's a continuous collaboration.**

### The Staggered Sprint Pipeline

UX work runs ahead of engineering:
- **Sprint N-2:** Research, problem validation, concept exploration
- **Sprint N-1:** Detailed design, prototyping, user testing
- **Sprint N:** Engineering builds Sprint N-1 designs while UX works on Sprint N+1

UX attends ALL sprint ceremonies: planning, standups, reviews, retros.

### Handoff Checklist

- [ ] Annotated high-fidelity mockups: behavior, states, edge cases, micro-interactions
- [ ] Interactive prototype demonstrating key flows
- [ ] Design specifications: spacing, typography, color, component states
- [ ] Design token documentation (primitive > semantic > component layers)
- [ ] Responsive breakpoints and behavior rules
- [ ] Accessibility requirements: ARIA labels, keyboard behavior, focus order
- [ ] QA checklist for visual fidelity verification
- [ ] Edge case catalog: what happens when [data is missing / network fails / input is invalid]?

**Target: >95% design-to-implementation accuracy on visual QA.**

### Ongoing Collaboration

- Engineers participate in design reviews early (not just at handoff)
- Designers review implemented features during sprints (design QA)
- Edge cases discovered during development trigger real-time design decisions
- Both reference the same design system tokens — no "pixel-pushing" from screenshots

> Deep dive: `references/design-handoff.md` — sprint integration patterns, design QA process, component documentation standards, responsive specification format.

---

## Phase 7: Post-Launch Optimization

**Goal:** Measure outcomes, iterate continuously, and drive sustainable growth.

**When to loop back:** When metrics stall, when new pain points surface in support tickets, or on a regular weekly cadence (continuous discovery).

### HEART Framework (UX Quality)

| Dimension | Measures | Example Metrics |
|-----------|---------|----------------|
| **H**appiness | Subjective satisfaction | CSAT, NPS, perceived ease |
| **E**ngagement | Depth/frequency of use | Session length, DAU/MAU, feature usage |
| **A**doption | New user/feature uptake | Signup rate, feature adoption % |
| **R**etention | Users returning over time | D7/D30 retention, churn rate |
| **T**ask Success | Behavioral efficiency | Completion rate, error rate, time-on-task |

### AARRR Pirate Metrics (Growth)

| Stage | Focus | Key Question |
|-------|-------|-------------|
| **A**cquisition | How users find you | Which channels drive quality users? |
| **A**ctivation | First "Aha!" moment | How fast do users experience core value? |
| **R**etention | Continued engagement | Do they come back after day 1? Day 7? Day 30? |
| **R**eferral | Users recommending you | Would they tell a friend? |
| **R**evenue | Financial sustainability | Does the unit economics work? |

**HEART measures experience quality. AARRR measures business health. You need both.**

### The Goals-Signals-Metrics Bridge

Don't track metrics in isolation. For every feature:

1. **Goal:** "New users should feel confident completing their first transaction"
2. **Signals of success:** Completes transaction, no support contact, returns within 7 days
3. **Signals of failure:** Abandons at confirmation, contacts support, uninstalls within 24 hours
4. **Metrics:** First-transaction completion rate >70%, support ticket rate <5%, D7 return >40%

### Optimization Checklist

- [ ] Define Goals > Signals > Metrics for each feature using HEART
- [ ] Track AARRR funnel to identify drop-off points
- [ ] Set up monitoring dashboards with automated anomaly alerts
- [ ] Run A/B tests on hypothesized improvements (minimum 2-week cycles)
- [ ] Conduct regular cohort analysis (acquisition, behavioral, feature cohorts)
- [ ] Maintain continuous discovery: weekly customer touchpoints
- [ ] Apply Product Kata: Direction > Current > Target > Experiment weekly
- [ ] Document learnings and feed back into next discovery cycle

> Deep dive: `references/metrics-optimization.md` — Goals-Signals-Metrics walkthrough, A/B testing methodology, cohort analysis, AI-driven optimization strategies.

---

## AI Integration Across Phases

AI is a co-pilot, not a replacement. It accelerates every phase when used with judgment:

| Phase | AI Role | What It Does Well | What It Does Poorly |
|-------|---------|------------------|-------------------|
| **1. Discover** | Research accelerator | Transcribe, cluster themes, social listening | Replacing actual user contact |
| **2. Define** | Synthesis partner | Pattern recognition, persona drafting, journey mapping | Making value judgments about priorities |
| **3. IA & Interaction** | Structure co-pilot | Generating variations, exploring edge cases, card sort analysis | Knowing what's actually feasible |
| **4. Prototype** | Production accelerator | Layout generation, component code, localization | Understanding cultural nuance deeply |
| **5. Validate** | Analysis engine | Auto-tagging findings, accessibility scanning, severity clustering | Judging subjective experience quality |
| **6. Handoff** | Documentation generator | Acceptance criteria, state docs, edge case catalogs, component cross-refs | Anticipating all engineering edge-case questions |
| **7. Optimize** | Monitoring agent | Anomaly detection, experiment proposals, cohort segmentation | Making business strategy decisions |

> Deep dive: `references/agentic-ai-design.md` — Plan-Act-Reflect pattern, multi-agent collaboration UX, observability design, the evolving role of UX as "Architect of Human-AI Collaboration."

---

## Autonomous Execution Protocol

When executing any phase of this workflow, follow this protocol to ensure self-sufficient, high-quality output.

### Step 1: Bootstrap Context

Before starting ANY phase work, self-load the required context. See `rules/skill-routing.md` → Context Bootstrap Protocol for exact file paths.

**Mandatory reads for every phase:**
- `rules/context-engineering.md` — Output format rules
- `rules/agent-coordination.md` — Agent invocation priority and data flow
- `rules/iteration-workflows.md` — Loop-back conditions and forward-only rules
- `rules/skill-routing.md` — Skill routing decisions and self-audit checklist

**Phase-specific reads:** Load the references, templates, and checklists listed in `rules/skill-routing.md` → Step 2 and Step 3 tables.

**Existing artifacts:** Glob `ux/` subdirectories and read `ux/phase-status.json` (if it exists) to understand what's already been produced.

### Step 2: Route to the Right Skill

All agents have access to the `Skill` tool, which can invoke **any installed skill** — not just the ones listed in the routing table. Use it:

```
Skill(skill: "jobs-to-be-done")        → JTBD analysis
Skill(skill: "accessibility")          → WCAG compliance
Skill(skill: "cro-methodology")        → Conversion optimization
Skill(skill: "speckit-full")           → Full spec-kit reasoning workflow
Skill(skill: "find-skills")            → Search 1000+ skills by keyword
```

**Routing priority:**
1. Match user intent to the Skill Routing Table in `rules/skill-routing.md`
2. If no match, search with `Skill(skill: "find-skills")` using keywords from the user's request
3. If still no match, use the phase-specific sub-skill (`ux-discover` through `ux-optimize`)

**Spec-Kit for planning**: When a phase requires structured reasoning, analysis, or specification — invoke `Skill(skill: "speckit-full")` for end-to-end spec workflow, or chain individual spec-kit commands (`speckit-analyze`, `speckit-plan`, `speckit-tasks`, `speckit-checklist`).

### Step 3: Execute with Evidence Tagging

Every claim in every artifact must be tagged:
- `[EVIDENCE: source]` — Backed by research data, analytics, or user quotes
- `[ASSUMPTION: reason]` — Explicitly flagged as unvalidated, with rationale
- `[MEASURED: tool]` — Quantified via MCP tool (AccessLint, Lighthouse, Playwright)
- `[CONTRADICTION]` — When new evidence conflicts with earlier findings

### Step 4: Self-Audit (Impeccable Standard)

After producing any deliverable, run the self-audit checklist in `rules/skill-routing.md` → Impeccable Standard Self-Audit. The five categories are:
1. **Content Quality** — Zero placeholders, evidence-tagged claims, consistent terminology
2. **Logical Completeness** — All 8 content states, all 5 interaction states, error paths, edge cases
3. **Accessibility Compliance** — WCAG 2.1 AA, contrast ratios, keyboard nav, ARIA labels
4. **Human-Centric Reasoning** — Traces to user needs, Ethical Design Hierarchy, Four-Risk Gate, cognitive load
5. **Deliverable Formatting** — Correct `ux/` subdirectory, progressive disclosure, stakeholder calibration

### Step 5: Check Phase Transition

After completing work, evaluate the current phase's Definition of Done checklist (`checklists/phase-N-*.md`). If met, recommend advancement. If a loop-back trigger fires (see `rules/iteration-workflows.md`), recommend the target phase with evidence. Update `ux/phase-status.json`.

### Data Self-Sufficiency

The agent must gather its own context rather than asking the user for information it can derive:
- **Codebase state** → Read files, glob directories, grep for patterns
- **Design system** → Query shadcn-ui MCP, read component files, check Storybook
- **Accessibility** → Run AccessLint MCP audits, Lighthouse via Chrome DevTools
- **Live prototypes** → Use Claude Preview or Playwright for screenshots, interaction testing
- **Library docs** → Use Context7 MCP for up-to-date API references
- **Existing artifacts** → Glob `ux/**/*.md` before creating duplicates

Only ask the user for information that cannot be derived from the codebase, MCP tools, or web search: business strategy decisions, stakeholder preferences, budget constraints, and timeline commitments.

---

## Quick Decision Guide

| User's situation | Start here | Key reference |
|-----------------|------------|---------------|
| "I'm starting a new product" | Phase 1: Discovery | `references/frameworks.md` |
| "I have research, need to make sense of it" | Phase 2: Define | `references/discovery-synthesis.md` |
| "I know the problem, need solution ideas" | Phase 3: Ideate | `references/ideation-prototyping.md` |
| "I'm building the interface" | Phase 4: Design | `references/laws-of-ux.md` |
| "I need to test my prototype" | Phase 5: Validate | `references/usability-testing.md` |
| "My product is live, needs improvement" | Phase 7: Optimize | `references/metrics-optimization.md` |
| "I need to prepare specs for engineers" | Phase 6: Handoff | `references/design-handoff.md` |
| "I'm designing for Arabic/MENA" | Phase 4 + RTL | `references/arabic-rtl-mena.md` |
| "I'm building AI-powered features" | Phase 5 + AI | `references/agentic-ai-design.md` |
| "I need to hand off to developers" | Phase 6: Handoff | `references/design-handoff.md` |
| "I need a competitive analysis" | Phase 1 | `references/competitive-analysis.md` |
| "I need to set up metrics" | Phase 7 | `references/metrics-optimization.md` |
| "I want to run a design sprint" | Phase 3 | `references/ideation-prototyping.md` |
| "Help me write a problem statement" | Phase 2 | See HMW Calibration table above |
| "How do I structure this app?" | Phase 3 | `references/ideation-prototyping.md` |
| "I need ethical design guidance" | Ethical Design Hierarchy | `references/agentic-ai-design.md` |
| "Help me assess product risks" | Four Product Risks | See framework above |
| "I need AI confidence indicators" | AI Behavioral Guidance | `references/agentic-ai-design.md` |

---

## Reference Files

| File | Contents | Read When |
|------|----------|-----------|
| `references/frameworks.md` | Double Diamond, Lean UX, Product Kata, Product Triad, Continuous Discovery, OST | Understanding the foundational methodology |
| `references/discovery-synthesis.md` | JTBD methodology, empathy mapping, 5W1H, CATWOE, cognitive prompting, bias mitigation | Doing research or synthesizing findings |
| `references/competitive-analysis.md` | Competitive analysis frameworks, UX teardowns, feature matrices, positioning | Analyzing the competitive landscape |
| `references/ideation-prototyping.md` | SCAMPER, Crazy 8s, card sorting, Design Sprint, prototyping fidelity, design tokens | Generating ideas or building prototypes |
| `references/laws-of-ux.md` | Fitts's, Hick's, Jakob's, Miller's, Peak-End, Gestalt principles, Nielsen's 10 | Designing interfaces or reviewing designs |
| `references/arabic-rtl-mena.md` | RTL mirroring rules, Egyptian fintech, InstaPay, trust patterns, BiDi, mobile-first | Building for Arabic-speaking markets |
| `references/usability-testing.md` | Testing methods, think-aloud, heuristic evaluation, WCAG POUR, reporting | Planning or analyzing usability tests |
| `references/metrics-optimization.md` | HEART, AARRR, Goals-Signals-Metrics, A/B testing, cohort analysis | Setting up metrics or optimizing post-launch |
| `references/agentic-ai-design.md` | Plan-Act-Reflect, Human-AI interaction, XAI, multi-agent UX | Designing AI-powered features |
| `references/design-handoff.md` | Sprint integration, design QA, component docs, responsive specs | Preparing for or managing developer handoff |
