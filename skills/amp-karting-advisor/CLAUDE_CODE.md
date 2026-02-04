# AMP Karting Advisor - Claude Code Reference

## Purpose
Quick reference for AI assistants and developers working with the race karting membership system at AMP. This covers membership-based karting where participants OWN their own race karts.

---

## Critical Distinction

```
RACE KARTING (this skill)          CONCESSION KARTING (different skill)
├── Own personal race kart         ├── Rent Sodi karts
├── Membership REQUIRED            ├── NO membership needed
├── $3,500+ initiation             ├── Pay per session
├── Age 5+ minimum                 ├── Age 12+ / 60" tall minimum
├── 40-70+ mph                     ├── 55+ mph
└── Competitive focus              └── Entertainment focus
```

**Routing rule:** If customer mentions "rent," "rental," or "arrive-and-drive" → Route to amp-concession-karting-advisor

---

## Membership Tiers

| Tier | Initiation | Monthly | Daily | Best For |
|------|------------|---------|-------|----------|
| Standard | $3,500 | $95 | $20 | Testing commitment |
| Standard Add-on | $2,000 | $55 | $20 | 2nd family member |
| Lifetime | $10,000 | $0 | $0 | Long-term (5+ years) |
| Lifetime Add-on | $5,500 | $0 | $0 | 2nd family member |

**Upgrade rule:** Standard → Lifetime within first year, $3,500 credited

---

## Age/Class Matrix

| Age | Class | Recommended Engine |
|-----|-------|-------------------|
| 5-7 | Kid Kart | LO206 Kid Kart, Comer |
| 7-12 | Cadet | LO206 Cadet, TaG Rookie |
| 12-15 | Junior | LO206 Junior, TaG Junior |
| 15+ | Senior | LO206 Senior, TaG Senior, Shifter |

**Engine recommendation logic:**
- Beginner (any age) → LO206 (four-stroke, lower maintenance, pump gas)
- Experienced → TaG (two-stroke, more power, race fuel)
- Advanced → Shifter (gearbox, highest power)

---

## Equipment Cost Reference

```
BEGINNER SETUP (LO206)
├── Chassis (new): ~$3,000
├── Engine (LO206): ~$850
├── Safety gear: ~$1,200
├── Wheels/tires: ~$500
└── TOTAL: ~$5,550
```

**Storage options:**
- Rental garages: $400/month (waitlist)
- AMP Kartwerks: $85/month + $20/day racking

---

## Decision Trees

### Recommend Membership Type
```
Is this their first motorsports experience?
├── Yes → Standard (test commitment first)
└── No → Do they plan to kart 5+ years?
          ├── Yes → Lifetime
          ├── No → Standard
          └── Unsure → Standard (can upgrade within 1 year)
```

### Starting Path Recommendation
```
Is the driver age 5-11?
├── Yes → Junior Discovery Experience ($249) first
└── No → Karting School ($549) first

After first experience:
├── Enjoyed it → Private Lesson → Equipment Purchase → Membership
└── Unsure → More time before committing
```

### Budget Reality Check
```
Total budget under $5,000?
├── Yes → Recommend schools only (not ready for membership + equipment)
└── No → Budget $8,000-$10,000?
          ├── Yes → Standard membership + used equipment
          └── No → Can afford new equipment + membership tier of choice
```

---

## Key Contacts

| For | Contact |
|-----|---------|
| Membership | shawn@atlantamotorsportspark.com |
| Schools/Lessons | eli@ampkartracing.com |
| Junior Discovery | motorsportreg.com or (678) 381-8526 |
| Member calendar | theclub.atlantamotorsportspark.com/calendar/ |

---

## Timeline Expectations

| Milestone | Typical Timeframe |
|-----------|-------------------|
| School → First lesson | 1-2 weeks |
| Equipment acquisition | 2-4 weeks |
| Practice period | 4-8 weeks |
| **First race** | **3-6 months** |

**Red flag:** Customer expects to race "next week" or "this month" → Set realistic expectations

---

## Common Edge Cases

### "My kid is 4, can they start?"
- Not eligible yet (minimum age 5)
- Suggest waiting and returning when eligible

### "I want to rent karts with a membership"
- Confusion with concession karting
- Race karting = own your kart
- Concession karting = rent karts (no membership needed)
- Route to amp-concession-karting-advisor

### "Can I race right after joining?"
- Technically yes, but not recommended
- Suggest 5-10 practice days minimum
- First race should focus on finishing, not winning

### "What's the cheapest way to start?"
- Karting School ($549) - no commitment
- If hooked: Standard membership + used equipment (~$8K total)
- Upgrade path available within first year

---

## Related Skills

| Skill | When to Route |
|-------|---------------|
| amp-concession-karting-advisor | Wants to rent karts, no ownership |
| amp-membership-explorer | Comparing karting vs road course |
| amp-main-track-advisor | Interested in cars/motorcycles instead |
| amp-event-finder | Looking for karting events/leagues |

---

## Competition Info

### Club Racing
- Regular wheel-to-wheel events
- Multiple classes available
- Points accumulated through season

### 2026 Championship
- 5 rounds
- Entry via club racing events
