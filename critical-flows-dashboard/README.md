# Critical Flows Dashboard

A lightweight dashboard for tracking E2E test coverage across critical user flows.

## Quick Start

1. Open `index.html` in a browser (or via GitHub Pages)
2. Dashboard reads data from `data/*.js` files

## Adding a New Team

Create `data/teamname.js`:

```javascript
const TEAMNAME_FLOWS = {
    team: "Team Name",
    owner: "Default Owner",  // default owner for tests without explicit owner
    priority: "P0",  // default priority for tests
    tests: [
        { test: "Test description", status: "Covered", owner: "John Doe", file: "spec-file.js", notes: "optional" },
        { test: "Another test", status: "Partial", owner: "Jane Smith", file: "other.spec.js", notes: "partial reason" },
        { test: "Missing test", status: "Missing" },  // inherits team owner
        { test: "P1 test override", status: "Missing", priority: "P1", owner: "Bob Wilson" },
    ]
};
```

Then add to `index.html`:
```html
<script src="data/teamname.js"></script>
```

And register in the JS section:
```javascript
if (typeof TEAMNAME_FLOWS !== 'undefined') ALL_DATA.push(TEAMNAME_FLOWS);
```

## Status Values

| Status | Meaning | Coverage Credit |
|--------|---------|-----------------|
| `Covered` | Full E2E test exists | 100% |
| `Partial` | Test exists but incomplete | 50% |
| `Missing` | No test coverage | 0% |

## Priority Values

- `P0` - Critical flows (red badge)
- `P1` - Important flows (orange badge)  
- `P2` - Nice to have (blue badge)

## Coverage Score Formula

```text
Score = (Covered × 100 + Partial × 50) / Total Tests
```

## Files

- `index.html` - Main dashboard
- `data/*.js` - Team data files

## GitHub Pages

To host internally:
1. Go to repo Settings → Pages
2. Set source to branch `main`, folder `/ (root)` or `/critical-flows-dashboard`
3. Access at `https://zocdoc.github.io/QAEngineeringSpace/critical-flows-dashboard/`
