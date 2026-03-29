# Skill Routing Intelligence

## Purpose

This file provides the routing logic that connects user intent to the right skill, agent, tool, or reference file. When the UX workflow is active, use this table to autonomously invoke complementary skills without user prompting.

## How to Invoke Skills

All agents in this workflow have access to the `Skill` tool. Use it to invoke any skill by name:

```
Skill(skill: "accessibility")           → WCAG 2.2 compliance skill
Skill(skill: "jobs-to-be-done")         → JTBD framework
Skill(skill: "speckit-full")            → Full spec-kit workflow
Skill(skill: "find-skills")             → Search for any skill by keyword
```

**Skill Discovery**: If the routing table below doesn't list a skill for your current need, use `Skill(skill: "find-skills")` to search the full skill catalog (1000+ skills). Search by keyword — e.g., "typography", "animation", "testing", "security", "database".

**Spec-Kit for Reasoning**: For complex planning, analysis, or specification work, chain spec-kit commands:
- `Skill(skill: "speckit-full")` — Full end-to-end spec workflow (preferred when no spec.md exists)
- `Skill(skill: "speckit-analyze")` — Analyze existing code/product
- `Skill(skill: "speckit-plan")` — Plan implementation (requires spec.md)
- `Skill(skill: "speckit-tasks")` — Break work into tasks
- `Skill(skill: "speckit-checklist")` — Quality verification

**Rule**: When a skill can improve the quality of a deliverable, invoke it. Don't limit yourself to the routing table — it covers common cases, not all cases.

## Context Bootstrap Protocol

Before starting ANY phase, the agent must self-load context:

### Step 1: Load Phase Context
```
Read: rules/context-engineering.md          → Understand output format rules
Read: rules/agent-coordination.md           → Know which agents to invoke
Read: rules/iteration-workflows.md          → Know loop-back conditions
Read: rules/skill-routing.md               → This file (routing decisions)
```

### Step 2: Load Phase-Specific References
| Phase | Required Reads |
|-------|---------------|
| 1 | `references/frameworks.md`, `references/discovery-synthesis.md`, `references/competitive-analysis.md` |
| 2 | `references/discovery-synthesis.md`, `references/frameworks.md` |
| 3 | `references/ideation-prototyping.md`, `references/laws-of-ux.md` |
| 4 | `references/laws-of-ux.md`, `references/ideation-prototyping.md`, `references/arabic-rtl-mena.md` (if RTL) |
| 5 | `references/usability-testing.md`, `references/agentic-ai-design.md` (if AI features) |
| 6 | `references/design-handoff.md` |
| 7 | `references/metrics-optimization.md`, `references/agentic-ai-design.md` |

### Step 3: Load Phase-Specific Templates
| Phase | Templates to Read |
|-------|------------------|
| 1 | `templates/research-plan-template.md`, `templates/competitive-analysis-template.md`, `templates/empathy-map-template.md`, `templates/jtbd-statement-template.md`, `templates/four-risk-gate-template.md`, `templates/design-brief-template.md` |
| 2 | `templates/persona-template.md`, `templates/journey-map-template.md`, `templates/problem-statement-template.md`, `templates/hmw-template.md`, `templates/opportunity-solution-tree-template.md` |
| 3 | `templates/sitemap-template.md`, `templates/user-flow-template.md`, `templates/state-inventory-template.md` |
| 4 | `templates/heuristic-evaluation-template.md` |
| 5 | `templates/test-plan-template.md`, `templates/participant-screener-template.md`, `templates/heuristic-evaluation-template.md`, `templates/findings-report-template.md` |
| 6 | `templates/handoff-checklist-template.md`, `templates/edge-case-catalog-template.md`, `templates/acceptance-criteria-template.md` |
| 7 | `templates/goals-signals-metrics-template.md`, `templates/experiment-backlog-template.md`, `templates/north-star-metric-template.md` |

### Step 4: Check Existing Artifacts
```
Glob: ux/research/**/*.md       → Phase 1 outputs
Glob: ux/define/**/*.md         → Phase 2 outputs
Glob: ux/ia/**/*.md             → Phase 3 outputs
Glob: ux/prototype/**/*.md      → Phase 4 outputs
Glob: ux/validate/**/*.md       → Phase 5 outputs
Glob: ux/handoff/**/*.md        → Phase 6 outputs
Glob: ux/optimize/**/*.md       → Phase 7 outputs
Read: ux/phase-status.json      → Current phase state (if exists)
```

---

## Skill Routing Table

**How to read this table**: The "Skill to Invoke" column is the skill name to pass to `Skill(skill: "name")`. Entries prefixed with `Agent:` are dispatched via the Agent tool instead. Entries prefixed with `MCP:` are direct MCP tool calls.

**Beyond this table**: Use `Skill(skill: "find-skills")` to search the full catalog (1000+ skills) by keyword when no row matches.

### Phase 1: Discovery & Research

| User Intent / Action | Skill to Invoke | When | File to Write |
|---------------------|----------------|------|---------------|
| JTBD analysis | `jobs-to-be-done` | User mentions jobs, hiring criteria, progress | `ux/research/jtbd-analysis.md` |
| Competitive ads/positioning | `competitive-ads-extractor` | Competitor ad/positioning data needed | `ux/research/competitive-ads.md` |
| Market/lead research | `lead-research-assistant` | Market sizing, lead data | `ux/research/market-research.md` |
| Content research | `content-research-writer` | Content strategy research | `ux/research/content-research.md` |
| Design sprint | `design-sprint` | "Design sprint" or 5-day process | `ux/research/design-sprint-output.md` |
| Blue ocean strategy | `blue-ocean-strategy` | Uncontested market space | `ux/research/blue-ocean-analysis.md` |
| Survey design | `survey-creator` | Survey instrument creation | `ux/research/survey-design.md` |
| Adoption lifecycle | `crossing-the-chasm` | Market adoption, early majority | `ux/research/adoption-analysis.md` |
| Viral/word-of-mouth | `contagious` | Why things spread, social currency | `ux/research/virality-analysis.md` |
| User motivation | `drive-motivation` | Intrinsic motivation, autonomy/mastery/purpose | `ux/research/motivation-map.md` |
| Stakeholder negotiation | `negotiation` | Stakeholder alignment, conflicting priorities | `ux/research/stakeholder-alignment.md` |
| Sentiment analysis | `analyzing-text-sentiment` | Analyze support tickets, reviews, feedback | `ux/research/sentiment-analysis.md` |
| NLP text analysis | `analyzing-text-with-nlp` | Extract themes from qualitative data | `ux/research/nlp-themes.md` |
| Data visualization | `data-visualization-helper` | Visualize research data | `ux/research/data-viz/` |
| Spec full workflow | `spec-kit:speckit-full` | Complex research needs structured planning | `ux/research/spec/` |
| Brainstorm session | `superpowers:brainstorm` | Need creative ideation before research | Referenced inline |
| Competitive UX teardown | Agent: `ux-researcher` | Competitor URLs provided | `ux/research/competitive-analysis.md` |
| Synthesize research | Agent: `ux-artifact-generator` | Raw data exists | `ux/define/` |

### Phase 2: Define & Problem Framing

| User Intent / Action | Skill to Invoke | When | File to Write |
|---------------------|----------------|------|---------------|
| Journey map | `user-journey-mapper` | Map user journeys | `ux/define/journey-maps/` |
| User stories | `user-story-generator` | User stories for backlog | `ux/define/user-stories.md` |
| Habit-forming design | `hooked-ux` | Hook Model analysis | `ux/define/hook-model.md` |
| Persuasion patterns | `influence-psychology` | Psychological influence mapping | `ux/define/influence-map.md` |
| Product positioning | `obviously-awesome` | Positioning strategy | `ux/define/positioning.md` |
| Mind map | `mindmap-generator` | Visualize concept relationships | `ux/define/mindmap.md` |
| Offer design | `hundred-million-offers` | Compelling offer creation | `ux/define/offer-design.md` |
| Traction channels | `traction-eos` | Entrepreneurial Operating System | `ux/define/traction.md` |
| Lean startup method | `lean-startup` | Build-Measure-Learn hypothesis | `ux/define/lean-hypothesis.md` |
| SaaS MVP scope | `saas-mvp-launcher` | Scoping MVP features | `ux/define/mvp-scope.md` |
| Micro SaaS scope | `micro-saas-launcher` | Lean product scope | `ux/define/micro-saas-scope.md` |
| Product design | `product-design` | End-to-end product design thinking | `ux/define/product-design.md` |
| Spec clarify | `spec-kit:speckit-clarify` | Ambiguous requirements need clarification | Referenced inline |
| Spec specify | `spec-kit:speckit-specify` | Write formal specification | `ux/define/spec/` |
| Generate personas | Agent: `ux-artifact-generator` | Research data available | `ux/define/personas/` |

### Phase 3: IA & Interaction Design

| User Intent / Action | Skill to Invoke | When | File to Write |
|---------------------|----------------|------|---------------|
| UI patterns | `ui-design-patterns` | Pattern references | Referenced inline |
| Design principles | `design-principles` | Visual design guidance | Referenced inline |
| Usability heuristics | `ux-heuristics` | Nielsen's 10 + Krug's | Referenced inline |
| Full design intelligence | `ui-ux-pro-max` | Complex design decisions with search | Referenced inline |
| Interface patterns | `interface-design` | Specific interface patterns | Referenced inline |
| Design everyday things | `design-everyday-things` | Norman's principles, affordances | Referenced inline |
| Design mastery | `design-masters` | High-level design patterns | Referenced inline |
| Design spells | `design-spells` | Design pattern library | Referenced inline |
| Flowcharts | `mermaid-flowchart-generator` | User flow diagrams | `ux/ia/flows/` |
| State diagrams | `mermaid-state-diagram-creator` | State machine diagrams | `ux/ia/state-diagrams/` |
| ER diagrams | `mermaid-er-diagram-creator` | Data model diagrams | `ux/ia/data-model/` |
| Sequence diagrams | `mermaid-sequence-diagram-creator` | Interaction sequences | `ux/ia/sequences/` |
| Class diagrams | `mermaid-class-diagram-generator` | Object model diagrams | `ux/ia/class-diagrams/` |
| Gantt charts | `mermaid-gantt-chart-generator` | Timeline/schedule diagrams | `ux/ia/timelines/` |
| Architecture diagrams | `architecture-diagram-creator` | System architecture | `ux/ia/architecture/` |
| Process flows | `process-flow-generator` | Business process flows | `ux/ia/process-flows/` |
| D2 diagrams | `d2-diagram-creator` | Complex technical diagrams | `ux/ia/d2-diagrams/` |
| PlantUML diagrams | `plantuml-diagram-generator` | UML diagrams | `ux/ia/plantuml/` |
| Graphviz diagrams | `graphviz-dot-generator` | Graph visualizations | `ux/ia/graphviz/` |
| Technical diagrams | `technical-diagram-analyzer` | Analyze existing diagrams | Referenced inline |
| Mobile IA | `mobile-design` | Mobile-specific IA patterns | Referenced inline |
| iOS patterns | `ios-hig-design` | Apple HIG compliance | Referenced inline |
| iOS HIG foundations | `hig-foundations` | HIG design foundations | Referenced inline |
| iOS HIG layout | `hig-components-layout` | HIG layout components | Referenced inline |
| iOS HIG navigation | `hig-components-menus` | HIG navigation/menus | Referenced inline |
| iOS HIG search | `hig-components-search` | HIG search patterns | Referenced inline |
| iOS HIG controls | `hig-components-controls` | HIG control components | Referenced inline |
| iOS HIG dialogs | `hig-components-dialogs` | HIG modal/dialog patterns | Referenced inline |
| iOS HIG status | `hig-components-status` | HIG status indicators | Referenced inline |
| iOS HIG content | `hig-components-content` | HIG content display | Referenced inline |
| iOS HIG inputs | `hig-inputs` | HIG input patterns | Referenced inline |
| iOS HIG patterns | `hig-patterns` | HIG UX patterns | Referenced inline |
| iOS HIG platforms | `hig-platforms` | HIG platform-specific | Referenced inline |
| SwiftUI patterns | `swiftui-expert-skill` | SwiftUI implementation | Referenced inline |
| Expo UI (iOS) | `expo-ui-swift-ui` | Expo + SwiftUI | Referenced inline |
| Expo UI (Android) | `expo-ui-jetpack-compose` | Expo + Jetpack Compose | Referenced inline |
| Spec plan | `spec-kit:speckit-plan` | Plan IA implementation | `ux/ia/spec/` |
| Component lookup | MCP: `shadcn-ui` → `search_items_in_registries` | Find UI components | Referenced inline |
| Figma design context | MCP: `plugin_figma_figma` → `get_design_context` | Read Figma designs | Referenced inline |

### Phase 4: Prototyping & Laws of UX

| User Intent / Action | Skill to Invoke | When | File to Write |
|---------------------|----------------|------|---------------|
| Full design system | `all-in-one-ui-ux-design` | End-to-end design system | `ux/prototype/design-system/` |
| Component library | `design-system-creation` | Component library + governance | `ux/prototype/components/` |
| Design system starter | `design-system-starter` | Bootstrap new design system | `ux/prototype/design-system/` |
| Design engineering | `design-engineer-mindset` | GPU/rendering/token optimization | Referenced inline |
| Baseline UI | `baseline-ui` | Starter UI component templates | `ux/prototype/baseline/` |
| Interactive artifacts | `artifacts-builder` | Interactive HTML/React prototypes | `ux/prototype/artifacts/` |
| Web artifacts | `web-artifacts-builder` | Web-based interactive artifacts | `ux/prototype/web-artifacts/` |
| Theme generation | `theme-factory` | Theme variants (dark mode, etc.) | `ux/prototype/themes/` |
| UI refactoring | `refactoring-ui` | Improving existing UI | Referenced inline |
| Typography | `web-typography` | Font pairing, type scale | `ux/prototype/typography.md` |
| Design movements | `design-movements` | Design movement inspiration | Referenced inline |
| Sticky messaging | `made-to-stick` | Memorable UI copy | Referenced inline |
| Brand narrative | `storybrand-messaging` | Narrative framework for copy | Referenced inline |
| Design orchestration | `design-orchestration` | Multi-component design coordination | Referenced inline |
| Shadcn components | `shadcn` | Shadcn/ui component usage | `ux/prototype/components/` |
| Shadcn studio | `shadcn-studio` | Shadcn studio workflow | `ux/prototype/components/` |
| Radix UI system | `radix-ui-design-system` | Radix UI primitives | `ux/prototype/components/` |
| Tailwind design system | `tailwind-design-system` | Tailwind-based design system | `ux/prototype/design-system/` |
| Tailwind patterns | `tailwind-patterns` | Tailwind utility patterns | Referenced inline |
| Tailwind theme | `tailwind-theme-builder` | Tailwind theme building | `ux/prototype/themes/` |
| Tailwind optimization | `tailwind-class-optimizer` | Optimize Tailwind classes | Referenced inline |
| Tailwind integration | `tailwindcss-framework-integration` | Framework-specific Tailwind | Referenced inline |
| Magic UI | `magic-ui-generator` | Magic UI components | `ux/prototype/components/` |
| React components | `react-component-generator` | React component generation | `ux/prototype/components/` |
| React UI patterns | `react-ui-patterns` | React UI best practices | Referenced inline |
| React hooks | `react-hook-creator` | Custom React hooks | `ux/prototype/hooks/` |
| React context | `react-context-setup` | React context/state setup | `ux/prototype/state/` |
| Vue components | `vue-component-generator` | Vue component generation | `ux/prototype/components/` |
| Vue composables | `vue-composable-creator` | Vue composables | `ux/prototype/composables/` |
| Styled components | `styled-components-helper` | CSS-in-JS styling | Referenced inline |
| CSS modules | `css-module-generator` | CSS module patterns | Referenced inline |
| Animations | `animate` | Animation principles | Referenced inline |
| Anime.js | `animejs-animation` | Anime.js animation | Referenced inline |
| CSS animations | `css-native` | CSS animation/transitions | Referenced inline |
| Scroll experience | `scroll-experience` | Scroll-driven interactions | Referenced inline |
| Motion performance | `fixing-motion-performance` | Fix animation jank | Referenced inline |
| Three.js scenes | `threejs-fundamentals` | 3D scene fundamentals | `ux/prototype/3d/` |
| Three.js animation | `threejs-animation` | 3D animation | `ux/prototype/3d/` |
| Three.js interaction | `threejs-interaction` | 3D interaction | `ux/prototype/3d/` |
| Three.js materials | `threejs-materials` | 3D materials/textures | `ux/prototype/3d/` |
| SVG icons | `svg-icon-generator` | SVG icon creation | `ux/prototype/icons/` |
| Icon library | `iconsax-library` | Iconsax icon library | Referenced inline |
| Favicon | `favicon` | Favicon generation | `ux/prototype/assets/` |
| Image optimization | `image-optimization-helper` | Image asset optimization | Referenced inline |
| OG/social meta | `open-graph-creator` | Open Graph tags | `ux/prototype/meta/` |
| SEO meta | `seo-meta-generator` | SEO metadata | `ux/prototype/meta/` |
| Color scheme | `colorize` | Color scheme generation | `ux/prototype/colors/` |
| Color contrast | `color-contrast-checker` | Check contrast during design | Referenced inline |
| Responsive analysis | `responsive-breakpoint-analyzer` | Breakpoint analysis | Referenced inline |
| Landing page | `landing-page-generator` | Landing page generation | `ux/prototype/pages/` |
| Website generation | `website-generator` | Full website generation | `ux/prototype/site/` |
| PWA manifest | `pwa-manifest-generator` | Progressive web app config | `ux/prototype/pwa/` |
| Frontend design | `frontend-design` | Frontend design patterns | Referenced inline |
| Frontend engineering | `frontend-prime` | Frontend engineering | Referenced inline |
| Senior frontend | `senior-frontend` | Senior-level patterns | Referenced inline |
| Frontend dev guide | `frontend-dev-guidelines` | Development guidelines | Referenced inline |
| Frontend developer | `frontend-developer` | Full frontend development | Referenced inline |
| Frontend UI dark TS | `frontend-ui-dark-ts` | Dark mode + TypeScript | Referenced inline |
| Frontend UI eng | `frontend-ui-engineering` | UI engineering patterns | Referenced inline |
| Remotion video | `remotion-video` | Programmatic video creation | `ux/prototype/video/` |
| Remotion | `remotion` | Video rendering | `ux/prototype/video/` |
| Figma to code | `figma:implement-design` | Implement from Figma design | `ux/prototype/` |
| Figma design rules | `figma:create-design-system-rules` | Create design system from Figma | `ux/prototype/design-system/` |
| Figma code connect | `figma:code-connect-components` | Map Figma ↔ code components | Referenced inline |
| Figma designer | `figma-friend:figma-designer` | Full Figma design workflow | Referenced inline |
| Clone UI from Figma | `figma-friend:clone-ui` | Clone UI from Figma file | `ux/prototype/` |
| Figma automation | `figma-automation` | Automate Figma workflows | Referenced inline |
| Prototype review | Agent: `ux-prototype-reviewer` | Prototype needs evaluation | `ux/validate/heuristic-evaluation.md` |

### Phase 5: Validation & Testing

| User Intent / Action | Skill to Invoke | When | File to Write |
|---------------------|----------------|------|---------------|
| WCAG accessibility | `accessibility` | WCAG 2.2 compliance | `ux/validate/accessibility/` |
| Fix accessibility | `fixing-accessibility` | Fix identified issues | `ux/validate/accessibility-fixes.md` |
| WCAG audit patterns | `wcag-audit-patterns` | Structured WCAG audit | `ux/validate/wcag-audit.md` |
| Color use (WCAG) | `use-of-color` | WCAG 1.4.1 color use check | `ux/validate/color-use.md` |
| Link purpose (WCAG) | `link-purpose` | WCAG 2.4.4 link purpose check | `ux/validate/link-purpose.md` |
| Color contrast | `color-contrast-checker` | WCAG contrast ratio validation | `ux/validate/contrast-report.md` |
| Keyboard navigation | `keyboard-navigation-tester` | Keyboard nav verification | `ux/validate/keyboard-nav.md` |
| Automated a11y scan | `scanning-accessibility` | Automated accessibility scanning | `ux/validate/a11y-scan.md` |
| Conversion optimization | `cro-methodology` | CRE conversion analysis | `ux/validate/cro-analysis.md` |
| E2E test patterns | `e2e-testing-patterns` | End-to-end testing guidance | `ux/validate/e2e-patterns.md` |
| UX specialist review | `ux-designer` | UX specialist with WCAG scripts | `ux/validate/ux-review.md` |
| UI visual validation | `ui-visual-validator` | Visual regression check | `ux/validate/visual-validation.md` |
| Visual regression | `testing-visual-regression` | Visual regression testing | `ux/validate/visual-regression.md` |
| Browser compatibility | `testing-browser-compatibility` | Cross-browser testing | `ux/validate/browser-compat.md` |
| Mobile testing | `testing-mobile-apps` | Mobile device testing | `ux/validate/mobile-testing.md` |
| Web app testing | `webapp-testing` | Full web app testing | `ux/validate/webapp-testing.md` |
| Lighthouse perf | `performance-lighthouse-runner` | Lighthouse performance audit | `ux/validate/lighthouse.md` |
| Core Web Vitals | `web-vitals-monitor` | CWV monitoring | `ux/validate/web-vitals.md` |
| Performance budgets | `validating-performance-budgets` | Performance budget check | `ux/validate/perf-budgets.md` |
| Bundle size | `bundle-size-analyzer` | Bundle size analysis | `ux/validate/bundle-analysis.md` |
| Lazy loading | `lazy-loading-implementer` | Lazy loading patterns | Referenced inline |
| Code splitting | `code-splitting-helper` | Code splitting patterns | Referenced inline |
| Security headers | `analyzing-security-headers` | Security header check | `ux/validate/security-headers.md` |
| CSP policy | `content-security-policy-generator` | Content security policy | `ux/validate/csp.md` |
| XSS scanning | `scanning-for-xss-vulnerabilities` | XSS vulnerability check | `ux/validate/xss-scan.md` |
| CORS validation | `validating-cors-policies` | CORS policy check | `ux/validate/cors.md` |
| GDPR scanning | `scanning-for-gdpr-compliance` | GDPR compliance check | `ux/validate/gdpr.md` |
| Privacy by design | `privacy-by-design` | Privacy-first validation | `ux/validate/privacy.md` |
| Spec checklist | `spec-kit:speckit-checklist` | Verify implementation completeness | Referenced inline |
| Accessibility audit | Agent: `ux-accessibility-auditor` | Live URL or component file | `ux/validate/accessibility-audit.md` |
| Lighthouse audit | MCP: `chrome-devtools` → `lighthouse_audit` | Live URL available | `ux/validate/lighthouse.md` |

### Phase 6: Design-to-Engineering Handoff

| User Intent / Action | Skill to Invoke | When | File to Write |
|---------------------|----------------|------|---------------|
| Tasks to issues | `speckit-taskstoissues` | GitHub/Linear issues from tasks | Issues created in tracker |
| Acceptance criteria | `acceptance-criteria-creator` | Given/When/Then criteria | `ux/handoff/acceptance-criteria/` |
| Definition of done | `definition-of-done-generator` | DoD checklist | `ux/handoff/dod.md` |
| Design doc | `design-doc-template` | Technical design document | `ux/handoff/design-doc.md` |
| Spec implement | `spec-kit:speckit-implement` | Implement from specification | Referenced inline |
| Spec tasks | `spec-kit:speckit-tasks` | Break spec into tasks | `ux/handoff/tasks.md` |
| GitHub issues | `github-issue-creator` | Create GitHub issues | Issues created in GitHub |
| Linear issues | `linear-issue-generator` | Create Linear issues | Issues created in Linear |
| Jira tickets | `jira-ticket-generator` | Create Jira tickets | Tickets created in Jira |
| Changelog | `changelog-generator` | Generate changelog | `ux/handoff/changelog.md` |
| Release notes | `release-notes-generator` | Generate release notes | `ux/handoff/release-notes.md` |
| API contract | `api-contract` | API contract for design | `ux/handoff/api-contract.md` |
| OpenAPI spec | `openapi-spec-generator` | Generate API spec | `ux/handoff/openapi.yaml` |
| GraphQL schema | `graphql-schema-generator` | Generate GraphQL schema | `ux/handoff/schema.graphql` |
| Database schema | `database-schema-designer` | Design database schema | `ux/handoff/db-schema.md` |
| Sprint planning | `sprint-planning-helper` | Sprint planning assistance | `ux/handoff/sprint-plan.md` |
| Sprint workflow | `sprint-workflow` | Sprint execution workflow | Referenced inline |
| Backlog grooming | `backlog-grooming-assistant` | Groom product backlog | `ux/handoff/backlog.md` |
| Figma to code | `figma:implement-design` | Implement Figma designs | Referenced inline |
| Figma code connect | `figma:code-connect-components` | Map Figma components to code | Referenced inline |
| Code review | `code-review:code-review` | Review implemented code | Referenced inline |
| Feature dev | `feature-dev:feature-dev` | Full feature development | Referenced inline |
| Handoff package | Agent: `ux-handoff-preparer` | Phase 5 complete | `ux/handoff/` |
| Component cross-ref | MCP: `shadcn-ui` → `view_items_in_registries` | Map design to components | Referenced in specs |
| Storybook gaps | MCP: `storybook-figma` → `get_component_context` | Find missing stories | `ux/handoff/storybook-gaps.md` |
| Figma design tokens | MCP: `plugin_figma_figma` → `get_variable_defs` | Extract design tokens | `ux/handoff/tokens.md` |
| Figma code map | MCP: `plugin_figma_figma` → `get_code_connect_map` | Component mappings | Referenced in specs |

### Phase 7: Post-Launch Optimization

| User Intent / Action | Skill to Invoke | When | File to Write |
|---------------------|----------------|------|---------------|
| CRO methodology | `cro-methodology` | Conversion rate optimization | `ux/optimize/cro-plan.md` |
| Hook Model audit | `hooked-ux` | Habit testing audit | `ux/optimize/hook-audit.md` |
| A/B test setup | `a-b-test-config-creator` | Configure A/B tests | `ux/optimize/ab-config.md` |
| A/B test analysis | `ab-test-analyzer` | Analyze A/B results | `ux/optimize/ab-results.md` |
| Statistical significance | `statistical-significance-calculator` | Significance validation | `ux/optimize/significance.md` |
| Funnel analysis | `funnel-analysis-builder` | Funnel visualization | `ux/optimize/funnel.md` |
| Cohort analysis | `cohort-analysis-creator` | Cohort analysis setup | `ux/optimize/cohorts.md` |
| Churn analysis | `churn-analysis-helper` | Churn prediction | `ux/optimize/churn.md` |
| Retention metrics | `retention-calculator` | Retention calculation | `ux/optimize/retention.md` |
| KPI dashboard | `kpi-dashboard-template` | KPI dashboard design | `ux/optimize/kpi-dashboard.md` |
| KPI definition | `kpi-definition-helper` | Define KPIs | `ux/optimize/kpi-definitions.md` |
| Dashboard layout | `dashboard-layout-planner` | Dashboard layout planning | `ux/optimize/dashboard-layout.md` |
| Lean methodology | `lean-startup` | Build-Measure-Learn cycles | `ux/optimize/lean-plan.md` |
| Revenue optimization | `predictable-revenue` | Revenue funnel alignment | `ux/optimize/revenue.md` |
| Marketing scorecard | `scorecard-marketing` | Marketing metrics scorecard | `ux/optimize/marketing-scorecard.md` |
| One-page marketing | `one-page-marketing` | Marketing plan | `ux/optimize/marketing-plan.md` |
| Regression analysis | `performing-regression-analysis` | Statistical regression | `ux/optimize/regression.md` |
| Anomaly detection | `anomaly-detector` | Detect metric anomalies | `ux/optimize/anomalies.md` |
| Correlation analysis | `correlation-analyzer` | Metric correlations | `ux/optimize/correlations.md` |
| Time series forecast | `forecasting-time-series-data` | Forecast metrics | `ux/optimize/forecast.md` |
| Performance bottlenecks | `detecting-performance-bottlenecks` | Perf bottleneck analysis | `ux/optimize/perf-bottlenecks.md` |
| Real user monitoring | `implementing-real-user-monitoring` | RUM implementation | `ux/optimize/rum.md` |
| Sentry error capture | `sentry-error-capture` | Error monitoring setup | `ux/optimize/error-monitoring.md` |
| Sentry performance | `sentry-performance-tracing` | Performance tracing | `ux/optimize/perf-tracing.md` |
| PostHog analytics | `posthog-hello-world` | PostHog analytics setup | `ux/optimize/posthog-setup.md` |
| Google Sheets data | `google-sheets-automation` | Automated reporting | `ux/optimize/sheets-automation.md` |
| Spec analyze | `spec-kit:speckit-analyze` | Analyze optimization results | Referenced inline |

### Cross-Phase Utilities (invoke anytime)

| User Intent / Action | Skill to Invoke | When |
|---------------------|----------------|------|
| Brand consistency | `brand-guidelines` | Any branding question |
| Brand strategy | `brand-strategy` | Strategic brand decisions |
| Brand systems | `brand-systems` | Brand system management |
| Canvas design | `canvas-design` | Custom font/canvas work |
| Design system context | `design-system-context` | Load existing design system |
| Premium SaaS design | `premium-saas-design` | SaaS-specific design |
| Design excellence | `top-design` | Design quality elevation |
| CSS animations | `css-native` | CSS animation principles |
| Frontend patterns | `frontend-prime` | Frontend engineering patterns |
| UI engineering | `frontend-ui-engineering` | UI engineering patterns |
| Prompt engineering UI | `prompt-engineering-ui` | AI prompt UI patterns |
| UI agent patterns | `ui-agent-patterns` | Agent UI patterns |
| Neurodivergent design | `neurodivergent-visual-org` | Neurodivergent-friendly design |
| Algorithmic art | `algorithmic-art` | Generative/algorithmic design |
| Infographic | `infographic-outline-creator` | Infographic design |
| Chart type recommender | `chart-type-recommender` | Choose right chart type |
| Chart.js config | `chart-js-config-creator` | Chart.js visualization |
| Plotly charts | `plotly-chart-generator` | Plotly visualization |
| Presentation outline | `presentation-slide-outliner` | Presentation design |
| Executive summary | `executive-summary-creator` | Summarize for stakeholders |
| Progress report | `progress-report` | Status reports |
| Stakeholder comms | `stakeholder-communication-template` | Stakeholder templates |
| Mermaid flowcharts | `mermaid-flowchart-generator` | Any flowchart need |
| D2 diagrams | `d2-diagram-creator` | Technical diagrams |
| ASCII diagrams | `ascii-art-diagram-creator` | Text-based diagrams |
| PDF generation | `pdf-generator` | Generate PDF reports |
| PDF parsing | `pdf-parser` | Parse PDF documents |
| DOCX creation | `anthropic-skills:docx` | Word document creation |
| XLSX creation | `anthropic-skills:xlsx` | Spreadsheet creation |
| PPTX creation | `anthropic-skills:pptx` | Presentation creation |
| Image enhancement | `image-enhancer` | Enhance images |
| Image studio | `image-studio` | Image generation/editing |

---

## Command Workflow Chains

Complex tasks benefit from chaining multiple skills. These are pre-mapped workflows:

### Research → Define → Plan (End-to-end discovery)
```
1. Skill(skill: "superpowers:brainstorm")     → Generate research hypotheses
2. Skill(skill: "jobs-to-be-done")            → JTBD analysis
3. Skill(skill: "competitive-ads-extractor")  → Competitive intelligence
4. Skill(skill: "user-journey-mapper")        → Journey maps from research
5. Skill(skill: "spec-kit:speckit-full")      → Full specification
```

### Design → Build → Validate (Prototype pipeline)
```
1. Skill(skill: "figma:implement-design")     → Get design from Figma
2. Skill(skill: "all-in-one-ui-ux-design")    → Design system setup
3. Skill(skill: "shadcn")                     → Component implementation
4. Skill(skill: "accessibility")              → Accessibility check
5. Skill(skill: "webapp-testing")             → Full validation
```

### Handoff → Ship → Monitor (Launch pipeline)
```
1. Skill(skill: "acceptance-criteria-creator") → Acceptance criteria
2. Skill(skill: "spec-kit:speckit-tasks")     → Task breakdown
3. Skill(skill: "speckit-taskstoissues")      → Create issues
4. Skill(skill: "code-review:code-review")    → Review implementation
5. Skill(skill: "sentry-error-capture")       → Error monitoring
6. Skill(skill: "posthog-hello-world")        → Analytics setup
```

### Spec-Kit Full Workflow
```
1. Skill(skill: "spec-kit:speckit-full")      → End-to-end (preferred when no spec.md exists)
--- OR chain individually: ---
1. Skill(skill: "spec-kit:speckit-analyze")   → Analyze existing code/product
2. Skill(skill: "spec-kit:speckit-clarify")   → Clarify ambiguous requirements
3. Skill(skill: "spec-kit:speckit-specify")   → Write formal specification
4. Skill(skill: "spec-kit:speckit-plan")      → Plan implementation
5. Skill(skill: "spec-kit:speckit-tasks")     → Break into tasks
6. Skill(skill: "spec-kit:speckit-implement") → Execute implementation
7. Skill(skill: "spec-kit:speckit-checklist") → Verify completeness
8. Skill(skill: "spec-kit:speckit-taskstoissues") → Create issues
```

### Superpowers Workflow
```
Skill(skill: "superpowers:brainstorm")         → Creative ideation session
Skill(skill: "superpowers:write-plan")         → Write implementation plan
Skill(skill: "superpowers:execute-plan")       → Execute plan step by step
Skill(skill: "superpowers:verification-before-completion") → Verify work
```

---

## Impeccable Standard Self-Audit

After completing any phase deliverable, run this self-audit:

### Content Quality
- [ ] Zero placeholder text (no Lorem Ipsum, no [TBD], no "TODO")
- [ ] Every claim tagged with evidence: `[EVIDENCE: source]` or `[ASSUMPTION: reason]`
- [ ] All cross-phase references resolve to existing artifacts
- [ ] Terminology is consistent across all documents

### Logical Completeness
- [ ] All 8 content states designed per screen (default, empty, loading, partial, error, success, offline, permission)
- [ ] All 5 interaction states per interactive element (default, hover, active, focus, disabled)
- [ ] Error paths documented for every flow
- [ ] Edge cases cataloged (data, timing, permission, connectivity)

### Accessibility Compliance
- [ ] WCAG 2.1 AA verified on core flows
- [ ] Color contrast ratios meet minimums (4.5:1 body, 3:1 large text)
- [ ] Keyboard navigation path documented
- [ ] ARIA labels specified for all interactive elements

### Human-Centric Reasoning
- [ ] Every design decision traces back to a user need (not business wish)
- [ ] Ethical Design Hierarchy satisfied (Rights > Functionality > Delight)
- [ ] Four-Risk Gate addressed (Value, Usability, Feasibility, Viability)
- [ ] Cognitive load managed (Hick's Law, Miller's Law verified)

### Deliverable Formatting
- [ ] Follows context-engineering.md output format rules
- [ ] Progressive disclosure applied (Executive > Findings > Detail > Appendix)
- [ ] Stakeholder calibration applied (audience-appropriate tone and depth)
- [ ] File saved to correct `ux/` subdirectory per routing table

---

## Auto-Routing Decision Tree

When receiving a user request, follow this decision flow:

```
1. Is this a new project? → Run Context Bootstrap Protocol (all 4 steps)
2. Does ux/phase-status.json exist? → Read it to determine current phase
3. If no phase-status → Invoke Agent: ux-phase-navigator
4. Based on detected phase:
   a. Match user intent to Skill Routing Table above
   b. If exact match → Invoke that skill
   c. If no match → Use phase-specific skill (ux-discover through ux-optimize)
   d. If cross-phase request → Check Cross-Phase Utilities table
5. After skill execution:
   a. Run Impeccable Standard Self-Audit
   b. Check Definition of Done (checklists/ directory)
   c. If DoD met → Recommend phase advancement
   d. If loop-back triggered → Follow rules/iteration-workflows.md
```
