# Calendar Access Rules

## Two Calendars

AMP maintains separate calendars for members and the public. Sharing the correct one is important.

---

## Member Calendar

### URL
theclub.atlantamotorsportspark.com/calendar/

### Contains
- All member track days
- Track Day Socials
- Competition events
- Club racing schedule
- Member-only activities

### Who Can Access
- Road course members
- Karting members
- Prospective members actively in sales process

### Who Should NOT Get This Link
- General public inquiries
- Non-members asking about events
- People unclear about membership

---

## Public Events Page

### URL
https://www.atlantamotorsportspark.com/events/

### Contains
- Driving schools
- Special experiences
- Events open to non-members
- Public track days (when scheduled)

### Who Should Get This Link
- Non-members
- People exploring options
- One-time visitors
- Anyone not confirmed as member

---

## Decision Logic

```
Is the person a confirmed AMP member?
├── Yes → Member calendar OK
├── No → Public events page only
└── Unsure → Public events page (safer option)
```

---

## Why This Matters

1. **Member experience:** Members pay for exclusive access; sharing their calendar devalues membership
2. **Expectations:** Non-members might show up expecting to participate in member events
3. **Security:** Member calendar may contain details not meant for public
4. **Sales:** Proper routing helps membership team track prospects

---

## Edge Cases

### "I'm thinking about membership"
- Share public events page
- Connect with shawn@atlantamotorsportspark.com for membership details
- Member calendar shared after sales process begins

### "I'm a member but forgot the link"
- OK to share member calendar
- May want to verify membership if uncertain

### "My friend is a member"
- Public events page for the friend
- They can bring you as a guest through proper channels
