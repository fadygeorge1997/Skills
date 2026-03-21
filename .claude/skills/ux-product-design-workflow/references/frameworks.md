# Foundational Frameworks

## Table of Contents
1. [The Double Diamond Process](#the-double-diamond-process)
2. [Lean UX: Rapid Experimentation](#lean-ux-rapid-experimentation)
3. [The Product Kata: Continuous Discovery](#the-product-kata-continuous-discovery)
4. [Integrating the Three Frameworks](#integrating-the-three-frameworks)
5. [The Product Triad Operating Model](#the-product-triad-operating-model)
6. [Continuous Discovery Habits](#continuous-discovery-habits)

---

## The Double Diamond Process

The Double Diamond (UK Design Council) visualizes the balance between divergent thinking (exploring widely) and convergent thinking (narrowing to decisions). It prevents teams from jumping to solutions before understanding the problem.

### Diamond 1: Solve the Right Problem

**Discover (Divergent)**
- Understand the user and problem space without bias
- Activities: ethnographic research, user interviews, surveys, competitive analysis
- Output: raw research data, observation notes, market landscape
- Mindset: curiosity, empathy, suspension of judgment
- Duration: typically 2-4 weeks depending on product complexity

**Define (Convergent)**
- Synthesize insights into a clear, actionable problem statement
- Activities: affinity mapping, persona creation, empathy maps, "How Might We" statements
- Output: prioritized problem statements, design brief, opportunity backlog
- Mindset: analytical, pattern-seeking, decisive
- Key discipline: resist the urge to ideate solutions here

### Diamond 2: Build the Right Solution

**Develop (Divergent)**
- Explore, brainstorm, and prototype a wide range of potential solutions
- Activities: structured brainstorming, storyboarding, rapid low-fidelity prototyping
- Output: concept sketches, wireframes, multiple solution directions
- Mindset: creative, generative, non-judgmental
- Key discipline: quantity over quality at this stage

**Deliver (Convergent)**
- Test, refine, and finalize the best iteration for launch
- Activities: usability testing, iteration, developer handoff, launch planning
- Output: validated high-fidelity designs, implementation specifications
- Mindset: evaluative, detail-oriented, pragmatic

### When to Use Double Diamond

- Starting a new product or major feature from scratch
- Tackling a problem where the root cause is unclear
- When the team needs structured diverge-converge discipline
- Projects with 4+ weeks of design time

---

## Lean UX: Rapid Experimentation

Lean UX (Jeff Gothelf, inspired by Eric Ries) discards time-consuming requirements elicitation in favor of hypothesis-driven validation. The focus shifts from producing heavy deliverables to achieving measurable outcomes.

### The Core Loop: Think > Make > Check

**Think**
- Brainstorm improvement areas based on customer feedback, competitor analysis, and behavioral analytics
- Develop a problem statement
- Formulate testable hypotheses: "We believe [action] for [user] will achieve [outcome]. We'll know this is true when [metric]."
- Decide which specific hypotheses to test first

**Make**
- Build the minimum viable artifact to test the hypothesis
- Speed matters more than polish
- Could be a paper sketch, clickable wireframe, "fake door" test, or concierge MVP
- The artifact exists solely to validate or invalidate the hypothesis

**Check**
- Test using UX surveys, A/B testing, analytics, or direct observation
- Determine whether the underlying hypothesis holds true
- Based on results: pivot (change direction) or persevere (scale the solution)
- Document learnings regardless of outcome

### Lean UX Principles

1. **Outcomes over outputs:** Measure success by user behavior change, not deliverables produced
2. **Shared understanding:** The team's collective knowledge reduces need for documentation
3. **No rock stars, gurus, or ninjas:** Cross-functional collaboration over individual heroics
4. **Permission to fail:** Rapid experimentation requires psychological safety
5. **Getting out of the building:** Real user contact beats internal debates

### When to Use Lean UX

- Agile/sprint-based development environments
- Feature iteration on existing products
- When speed of learning matters more than comprehensive documentation
- Startup or growth-stage products with high uncertainty

---

## The Product Kata: Continuous Discovery

Rooted in lean manufacturing (Toyota Production System), the Product Kata embeds a continuous discovery habit through four iterative steps.

### The Four Steps

**1. Understand the Direction**
- Align with overarching company strategy
- Understand major business objectives and ultimate product vision
- This is the North Star that all experiments point toward
- Example: "Become the most trusted digital wallet in Egypt by 2027"

**2. Grasp the Current Condition**
- Analyze the current state of the product
- Identify baseline metrics and current user behaviors
- Use both quantitative data (analytics, funnel metrics) and qualitative data (user interviews, support tickets)
- Be honest about where you actually are, not where you wish you were

**3. Define the Target Condition**
- Establish the next immediate, measurable interim goal
- This is NOT the final vision; it's the next achievable checkpoint
- Should be reachable within 1-4 weeks of experimentation
- Example: "Increase first-transaction completion from 34% to 50%"

**4. Move Iteratively**
- Execute small, rapid experiments (lasting a week or less)
- Each experiment tests a specific assumption about how to reach the target
- Uncover obstacles, validate assumptions, and incrementally progress
- After each experiment: What did we expect? What happened? What did we learn? What's next?

### When to Use Product Kata

- Continuous improvement of live products
- When the team needs a scientific habit for decision-making
- Bridging the gap between strategy and daily execution
- Complementing Lean UX with a more structured rhythm

---

## Integrating the Three Frameworks

These frameworks are complementary, not competing:

```
Double Diamond          Lean UX              Product Kata
(Macro Structure)      (Sprint Velocity)    (Continuous Habit)
┌─────────────┐        ┌──────────┐         ┌─────────────┐
│ Discover     │  ←──── │ Think    │  ←───── │ Understand  │
│ Define       │        │          │         │ Grasp       │
├─────────────┤        ├──────────┤         ├─────────────┤
│ Develop      │  ←──── │ Make     │  ←───── │ Target      │
│ Deliver      │        │ Check    │         │ Experiment  │
└─────────────┘        └──────────┘         └─────────────┘

     PHASES              VELOCITY              RHYTHM
```

- **Double Diamond** tells you WHAT phases to go through
- **Lean UX** tells you HOW FAST to move within each phase
- **Product Kata** tells you HOW TO SUSTAIN the practice over time

In practice: Use the Double Diamond's phases for project structure. Within each phase, apply Lean UX's hypothesis-driven loops for speed. Across product lifecycles, use the Product Kata's rhythm for continuous improvement.

---

## The Product Triad Operating Model

### Roles in Detail

**Product Management (Viability)**
- Guides strategic direction, aligns product vision with business goals
- Maps the development journey, prioritizes features
- Ensures the product makes financial and market sense
- Owns the "what" and "why" of the roadmap

**UX / Product Design (Desirability)**
- Connects strategy with user needs through deep empathy
- Crafts intuitive, engaging interfaces
- Advocates for the user experience throughout the process
- Owns the "how it feels" and "how it works"

**Engineering (Feasibility)**
- Transforms vision into reality
- Advises on technical complexity, architecture, scalability
- Ensures the product is robust, secure, and efficient
- Owns the "how it's built" and "what's possible"

### Collaboration Rituals

- **Weekly Triad Sync:** 30-minute alignment on current sprint priorities and blockers
- **Joint User Interviews:** All three roles participate in discovery research together
- **Design Reviews:** Engineers present early, before pixel-perfect delivery
- **Sprint Planning:** Triad jointly estimates and sequences work
- **Retrospectives:** Shared reflection on process and collaboration quality

### Decision Forums

Clarify decision ownership early:
- **User need validation:** UX leads, PM and Eng input
- **Prioritization:** PM leads, UX and Eng input
- **Technical approach:** Eng leads, PM and UX input
- **Shared metrics:** All three agree on outcome metrics (e.g., activation rate, retention)

The tension between desirability, feasibility, and viability is productive when all three voices are heard equally. No single discipline should dominate.

### Four Product Risks

Every product initiative faces four risks that the Triad must address:

| Risk | Question | Who Validates | How |
|------|----------|---------------|-----|
| **Value risk** | Will users want this? | PM + Design | User interviews, demand testing, JTBD analysis |
| **Usability risk** | Can users figure it out? | Design | Usability testing, heuristic evaluation |
| **Feasibility risk** | Can we build and scale it? | Engineering | Technical spikes, architecture review, prototypes |
| **Viability risk** | Does it work for the business? | PM | Business modeling, unit economics, compliance review |

If any risk is unaddressed, the product fails. The Triad exists to ensure all four are covered simultaneously, not sequentially.

### Missionaries vs. Mercenaries

High-performing product teams operate as **missionaries** (driven by the problem and the user) rather than **mercenaries** (driven by specs and deadlines):

| Missionaries | Mercenaries |
|-------------|-------------|
| Obsessed with the user's problem | Focused on shipping features |
| Measure outcomes (retention, satisfaction) | Measure output (features shipped, velocity) |
| Empowered to find the best solution | Given a solution to implement |
| Feel ownership of the product's success | Feel ownership of their task list |
| Push back on bad ideas with evidence | Build whatever is requested |

Build missionary teams by: sharing the vision, empowering with context, measuring outcomes, and giving the Triad real decision authority.

---

## Continuous Discovery Habits

Teresa Torres' framework mandates an ongoing rhythm rather than treating research as a one-time kickoff:

### Weekly Customer Touchpoints
- The team building the product conducts weekly interviews
- Small research activities in pursuit of a desired product outcome
- Focus on understanding the opportunity space (needs, pain points, desires)

### The Opportunity Solution Tree (OST)

Visual mapping structure with four components:

1. **Outcome Metric:** The business-relevant metric guiding discovery
2. **Opportunities:** Customer pain points and unmet needs (discovered through research)
3. **Solution Ideas:** Hypotheses for addressing opportunities
4. **Experiments:** Validation methods to de-risk solutions before building

```
         [Outcome Metric]
              │
    ┌─────────┼─────────┐
    │         │         │
[Opp A]   [Opp B]   [Opp C]
    │         │
 ┌──┴──┐   ┌─┴──┐
[S1] [S2] [S3] [S4]
 │         │
[E1]      [E2]
```

This shifts teams from "feature delivery" to "rapid experimentation," tying every solution to a customer problem and a measurable business outcome.

### OST Best Practices

- **One tree per outcome.** Don't overload a single tree with multiple business metrics.
- **Opportunities come from research, not brainstorming.** They must be grounded in evidence from user interviews, analytics, or support data.
- **Multiple solutions per opportunity.** Don't fall in love with the first idea. Generate at least 3 alternatives.
- **Small, fast experiments.** Each experiment should be completable in 1-2 weeks and test a specific assumption.
- **Compare and contrast.** Test multiple solutions for the same opportunity simultaneously when possible.

---

## Design Thinking: The Five Phases

While the Double Diamond provides macro-structure and Lean UX provides velocity, Design Thinking (Stanford d.school / IDEO) provides the mindset. Its five phases are non-linear and iterative:

1. **Empathize:** Observe and engage with users to understand their experiences and motivations
2. **Define:** Synthesize findings into a point-of-view statement about the user's core need
3. **Ideate:** Generate a broad range of creative solutions without judgment
4. **Prototype:** Build quick, cheap representations of ideas to learn through making
5. **Test:** Share prototypes with users to get feedback and refine understanding

The key insight of Design Thinking is that the process is non-linear. Testing often reveals that the problem needs redefining. Prototyping often generates new ideas. Each phase can loop back to any previous phase.

---

## Framework Selection Guide

| Situation | Primary Framework | Why |
|-----------|------------------|-----|
| New product, unknown problem | Double Diamond | Need structured diverge-converge to find the right problem first |
| Existing product, feature iteration | Lean UX | Hypothesis-driven sprints move faster than full discovery cycles |
| Post-launch optimization | Product Kata | Scientific experimentation habit for incremental improvement |
| Design sprint (1 week) | Design Thinking + Lean UX | Compressed timeline needs empathy + rapid prototyping |
| Enterprise redesign | Double Diamond + Continuous Discovery | Long-term structural work needs both exploration and ongoing validation |
| Startup MVP | Lean UX | Speed to learning is the priority; minimize upfront investment |

In practice, most teams blend all three. The frameworks are lenses, not cages. Use whichever lens gives the clearest view for the current challenge.
