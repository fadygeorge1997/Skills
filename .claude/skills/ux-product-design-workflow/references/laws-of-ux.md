# Laws of UX & Design Heuristics

## Table of Contents
1. [Predictive Models (Time & Interaction)](#predictive-models)
2. [Cognitive Bias & Memory](#cognitive-bias--memory)
3. [Gestalt Principles (Visual Perception)](#gestalt-principles)
4. [Nielsen's 10 Usability Heuristics](#nielsens-10-usability-heuristics)
5. [Application Checklist](#application-checklist)

---

## Predictive Models

### Fitts's Law
**The time to acquire a target is a function of the distance to and size of the target.**

Design implications:
- Primary CTA buttons must be prominent and easily reachable
- On mobile: place primary actions in the thumb zone (bottom-center)
- Increase touch targets to minimum 44x44px (iOS) or 48x48dp (Android)
- Reduce distance between related actions (e.g., form field and submit button)
- Edge and corner targets are fastest to reach (infinite depth on screen edges)

### Hick's Law
**Decision time increases with the number and complexity of choices.**

Design implications:
- Embrace functional minimalism — strip away extraneous options
- Progressive disclosure: show only what's needed at each step
- Break complex choices into sequential smaller decisions
- Categorize and group options to reduce cognitive load
- Highlight recommended options to simplify decision-making
- Maximum 5-7 primary navigation items

### Jakob's Law
**Users spend most of their time on other sites and prefer your site to work the same way.**

Design implications:
- Leverage established mental models and conventional interaction patterns
- Use familiar UI patterns: hamburger menu, search bar placement, cart icon
- Don't reinvent the wheel unless there's a compelling reason
- When introducing new patterns, provide clear affordances and onboarding
- Platform conventions matter: follow iOS HIG or Material Design guidelines

### Doherty Threshold
**Productivity soars when a system responds in under 300 milliseconds.**

Modern user expectations have shifted to <300ms for perceived instantaneity (updated from the original 400ms threshold established in 1982). For mobile on constrained networks, aim for <500ms with skeleton/progress indicators.

Design implications:
- Loading skeletons instead of spinners (perceived performance)
- Optimistic UI updates: show success before server confirms
- Preload predictable next actions
- Animate transitions to mask loading (300-500ms animations)
- If >1s delay is unavoidable, show progress indicators
- If >10s delay, allow background processing with notifications

### Tesler's Law (Conservation of Complexity)
**Every application has an inherent amount of complexity that cannot be removed. Ensure that as much as possible of the burden is lifted from the user.**

Design implications:
- If a task is complex, the system — not the user — should handle the complexity
- Identify irreducible complexity and absorb it into the system's logic
- Pre-fill, auto-detect, and intelligently default wherever possible
- Don't simplify the UI at the cost of pushing complexity onto the user (e.g., forcing users to format data manually)
- Accept that some features require sophisticated implementation to appear simple

### Weber's Law (Just Noticeable Difference)
**The change in a stimulus that will be just noticeable is a constant ratio of the original stimulus.**

Design implications:
- Small changes to large elements go unnoticed — make UI changes proportionally visible
- When updating prices, sizes, or spacing, the change must be proportional to the original to be perceived
- Use this principle in A/B testing: ensure variants are different enough to be noticed
- Progressive changes (slow animation of values) are perceived differently than abrupt changes
- In dark mode or theme transitions, ensure contrast changes are proportionally significant

### Postel's Law (Robustness Principle)
**Be liberal in what you accept, conservative in what you send.**

Design implications:
- Accept varied input formats (phone numbers with/without dashes, dates in multiple formats)
- Provide clear, specific output (standardized display regardless of input format)
- Forgive user errors rather than rejecting input outright
- Auto-format and auto-correct where safe to do so

---

## Cognitive Bias & Memory

### Miller's Law
**The average person can keep 7 (plus or minus 2) items in working memory.**

Design implications:
- Chunk information into digestible groups (phone numbers, credit card digits)
- Limit form sections to 5-7 fields before a visual break
- Use progressive disclosure for complex information
- Group related navigation items under clear categories
- Avoid requiring users to remember information across screens

### Peak-End Rule
**People judge an experience based on how they felt at its peak and at its end.**

Design implications:
- Design moments of delight at task completion (celebratory animations, clear success states)
- The final screen of any flow is disproportionately important
- Recovery from errors should feel empowering, not punishing
- Financial applications: confirm successful transactions with emotional warmth
- Onboarding: end with an immediate "win" that demonstrates value

### Zeigarnik Effect
**People remember uncompleted tasks better than completed ones.**

Design implications:
- Progress bars and step indicators motivate completion of multi-step processes
- Show "80% complete" profile indicators to drive engagement
- Use checklists that visually track completion
- Incomplete tasks should be salient and easy to resume
- Don't break flow unnecessarily — each interruption creates a new "incomplete" task

### Serial Position Effect
**People best remember items at the beginning and end of a list.**

Design implications:
- Place the most important items first and last in lists
- Middle items get least attention — don't hide critical actions there
- Navigation menus: most important items at start and end
- Pricing pages: place recommended plan at a visual anchor point

### Von Restorff Effect (Isolation Effect)
**An item that stands out from its peers is more likely to be remembered.**

Design implications:
- Make primary CTAs visually distinct from secondary actions
- Use color, size, or animation to draw attention to key elements
- Avoid making everything "stand out" — visual hierarchy requires contrast
- Notifications and alerts should be visually differentiated from content

### Aesthetic-Usability Effect
**Users perceive aesthetically pleasing designs as more usable.**

Design implications:
- Visual polish is not merely decorative — it builds initial trust
- Users tolerate minor usability flaws in beautiful interfaces
- First impressions are heavily influenced by visual design quality
- Invest in visual design particularly for landing pages, onboarding, and checkout
- In fintech: premium aesthetics signal security and trustworthiness

---

## Gestalt Principles

### Law of Proximity
**Elements positioned close together are perceived as a group.**

Design implications:
- Related form fields should be physically close
- Use spacing to create visual groups (not just lines or boxes)
- Group related information: account balance near recent transactions
- Separate unrelated actions with meaningful whitespace

### Law of Common Region
**Elements sharing a clearly defined boundary are perceived as a group.**

Design implications:
- Use cards, containers, and bordered sections to group related content
- Background color changes define visual regions
- Combine with proximity for stronger grouping cues
- Financial data: group related metrics within shared containers

### Law of Similarity
**Elements that look similar are perceived as part of the same group.**

Design implications:
- Use consistent styling for same-type elements (all navigation links, all form fields)
- Differentiate actionable elements from static content through visual treatment
- Status indicators should use consistent color coding across the product

### Law of Continuity
**Elements arranged on a line or curve are perceived as related.**

Design implications:
- Align elements along clear visual lines
- Use alignment to create implicit relationships
- Horizontal and vertical rhythm creates coherent layouts
- Timelines and progress indicators leverage continuity naturally

### Law of Closure
**The mind completes incomplete shapes.**

Design implications:
- Truncated lists with "show more" work because users infer continuation
- Partially visible cards at screen edge suggest scrollability
- Progress indicators don't need to show every step explicitly
- Icon design can use negative space effectively

### Figure-Ground
**People instinctively perceive objects as either in the foreground or background.**

Design implications:
- Modal overlays use dimmed backgrounds to separate figure from ground
- Active/selected states should clearly "pop" from surroundings
- Shadow and elevation create depth hierarchy
- Ensure sufficient contrast between content and background

---

## Nielsen's 10 Usability Heuristics

### 1. Visibility of System Status
Keep users informed about what's happening through timely, appropriate feedback.
- Show loading states, progress indicators, success/error confirmations
- Real-time validation on form inputs
- Sync status, connection status, processing status

### 2. Match Between System and Real World
Use language, concepts, and conventions familiar to the user.
- Avoid technical jargon; use the user's vocabulary
- Follow real-world conventions (calendar metaphor for dates)
- Cultural appropriateness in icons, imagery, and copy

### 3. User Control and Freedom
Provide clearly marked "emergency exits" — undo, cancel, back.
- Every destructive action should be reversible or require confirmation
- "Back" should always work predictably
- Allow users to cancel in-progress operations
- Undo is better than "Are you sure?" confirmations

### 4. Consistency and Standards
Follow platform and industry conventions.
- Internal consistency: same patterns throughout the product
- External consistency: follow platform conventions (iOS, Android, Web)
- Visual consistency: same colors, spacing, typography treatment for same elements

### 5. Error Prevention
Eliminate error-prone conditions before they occur.
- Constraints: date pickers prevent invalid dates
- Confirmation: "Delete this account?" with clear consequences
- Defaults: pre-fill with sensible values
- Suggestions: autocomplete to prevent typos

### 6. Recognition Rather Than Recall
Make elements, actions, and options visible; minimize memory load.
- Show recent items, search history, saved preferences
- Labels on icons (especially for infrequent actions)
- Contextual help and tooltips
- Don't require memorizing information across screens

### 7. Flexibility and Efficiency of Use
Provide shortcuts for experts while remaining accessible to novices.
- Keyboard shortcuts for power users
- Customizable dashboards and workflows
- Recent/frequent items for quick access
- Advanced search options hidden by default

### 8. Aesthetic and Minimalist Design
Remove irrelevant information; every element should serve a purpose.
- Content hierarchy: most important information first
- Reduce visual noise
- White space is a design element, not wasted space
- Progressive disclosure for complexity management

### 9. Help Users Recognize, Diagnose, and Recover from Errors
Error messages should be in plain language, indicate the problem precisely, and suggest solutions.
- "Your password must be at least 8 characters" not "Error: validation failed"
- Point to the specific field with the issue
- Suggest corrective action
- Don't lose user-entered data on error

### 10. Help and Documentation
Easy to search, task-focused, concise, with concrete steps.
- Contextual help near where users need it
- Searchable documentation
- Onboarding tutorials for complex features
- FAQ addressing common pain points

---

## Application Checklist

When designing any interface, verify against these categories:

**Interaction Efficiency:**
- [ ] Primary CTAs follow Fitts's Law (large, reachable, in thumb zone on mobile)
- [ ] Number of choices follows Hick's Law (minimal, progressive disclosure)
- [ ] Patterns follow Jakob's Law (familiar conventions)
- [ ] Response times meet Doherty Threshold (<300ms perceived)

**Cognitive Load:**
- [ ] Information is chunked per Miller's Law (7 +/- 2 groups)
- [ ] Flow endings are designed for Peak-End Rule (delight at completion)
- [ ] Multi-step processes show progress (Zeigarnik Effect)
- [ ] Visual hierarchy uses Von Restorff Effect appropriately

**Visual Perception:**
- [ ] Related elements are grouped (Proximity, Common Region)
- [ ] Same-type elements look similar (Similarity)
- [ ] Elements align on clear lines (Continuity)
- [ ] Foreground/background separation is clear (Figure-Ground)

**Usability:**
- [ ] System status is always visible (Heuristic 1)
- [ ] Language matches user's world (Heuristic 2)
- [ ] Users can undo/escape (Heuristic 3)
- [ ] Patterns are consistent (Heuristic 4)
- [ ] Errors are prevented where possible (Heuristic 5)
- [ ] Recognition over recall (Heuristic 6)
- [ ] Shortcuts for experts (Heuristic 7)
- [ ] Design is minimal and focused (Heuristic 8)
- [ ] Error messages are helpful (Heuristic 9)
- [ ] Help is available when needed (Heuristic 10)

---

## Dark Patterns: The Anti-Laws

Understanding UX laws also means recognizing when they're weaponized against users. Dark patterns exploit psychological principles to trick users into actions they didn't intend.

| Dark Pattern | UX Law Exploited | Example |
|-------------|-----------------|---------|
| **Confirmshaming** | Aesthetic-Usability | "No thanks, I don't want to save money" |
| **Roach Motel** | Jakob's Law | Easy to sign up, impossible to cancel |
| **Hidden Costs** | Peak-End Rule | Fees revealed only at final checkout step |
| **Forced Continuity** | Zeigarnik Effect | Free trial auto-converts to paid with no warning |
| **Misdirection** | Von Restorff Effect | Making the "accept all cookies" button 3x larger |
| **Trick Questions** | Miller's Law | Double negatives in consent forms |
| **Sneak into Basket** | Hick's Law | Pre-checked add-on items during checkout |

**Design with integrity.** These patterns may boost short-term metrics but destroy long-term trust. In fintech and regulated industries, they can also create legal liability.

---

## Accessibility Connection to UX Laws

Each UX law has accessibility implications:

| Law | Accessibility Connection |
|-----|------------------------|
| **Fitts's Law** | Touch targets must be 44px+ minimum; larger for motor impairments |
| **Hick's Law** | Simplification benefits users with cognitive disabilities |
| **Jakob's Law** | Following conventions aids screen reader users who learn patterns |
| **Doherty Threshold** | Loading states must be announced to screen readers |
| **Miller's Law** | Chunking helps users with attention or memory differences |
| **Gestalt: Proximity** | Visual grouping must also be semantic (proper HTML structure) |
| **Gestalt: Similarity** | Color-based grouping needs non-color alternatives |
| **Gestalt: Figure-Ground** | Sufficient contrast benefits low-vision users |

Accessibility isn't a separate concern — it's built into the same psychological principles that make interfaces usable for everyone.

---

### Cross-References
- For applying laws during competitive UX teardowns → `competitive-analysis.md`
- For state design implications (Doherty Threshold) → `ideation-prototyping.md`
- For dark pattern detection in AI interfaces → `agentic-ai-design.md`
- For MENA-specific touch zone patterns → `arabic-rtl-mena.md`
- For measuring law compliance via metrics → `metrics-optimization.md`
