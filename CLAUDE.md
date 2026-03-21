# Skills Hub - Claude Configuration

This workspace is the central hub for all Claude Code skills, plugins, and agents. Every skill installed here is accessible to all projects and workflows.

## UX & Product Design Agent

The primary agent in this workspace. A comprehensive 7-phase UX workflow system.

**Skill location**: `.claude/skills/ux-product-design-workflow/`

### Phase Commands

| Command | Phase | Skill Path |
|---------|-------|------------|
| `/ux.discover` | 1. Discovery & Research | `skills/ux-discover/SKILL.md` |
| `/ux.define` | 2. Define & Problem Framing | `skills/ux-define/SKILL.md` |
| `/ux.ia` | 3. IA & Interaction Design | `skills/ux-ia/SKILL.md` |
| `/ux.prototype` | 4. Prototyping & Laws of UX | `skills/ux-prototype/SKILL.md` |
| `/ux.validate` | 5. Validation & Testing | `skills/ux-validate/SKILL.md` |
| `/ux.handoff` | 6. Design-to-Engineering Handoff | `skills/ux-handoff/SKILL.md` |
| `/ux.optimize` | 7. Post-Launch Optimization | `skills/ux-optimize/SKILL.md` |

### Key Resources

- **References**: 10 deep-dive documents in `references/`
- **Templates**: 24 artifact templates in `templates/`
- **Checklists**: 7 Definition-of-Done checklists in `checklists/`
- **Specs**: Feature specification with contracts in `specs/001-ux-design-agent/`
- **Rules**: Context engineering rules in `rules/`

## Complementary Skills Access

The UX agent automatically chains complementary skills installed at the user level (`~/.claude/skills/`). All skills listed below are available system-wide and can be invoked by any agent or workflow.

### Discovery Phase Skills
- `jobs-to-be-done` - JTBD framework for job statements and customer research
- `competitive-ads-extractor` - Competitive intelligence and ad analysis
- `lead-research-assistant` - Lead and market research
- `content-research-writer` - Content research and writing
- `design-sprint` - 5-day Design Sprint methodology
- `blue-ocean-strategy` - Blue ocean strategic analysis
- `survey-creator` - Survey design and creation

### Define Phase Skills
- `user-journey-mapper` - Journey map creation
- `user-story-generator` - User story generation
- `hooked-ux` - Hook Model for habit-forming products
- `influence-psychology` - Psychology of persuasion
- `obviously-awesome` - Product positioning
- `mindmap-generator` - Mind map creation
- `hundred-million-offers` - Offer design framework

### IA & Interaction Phase Skills
- `ui-design-patterns` - UI pattern library and best practices
- `design-principles` - Visual design fundamentals
- `ux-heuristics` - Nielsen's 10 + Krug's usability principles
- `ui-ux-pro-max` - Comprehensive design intelligence with search
- `interface-design` - Interface design patterns
- `mermaid-flowchart-generator` - Flowchart generation
- `mermaid-state-diagram-creator` - State diagram generation

### Prototyping Phase Skills
- `all-in-one-ui-ux-design` - End-to-end design system (build/redesign/audit/flow)
- `design-system-creation` - Component library and governance
- `design-engineer-mindset` - Design engineering (rendering, GPU, tokens)
- `baseline-ui` - Baseline UI component templates
- `artifacts-builder` - Interactive artifact generation
- `theme-factory` - Design theme generation
- `refactoring-ui` - UI refactoring principles
- `web-typography` - Typography systems and font pairing
- `design-movements` - Design movement references
- `made-to-stick` - Message stickiness principles
- `storybrand-messaging` - Narrative framework for UI copy

### Validation Phase Skills
- `accessibility` - WCAG 2.2 compliance and semantic HTML
- `fixing-accessibility` - Automated accessibility fix suggestions
- `cro-methodology` - CRE conversion rate optimization
- `color-contrast-checker` - WCAG contrast ratio validation
- `keyboard-navigation-tester` - Keyboard navigation verification
- `scanning-accessibility` - Automated accessibility scanning
- `e2e-testing-patterns` - End-to-end testing patterns
- `ux-designer` - UX design specialist with WCAG scripts

### Handoff Phase Skills
- `speckit-taskstoissues` - Convert tasks to GitHub/Linear issues
- `acceptance-criteria-creator` - Given/When/Then criteria generation
- `definition-of-done-generator` - DoD checklist generation
- `design-doc-template` - Technical design document templates

### Optimization Phase Skills
- `cro-methodology` - CRE Methodology for conversion optimization
- `hooked-ux` - Hook Model audit and habit testing
- `a-b-test-config-creator` - A/B test configuration
- `ab-test-analyzer` - A/B test result analysis
- `statistical-significance-calculator` - Statistical significance validation
- `funnel-analysis-builder` - Funnel visualization and analysis
- `cohort-analysis-creator` - Cohort analysis setup
- `churn-analysis-helper` - Churn prediction and analysis
- `retention-calculator` - Retention metric calculation
- `kpi-dashboard-template` - KPI dashboard design
- `lean-startup` - Build-Measure-Learn methodology
- `predictable-revenue` - Revenue funnel alignment

### Cross-Phase Utilities
- `brand-guidelines` - Brand consistency
- `brand-strategy` - Brand strategy
- `brand-systems` - Brand system management
- `canvas-design` - Canvas-based design with custom fonts
- `design-system-context` - Design system context loading
- `premium-saas-design` - Premium SaaS design patterns
- `top-design` - Design excellence patterns
- `css-native` - CSS animation principles
- `frontend-prime` - Frontend engineering patterns
- `frontend-ui-engineering` - UI engineering patterns

## MCP Server Integrations

The UX agent auto-detects and leverages these MCP servers when connected:

| Server | Capabilities | Used In |
|--------|-------------|---------|
| **AccessLint** | `audit_url`, `audit_html`, `audit_file`, `diff_html` | Validate, Handoff |
| **Playwright** | Browser automation, flow testing | Prototype, Validate |
| **Chrome DevTools** | Lighthouse audits, performance tracing, screenshots | Validate, Optimize |
| **Claude Preview** | Live HTML preview, click/fill/screenshot | Prototype, Validate |
| **shadcn-ui** | Component lookup, audit checklists | IA, Prototype |
| **shadcn-community** | Community themes and components | Prototype |
| **Storybook-Figma** | Design-to-code bridging, Figma integration | Prototype, Handoff |
| **Context7** | Up-to-date library documentation | All phases |
| **Google Drive** | Research document access | Discovery |

## Spec Kit Integration

The UX agent works with Spec Kit commands:
- `/speckit.specify` + `/ux.define` - Problem statements feed into specs
- `/speckit.plan` + `/ux.ia` - IA constraints inform implementation plans
- `/speckit.tasks` - UX work items appear alongside engineering tasks

## Conventions

- All UX artifacts are saved under `ux/` in the target project directory
- Evidence tagging: `[EVIDENCE: source]`, `[ASSUMPTION: reason]`, `[MEASURED: tool]`
- Context modes: `--mode mvp`, `--mode growth`, `--mode enterprise`
- Cross-phase referencing is mandatory (later phases cite earlier artifacts)
- Phase transitions require Definition of Done checklist completion
