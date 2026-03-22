---
name: ux-product-design-workflow
description: >
  Complete UX and Product Design workflow system integrating Double Diamond, Lean UX, Product Kata,
  JTBD, Laws of UX, HEART/AARRR metrics, ethical design hierarchy, four product risks, confidence
  scoring, and agentic AI design patterns. Guides teams through the full product lifecycle:
  Discovery, Define, Ideate, Design, Test, and Optimize with phase transition signals.

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
  │ DISCOVER      DEFINE         │     │ DEVELOP       DESIGN         │
  │ (Diverge)     (Converge)     │     │ (Diverge)     (Converge)     │
  │                              │     │                              │
  │ Understand    Synthesize     │     │ Explore       Build &        │
  │ users &       into focus     │     │ solutions     refine         │
  │ problem                      │     │ widely        the best       │
  └──────────────────────────────┘     └──────────────────────────────┘

                    Phase 5: VALIDATE              Phase 6: OPTIMIZE
                    Test with real users           Measure, learn, iterate
                    ────────────────────           ────────────────────
                    Usability testing              HEART + AARRR metrics
                    Heuristic evaluation           A/B experiments
                    Accessibility audit            Continuous discovery
                    Human-AI checks                Product Kata cycles
```

**Phase Transition Signals:** Each phase has a "Definition of Done" checklist. Don't advance until you've met the transition criteria — they're documented in each phase's reference file. Moving forward prematurely is the most common cause of product failure.

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
- [ ] Create empathy maps (Says, Thinks, Does, Feels) per segment
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
| Empathy maps | Capture user psychology | 4-quadrant canvas per segment |
| JTBD job map | Map the user's job chronologically | Step-by-step with service gaps |
| Competitive landscape | Position against alternatives | Feature matrix + UX teardown |
| Opportunity backlog | Prioritize unmet needs | Ranked list with evidence weight |

### Anti-Patterns

- **Confirmation tourism:** Interviewing only to validate what you already believe. Actively seek disconfirming evidence.
- **Persona theater:** Creating personas from demographics and guesses instead of behavioral research data.
- **Analysis paralysis:** Researching endlessly without converging. Set a timebox. 2-4 weeks is usually enough.
- **Skipping to solutions:** "I already know what to build" — the most expensive assumption in product development.

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
- [ ] Design all states: default, empty, loading, error, success, partial, offline, permission
- [ ] Create low-fidelity wireframes focused on layout, hierarchy, and flow
- [ ] Validate IA with tree testing (target >80% on primary paths)

### State Design — The Often-Forgotten States

Every screen has more than just the "happy path." Design these explicitly:

| State | What the user sees | Design question |
|-------|-------------------|----------------|
| **Empty** | No data yet | How do we explain and motivate first action? |
| **Loading** | Data being fetched | Skeleton, spinner, or progress bar? |
| **Partial** | Some data available | What loads first? What's deferred? |
| **Error** | Something broke | Can they retry? Is data preserved? |
| **Success** | Action completed | What's the next logical step? Delight moment? |
| **Offline** | No network | What's cached? What's queued? |
| **Permission** | Access needed | Why do we need this? What if they refuse? |

### Anti-Patterns

- **Premature convergence:** Falling in love with the first idea. Force yourself to generate alternatives.
- **IA by org chart:** Structuring navigation around internal departments instead of user mental models.
- **Wireframe theater:** Creating wireframes no one tests. Even 5 minutes of hallway testing beats zero.

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
| **Doherty Threshold** | <400ms response feels instant | Skeleton screens, optimistic UI, preloading |
| **Miller's Law** | Working memory holds ~7 items | Chunk form fields; group related info |
| **Peak-End Rule** | Memory = peak moment + final moment | Design delight at completion; never end on an error |
| **Zeigarnik Effect** | Incomplete tasks nag the mind | Progress bars; "3 of 5 steps complete" |
| **Aesthetic-Usability** | Beautiful = perceived as more usable | Polish builds trust, especially in fintech |

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
- [ ] Handle ALL states: default, hover, active, focus, disabled, error, loading, empty, success
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

## Design Handoff & Development Collaboration

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

## Phase 6: Post-Launch Optimization

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
| **Discover** | Research accelerator | Transcribe, cluster themes, social listening | Replacing actual user contact |
| **Define** | Synthesis partner | Pattern recognition, persona drafting, journey mapping | Making value judgments about priorities |
| **Ideate** | Brainstorming co-pilot | Generating variations, exploring edge cases | Knowing what's actually feasible |
| **Design** | Production accelerator | Layout generation, component code, localization | Understanding cultural nuance deeply |
| **Validate** | Analysis engine | Auto-tagging findings, accessibility scanning | Judging subjective experience quality |
| **Optimize** | Monitoring agent | Anomaly detection, experiment proposals | Making business strategy decisions |

> Deep dive: `references/agentic-ai-design.md` — Plan-Act-Reflect pattern, multi-agent collaboration UX, observability design, the evolving role of UX as "Architect of Human-AI Collaboration."

---

## Quick Decision Guide

| User's situation | Start here | Key reference |
|-----------------|------------|---------------|
| "I'm starting a new product" | Phase 1: Discovery | `references/frameworks.md` |
| "I have research, need to make sense of it" | Phase 2: Define | `references/discovery-synthesis.md` |
| "I know the problem, need solution ideas" | Phase 3: Ideate | `references/ideation-prototyping.md` |
| "I'm building the interface" | Phase 4: Design | `references/laws-of-ux.md` |
| "I need to test my prototype" | Phase 5: Validate | `references/usability-testing.md` |
| "My product is live, needs improvement" | Phase 6: Optimize | `references/metrics-optimization.md` |
| "I'm designing for Arabic/MENA" | Phase 4 + RTL | `references/arabic-rtl-mena.md` |
| "I'm building AI-powered features" | Phase 5 + AI | `references/agentic-ai-design.md` |
| "I need to hand off to developers" | Handoff section | `references/design-handoff.md` |
| "I need a competitive analysis" | Phase 1 | `references/competitive-analysis.md` |
| "I need to set up metrics" | Phase 6 | `references/metrics-optimization.md` |
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


# --- IMPORTED FROM CLAUDE.md ---

﻿# Skills Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-03-13

## Active Technologies
- File-based markdown in `ux/` directory tree, version-controlled alongside code (001-ux-design-agent)

- Markdown + Bash/PowerShell scripting (skill files, templates, automation scripts) + Claude Code skill system (SKILL.md format), Spec Kit workflow (.specify/), optional @anthropic-ai/claude-agent-sdk for MCP tool exposure (001-ux-design-agent)

## Project Structure

```text
src/
tests/
```

## Commands

# Add commands for Markdown + Bash/PowerShell scripting (skill files, templates, automation scripts)

## Code Style

Markdown + Bash/PowerShell scripting (skill files, templates, automation scripts): Follow standard conventions

## Recent Changes
- 001-ux-design-agent: Added Markdown + Bash/PowerShell scripting (skill files, templates, automation scripts) + Claude Code skill system (SKILL.md format), Spec Kit workflow (.specify/), optional @anthropic-ai/claude-agent-sdk for MCP tool exposure

- 001-ux-design-agent: Added Markdown + Bash/PowerShell scripting (skill files, templates, automation scripts) + Claude Code skill system (SKILL.md format), Spec Kit workflow (.specify/), optional @anthropic-ai/claude-agent-sdk for MCP tool exposure

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->


# --- IMPORTED FROM SPEC.MD ---

# Feature Specification: UX & Product Design Agent

**Feature Branch**: `001-ux-design-agent`
**Created**: 2026-03-13
**Status**: Draft
**Input**: User description: "Build an AI-powered UX & Product Design Agent that lives inside a Spec-Driven Development workflow, helping product teams move from problem discovery to post-launch optimization with opinionated, artifact-first guidance."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Guided Phase Navigation (Priority: P1)

A product team member (PM, designer, or founder) opens their editor, invokes the agent, and receives guidance on which UX phase they are in based on existing project artifacts. The agent identifies whether they are starting fresh, mid-research, designing, testing, or optimizing — and gives them the exact next step with a clear "Definition of Done" before the next phase.

**Why this priority**: This is the core value loop. Without phase awareness and guided progression, the agent is just a chatbot. Users must always know where they are and what's next — this is the #1 JTBD ("I want a guided UX workflow so I don't miss critical steps").

**Independent Test**: Invoke the agent on a project with no UX artifacts. The agent correctly identifies Phase 1 (Discovery), provides a research plan template, and lists the Definition of Done criteria. Invoke on a project with completed personas and journey maps — agent correctly identifies Phase 3 (Ideation & IA) and provides appropriate next steps.

**Acceptance Scenarios**:

1. **Given** a project with no UX artifacts in the repo, **When** the user invokes the agent, **Then** the agent identifies Phase 1 (Discovery) and produces a structured research plan with timeline, methods, and participant criteria.
2. **Given** a project with completed personas, journey maps, and problem statements, **When** the user invokes the agent, **Then** the agent identifies Phase 3 (Ideation & IA) and recommends ideation methods appropriate to the problem scope.
3. **Given** the user is in Phase 2 (Define) and has not completed the journey map, **When** the user asks to advance to Phase 3, **Then** the agent warns that the Definition of Done for Phase 2 is incomplete and lists the missing artifacts.

---

### User Story 2 - Artifact Generation from Research Input (Priority: P2)

A user has raw research data (interview notes, survey results, support tickets, analytics observations) and asks the agent to synthesize it into standard UX artifacts: personas, journey maps, empathy maps, problem statements, and HMW statements. The agent produces structured, evidence-grounded deliverables — not generic templates.

**Why this priority**: This is the second-highest JTBD ("I want help turning research into personas, journey maps, and problem statements"). Raw research is where most teams stall — they collect data but don't synthesize it into actionable artifacts. This is high-leverage acceleration.

**Independent Test**: Provide the agent with 3-5 interview transcript excerpts. The agent produces at least one persona with demographics, behaviors, goals, pain points, JTBD statement, and a representative quote — all grounded in the provided data, not fabricated.

**Acceptance Scenarios**:

1. **Given** the user provides 3 interview transcript excerpts, **When** they ask the agent to generate personas, **Then** the agent produces 2-4 personas with all required fields (name, demographics, behaviors, goals, pain points, JTBD, quote) and cites which transcript evidence supports each attribute.
2. **Given** the user provides a list of observed pain points, **When** they ask for problem statements, **Then** the agent produces statements in the format "[User] needs a way to [need] because [insight]" with each insight traceable to provided evidence.
3. **Given** the user provides partial research (e.g., only survey data, no interviews), **When** they request a journey map, **Then** the agent produces a best-effort journey map clearly marking which stages are evidence-backed and which are assumptions requiring validation.

---

### User Story 3 - IA, Flows & Interaction Design Guidance (Priority: P3)

A user has defined the problem and needs help structuring their product's information architecture, user flows, and interaction patterns. The agent generates structured IA recommendations, annotated flow descriptions, and state-by-state interaction specs that engineering can build from with minimal ambiguity.

**Why this priority**: This bridges the gap between problem understanding and buildable design — the JTBD of "structured guidance on IA, interaction patterns, and states so engineering can build with minimal back-and-forth." Critical for reducing rework.

**Independent Test**: Describe a feature (e.g., "user onboarding for a fintech app") and the agent produces a sitemap recommendation, a primary user flow with decision points, and a screen-by-screen state inventory (default, empty, loading, error, success, offline, permission).

**Acceptance Scenarios**:

1. **Given** a defined problem statement and target persona, **When** the user asks for IA recommendations, **Then** the agent produces a sitemap structure organized by user mental model (not org chart), with navigation hierarchy and recommended card-sorting validation approach.
2. **Given** a core user task (e.g., "complete first transaction"), **When** the user asks for a user flow, **Then** the agent produces an annotated step-by-step flow including decision points, error paths, and edge cases.
3. **Given** a screen description, **When** the user asks for interaction specs, **Then** the agent describes all 7+ states (default, empty, loading, partial, error, success, offline, permission) with specific behavioral notes for each.

---

### User Story 4 - Post-Launch Metrics & Optimization Framework (Priority: P4)

A user has a live product and wants to set up a measurement framework and optimization loop. The agent helps define Goals-Signals-Metrics using HEART and AARRR frameworks, suggests experiment hypotheses, and structures a Product Kata cycle for continuous improvement.

**Why this priority**: This completes the lifecycle loop — the JTBD of "a clear framework for metrics, experiments, and iteration." Without this, teams ship and forget. Lower priority than Phases 1-3 because it requires a live product.

**Independent Test**: Describe a live feature and the agent produces a Goals-Signals-Metrics table with at least 3 HEART dimensions, an AARRR funnel analysis with identified drop-off hypotheses, and a Product Kata cycle plan for the next 4 weeks.

**Acceptance Scenarios**:

1. **Given** a live feature description and basic usage data, **When** the user asks for a metrics framework, **Then** the agent produces a Goals-Signals-Metrics table covering all 5 HEART dimensions with specific, measurable metrics tied to the feature.
2. **Given** a described funnel with known drop-off points, **When** the user asks for optimization recommendations, **Then** the agent produces 2-3 experiment hypotheses in the format "We believe [change] will [outcome] because [evidence/rationale]" with suggested success criteria.
3. **Given** a request for a Product Kata plan, **When** the agent generates the plan, **Then** it includes Direction (north-star metric), Current State (baseline), Target Condition (4-week goal), and 2-3 specific experiments to run.

---

### User Story 5 - Context-Adaptive Output Depth (Priority: P5)

The agent adapts its output rigor based on the user's context: lean/scrappy for solo founders and MVPs, rigorous/compliant for enterprise and regulated environments. The user can explicitly set their context or the agent infers it from project signals.

**Why this priority**: Core differentiator that prevents the agent from being either too heavy for startups or too light for enterprises. Important but depends on the core functionality (US1-4) working first.

**Independent Test**: Ask the same question ("generate a research plan") in MVP mode and Enterprise mode. MVP output is 1-2 pages with 3-5 interview targets. Enterprise output includes compliance considerations, larger sample sizes, IRB-style participant protections, and audit trail references.

**Acceptance Scenarios**:

1. **Given** the user sets context to "MVP / early-stage," **When** they request any artifact, **Then** the agent produces a lean version focused on speed (fewer participants, shorter timelines, essential fields only) with a note on what to expand later.
2. **Given** the user sets context to "Enterprise / regulated," **When** they request a research plan, **Then** the agent includes compliance checkpoints, larger sample sizes, data handling protocols, and references to relevant standards (WCAG, GDPR, accessibility mandates).
3. **Given** no explicit context is set, **When** the user invokes the agent on a project with a `package.json` listing 2 dependencies, **Then** the agent defaults to MVP mode. On a project with CI/CD configs, design system tokens, and compliance docs, it defaults to Enterprise mode.

---

### User Story 6 - Usability Validation & Heuristic Evaluation (Priority: P3)

A user has a design (described screens, prototypes, or live product) and wants expert-level validation before investing in engineering. The agent produces structured heuristic evaluations using Nielsen's heuristics and the project's Laws of UX, generates usability test plans with task scenarios and success metrics, and provides severity-rated findings with actionable remediation.

**Why this priority**: Validation prevents costly rework. Most teams skip formal heuristic evaluation because it requires UX expertise — the agent democratizes this by providing structured, methodology-backed evaluation that any team member can execute.

**Independent Test**: Describe 3 screens of a checkout flow. The agent produces a heuristic evaluation covering all 10 Nielsen heuristics, identifies at least 5 usability issues with severity ratings (critical/major/minor/cosmetic), and generates a test plan with 5+ task scenarios, participant criteria, and measurable success metrics.

**Acceptance Scenarios**:

1. **Given** a described screen or flow, **When** the user requests a heuristic evaluation, **Then** the agent evaluates against all 10 Nielsen heuristics, rates each finding by severity (0-4 scale), and provides specific remediation recommendations citing applicable Laws of UX.
2. **Given** a feature ready for testing, **When** the user requests a test plan, **Then** the agent produces a plan with: research objectives, methodology (moderated/unmoderated, remote/in-person), 5+ task scenarios with expected paths, success metrics (task completion rate, time-on-task, error rate, SUS score target), participant criteria (segment, screening questions, sample size with statistical justification), and a timeline.
3. **Given** test results (task completion rates, error observations, user quotes), **When** the user provides them to the agent, **Then** the agent produces a findings report with severity-ranked issues, pattern analysis across participants, and prioritized recommendations using an impact-effort matrix.

---

### User Story 7 - Design-to-Engineering Handoff (Priority: P3)

A designer or PM has finalized a design and needs to create comprehensive handoff documentation that engineering can build from without ambiguity. The agent generates annotated specs, edge-case catalogs, state documentation, accessibility requirements, responsive behavior rules, and acceptance criteria that map directly to testable engineering tasks.

**Why this priority**: Handoff quality directly determines rework. Incomplete handoffs cause 30-50% of design-engineering friction. The agent ensures nothing is missed by systematically covering all interaction states, edge cases, and accessibility requirements.

**Independent Test**: Describe a form with 5 fields and a submit button. The agent produces handoff documentation covering: all 7+ interaction states per field, validation rules, error messages, keyboard navigation path, screen reader announcements, responsive breakpoint behavior, and acceptance criteria for each state.

**Acceptance Scenarios**:

1. **Given** a screen description, **When** the user requests handoff documentation, **Then** the agent produces: annotated specs (component-by-component behavior), state catalog (all 7+ states per interactive element), accessibility requirements (WCAG 2.1 AA: focus order, ARIA labels, color contrast ratios, keyboard paths), and responsive behavior (breakpoint-specific layout changes).
2. **Given** a user flow, **When** the user requests an edge-case catalog, **Then** the agent systematically identifies edge cases across categories: data edge cases (empty, null, overflow, special characters), timing edge cases (race conditions, timeouts, concurrent actions), permission edge cases (revoked access mid-flow, expired sessions), and connectivity edge cases (offline, slow network, interrupted uploads).
3. **Given** handoff documentation, **When** the user requests acceptance criteria, **Then** the agent produces testable Given/When/Then scenarios for each interaction state and edge case, formatted for direct import into issue trackers.

---

### User Story 8 - Spec Kit Lifecycle Integration (Priority: P4)

A team using the Spec Kit workflow (`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`) wants UX artifacts to feed directly into their development pipeline. The agent detects existing spec artifacts and cross-references them, ensuring UX outputs align with and enrich the specification, planning, and task generation phases.

**Why this priority**: Integration with existing workflows prevents UX from being siloed. Teams already using Spec Kit should get UX guidance that flows naturally into their development process without manual translation.

**Independent Test**: In a project with a `specs/` directory containing a feature spec, invoke `/ux.define`. The agent detects the existing spec, cross-references user scenarios, and produces personas and problem statements that align with the spec's stated user needs. The output includes a mapping table showing which UX artifacts support which spec requirements.

**Acceptance Scenarios**:

1. **Given** a project with `specs/[feature]/spec.md`, **When** the user invokes `/ux.discover` or `/ux.define`, **Then** the agent reads existing spec artifacts and cross-references user scenarios, requirements, and success criteria when generating UX artifacts.
2. **Given** completed IA and flow artifacts from `/ux.ia`, **When** the user runs `/speckit.plan`, **Then** the UX artifacts are available as technical context inputs and the plan references IA constraints and flow requirements.
3. **Given** a request to generate tasks via `/speckit.tasks`, **When** UX phases have been completed, **Then** the agent contributes UX-specific tasks (research, design, testing, handoff) tagged with `[UX]` alongside engineering tasks, with dependencies correctly mapped.

---

### Edge Cases

- **Contradictory research data**: When interviews say users want X but analytics show they avoid X, the agent MUST surface the contradiction explicitly with a structured comparison table, recommend resolution methods (segmented analysis by user type, A/B test, additional contextual inquiry), and tag the conflicting data points with `[CONTRADICTION: source1 vs source2]`.
- **Phase skipping**: When the user tries to skip from Phase 1 to Phase 5, the agent warns about skipped phases with specific risks (e.g., "Skipping Define means personas are unvalidated — test results may not represent actual users"), but allows override. Override requires the user to provide a documented justification that is recorded in `phase-status.json` with a `skipped_phases` array and `skip_justification` per entry.
- **No research data**: When no research exists and the user asks for personas, the agent generates "proto-personas" with every field explicitly marked `[ASSUMPTION: no research data]` and includes a validation plan (3-5 lightweight guerrilla interviews) to convert assumptions to evidence. Proto-personas use a distinct template header: `confidence: hypothesis`.
- **Production code requests**: The agent declines with a specific response: explains its scope (UX guidance and artifact generation), identifies what type of engineering artifact would serve the need (component spec, API contract, state machine definition), and generates a structured handoff document the user can give to engineering.
- **Multi-persona conflicts**: When different personas have conflicting needs for the same feature, the agent produces a persona priority matrix showing which persona is primary for this feature, documents the tradeoff explicitly, and recommends progressive disclosure or segmented experiences where both needs can coexist.
- **RTL/Bidirectional content**: When the user's project targets Arabic, Hebrew, or other RTL languages (detected via locale files, i18n configs, or explicit user statement), the agent automatically applies MENA-specific patterns: mirrored layouts, bidirectional text handling, culturally appropriate iconography, and right-to-left reading flow in all IA and flow artifacts.
- **Regulated industry detection**: When the project contains HIPAA, PCI-DSS, SOC 2, or GDPR compliance markers (detected via config files, documentation, or domain keywords like "healthcare," "payments," "financial"), the agent automatically escalates to Enterprise mode and includes compliance-specific checklists in all phase outputs.
- **Large-scale IA (50+ screens)**: When the sitemap exceeds 50 nodes, the agent automatically segments into navigation zones (primary, secondary, utility, footer), recommends a hub-and-spoke or flat hierarchy based on user mental models, and suggests tree-testing validation before implementation.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Agent MUST identify the user's current UX phase based on existing project artifacts (files, directories, document content) and provide phase-appropriate guidance.
- **FR-002**: Agent MUST generate structured UX artifacts (personas, journey maps, empathy maps, problem statements, HMW statements) from user-provided research inputs.
- **FR-003**: Agent MUST produce all artifacts in consistent, structured markdown formats matching the default output formats defined in the project constitution.
- **FR-004**: Agent MUST enforce phase progression by checking "Definition of Done" criteria before recommending advancement to the next phase.
- **FR-005**: Agent MUST explicitly distinguish between evidence-backed content and assumptions in all generated artifacts.
- **FR-006**: Agent MUST generate IA recommendations, user flow descriptions, and interaction state inventories (all 7+ states) for design guidance requests.
- **FR-007**: Agent MUST produce Goals-Signals-Metrics tables, experiment hypotheses, and Product Kata plans for post-launch optimization requests.
- **FR-008**: Agent MUST adapt output depth based on user context (MVP vs. Enterprise) either through explicit user setting or project-signal inference.
- **FR-009**: Agent MUST apply the Four-Risk Gate (value, usability, feasibility, viability) as a checkpoint before advancing initiatives past discovery.
- **FR-010**: Agent MUST refuse to generate production backend code and instead provide structured UX guidance and handoff documentation.
- **FR-011**: Agent MUST apply Laws of UX (Fitts's, Hick's, Jakob's, Miller's, Doherty Threshold, Peak-End Rule, Zeigarnik Effect, Aesthetic-Usability) when generating interaction design recommendations.
- **FR-012**: Agent MUST provide accessibility guidance aligned with WCAG 2.1 AA standards in all design-phase outputs.
- **FR-013**: Agent MUST support all 7 phases: Discovery, Problem Framing, IA & Interaction Design, Ideation & Prototyping, Evaluative Research/Validation, Design-to-Engineering Handoff, Post-Launch Optimization. Note: The master SKILL.md Phase Map diagram shows 6 phases (Handoff is treated as a transition between Validate and Optimize). The spec explicitly numbers Handoff as Phase 6 because it generates distinct artifacts requiring a dedicated contract and DoD checklist.
- **FR-014**: Agent MUST generate usability test plans with objectives, methodology, task scenarios, metrics, participant criteria, and schedule when requested.
- **FR-015**: Agent MUST produce design handoff documentation including annotated specs, state catalogs, accessibility requirements, and responsive behavior rules.
- **FR-016**: Agent MUST generate Jobs-to-Be-Done statements in the format "When [situation], I want to [motivation], so I can [expected outcome]" grounded in user research or explicitly marked as assumptions.
- **FR-017**: Agent MUST produce competitive analysis frameworks with structured comparison matrices covering: feature parity, UX patterns used, onboarding flows, pricing models, and identified gaps/opportunities.
- **FR-018**: Agent MUST generate Opportunity Solution Trees connecting target outcomes to opportunities (user needs/pain points) to solutions (feature ideas) to experiments (validation methods), maintaining traceability from research to implementation.
- **FR-019**: Agent MUST cross-reference artifacts across phases — later-phase outputs MUST cite earlier-phase artifacts (e.g., user flows reference personas by name, test plans reference journey map pain points, handoff docs reference state inventories).
- **FR-020**: Agent MUST apply RTL/Arabic/MENA design patterns when the project targets bidirectional or right-to-left languages, including mirrored layouts, culturally appropriate iconography, and bidirectional text handling rules.
- **FR-021**: Agent MUST integrate with Spec Kit lifecycle phases by reading existing spec artifacts from `specs/` directory and contributing UX-specific content to specification, planning, and task generation workflows.
- **FR-022**: Agent MUST generate severity-rated heuristic evaluation findings using Nielsen's 10 heuristics with a 0-4 severity scale (0=not a problem, 1=cosmetic, 2=minor, 3=major, 4=catastrophic) and provide specific remediation recommendations for each finding.
- **FR-023**: Agent MUST produce empathy maps with six quadrants (Says, Thinks, Does, Feels, Sees, Hears) derived from research data, with each entry traceable to a specific research source or explicitly marked as an inference. The Sees and Hears quadrants capture environmental context (competitor exposure, peer influence, media messages) per the discovery-synthesis reference.

### Key Entities

- **Phase**: Represents one of the 7 workflow stages. Attributes: name, sequence number, Definition of Done criteria, applicable artifact types, transition signals.
- **Artifact**: A UX deliverable generated by the agent. Attributes: type (persona, journey map, problem statement, etc.), phase association, evidence sources, confidence level (evidence-backed vs. assumption), context depth (MVP vs. Enterprise).
- **User Context**: The user's environment and needs profile. Attributes: team size indicator (solo/small/mid/enterprise), domain constraints (fintech, SaaS, healthcare, etc.), existing artifacts inventory, current phase.
- **Risk Assessment**: A Four-Risk Gate evaluation for an initiative. Attributes: value risk status, usability risk status, feasibility risk status, viability risk status, overall gate status (pass/fail/incomplete).
- **Evidence Tag**: An inline annotation classifying the confidence level of a claim. Types: `[EVIDENCE: source]` (backed by specific research), `[ASSUMPTION: reason]` (hypothesis requiring validation), `[MEASURED: metric, source]` (quantified observation from analytics), `[CONTRADICTION: source1 vs source2]` (conflicting data requiring resolution).
- **Heuristic Finding**: A usability issue identified during evaluation. Attributes: heuristic violated (Nielsen 1-10), severity (0-4), location (screen/component), description, evidence, remediation recommendation, applicable Law of UX.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A new user can produce their first valuable artifact (persona, problem statement, or research plan) within 15 minutes of first invocation.
- **SC-002**: Users can correctly identify which phase they are in and what "done" means for that phase in 100% of agent interactions where phase guidance is requested.
- **SC-003**: 80% or more of generated artifacts pass the project's own quality checklists (e.g., personas include all required fields, journey maps cover all stages, problem statements follow the "[User] needs [need] because [insight]" format).
- **SC-004**: Teams using the agent produce at least 3 of the 5 core artifact types (personas, journey maps, problem statements, test plans, metrics frameworks) per product initiative, compared to a baseline of teams not using the agent.
- **SC-005**: Design-to-engineering handoff documents reduce clarification questions by 50% compared to unstructured handoff (measured by follow-up questions per feature).
- **SC-006**: The agent correctly applies context-adaptive depth: MVP-context outputs are under 2 pages for single artifacts; Enterprise-context outputs include compliance and audit references.
- **SC-007**: For teams that instrument post-launch metrics using the agent's framework, activation rate improves by at least 10% and task success rate improves by at least 15% for features designed using the agent versus baseline.

- **SC-008**: Cross-phase artifact referencing is present in 100% of Phase 3+ outputs — every user flow references a persona, every test plan references journey map pain points, every handoff doc references state inventories.
- **SC-009**: Heuristic evaluations cover all 10 Nielsen heuristics with severity ratings, and 90%+ of findings include specific, actionable remediation recommendations (not generic advice).
- **SC-010**: Edge-case catalogs generated during handoff cover at least 4 categories (data, timing, permission, connectivity) with a minimum of 3 scenarios per category for complex features.

### Assumptions

- Users interact with the agent through a code editor or terminal environment where markdown output is rendered or easily readable.
- Users are willing to provide raw research inputs (interview notes, survey data, analytics observations) for the agent to synthesize — the agent does not conduct research autonomously.
- The 7-phase workflow is the right macro structure for the target audience; teams may compress phases but should not skip them entirely.
- JTBD, Double Diamond, and Lean UX are widely accepted frameworks among the target user base and do not require extensive justification.
- The agent operates as a skill/prompt system within an AI coding assistant, not as a standalone application with its own UI.
- Teams using Spec Kit have existing `specs/` and `.specify/` directories that the agent can read for cross-referencing.
- Users understand that proto-personas and assumption-tagged outputs require validation and are not substitutes for actual user research.

---

## Appendix A: Definition of Done per Phase

### Phase 1 — Discovery & Research
- [ ] Stakeholder alignment on business objectives documented
- [ ] Research plan with methodology, participants, and timeline
- [ ] JTBD statements (minimum 3) in canonical format
- [ ] Competitive analysis of 3-5 competitors with UX teardown
- [ ] Empathy maps with evidence-tagged entries
- [ ] Opportunity backlog prioritized by impact
- [ ] Four-Risk Gate initial assessment (all 4 risks have a status)
- [ ] All assumptions explicitly tagged `[ASSUMPTION]`
- [ ] Context mode set (MVP/Growth/Enterprise)

### Phase 2 — Define & Problem Framing
- [ ] 2-4 personas with all required fields, evidence-tagged
- [ ] Journey maps for primary personas (minimum 1 per persona)
- [ ] Problem statements in "[User] needs [need] because [insight]" format
- [ ] HMW statements calibrated (not too broad, not too narrow)
- [ ] Opportunity Solution Tree linking outcomes to opportunities to solutions
- [ ] All personas reference JTBD from Phase 1
- [ ] Contradictory evidence surfaced and resolution recommended

### Phase 3 — IA & Interaction Design
- [ ] Sitemap organized by user mental model (not org chart)
- [ ] User flows for core scenarios with error paths and edge cases
- [ ] State inventories for all primary screens (all 7+ states)
- [ ] Wireframe descriptions with behavioral annotations
- [ ] Navigation taxonomy with Hick's Law validation (<=7 items per level)
- [ ] All flows reference personas by name
- [ ] Card sorting validation approach recommended

### Phase 4 — Prototyping & Interaction Design
- [ ] Laws of UX applied as concrete design actions (not abstract mentions)
- [ ] Design system token mapping (primitive > semantic > component)
- [ ] Micro-interaction specs with timing, easing, and purpose
- [ ] Responsive behavior rules per breakpoint
- [ ] RTL/MENA patterns applied (if applicable)
- [ ] Nielsen's 10 heuristic self-check completed
- [ ] Ethical Design Hierarchy check (safety > function > delight)

### Phase 5 — Validation & Usability Testing
- [ ] Usability test plan with JTBD-based task scenarios
- [ ] Heuristic evaluation covering all 10 Nielsen heuristics
- [ ] Severity ratings for all findings (0-4 scale)
- [ ] Accessibility audit (WCAG 2.1 AA, POUR framework)
- [ ] Human-AI interaction checks (if applicable)
- [ ] Test plan references journey map pain points
- [ ] Participant criteria match persona segments
- [ ] Sample size justified (minimum 5 per segment)

### Phase 6 — Design-to-Engineering Handoff
- [ ] Annotated specifications (component-by-component behavior)
- [ ] State catalog covering all 7+ states per interactive element
- [ ] Edge-case catalog with 4 categories (data, timing, permission, connectivity)
- [ ] Accessibility requirements (ARIA, keyboard, focus, contrast, screen reader)
- [ ] Responsive behavior rules with touch targets
- [ ] Acceptance criteria in Given/When/Then format
- [ ] Error messages follow guidelines (friendly, actionable, no jargon)
- [ ] Empty states include education, CTA, and motivation
- [ ] All handoff docs reference state inventories from Phase 3

### Phase 7 — Post-Launch Optimization
- [ ] HEART framework with Goals, Signals, Metrics for all applicable dimensions
- [ ] AARRR funnel analysis with drop-off hypotheses
- [ ] Goals-Signals-Metrics consolidated table
- [ ] Experiment backlog with hypotheses, success criteria, and guardrail metrics
- [ ] Product Kata plan (Direction, Current State, Target Condition, Experiments)
- [ ] Metrics are user-facing outcomes (not system internals)
- [ ] Experiment duration >= 2 weeks

---

## Appendix B: Cross-Phase Referencing Matrix (FR-019)

Every artifact generated in Phase 3 or later MUST cite earlier-phase artifacts. This matrix specifies the mandatory references:

| Generated In | Artifact | MUST Reference | From Phase |
|-------------|----------|----------------|------------|
| Phase 2 | Persona | JTBD statements, research plan findings | Phase 1 |
| Phase 2 | Journey map | Competitive analysis gaps, empathy maps | Phase 1 |
| Phase 3 | User flow | Persona (by name), journey map pain points | Phase 2 |
| Phase 3 | Sitemap | Problem statements (navigation justification) | Phase 2 |
| Phase 4 | UX audit | State inventories, user flow decision points | Phase 3 |
| Phase 4 | Responsive rules | Persona device preferences | Phase 2 |
| Phase 5 | Test plan | Journey map pain points, persona segments | Phase 2 |
| Phase 5 | Heuristic eval | State inventories, Laws of UX application | Phase 3, 4 |
| Phase 6 | Handoff docs | State inventories, heuristic findings | Phase 3, 5 |
| Phase 6 | Acceptance criteria | Test plan scenarios | Phase 5 |
| Phase 7 | HEART goals | Problem statements | Phase 2 |
| Phase 7 | Experiments | Heuristic findings, test plan results | Phase 5 |

---

## Appendix C: Error Message & Empty State Guidelines

### Error Message Framework

All error messages generated in handoff documentation follow:

**Structure**: `[What happened]` + `[Why it matters to the user]` + `[What to do next]`

**Tone Rules**:
- Never blame the user ("You entered invalid data" -> "That format didn't work")
- Never use technical jargon ("Error 500" -> "Something went wrong on our end")
- Always provide a next step ("Try again" or "Contact support" or auto-retry)
- Use the user's vocabulary (match persona language register)

### Empty State Framework

All empty states in handoff documentation specify:

| Element | Purpose | Example |
|---------|---------|---------|
| Illustration/icon | Visual context | Relevant, not generic placeholder |
| Headline | What this area is for | "Your transactions will appear here" |
| Description | Why it's valuable | "Track spending, spot patterns, stay on budget" |
| Primary CTA | First action | "Make your first transfer" |
| Secondary info | Reduce anxiety | "It takes less than 2 minutes"  |

---

## Appendix D: Product Triad & Cross-Functional Collaboration

### The Product Triad in Practice

Every phase operates through the Product Triad (PM + Design + Engineering). The agent MUST recommend Triad-appropriate activities per phase:

| Phase | Product Manager | UX Designer | Engineering Lead |
|-------|----------------|-------------|-----------------|
| Discovery | Defines desired outcome, business constraints | Conducts user research, synthesizes insights | Assesses technical landscape, feasibility |
| Define | Prioritizes opportunities against business value | Creates personas, journey maps, problem statements | Identifies technical risks and dependencies |
| IA & Interaction | Evaluates ideas against business viability | Generates concepts, facilitates workshops | Provides feasibility feedback on solutions |
| Prototyping | Reviews prototypes against business goals | Builds and tests prototypes with users | Advises on implementation approach |
| Validation | Aligns test objectives with success criteria | Plans and conducts usability testing | Provides technical test support |
| Handoff | Manages sprint backlog and priorities | Delivers annotated designs and specs | Implements with design QA |
| Optimize | Prioritizes experiments by business impact | Designs experiments, analyzes user behavior | Implements experiments, manages feature flags |

### Stakeholder Communication Cadence

| Frequency | Activity | Participants |
|-----------|----------|-------------|
| Weekly | Product triad sync + customer interview | PM, Design, Engineering |
| Bi-weekly | Sprint review with broader stakeholders | Triad + stakeholders |
| Monthly | Product review with leadership (metrics, learnings, roadmap) | Triad + leadership |
| Quarterly | Strategic review (opportunity landscape, OKR alignment) | Full organization |

### Continuous Discovery Operating Rhythm

Rather than treating research as a project kickoff activity, the agent MUST encourage continuous discovery:
- **Weekly customer touchpoints** by the team building the product
- **Small research activities** in pursuit of a desired product outcome
- Interviews focused on understanding the **opportunity space** (needs, pain points, desires)
- Use of the **Opportunity Solution Tree** to visually map outcomes → opportunities → solutions → experiments

---

## Appendix E: AI as Design Partner

The agent itself is an AI design partner. When recommending AI integration in the user's product, apply this matrix:

| Phase | AI Can Do | Human Must Do |
|-------|----------|---------------|
| Discovery | Transcribe interviews, synthesize themes, generate research questions, create screening criteria | Design research methodology, conduct interviews, interpret nuance |
| Define | Generate personas from data, create journey maps, draft problem statements | Validate with real users, prioritize by judgment |
| IA & Interaction | Generate sitemaps, suggest navigation structures, wireframe from text | Test with real users, refine based on mental models |
| Prototyping | Generate layouts, draft microcopy, explore visual directions | Curate, critique, select best directions |
| Validation | Auto-transcribe sessions, tag pain points, evaluate against heuristics | Observe behavior, ask follow-ups, interpret meaning |
| Handoff | Generate annotations, component specs, design-to-code translation | Review, validate, handle edge cases |
| Optimize | Monitor analytics, surface anomalies, categorize feedback, generate reports | Interpret context, prioritize actions, make strategic decisions |

**Principle**: AI eliminates drudgery; humans provide empathy, creativity, and strategic thinking.

---

## Appendix F: Key Benchmarks & Rules of Thumb

| Benchmark | Value | Source |
|-----------|-------|--------|
| LTV:CAC ratio | 3:1 minimum (below 1:1 = destroying value) | Industry standard |
| Optimization vs. new features | 80% optimization, 20% new features | Pareto principle for mature products |
| Usability test participants | 5 per segment finds ~85% of issues | Nielsen's research |
| Heuristic evaluators | 3-5 evaluators catch ~75% of usability issues | Nielsen/Molich |
| Touch target minimum | 44x44px (iOS) / 48x48dp (Android) | Apple HIG / Material Design |
| Color contrast minimum | 4.5:1 normal text, 3:1 large text | WCAG 2.1 AA |
| Doherty Threshold | <400ms for perceived responsiveness | IBM research |
| SUS score target | ≥68 (above average) | Bangor et al. |
| Task completion rate target | >80% for primary flows | Industry benchmark |
| Card sorting participants | 15-30 per study | Optimal Workshop |


# --- IMPORTED FROM PLAN.MD ---

# Implementation Plan: UX & Product Design Agent

**Branch**: `001-ux-design-agent` | **Date**: 2026-03-13 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-ux-design-agent/spec.md`

## Summary

Build an AI-powered UX & Product Design Agent implemented as a set of Spec Kit-integrated skill files and slash commands. The agent guides product teams through a 7-phase UX workflow (Discovery through Post-Launch Optimization), generating concrete artifacts (personas, journey maps, IA, test plans, metrics frameworks) from user input and repository context. It enforces phase progression with Definition of Done gates, applies the Ethical Design Hierarchy and Four-Risk Gate, and adapts output depth to team context (MVP vs Enterprise).

The implementation uses markdown-based skill files with reference documents, slash commands per phase, and a structured `ux/` directory for persisted artifacts — no custom backend, no standalone application.

## Technical Context

**Language/Version**: Markdown + Bash/PowerShell scripting (skill files, templates, automation scripts)
**Primary Dependencies**: Claude Code skill system (SKILL.md format), Spec Kit workflow (.specify/), optional @anthropic-ai/claude-agent-sdk for MCP tool exposure
**Storage**: File-based markdown in `ux/` directory tree, version-controlled alongside code
**Testing**: Manual validation via Definition of Done checklists per phase; automated checklist validation via PowerShell scripts
**Target Platform**: Claude Code (primary), any agentic IDE supporting SKILL.md conventions (Gemini CLI, Windsurf, Cursor)
**Project Type**: AI agent skill system (collection of prompt-based skills + reference docs + templates + automation)
**Performance Goals**: First valuable artifact (persona, problem statement, or research plan) in <15 minutes from first invocation
**Constraints**: No production backend code generation; all outputs are markdown/JSON artifacts; no autonomous research execution
**Scale/Scope**: 7 phase-specific skills, 10 reference documents, 24 templates, 7 DoD checklists, 1 master SKILL.md orchestrator, 21 artifact types

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Ethical Design Hierarchy | PASS | Agent enforces safety > function > delight in all recommendations. FR-009 requires Four-Risk Gate. FR-012 requires WCAG 2.1 AA. |
| II. Four-Risk Gate | PASS | FR-009 explicitly requires value/usability/feasibility/viability checks before advancing past discovery. Each phase skill includes risk checkpoint. |
| III. Product Triad Collaboration | PASS | Artifacts designed for shared consumption by PM, Design, and Engineering. Handoff phase (Phase 6) explicitly bridges Design-Engineering. |
| IV. UX Quality & Interaction Standards | PASS | FR-011 requires Laws of UX application. FR-006 requires all 7+ interaction states. FR-012 requires WCAG 2.1 AA. |
| V. Evidence Over Assumption | PASS | FR-005 requires explicit evidence vs assumption tagging. Edge case handles contradictory data. Proto-personas labeled as hypotheses. |
| VI. AI as Co-Pilot | PASS | FR-010 refuses production code generation. Agent generates artifacts for human review, not autonomous decisions. Guardrails require clarifying questions over hallucination. |
| Workflow Frameworks | PASS | FR-013 implements all 7 phases (Double Diamond macro + Lean UX loops). FR-007 implements Product Kata for post-launch. JTBD is the core mental model throughout. |
| Operating Rules | PASS | FR-003 enforces consistent output formats. FR-008 implements context-adaptive depth. Progressive disclosure via phase gating (FR-004). |

**Gate result: PASS** — All 6 principles and 2 sections satisfied. No violations.

## Project Structure

### Documentation (this feature)

```text
specs/001-ux-design-agent/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (slash command contracts)
│   ├── ux-discover.md
│   ├── ux-define.md
│   ├── ux-ia.md
│   ├── ux-prototype.md
│   ├── ux-validate.md
│   ├── ux-handoff.md
│   └── ux-optimize.md
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Phase 2 output (/speckit.tasks - NOT created here)
```

### Source Code (repository root)

```text
ux-product-design-workflow/
├── SKILL.md                          # Master orchestrator skill (already exists)
├── references/                       # Deep-dive reference docs (already exist)
│   ├── frameworks.md
│   ├── discovery-synthesis.md
│   ├── competitive-analysis.md
│   ├── ideation-prototyping.md
│   ├── laws-of-ux.md
│   ├── arabic-rtl-mena.md
│   ├── usability-testing.md
│   ├── metrics-optimization.md
│   ├── agentic-ai-design.md
│   └── design-handoff.md
├── skills/                           # NEW: Phase-specific sub-skills
│   ├── ux-discover/
│   │   └── SKILL.md                  # Phase 1: Discovery & Research
│   ├── ux-define/
│   │   └── SKILL.md                  # Phase 2: Define & Problem Framing
│   ├── ux-ia/
│   │   └── SKILL.md                  # Phase 3: IA & Interaction Design
│   ├── ux-prototype/
│   │   └── SKILL.md                  # Phase 4: Prototyping & Laws of UX
│   ├── ux-validate/
│   │   └── SKILL.md                  # Phase 5: Validation & Testing
│   ├── ux-handoff/
│   │   └── SKILL.md                  # Phase 6: Design-to-Eng Handoff
│   └── ux-optimize/
│       └── SKILL.md                  # Phase 7: Post-Launch Optimization
├── templates/                        # NEW: Reusable artifact templates
│   ├── persona-template.md
│   ├── journey-map-template.md
│   ├── empathy-map-template.md        # 6 quadrants: Says, Thinks, Does, Feels, Sees, Hears
│   ├── problem-statement-template.md
│   ├── hmw-template.md
│   ├── research-plan-template.md
│   ├── sitemap-template.md
│   ├── user-flow-template.md
│   ├── state-inventory-template.md
│   ├── test-plan-template.md
│   ├── heuristic-evaluation-template.md
│   ├── handoff-checklist-template.md
│   ├── goals-signals-metrics-template.md
│   ├── experiment-backlog-template.md
│   ├── four-risk-gate-template.md
│   ├── competitive-analysis-template.md
│   ├── opportunity-solution-tree-template.md
│   ├── jtbd-statement-template.md
│   ├── findings-report-template.md
│   ├── edge-case-catalog-template.md
│   ├── participant-screener-template.md  # Screener for usability test recruitment
│   ├── north-star-metric-template.md     # NSM definition + input metric tree
│   ├── design-brief-template.md          # Problem summary + constraints + risk gate
│   └── acceptance-criteria-template.md   # Given/When/Then (Gherkin) format
├── checklists/                       # NEW: Phase DoD checklists
│   ├── phase-1-discovery-dod.md
│   ├── phase-2-define-dod.md
│   ├── phase-3-ia-dod.md
│   ├── phase-4-prototype-dod.md
│   ├── phase-5-validate-dod.md
│   ├── phase-6-handoff-dod.md
│   └── phase-7-optimize-dod.md
└── .specify/                         # Spec Kit integration
    ├── memory/
    │   └── constitution.md           # Already created
    └── templates/
        ├── plan-template.md
        ├── spec-template.md
        └── tasks-template.md
```

### User Project Output (generated in consuming repos)

```text
ux/                                   # Created in user's project by agent
├── personas/
│   ├── persona-1-name.md
│   └── persona-2-name.md
├── journeys/
│   ├── journey-1-name.md
│   └── journey-2-name.md
├── research/
│   ├── research-plan.md
│   ├── competitive-analysis.md
│   ├── empathy-maps.md               # 6 quadrants per map
│   ├── jtbd-statements.md
│   ├── participant-screener.md       # Recruitment screener for usability tests
│   └── design-brief.md              # Problem summary + four-risk gate summary
├── ia/
│   ├── sitemap.md                    # Navigation zones + Hick's Law check
│   ├── user-flows.md                 # Happy path + error paths + edge cases
│   └── state-inventories.md          # All 7+ states per interactive element
├── validation/
│   ├── test-plan.md                  # Task-based scenarios, not feature-based
│   ├── heuristic-evaluation.md       # Nielsen's 10, severity-rated (0-4)
│   ├── accessibility-audit.md        # WCAG 2.1 AA POUR checklist
│   ├── findings-report.md            # Severity-rated with impact-effort matrix
│   └── recommendations.md           # Prioritized by impact-effort
├── handoff/
│   ├── handoff-checklist.md          # 4-layer documentation (Context/Flow/Spec/Edge)
│   ├── edge-case-catalog.md
│   ├── state-documentation.md
│   ├── accessibility-spec.md         # ARIA roles, keyboard shortcuts, focus management
│   └── acceptance-criteria.md        # Given/When/Then (Gherkin) format
├── metrics/
│   ├── heart-framework.md            # 5 dimensions with Goals/Signals/Metrics/Targets
│   ├── aarrr-funnel.md              # Stage-by-stage with drop-off hypotheses
│   ├── goals-signals-metrics.md
│   ├── experiment-backlog.md         # Prioritized with hypothesis + success criteria
│   ├── north-star-metric.md          # NSM + input metric tree + counter-metrics
│   └── product-kata-[date].md        # 2-4 week cycle plans (ongoing)
├── risk-assessments/
│   └── four-risk-gate.md
└── phase-status.json                 # Phase tracking metadata
```

**Structure Decision**: This is a skill-system project (not a traditional app). The primary deliverables are SKILL.md files, markdown templates, reference docs, and checklists. The `ux/` directory structure is what the agent *creates in consuming projects* — it's documented here as a contract but not pre-created in this repo.

## Constitution Check — Post-Design Re-evaluation

*Re-check after Phase 1 design completion (data-model.md, contracts/, quickstart.md).*

| Principle | Status | Post-Design Evidence |
|-----------|--------|---------------------|
| I. Ethical Design Hierarchy | PASS | All 7 contracts enforce safety > function > delight ordering. `ux-prototype` contract requires Ethical Design Hierarchy check before Laws of UX application. `ux-handoff` contract requires accessibility requirements (WCAG 2.1 AA) in every handoff doc. FR-012 expanded to cover all design-phase outputs. |
| II. Four-Risk Gate | PASS | `four-risk-gate-template.md` defined in data-model.md with pass/fail/incomplete per risk dimension. `ux-discover` contract includes risk gate as step 6. All phase transitions check risk status in `phase-status.json`. |
| III. Product Triad Collaboration | PASS | Artifact schemas designed for shared consumption: persona templates include engineering-relevant fields (technical constraints, API touchpoints). Handoff contract produces acceptance criteria in Given/When/Then format for engineering. Metrics contract produces GSM tables consumable by PM, Design, and Engineering. |
| IV. UX Quality & Interaction Standards | PASS | `ux-ia` contract mandates all 7+ states per interactive element. `ux-prototype` contract requires Laws of UX application with citations. State inventory template in data-model.md covers: default, empty, loading, partial, error, success, offline, permission. FR-020 adds RTL/MENA patterns. |
| V. Evidence Over Assumption | PASS | Evidence tagging system defined in data-model.md: `[EVIDENCE]`, `[ASSUMPTION]`, `[MEASURED]`, `[CONTRADICTION]`. All artifact schemas include `confidence` field (evidence-backed/assumption/hypothesis). Proto-persona handling explicitly defined in edge cases. FR-023 requires empathy map entries to be traceable. |
| VI. AI as Co-Pilot | PASS | All contracts include guardrails section preventing autonomous decisions. `ux-discover` refuses to fabricate research data. `ux-validate` generates test plans for humans to execute. `ux-handoff` produces documentation for engineering review, not auto-generated code. FR-010 explicitly refuses production code. |
| Workflow Frameworks | PASS | 7 contracts map 1:1 to the 7 phases. Context-adaptive output rules defined in data-model.md with MVP/Growth/Enterprise mode impact table covering all 7 behavioral aspects. Product Kata explicitly implemented in `ux-optimize` contract. |
| Operating Rules | PASS | All contracts produce artifacts (not theory). Context depth adapts per data-model.md inference rules. Progressive disclosure enforced via DoD gating in `phase-status.json`. Cross-phase referencing mandated by FR-019. Spec Kit integration defined in FR-021 and US8. |

**Post-design gate result: PASS** — All 6 principles and 2 sections remain satisfied after Phase 1 design. Enhanced spec adds FR-016 through FR-023, US6-US8, and 4 additional edge cases — all consistent with constitution principles.

## Complexity Tracking

No violations detected. No complexity justifications needed.

## ⚙️ Agent System Specifications & Internal Rules
*(The following operational rules govern this AI Agent's behavior, seamlessly merged from technical specs, CLAUDE.md, and implementation plans).*

### 1. Core Functional Directives
* **Phase Awareness:** The agent MUST identify the user's current UX phase based on existing artifacts and enforce the "Definition of Done" criteria before advancing.
* **Evidence over Assumption:** All generated artifacts MUST explicitly distinguish between evidence-backed content `[EVIDENCE: source]` and assumptions `[ASSUMPTION: reason]`. Proto-personas must be clearly labeled as hypotheses.
* **Context-Adaptive Depth:** Output rigor must scale based on context (lean/scrappy for MVP/Startups; rigorous with compliance checks for Enterprise/Regulated).
* **Scope Guardrails:** The agent MUST strictly refuse to generate production backend code. It provides UX guidance, interaction architectures, and engineering handoff specs.
* **Spec Kit Integration:** The agent MUST cross-reference existing spec artifacts from the `specs/` directory and contribute UX tasks tagged with `[UX]` to the development pipeline.

### 2. Cross-Phase Referencing Matrix (Traceability)
To ensure continuity, the agent MUST link artifacts across phases:
* **Phase 2 (Personas/Journeys):** Must directly reference JTBD statements and research findings from Phase 1.
* **Phase 3 (User Flows/Sitemaps):** Must reference Personas (by name) and Problem Statements from Phase 2.
* **Phase 5 (Test Plans):** Must reference Journey Map pain points.
* **Phase 6 (Handoff Docs):** Must reference State Inventories (Phase 3) and Heuristic Findings (Phase 5).

### 3. Error Message & Empty State Standards
* **Error Messages:** Must follow the structure: `[What happened] + [Why it matters] + [What to do next]`. Never blame the user. Never use technical jargon.
* **Empty States:** Must explicitly include: Visual context (illustration), Headline, Description of value, Primary CTA, and secondary anxiety-reducing information.

### 4. Key UX Benchmarks & Thresholds
* **Usability Testing:** 5 users per segment (finds ~85% of issues).
* **Heuristic Evaluation:** 3-5 evaluators.
* **Touch Targets:** Minimum 44x44px (iOS) / 48x48dp (Android).
* **Color Contrast:** 4.5:1 normal text, 3:1 large text (WCAG 2.1 AA).
* **Doherty Threshold:** <400ms for perceived responsiveness.
* **SUS Score:** Target ≥68. 
* **Task Completion:** Target >80% for primary flows.
* **LTV:CAC Ratio:** Minimum 3:1 for viable product scale.

### 5. Definition of Done (DoD) Gate Checks
Before transitioning phases, the agent must verify:
* **Phase 1 to 2:** Empathy maps, JTBD, competitive analysis, and Four-Risk Gate initial assessment completed.
* **Phase 2 to 3:** Personas, journey maps, Opportunity Solution Tree, and HMW statements validated.
* **Phase 3 to 4:** Sitemap, user flows, and all 7+ state inventories defined.
* **Phase 4 to 5:** Laws of UX applied, micro-interactions spec'd, RTL/MENA patterns (if applicable) applied.
* **Phase 5 to 6:** Heuristic evaluation, accessibility audit, and severity-rated findings documented.
* **Phase 6 to 7:** Annotated specs, edge-case catalog, and Given/When/Then acceptance criteria ready.