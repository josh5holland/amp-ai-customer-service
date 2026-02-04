# AMP Main Track Advisor - Claude Code Reference

## Purpose
Quick reference for AI assistants and developers working with the road course membership system at AMP. This covers the 2-mile, 16-turn circuit for cars and motorcycles.

---

## Membership Model Overview

**Key concept:** AMP road course is membership-based. Regular track days require membership. This is NOT a "pay per session" facility.

```
ROAD COURSE (this skill)           KARTING (different skills)
├── Cars & motorcycles             ├── Race karts OR rental karts
├── Membership REQUIRED            ├── Membership for race karting
├── $25,000+ initiation            ├── $3,500+ (race) / per-session (rental)
├── Licensed drivers               ├── Age 5+ (race) / 12+ (rental)
└── 2-mile circuit                 └── Separate kart track
```

---

## Membership Tiers

| Tier | Initiation | Monthly | Weekend Days | Total Days | Best For |
|------|------------|---------|--------------|------------|----------|
| Platinum Individual | $25,000 | $299 | 24/year | 102/year | 1-2 weekends/month |
| Diamond Individual | $50,000 | $299 | 48/year | 153/year | 3-4+ weekends/month |
| Diamond + Family | $60,000 | $399 | 48/year | 153/year | Family drivers |
| Corporate Diamond | $100,000 | $899 | 48/year | 153/year | Business use |

---

## Tier Selection Decision Tree

```
Is this for business/client entertainment?
├── Yes → Corporate Diamond ($100,000)
└── No → Multiple family members driving?
          ├── Yes → Diamond + Family ($60,000)
          └── No → How many weekends/month?
                    ├── 1-2 → Platinum ($25,000)
                    └── 3-4+ → Diamond ($50,000)
```

---

## What's Included (All Tiers)

- Member track days: Thursday, Friday, alternating weekends
- Monthly classroom instruction (no extra cost)
- 5+ Track Day Socials per year
- Holiday party and member events
- Guest privileges

---

## Non-Member Handling

### Can non-members use the road course?
**Regular track days: NO** - membership required

### Options for non-members:
1. Public events (driving schools, special experiences)
2. Come as a member's guest
3. Explore membership when ready

### URL Routing Logic
```
Is the person a member or serious prospect?
├── Yes → theclub.atlantamotorsportspark.com/calendar/
└── No → https://www.atlantamotorsportspark.com/events/
```

**NEVER share member calendar with non-members**

---

## Competition Options

| Type | Description | Vehicle Requirement |
|------|-------------|---------------------|
| Autocross | Cone course | Street-legal cars |
| Time Attack | Timed laps | Track-prepped cars |
| Club Racing | Wheel-to-wheel | Caged race cars |

### 2026 Championship
- 5 rounds

**Important:** Competition is OPTIONAL. Most members drive for fun, not competition. Don't oversell the racing aspect.

---

## Common Confusions

### "I want to do a track day"
- Determine if they mean one-time or regular
- One-time → Public events or member guest
- Regular → Membership required

### "How much for a track day?"
- AMP doesn't sell individual track days to non-members
- Membership model = initiation + monthly dues
- Point to public events for one-time experiences

### "I want karting membership to drive my car"
- Confusion between road course and kart track
- Road course = cars/motorcycles
- Kart track = go-karts
- Route to correct skill

### "What's included vs what costs extra?"
- Track days: Included in membership
- Competition events: May have entry fees
- Instruction: Monthly classroom included free
- Private coaching: Extra cost

---

## Key Contacts

| For | Contact |
|-----|---------|
| Membership | shawn@atlantamotorsportspark.com |
| Public events | https://www.atlantamotorsportspark.com/events/ |
| Member calendar | theclub.atlantamotorsportspark.com/calendar/ |

---

## Qualifying Questions Reference

1. **Vehicle type?** → Validates this is the right skill
2. **Prior track experience?** → Sets expectation level
3. **Expected frequency?** → Tier recommendation
4. **Business use?** → Corporate tier consideration

---

## Related Skills

| Skill | When to Route |
|-------|---------------|
| amp-karting-advisor | Interested in race karts (membership) |
| amp-concession-karting-advisor | Interested in rental karts |
| amp-membership-explorer | Comparing all membership types |
| amp-event-finder | Looking for public events |
| amp-competition-guide | Detailed racing series questions |

---

## Location Reference

**Atlanta Motorsports Park**
20 Duck Thurmond Road
Dawsonville, GA 30534
(About 1 hour north of Atlanta)
