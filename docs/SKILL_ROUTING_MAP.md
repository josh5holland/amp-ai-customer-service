# Skill Routing Map

## Purpose
Decision tree for routing customer inquiries to the appropriate skill.

---

## Primary Routing Decision Tree

```
INCOMING INQUIRY
│
├── Contains escalation triggers (anger, safety, legal, refund)?
│   └── YES → amp-escalation-handler
│
├── About track rules, safety, or requirements?
│   └── YES → amp-rules-expert
│
├── New member asking "what do I do now?"
│   └── YES → amp-onboarding-coordinator
│
├── Looking for events or calendar?
│   └── YES → amp-event-finder
│
├── Wants to compare membership options?
│   └── YES → amp-membership-explorer
│
├── Interested in cars/motorcycles on track?
│   └── YES → amp-main-track-advisor
│
├── Interested in karting?
│   │
│   ├── Wants to rent karts / casual fun?
│   │   └── YES → amp-concession-karting-advisor
│   │
│   └── Wants to own kart / compete?
│       └── YES → amp-karting-advisor
│
└── Unclear intent?
    └── amp-lead-qualifier (classify first)
```

---

## Skill Summary Table

| Skill | Purpose | Key Triggers |
|-------|---------|--------------|
| amp-lead-qualifier | Classify incoming emails | Initial classification, unclear intent |
| amp-main-track-advisor | Road course membership | "car," "motorcycle," "track day," "$25K" |
| amp-karting-advisor | Race karting membership | "own kart," "buy kart," "compete," "racing" |
| amp-concession-karting-advisor | Rental karting | "rent," "session," "no membership," "arrive-and-drive" |
| amp-membership-explorer | Compare options | "what membership," "compare," "options," "which one" |
| amp-event-finder | Find events/calendar | "events," "calendar," "schedule," "when" |
| amp-rules-expert | Rules and safety | "rules," "helmet," "requirements," "tech" |
| amp-onboarding-coordinator | New member help | "just joined," "first time," "what now," "new member" |
| amp-escalation-handler | Human handoff | "refund," "manager," "lawyer," angry sentiment |

---

## Keyword-Based Routing

### Route to amp-main-track-advisor
- "car," "motorcycle," "road course"
- "track day," "track membership"
- "$25,000," "$50,000," "Platinum," "Diamond"
- "2-mile track," "16 turns"

### Route to amp-karting-advisor
- "race kart," "own kart," "buy kart"
- "karting membership," "compete," "racing"
- "Kid Kart," "Cadet," "LO206"
- "Karting School," "eli@"
- Kids ages 5-11 wanting serious karting

### Route to amp-concession-karting-advisor
- "rent," "rental," "arrive-and-drive"
- "session," "no membership"
- "Clubspeed," "book karting"
- "team event," "enduro," "league"
- "Junior Discovery" (ages 5-11)

### Route to amp-membership-explorer
- "what membership," "which membership"
- "compare," "options," "difference between"
- "confused about," "not sure which"

### Route to amp-event-finder
- "events," "calendar," "schedule"
- "when," "dates," "upcoming"
- "what's happening," "activities"

### Route to amp-rules-expert
- "rules," "requirements," "allowed"
- "helmet," "safety gear," "tech inspection"
- "noise limit," "flags," "passing"

### Route to amp-onboarding-coordinator
- "just joined," "new member"
- "first visit," "first time"
- "what do I do now," "next steps"

### Route to amp-escalation-handler
- "refund," "money back"
- "manager," "supervisor," "complaint"
- "lawyer," "legal," "sue"
- "injured," "accident," "unsafe"
- ALL CAPS, multiple exclamation marks
- "unacceptable," "outrageous," "worst"

---

## Age-Based Routing

| Age | Options | Primary Skill |
|-----|---------|---------------|
| Under 5 | No programs available | amp-escalation-handler (explain) |
| 5-11 | Junior Discovery, Race Karting | amp-karting-advisor or amp-concession-karting-advisor |
| 12+ | All karting options | Based on rent vs own |
| Licensed driver | All options | Based on vehicle type |

---

## Cross-Skill References

Each skill may route to others. Common patterns:

| From | To | When |
|------|-----|------|
| amp-lead-qualifier | Any skill | After classification |
| amp-membership-explorer | Specific advisors | After decision made |
| amp-concession-karting-advisor | amp-karting-advisor | "Want to get serious" |
| amp-karting-advisor | amp-concession-karting-advisor | "Just want to rent" |
| amp-main-track-advisor | amp-event-finder | Looking for public events |
| Any skill | amp-escalation-handler | Triggers detected |

---

## Intent Classification Categories

For amp-lead-qualifier, emails should be classified into:

1. **road_course_inquiry** → amp-main-track-advisor
2. **race_karting_inquiry** → amp-karting-advisor
3. **concession_karting_inquiry** → amp-concession-karting-advisor
4. **membership_comparison** → amp-membership-explorer
5. **event_inquiry** → amp-event-finder
6. **rules_question** → amp-rules-expert
7. **new_member_help** → amp-onboarding-coordinator
8. **escalation_required** → amp-escalation-handler
9. **general_inquiry** → amp-lead-qualifier (ask clarifying questions)

---

## Confidence Thresholds

When routing, consider:
- **High confidence (>80%):** Route directly
- **Medium confidence (50-80%):** Route with verification question
- **Low confidence (<50%):** Ask clarifying question before routing

Example medium confidence response:
> "It sounds like you're interested in [topic]. Is that right, or were you asking about something else?"
