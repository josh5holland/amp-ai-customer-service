# AMP Concession Karting Advisor - Claude Code Reference

## Purpose
Quick reference for AI assistants and developers working with the arrive-and-drive karting system at AMP. This covers rental kart sessions - NO membership required.

---

## Critical Distinction

```
CONCESSION KARTING (this skill)    RACE KARTING (different skill)
├── Rental Sodi karts              ├── Own personal race kart
├── NO membership needed           ├── Membership REQUIRED ($3,500+)
├── Age 12+ / 60" tall minimum     ├── Age 5+ minimum
├── 55+ mph                        ├── 40-70+ mph
└── Entertainment focus            └── Competitive focus
```

**Routing rules:**
- Owns/buying a kart → amp-karting-advisor
- Kids under 12 → Junior Discovery OR amp-karting-advisor
- "Get serious about karting" → amp-karting-advisor

---

## Requirements Quick Reference

| Requirement | Value |
|-------------|-------|
| Minimum age | 12 years |
| Minimum height | 60 inches (5 feet) |
| Minors under 18 | Waiver required, adult present |
| Footwear | Closed-toe required |
| What's provided | Kart, helmet, safety briefing |

---

## Session Types

| Type | Booking URL | Best For |
|------|-------------|----------|
| Public Sessions | bookings.clubspeed.com/amp | Individuals, drop-in |
| League Racing | motorsportreg.com/orgs/atlanta-motorsports-park/events | Regular competitors |
| Team Enduros | motorsportreg.com/orgs/atlanta-motorsports-park/events | Groups, corporate |
| Corporate Events | Contact AMP directly | Large groups, private |

---

## Under-12 Handling

```
Is the driver under 12?
├── Yes → Age 5-11?
│         ├── Yes → Junior Discovery Experience ($249)
│         └── No (under 5) → Not eligible for any program
└── No → Standard rental karts OK
```

### Junior Discovery Experience
- Ages: 5-11
- Duration: 2.5 hours
- Cost: $249
- Includes: Kart, helmet, racing suit, snacks, water
- Booking: motorsportreg.com or (678) 381-8526

---

## Booking URLs

| Purpose | URL |
|---------|-----|
| Public sessions | bookings.clubspeed.com/amp |
| Leagues/Enduros | motorsportreg.com/orgs/atlanta-motorsports-park/events |
| Junior Discovery | motorsportreg.com or (678) 381-8526 |
| Race karting (schools) | eli@ampkartracing.com |

---

## Common Questions Decision Tree

### "How much is karting?"
→ ~$35 for 10-minute session, packages available
→ Point to: bookings.clubspeed.com/amp

### "Can my [age] year old drive?"
```
Age >= 12 AND Height >= 60"?
├── Yes → Standard rental karts OK
├── Age 5-11 → Junior Discovery Experience
└── Under 5 → Not eligible
```

### "I want to get serious"
→ Route to amp-karting-advisor (race karting)
→ Suggest: Karting School ($549) as first step

### "Group booking"
```
Group size <= 10?
├── Yes → Book same time slot at bookings.clubspeed.com/amp
└── No →
    Group size 10-20?
    ├── Yes → Enduro event or contact AMP
    └── No (20+) → Escalate to human
```

---

## Equipment Provided

| Item | Notes |
|------|-------|
| Sodi rental kart | Bumpers, seatbelts, 55+ mph |
| Helmet | Available to borrow (free) |
| Safety briefing | Required before driving |

**Customer brings:** Closed-toe shoes, long pants recommended

---

## Escalation Triggers

- Groups 20+ people
- Corporate events with special requirements
- Questions about competitive racing → route to amp-karting-advisor
- Safety concerns or injuries
- Complaints

---

## Related Skills

| Skill | When to Route |
|-------|---------------|
| amp-karting-advisor | Owns kart, wants membership, competitive racing |
| amp-membership-explorer | Comparing all membership types |
| amp-event-finder | Looking for specific events |

---

## Key Contacts

| For | Contact |
|-----|---------|
| Session booking | bookings.clubspeed.com/amp |
| Leagues/Events | motorsportreg.com/orgs/atlanta-motorsports-park/events |
| Junior Discovery | motorsportreg.com or (678) 381-8526 |
| Race karting path | eli@ampkartracing.com |
