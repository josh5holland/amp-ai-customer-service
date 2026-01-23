# AMP AI Skills

## What This Folder Contains
This folder contains 9 AI skills that power the AMP customer service automation. Each skill is a specialized module that handles a specific type of customer inquiry.

---

## Skill Overview

| Skill | Folder | Primary Use Case | Status |
|-------|--------|------------------|--------|
| Lead Qualifier | `amp-lead-qualifier/` | Classifies incoming emails by intent | Ready |
| Main Track Advisor | `amp-main-track-advisor/` | Road course membership (cars/motorcycles) | Ready |
| Karting Advisor | `amp-karting-advisor/` | Race karting membership (personal karts) | Ready |
| Concession Karting Advisor | `amp-concession-karting-advisor/` | Arrive-and-drive rental karting | Ready |
| Membership Explorer | `amp-membership-explorer/` | Compare membership options | Ready |
| Event Finder | `amp-event-finder/` | Calendar and event information | Ready |
| Rules Expert | `amp-rules-expert/` | Track rules and safety policies | Ready |
| Onboarding Coordinator | `amp-onboarding-coordinator/` | New member orientation | Ready |
| Escalation Handler | `amp-escalation-handler/` | Complex issues needing humans | Ready |

---

## Skill Routing Flow

```
INCOMING EMAIL
      │
      ▼
amp-lead-qualifier (classify intent)
      │
      ├─► road_course ──────────► amp-main-track-advisor
      ├─► race_karting ─────────► amp-karting-advisor
      ├─► concession_karting ───► amp-concession-karting-advisor
      ├─► membership_comparison ► amp-membership-explorer
      ├─► events ───────────────► amp-event-finder
      ├─► rules ────────────────► amp-rules-expert
      ├─► onboarding ───────────► amp-onboarding-coordinator
      └─► escalation ───────────► amp-escalation-handler
```

---

## Skill Structure

Each skill follows this structure:

```
amp-[skill-name]/
├── SKILL.md              # Customer service AI instructions
├── CLAUDE_CODE.md        # Developer/AI context reference
├── knowledge/            # Reference data
│   └── *.md              # Knowledge documents
└── scripts/              # Helper tools (optional)
```

### File Purposes:
- **SKILL.md**: Instructions for customer-facing AI responses
- **CLAUDE_CODE.md**: Quick reference for AI assistants and developers
- **knowledge/*.md**: Detailed information organized by topic

---

## Skill Descriptions

### amp-lead-qualifier
The "traffic controller" - classifies all incoming inquiries and routes to appropriate skill.

### amp-main-track-advisor
Road course membership for cars and motorcycles. Handles Platinum/Diamond tiers, competition options, non-member alternatives.

### amp-karting-advisor
Race karting membership for people who own/buy their own race kart. Covers schools, equipment, classes by age.

### amp-concession-karting-advisor
Arrive-and-drive rental karting. No membership required. Includes leagues, enduros, Junior Discovery (ages 5-11).

### amp-membership-explorer
Helps confused prospects compare different membership types. Routes to specific advisors after clarification.

### amp-event-finder
Helps customers find events and calendars. Distinguishes member calendar from public events.

### amp-rules-expert
Track rules, safety requirements, vehicle requirements, flag meanings.

### amp-onboarding-coordinator
Guides new members from "I just joined" to first track day.

### amp-escalation-handler
Recognizes when human intervention is needed. Safety, legal, refunds, complaints.

---

## Quick Commands

```bash
# Test a specific skill
python scripts/test-skill.py amp-karting-advisor

# Deploy a specific skill
python scripts/deploy-skill.py amp-karting-advisor

# Deploy all skills
python scripts/deploy-all-skills.py

# Update knowledge and redeploy
python scripts/update-knowledge.py amp-karting-advisor
```

---

## Key Documentation

| Document | Location | Purpose |
|----------|----------|---------|
| Business Model Overview | `docs/AMP_BUSINESS_MODEL.md` | Complete business context |
| Skill Routing Map | `docs/SKILL_ROUTING_MAP.md` | Decision trees for routing |
| Claude Code Integration | `docs/CLAUDE_CODE_INTEGRATION.md` | Dual-purpose skill design |
| Skill Development Guide | `docs/SKILL_DEVELOPMENT_GUIDE.md` | How to create new skills |

---

## Adding a New Skill

See [Skill Development Guide](../docs/SKILL_DEVELOPMENT_GUIDE.md) for detailed instructions.

Quick steps:
1. Create folder: `mkdir -p skills/amp-new-skill/knowledge`
2. Write SKILL.md with customer service AI instructions
3. Write CLAUDE_CODE.md with developer/AI context
4. Add knowledge files
5. Update amp-lead-qualifier to route to new skill
6. Test and deploy

---

## Maintenance Notes

- **Monthly**: Review knowledge files for pricing/schedule accuracy
- **Quarterly**: Analyze which skills are used most
- **Annually**: Full review of all skill instructions
- **After changes**: Update amp-lead-qualifier intent-classification-examples.json
