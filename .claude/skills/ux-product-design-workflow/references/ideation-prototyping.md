# Ideation, Information Architecture & Prototyping

## Table of Contents
1. [Structured Ideation Frameworks](#structured-ideation-frameworks)
2. [Information Architecture](#information-architecture)
3. [Card Sorting Methodology](#card-sorting-methodology)
4. [User Flows & Task Flows](#user-flows--task-flows)
5. [Prototyping Progression](#prototyping-progression)
6. [Design Sprint (5-Day Process)](#design-sprint)
7. [Design Systems & Tokens](#design-systems--tokens)

---

## Structured Ideation Frameworks

### SCAMPER

A mnemonic-based checklist for systematically generating product improvements:

| Letter | Technique | Prompt Question | Example |
|--------|-----------|----------------|---------|
| **S** | Substitute | What can be replaced? | Replace manual KYC with biometric verification |
| **C** | Combine | What can be merged? | Combine balance check and send money into one screen |
| **A** | Adapt | What can be borrowed from elsewhere? | Adapt ride-sharing's real-time tracking for delivery |
| **M** | Modify | What can be enlarged, reduced, or changed? | Simplify the 7-step onboarding to 3 steps |
| **P** | Put to another use | Can this serve a different purpose? | Use transaction history as a budgeting tool |
| **E** | Eliminate | What can be removed? | Remove mandatory email verification for mobile-first users |
| **R** | Reverse | What if you did the opposite? | Instead of users finding products, products find users |

### Crazy 8s

Rapid divergent thinking exercise:
1. Fold a sheet of paper into 8 sections
2. Set timer for 8 minutes
3. Sketch one idea per section (1 minute each)
4. No judgment, no erasing — just get ideas down
5. Share and discuss with the team
6. Vote on most promising concepts

### Design Studio

Collaborative sketching workshop:
1. Individual sketching round (10 minutes)
2. Present to group (2 minutes each)
3. Critique and feedback (structured, constructive)
4. Second sketching round incorporating feedback
5. Team converges on strongest concepts
6. Refine into wireframe-level concepts

### Lateral Thinking

Break out of habitual logic patterns:
- **Random entry:** Pick a random word, force connections to the problem
- **Provocation:** Make deliberately outrageous statements, then extract useful ideas
- **Reversal:** Describe the worst possible solution, then invert it
- **Analogy:** How is this problem solved in a completely different domain?

### TRIZ (Theory of Inventive Problem Solving)

For resolving technical contradictions:
- Identify the contradiction: "We need the interface to show more information BUT also be simpler"
- Apply inventive principles: segmentation, extraction, local quality, asymmetry, merging
- Draw from 40 established principles that have solved similar contradictions across industries

---

## Information Architecture

### Principles

IA defines how content relates and fits together as a coherent unit:

- **Organization:** How content is categorized and structured
- **Labeling:** How content is named and described
- **Navigation:** How users move through the structure
- **Search:** How users find specific content

### IA Design Process

1. **Content inventory:** Catalog all existing and planned content
2. **Content audit:** Evaluate quality, relevance, and redundancy
3. **Card sorting:** Discover user mental models for grouping
4. **Sitemap creation:** Define hierarchical structure
5. **Navigation design:** Determine primary, secondary, and utility navigation
6. **Tree testing:** Validate that users can find things in the proposed structure

### Navigation Patterns

| Pattern | Best For | Considerations |
|---------|----------|----------------|
| **Bottom tabs** | Mobile apps, 3-5 primary sections | Most discoverable on mobile; limited space |
| **Sidebar navigation** | Desktop apps, complex hierarchies | Supports deep navigation; responsive challenge |
| **Hamburger menu** | Secondary navigation, space-constrained | Lower discoverability; hide-and-seek problem |
| **Top tabs** | Content categories, settings screens | Good for 2-5 peer sections |
| **Breadcrumbs** | Deep hierarchies, e-commerce | Orientation and backtracking |
| **Search-first** | Content-heavy platforms, utilities | Requires good search implementation |

---

## Card Sorting Methodology

### Types

| Type | Description | When to Use |
|------|-------------|------------|
| **Open** | Users create their own groups and labels | New IA, discovering mental models |
| **Closed** | Users organize into predefined categories | Validating an existing structure |
| **Hybrid** | Predefined categories + user-created ones | Refining and extending existing IA |
| **Tree testing** | Users navigate a hierarchy to find items | Validating navigation paths |

### Running a Card Sort

**Preparation:**
- Select 30-70 content cards representing key content items
- Avoid identical words across cards (auto-grouping bias)
- Recruit 15-30 participants per round
- Choose open sort for discovery, closed for validation

**Analysis:**
- **Similarity matrix:** Which cards are frequently grouped together?
- **Dendrogram:** Visual cluster analysis showing grouping strength
- **Category agreement:** What percentage of participants grouped items the same way?
- **Standardized labels:** What names do participants give to their groups?

**Success criteria:**
- >70% agreement on key categories indicates strong mental model alignment
- Categories with <50% agreement need further investigation
- Outlier cards that don't fit any group may indicate content gaps or labeling issues

---

## User Flows & Task Flows

### User Flow
High-level path a user takes through the product to accomplish a goal:
- Start with the entry point (how the user arrives)
- Map decision points (branches based on user choices or system state)
- Show all possible paths, including error and edge cases
- End with the goal state (success) or exit points (abandonment, error)

### Task Flow
Detailed step-by-step sequence for a specific task:
- Single path, no branching
- Every screen/state the user encounters
- Every action the user takes
- Every system response

### State Design

Every screen must account for these states:

| State | Description | Design Consideration |
|-------|-------------|---------------------|
| **Default** | Normal, populated state | The primary design |
| **Empty** | No data yet | Explain why, guide action, show potential |
| **Loading** | Data being fetched | Skeleton screens, spinners, progress indicators |
| **Error** | Something went wrong | Clear message, recovery action, don't lose data |
| **Success** | Action completed | Confirmation, next steps, delight moment |
| **Partial** | Some data available | Progressive loading, prioritize critical content |
| **Offline** | No network | Show cached data, queue actions, indicate status |
| **Permission** | Access required | Explain why, show value, respect refusal |

---

## Prototyping Progression

### Fidelity Levels

**Low-Fidelity (Paper/Sketch)**
- Hand-drawn sketches, paper prototypes
- 15-30 minutes to create
- Advantages: fast, cheap, encourages divergent thinking, easy to modify during testing
- Limitations: lacks detail, limited interactivity
- Best for: early exploration, rapid ideation, team alignment

**Mid-Fidelity (Wireframes)**
- Digital wireframes with basic interactions
- 1-3 hours per screen
- Advantages: tests structure without visual bias, quick iteration
- Limitations: may confuse stakeholders expecting polish
- Best for: IA validation, flow testing, internal reviews

**High-Fidelity (Interactive)**
- Polished visuals, realistic interactions, real content
- 4-8 hours per screen
- Advantages: realistic behavior, meaningful feedback, users treat as real product
- Limitations: time-intensive, harder to change, may anchor team on specific direction
- Best for: usability testing, stakeholder presentations, developer handoff

### Progressive Fidelity Rules

**No Lorem Ipsum — ever.** Use realistic content at every fidelity level:
- Low-fi: handwritten realistic text (even rough)
- Mid-fi: actual copy or near-final text
- High-fi: production-ready content in every state (empty, populated, error, overflow)

Why: Lorem Ipsum hides content strategy failures. Real text reveals truncation bugs, awkward label lengths, and localization issues early.

**Real data, not ideal data.** Design with:
- Names that are long (محمد عبدالرحمن الشريف), short (أحمد), and transliterated
- Amounts that span ranges (EGP 0.50 to EGP 999,999.99)
- Lists that have 0 items, 1 item, and 200 items
- Dates in multiple formats and calendars

### Whitespace Management Rule

Whitespace allocation should match usage frequency:

| Page Type | Usage Pattern | Whitespace Rule |
|-----------|--------------|-----------------|
| **Dashboard / daily-use** | High frequency, task-focused | **Tighter whitespace** — users need density and efficiency |
| **Landing page / onboarding** | Low frequency, first impression | **More spacious** — users need breathing room and orientation |
| **Settings / configuration** | Rare usage, reference-based | **Moderate** — scannable with clear grouping |
| **Data tables / reports** | Analysis mode, comparison | **Tight with clear borders** — maximize information density |

This is not about aesthetics — it's about matching cognitive load to task frequency.

### Fidelity Selection Guide

| Factor | Low-Fi | Mid-Fi | High-Fi |
|--------|--------|--------|---------|
| **Time available** | Hours | Days | Weeks |
| **Questions to answer** | "Is this the right concept?" | "Does the structure work?" | "Is this usable and delightful?" |
| **Audience** | Internal team | Internal + stakeholders | Users, investors, developers |
| **Risk of test** | Low (easy to pivot) | Medium | High (significant investment) |

---

## Design Sprint

### The 5-Day Process (Google Ventures)

For high-priority, time-sensitive problems:

**Monday — Map**
- Define the long-term goal
- Map the challenge: user journey from start to goal
- Identify the target: which moment in the journey to focus on
- Interview experts (stakeholders, engineers, support)
- Choose the sprint target

**Tuesday — Sketch**
- Lightning demos: review existing solutions in the market
- Individual sketching: each person works independently
- Crazy 8s: 8 ideas in 8 minutes
- Solution sketch: detailed, self-explanatory concept
- No group brainstorming (avoids groupthink)

**Wednesday — Decide**
- Art museum: post all sketches, silent review
- Heat map: dot voting on compelling elements
- Speed critique: 3-minute guided discussion per sketch
- Straw poll: everyone votes for their top pick
- Decider makes the final call
- Storyboard: plan the prototype screen-by-screen

**Thursday — Prototype**
- Build a realistic facade (looks real, isn't functional)
- Divide and conquer: assign screens to team members
- "Goldilocks quality": just enough polish to test
- Tools: Figma, Keynote, or even hand-drawn slides
- Prepare the interview script for Friday

**Friday — Test**
- 5 one-on-one user interviews (45-60 minutes each)
- Entire team observes via screen share or one-way mirror
- Take structured notes on patterns
- End-of-day debrief: what did we learn? What's next?
- Decide: iterate, pivot, or ship

---

## Design Systems & Tokens

### Design Token Architecture

Three-layer organization:

**Primitive tokens** — Raw values
```
color-blue-500: #3B82F6
color-gray-900: #111827
spacing-4: 16px
font-size-base: 16px
radius-md: 8px
```

**Semantic tokens** — Contextual meaning
```
text-default: color-gray-900
text-muted: color-gray-500
bg-primary: color-blue-500
spacing-section: spacing-8
```

**Component tokens** — Component-specific values
```
button-bg: bg-primary
button-radius: radius-md
button-padding-x: spacing-4
card-shadow: shadow-md
input-border: color-gray-300
```

### Component Library Requirements

Each component should document:
- **Purpose:** When and why to use this component
- **Variants:** All visual/behavioral variations (primary, secondary, ghost, etc.)
- **States:** Default, hover, active, focus, disabled, error, loading
- **Sizes:** Small, medium, large (if applicable)
- **Accessibility:** ARIA labels, keyboard behavior, screen reader announcements
- **Usage guidelines:** Do's and don'ts with examples
- **Code examples:** Implementation reference

### Shared Language

Designers and developers must use the same naming conventions:
- Same token names in Figma and code
- Same component names across design and implementation
- Documented mapping when names must differ
- Regular sync to prevent drift

---

## Workshop Facilitation

### Facilitator Responsibilities

A good facilitator enables the group's best thinking rather than directing it:

- **Set the frame:** Define the problem, constraints, and time boundaries clearly before starting
- **Manage energy:** Alternate between divergent (generative) and convergent (evaluative) activities
- **Protect quiet voices:** Use silent ideation before group discussion; round-robin sharing ensures everyone contributes
- **Time-box ruthlessly:** Parkinson's law applies — work expands to fill available time. Tight time-boxes force decisiveness
- **Stay neutral:** The facilitator doesn't contribute ideas or evaluate them. If you have strong opinions, hand facilitation to someone else

### Workshop Toolkit

| Activity | Duration | Purpose | Group Size |
|----------|----------|---------|-----------|
| **Icebreaker** | 5-10 min | Build psychological safety | Any |
| **How Might We** | 15 min | Convert problems to opportunities | 3-8 |
| **Crazy 8s** | 8 min | Rapid divergent sketching | Individual → group share |
| **Dot voting** | 5 min | Quick democratic prioritization | Any |
| **Affinity mapping** | 20-30 min | Cluster and theme ideas | 3-8 |
| **2x2 matrix** | 15 min | Plot ideas on impact vs. effort | 3-8 |
| **Rose/Bud/Thorn** | 10 min | Structured feedback on concepts | Any |
| **Storyboarding** | 30-45 min | Visualize a concept end-to-end | 2-4 per story |

### Psychological Safety in Ideation

Ideation fails when people don't feel safe contributing. Establish these norms explicitly:

- **"Yes, and..."** — Build on ideas instead of shooting them down
- **No idea ownership** — Once shared, ideas belong to the group, not the individual
- **Separate generation from evaluation** — Diverge first (no judgment), then converge (structured critique)
- **Equal voice protocol** — Silent writing before group discussion; round-robin sharing; anonymous dot voting
- **Celebrate wild ideas** — The goal during divergence is volume and variety, not quality. Quality comes during convergence
- **Name the elephant** — If seniority or politics are suppressing ideas, the facilitator must call it out

### Workshop Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| **HiPPO effect** | Highest-paid person's opinion dominates | Silent ideation first; anonymous voting |
| **Groupthink** | Everyone agrees too quickly | Devil's advocate role; "What could go wrong?" round |
| **Analysis paralysis** | Can't commit to a direction | Time-box decisions; "disagree and commit" protocol |
| **Scope creep** | Workshop tries to solve everything | Write a parking lot for off-topic ideas; stay focused on sprint question |
| **No outcomes** | Fun workshop with no actionable result | End every workshop with: decisions made, owners assigned, next steps dated |

---

## Remote Ideation

### Adapting for Remote Teams

Remote ideation has unique challenges but also advantages (asynchronous contribution, broader participation, persistent artifacts):

**Tools:**
- **FigJam / Miro / MURAL:** Virtual whiteboard for real-time collaboration
- **Figma:** For collaborative wireframing and design studio exercises
- **Google Docs/Slides:** For asynchronous concept development
- **Loom:** For asynchronous concept presentations when synchronous time is limited

**Remote-specific adaptations:**
- **Camera on for generative sessions:** Non-verbal cues matter for creative energy
- **Breakout rooms for parallel work:** Groups of 2-3 generate more ideas than one large group
- **Async pre-work:** Share context materials 24 hours before the session so workshop time is for creating, not reading
- **Timer visible on screen:** Shared timer keeps everyone aligned
- **Dedicated note-taker:** Someone other than the facilitator captures decisions and ideas in real-time

**Session length guidelines:**
- Remote attention spans are shorter than in-person
- Maximum 90-minute blocks with 10-minute breaks
- For full-day design sprints, split across 2-3 days with async work between sessions
- Morning sessions are more productive for creative work

---

## Convergence & Decision Techniques

After divergent ideation, the team must converge on which ideas to pursue. This is where most workshops fail — teams either can't decide or the loudest voice wins.

### Dot Voting

The simplest convergence technique:
1. Each participant gets 3-5 dot stickers (or virtual dots)
2. Place dots on the ideas you find most promising
3. Can place multiple dots on one idea (shows conviction)
4. Count dots, discuss top-voted ideas
5. Facilitator or decider makes final call

**When to use:** Quick prioritization among many options
**Limitation:** Popularity isn't always quality. Use as input, not final decision.

### Decision Matrix

Structured evaluation against defined criteria:

| Idea | User Impact (1-5) | Feasibility (1-5) | Business Value (1-5) | Novelty (1-5) | Total |
|------|-------------------|-------------------|---------------------|--------------|-------|
| Concept A | 5 | 3 | 4 | 2 | 14 |
| Concept B | 3 | 5 | 3 | 4 | 15 |
| Concept C | 4 | 2 | 5 | 5 | 16 |

**When to use:** When you need a defensible, criteria-based decision
**Limitation:** Weighting criteria is subjective. Discuss weights before scoring.

### Note-and-Vote

Jake Knapp's method from Design Sprints:
1. **Note:** Everyone silently writes their top pick on a sticky note (with brief rationale)
2. **Vote:** Reveal simultaneously — no influence from seeing others' votes first
3. **Discuss:** Only discuss if there's disagreement. The Decider has final call.

**When to use:** When you need fast commitment and have a clear decision-maker
**Limitation:** Requires a designated Decider who the team trusts.

### Idea Portfolio

Not every decision is binary. Consider maintaining a portfolio:
- **Build now:** High confidence, high impact, feasible
- **Prototype and test:** High potential but uncertain — needs validation
- **Revisit later:** Interesting but not timely — add to opportunity backlog
- **Kill:** Low potential or redundant — explicitly retire

This avoids the trap of losing good ideas that aren't right for this moment.

---

## Feature Prioritization Template

Use this template to evaluate and rank features systematically. It combines user impact with business and feasibility factors to prevent prioritization by gut feeling or seniority (HiPPO effect).

### RICE Scoring Matrix

| Feature | Reach | Impact | Confidence | Effort | RICE Score | Priority |
|---------|-------|--------|------------|--------|------------|----------|
| [Feature name] | [# users affected per quarter] | [0.25 / 0.5 / 1 / 2 / 3] | [50% / 80% / 100%] | [person-weeks] | [R×I×C÷E] | [Rank] |

**Scoring guide:**
- **Reach:** Estimated number of users who will encounter this feature per quarter. Use analytics data, not guesses.
- **Impact:** How much this moves the target metric per user. 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal.
- **Confidence:** How sure you are about Reach and Impact estimates. 100% = backed by data/testing. 80% = strong signals. 50% = speculative.
- **Effort:** Total person-weeks of design + engineering work. Include QA and deployment.
- **RICE Score:** (Reach × Impact × Confidence) ÷ Effort. Higher = prioritize first.

### Worked Example: Mobile Wallet Feature Backlog

| Feature | Reach | Impact | Confidence | Effort | RICE Score | Priority |
|---------|-------|--------|------------|--------|------------|----------|
| Repeat last transfer (one-tap) | 45,000 | 2 | 100% | 2 | 45,000 | 1st |
| Instant transfer confirmation | 60,000 | 1 | 80% | 3 | 16,000 | 2nd |
| Bill payment integration | 30,000 | 2 | 50% | 8 | 3,750 | 3rd |
| Family group wallets | 10,000 | 3 | 50% | 12 | 1,250 | 4th |

### Complementary Lenses

RICE alone isn't sufficient. Cross-check with:

| Lens | Question | Override condition |
|------|----------|--------------------|
| **Four Product Risks** | Does this reduce value, usability, feasibility, or viability risk? | Deprioritize features that don't address a validated risk |
| **Strategic alignment** | Does this support our current OKRs? | Features misaligned with strategy need executive sponsor |
| **Dependencies** | Does another feature require this first? | Sequence blockers override RICE ranking |
| **User pain severity** | Is this a showstopper or a nice-to-have? | Showstopper bugs override all feature work |
| **Ethical baseline** | Does skipping this create accessibility or safety gaps? | Ethics gaps are non-negotiable — always prioritize |

### Anti-Pattern: Prioritization Without User Evidence

| Symptom | Fix |
|---------|-----|
| RICE scores use made-up Reach numbers | Pull Reach from analytics or validated user counts |
| Impact scores are all 3 ("everything is critical") | Force-rank: only 20% of features can be Impact 3 |
| Confidence is always 100% | If there's no user testing data, Confidence cannot exceed 80% |
| Features added by executives bypass the matrix | Every feature goes through RICE — executives can increase priority with a documented rationale, but not skip evaluation |

---

## Phase Transition Signals for Ideation

### Definition of Done — Ideation & IA Phase

Before moving from Ideation into Interaction Design:

- [ ] At least 3 distinct solution concepts generated and evaluated per core problem
- [ ] Concepts evaluated against desirability (user want), feasibility (can build), viability (business case)
- [ ] Information architecture validated through card sorting or tree testing (>80% findability on primary paths)
- [ ] User flows mapped for all primary scenarios including error and edge cases
- [ ] All screen states designed: default, empty, loading, error, success, partial, offline, permission
- [ ] Low-fidelity wireframes reviewed by the Triad (PM, Design, Engineering)
- [ ] No concept selected purely based on HiPPO — evidence-based decision documented
- [ ] Ideas explicitly killed are documented with rationale (institutional memory)
- [ ] Selected concept(s) have clear next-step: prototype fidelity level and test plan

---

### Cross-References
- For cognitive load in navigation design → `laws-of-ux.md` (Miller's Law, Hick's Law)
- For accessibility-first component design → `usability-testing.md` (WCAG POUR)
- For RTL navigation patterns → `arabic-rtl-mena.md`
- For RICE scoring metric alignment → `metrics-optimization.md`
- For AI-assisted ideation → `agentic-ai-design.md`
