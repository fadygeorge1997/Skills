# Claude Code UX/UI Complete Toolkit
### Every Tool, Plugin, Skill, and MCP Server for Design & Frontend Work
*Deep Research — March 2026*

---

## 1. BUILT-IN SKILLS (Available in Claude.ai & Claude Code)

These are Anthropic's official skills that ship with Claude Code or are available in the skills directory.

### 1.1 Frontend Design Skill
- **Source:** `anthropics/skills` → `skills/frontend-design/`
- **What it does:** Breaks Claude out of "AI slop" aesthetics (generic purple gradients, Inter font, predictable layouts). Forces Claude to think through purpose, tone, constraints, and differentiation before writing any code.
- **Key features:**
  - Distinctive typography (no generic fonts like Arial, Inter, Roboto)
  - Intentional color palettes with CSS variables
  - Motion/animations via CSS or Motion library
  - Asymmetric layouts, overlap, diagonal flow
  - Gradient meshes, noise textures, geometric patterns, grain overlays

### 1.2 Canvas Design Skill
- **Source:** `/mnt/skills/examples/canvas-design/`
- **What it does:** Creates museum-quality visual art as `.png` and `.pdf` using a two-phase process: first generates a design philosophy manifesto, then expresses it visually on canvas.
- **Best for:** Posters, visual art, branding materials, static design pieces

### 1.3 Theme Factory Skill
- **Source:** `/mnt/skills/examples/theme-factory/`
- **What it does:** 10 pre-built professional themes (colors + fonts) that can be applied to any artifact (slides, docs, HTML pages, reports). Can also generate custom themes on-the-fly.
- **Themes include:** Ocean Depths, Sunset Boulevard, Forest Canopy, Modern Minimalist, Golden Hour, Arctic Frost, Desert Rose, Tech Innovation, Botanical Garden, Midnight Galaxy

### 1.4 Web Artifacts Builder Skill
- **Source:** `/mnt/skills/examples/web-artifacts-builder/`
- **Stack:** React 18 + TypeScript + Vite + Parcel + Tailwind CSS + shadcn/ui
- **What it does:** Builds complex, multi-component Claude.ai HTML artifacts with state management, routing, and 40+ shadcn/ui components pre-installed
- **Setup:** `bash scripts/init-artifact.sh <project-name>` → develop → `bash scripts/bundle-artifact.sh` → single HTML output

### 1.5 Algorithmic Art Skill
- **Source:** `/mnt/skills/examples/algorithmic-art/`
- **What it does:** Creates generative art using p5.js with seeded randomness and interactive parameter exploration
- **Best for:** Flow fields, particle systems, generative patterns, computational aesthetics

### 1.6 Brand Guidelines Skill
- **Source:** `anthropics/skills`
- **What it does:** Applies Anthropic's official brand colors and typography to artifacts

### 1.7 MCP Builder Skill
- **Source:** `/mnt/skills/examples/mcp-builder/`
- **What it does:** Guide for creating high-quality MCP servers (TypeScript or Python) to integrate external APIs and services into Claude Code workflows

---

## 2. COMMUNITY PLUGINS (Install via Claude Code Plugin Marketplace)

### 2.1 UI/UX Pro Max
- **Source:** `nextlevelbuilder/ui-ux-pro-max-skill`
- **Website:** https://ui-ux-pro-max-skill.nextlevelbuilder.io/
- **What it does:** The most comprehensive design intelligence skill in the ecosystem
- **Database includes:**
  - 50+ UI styles
  - 97 color palettes
  - 57 font pairings
  - 99 UX guidelines
  - 25 chart types
  - 9 technology stacks (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui)
- **Workflow:** Requirements analysis → `--design-system` search → targeted domain searches → stack guidelines → implementation
- **Install:** Available on LobeHub Skills Marketplace and Claude plugin registries

### 2.2 Interface Design Plugin
- **Source:** `Dammyjay93/interface-design`
- **Install:** `/plugin marketplace add Dammyjay93/interface-design`
- **What it does:** Design engineering for dashboards, apps, tools, and admin panels. Enforces consistent design decisions (spacing, colors, depth, elevation) across sessions.
- **Key feature:** Creates `.interface-design/system.md` that persists design decisions. Claude reads this before every component and applies established patterns automatically.

### 2.3 LibreUIUX-Claude-Code
- **Source:** `HermeticOrmus/LibreUIUX-Claude-Code`
- **Scale:** 152 agents, 70 plugins, 76 commands, 74 skills
- **What it does:** Complete UI/UX system for Claude Code covering:
  - Design mastery (agents, commands, skills)
  - Accessibility compliance (WCAG, ARIA, a11y testing)
  - Frontend & mobile development (React, Vue, React Native)
  - Backend development (APIs, databases, architecture)
  - CI/CD automation

### 2.4 UI Designer Plugin (ClaudePluginHub)
- **Source:** ClaudePluginHub
- **What it does:** Sprint-focused UI design agent with 50 styles, 21 palettes, 50 font pairings, 20 chart types, 9 stacks
- **Styles supported:** Glassmorphism, claymorphism, minimalism, brutalism, neumorphism, bento grid, dark mode, skeuomorphism, flat design

### 2.5 Superpowers Plugin
- **Source:** `obra/superpowers`
- **What it does:** 20+ battle-tested skills including TDD, debugging, brainstorming, code review, and collaboration patterns. Structured lifecycle planning with skills framework.

### 2.6 Ralph Wiggum Plugin (Visual Testing)
- **Source:** Anthropic marketplace
- **What it does:** Visual testing for apps (especially Swift). Uses Xcode MCP to bridge Claude and running simulator for automated UI and functionality checks.

### 2.7 Dev-Browser Plugin
- **What it does:** Lightweight, faster browsing/testing alternative to Playwright with lower context overhead

### 2.8 Plannotator
- **What it does:** Visual plan review for Claude Code — structured, annotated plans you can review and share

### 2.9 Claude Code Plugins Plus
- **Source:** `jeremylongshore/claude-code-plugins-plus-skills`
- **Scale:** 339 plugins + 1,896 agent skills
- **Frontend skills included:** UI/UX improvements, responsive design, accessibility
- **All validated against Anthropic's 2026 schema**

---

## 3. MCP SERVERS FOR DESIGN

### 3.1 Figma MCP Server (Official — Remote)
- **URL:** `https://mcp.figma.com/mcp`
- **Install (Claude Code):** `claude mcp add --transport http figma https://mcp.figma.com/mcp`
- **Or via plugin:** `claude plugin install figma@claude-plugins-official`
- **Capabilities:**
  - **Design → Code:** Select a Figma frame, paste link into Claude Code, get implementation
  - **Code → Design (Claude Code to Figma):** Type "Send this to Figma" to capture live UI as editable Figma layers
  - **Code Connect:** Pull variables, components, and layout data directly into IDE
  - **FigJam access:** Read content from FigJam diagrams
  - **Multi-screen capture:** Capture entire flows preserving sequence and context
- **Requirements:** Figma Dev or Full seat, Claude Code installed

### 3.2 Figma MCP Server (Desktop/Local)
- **Runs locally:** `http://127.0.0.1:3845/sse`
- **Install:** Enable in Figma Desktop App → Preferences → "Dev Mode MCP Server"
- **Claude Code:** `claude mcp add --transport sse figma-dev-mode-mcp-server http://127.0.0.1:3845/sse`
- **Advantage:** Direct frame selection in desktop app

### 3.3 Composio Figma MCP
- **Source:** `mcp.composio.dev`
- **Install:** `npx @composio/mcp@latest setup "<URL>" "figma-605dcr-13" --client`
- **Advantage:** Works with free Figma accounts, supports Cursor too

### 3.4 Figma-Friend Plugin (Browser-Based)
- **Source:** `markacianfrani/claude-code-figma`
- **Install:** `/plugin marketplace add markacianfrani/claude-code-figma`
- **How it works:** Uses Chrome DevTools MCP to access Figma's plugin API directly in the browser. Claude writes and executes code against Figma's API instead of clicking/dragging.
- **Advantage:** Can manipulate Figma designs, not just read them

### 3.5 Figma CLI (No MCP Needed)
- **Source:** `silships/figma-cli`
- **What it does:** Connects Claude Code to Figma through DevTools in 60 seconds
- **Advantage:** No API key, no JSON config, burns fewer tokens, works with free Figma accounts

### 3.6 shadcn/ui MCP Server (Official)
- **Install:** `claude mcp add shadcn -- npx shadcn@latest mcp`
- **Config (`.mcp.json`):**
  ```json
  { "mcpServers": { "shadcn": { "command": "npx", "args": ["shadcn@latest", "mcp"] } } }
  ```
- **Capabilities:**
  - Browse all available components, blocks, and templates
  - Search across multiple registries (public + private)
  - Install components with natural language
  - Access private company registries with auth

### 3.7 shadcn/ui MCP Server (Community — Multi-Framework)
- **Source:** `Jpisnice/shadcn-ui-mcp-server`
- **Frameworks:** React, Svelte, Vue, React Native
- **Install:** `claude mcp add shadcn -- bunx -y @jpisnice/shadcn-ui-mcp-server --github-api-key YOUR_TOKEN`
- **Features:** Component source code, demos, blocks, metadata, directory browsing

### 3.8 shadcn Studio MCP Server
- **Source:** shadcnstudio.com
- **Commands:** `/cui` (create UI), `/iui` (improve UI), `/rui` (refine UI), `/ftc` (Figma to Code)
- **Features:** AI theme generator, Figma-to-code plugin, Copy Prompt for v0/Bolt/Lovable

### 3.9 v0 MCP Server (Vercel)
- **Source:** `hellolucky/v0-mcp`
- **Tools:**
  - `v0_generate_ui` — Generate UI components from text
  - `v0_generate_from_image` — Convert design images to React code
  - `v0_chat_complete` — Iterative UI development chat
- **Models:** v0-1.5-md, v0-1.5-lg, v0-1.0-md

### 3.10 Playwright MCP Server (Microsoft Official)
- **Install:** `claude mcp add playwright npx @playwright/mcp@latest`
- **What it does:** 34 browser automation tools via accessibility tree (not screenshots)
- **Key tools:** `browser_navigate`, `browser_click`, `browser_type`, `browser_take_screenshot`, `browser_snapshot`
- **UX use cases:**
  - Self-QA: Build a feature, then tell Claude to verify it visually
  - Visual regression testing
  - Automated UI testing
  - Generating Playwright test files from real interactions
  - Auth handling (login manually, Claude continues with cookies)
- **Playwright Agents (v1.56+):** Planner, Generator, and Healer subagents for structured test automation

### 3.11 Storybook MCP Server
- **Source:** `pieter365-mcp-server`
- **What it does:** Works with Storybook stories and React components
- **Capabilities:** List stories, convert stories to standalone components, generate stories for components, audit component/story prop mismatches, migrate CSF2 → CSF3

### 3.12 Storybook-Figma MCP (Combined)
- **Source:** `vahapa221328-storybook-figma-mcp`
- **What it does:** Merges Storybook component metadata and Figma design context into single rich context
- **Framework-agnostic:** Works with React, Vue, Svelte, Angular
- **Key feature:** Tells AI which components are ready to use, which need updates, and which need to be built from scratch

### 3.13 Chrome DevTools MCP
- **Install:** `claude mcp add chrome-devtools npx chrome-devtools-mcp@latest`
- **What it does:** Controls and inspects a live Chrome browser for automation, debugging, and performance analysis
- **Used by:** Figma-Friend plugin for direct Figma manipulation

### 3.14 AccessLint MCP Server
- **Source:** `accesslint/claude-marketplace`
- **What it does:** Dedicated accessibility toolkit with bundled MCP server for programmatic color contrast analysis
- **Skills included:** contrast-checker, refactor, use-of-color, link-purpose
- **Agent:** `accesslint:reviewer` performs comprehensive WCAG 2.1 Level A/AA audits

### 3.15 Context7 MCP (Upstash)
- **What it does:** Pulls version-specific documentation and code examples from source repositories into your LLM context
- **Use case:** Always up-to-date docs for any UI framework or library

---

## 4. SKILLS & SKILL SETS (Install via `npx skills add`)

### 4.1 shadcn/ui Skills
- **Install:** `npx skills add shadcn/ui`
- **What it does:** Detects `components.json`, runs `shadcn info --json`, feeds AI your exact project setup (correct variant names, color variables, import paths)

### 4.2 Vercel Web Design Guidelines
- **What it does:** Ensures accessibility standards and web best practices compliance

### 4.3 Vercel React Best Practices
- **What it does:** Performance and architecture patterns for professional component libraries

### 4.4 Vercel Composition Patterns
- **What it does:** React composition patterns for scalable UI architectures

### 4.5 Vercel React Native Skills
- **What it does:** Mobile-specific patterns and best practices

### 4.6 AccessLint Skills
- **Skills:** contrast-checker, refactor, use-of-color, link-purpose
- **Agent:** `accesslint:reviewer` for comprehensive accessibility audits

---

## 5. DESIGN SYSTEM & WORKFLOW INTEGRATION

### 5.1 The "3 Settings" Stack for shadcn/ui
Best practice setup for high-quality AI-generated UI:
1. **Project context:** `npx skills add shadcn/ui`
2. **Live docs:** `claude mcp add shadcn -- npx shadcn@latest mcp`
3. **Design system:** `npx shadcn@latest init --preset <preset_id>`

### 5.2 Figma + Code Connect Workflow
- Design components in Figma with proper naming/tokens
- Connect to source code via Code Connect
- Figma MCP gives AI both design context and production awareness
- Claude Code reuses proper tokens, syntax, and patterns from codebase

### 5.3 CLAUDE.md Pattern
Create a `CLAUDE.md` in your project root with:
- Design system rules (spacing, colors, depth strategy)
- Component naming conventions
- Typography and font stack
- Preferred patterns and anti-patterns
- Claude reads this automatically every session

---

## 6. PLUGIN MARKETPLACES & REGISTRIES

| Marketplace | URL | Notes |
|------------|-----|-------|
| **Anthropic Official** | Via `claude plugin install` | Official plugins |
| **BuildWithClaude** | https://buildwithclaude.com | Plugin marketplace |
| **ClaudePluginHub** | https://claudepluginhub.com | Community plugins |
| **ClaudeMarketplaces** | https://claudemarketplaces.com | Plugin discovery |
| **claude-plugins.dev** | https://claude-plugins.dev/skills | Auto-indexed, 34,000+ skills |
| **LobeHub Skills** | https://lobehub.com/skills | Skills marketplace |
| **Awesome Claude Plugins** | github.com/composio/awesome-claude-plugins | Curated registry |
| **Awesome Claude Skills** | github.com/travisvn/awesome-claude-skills | Curated skills list |

---

## 7. VISUAL TESTING TOOLS

| Tool | Type | Best For |
|------|------|----------|
| **Playwright MCP (Microsoft)** | MCP Server | Self-QA, accessibility-tree testing, test generation |
| **Ralph Wiggum Plugin** | Plugin | Swift/Xcode visual testing |
| **Dev-Browser Plugin** | Plugin | Lightweight browser testing |
| **Playwright CLI** | CLI | CI/CD repeatable tests |
| **Claude-Playwright Toolkit** | MCP + CLI | Session management, profile management, test saving |

---

## 8. RECOMMENDED SETUP MATRIX

### For a Solo Designer/Developer:
```
1. shadcn/ui Skills + MCP Server
2. Figma MCP (remote)
3. Playwright MCP
4. UI/UX Pro Max skill
5. Frontend Design skill (built-in)
```

### For a Design System Team:
```
1. shadcn/ui Skills + MCP + Preset
2. Figma MCP + Code Connect
3. Storybook-Figma MCP
4. AccessLint skills + MCP
5. Interface Design plugin
6. CLAUDE.md with design tokens
```

### For Rapid Prototyping:
```
1. v0 MCP Server
2. Figma MCP (for code-to-canvas)
3. Web Artifacts Builder skill
4. Frontend Design skill
5. Theme Factory skill
```

---

## 9. KEY COMMANDS REFERENCE

```bash
# Figma MCP (remote)
claude mcp add --transport http figma https://mcp.figma.com/mcp

# Figma MCP (local/desktop)
claude mcp add --transport sse figma-dev-mode-mcp-server http://127.0.0.1:3845/sse

# shadcn/ui MCP
claude mcp add shadcn -- npx shadcn@latest mcp

# Playwright MCP
claude mcp add playwright npx @playwright/mcp@latest

# Chrome DevTools MCP
claude mcp add chrome-devtools npx chrome-devtools-mcp@latest

# shadcn/ui Skills
npx skills add shadcn/ui

# Check MCP status
/mcp

# Install plugins
/plugin marketplace add <author>/<plugin-name>
/plugin menu
```

---

*Sources: Figma Blog, Snyk, Composio, Builder.io, LobeHub, uxdesign.cc, proofsource.ai, shadcn.com, dev.to, various GitHub repositories. Compiled March 2026.*
