# UX & Product Design Workflow

A comprehensive 7-phase UX & Product Design workflow plugin for Claude Code. Provides 6 autonomous agents, 8 skills, 24 templates, 7 Definition of Done checklists, and MCP integrations for accessibility auditing, browser automation, design system lookup, and prototype review.

## Installation

This plugin is installed as a Claude Code plugin. Ensure it is listed in your Claude Code settings or installed via the plugin manager.

## Phases

| Phase | Skill | Description |
|-------|-------|-------------|
| 1 | `ux-discover` | Discovery & Research |
| 2 | `ux-define` | Define & Problem Framing |
| 3 | `ux-ia` | IA & Interaction Design |
| 4 | `ux-prototype` | Prototyping & Laws of UX |
| 5 | `ux-validate` | Validation & Usability Testing |
| 6 | `ux-handoff` | Design-to-Engineering Handoff |
| 7 | `ux-optimize` | Post-Launch Optimization |

## Agents

| Agent | Purpose |
|-------|---------|
| `ux-accessibility-auditor` | WCAG 2.1 AA accessibility auditing |
| `ux-artifact-generator` | Research-to-artifact synthesis |
| `ux-handoff-preparer` | Engineering handoff package generation |
| `ux-phase-navigator` | Phase detection and transition gating |
| `ux-prototype-reviewer` | Live prototype heuristic review |
| `ux-researcher` | Autonomous competitive analysis and UX teardowns |

## MCP Server Dependencies

All MCP servers are optional. The plugin degrades gracefully when servers are unavailable.

| Server | Purpose | Used By |
|--------|---------|---------|
| **AccessLint** | WCAG accessibility auditing | ux-accessibility-auditor, ux-researcher |
| **Playwright** | Browser automation | ux-prototype-reviewer, ux-researcher |
| **Chrome DevTools** | Performance/Lighthouse auditing | ux-prototype-reviewer, ux-accessibility-auditor |
| **Claude Preview** | Live HTML/React preview | ux-prototype-reviewer |
| **shadcn-ui** | Component registry lookup | ux-handoff-preparer |
| **shadcn-community** | Community components/themes | ux-handoff-preparer |
| **Storybook-Figma** | Design-to-code bridging | ux-prototype-reviewer, ux-handoff-preparer |
| **Context7** | Library docs lookup | ux-researcher, ux-artifact-generator, ux-handoff-preparer |

## Quick Start

```
# Invoke the master workflow
/ux-product-design-workflow

# Or invoke a specific phase
/ux-discover
/ux-define
/ux-ia
/ux-prototype
/ux-validate
/ux-handoff
/ux-optimize
```

## License

Copyright (c) Fady. All rights reserved.
