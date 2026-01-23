# Membership System - Claude Code Quick Reference

> **Purpose**: Fast lookup for Claude Code instances building membership-related features in AMP apps.
> See SKILL.md for customer service AI instructions.

---

## Data Types

```typescript
type MembershipTier = 'diamond' | 'platinum' | 'tungsten';
type MembershipCategory = 'track' | 'karting' | 'both';
type MembershipStatus = 'active' | 'suspended' | 'expired';
```

---

## Tier Hierarchy

| Tier | Rank | Monthly Cost | Track Access |
|------|------|--------------|--------------|
| diamond | 3 | $$$$ | All events including exclusive |
| platinum | 2 | $$$ | Most events |
| tungsten | 1 | $$ | Entry-level events |

**Comparison Logic**: `tierRank[member.tier] >= tierRank[event.min_tier]`

---

## Category Access Matrix

| Member Category | Track Events | Karting Events |
|-----------------|--------------|----------------|
| track | Yes (tier-gated) | No |
| karting | No | Yes (all) |
| both | Yes (tier-gated) | Yes (all) |

**Key Insight**: Karting has NO tier hierarchy. All karting members have equal access to karting events.

---

## Event Access Decision Tree

```
canMemberAccessEvent(member, event):
│
├── Is event.event_category === 'karting'?
│   ├── Yes → return member.category IN ['karting', 'both']
│   └── No (track event) ↓
│
├── Does member have track access?
│   └── member.category IN ['track', 'both']?
│       ├── No → return false
│       └── Yes ↓
│
└── Does member meet tier requirement?
    └── event.min_tier === null?
        ├── Yes → return true (open to all track members)
        └── No → return tierRank[member.tier] >= tierRank[event.min_tier]
```

---

## Staff Override System

Staff members can test as any membership combination:

```typescript
// In AuthContext
tierOverride: MembershipTier | null;      // Set via Staff Profile
categoryOverride: MembershipCategory | null;

// Always use these for access checks:
effectiveTier    // Returns tierOverride ?? profile.membership_tier
effectiveCategory // Returns categoryOverride ?? profile.membership_category
```

**Security**: Overrides only work when `isStaff === true`. Cleared on logout.

---

## UI Display Mapping

```json
{
  "diamond": {
    "color": "#f97316",
    "icon": "gem",
    "label": "Diamond"
  },
  "platinum": {
    "color": "#a855f7",
    "icon": "crown",
    "label": "Platinum"
  },
  "tungsten": {
    "color": "#6b7280",
    "icon": "medal",
    "label": "Tungsten"
  }
}
```

Location in codebase: `constants/Colors.ts` → `membershipTiers`

---

## Test Accounts (Mock Mode)

| Email | Password | Tier | Category | Staff | Use For |
|-------|----------|------|----------|-------|---------|
| member@test.com | password | diamond | both | No | Full member access |
| staff@test.com | password | diamond | both | Yes | Testing overrides |

---

## Common Patterns

### Filtering Events by Access
```typescript
const visibleEvents = events.filter(event =>
  canAccessEvent(effectiveTier, effectiveCategory, event)
);
```

### Displaying Tier Badge
```typescript
const tierConfig = membershipTiers[profile.membership_tier];
<Badge color={tierConfig.color} icon={tierConfig.icon}>
  {tierConfig.label}
</Badge>
```

---

## Files to Know

| File | Contains |
|------|----------|
| `types/database.ts` | MembershipTier, MembershipCategory types |
| `types/membership.ts` | canAccessEvent(), tierRank constant |
| `lib/auth.tsx` | effectiveTier, effectiveCategory, override logic |
| `constants/Colors.ts` | membershipTiers UI config |
| `lib/mockData.ts` | Test events with various tier/category combos |

---

## TODO: Information Still Needed

- [ ] Actual pricing for each tier
- [ ] Full list of Diamond-exclusive benefits
- [ ] Upgrade/downgrade rules
- [ ] Renewal process details
- [ ] Family membership add-on rules
