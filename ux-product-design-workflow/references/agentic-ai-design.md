# Agentic AI Design Patterns & Human-AI Interaction

## Table of Contents
1. [Core Agentic Design Patterns](#core-agentic-design-patterns)
2. [Human-AI Interaction Guidelines](#human-ai-interaction-guidelines)
3. [Explainable AI (XAI) in UX](#explainable-ai-in-ux)
4. [Multi-Agent Collaboration UX](#multi-agent-collaboration-ux)
5. [AI Integration by Phase](#ai-integration-by-phase)
6. [Future-Proofing the UX Role](#future-proofing-the-ux-role)
7. [Design Checklist for AI Features](#design-checklist-for-ai-features)

---

## Core Agentic Design Patterns

As AI evolves from single-turn chatbots to goal-driven autonomous agents capable of planning, reasoning, and collaborating, product designers must adapt to this architectural shift.

### The Planning Pattern (Plan-Act-Reflect)

Agentic AI operates by breaking down complex goals into sub-tasks. The UX must make this internal planning visible and controllable.

**Design requirements:**
- Display the generated plan before execution begins
- Allow users to intervene, approve, modify, or reject steps
- Show clear progress through the plan's execution
- Enable pausing and resuming at any step
- Provide rollback capability for completed steps

**Example flow:**
```
User goal: "Analyze my Q4 expenses and suggest budget optimizations"

Agent Plan (shown to user):
  1. Retrieve Q4 transaction data ✓
  2. Categorize expenses by type ← Currently here
  3. Compare against Q3 and industry benchmarks
  4. Identify top 5 optimization opportunities
  5. Generate recommendation report

[Pause] [Modify Plan] [Skip Step] [Cancel]
```

### The Tool Use Pattern

Agents interact with external databases, APIs, and services. The UX must communicate what the agent is doing and why.

**Design requirements:**
- Visually distinguish when the agent is retrieving data vs. generating text
- Show which tools/sources the agent is consulting
- Display data provenance: "Based on data from [source] retrieved at [time]"
- Never trust a single-shot answer blindly — build verification into the flow

### The Reflection Pattern

Agents should evaluate their own outputs before presenting them. The UX should surface this self-evaluation.

**Design requirements:**
- Show confidence indicators where appropriate (not false precision)
- Flag areas of uncertainty: "I'm less certain about this recommendation because..."
- Provide the reasoning chain, not just the conclusion
- Allow users to request deeper analysis on specific points

### Confidence Scoring System

When AI agents present recommendations to users, use a tiered confidence indicator rather than false-precision percentages:

| Indicator | Level | Meaning | UX Treatment |
|-----------|-------|---------|-------------|
| 🟢 | **High confidence** | Strong evidence, well-established pattern | Present as recommendation; user can accept directly |
| 🟡 | **Moderate confidence** | Some evidence, reasonable inference | Present as suggestion with reasoning; prompt user review |
| 🔴 | **Low confidence** | Limited data, novel situation, high uncertainty | Present as possibility; require user verification before acting |

**Design rules for confidence display:**
- Never show numeric confidence percentages to end users (creates false precision)
- Color + label + explanation is more effective than numbers
- Higher stakes = more conservative display (show 🟡 even when model says 85%)
- Always accompany confidence with reasoning: "I'm suggesting X because Y"
- Allow users to drill into the basis for confidence when needed

### Progressive Disclosure for AI Guidance

Structure AI output in tiers so users get the depth they need, not more:

**Tier 1: Action summary** (always visible)
- One-sentence recommendation with confidence indicator
- "🟢 I recommend splitting the onboarding into 3 steps to reduce drop-off."

**Tier 2: Supporting rationale** (expandable)
- Key evidence and reasoning
- "Based on your analytics showing 62% drop-off at step 4, and industry benchmarks showing 3-step onboarding has 28% higher completion."

**Tier 3: Detailed analysis** (on demand)
- Full data, methodology, alternatives considered, limitations
- Comparable to an analyst's report — available but not forced

---

## Human-AI Interaction Guidelines

These standards ensure AI features maintain user trust and usability.

### Transparency and Scoping

**What the system can do:**
- Clearly communicate AI capabilities AND limitations upfront
- "I can analyze your transaction patterns, but I cannot access real-time market data"
- Set expectations about accuracy and error likelihood

**Scoping services when uncertain:**
- When the AI is unsure about user intent, engage in disambiguation
- "Did you mean [option A] or [option B]?"
- Gracefully degrade output rather than hallucinating
- If the AI cannot perform a task, say so clearly and suggest alternatives

### Error Recovery

**Efficient correction mechanisms:**
- Users can easily edit, refine, or dismiss AI suggestions
- Inline editing of AI-generated content without starting over
- "Undo" for AI actions that modified user data
- History of AI actions for review and selective reversal

**Error communication:**
- Acknowledge errors promptly and specifically
- Explain what went wrong in user terms
- Suggest next steps for recovery
- Don't blame the user for AI misunderstandings

### Learning and Personalization

**Adaptive behavior:**
- Learn from user corrections to improve future suggestions
- Communicate when the system has learned: "I've noted your preference for..."
- Allow users to view and manage what the AI has learned about them
- Provide controls to reset or delete learned preferences

**Boundaries:**
- Never change user data or settings without explicit permission
- Distinguish between "suggestion" and "action"
- AI recommendations should be clearly separate from user decisions

### Feedback Mechanisms

- Thumbs up/down on AI outputs for quality signaling
- "Not helpful" or "Incorrect" flags with optional detail
- Feedback should feel lightweight, not like a chore
- Show that feedback has impact: "Thanks, we'll improve this"

---

## Explainable AI (XAI) in UX

Transparency is critical — users must understand the rationale behind AI decisions, especially in financial or health-related products.

### Levels of Explanation

**Level 1: What happened**
- "We flagged this transaction as unusual"
- Simple, clear statement of the AI's action

**Level 2: Why it happened**
- "This transaction was flagged because it's 3x larger than your average spending in this category"
- Provides the primary reason in user terms

**Level 3: How the decision was made**
- Feature importance visualization (simplified SHAP-like display)
- "Factors considered: transaction amount (high impact), location (medium), time of day (low)"
- For advanced users or regulatory compliance

### Design Patterns for XAI

**Confidence visualization:**
- Avoid numeric percentages (false precision); use qualitative labels
- "High confidence" / "Moderate confidence" / "Low confidence — verify manually"
- Use color and visual weight to communicate certainty levels

**Reasoning chains:**
- Expandable/collapsible explanation sections
- "Show me why" links on AI recommendations
- Step-by-step breakdowns for complex decisions

**Comparison explanations:**
- "We recommended Plan A over Plan B because..."
- Side-by-side factor comparison
- Highlight the decisive factors

### When Explainability Matters Most

- Financial decisions (loan approvals, spending recommendations)
- Healthcare recommendations
- Content filtering or moderation decisions
- Any action with significant consequences
- Regulatory compliance requirements

---

## Multi-Agent Collaboration UX

Future systems will feature specialized agents working together. The UI must make this collaboration transparent.

### Visual Clarity

- **Active agent indicator:** Show which agent is currently working
- **Agent roles:** Label each agent's specialization ("Research Agent," "Analysis Agent")
- **Handoff visualization:** Clearly show when one agent passes work to another
- **State tracking:** What information each agent holds and has passed along

### Conflict Resolution

When multiple agents disagree:
- Surface the disagreement transparently
- Show each agent's reasoning
- Let the user decide or set resolution preferences
- Don't hide disagreements behind a false consensus

### Orchestration Visibility

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Research    │────>│  Analysis   │────>│  Report     │
│  Agent       │     │  Agent       │     │  Agent       │
│  Finding...  │     │  Waiting     │     │  Waiting     │
└─────────────┘     └─────────────┘     └─────────────┘
     ↑
  [Your data]

Status: Research Agent is gathering market data from 3 sources
Estimated completion: ~2 minutes
```

---

## AI Integration by Phase

### Discovery Phase
- **Transcription & synthesis:** AI transcribes interviews, auto-generates summaries, extracts key themes
- **Social listening:** Continuous monitoring of social channels for sentiment, complaints, viral pain points
- **Pattern recognition:** AI clusters qualitative data, identifies non-obvious connections
- **Research planning:** AI suggests methodologies, generates screening criteria

### Define Phase
- **Cognitive prompting:** Structured AI synthesis of qualitative data (see discovery-synthesis.md)
- **Persona generation:** AI creates initial personas from research data (with bias checks)
- **Journey map drafting:** AI generates journey maps from interview insights
- **Problem framing:** AI transforms pain points into structured problem statements

### Ideate Phase
- **Brainstorming co-pilot:** Chain-of-thought reasoning for solution generation
- **User flow variations:** AI generates multiple architectural approaches
- **Concept evaluation:** AI evaluates ideas against defined constraints and heuristics

### Design Phase
- **Layout generation:** AI generates UI layouts from text prompts or wireframes
- **Component assembly:** AI reads design tokens and component libraries to build compliant UIs
- **Localization:** AI generates culturally aware Arabic copy, tests RTL text elasticity
- **Micro-copy:** AI drafts button labels, error messages, empty states, onboarding text

### Validate Phase
- **Session analysis:** AI analyzes usability test logs, performs intent identification and entity extraction
- **Documentation automation:** AI generates Jira tickets from prototype test recordings
- **Adversarial debiasing:** AI tests models for discriminatory patterns, reweights samples
- **Accessibility scanning:** AI evaluates interfaces against WCAG criteria

### Optimize Phase
- **Anomaly detection:** AI flags unexpected metric drops without manual SQL querying
- **Agentic experimentation:** Bounded AI proposes micro-optimizations under human governance
- **Cohort analysis automation:** AI identifies significant differences across user segments
- **Churn prediction:** AI models identify at-risk users for proactive intervention

---

## Future-Proofing the UX Role

As AI assumes more generative and analytical tasks, UX practitioners evolve into "Architects of Human-AI Collaboration."

### New Competencies

- **AI literacy:** Working grasp of how AI systems learn, fail, and retain memory
- **Prompt design:** Crafting effective system prompts and user-facing AI interactions
- **Orchestrated sensemaking:** Architecting feedback systems that triangulate signals across massive data streams
- **Ecosystem design:** Ensuring human governance, ethical boundaries, and usability heuristics remain at the core
- **Observability architecture:** Designing transparency layers so users always understand what AI is doing

### The Shift

From: Designing screens and interactions
To: Designing systems where humans and AI collaborate to solve complex problems

This means:
- UX research includes studying how users interact with AI features
- Design systems include AI-specific components (explanation widgets, confidence indicators, feedback mechanisms)
- Usability testing includes AI behavior evaluation
- Metrics include AI-specific dimensions (trust, transparency, correctness perception)

---

## Design Checklist for AI Features

### Before Launch
- [ ] AI capabilities and limitations clearly communicated to users
- [ ] Disambiguation flow for ambiguous user intents
- [ ] Graceful degradation when AI is uncertain or fails
- [ ] Error recovery: users can easily undo/edit AI actions
- [ ] Explanation available for AI decisions (appropriate level of detail)
- [ ] Confidence indicators used where applicable (not false precision)
- [ ] User control: can approve, reject, or modify AI suggestions before execution
- [ ] Privacy: users understand what data AI accesses and stores
- [ ] Bias testing completed across user segments
- [ ] Feedback mechanism for users to rate AI quality

### During Operation
- [ ] Active agent/tool use is visible to the user
- [ ] Progress and status are communicated for long-running AI tasks
- [ ] Data provenance is displayed ("Based on data from...")
- [ ] Users can pause, cancel, or modify AI operations in progress
- [ ] AI-generated content is visually distinguishable from user content

### Continuous Improvement
- [ ] User feedback on AI quality is collected and analyzed
- [ ] AI accuracy metrics are tracked alongside UX metrics
- [ ] Bias monitoring runs on production outputs
- [ ] Model updates are tested for UX regression
- [ ] Trust metrics (user confidence in AI) are measured over time

---

## Conversational UX Patterns

### When to Use Conversational UI

Conversational interfaces (chatbots, voice assistants, AI copilots) are appropriate when:
- The task is exploratory and doesn't have a fixed structure
- Users need guidance through a complex decision
- The domain has high variability in user intents
- Natural language is more efficient than navigating menus

They are NOT appropriate when:
- The task is repetitive and well-structured (use forms)
- Speed matters more than flexibility (use direct manipulation)
- The user needs to compare options visually (use tables/cards)
- Precision is critical (use structured inputs)

### Conversation Design Principles

**Turn-taking clarity:**
- Make it obvious when the AI is "thinking" vs. waiting for user input
- Use typing indicators, progress animations, or status messages
- Don't leave the user wondering if the system heard them

**Memory and context:**
- Reference earlier parts of the conversation naturally: "Earlier you mentioned..."
- Don't ask for information the user already provided
- Show what the AI remembers in an accessible way (conversation sidebar, context panel)

**Repair mechanisms:**
- "I didn't understand that. Did you mean A or B?"
- Let users rephrase without losing context
- Offer structured fallbacks when free-text fails (quick-reply buttons)

**Conversation flow patterns:**

| Pattern | Description | Example |
|---------|-------------|---------|
| **Slot filling** | Gathering required info piece by piece | "What amount?" → "To whom?" → "From which account?" |
| **Disambiguation** | Resolving ambiguity in user intent | "Did you mean Ahmed in your contacts or Ahmed's store?" |
| **Progressive refinement** | Narrowing down through follow-ups | "What kind of chart? Bar, line, or pie?" |
| **Proactive suggestion** | AI offers next steps before asked | "Would you also like to set a reminder for this payment?" |
| **Graceful handoff** | AI recognizes its limits and escalates | "This looks like a disputed charge. Let me connect you with support." |

### Multi-Modal Conversations

Modern AI interfaces blend conversation with visual elements:
- Show a chart alongside an explanation
- Display interactive cards within the conversation flow
- Allow users to switch between typing and clicking
- Use conversation for exploration, then transition to structured UI for action

---

## Prompt Design for UX

### System Prompt Architecture

When designing AI features, the system prompt is the invisible UX layer. Treat it with the same rigor as visual design:

**Persona definition:**
- Define the AI's voice, tone, and personality
- Specify formality level (match the product's brand)
- Set boundaries: what the AI should and shouldn't say

**Behavioral constraints:**
- Response length guidelines (concise for mobile, detailed for analysis)
- When to ask clarifying questions vs. make assumptions
- How to handle off-topic requests
- Error acknowledgment style

**Output formatting:**
- Structured output for predictable UI rendering
- Consistent formatting across response types
- Support for mixed content (text + data + actions)

### Prompt Engineering for Non-Technical Teams

UX designers should be able to iterate on AI behavior without engineering:

| Adjustment | Prompt Technique | Example |
|-----------|-----------------|---------|
| Make responses shorter | Add length constraint | "Respond in 2-3 sentences maximum" |
| Add warmth | Adjust persona | "Respond in a friendly, encouraging tone" |
| Improve Arabic | Specify dialect | "Use Egyptian colloquial Arabic (Ammiya) for casual guidance" |
| Add structure | Define format | "Always respond with: Summary, Details, Next Steps" |
| Reduce hallucination | Add grounding | "Only reference data from the user's transaction history. If unsure, say so." |

### UX Review of AI Outputs

AI-generated content should go through UX review just like any other copy:
- Does the tone match the product's voice?
- Is the reading level appropriate for the audience?
- Are technical terms explained or avoided?
- Does the response length fit the context (mobile screen, notification, full page)?
- Is the AI honest about uncertainty?

---

## AI Error Pattern Catalog

### Common AI Failure Modes and UX Responses

| Failure Mode | What Happens | UX Response Pattern |
|-------------|-------------|-------------------|
| **Hallucination** | AI generates plausible but false information | Show source citations; add "Verify this" prompts; never show financial data without source |
| **Overconfidence** | AI presents uncertain results as definitive | Use hedging language; show confidence levels; add "I'm not sure about..." framing |
| **Context loss** | AI forgets earlier conversation context | Show context summary panel; allow users to "remind" the AI; indicate context window limits |
| **Latency spike** | AI takes much longer than expected | Progressive loading; show "still working" after 3s; offer to notify when done |
| **Partial failure** | AI completes some tasks but not others | Show what succeeded and what failed separately; allow retry of failed portions only |
| **Bias leak** | AI output reflects training data biases | Run bias checks pre-launch; monitor for patterns post-launch; offer feedback mechanism |
| **Misinterpretation** | AI understood the request differently than intended | Confirm interpretation before acting; show "I understood this as..." preview |
| **Rate limiting** | Too many requests hit API limits | Queue requests gracefully; show position in queue; degrade to cached responses |

### Error Recovery Hierarchy

1. **Prevent:** Design prompts and guardrails that minimize errors
2. **Detect:** Monitor for error patterns in production
3. **Communicate:** Tell the user clearly what happened
4. **Recover:** Offer a clear path forward (retry, rephrase, escalate)
5. **Learn:** Feed error data back into prompt improvements

---

## Trust Calibration

### The Trust Lifecycle

User trust in AI follows a predictable arc that UX must manage:

```
Trust Level
    │
    │          Overreliance
    │         ╱ danger zone
    │    ●───●
    │   ╱     ╲         Calibrated
    │  ╱       ╲       ╱ trust
    │ ╱         ●─────●──────────
    │╱           ╲   ╱
    ●             ●─●
    │        First failure
    │        (trust dip)
    └────────────────────────────── Time
   Initial   Honeymoon  Calibration  Stable
```

**Initial skepticism:** Users don't trust AI. Show quick wins and be transparent.
**Honeymoon phase:** After first success, users over-trust. Build in verification.
**First failure:** Trust drops sharply. How you handle errors determines recovery.
**Calibration:** Users learn the AI's real capabilities. Support accurate mental models.
**Stable trust:** Users know when to trust and when to verify. This is the goal.

### Design for Appropriate Trust

**Prevent over-trust:**
- Don't hide AI limitations behind confident language
- Add friction before high-stakes AI actions (confirmation screens)
- Show reasoning, not just conclusions
- Include "I might be wrong about..." where appropriate
- Don't anthropomorphize excessively (avoid "I know" when the AI is inferring)

**Prevent under-trust:**
- Show track record: "This type of recommendation has been accurate 94% of the time"
- Allow low-stakes experimentation before high-stakes reliance
- Build trust incrementally: get small things right before offering big suggestions
- Show the AI's data sources to build credibility

**Trust repair after failures:**
- Acknowledge the error explicitly and promptly
- Explain what went wrong (not just "Something went wrong")
- Show what's been done to prevent recurrence
- Give the user more control temporarily (more confirmation steps)
- Track trust recovery through behavioral metrics (do users resume using the feature?)

### Measuring Trust

| Metric | How to Measure | What It Tells You |
|--------|---------------|------------------|
| **Adoption rate** | % users who try AI features | Initial willingness to trust |
| **Override rate** | % of AI suggestions users modify | Trust calibration accuracy |
| **Verification rate** | % of AI outputs users double-check | Whether trust is appropriate |
| **Recovery rate** | % users who return after AI error | Trust resilience |
| **Escalation rate** | % users who bypass AI for human help | Trust ceiling |
| **Survey: perceived accuracy** | Self-reported accuracy belief | Subjective trust level |

---

## AI Behavioral Guidance Framework

### Defining AI Agent Personas for Products

When building AI features, define the agent's behavioral parameters the same way you'd define a design system — systematically, not ad hoc:

**Role definition:**
```
Role: Senior [domain] Advisor
Tone: Professional but approachable. Use clear, jargon-free language.
Boundaries: Never provide definitive financial/medical/legal advice.
Always present as "guidance" or "suggestion," not prescription.
```

**Behavioral constraints:**
- **Response length:** Concise for mobile (2-3 sentences), detailed for analysis views
- **Clarification threshold:** If user intent is <80% clear, ask before acting
- **Off-topic handling:** Acknowledge, redirect gently, stay within product scope
- **Error style:** "I wasn't able to find that. Here's what I can help with..." (not "Error 404")
- **Cultural adaptation:** Match dialect, formality, and communication norms to the target market

### AI Ethics Baseline

Before shipping any AI feature, verify:

- [ ] AI does not discriminate based on protected characteristics (gender, race, religion, disability)
- [ ] Training data has been audited for bias (gender, geographic, socioeconomic)
- [ ] Users can opt out of AI features without losing core product functionality
- [ ] AI decisions in high-stakes domains (finance, health) have human review paths
- [ ] Data retention and usage policies are transparent and user-controllable
- [ ] The AI never impersonates a human without disclosure
- [ ] Dark patterns (manipulative AI persuasion, artificial urgency) are explicitly prohibited

### Ethical Design Hierarchy

Modeled on Maslow's hierarchy — lower levels must be satisfied before pursuing higher ones:

```
         ┌─────────────┐
         │   DELIGHT    │  Emotional resonance, surprise & joy
         │  (Level 3)   │  Only pursue when Levels 1-2 are solid
         ├─────────────┤
         │ FUNCTIONALITY│  Usability, performance, reliability
         │  (Level 2)   │  The product works well for its purpose
         ├─────────────┤
         │ HUMAN RIGHTS │  Accessibility, privacy, security, inclusivity
         │  (Level 1)   │  Non-negotiable baseline. Ship nothing that
         │              │  compromises safety, access, or dignity.
         └─────────────┘
```

**Application:** Never sacrifice accessibility for aesthetics. Never sacrifice privacy for personalization. Never sacrifice safety for speed-to-market. The hierarchy is non-negotiable.
