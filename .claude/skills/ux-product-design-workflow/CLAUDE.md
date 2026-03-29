# UX & Product Design Workflow Plugin

## Overview

An autonomous 7-phase UX & Product Design workflow plugin for Claude Code. Self-loads context, routes to 56+ complementary skills, and self-audits to Impeccable Standard. Covers Discovery, Define, IA & Interaction Design, Prototyping, Validation, Handoff, and Post-Launch Optimization with non-linear iteration support.

## Structure

```
SKILL.md                    # Master orchestrator skill (root)
skills/                     # 7 phase-specific sub-skills
  ux-discover/SKILL.md      # Phase 1: Discovery & Research
  ux-define/SKILL.md        # Phase 2: Define & Problem Framing
  ux-ia/SKILL.md            # Phase 3: IA & Interaction Design
  ux-prototype/SKILL.md     # Phase 4: Prototyping & Laws of UX
  ux-validate/SKILL.md      # Phase 5: Validation & Usability Testing
  ux-handoff/SKILL.md       # Phase 6: Design-to-Engineering Handoff
  ux-optimize/SKILL.md      # Phase 7: Post-Launch Optimization
agents/                     # 6 autonomous agents
  ux-accessibility-auditor.md
  ux-artifact-generator.md
  ux-handoff-preparer.md
  ux-phase-navigator.md
  ux-prototype-reviewer.md
  ux-researcher.md
templates/                  # 24 artifact templates
checklists/                 # 7 Definition of Done checklists (with loop-back triggers)
references/                 # 10 deep-dive reference docs (cross-referenced)
rules/                      # Orchestration layer
  context-engineering.md    # Output format rules, evidence tagging
  agent-coordination.md     # Agent priority, data flow, conflict resolution
  iteration-workflows.md    # Loop-back triggers, forward-only conditions
  skill-routing.md          # Context Bootstrap, Skill Routing Table, Self-Audit
integrations/               # MCP tools guide + skill chaining guide
.claude-plugin/plugin.json  # Plugin manifest
```

## MCP Server Dependencies (all optional, graceful degradation)

- **AccessLint** — WCAG accessibility auditing
- **Playwright** — Browser automation for prototype testing
- **Chrome DevTools** — Performance auditing, Lighthouse, CWV
- **Claude Preview** — Live HTML/React prototype preview
- **shadcn-ui** — Component registry lookup
- **shadcn-community** — Community components and themes
- **Storybook-Figma** — Design-to-code bridging
- **Context7** — Library documentation lookup

## Phase Model (7 phases)

1. Discovery & Research
2. Define & Problem Framing
3. IA & Interaction Design
4. Prototyping & Laws of UX
5. Validation & Usability Testing
6. Design-to-Engineering Handoff
7. Post-Launch Optimization

## Skill Access

All 6 agents have the `Skill` tool and can invoke **any installed skill** (1000+ available):
- `Skill(skill: "find-skills")` — Search skills by keyword when the routing table doesn't cover a need
- `Skill(skill: "speckit-full")` — Full spec-kit workflow for reasoning and planning
- `Skill(skill: "accessibility")`, `Skill(skill: "cro-methodology")`, etc. — Direct invocation by name
- Agents autonomously chain skills when a complementary skill improves deliverable quality

## Conventions

- All artifacts use evidence tagging: `[EVIDENCE: source]`, `[ASSUMPTION: reason]`, `[CONTRADICTION: source1 vs source2]`
- Empathy maps use 6 quadrants: Says, Thinks, Does, Feels, Sees, Hears
- 8 content states per screen: Default, Empty, Loading, Partial, Error, Success, Offline, Permission
- 5 interaction states per element: Default, Hover, Active, Focus, Disabled
- Context-adaptive depth: MVP / Growth / Enterprise scaling
- Autonomous Execution Protocol: context bootstrap → skill routing → evidence tagging → self-audit → phase transition check
