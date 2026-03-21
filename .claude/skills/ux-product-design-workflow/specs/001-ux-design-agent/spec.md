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

---

## Appendix G: Complete Tooling & Integration Ecosystem

The UX agent leverages a layered ecosystem of skills, MCP servers, browser automation tools, and specialized agents. Each phase maps to specific tooling that the agent SHOULD invoke when available.

### Tier 1: MCP Server Tools (Direct Integration)

These tools are invoked programmatically when the corresponding MCP server is connected:

| MCP Server | Key Tools | Phase(s) | Use Case |
|------------|-----------|----------|----------|
| **AccessLint** | `audit_url`, `audit_html`, `audit_file`, `diff_html`, `list_rules` | 5 (Validate), 6 (Handoff) | Automated WCAG accessibility auditing of prototypes and live pages |
| **Playwright** | `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_fill_form`, `browser_take_screenshot`, `browser_evaluate` | 4 (Prototype), 5 (Validate) | Automated browser testing, interaction flow verification, visual regression |
| **Chrome DevTools** | `lighthouse_audit`, `take_screenshot`, `take_snapshot`, `performance_start_trace`, `performance_stop_trace`, `list_network_requests` | 4 (Prototype), 5 (Validate), 7 (Optimize) | Performance auditing (Lighthouse), CWV measurement, network analysis |
| **Claude Preview** | `preview_start`, `preview_screenshot`, `preview_click`, `preview_fill`, `preview_console_logs` | 4 (Prototype), 5 (Validate) | Live preview of HTML prototypes, interactive testing |
| **shadcn-ui** | `list_items_in_registries`, `get_item_examples_from_registries`, `search_items_in_registries`, `get_audit_checklist` | 3 (IA), 4 (Prototype) | Component library lookup, design system alignment, audit checklists |
| **shadcn-community** | `list_components`, `get_component`, `get_component_demo`, `list_themes`, `apply_theme` | 4 (Prototype) | Community component discovery, theme exploration |
| **Storybook-Figma** | `get_component_context`, `scope_design_components`, `call_figma_tool`, `call_storybook_tool` | 4 (Prototype), 6 (Handoff) | Design-to-code bridging, component context retrieval, Figma integration |
| **Context7** | `resolve-library-id`, `query-docs` | All phases | Up-to-date library documentation lookup for any framework |
| **Google Drive** | `google_drive_search`, `google_drive_fetch` | 1 (Discover), 2 (Define) | Research document retrieval, stakeholder brief access |

### Tier 2: Complementary Skills (Per Phase)

Skills the agent should invoke or reference at each phase:

#### Phase 1: Discovery & Research
| Skill | Purpose | Invocation |
|-------|---------|------------|
| `ux-product-design-workflow` | Master framework: JTBD, empathy maps, competitive analysis | Core orchestrator |
| `jobs-to-be-done` | Forces of Progress analysis, Big Hire/Little Hire, job statements | When framing user motivation |
| `content-research-writer` | Structured content research from web sources | When gathering secondary research |
| `lead-research-assistant` | Lead/audience research and profiling | When building user segments |
| `competitive-ads-extractor` | Competitor ad strategy extraction | When performing competitive analysis |
| `survey-creator` | Research survey design and deployment | When planning primary research instruments |
| `design-sprint` | Monday exercises: Map, HMW notes, expert interviews | When running compressed discovery |
| `blue-ocean-strategy` | Non-obvious market positioning, value innovation | When analyzing competitive landscape |

#### Phase 2: Define & Problem Framing
| Skill | Purpose | Invocation |
|-------|---------|------------|
| `user-journey-mapper` | Journey map visualization and structure | When creating journey maps |
| `user-story-generator` | Structured user story generation | When translating insights to stories |
| `design-sprint` | Tuesday/Wednesday: Sketch, Decide exercises | When running design sprint define phase |
| `jobs-to-be-done` | Job statement refinement, competitive landscape mapping | When writing problem statements |
| `hooked-ux` | Trigger mapping, habit zone analysis | When defining engagement models |
| `influence-psychology` | Persuasion principles for user motivation | When framing behavioral insights |
| `contagious` | Virality and word-of-mouth frameworks | When assessing referral/adoption potential |

#### Phase 3: IA & Interaction Design
| Skill | Purpose | Invocation |
|-------|---------|------------|
| `ui-design-patterns` | Navigation, form, data display, feedback patterns | When selecting interaction patterns |
| `design-principles` | Gestalt, hierarchy, visual balance, alignment | When structuring layouts |
| `ux-heuristics` | Nielsen's 10, Krug's Laws, severity ratings | When evaluating IA decisions |
| `ui-ux-pro-max` | Style selection, color palettes, typography, layout rules | When making visual design decisions |
| `interface-design` | Interface design principles and patterns | When designing screen layouts |
| `ios-hig-design` | iOS Human Interface Guidelines | When designing for iOS |

#### Phase 4: Prototyping & Design
| Skill | Purpose | Invocation |
|-------|---------|------------|
| `all-in-one-ui-ux-design` | End-to-end design system: build/redesign/audit/design-system/flow modes | Primary design execution skill |
| `design-system-creation` | Component library, governance, documentation | When building or extending design systems |
| `design-engineer-mindset` | Rendering pipeline, GPU acceleration, design tokens as code | When optimizing prototype performance |
| `baseline-ui` | Baseline UI component templates | When bootstrapping component sets |
| `artifacts-builder` | Interactive artifact generation | When building clickable prototypes |
| `frontend-slides` | Slide-based presentation prototypes | When creating stakeholder presentations |
| `theme-factory` | Design theme generation and application | When exploring visual directions |
| `shadcn` | shadcn/ui component integration | When building with shadcn components |
| `css-native` | Native CSS patterns and modern techniques | When writing production CSS |
| `tailwindcss-framework-integration` | Tailwind CSS integration patterns | When using Tailwind |
| `premium-saas-design` | Premium SaaS UI patterns | When designing SaaS interfaces |
| `refactoring-ui` | UI refactoring principles | When improving existing designs |
| `canvas-design` | Canvas-based design with font system | When creating visual assets |
| `top-design` | Top design patterns and trends | When seeking design inspiration |
| `design-movements` | Design movement references (Bauhaus, Swiss, etc.) | When selecting aesthetic direction |
| `web-typography` | Typography systems and font pairing | When defining type hierarchy |

#### Phase 5: Validation & Testing
| Skill | Purpose | Invocation |
|-------|---------|------------|
| `ux-heuristics` | Heuristic evaluation with severity ratings (0-4) | When performing expert review |
| `accessibility` | WCAG 2.2 compliance, semantic HTML, ARIA, keyboard nav | When auditing accessibility |
| `fixing-accessibility` | Automated accessibility fix suggestions | When remediating a11y issues |
| `cro-methodology` | O/CO framework, persuasion assets audit, A/B test design | When validating conversion flows |
| `webapp-testing` | Web application testing patterns | When planning automated tests |
| `scanning-accessibility` | Automated accessibility scanning | When running accessibility scans |
| `color-contrast-checker` | WCAG color contrast verification | When validating color choices |
| `keyboard-navigation-tester` | Keyboard nav path testing | When verifying keyboard accessibility |
| `performance-lighthouse-runner` | Lighthouse audit execution | When measuring performance |
| `testing-visual-regression` | Visual regression testing setup | When catching unintended visual changes |
| `e2e-testing-patterns` | End-to-end testing patterns | When designing test automation |

#### Phase 6: Design-to-Engineering Handoff
| Skill | Purpose | Invocation |
|-------|---------|------------|
| `speckit-taskstoissues` | Convert spec tasks to GitHub/Linear issues | When creating engineering work items |
| `figma:code-connect-components` | Figma-to-code component connection | When bridging design-code gap |
| `figma:create-design-system-rules` | Design system rule generation from Figma | When documenting design system |
| `figma:implement-design` | Figma design implementation | When translating designs to code |
| `acceptance-criteria-creator` | Given/When/Then acceptance criteria | When writing engineering specs |
| `definition-of-done-generator` | DoD checklist generation | When defining completion criteria |
| `design-doc-template` | Technical design document templates | When creating engineering design docs |

#### Phase 7: Post-Launch Optimization
| Skill | Purpose | Invocation |
|-------|---------|------------|
| `cro-methodology` | Full CRE Methodology: research, O/CO, hypothesis, ICE scoring, A/B testing | Primary optimization framework |
| `hooked-ux` | Hook Model audit, habit testing, Manipulation Matrix ethics | When optimizing engagement loops |
| `a-b-test-config-creator` | A/B test configuration | When setting up experiments |
| `ab-test-analyzer` | A/B test result analysis | When interpreting experiment data |
| `statistical-significance-calculator` | Statistical significance validation | When evaluating test results |
| `funnel-analysis-builder` | Funnel visualization and analysis | When diagnosing drop-off points |
| `cohort-analysis-creator` | Cohort analysis setup | When measuring retention |
| `churn-analysis-helper` | Churn prediction and analysis | When investigating user loss |
| `retention-calculator` | Retention metric calculation | When tracking user return rates |
| `kpi-dashboard-template` | KPI dashboard design | When building monitoring dashboards |

### Tier 3: Cross-Phase Utilities

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| `mermaid-flowchart-generator` | User flow diagrams | Any phase needing flow visualization |
| `mermaid-sequence-diagram-creator` | Interaction sequence diagrams | Phases 3, 4, 6 |
| `mermaid-state-diagram-creator` | State machine diagrams | Phase 3 (state inventories) |
| `mermaid-er-diagram-creator` | Entity relationship diagrams | Phase 3 (data modeling) |
| `plantuml-diagram-generator` | UML diagrams | Architecture documentation |
| `mindmap-generator` | Mind map creation | Phases 1, 2 (ideation, synthesis) |
| `org-chart-creator` | Organizational charts | Phase 1 (stakeholder mapping) |
| `process-flow-generator` | Process flow documentation | Phases 3, 6 |
| `presentation-slide-outliner` | Stakeholder presentation structure | Any phase for stakeholder communication |
| `report-generator` | Structured report generation | Phases 1, 5, 7 (research reports, findings, metrics) |
| `find-skills` | Discover additional relevant skills dynamically | When encountering unfamiliar domain needs |

### Tier 4: Browser Automation Agents

For prototyping and validation, the agent can leverage browser automation:

| Agent Type | Tools | Use Case |
|------------|-------|----------|
| **Claude in Chrome** | `navigate`, `read_page`, `computer`, `javascript_tool`, `gif_creator` | Live page inspection, interaction recording, competitive UX teardowns |
| **Playwright Agent** | Full browser automation suite | Automated usability flow testing, form validation, responsive checks |
| **Chrome DevTools Agent** | Performance tracing, memory snapshots, network analysis | Performance optimization, CWV measurement, resource audit |

### Tier 5: Strategy & Business Skills

These skills inform the business context that shapes UX decisions:

| Skill | Phase Relevance | Contribution |
|-------|----------------|--------------|
| `blue-ocean-strategy` | 1 (Discover) | Value innovation canvas, non-customer analysis |
| `lean-startup` | 1 (Discover), 7 (Optimize) | Build-Measure-Learn, MVP definition, pivot criteria |
| `crossing-the-chasm` | 2 (Define), 7 (Optimize) | Adoption lifecycle, segment targeting |
| `obviously-awesome` | 2 (Define) | Product positioning, competitive alternatives framing |
| `storybrand-messaging` | 2 (Define), 4 (Prototype) | Narrative framework for UI copy and messaging |
| `predictable-revenue` | 7 (Optimize) | Revenue funnel alignment with UX metrics |
| `traction-eos` | 7 (Optimize) | Organizational alignment, scorecard metrics |
| `made-to-stick` | 4 (Prototype) | Message stickiness principles for UI copy |
| `contagious` | 7 (Optimize) | Virality triggers, social currency, STEPPS framework |
| `hundred-million-offers` | 2 (Define), 4 (Prototype) | Offer construction, value equation |
| `negotiation` | 1 (Discover) | Stakeholder alignment, research buy-in |
| `drive-motivation` | 2 (Define) | Autonomy/mastery/purpose for engagement design |
| `influence-psychology` | 4 (Prototype) | Cialdini's principles for ethical persuasion in UI |

### Integration Rules

1. **Auto-detect available tools**: At session start, the agent checks which MCP servers are connected and adjusts recommendations accordingly.
2. **Graceful degradation**: If an MCP tool is unavailable, the agent falls back to manual instructions (e.g., "Run Lighthouse in Chrome DevTools manually").
3. **Skill chaining**: Skills should be invoked in sequence when they complement each other (e.g., `ui-ux-pro-max` for style selection → `all-in-one-ui-ux-design` for implementation → `accessibility` for audit).
4. **Evidence tagging from tools**: Outputs from MCP tools (Lighthouse scores, accessibility violations, performance traces) should be tagged as `[MEASURED: tool-name]` in artifacts.
5. **No tool dependency**: The agent MUST function fully without any MCP tools connected — tools enhance but are never required.

---

## Appendix H: Complementary Skills Matrix

Cross-reference of skill capabilities to UX agent functional requirements:

| Functional Requirement | Primary Skill(s) | Supporting Skill(s) | MCP Tool(s) |
|----------------------|-------------------|---------------------|-------------|
| FR-001: Phase guidance | `ux-product-design-workflow` | — | — |
| FR-002: Artifact generation | `all-in-one-ui-ux-design`, `ux-designer` | `artifacts-builder`, `report-generator` | — |
| FR-003: Consistent output format | `ux-product-design-workflow` | `ui-ux-pro-max` | — |
| FR-004: Phase progression (DoD) | `ux-product-design-workflow` | `definition-of-done-generator` | — |
| FR-005: Evidence vs assumption | `jobs-to-be-done`, `cro-methodology` | `survey-creator`, `lead-research-assistant` | — |
| FR-006: Interaction states (7+) | `ui-design-patterns`, `ui-ux-pro-max` | `design-system-creation` | — |
| FR-007: Product Kata | `cro-methodology` | `ab-test-analyzer`, `funnel-analysis-builder` | `chrome-devtools` (Lighthouse) |
| FR-008: Context-adaptive output | `ux-product-design-workflow` | — | — |
| FR-009: Four-Risk Gate | `ux-product-design-workflow` | `blue-ocean-strategy`, `lean-startup` | — |
| FR-010: No production code | `ux-product-design-workflow` | — | — |
| FR-011: Laws of UX | `ux-heuristics`, `design-principles` | `ui-ux-pro-max` | — |
| FR-012: WCAG 2.1 AA | `accessibility`, `fixing-accessibility` | `color-contrast-checker`, `keyboard-navigation-tester` | `accesslint`, `playwright` |
| FR-013: 7-phase workflow | `ux-product-design-workflow` | All phase-specific skills | — |
| FR-014: Clarifying questions | `ux-product-design-workflow` | `jobs-to-be-done` | — |
| FR-015: Competitive analysis | `ux-product-design-workflow` | `competitive-ads-extractor`, `blue-ocean-strategy` | `Claude in Chrome` |
| FR-016: Empathy maps (6 quad) | `ux-product-design-workflow` | `user-journey-mapper` | — |
| FR-017: JTBD statements | `jobs-to-be-done` | `ux-product-design-workflow` | — |
| FR-018: Synthesis methods | `ux-product-design-workflow` | `mindmap-generator` | — |
| FR-019: Cross-phase refs | `ux-product-design-workflow` | — | — |
| FR-020: RTL/MENA patterns | `ux-product-design-workflow` (arabic-rtl-mena ref) | `ui-ux-pro-max` | — |
| FR-021: Spec Kit integration | `speckit-*` skills | `speckit-taskstoissues` | — |
| FR-022: Design brief | `all-in-one-ui-ux-design` | `design-sprint` | — |
| FR-023: Empathy map tracing | `ux-product-design-workflow` | `jobs-to-be-done` | — |
