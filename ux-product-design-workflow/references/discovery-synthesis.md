# Discovery & Synthesis

## Table of Contents
1. [Jobs-To-Be-Done (JTBD) Framework](#jobs-to-be-done-framework)
2. [Research Methods](#research-methods)
3. [Problem Definition Frameworks](#problem-definition-frameworks)
4. [Empathy Mapping](#empathy-mapping)
5. [Persona Development](#persona-development)
6. [Journey Mapping](#journey-mapping)
7. [The DIKW Pyramid](#the-dikw-pyramid)
8. [Cognitive Prompting for AI Synthesis](#cognitive-prompting-for-ai-synthesis)
9. [Bias Mitigation](#bias-mitigation)

---

## Jobs-To-Be-Done Framework

People don't buy products; they "hire" them to make functional, emotional, and social progress. Jobs remain stable over time even as technologies change, making innovation more predictable.

### JTBD Job Map

Trace the customer's chronological steps when performing a job:

| Step | Description | Design Question |
|------|-------------|----------------|
| **Define** | Identify what needs to be accomplished and why | How do users frame the need? |
| **Locate** | Gather necessary resources and information | Where do they look first? What's missing? |
| **Prepare** | Set up the environment to begin | What setup friction exists? |
| **Confirm** | Ensure everything is ready before execution | What uncertainty do they feel? |
| **Execute** | Perform the job to achieve the desired outcome | Where do they struggle or get confused? |
| **Monitor** | Check progress to ensure the job proceeds as planned | How do they know it's working? |
| **Modify** | Adjust approach if obstacles or errors arise | What recovery options do they need? |

### Service Categories

At each step, users may be:
- **Underserved:** Opportunity for new features or improvements
- **Overserved:** Opportunity to simplify and reduce complexity
- **Appropriately served:** Maintain current experience

### JTBD Interview Questions

**Trigger Questions:**
- "Walk me through the last time you needed to [job]. What prompted you?"
- "What was happening in your life/work when you decided to look for a solution?"

**Pain Point Questions:**
- "What was the hardest part about [the job]?"
- "What workarounds have you tried? Why did you stop using them?"

**Desired Outcome Questions:**
- "If you could wave a magic wand, what would the ideal experience look like?"
- "What would success feel like when this job is done?"

**Three Dimensions:**
- **Functional:** What practical outcome are they trying to achieve?
- **Emotional:** How do they want to feel during and after?
- **Social:** How do they want to be perceived by others?

### Enhanced JTBD Statement Format

Go beyond simple job statements to capture full context:

> "When [circumstance], I want to [job], so I can [need/outcome] without [pain point]."

**Examples:**

| Component | Example 1 (Fintech) | Example 2 (E-commerce) |
|-----------|---------------------|----------------------|
| **When** | I receive my monthly salary | I'm browsing on my commute |
| **I want to** | pay all my bills in one session | save items to buy later |
| **So I can** | feel financially organized | make purchase decisions at home |
| **Without** | worrying I've missed a payment or been overcharged | losing my selections when I close the app |

This format gives designers richer material than simple job statements by explicitly capturing the situational trigger, the desired emotional outcome, and the friction to eliminate.

---

## Research Methods

### Qualitative Methods

**User Interviews (Generative)**
- Open-ended, exploratory conversations
- 45-60 minutes per session
- Record and transcribe for analysis
- Focus on stories and specific examples, not hypothetical opinions

**Contextual Inquiry / Field Studies**
- Observe users in their real environment
- Combines observation with interview
- Captures environmental context that interviews miss
- Particularly valuable for understanding mobile usage patterns

**Diary Studies**
- Longitudinal: capture behaviors and feelings over days/weeks
- Users self-report at natural moments
- Reveals patterns that single-session research cannot

### Quantitative Methods

**Surveys**
- Validate patterns identified in qualitative research
- Standardized scales: SUS, NPS, CSAT, custom Likert scales
- Sample size: minimum 30 for basic trends, 100+ for statistical significance

**Analytics Review**
- Heatmaps, session recordings, conversion funnels
- Support ticket analysis for pain point frequency
- Feature usage data, drop-off rates, error logs

**Competitive Analysis**
- Feature comparison matrices
- UX teardowns of competitor products
- Identify market gaps and established patterns

---

## Problem Definition Frameworks

### 5W1H Method

Systematic questioning to ensure all aspects of a problem are captured:

| Question | Focus | Example |
|----------|-------|---------|
| **Who** | Users affected | First-time mobile wallet users aged 25-35 |
| **What** | The problem | Cannot complete first transaction |
| **When** | Timing/context | During initial onboarding, within first 48 hours |
| **Where** | Environment | Mobile app, predominantly Android, unreliable connectivity |
| **Why** | Root cause | Unclear fee structure creates anxiety about hidden charges |
| **How** | Mechanism | Users reach payment confirmation screen and abandon |

### CATWOE Analysis

Systems-thinking approach for complex organizational ecosystems:

- **C**ustomers: Who benefits or suffers from the system?
- **A**ctors: Who performs the activities within the system?
- **T**ransformation: What inputs become what outputs?
- **W**orldview: What perspective makes this system meaningful?
- **O**wners: Who has authority to change the system?
- **E**nvironment: What external constraints exist?

### Root Cause Analysis

**5 Whys Technique:**
Start with the observed problem and ask "why" five times to dig past symptoms:

1. Users abandon checkout → Why? They're confused by the total
2. Why? Fees appear unexpectedly at the last step
3. Why? Fee calculation happens server-side after address entry
4. Why? The architecture was built for desktop with different flow
5. Why? Mobile experience was retrofitted, not designed mobile-first

**Ishikawa (Fishbone) Diagram:**
Organize multiple causal factors visually. Categories often include: People, Process, Technology, Environment, Policy, Content.

**Iceberg Model:**
Look beyond surface events to identify:
- **Events:** What happened? (visible)
- **Patterns:** What trends recur? (behavioral)
- **Structures:** What systems cause these patterns? (systemic)
- **Mental Models:** What assumptions drive the structures? (foundational)

---

## Empathy Mapping

Capture what users Say, Think, Do, and Feel:

| Quadrant | What to Capture | Sources |
|----------|----------------|---------|
| **Says** | Direct quotes from interviews and observations | Transcripts, verbatim notes |
| **Thinks** | Internal thoughts inferred from context, tone, body language | Behavioral cues, follow-up probes |
| **Does** | Observable behaviors and actions | Screen recordings, field observations |
| **Feels** | Emotional drivers: frustration, excitement, anxiety | Tone analysis, facial expressions, word choice |
| **Sees** | What the user observes about brands, competitors, market | Environmental context, competitive landscape |
| **Hears** | What friends, colleagues, influencers tell them | Social context, peer influence |

Subdivide into **Pains** (blockers, fears, frustrations) and **Gains** (desired outcomes, delights) to prioritize solutions.

---

## Persona Development

### Evidence-Based Personas

Build from research data, not assumptions:

**Core Components:**
- Demographic details: age, occupation, income, location, tech literacy
- Behavioral patterns: how they interact with products, preferred platforms, frequency
- Pain points and motivations: what frustrates or drives them
- Goals: what they're trying to achieve (linked to JTBD)
- Preferred engagement channels: mobile, web, in-person, chat
- A representative quote from actual research

**Personas + JTBD Together:**
- Personas answer "Who are your users?" (context)
- JTBD answers "What are they trying to accomplish?" (action)
- Use both: personas provide empathy, JTBD provides actionable direction

---

## Journey Mapping

### Key Elements

- **Stages:** Awareness > Consideration > Onboarding > Core Use > Retention > Advocacy
- **Touchpoints:** Every interaction point (website, app, email, support, physical)
- **Actions:** What the user does at each stage
- **Emotions:** The emotional arc — frustration, confusion, delight — at each step
- **Pain Points:** Where friction occurs and users drop off
- **Opportunities:** Where the experience can be improved

### Best Practices

- Base maps on real user data, not internal assumptions
- Focus on the user's perspective, not internal processes
- Combine with JTBD to annotate what "job" the user performs at each stage
- Include both quantitative drop-off data and qualitative emotional insights
- Validate maps with actual users

### AI-Assisted Journey Map Generation

When using AI to draft journey maps from research data, use this structured prompt template:

```
Based on [X] user interview transcripts, generate a journey map for
the persona [Name] performing the job of [JTBD statement].

For each stage, provide:
1. Stage name and user goal
2. Key actions (what they do)
3. Touchpoints (channels/interfaces they interact with)
4. Emotional state (frustrated / neutral / satisfied / delighted)
5. Pain points (friction, confusion, anxiety)
6. Opportunities (design interventions)
7. Branching paths (what happens if they fail at this step?)

Include both the happy path and the primary failure path.
Flag any stages where data is insufficient with [NEEDS VALIDATION].
```

**Critical rule:** AI-generated journey maps are first drafts, not final artifacts. Always validate with actual users and cross-reference with quantitative funnel data.

### Journey Map Template

Use this blank template for each persona-job combination. Fill every cell with research-backed data — mark cells `[NEEDS VALIDATION]` if based on assumption rather than evidence.

```
## Journey Map: [Persona Name] — [Job/Task]
Date: [YYYY-MM-DD] | Based on: [X interviews, Y analytics sources]

| Stage | User Goal | Actions | Touchpoints | Emotion | Pain Points | Opportunities |
|-------|-----------|---------|-------------|---------|-------------|---------------|
| Awareness | [What triggers the need?] | | | | | |
| Consideration | [How do they evaluate options?] | | | | | |
| Onboarding | [First-time setup/entry] | | | | | |
| Core Use | [Primary task execution] | | | | | |
| Repeat Use | [Ongoing engagement] | | | | | |
| Advocacy | [Sharing/recommending] | | | | | |

### Failure Path
| Stage where failure occurs | Failure trigger | User reaction | Recovery path | Design intervention |
|----------------------------|----------------|---------------|---------------|---------------------|
| | | | | |

### Key Metrics per Stage
| Stage | Drop-off rate | Avg. time spent | Satisfaction score | Primary friction |
|-------|--------------|-----------------|--------------------|-----------------|
| | | | | |

### Summary
- Highest-anxiety moment: [stage + why]
- Biggest drop-off point: [stage + data]
- #1 priority fix: [intervention + expected impact]
```

**Adaptation notes:**
- Add or remove stages to match your product's actual flow — the 6 stages above are a starting point, not rigid.
- For B2B products, add "Procurement" and "Admin Setup" stages between Consideration and Onboarding.
- For marketplace products, create separate maps for each side (buyer, seller).

### Worked Example: Journey Map

**Persona:** Mariam, 28, first-time mobile wallet user in Cairo
**Job:** Send money to her mother in Assiut monthly

| Stage | Actions | Touchpoints | Emotion | Pain Points | Opportunities |
|-------|---------|-------------|---------|-------------|---------------|
| **Awareness** | Hears about app from coworker; searches app store | Word of mouth, App Store | Curious, slightly skeptical | Too many wallet apps with similar names; unclear which is trustworthy | Differentiate through trust signals in store listing; show Arabic-first screenshots |
| **Onboarding** | Downloads app, enters phone number, submits national ID photo | App (registration flow) | Anxious → Relieved | ID verification takes 24h; no clear progress indicator; "what happens to my ID photo?" | Add real-time verification status; show data privacy statement upfront; target <5min verification |
| **First Transfer** | Adds mother's phone number, enters amount, confirms | App (send money flow) | Confused → Frustrated | Doesn't understand fee structure; unsure if mother needs the app too; button says "Submit" not "Send" | Show fee breakdown before confirmation; clarify recipient requirements; use action-oriented label "Send 500 EGP to Mama" |
| **Confirmation** | Waits for success screen, screenshots receipt | App (confirmation), SMS | Relieved → Satisfied | No SMS confirmation for 3 minutes; worries money is lost | Instant in-app confirmation + push notification; SMS as backup; show estimated arrival time |
| **Repeat Use** | Opens app monthly, repeats flow | App (home screen) | Neutral → Efficient | Must re-enter amount each time; no "send again" shortcut | Add "repeat last transfer" one-tap action on home screen; saved recipients with nicknames |
| **Advocacy** | Tells mother to tell relatives about the app | WhatsApp, phone calls | Proud → Delighted | No easy way to share/refer; mother struggles to explain the app | In-app referral link with pre-written Arabic message; family group feature |

**Key insight from this map:** The highest-anxiety moment is between "First Transfer" and "Confirmation" — a 3-minute gap where Mariam doesn't know if her money arrived. This is the #1 priority fix because it directly causes churn (analytics show 34% of first-time senders never send again).

---

## The DIKW Pyramid

Extract meaningful insights from raw research:

| Level | Description | Product Example |
|-------|-------------|----------------|
| **Data** | Raw facts, unprocessed | 2,847 support tickets filed last month |
| **Information** | Organized, contextualized | 68% of tickets relate to payment failures |
| **Knowledge** | Patterns and heuristics identified | Payment failures correlate with first-time users on Android in low-connectivity areas |
| **Wisdom** | Value judgments, strategic decisions | Build offline-capable payment confirmation with progressive retry logic |

Complement with Exploratory Data Analysis (EDA): visualize user distributions, identify behavioral trends, spot outliers in product analytics.

---

## Cognitive Prompting for AI Synthesis

When using LLMs to synthesize thousands of qualitative data points, apply this structured reasoning framework (Cognitive Prompting / CP):

### The 8-Step Workflow

1. **Goal Clarification:** Align the AI with the desired outcome
   - "Identify the three primary friction points in our checkout flow based on these 47 interview transcripts"

2. **Decomposition:** Break the dataset into manageable sub-components
   - Group by demographic, by task, by journey stage, or by sentiment

3. **Filtering:** Select only the most relevant information
   - Exclude noisy, off-topic, or duplicate data

4. **Reorganization:** Rearrange data to reveal underlying structures
   - Chronological, thematic, severity-based, or frequency-based ordering

5. **Pattern Recognition:** Identify recurring relationships
   - Connect user problems to known UX heuristics or behavioral patterns

6. **Abstraction:** Extract broader principles from identified patterns
   - "Users with low digital literacy need explicit confirmation at every financial step"

7. **Generalization:** Apply principles to broader user segments
   - Formulate personas or behavioral archetypes from patterns

8. **Integration:** Synthesize into cohesive outputs
   - Unified problem statements, journey maps, or persona documents

---

## Bias Mitigation

### Common Biases in UX Research

- **Confirmation bias:** Seeking data that confirms existing beliefs
- **Framing bias:** How questions are phrased influences responses
- **Survivorship bias:** Only studying current users, ignoring those who left
- **Group attribution bias:** Assuming all members of a group share characteristics

### Self-Help Debiasing for AI

When generating personas or synthesizing research with AI, prompt the model to autonomously rewrite its own instructions to remove bias:

"Before generating this persona, review your instructions for potential biases — framing effects, group attributions, or demographic stereotypes. Rewrite any biased framing, then proceed with the generation."

This ensures AI-generated artifacts reflect diverse user bases without relying on harmful stereotypes.

### Research Bias Prevention

- Triangulate findings across multiple methods (interviews + analytics + surveys)
- Include users who churned or never converted, not just power users
- Use neutral, non-leading interview questions
- Have multiple team members independently analyze the same data
- Document and challenge assumptions explicitly

---

## Affinity Mapping Process

Affinity mapping (also called affinity diagramming or KJ method) is the primary synthesis technique for qualitative data.

### Step-by-Step

1. **Extract observations:** Write each insight, quote, or observation on a separate sticky note (physical or digital). One idea per note. Use the participant's words where possible.

2. **Silent sorting:** Team members silently group notes that feel related. No talking during this phase — it prevents dominant voices from biasing the grouping.

3. **Label clusters:** Once groups stabilize, the team names each cluster with a descriptive theme. The label should capture the insight, not just the topic: "Users fear hidden fees" not "Fees."

4. **Prioritize:** Rank clusters by:
   - **Frequency:** How many participants mentioned this?
   - **Severity:** How much does this block the user's job?
   - **Business impact:** How does this affect conversion, retention, or revenue?

5. **Extract insights:** For each priority cluster, write an insight statement:
   - "We observed [behavior/pattern] among [user segment], which suggests [interpretation] because [evidence]."

### Tips

- Minimum 3 team members for diverse perspective
- Allow 60-90 minutes for a full session
- Digital tools: Miro, FigJam, MURAL
- Physical: actual sticky notes on a wall (often better for first-time teams)
- Don't over-organize — let natural clusters emerge before forcing structure

---

## Stakeholder Interview Guide

Before starting user research, align with internal stakeholders to understand constraints, assumptions, and politics.

### Key Questions

| Question | What You Learn |
|----------|---------------|
| "What does success look like for this project?" | Business goals and KPIs |
| "What do you already know (or think you know) about users?" | Existing assumptions to validate or challenge |
| "What are the business constraints we must work within?" | Budget, timeline, tech, regulatory limits |
| "What would make this project fail?" | Risk factors and organizational politics |
| "Who are the key decision-makers?" | Approval chain and influence map |
| "What has been tried before? What happened?" | History, past failures, institutional knowledge |

### Output

A stakeholder alignment brief (1-2 pages) documenting:
- Agreed business objectives and success metrics
- Known constraints and non-negotiables
- Assumption inventory (to test during research)
- Decision-making process and key approvers
- Timeline and phase expectations
