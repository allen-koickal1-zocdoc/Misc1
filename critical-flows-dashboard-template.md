# Critical Flows Dashboard Template

## How to Use

1. Create a new Google Sheet
2. Create the sheets listed below
3. Copy the data and formulas

---

## Sheet 1: "Instructions"

```
CRITICAL FLOWS TRACKING - INSTRUCTIONS

PURPOSE:
Track all business-critical flows and their test automation coverage across QA pods.

FIELD DEFINITIONS:

| Field | Description | Valid Values |
|-------|-------------|--------------|
| Flow ID | Unique identifier | Format: {TEAM}-{NNN} (e.g., BOOK-001, SEARCH-005) |
| Flow Name | Descriptive name | Free text |
| Priority | Business criticality | P0 = Revenue-blocking, P1 = Core experience, P2 = Important |
| Flow Type | Category | Booking, Auth, Search, Payment, Dashboard, Profile, Settings, Messaging |
| Description | What the flow does | 1-2 sentences |
| Entry Point | Where flow starts | URL or user action |
| Happy Path Steps | Golden path | Numbered steps |
| Edge Cases | Alternative scenarios | Bullet list |
| Automation Status | Current state | ✅ Automated, 🟡 Partial, ❌ Manual Only, 🚫 None |
| Test Location | Path to spec file | File path or "N/A" |
| CI Included | Runs in CI pipeline | Yes / No |
| Last Validated | Last confirmation date | YYYY-MM-DD |
| Owner | Responsible QAE | Name |
| Notes | Additional context | Free text |

AUTOMATION STATUS DEFINITIONS:

✅ Automated - Full happy path covered in automated tests
🟡 Partial - Some steps automated, gaps remain  
❌ Manual Only - Tested manually, no automation exists
🚫 None - No test coverage (manual or automated)

PRIORITY DEFINITIONS:

P0 - Revenue-blocking: Failure directly impacts bookings, payments, or provider revenue
P1 - Core experience: Failure significantly degrades user experience
P2 - Important: Failure causes friction but workarounds exist
```

---

## Sheet 2: "Dashboard" (Summary View)

### Row 1-2: Header
```
| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| CRITICAL FLOWS DASHBOARD | | | | | Last Updated: | =TODAY() |
| | | | | | | |
```

### Row 4-5: Overall Metrics Header
```
| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| OVERALL COVERAGE | | | | | | |
| Total Flows | P0 Flows | P1 Flows | P2 Flows | Automated | Partial | No Coverage |
```

### Row 6: Overall Metrics Formulas
```
| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| =COUNTA(Flows!A:A)-1 | =COUNTIF(Flows!C:C,"P0") | =COUNTIF(Flows!C:C,"P1") | =COUNTIF(Flows!C:C,"P2") | =COUNTIF(Flows!I:I,"✅ Automated") | =COUNTIF(Flows!I:I,"🟡 Partial") | =COUNTIF(Flows!I:I,"🚫 None")+COUNTIF(Flows!I:I,"❌ Manual Only") |
```

### Row 8-9: Coverage Percentage Header
```
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| COVERAGE PERCENTAGES | | | | | |
| Overall Automation % | P0 Automation % | P1 Automation % | CI Coverage % | Stale Tests (>30 days) | |
```

### Row 10: Coverage Percentage Formulas
```
| A | B | C | D | E |
|---|---|---|---|---|
| =COUNTIF(Flows!I:I,"✅ Automated")/(COUNTA(Flows!A:A)-1) | =COUNTIFS(Flows!C:C,"P0",Flows!I:I,"✅ Automated")/COUNTIF(Flows!C:C,"P0") | =COUNTIFS(Flows!C:C,"P1",Flows!I:I,"✅ Automated")/COUNTIF(Flows!C:C,"P1") | =COUNTIF(Flows!K:K,"Yes")/(COUNTA(Flows!A:A)-1) | =COUNTIF(Flows!L:L,"<"&TODAY()-30) |
```

Format cells A10:D10 as Percentage.

### Row 12-13: By Team Header
```
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| COVERAGE BY TEAM | | | | | |
| Team | Total Flows | Automated | Partial | None | Automation % |
```

### Row 14+: Team Breakdown (add rows per team)
```
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Booking | =COUNTIF(Flows!D:D,"Booking") | =COUNTIFS(Flows!D:D,"Booking",Flows!I:I,"✅ Automated") | =COUNTIFS(Flows!D:D,"Booking",Flows!I:I,"🟡 Partial") | =COUNTIFS(Flows!D:D,"Booking",Flows!I:I,"🚫 None")+COUNTIFS(Flows!D:D,"Booking",Flows!I:I,"❌ Manual Only") | =C14/B14 |
| Search Relevance | ... | ... | ... | ... | ... |
| Patient Acquisition | ... | ... | ... | ... | ... |
| Patient Retention | ... | ... | ... | ... | ... |
| Provider Onboarding | ... | ... | ... | ... | ... |
| Provider Success | ... | ... | ... | ... | ... |
| Provider Preferences | ... | ... | ... | ... | ... |
| Provider Billing | ... | ... | ... | ... | ... |
| Provider Roster | ... | ... | ... | ... | ... |
| Branded Directory | ... | ... | ... | ... | ... |
| Appointment Management | ... | ... | ... | ... | ... |
| User Permissions | ... | ... | ... | ... | ... |
```

---

## Sheet 3: "Flows" (Main Data Entry)

### Headers (Row 1)
```
| A | B | C | D | E | F | G | H | I | J | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Flow ID | Flow Name | Priority | Team | Description | Entry Point | Happy Path Steps | Edge Cases | Automation Status | Test Location | CI Included | Last Validated | Owner | Notes |
```

### Data Validation Rules

**Column C (Priority):** Dropdown with values:
- P0
- P1
- P2

**Column D (Team):** Dropdown with values:
- Booking
- Search Relevance
- Patient Acquisition
- Patient Retention
- Provider Onboarding
- Provider Success
- Provider Preferences
- Provider Billing
- Provider Roster
- Branded Directory
- Appointment Management
- User Permissions
- Zo
- Mobile
- Interop
- Provider Infrastructure

**Column I (Automation Status):** Dropdown with values:
- ✅ Automated
- 🟡 Partial
- ❌ Manual Only
- 🚫 None

**Column K (CI Included):** Dropdown with values:
- Yes
- No

**Column L (Last Validated):** Date format

### Conditional Formatting Rules

1. **Priority P0 rows:** Light red background (#F4CCCC)
2. **Priority P1 rows:** Light yellow background (#FFF2CC)
3. **Automation Status "🚫 None":** Red text
4. **Automation Status "✅ Automated":** Green text
5. **Last Validated > 30 days ago:** Orange background on that cell

---

## Sheet 4: "Gaps" (Auto-filtered view)

This sheet shows only flows that need attention.

### Filter Criteria
Show rows where:
- Automation Status = "🚫 None" OR "❌ Manual Only"
- OR Priority = "P0" AND Automation Status ≠ "✅ Automated"

### Formula to create filtered list
Use FILTER function:
```
=FILTER(Flows!A:N, (Flows!I:I="🚫 None")+(Flows!I:I="❌ Manual Only")+((Flows!C:C="P0")*(Flows!I:I<>"✅ Automated")))
```

---

## Sheet 5: "Changelog"

Track updates to the critical flows list.

| Date | Editor | Change Description |
|------|--------|-------------------|
| 2026-05-06 | Allen | Initial template created |

---

## Quick Start Checklist

- [ ] Create Google Sheet with 5 sheets: Instructions, Dashboard, Flows, Gaps, Changelog
- [ ] Set up data validation dropdowns on Flows sheet
- [ ] Add conditional formatting rules
- [ ] Add dashboard formulas
- [ ] Share with all QAEs
- [ ] Each QAE adds their team's critical flows
- [ ] Review and validate entries
- [ ] Set up weekly review cadence

---

## Example Flows Data (Starter Rows)

```csv
Flow ID,Flow Name,Priority,Team,Description,Entry Point,Happy Path Steps,Edge Cases,Automation Status,Test Location,CI Included,Last Validated,Owner,Notes
BOOK-001,New Patient Booking,P0,Booking,New user completes first booking,/search,"1. Search specialty 2. Select provider 3. Pick slot 4. Create account 5. Confirm",Insurance mismatch; No slots,✅ Automated,BU/Marketplace/Booking/Flows/booking-flow.spec.js,Yes,2026-05-01,Ayushi,
BOOK-002,Returning Patient Booking,P0,Booking,Existing patient books appointment,/search,"1. Login 2. Search 3. Select 4. Confirm",Saved insurance expired,🟡 Partial,BU/Marketplace/Booking/Flows/returning-patient.spec.js,Yes,2026-04-20,Ayushi,Login step needs work
SEARCH-001,Basic Search,P0,Search Relevance,Patient searches for provider,/,"1. Enter location 2. Select specialty 3. View results",No results; Invalid location,✅ Automated,BU/Marketplace/Search-Relevance/Flows/basic-search.spec.js,Yes,2026-05-03,Jyoti,
SEARCH-002,Filtered Search,P1,Search Relevance,Patient applies filters to search,/search,"1. Search 2. Apply insurance filter 3. Apply availability filter",Filter combo yields no results,🟡 Partial,BU/Marketplace/Search-Relevance/Pages/search-filters.spec.js,Yes,2026-04-28,Jyoti,Gender filter not covered
```
