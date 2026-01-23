# Claude Code Integration Guide

## What This Document Is For
This guide helps when building skills that serve **multiple AI contexts** - not just customer service automation, but also Claude Code instances working on AMP's mobile app, CRM, and other codebases.

---

## The Dual-Purpose Skill Model

Each skill in this repo can serve two audiences:

| Audience | Use Case | Format Needs |
|----------|----------|--------------|
| **Customer Service AI** | Answer customer emails | Conversational, includes tone guidance, example responses |
| **Claude Code (Developer AI)** | Build features in AMP apps | Technical, includes data structures, access logic, code patterns |

When building a skill, consider both audiences.

---

## What Claude Code Instances Need Most

Based on feedback from Claude Code sessions working on `amp-member-app`, here's what's most valuable:

### 1. Decision Logic as Pseudocode
Don't just describe rules - show the logic:

```
# BAD (vague)
"Diamond members have more access than Platinum"

# GOOD (actionable)
Can member access event?
├── Check category match (track/karting/both)
├── If karting event → member.category in ['karting', 'both']
├── If track event → member.category in ['track', 'both']
│                    AND tierRank[member.tier] >= tierRank[event.min_tier]
```

### 2. Explicit Hierarchies with Rankings
Provide numeric values that can be used in code:

```json
{
  "tierHierarchy": {
    "diamond": 3,
    "platinum": 2,
    "tungsten": 1
  },
  "comparison": "higher number = more access"
}
```

### 3. Edge Cases & Exceptions
What breaks the normal rules?
- Events with `min_tier: null` - open to all members of that category
- Staff accounts - can override tier/category for testing
- Karting has NO tier hierarchy (all karting members equal)

### 4. Test Account Reference
What mock data exists for development?

| Email | Tier | Category | Role | Purpose |
|-------|------|----------|------|---------|
| member@test.com | diamond | both | member | Full access testing |
| staff@test.com | diamond | both | staff | Override testing |

### 5. UI Mapping
How do data values map to display?

```json
{
  "diamond": { "color": "#f97316", "icon": "gem", "label": "Diamond" },
  "platinum": { "color": "#a855f7", "icon": "crown", "label": "Platinum" },
  "tungsten": { "color": "#6b7280", "icon": "medal", "label": "Tungsten" }
}
```

### 6. Business Context (The "Why")
Technical logic is easier to implement correctly when the reasoning is clear:
- "Karting is separate because it's a different revenue stream with different equipment"
- "Diamond gets exclusive events because they pay 3x the Tungsten rate"

---

## Recommended Skill Structure for Dual-Purpose Use

```
amp-[skill-name]/
├── SKILL.md                    # Customer service AI instructions
├── CLAUDE_CODE.md              # Developer-focused quick reference (NEW)
├── knowledge/
│   ├── [topic]-rules.md        # Business logic & decision trees
│   ├── [topic]-data.json       # Structured data with types
│   ├── [topic]-faq.md          # Common questions (both audiences)
│   └── [topic]-ui-mapping.json # Colors, icons, labels
└── scripts/
    └── [helpers].py            # Calculators, validators
```

### The CLAUDE_CODE.md File

This is a **quick reference** optimized for developer AI. Include:

1. **Data Types** - TypeScript interfaces or similar
2. **Access Logic** - Pseudocode decision trees
3. **Constants** - Tier rankings, category options
4. **Test Data** - Mock accounts and their configurations
5. **Common Patterns** - "When filtering events, always check category first"

Keep it scannable - use tables, code blocks, and bullet points over prose.

---

## Example: Membership Explorer Skill

Here's what the `amp-membership-explorer` skill should contain for Claude Code:

### CLAUDE_CODE.md (excerpt)
```markdown
# Membership System - Developer Reference

## Types
- `MembershipTier`: 'diamond' | 'platinum' | 'tungsten'
- `MembershipCategory`: 'track' | 'karting' | 'both'

## Tier Ranking (use for comparisons)
| Tier | Rank | Access Level |
|------|------|--------------|
| diamond | 3 | All track events |
| platinum | 2 | Most track events |
| tungsten | 1 | Entry-level track |

## Event Access Check
```typescript
function canAccessEvent(member, event): boolean {
  // Category check first
  if (event.category === 'karting') {
    return member.category === 'karting' || member.category === 'both';
  }
  // Track event - check category AND tier
  const hasCategory = member.category === 'track' || member.category === 'both';
  const hasTier = event.min_tier === null ||
                  tierRank[member.tier] >= tierRank[event.min_tier];
  return hasCategory && hasTier;
}
```

## Staff Override System
Staff can set `tierOverride` and `categoryOverride` in AuthContext.
Use `effectiveTier` and `effectiveCategory` (not raw profile values) for access checks.
```

---

## How to Add Claude Code Support to Existing Skills

1. **Create CLAUDE_CODE.md** in the skill folder
2. **Extract technical details** from SKILL.md into developer-friendly format
3. **Add type definitions** if the skill relates to database entities
4. **Include test data** references
5. **Document edge cases** that might trip up code generation

---

## Questions?

When building skills, ask: "If a Claude Code instance needed to implement a feature using this knowledge, would they have enough to do it correctly on the first try?"

If not, add more specificity.
