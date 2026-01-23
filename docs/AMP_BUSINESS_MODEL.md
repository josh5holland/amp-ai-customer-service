# AMP Business Model Overview

## Purpose
This document provides a consolidated overview of Atlanta Motorsports Park's business model for AI assistants and customer service systems.

---

## Facility Overview

**Atlanta Motorsports Park (AMP)**
20 Duck Thurmond Road
Dawsonville, GA 30534
(About 1 hour north of Atlanta)

AMP is a motorsports facility with multiple revenue streams serving different customer segments.

---

## Three Revenue Streams

### 1. Road Course (Cars & Motorcycles)
- **Track:** 2-mile, 16-turn road circuit
- **Model:** Membership required
- **Customer:** Automotive enthusiasts, track day hobbyists
- **Focus:** Community and hobby driving (not primarily competition)
- **Entry cost:** $25,000 - $100,000 initiation
- **Skill:** amp-main-track-advisor

### 2. Race Karting (Personal Karts)
- **Track:** Dedicated kart track
- **Model:** Membership required
- **Customer:** Competitive karters who own equipment
- **Focus:** Racing and competition
- **Entry cost:** $3,500 - $10,000 initiation + equipment (~$5,500)
- **Skill:** amp-karting-advisor

### 3. Concession Karting (Rental Karts)
- **Track:** Same kart track
- **Model:** No membership required
- **Customer:** Public, families, groups, entertainment
- **Focus:** Fun and entertainment
- **Entry cost:** ~$35/session
- **Skill:** amp-concession-karting-advisor

---

## Membership Hierarchy

### Road Course Tiers

| Tier | Initiation | Monthly | Weekend Days |
|------|------------|---------|--------------|
| Platinum Individual | $25,000 | $299 | 24/year |
| Diamond Individual | $50,000 | $299 | 48/year |
| Diamond + Family | $60,000 | $399 | 48/year |
| Corporate Diamond | $100,000 | $899 | 48/year |

### Race Karting Tiers

| Tier | Initiation | Monthly | Daily |
|------|------------|---------|-------|
| Standard | $3,500 | $95 | $20 |
| Standard Add-on | $2,000 | $55 | $20 |
| Lifetime | $10,000 | None | None |
| Lifetime Add-on | $5,500 | None | None |

---

## Key Distinctions

### Road Course vs Karting
| Aspect | Road Course | Karting |
|--------|-------------|---------|
| Vehicle | Cars/Motorcycles | Go-karts |
| Track | 2-mile circuit | Kart track |
| Cost | Higher ($25K+) | Lower ($3.5K+) |
| Age | Licensed drivers | Age 5+ |
| Focus | Community/Hobby | Competition |

### Race Karting vs Concession Karting
| Aspect | Race Karting | Concession Karting |
|--------|--------------|-------------------|
| Karts | Own your own | Rent from AMP |
| Membership | Required | Not required |
| Age | 5+ | 12+ / 60" tall |
| Speed | 40-70+ mph | ~35 mph |
| Focus | Competition | Entertainment |

---

## Common Customer Confusions

| What They Say | What They Mean | Correct Program |
|---------------|----------------|-----------------|
| "Karting membership to drive my car" | Road course access | Road Course Membership |
| "Membership to rent karts" | Casual karting | Concession (no membership) |
| "My 8-year-old wants karting" | Kids karting | Race Karting (8 eligible for Cadet) or Junior Discovery |
| "How much is membership?" | Need clarification | Ask: cars or karts? |

---

## Non-Member Options

### Road Course
- Public events (driving schools, experiences): https://www.atlantamotorsportspark.com/events/
- Come as a member's guest

### Karting
- Rental sessions: bookings.clubspeed.com/amp
- Leagues/Enduros: motorsportreg.com/orgs/atlanta-motorsports-park/events
- Junior Discovery (ages 5-11): $249, motorsportreg.com

---

## Key Contacts

| For | Contact |
|-----|---------|
| Membership (all types) | shawn@atlantamotorsportspark.com |
| Karting schools/lessons | eli@ampkartracing.com |
| Rental karting booking | bookings.clubspeed.com/amp |
| Public events | https://www.atlantamotorsportspark.com/events/ |
| Member calendar | theclub.atlantamotorsportspark.com/calendar/ |

---

## System Integrations

AMP uses several systems that may appear in customer service contexts:

| System | Purpose |
|--------|---------|
| Clubspeed | Karting booking, timing, member management |
| Glue Up | Membership CRM |
| MotorsportReg | Event registration (leagues, enduros, racing) |
| Google Workspace | Calendars, documents |
| Zoho CRM | Lead tracking, customer management |

---

## Skill Routing Summary

| Customer Intent | Route To |
|-----------------|----------|
| Cars/motorcycles on track | amp-main-track-advisor |
| Own race kart, compete | amp-karting-advisor |
| Rent kart for fun | amp-concession-karting-advisor |
| Compare membership options | amp-membership-explorer |
| Find events | amp-event-finder |
| Track rules/safety | amp-rules-expert |
| New member questions | amp-onboarding-coordinator |
| Complaints/escalation | amp-escalation-handler |
| Initial classification | amp-lead-qualifier |

---

## Business Philosophy

AMP emphasizes:
1. **Community over competition** - Especially on road course, it's about finding your tribe
2. **Safety first** - Rules exist for good reasons
3. **Proper preparation** - Don't skip the learning curve
4. **Long-term relationships** - Membership model builds community
5. **Clear communication** - Set proper expectations

**Key message to prospects:**
> "Becoming an AMP member makes this your home track."
