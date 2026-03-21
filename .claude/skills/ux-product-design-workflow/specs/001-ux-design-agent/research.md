# Research: UX & Product Design Agent

**Feature**: 001-ux-design-agent
**Date**: 2026-03-13

## Research Questions & Decisions

### R1: Skill Architecture — Sub-skills vs Monolithic SKILL.md

**Decision**: Use a master SKILL.md orchestrator + 7 phase-specific sub-skills in `skills/` subdirectory.

**Rationale**: The existing SKILL.md (560+ lines) already serves as the master orchestrator with phase map, Quick Decision Guide, and reference file routing. Each phase has distinct enough responsibilities (different artifacts, different checklists, different reference docs) to warrant its own SKILL.md. This matches the pattern seen in `speckit-*` skills where each command has its own skill file.

**Alternatives considered**:
- **Single monolithic SKILL.md**: Rejected — already 560 lines, adding 7 phase implementations would make it unmanageable. Progressive disclosure is better served by separate files loaded on demand.
- **Flat skills (ux-discover, ux-define, etc. at top level)**: Rejected — these are semantically part of the same workflow and should be co-located under the parent skill directory.

### R2: Slash Command Registration

**Decision**: Register 7 slash commands (`/ux.discover` through `/ux.optimize`) as individual skills that can be invoked via the Skill tool.

**Rationale**: Claude Code's skill system uses SKILL.md files with frontmatter (name, description) as the registration mechanism. Skills are discovered by the system and appear in the skill list. The `speckit.*` pattern (`speckit.specify`, `speckit.plan`, `speckit.tasks`) demonstrates this approach successfully. Each skill's `description` field in frontmatter controls when it triggers.

**Alternatives considered**:
- **Claude Code commands (.claude/commands/)**: These are simpler but less portable across IDE environments. Skills are the more robust pattern.
- **MCP tools**: More powerful but heavier. Deferred to v2 (see R4).

### R3: Template and Checklist Management

**Decision**: Templates stored in `templates/` subdirectory within the skill project. Checklists stored in `checklists/`. Both referenced by phase skills at runtime.

**Rationale**: Templates define the structural contract for each artifact type. Phase skills read these templates and fill them with content derived from user input and repo context. This separates structure (template) from content (generated artifact) and allows templates to evolve independently.

**Pattern**: Each phase skill's SKILL.md includes a `templates:` section listing which templates it uses, plus instructions to read and fill them. The filled output goes to the user's `ux/` directory.

### R4: MCP Tools / Agent SDK — v1 Scope

**Decision**: Defer MCP tool exposure and Claude Agent SDK integration to v2. v1 is skill-only.

**Rationale**: The user specified MCP/SDK as "optional." The skill system provides the full capability needed for v1: phase guidance, artifact generation, context-adaptive output, checklist enforcement. MCP tools would add value for:
- Figma integration (read design tokens, export annotations)
- Analytics platform integration (pull metrics data)
- Jira/Linear integration (create UX tasks from agent output)

These integrations require API keys, authentication, and infrastructure that is out of scope for v1's "artifact-first" approach.

**v2 roadmap items**:
- `generate_persona` MCP tool: accepts research data, returns structured persona
- `run_heuristic_evaluation` MCP tool: accepts screen descriptions, returns scored evaluation
- `configure_metrics` MCP tool: generates HEART/AARRR config files for analytics platforms
- Figma MCP: read design tokens, push annotations
- Analytics MCP: pull funnel data, detect anomalies

### R5: Phase State Tracking

**Decision**: Use `ux/phase-status.json` as a lightweight JSON file in the user's project for phase tracking.

**Rationale**: JSON is machine-readable (agents can parse it), version-controlled (visible in diffs), and doesn't require a database. The schema (defined in data-model.md) tracks: current phase, DoD completion per phase, artifact inventory, user context mode, and timestamps.

**Alternatives considered**:
- **Markdown-only tracking**: Rejected — harder to parse programmatically for phase detection.
- **Separate database/service**: Rejected — violates the "everything in the repo" principle.
- **No tracking (stateless)**: Rejected — users need to know "where am I" across sessions.

### R6: Evidence Tagging System

**Decision**: Use inline tags in generated artifacts: `[EVIDENCE: source]`, `[ASSUMPTION: reason]`, `[MEASURED: metric]`.

**Rationale**: Constitution Principle V (Evidence Over Assumption) requires explicit distinction between validated evidence and assumptions. Inline tags are:
- Visible in context (not hidden in metadata)
- Searchable (grep for `[ASSUMPTION]` to find all unvalidated claims)
- Low-friction (no separate evidence database)

**Format**:
- `[EVIDENCE: interview #3, user quote]` — backed by specific research
- `[ASSUMPTION: inferred from segment behavior]` — hypothesis, needs validation
- `[MEASURED: D7 retention = 42%, analytics dashboard]` — quantified observation

### R7: Context-Adaptive Depth Inference

**Decision**: Infer context mode from project signals with explicit override via command argument.

**Rationale**: The spec requires the agent to adapt output depth (FR-008). Inference rules (defined in data-model.md) use simple heuristics: file count, presence of CI/CD, design tokens, compliance docs. These are imperfect but provide a reasonable default. Explicit `--mode mvp|growth|enterprise` overrides inference.

**Risk**: Inference may misclassify. Mitigation: agent announces its inferred mode and invites correction on first invocation.

### R8: Spec Kit Integration Points

**Decision**: UX agent integrates with Spec Kit at three lifecycle points.

**Rationale**: The user explicitly requested alignment with `speckit.specify`, `speckit.plan`, and `speckit.tasks`.

| Spec Kit Phase | UX Agent Contribution |
|----------------|----------------------|
| `/speckit.specify` | Problem statements, JTBD, user segments, opportunity areas from `/ux.define` artifacts feed into spec's User Scenarios section |
| `/speckit.plan` | IA constraints, flow requirements, state inventories from `/ux.ia` feed into plan's Technical Context and Constitution Check |
| `/speckit.tasks` | UX work items (research, design, testing, handoff) generated alongside engineering tasks with `[UX]` tag |

**Implementation**: Each UX phase skill checks for `specs/` directory and cross-references existing spec artifacts. The integration is advisory (agent suggests, human decides) — not automated pipeline.

### R9: Existing Asset Reuse

**Decision**: Reuse the existing SKILL.md and 10 reference files as-is. They form the knowledge base; phase skills are the execution layer.

**Rationale**: The existing SKILL.md + references already contain:
- Complete phase methodology (Discovery through Optimization)
- Ethical Design Hierarchy and Four-Risk Gate
- Laws of UX with design actions
- HEART + AARRR frameworks with examples
- Arabic RTL/MENA patterns
- Usability testing methodology
- Design handoff standards

Phase skills reference these files via `> Deep dive: references/[file].md` rather than duplicating content. This keeps maintenance centralized.

**What's new** (not in existing assets):
- Phase-specific SKILL.md files with execution logic
- Artifact templates with structured schemas
- DoD checklists with pass/fail tracking
- `phase-status.json` tracking schema
- Slash command contracts
- Context-adaptive output rules
