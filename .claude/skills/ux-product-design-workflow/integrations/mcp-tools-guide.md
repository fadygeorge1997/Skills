# MCP Tools Guide: UX & Product Design Workflow

This guide maps the available MCP servers to specific UX workflow phases and use cases. Use it to know which tool to reach for at each stage of the design process.

---

## MCP Server Overview

| Server | Tool Prefix | Best For |
|--------|-------------|----------|
| AccessLint | `mcp__accesslint__*` | WCAG auditing, a11y rule checking |
| Playwright | `mcp__playwright__*` | Browser automation, flow testing, screenshots |
| Chrome DevTools | `mcp__chrome-devtools__*` | Performance, network, DOM inspection |
| Claude Preview | `mcp__Claude_Preview__*` | Local component previews, hot-reload testing |
| shadcn-ui | `mcp__shadcn-ui__*` | Component registry (official shadcn) |
| shadcn-community | `mcp__shadcn-community__*` | Community components, themes, blocks |
| Storybook-Figma | `mcp__storybook-figma__*` | Design system stories, Figma file access |
| Context7 | `mcp__context7__*` | Documentation lookup for any library |
| Google Drive | *(environment-specific — configure if available)* | Research storage, team document access |

---

## Phase 1: Discovery & Research

### Competitive Analysis
```
Primary: mcp__playwright__browser_navigate + mcp__playwright__browser_take_screenshot
Fallback: mcp__chrome-devtools__navigate_page + mcp__chrome-devtools__take_screenshot
Research storage: google_drive_search (if Drive MCP is configured)
```

**Workflow:**
1. `mcp__playwright__browser_navigate` → competitor URL
2. `mcp__playwright__browser_take_screenshot` → capture each key screen
3. `mcp__chrome-devtools__lighthouse_audit` → get performance/accessibility baseline
4. `mcp__accesslint__audit_url` → accessibility scan
5. `google_drive_search (if Drive MCP is configured)` → search for existing research

**Key Playwright tools:**
- `mcp__playwright__browser_navigate` — go to URL
- `mcp__playwright__browser_take_screenshot` — capture state
- `mcp__playwright__browser_snapshot` — get accessibility tree
- `mcp__playwright__browser_console_messages` — check for JS errors
- `mcp__playwright__browser_network_requests` — observe API calls

### Research Documentation Storage
```
google_drive_search (if Drive MCP is configured) → find existing docs
google_drive_fetch (if Drive MCP is configured) → load document content
```

---

## Phase 2: Define

### Pattern Research
```
mcp__context7__resolve-library-id → find library docs
mcp__context7__query-docs → load documentation for reference
```

**Use context7 to research:**
- Design system documentation
- UX framework best practices
- Component pattern libraries
- Accessibility guidelines

**Workflow:**
1. `mcp__context7__resolve-library-id` → identify library (e.g., "react-aria", "headlessui")
2. `mcp__context7__query-docs` → load relevant docs into context
3. Apply documented patterns to artifact generation

---

## Phase 3: IA & Interaction Design

### Component Research for IA
```
mcp__shadcn-ui__list_items_in_registries → see available components
mcp__shadcn-ui__search_items_in_registries → find specific components
mcp__shadcn-ui__view_items_in_registries → get component details
mcp__shadcn-community__list_components → community component list
mcp__shadcn-community__get_component → get community component
mcp__shadcn-community__list_blocks → see page-level blocks
```

**Use when:**
- Defining navigation patterns → check shadcn navigation components
- Designing data tables → check shadcn DataTable
- Planning form interactions → check shadcn Form + validation

**Workflow:**
1. `mcp__shadcn-ui__list_items_in_registries` → see what components exist
2. `mcp__shadcn-ui__get_add_command_for_items` → get installation command
3. `mcp__shadcn-community__get_block` → for full page-level patterns

---

## Phase 4: Prototyping

### Live Preview
```
mcp__Claude_Preview__preview_start → start local preview server
mcp__Claude_Preview__preview_list → see running previews
mcp__Claude_Preview__preview_screenshot → capture current state
mcp__Claude_Preview__preview_click → interact with preview
mcp__Claude_Preview__preview_fill → fill form fields
mcp__Claude_Preview__preview_snapshot → accessibility tree
mcp__Claude_Preview__preview_logs → check for errors
mcp__Claude_Preview__preview_network → observe requests
```

**Prototyping workflow:**
1. Build or open prototype
2. `mcp__Claude_Preview__preview_start` → if local file
3. `mcp__Claude_Preview__preview_screenshot` → baseline screenshot
4. Click through key flows using `preview_click`
5. `mcp__Claude_Preview__preview_logs` → check for JS errors
6. `mcp__Claude_Preview__preview_console_logs` → monitor console

### Design System Integration
```
mcp__storybook-figma__list_storybook_tools → see available Storybook operations
mcp__storybook-figma__call_storybook_tool → query component stories
mcp__storybook-figma__list_figma_tools → see Figma operations
mcp__storybook-figma__call_figma_tool → access Figma designs
mcp__storybook-figma__get_component_context → get component info
mcp__storybook-figma__scope_design_components → scope to specific components
```

**Use when:**
- Checking if a component story exists before building custom
- Comparing prototype against Figma designs
- Validating design tokens are implemented correctly

### Theme Application
```
mcp__shadcn-community__apply_theme → apply a shadcn theme
mcp__shadcn-community__get_theme → get theme details
mcp__shadcn-community__list_themes → see available themes
```

---

## Phase 5: Validation & Testing

### Accessibility Audit
```
mcp__accesslint__audit_url → audit a live URL
mcp__accesslint__audit_file → audit a file
mcp__accesslint__audit_html → audit HTML string
mcp__accesslint__diff_html → compare before/after HTML
mcp__accesslint__list_rules → see all accessibility rules
```

**Full audit workflow:**
1. `mcp__accesslint__list_rules` → review applicable rules
2. `mcp__accesslint__audit_url` → run automated scan
3. Review each violation by severity
4. For browser hints: use `mcp__chrome-devtools__take_screenshot` to inspect visually
5. `mcp__accesslint__diff_html` → verify fixes applied

### Usability Testing Support
```
mcp__playwright__browser_navigate → set up test scenario
mcp__playwright__browser_fill_form → simulate form completion
mcp__playwright__browser_click → simulate user interactions
mcp__playwright__browser_wait_for → wait for async states
mcp__playwright__browser_take_screenshot → document findings
mcp__playwright__browser_console_messages → check for errors during task
```

### Performance Audit (Chrome DevTools)
```
mcp__chrome-devtools__lighthouse_audit → full Lighthouse audit
mcp__chrome-devtools__performance_start_trace → start recording
mcp__chrome-devtools__performance_stop_trace → stop recording
mcp__chrome-devtools__performance_analyze_insight → analyze result
```

---

## Phase 6: Design-to-Engineering Handoff

### Component Implementation Verification
```
mcp__shadcn-ui__get_audit_checklist → get component audit checklist
mcp__shadcn-ui__get_item_examples_from_registries → see usage examples
mcp__shadcn-community__get_component_demo → get component demo
mcp__shadcn-community__get_component_metadata → get metadata
```

### Figma Handoff
```
mcp__storybook-figma__call_figma_tool → access Figma content
mcp__storybook-figma__get_component_context → get design context
mcp__storybook-figma__scope_design_components → focus on specific components
```

### Accessibility Spec Verification
```
mcp__accesslint__audit_file → verify component implementation
mcp__accesslint__diff_html → verify fixes from Phase 5
```

---

## Phase 7: Post-Launch Optimization

### Live Product Analysis
```
mcp__chrome-devtools__lighthouse_audit → performance baseline
mcp__playwright__browser_navigate → navigate live product
mcp__playwright__browser_network_requests → observe API performance
mcp__chrome-devtools__performance_analyze_insight → deep performance
```

### Experiment Documentation
```
google_drive_search (if Drive MCP is configured) → find existing experiments
google_drive_fetch (if Drive MCP is configured) → load experiment results
```

---

## Quick Reference: Which Tool for Which Task?

| Task | Primary Tool | Notes |
|------|-------------|-------|
| Browse a competitor site | `mcp__playwright__browser_navigate` | |
| Take screenshots | `mcp__playwright__browser_take_screenshot` | |
| Run accessibility audit | `mcp__accesslint__audit_url` | For live URLs |
| Audit a component file | `mcp__accesslint__audit_file` | For .jsx/.tsx files |
| Preview a local component | `mcp__Claude_Preview__preview_start` | Starts local server |
| Look up design patterns | `mcp__context7__query-docs` | Library docs |
| Find shadcn component | `mcp__shadcn-ui__search_items_in_registries` | |
| Access Figma designs | `mcp__storybook-figma__call_figma_tool` | |
| Run Lighthouse audit | `mcp__chrome-devtools__lighthouse_audit` | |
| Store research to Drive | `google_drive_fetch (if Drive MCP is configured)` | |
| Check component stories | `mcp__storybook-figma__call_storybook_tool` | |
| Apply design theme | `mcp__shadcn-community__apply_theme` | |
