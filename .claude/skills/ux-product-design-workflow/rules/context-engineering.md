# Context Engineering Rules for UX Agent

## Overview

Context engineering is the practice of optimizing instructions and context for AI agents. This document provides specific rules for the UX & Product Design Agent to ensure expert-level performance.

---

## Rule 1: Right Altitude Principle

Present ideas at the appropriate abstraction level for the context.

| Context | Altitude | Example |
|---------|----------|---------|
| MVP Startup | Low (concrete) | "Create a 3-field signup form with email validation" |
| Enterprise | Medium (structured) | "Design a multi-step onboarding flow with role-based paths" |
| Innovation | High (strategic) | "Explore opportunities to reduce time-to-first-value by 50%" |

**Implementation:**
```markdown
When generating outputs, always:
1. Assess the context mode (MVP/Growth/Enterprise)
2. Adjust output depth accordingly
3. Include appropriate level of detail and justification
```

---

## Rule 2: Structured Output Format

Always produce outputs in structured, parseable formats.

### Persona Output Structure
```markdown
# [NAME]: The [Archetype]

## Demographics
| Attribute | Value | Evidence |
|-----------|-------|----------|
| Age | [value] | [EVIDENCE: source] |

## Behaviors
- [Behavior] [EVIDENCE: source]

## Goals
- [Goal] [EVIDENCE: source]

## Pain Points
| Pain Point | Severity | Evidence |
|------------|----------|----------|
| [Pain] | High/Medium/Low | [source] |

## JTBD Statement
> "When [situation], I want to [job], so I can [outcome]."

## Quote
> "[Quote]" — [Participant #]
```

---

## Rule 3: Evidence-First Reasoning

Every claim must be tagged with its evidence source.

### Evidence Tags
```markdown
[EVIDENCE: interview-3]      # Direct from user research
[EVIDENCE: analytics-Q3]     # From data/analytics
[MEASURED: 43%, GA4]         # Quantified observation
[ASSUMPTION: inference]      # Hypothesis requiring validation
[CONTRADICTION: i3 vs a1]    # Conflicting data points
```

---

## Rule 4: Phased Context Injection

Inject context appropriate to the current phase.

| Phase | Required Context | Optional Context |
|-------|-----------------|------------------|
| Discovery | Business objectives, constraints | Existing research, analytics |
| Define | Discovery outputs, empathy maps | Competitive analysis |
| IA | Personas, problem statements | Card sorting results |
| Prototype | IA artifacts, design tokens | Brand guidelines |
| Validate | Prototypes, test plan | Previous findings |
| Handoff | Validated designs, specs | Technical constraints |
| Optimize | Live metrics, experiment results | User feedback |

---

## Rule 5: Cross-Reference Enforcement

All outputs must reference earlier-phase artifacts.

```markdown
**References:**
- Persona: [Persona Name] ([link])
- Journey Map: [Journey Name] ([link])
- Pain Point: [Pain Point ID] from [source]
```

---

## Rule 6: Confidence Declaration

Declare confidence level for all outputs.

| Level | Criteria | Action |
|-------|----------|--------|
| **High** | Multiple evidence sources, no contradictions | Proceed with implementation |
| **Medium** | Some evidence, minor gaps | Proceed with validation plan |
| **Low** | Limited evidence, significant assumptions | Validate before action |
| **Hypothesis** | No direct evidence, inference only | Mark for research |

---

## Rule 7: Progressive Disclosure

Layer information from essential to supplementary.

```markdown
## Layer 1: Executive Summary (Required)
[2-3 sentences capturing the core output]

## Layer 2: Key Findings (Required)
[Top 3-5 points with evidence]

## Layer 3: Detailed Analysis (Default expanded)
[Full analysis with supporting data]

## Layer 4: Appendix (Collapsed by default)
[Raw data, full quotes, methodology details]
```

---

## Rule 8: Anti-Pattern Detection

Actively identify and flag anti-patterns.

```markdown
Scan outputs for:

1. **Confirmation Bias**: Are all findings aligned? [Flag if no disconfirming evidence sought]
2. **Solution-Framed Problems**: Is the problem stated as a feature? [Reframe as need]
3. **Assumption Leakage**: Are assumptions presented as facts? [Tag appropriately]
4. **Persona Theater**: Could this persona apply to anyone? [Add specificity]
5. **Happy Path Only**: Are edge cases missing? [Add error/empty states]
```

---

## Rule 9: Stakeholder Calibration

Adjust communication style based on audience.

| Audience | Tone | Detail Level | Format |
|----------|------|--------------|--------|
| **Executive** | Strategic | Summary | 1-page, metrics-focused |
| **Product Manager** | Balanced | Moderate | Problem + solution framing |
| **Designer** | Practical | Detailed | Specifications + rationale |
| **Engineer** | Technical | Implementation | Code-ready specs |
| **Researcher** | Rigorous | Full | Methodology + evidence |

---

## Rule 10: Continuous Validation

Validate outputs against quality criteria.

### Quality Criteria by Artifact

**Persona Quality:**
- [ ] Specific enough to make design decisions
- [ ] Every attribute has evidence or assumption tag
- [ ] Includes surprising/non-obvious detail
- [ ] JTBD statement present
- [ ] Representative quote from research

**Journey Map Quality:**
- [ ] All stages defined with touchpoints
- [ ] Emotional arc captured
- [ ] Pain points severity-rated
- [ ] Opportunities documented
- [ ] Evidence sources cited

**Problem Statement Quality:**
- [ ] Specific user segment named
- [ ] Real need (not feature)
- [ ] Evidence-backed insight
- [ ] Testable
- [ ] Business-relevant
