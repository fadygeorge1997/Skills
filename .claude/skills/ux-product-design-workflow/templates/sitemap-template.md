# Sitemap Template

## Sitemap Overview

| Attribute | Value |
|-----------|-------|
| **Product** | [Name] |
| **Version** | [Version] |
| **Created** | [Date] |
| **Owner** | [Name] |

---

## Navigation Structure

### Primary Navigation

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           PRIMARY NAV                                    │
│  [Home] │ [Section 1] │ [Section 2] │ [Section 3] │ [Section 4]        │
│    1        2             3             4             5                  │
└─────────────────────────────────────────────────────────────────────────┘
```

**Hick's Law Check:**
- Items in primary nav: [#]
- Target: ≤7 items
- Status: ✓ Pass / ✗ Needs revision

---

## Full Sitemap

```
┌─────────────────────────────────────────────────────────────────────────┐
│                              HOME (/)                                    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│  SECTION 1    │          │  SECTION 2    │          │  SECTION 3    │
│    (/[s1])    │          │    (/[s2])    │          │    (/[s3])    │
└───────┬───────┘          └───────┬───────┘          └───────┬───────┘
        │                          │                          │
   ┌────┴────┐                ┌────┴────┐                ┌────┴────┐
   │         │                │         │                │         │
   ▼         ▼                ▼         ▼                ▼         ▼
┌─────┐   ┌─────┐          ┌─────┐   ┌─────┐          ┌─────┐   ┌─────┐
│Sub  │   │Sub  │          │Sub  │   │Sub  │          │Sub  │   │Sub  │
│1.1  │   │1.2  │          │2.1  │   │2.2  │          │3.1  │   │3.2  │
└─────┘   └─────┘          └─────┘   └─────┘          └─────┘   └─────┘
```

---

## Detailed Page Inventory

### Level 1: Primary Pages

| ID | Page Name | URL | Description | Primary Action |
|----|-----------|-----|-------------|----------------|
| 1.0 | Home | / | Landing page | [Primary CTA] |
| 2.0 | [Section 1] | /[s1] | [Description] | [Action] |
| 3.0 | [Section 2] | /[s2] | [Description] | [Action] |
| 4.0 | [Section 3] | /[s3] | [Description] | [Action] |

---

### Level 2: Secondary Pages

#### Section 1 Children

| ID | Page Name | URL | Parent | Description | Type |
|----|-----------|-----|--------|-------------|------|
| 1.1 | [Sub Page] | /[s1]/[sub] | 1.0 | [Description] | [List/Detail/Form] |
| 1.2 | [Sub Page] | /[s1]/[sub] | 1.0 | [Description] | [Type] |

#### Section 2 Children

| ID | Page Name | URL | Parent | Description | Type |
|----|-----------|-----|--------|-------------|------|
| 2.1 | [Sub Page] | /[s2]/[sub] | 2.0 | [Description] | [Type] |
| 2.2 | [Sub Page] | /[s2]/[sub] | 2.0 | [Description] | [Type] |

---

### Level 3: Tertiary Pages (if applicable)

| ID | Page Name | URL | Parent | Description |
|----|-----------|-----|--------|-------------|
| 1.1.1 | [Page] | /[path] | 1.1 | [Description] |

---

## Navigation Zones

### Primary Navigation

| Item | Icon | Label | Active State | Badge |
|------|------|-------|--------------|-------|
| Home | [Icon] | Home | [Style] | - |
| [Section 1] | [Icon] | [Label] | [Style] | [Optional] |

### Secondary Navigation

| Item | Placement | Trigger | Contents |
|------|-----------|---------|----------|
| [Utility] | Header right | Click | [Links] |
| [Search] | Header | Click/Icon | Search input |
| [Notifications] | Header | Icon | Notification list |
| [Profile] | Header | Avatar | Account menu |

### Footer Navigation

| Section | Links |
|---------|-------|
| Company | [About], [Careers], [Press] |
| Legal | [Terms], [Privacy], [Cookies] |
| Support | [Help], [Contact], [FAQ] |

---

## Mental Model Alignment

### User Mental Model

| User Group | Expected Navigation | Actual Mapping | Gap |
|------------|--------------------| ---------------|-----|
| [Persona 1] | [How they think about content] | [Where it actually is] | [Any mismatch] |
| [Persona 2] | [Mental model] | [Mapping] | [Gap] |

### Card Sorting Validation

| Method | Participants | Key Findings |
|--------|--------------|--------------|
| [Open/Closed] | [#] | [What we learned] |

---

## Page Type Classification

| Type | Pages | Template | Notes |
|------|-------|----------|-------|
| **Landing** | [List] | [Template name] | [Special considerations] |
| **List/Dashboard** | [List] | [Template] | [Notes] |
| **Detail** | [List] | [Template] | [Notes] |
| **Form** | [List] | [Template] | [Notes] |
| **Settings** | [List] | [Template] | [Notes] |

---

## URL Structure

### URL Patterns

| Pattern | Example | Purpose |
|---------|---------|---------|
| /section | /products | Section landing |
| /section/item | /products/widget | Detail page |
| /section/item/action | /products/widget/edit | Action page |

### URL Naming Conventions

- **Use:** lowercase, hyphens for spaces (`/my-account`)
- **Avoid:** underscores, camelCase, special characters
- **Parameters:** Use query strings for filters (`/products?category=shoes`)

---

## Search & Discovery

### Search Scope

| Search Type | Scope | Results Page |
|-------------|-------|--------------|
| Global search | All content | /search?q=[query] |
| Section search | Section only | /[section]/search?q=[query] |

### Search Results

| Content Type | Display | Click Behavior |
|--------------|---------|----------------|
| [Page type] | [How shown] | [Where it goes] |

---

## Cross-References

### User Flow Connections

| Flow | Entry Point | Pages Used | Exit Point |
|------|-------------|------------|------------|
| [Flow name] | [Start page] | [Pages] | [End page] |

---

## Hick's Law Validation

| Navigation Level | Item Count | Target | Status |
|------------------|------------|--------|--------|
| Primary nav | [#] | ≤7 | ✓/✗ |
| Secondary nav | [#] | ≤7 | ✓/✗ |
| Footer columns | [#] | ≤5 | ✓/✗ |

---

## Tree Testing Results (if conducted)

| Task | Success Rate | Target | Status |
|------|--------------|--------|--------|
| [Task 1] | [%] | >80% | ✓/✗ |
| [Task 2] | [%] | >80% | ✓/✗ |

---

## Connected Artifacts

| Artifact | Relationship | Link |
|----------|--------------|------|
| Personas | [Mental model alignment] | [Link] |
| Card Sorting | [Validation data] | [Link] |
| User Flows | [How users navigate] | [Link] |

---

## Metadata

| Field | Value |
|-------|-------|
| Created | [Date] |
| Created By | [Name] |
| Last Updated | [Date] |
| Version | [Version] |
