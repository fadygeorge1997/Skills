# Usability Testing & Validation

## Table of Contents
1. [Testing Methods](#testing-methods)
2. [Conducting Usability Tests](#conducting-usability-tests)
3. [Think-Aloud Protocol](#think-aloud-protocol)
4. [Heuristic Evaluation](#heuristic-evaluation)
5. [Accessibility Audit (WCAG)](#accessibility-audit)
6. [Analyzing and Reporting Results](#analyzing-and-reporting-results)
7. [Iteration Prioritization](#iteration-prioritization)

---

## Testing Methods

### Method Selection Guide

| Method | Setup | Best For | Participants | Time |
|--------|-------|----------|-------------|------|
| **Remote Moderated** | Facilitator + user on video call | Complex tasks, early prototypes, deep insight | 5-8 per segment | 45-60 min each |
| **Remote Unmoderated** | User completes tasks alone, recorded | Specific features, tight timelines, quantitative | 10-30 per segment | 15-30 min each |
| **In-Person Moderated** | Face-to-face in lab or office | Nuanced body language, physical products | 5-8 per segment | 45-60 min each |
| **Guerrilla Testing** | Quick sessions in public spaces | Fast validation, budget constraints | 3-5 quick tests | 5-15 min each |

### When to Use Each

**Remote moderated:** Use when you need to explore "why" users behave a certain way. The facilitator can ask follow-up questions, probe deeper into confusion, and redirect when users get stuck. Best for early-stage prototypes and complex flows.

**Remote unmoderated:** Use when you need to test specific, well-defined tasks at scale. Studies run simultaneously on users' own schedules. Ideal for benchmarking task completion times and error rates on polished prototypes.

**In-person moderated:** Use when body language and physical context matter. Allows observation of hesitation, frustration, and environmental factors. Best for accessibility testing and culturally-sensitive interfaces.

**Guerrilla testing:** Use for quick gut-checks on specific concepts. Uncontrolled environment and non-representative users mean results are directional, not definitive.

---

## Conducting Usability Tests

### Session Structure

**1. Welcome (5 minutes)**
- Introduce yourself and the purpose (testing the product, not the user)
- Explain the process: think aloud, no wrong answers
- Get consent for recording
- Reassure: "If anything is confusing, that's the product's fault, not yours"

**2. Background Questions (5 minutes)**
- Relevant experience with similar products
- Current habits and tools they use
- Comfort level with technology (calibrate expectations)

**3. Task Scenarios (30-40 minutes)**
- Present 4-6 tasks, progressing from simple to complex
- Use realistic scenarios, not instructions: "You want to send EGP 200 to your friend Ahmed for dinner" NOT "Click the Send Money button"
- Observe without intervening unless the user is completely stuck
- Note: time on task, errors, confusion points, successful paths

**4. Post-Task Questions (after each task)**
- "How easy or difficult was that?" (1-7 scale)
- "What did you expect to happen when you tapped [element]?"
- "Is there anything that surprised or confused you?"

**5. Debrief (10 minutes)**
- Overall impressions
- What they liked most/least
- What they would change
- SUS questionnaire (if applicable)

### Facilitator Discipline

- **Do not lead:** "What would you do next?" not "Would you click the blue button?"
- **Do not help:** Let users struggle (within reason) to reveal real friction
- **Do not react:** Maintain neutral expression when users succeed or fail
- **Do not explain:** If users ask "What does this do?" respond with "What do you think it does?"
- **Do probe:** "Tell me more about why you expected that" and "What were you looking for there?"

---

## Think-Aloud Protocol

### Classic Thinking Aloud (Level 1-2)
Users narrate their immediate thoughts as they navigate:
- "I see a green button, I think that's where I pay..."
- "I'm looking for where to check my balance..."
- "This is confusing, I'm not sure what this number means..."

### Level 3 Verbalizations (Deep Insight)
Extract deeper cognitive insights through specific probes:

**Causal Explanations:**
- User explains WHY they took an action
- "I tapped here because I assumed the settings would be under my profile, like in Instagram"

**Problem Formulations:**
- User defines the exact nature of their difficulty
- "The problem is I can't tell whether this fee is per transaction or monthly"

**Recommendations:**
- User suggests an improvement
- "It would be better if the total showed up before I have to enter my PIN"

### When to Use Which

- **Classic:** Standard usability testing, sufficient for most cases
- **Level 3:** When you need to understand decision-making processes, especially for financial or high-stakes interfaces

---

## Heuristic Evaluation

### Process

1. **Select 3-5 evaluators** (UX experts, ideally familiar with the domain)
2. **Brief evaluators** on user personas, context, and key flows
3. **Independent evaluation:** Each evaluator reviews alone, rating each screen against all 10 heuristics
4. **Severity rating** per issue:

| Rating | Severity | Description |
|--------|----------|-------------|
| 0 | Not a problem | Disagreement among evaluators |
| 1 | Cosmetic | Fix if time allows |
| 2 | Minor | Low priority fix |
| 3 | Major | High priority, significant impact on usability |
| 4 | Catastrophic | Must fix before launch |

5. **Consolidate findings:** Merge evaluator reports, resolve duplicates, prioritize
6. **Present to Triad:** Share findings with severity, screenshots, and recommendations

### Typical Issue Distribution

- 3-5 evaluators catch ~75% of usability issues
- A single evaluator catches ~35%
- Expect 30-50 issues from a thorough evaluation of a complex product
- Typically: 5% catastrophic, 25% major, 40% minor, 30% cosmetic

---

## Accessibility Audit

### POUR Framework (WCAG 2.1 Level AA)

**Perceivable** — Users can perceive all information:
- [ ] All images have descriptive alt text
- [ ] Videos have captions and audio descriptions
- [ ] Color contrast ratio meets minimums (4.5:1 for normal text, 3:1 for large text)
- [ ] Information is not conveyed by color alone
- [ ] Text can be resized to 200% without loss of functionality
- [ ] Content is readable and functional without CSS

**Operable** — Users can navigate and interact:
- [ ] All functionality accessible via keyboard (no keyboard traps)
- [ ] Focus order is logical and predictable
- [ ] Focus indicators are visible
- [ ] No content flashes more than 3 times per second
- [ ] Users can pause, stop, or hide moving content
- [ ] Skip navigation links for repetitive content
- [ ] Touch targets are minimum 44x44px

**Understandable** — Content is readable and predictable:
- [ ] Language of page is identified in HTML
- [ ] Abbreviations and jargon are defined
- [ ] Navigation is consistent across pages
- [ ] Form inputs have visible labels (not just placeholders)
- [ ] Error messages identify the field and suggest correction
- [ ] Input purpose is identified for autocomplete

**Robust** — Works across assistive technologies:
- [ ] Valid, semantic HTML
- [ ] ARIA labels used correctly (not overused)
- [ ] Custom components have proper roles and states
- [ ] Tested with screen readers (VoiceOver, TalkBack, NVDA)
- [ ] Tested with keyboard only
- [ ] Tested with screen magnification

### Automated + Manual Testing

**Automated tools catch:** Missing alt text, contrast issues, missing labels, invalid HTML, ARIA misuse
**Manual testing required for:** Logical reading order, meaningful alt text quality, keyboard navigation flow, screen reader experience, cognitive accessibility

Use both: automated tools for broad coverage, manual testing for quality and edge cases.

---

## Analyzing and Reporting Results

### Quantitative Metrics

| Metric | Target | How to Measure |
|--------|--------|---------------|
| **Task completion rate** | >80% for primary flows | Successful completions / total attempts |
| **Time on task** | Benchmark against industry | Stopwatch from task start to completion |
| **Error rate** | <2 errors per task | Count slips (wrong tap) and mistakes (wrong mental model) |
| **SUS score** | >68 (above average) | 10-question standardized questionnaire |
| **Satisfaction (per task)** | >5 on 7-point scale | Post-task rating |

### Qualitative Analysis

1. **Review all session recordings/notes**
2. **Tag observations:** pain point, confusion, delight, suggestion, error
3. **Affinity map:** Group similar observations across participants
4. **Identify patterns:** Issues seen by 3+ participants are systemic
5. **Quote capture:** Collect representative user quotes for each finding
6. **Severity rating:** Assign based on frequency, impact, and persistence

### Report Structure

```
1. Executive Summary (key findings, 3-5 bullets)
2. Methodology (who, what, when, how)
3. Participants (demographics, recruitment criteria)
4. Key Findings (prioritized by severity)
   For each finding:
   - Description
   - Severity rating
   - Frequency (X of Y participants)
   - Supporting evidence (quotes, screenshots)
   - Recommendation
5. Quantitative Summary (metrics table)
6. Positive Findings (what worked well)
7. Next Steps (prioritized action items)
```

---

## Iteration Prioritization

### Impact vs. Effort Matrix

```
         High Impact
              │
    Quick     │    Strategic
    Wins      │    Initiatives
              │
──────────────┼──────────────
              │
    Low       │    Time
    Priority  │    Sinks
              │
         Low Impact
    Low Effort ──────── High Effort
```

### Prioritization Criteria

| Factor | Weight | Assessment |
|--------|--------|-----------|
| **Severity** | High | Is it catastrophic, major, minor, or cosmetic? |
| **Frequency** | High | How many users encountered this? |
| **Impact on conversion** | High | Does it block task completion or just slow it? |
| **Development effort** | Medium | How long to fix? |
| **User expectation** | Medium | How frustrated are users? |
| **Business alignment** | Medium | Does fixing this support business goals? |

### Iteration Process

Follow the Lean UX Think > Make > Check loop:
1. **Think:** Formulate hypotheses about which changes will improve the experience
2. **Make:** Create the minimum prototype needed to test the hypothesis
3. **Check:** Test with users, measure against hypothesis, learn

Start with high-impact, low-effort fixes. Track improvements across iterations using the same metrics.

### Validation Anti-Patterns

| Anti-Pattern | Why It's Dangerous | Fix |
|-------------|-------------------|-----|
| **White/able-bodied default** | Testing only with tech-savvy, non-disabled users misses critical accessibility and usability issues | Recruit participants with diverse abilities, tech literacy levels, and cultural backgrounds |
| **"Research takes too long"** | Skipping validation to hit a deadline — the most expensive shortcut in product development | Even 3 guerrilla tests in a day reveal blockers. No test = blind launch. |
| **Confirmation bias in analysis** | Interpreting ambiguous results as confirming the team's existing beliefs | Have someone outside the design team review findings independently |
| **Testing ideal conditions only** | Testing on fast WiFi, latest phone, fully populated account | Test on constrained devices, slow networks, empty accounts, edge-case data |
| **Celebrating the positive** | Reporting only what worked well and burying the problems | Lead every report with problems ranked by severity; celebrate wins separately |
| **Stakeholder-only testing** | Showing the prototype to executives and calling it "tested" | Stakeholders are not users. Internal demos are alignment, not validation. |

### Phase Transition Signals — Validation

Definition of Done before handing off to engineering:

- [ ] Usability testing completed with ≥5 participants per target segment
- [ ] Task completion rate >80% on all primary flows
- [ ] No Severity 4 (catastrophic) issues remaining
- [ ] All Severity 3 (major) issues either fixed or documented with mitigation plan
- [ ] SUS score ≥68 (above average)
- [ ] Heuristic evaluation completed by 3-5 evaluators
- [ ] WCAG 2.1 Level AA accessibility audit passed (automated + manual)
- [ ] Human-AI interaction patterns validated (if applicable)
- [ ] Design works with realistic data across all target breakpoints/devices
- [ ] "Empty state" and "error state" designs tested with users
- [ ] Handoff documentation walked through with lead developer

---

## Participant Recruitment

### How Many Participants

| Study Type | Minimum | Ideal | Rationale |
|-----------|---------|-------|-----------|
| **Qualitative usability** | 5 per segment | 5-8 | Nielsen's research: 5 users find ~85% of usability issues |
| **Card sorting** | 15 | 20-30 | Need statistical stability in grouping patterns |
| **A/B testing** | Varies | Use power calculator | Depends on baseline conversion and minimum detectable effect |
| **Survey** | 30 | 100+ | 30 for trends, 100+ for statistical significance |
| **Accessibility** | 3-5 per disability type | 5+ | Include range of assistive technologies |

### Screening Criteria

Define a screener that filters for your target users:

**Must-have criteria (hard filters):**
- Demographics matching your persona (age, location, device)
- Relevant experience level (e.g., "uses mobile banking at least weekly")
- Technology access (e.g., "owns an Android device")
- Language (e.g., "primary language is Arabic")

**Nice-to-have criteria (soft filters):**
- Mix of genders, ages within target range
- Range of tech literacy levels
- Mix of competitor users and non-users
- Both urban and rural if relevant

**Disqualification criteria:**
- Works in UX, design, or market research (professional bias)
- Works for a direct competitor
- Participated in research for your product in the last 6 months
- Cannot meet technical requirements (device, connectivity, software)

### Participant Screener Template

Use this template to build a screening survey. Distribute via Google Forms, Typeform, or email. Score responses to rank candidates.

```
## Screener: [Study Name]
Target: [N] participants | Study dates: [range] | Compensation: [amount]

### Section 1: Demographics
Q1. What is your age? [dropdown: 18-24, 25-34, 35-44, 45-54, 55+]
    Target: [specify range]

Q2. Where do you live? [open text or dropdown by region]
    Target: [specify locations]

Q3. What is your primary language? [dropdown]
    Target: [specify]

### Section 2: Behavioral Filters
Q4. How often do you [relevant behavior, e.g., "send money digitally"]?
    [ ] Daily
    [ ] Weekly        ← Target
    [ ] Monthly       ← Target
    [ ] Rarely
    [ ] Never         ← Disqualify

Q5. Which of the following products have you used? (Select all that apply)
    [ ] [Competitor A]
    [ ] [Competitor B]
    [ ] [Your product]
    [ ] None of these
    Target: Mix of competitor users and non-users

Q6. What device do you primarily use for [activity]?
    [ ] iPhone
    [ ] Android phone  ← Target (if testing Android)
    [ ] Tablet
    [ ] Desktop/Laptop
    Target: [specify]

### Section 3: Disqualification
Q7. Do you or does anyone in your household work in any of these fields?
    [ ] UX Design / User Research
    [ ] Market Research
    [ ] [Your company name]
    [ ] [Competitor company names]
    [ ] None of the above  ← Required to proceed

Q8. Have you participated in a research study for [product] in the past 6 months?
    [ ] Yes  ← Disqualify
    [ ] No

### Section 4: Logistics
Q9. Are you available for a [duration]-minute session between [dates]?
Q10. Do you have reliable [internet/device] access for a remote session?

### Scoring
- Meets all must-have criteria: +3 points
- Meets each nice-to-have criterion: +1 point
- Increases demographic diversity of current pool: +1 point
- Rank by score, select top N + 2 backups
```

### Recruitment Channels

| Channel | Speed | Cost | Quality |
|---------|-------|------|---------|
| **User panel services** (UserTesting, dscout, Respondent) | Fast (days) | Medium-high | Good for general demographics |
| **Your own user base** | Medium (1-2 weeks) | Low | Best for existing users; biased toward engaged users |
| **Social media** | Fast | Low | Wide reach but screening burden is high |
| **Intercept (in-app)** | Fast | Low | Real users in natural context; limited control |
| **Professional recruiters** | Slow (2-3 weeks) | High | Best for niche demographics |
| **Community groups** | Medium | Low | Good for specific cultural/regional research |

### Compensation Guidelines

Compensate fairly — participants are giving you their time and expertise:
- 30-minute session: $30-50 USD equivalent
- 60-minute session: $50-100 USD equivalent
- Diary study (1 week): $100-200 USD equivalent
- Adjust for local purchasing power (Egypt: EGP 500-1000 for 60 min is generous)
- Offer gift cards, mobile credit, or cash — whatever works in your market
- Pay even if the session ends early or the participant isn't a good fit

---

## Consent & Ethics

### Informed Consent Template

```
RESEARCH PARTICIPATION CONSENT

Study: [Study name]
Researcher: [Name, Organization]

Purpose: We are testing [product/prototype] to understand how people
use it. We are evaluating the product, not you — there are no wrong
answers.

What you'll do: [Brief description of tasks, duration]

Recording: This session will be [audio/video/screen] recorded for
research purposes only. Recordings will be [stored securely / deleted
after analysis / may be shared with the product team].

Your data: Your personal information will be kept confidential.
Research findings will be reported anonymously. We will never share
your name or identifying details publicly.

Voluntary: Your participation is entirely voluntary. You may stop at
any time, skip any question, or withdraw without penalty. You will
still receive your compensation.

Questions? Contact [researcher email/phone].

[ ] I agree to participate in this study
[ ] I agree to be [audio/video/screen] recorded

Name: ___________________
Date: ___________________
Signature: ___________________
```

### Ethical Guidelines

- **Never deceive:** Be honest about the study's purpose. If you can't reveal everything upfront, debrief fully afterward
- **Protect vulnerable users:** Extra care with children, elderly, financially distressed, or users with disabilities
- **Right to withdraw:** Make it genuinely easy to stop. Watch for discomfort signals
- **Data minimization:** Collect only what you need. Delete recordings when analysis is complete
- **Cultural sensitivity:** In MENA contexts, consider gender-separated sessions if needed; respect religious observance schedules; ensure Arabic consent forms are available

### Inclusive Testing Checklist

Beyond standard usability, verify the design doesn't exclude:

- [ ] **Screen reader users:** Test full flows with VoiceOver (iOS), TalkBack (Android), NVDA (Windows)
- [ ] **Keyboard-only users:** Complete all tasks without mouse or touch
- [ ] **Low vision users:** Test at 200% zoom; verify contrast ratios
- [ ] **Motor impairment:** Test with switch access; verify target sizes ≥44x44px
- [ ] **Cognitive accessibility:** Test with users who have varying literacy levels; simplify language
- [ ] **Low bandwidth/constrained devices:** Test on 3G network and budget devices (not just flagship phones)
- [ ] **Multilingual:** Test with Arabic/RTL, transliterated names, mixed-script content
- [ ] **New-to-digital users:** Test with participants who have minimal smartphone experience (critical for emerging markets)

---

## Remote Testing Tools

### Platform Comparison

| Tool | Type | Strengths | Limitations |
|------|------|-----------|------------|
| **UserTesting** | Unmoderated + moderated | Large panel, video recording, highlight reels | Expensive; panel skews Western |
| **Maze** | Unmoderated | Quantitative task analytics, heatmaps, Figma integration | Limited qualitative depth |
| **Lookback** | Moderated + unmoderated | Live observation, team notes, mobile testing | Smaller panel; more manual |
| **dscout** | Diary studies + missions | Longitudinal research, mobile-first | Expensive; learning curve |
| **Optimal Workshop** | Card sorting, tree testing | Purpose-built for IA research | Limited to specific methods |
| **Hotjar/FullStory** | Session recording, heatmaps | Production usage data, no recruitment needed | Observational only; no task framing |
| **Zoom/Teams** | Moderated | Free/cheap, familiar, screen share | No built-in analysis tools |

### DIY Remote Testing Stack (Budget-Friendly)

For teams without dedicated research tool budgets:
1. **Recruitment:** Google Forms screener → schedule via Calendly
2. **Session:** Zoom with cloud recording + screen share
3. **Consent:** DocuSign or simple email confirmation
4. **Notes:** Shared Google Doc with timestamped observations
5. **Analysis:** FigJam for affinity mapping observations
6. **Reporting:** Notion or Google Slides for findings

---

## Moderation Script Template

### Pre-Session Checklist

```
Before the participant joins:
- [ ] Recording software running and tested
- [ ] Prototype loaded and at starting screen
- [ ] Task scenarios printed or on second screen
- [ ] Note-taking template open
- [ ] Backup plan if technology fails (phone call, reschedule)
- [ ] Consent form ready (send before or display at start)
- [ ] Timer ready
```

### Script

```
INTRODUCTION (5 min)
────────────────────
"Hi [Name], thanks for joining today. My name is [Name] and I'm
a [role] at [company].

Today we're going to look at [product/prototype]. I want to
emphasize: we're testing the product, not you. There are no wrong
answers or actions. If something is confusing, that's really
valuable feedback for us.

I'll ask you to complete a few tasks and share your thoughts out
loud as you go. Feel free to say anything — what you're looking
at, what you expect, what's confusing. The more you share, the
more we learn.

This session will take about [X] minutes. You can stop at any
time or skip anything you're not comfortable with.

Do you have any questions before we begin?

[Get verbal consent for recording if not already obtained]

WARM-UP (5 min)
────────────────
"Before we look at the product, I'd like to learn a bit about you.

- Can you tell me about the last time you [relevant activity]?
- What tools or apps do you currently use for [domain]?
- How comfortable are you with [relevant technology]?"

TASKS (30-40 min)
─────────────────
[For each task, read the scenario verbatim]

"Imagine you [realistic scenario]. Using this [app/prototype],
show me how you would [goal]. Please think out loud as you go."

[After each task:]
"On a scale of 1-7, how easy or difficult was that?
What, if anything, confused you?
What did you expect to happen when you [specific action]?"

PROBING QUESTIONS (use as needed)
─────────────────────────────────
- "What are you looking for right now?"
- "What do you think that [element] does?"
- "You paused there — what were you thinking?"
- "Was there anything you expected to see that wasn't there?"
- "How does this compare to [competitor/current solution]?"

DEBRIEF (10 min)
────────────────
"We're done with the tasks. I have a few final questions:

- What was your overall impression of [product]?
- What stood out as the best part of the experience?
- What was the most frustrating part?
- If you could change one thing, what would it be?
- Is there anything else you'd like to share?"

CLOSING
───────
"Thank you so much for your time today. Your feedback is
incredibly valuable and will directly shape how we improve
this product. [Explain compensation process]. Do you have
any final questions for me?"
```

### Observer Note-Taking Template

```
Participant: [ID, not name]
Date: [Date]
Facilitator: [Name]
Observer: [Name]

| Time | Task | Observation | Type | Severity |
|------|------|-------------|------|----------|
| 2:05 | Task 1 | Looked for send button in top nav first | Confusion | Minor |
| 2:08 | Task 1 | "Oh, it's down here" — found it in bottom bar | Recovery | — |
| 2:15 | Task 2 | Couldn't find fee info, asked "Is this free?" | Pain point | Major |
| ... | ... | ... | ... | ... |

Types: Confusion, Pain point, Delight, Suggestion, Error, Recovery, Quote
Severity: Critical, Major, Minor, Cosmetic, Positive
```
