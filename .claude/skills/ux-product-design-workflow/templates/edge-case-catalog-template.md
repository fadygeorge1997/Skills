# Edge Case Catalog Template

## Catalog Overview

| Attribute | Value |
|-----------|-------|
| **Product/Feature** | [Name] |
| **Version** | [Version] |
| **Created** | [Date] |
| **Owner** | [Name] |
| **Total Edge Cases** | [#] |

---

## Edge Case Categories

### 1. Data Edge Cases

Edge cases related to data content, structure, and availability.

| ID | Scenario | Handling | Error Message | User Action | Status |
|----|----------|----------|---------------|-------------|--------|
| D1 | **Empty data** - No items in list | Show empty state with CTA | N/A | "Add your first [item]" | ✓/✗ |
| D2 | **Null values** - Field is null | Show placeholder or hide field | N/A | — | ✓/✗ |
| D3 | **Very long text** - Text exceeds display | Truncate with ellipsis + tooltip | N/A | Tap to expand | ✓/✗ |
| D4 | **Special characters** - Emojis, symbols in input | Sanitize/escape before display | "Some characters aren't allowed" | Re-enter | ✓/✗ |
| D5 | **Negative numbers** - Unexpected negative values | Handle per business rules | N/A | — | ✓/✗ |
| D6 | **Zero values** - Zero in calculation/display | Show appropriate message | N/A | — | ✓/✗ |
| D7 | **Overflow** - Values exceed maximum | Cap at max, show warning | "Value exceeds limit" | Adjust value | ✓/✗ |
| D8 | **Invalid format** - Wrong data format | Validate before submission | "Expected format: [format]" | Correct format | ✓/✗ |
| D9 | **Duplicate data** - Duplicate entries | Prevent or merge | "[Item] already exists" | Acknowledge | ✓/✗ |
| D10 | **Data mismatch** - Inconsistent related data | Reconcile or flag | "Data inconsistency detected" | Contact support | ✓/✗ |

---

### 2. Timing Edge Cases

Edge cases related to sequence, speed, and concurrency.

| ID | Scenario | Handling | Error Message | User Action | Status |
|----|----------|----------|---------------|-------------|--------|
| T1 | **Slow network** - Request takes >5s | Show progress, allow cancel | "Still loading..." | Wait or cancel | ✓/✗ |
| T2 | **Timeout** - Request exceeds limit | Show timeout error with retry | "Request timed out. Try again?" | Retry | ✓/✗ |
| T3 | **Race condition** - Multiple simultaneous requests | Debounce, cancel previous | N/A | — | ✓/✗ |
| T4 | **Concurrent edits** - Two users edit same data | Lock or merge with conflict UI | "[User] is editing this" | Wait or force edit | ✓/✗ |
| T5 | **Stale data** - Data changed since load | Refresh or prompt user | "This data has changed. Refresh?" | Refresh | ✓/✗ |
| T6 | **Action interrupted** - User leaves mid-flow | Save progress or warn | "Save your progress?" | Save or discard | ✓/✗ |
| T7 | **Session timeout** - Session expires mid-action | Preserve data, prompt re-login | "Session expired. Please log in." | Re-login | ✓/✗ |
| T8 | **Background refresh** - Data updates while viewing | Update smoothly or notify | "Updated with new data" | — | ✓/✗ |

---

### 3. Permission Edge Cases

Edge cases related to access, authorization, and permissions.

| ID | Scenario | Handling | Error Message | User Action | Status |
|----|----------|----------|---------------|-------------|--------|
| P1 | **Not logged in** - Unauthenticated access | Redirect to login, preserve destination | "Log in to continue" | Log in | ✓/✗ |
| P2 | **Insufficient permissions** - User lacks access | Explain limitation, offer upgrade | "You need [permission] to do this" | Request access | ✓/✗ |
| P3 | **Permission revoked mid-session** - Access removed during use | Notify, limit access gracefully | "Your access has changed" | Contact admin | ✓/✗ |
| P4 | **Expired credentials** - Password/token expired | Prompt re-authentication | "Your session has expired" | Re-authenticate | ✓/✗ |
| P5 | **Account suspended** - Account disabled | Explain situation | "Account suspended. Contact support." | Contact support | ✓/✗ |
| P6 | **Feature locked** - Premium feature access | Show upgrade prompt | "Unlock with [Plan]" | Upgrade | ✓/✗ |
| P7 | **Location permission denied** - Required location not granted | Explain why needed | "Location needed for [feature]" | Grant or skip | ✓/✗ |
| P8 | **Camera/microphone denied** - Media permission denied | Explain why needed | "Camera needed to [action]" | Grant or skip | ✓/✗ |

---

### 4. Connectivity Edge Cases

Edge cases related to network and connectivity.

| ID | Scenario | Handling | Error Message | User Action | Status |
|----|----------|----------|---------------|-------------|--------|
| C1 | **Offline** - No network connection | Show cached content, queue actions | "You're offline. Some features unavailable." | Retry when online | ✓/✗ |
| C2 | **Intermittent connection** - Unstable network | Retry with exponential backoff | "Connection unstable. Retrying..." | Wait or retry manually | ✓/✗ |
| C3 | **Slow network (2G/3G)** - Very slow connection | Optimize for low bandwidth | "Loading on slow connection..." | Wait | ✓/✗ |
| C4 | **WiFi to cellular switch** - Network change mid-action | Resume or restart gracefully | "Network changed. Reconnecting..." | — | ✓/✗ |
| C5 | **Airplane mode** - Device in airplane mode | Detect and inform | "Airplane mode is on" | Disable airplane mode | ✓/✗ |
| C6 | **Connection lost mid-upload** - Upload interrupted | Pause and resume or restart | "Upload paused. Resume when online." | Resume manually | ✓/✗ |
| C7 | **Server unreachable** - Backend down | Show status, offer retry | "Service temporarily unavailable" | Retry | ✓/✗ |
| C8 | **API rate limited** - Too many requests | Queue requests, inform user | "Too many requests. Wait a moment." | Wait | ✓/✗ |

---

## Edge Case Summary Matrix

| Category | Total | Handled | Unhandled | Priority |
|----------|-------|---------|-----------|----------|
| Data | [#] | [#] | [#] | [H/M/L] |
| Timing | [#] | [#] | [#] | [H/M/L] |
| Permission | [#] | [#] | [#] | [H/M/L] |
| Connectivity | [#] | [#] | [#] | [H/M/L] |
| **Total** | [#] | [#] | [#] | — |

---

## Edge Case by Screen/Flow

### [Screen Name 1]

| ID | Scenario | Handling | Status |
|----|----------|----------|--------|
| [ID] | [Scenario] | [How it's handled] | ✓/✗ |

### [Screen Name 2]

| ID | Scenario | Handling | Status |
|----|----------|----------|--------|
| [ID] | [Scenario] | [How it's handled] | ✓/✗ |

---

## Unhandled Edge Cases (Priority Fixes)

| ID | Scenario | Impact | Effort | Priority | Owner |
|----|----------|--------|--------|----------|-------|
| [ID] | [Scenario] | [High/Medium/Low] | [H/M/L] | [1-5] | [Name] |
| [ID] | [Scenario] | [Impact] | [Effort] | [Priority] | [Owner] |

---

## Error Message Review

### Current Error Messages

| Scenario | Current Message | Tone | Actionable? | Improvement |
|----------|-----------------|------|-------------|-------------|
| [Scenario] | [Current copy] | [Appropriate/Harsh/Vague] | [Yes/No] | [Better version] |

### Error Message Guidelines

**Good Error Message Structure:**
`[What happened]` + `[Why it matters]` + `[What to do next]`

**Examples:**

| Bad | Good |
|-----|------|
| "Error 500" | "Something went wrong on our end. Please try again in a moment." |
| "Invalid input" | "That email format didn't work. Try something like name@example.com" |
| "User not found" | "We couldn't find an account with that email. Want to sign up?" |

---

## Testing Checklist

### Data Edge Cases to Test

- [ ] Empty list/state
- [ ] Maximum character limit
- [ ] Special characters in inputs
- [ ] Negative numbers
- [ ] Zero values
- [ ] Duplicate submissions

### Timing Edge Cases to Test

- [ ] Slow network (throttle to 3G)
- [ ] Request timeout
- [ ] Multiple rapid submissions
- [ ] Background/foreground transitions

### Permission Edge Cases to Test

- [ ] Logged out state
- [ ] Insufficient permissions
- [ ] Permission denied mid-flow
- [ ] Session expiration

### Connectivity Edge Cases to Test

- [ ] Offline mode
- [ ] Intermittent connection
- [ ] Network switch (WiFi to cellular)
- [ ] Server unavailable

---

## Connected Artifacts

| Artifact | Relationship | Link |
|----------|--------------|------|
| State Inventory | [States that handle edge cases] | [Link] |
| User Flows | [Flows with edge case branches] | [Link] |
| Acceptance Criteria | [Edge case scenarios to test] | [Link] |
| Handoff Docs | [Where edge cases are documented] | [Link] |

---

## Metadata

| Field | Value |
|-------|-------|
| Created | [Date] |
| Created By | [Name] |
| Last Updated | [Date] |
| Version | [Version] |
