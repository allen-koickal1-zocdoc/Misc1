# QAEngineeringSpace

This repo contains QA tools, dashboards, and documentation.

## Critical Flows Dashboard

Location: `critical-flows-dashboard/`

When creating or updating test coverage data files, use this format:

```javascript
const TEAMNAME_FLOWS = {
    team: "Team Name",
    owner: "Default Owner",  // optional
    priority: "P0",          // default: P0, P1, or P2
    tests: [
        { test: "Test description", status: "Covered", file: "spec-file.js" },
        { test: "Another test", status: "Partial", file: "other.spec.js", notes: "explain gap" },
        { test: "Missing test", status: "Missing", owner: "Specific Owner", priority: "P1" },
    ]
};
```

**Required fields per test:**
- `test` - description of the critical flow
- `status` - one of: `Covered`, `Partial`, `Missing`

**Optional fields per test:**
- `owner` - overrides team default
- `priority` - overrides team default (P0/P1/P2)
- `file` - spec file that covers it
- `notes` - explains why partial or other context

**After creating a new data file:**
1. Add `<script src="data/teamname.js"></script>` to index.html
2. Register: `if (typeof TEAMNAME_FLOWS !== 'undefined') ALL_DATA.push(TEAMNAME_FLOWS);`

**Variable naming:** Use `UPPERCASE_FLOWS` format (e.g., `BOOKING_FLOWS`, `AUTH_FLOWS`).
