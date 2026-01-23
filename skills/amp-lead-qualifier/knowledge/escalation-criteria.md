# Escalation Criteria

## What This Document Does
Defines exactly when the Lead Qualifier should flag an email for human review instead of automated handling.

---

## Immediate Escalation Triggers

These keywords or topics should ALWAYS trigger escalation:

### Safety Keywords
- injury, injured, hurt
- accident, crash, collision
- unsafe, dangerous
- broken, malfunction
- emergency

### Legal Keywords
- lawyer, attorney, legal
- lawsuit, sue, court
- liability
- police, report

### Financial Keywords
- refund, money back
- overcharged, billing error
- dispute, chargeback
- fraud

### Complaint Indicators
- terrible, awful, worst
- unacceptable, outraged
- never again, warning others
- complaint, complain
- manager, supervisor, owner

### Media/PR
- reporter, journalist, press
- news, media inquiry
- interview, statement
- publication, article

### VIP/Special Handling
- NASCAR, professional driver (name drop)
- sponsor, partnership
- celebrity (if mentioned)
- large corporation (named)

---

## Sentiment-Based Escalation

Even without specific keywords, escalate if:

1. **Overall negative sentiment** - Customer sounds upset or frustrated
2. **Multiple exclamation points** - "This is ridiculous!!!"
3. **ALL CAPS sections** - "I CANNOT BELIEVE..."
4. **Threats** - Even vague ones ("you'll be hearing from me")

---

## Confidence-Based Escalation

Escalate when:

- Confidence score < 70%
- Multiple intents seem equally likely
- Email is ambiguous or confusing
- Foreign language (we can't reliably classify)

---

## Context-Based Escalation

Escalate if the email mentions:

- Previous negative experience
- Ongoing unresolved issue
- Communication with specific staff member
- Promises made by AMP that weren't kept

---

## Do NOT Escalate

These are normal and should be handled by skills:

- Simple pricing questions
- Availability inquiries
- General information requests
- Positive feedback (route to appropriate skill)
- Standard booking questions

---

## Escalation Response Format

When escalating, always include:

```json
{
  "escalate": true,
  "escalation_reason": "Specific reason from this document",
  "priority": "high"
}
```

Example reasons:
- "Refund request - requires human handling"
- "Safety concern mentioned - needs immediate review"
- "Media inquiry - PR team should respond"
- "Low confidence (65%) - unclear customer intent"
- "Complaint with negative sentiment - human judgment needed"
