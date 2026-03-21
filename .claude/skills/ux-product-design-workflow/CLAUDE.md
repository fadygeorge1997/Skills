# UX & Product Design Workflow Plugin

## Overview

A comprehensive 7-phase UX & Product Design workflow plugin for Claude Code. Covers Discovery, Define, IA & Interaction Design, Prototyping, Validation, Handoff, and Post-Launch Optimization.

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
checklists/                 # 7 Definition of Done checklists
references/                 # 10 deep-dive reference docs
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

## Conventions

- All artifacts use evidence tagging: `[EVIDENCE: source]`, `[ASSUMPTION: reason]`, `[CONTRADICTION: source1 vs source2]`
- Empathy maps use 6 quadrants: Says, Thinks, Does, Feels, Sees, Hears
- State inventories cover 7+ states: Default, Empty, Loading, Partial, Error, Success, Offline, Permission
- Context-adaptive depth: MVP / Growth / Enterprise scaling
