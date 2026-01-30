# AMP Escalation Handler - Claude Code Reference

## Purpose
Quick reference for AI assistants determining when to escalate to humans.

---

## Escalation Decision Tree

```
Does message contain safety/legal keywords?
├── Yes → ESCALATE IMMEDIATELY
└── No → Does message show negative sentiment?
          ├── Yes (anger, caps, threats) → ESCALATE
          └── No → Is request within AI scope?
                    ├── No (refunds, custom, complex) → ESCALATE
                    └── Yes → Handle normally
```

---

## Keyword Triggers

### IMMEDIATE ESCALATION
| Category | Keywords |
|----------|----------|
| Safety | "injured," "accident," "hurt," "dangerous," "unsafe" |
| Legal | "lawyer," "attorney," "legal," "sue," "lawsuit" |
| Financial | "refund," "money back," "overcharged" |
| Complaint | "manager," "supervisor," "complaint," "unacceptable" |
| Media | "media," "news," "reporter," "press" |

### SENTIMENT TRIGGERS
- Multiple exclamation marks (!!!)
- ALL CAPS sentences
- Words: "outrageous," "worst," "never again," "warn others"

---

## Routing Table

| Situation | Contact |
|-----------|---------|
| Membership issues | shawn@atlantamotorsportspark.com |
| Karting program | eli@ampkartracing.com |
| Group events | jessica@atlantamotorsportspark.com |
| HR / Employment / Legal | hr@atlantamotorsportspark.com |
| General/Unknown | info@atlantamotorsportspark.com |
| Safety concerns | Management (escalate with urgency) |

**Note:** Always route HR-related inquiries (employment, complaints, legal) to hr@ - NOT info@.

---

## Escalation Categories

### Always Escalate
- Safety/injury reports
- Legal/liability mentions
- Refund requests
- Angry/frustrated customers
- Media inquiries
- VIP situations

### Conditional Escalate
- Corporate events
- Large groups (20+)
- Custom requests
- Technical questions outside scope
- Previous complaint references

### Don't Escalate (Handle Normally)
- Basic pricing questions
- General event inquiries
- Booking help
- Standard information requests

---

## Response Framework

1. **Acknowledge** - Validate their concern
2. **Explain** - Why you're escalating
3. **Connect** - Provide contact info
4. **Set expectations** - When they'll hear back
5. **Summarize** - Note conversation for human

---

## Sample Handoff Email Format

```
TO: [appropriate contact]
SUBJECT: [Priority Level] - [Brief Description]

CUSTOMER: [Name/Contact if available]
INQUIRY TYPE: [Category]
SUMMARY: [2-3 sentences]
URGENCY: [High/Medium/Low]

CONVERSATION CONTEXT:
[Key points from conversation]

ACTION NEEDED:
[What human needs to do]
```
