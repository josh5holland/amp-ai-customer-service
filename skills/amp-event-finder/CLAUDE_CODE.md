# AMP Event Finder - Claude Code Reference

## Purpose
Quick reference for AI assistants helping customers find events and activities at AMP.

---

## Calendar URL Routing

| User Type | Calendar URL |
|-----------|--------------|
| Members | theclub.atlantamotorsportspark.com/calendar/ |
| Non-members | https://www.atlantamotorsportspark.com/events/ |

**CRITICAL:** Never share member calendar with non-members.

---

## Booking Systems

| Activity | Booking System | URL |
|----------|----------------|-----|
| Public events | AMP website | https://www.atlantamotorsportspark.com/events/ |
| Member events | Member calendar | theclub.atlantamotorsportspark.com/calendar/ |
| Rental karting | Clubspeed | bookings.clubspeed.com/amp |
| Karting leagues | MotorsportReg | motorsportreg.com/orgs/atlanta-motorsports-park/events |
| Junior Discovery | MotorsportReg | motorsportreg.com or (678) 381-8526 |

---

## Event Type Matrix

### Road Course Events

| Event | Description | Members Only |
|-------|-------------|--------------|
| Track Days | Regular practice | Yes |
| Track Day Socials | Driving + community | Yes |
| Club Racing | Wheel-to-wheel | Yes |
| Time Attack | Timed laps | Yes |
| Autocross | Cone course | Yes |
| Public Events | Schools, experiences | No |

### Karting Events

| Event | Description | Requires |
|-------|-------------|----------|
| Member Practice | Race kart practice | Karting membership |
| Club Racing | Competitive racing | Karting membership |
| Public Sessions | Rental sessions | None (age 12+) |
| Leagues | Multi-week series | None (age 12+) |
| Enduros | Team races | None (age 12+) |
| Junior Discovery | Kids intro | None (ages 5-11) |

---

## Decision Tree

```
Is user a member?
├── Yes → Member calendar + all event types
│          URL: theclub.atlantamotorsportspark.com/calendar/
└── No → What activity?
         ├── Cars/motorcycles → Public events only
         │                      URL: atlantamotorsportspark.com/events/
         └── Karting → What type?
                       ├── Rental sessions → bookings.clubspeed.com/amp
                       ├── Leagues/Enduros → motorsportreg.com/...
                       └── Kids 5-11 → Junior Discovery
```

---

## Quick Routing

| Customer Says | Route To |
|---------------|----------|
| "Event calendar" (member) | Member calendar |
| "Event calendar" (non-member) | Public events |
| "Track day" (member) | Member calendar |
| "Track day" (non-member) | Public events |
| "Karting session" | bookings.clubspeed.com/amp |
| "Karting league" | motorsportreg.com |
| "Kids activity" (5-11) | Junior Discovery |
| "Kids activity" (12+) | Rental karting |

---

## Escalation Triggers

- Private/corporate events
- Large group planning
- Hosting own event
- Scheduling conflicts
- Event complaints
