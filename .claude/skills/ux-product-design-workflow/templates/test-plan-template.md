# Usability Test Plan Template

## Test Overview

| Attribute | Value |
|-----------|-------|
| **Test Initiative** | [Name/Title] |
| **Product/Feature** | [What's being tested] |
| **Test Lead** | [Name] |
| **Test Dates** | [Start] to [End] |
| **Methodology** | [Remote Moderated/Unmoderated/In-person] |

---

## Research Objectives

### Primary Objective
[What's the main thing we want to learn?]

### Secondary Objectives
1. [Secondary learning goal]
2. [Secondary learning goal]

### Link to HMW Statement
> [The HMW statement this test addresses]

---

## Methodology

### Test Type

| Aspect | Choice | Rationale |
|--------|--------|-----------|
| **Format** | [Remote/In-person] | [Why] |
| **Moderation** | [Moderated/Unmoderated] | [Why] |
| **Platform** | [Tool name] | [Why] |
| **Duration** | [Minutes per session] | [Based on task complexity] |

### Test Materials
- [ ] Prototype/designs ready
- [ ] Task scenarios written
- [ ] Screener questions prepared
- [ ] Consent form ready
- [ ] Recording setup confirmed

---

## Participants

### Recruitment Criteria

| Segment | Description | Count | Screener Criteria |
|---------|-------------|-------|-------------------|
| [Segment 1] | [Who] | 5-8 | [Key characteristics] |
| [Segment 2] | [Who] | 5-8 | [Key characteristics] |

**Total Participants:** [Count]

### Participant Profile (Linked to Persona)

| Persona | Segment | Match Criteria | Priority |
|---------|---------|----------------|----------|
| [Persona 1] | [Segment 1] | [What makes a match] | Primary |
| [Persona 2] | [Segment 2] | [What makes a match] | Secondary |

---

## Task Scenarios

### Task 1: [Task Name]

| Element | Description |
|---------|-------------|
| **Scenario** | "You [context]. You want to [goal]." |
| **Starting Point** | [Where participant begins] |
| **Success Path** | [Expected steps to complete] |
| **Success Criteria** | [What counts as successful completion] |
| **Time Target** | [Expected duration] |

### Task 2: [Task Name]

| Element | Description |
|---------|-------------|
| **Scenario** | "You [context]. You want to [goal]." |
| **Starting Point** | [Where participant begins] |
| **Success Path** | [Expected steps to complete] |
| **Success Criteria** | [What counts as successful completion] |
| **Time Target** | [Expected duration] |

### Task 3: [Task Name]

| Element | Description |
|---------|-------------|
| **Scenario** | "You [context]. You want to [goal]." |
| **Starting Point** | [Where participant begins] |
| **Success Path** | [Expected steps to complete] |
| **Success Criteria** | [What counts as successful completion] |
| **Time Target** | [Expected duration] |

### Task 4: [Task Name - Error/Edge Case]

| Element | Description |
|---------|-------------|
| **Scenario** | "You [context with edge case]. You want to [goal]." |
| **Starting Point** | [Where participant begins] |
| **What We're Testing** | [Error handling, recovery, empty state, etc.] |
| **Success Criteria** | [Can they recover? Understand what happened?] |

---

## Metrics

### Primary Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **Task Completion Rate** | >80% | [Completed / Attempted × 100] |
| **SUS Score** | ≥68 | [10-item questionnaire] |

### Secondary Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **Time on Task** | [Baseline or target] | [Timer from start to completion] |
| **Error Rate** | <10% | [Errors / Actions × 100] |
| **SEQ (Single Ease Question)** | ≥5 (1-7 scale) | ["Overall, how easy or difficult was this task?"] |

### Qualitative Measures

| Measure | Collection Method |
|---------|-------------------|
| **Think-aloud insights** | [Real-time notes and quotes] |
| **Pain points** | [Observed struggles and comments] |
| **Confusion points** | [Where participants hesitate or ask questions] |
| **Positive moments** | [Where participants express satisfaction] |

---

## Session Structure

### Pre-Test (5 minutes)
1. Welcome and introduction
2. Consent and recording permission
3. Technology check (if remote)
4. "Remember, we're testing the design, not you"

### Warm-up (5 minutes)
1. Background questions
2. Relevant experience questions
3. "Tell me about how you currently [relevant activity]"

### Tasks (30-40 minutes)
1. Think-aloud instructions
2. Task scenarios in order
3. Follow-up questions after each task

### Post-Test (10 minutes)
1. SUS questionnaire
2. Overall impressions
3. "What would make this better?"
4. Thank you and incentive information

---

## Think-Aloud Protocol

### Instructions to Participants
> "We're interested in what you're thinking, not just what you're doing. As you work through these tasks, please say everything you're thinking — your impressions, what you're looking for, what confuses you, what you expect to happen. There are no wrong answers."

### Moderator Guidelines
| Do | Don't |
|----|-------|
| "What are you looking for?" | "Click on that button" |
| "What did you expect to happen?" | "You're looking for X" |
| "Tell me more about that" | React with surprise or concern |
| "What would you do next?" | Help them complete the task |

---

## Data Collection

### Recording Setup
| Element | Tool/Method |
|---------|-------------|
| Screen recording | [Tool] |
| Audio | [Tool] |
| Notes | [Note-taking tool/template] |
| Observers | [Names and roles] |

### Note-Taking Template

| Time | Task | Participant Says | Participant Does | Issue Type | Severity |
|------|------|------------------|------------------|------------|----------|
| [00:00] | [Task #] | [Quote] | [Action] | [UX/Content/Technical] | [1-4] |

---

## Analysis Plan

### Immediate (After Each Session)
- [ ] Quick debrief with observers
- [ ] Top 3 observations noted
- [ ] Any immediate pattern recognition

### Post-Test Analysis
- [ ] Review all recordings
- [ ] Code issues by type and severity
- [ ] Calculate metrics
- [ ] Affinity map findings
- [ ] Prioritize recommendations

### Severity Rating

| Rating | Level | Description | Action |
|--------|-------|-------------|--------|
| 4 | Catastrophic | Blocks task completion | Must fix before launch |
| 3 | Major | Significant friction, difficult workaround | High priority fix |
| 2 | Minor | Inconvenience, easy workaround | Fix when possible |
| 1 | Cosmetic | Polish issue | Fix if time allows |

---

## Schedule

| Date | Time | Participant # | Segment | Status |
|------|------|---------------|---------|--------|
| [Date] | [Time] | P1 | [Segment] | [Scheduled/Complete] |
| [Date] | [Time] | P2 | [Segment] | [Scheduled/Complete] |
| [Date] | [Time] | P3 | [Segment] | [Scheduled/Complete] |

**Buffer:** Schedule 15-30 minutes between sessions for note review and breaks.

---

## Deliverables

| Deliverable | Format | Audience | Due Date |
|-------------|--------|----------|----------|
| **Findings Report** | [Deck/Doc] | [Stakeholders] | [Date] |
| **Highlights Video** | [Video clips] | [Stakeholders] | [Date] |
| **Recommendations** | [Prioritized list] | [Design/Dev team] | [Date] |

---

## Risk Mitigation

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Participant no-shows | Medium | Overbook by 20%, backup list |
| Technical issues | Medium | Test setup beforehand, backup plan |
| Prototype fails | Low | Backup version, paper prototype |
| Session runs long | Medium | Prioritize tasks, have cut list |

---

## Connected Artifacts

| Artifact | Relationship | Link |
|----------|--------------|------|
| Personas | [Participant match] | [Link] |
| Journey Map | [Pain points to test] | [Link] |
| Prototype | [What's being tested] | [Link] |
| Test Results | [Output from this test] | [Link to findings report] |

---

## Metadata

| Field | Value |
|-------|-------|
| Created | [Date] |
| Created By | [Name] |
| Last Updated | [Date] |
| Version | [Version number] |
| Status | [Draft/Approved/In Progress/Complete] |
