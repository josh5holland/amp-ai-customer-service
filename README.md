# AMP AI Customer Service Skills

## What This Repository Does
This repository contains modular AI "skills" that power Atlanta Motorsports Park's automated customer service system. Each skill is a specialized knowledge module that helps our AI assistant answer specific types of customer inquiries via email.

**Dual-Purpose Design**: These skills also serve as knowledge bases for **Claude Code** instances working on AMP's mobile app, CRM, and other codebases. See [Claude Code Integration Guide](docs/CLAUDE_CODE_INTEGRATION.md) for details.

## Which AMP Systems This Connects To
- **N8N** - Workflow automation (triggers email processing)
- **Zoho CRM** - Customer data and lead management
- **Clubspeed** - Karting bookings and timing data
- **Google Workspace** - Email handling via Gmail API

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/josh5holland/amp-ai-customer-service.git

# 2. Install dependencies
cd amp-ai-customer-service
npm install

# 3. Copy environment template and add your API keys
cp .env.example .env

# 4. Test a skill locally
python scripts/test-skill.py amp-karting-advisor
```

---

## Repository Structure

```
amp-ai-customer-service/
├── docs/                    # Architecture & deployment guides
├── skills/                  # The 8 AI skill modules
│   ├── amp-lead-qualifier/
│   ├── amp-karting-advisor/
│   ├── amp-membership-explorer/
│   ├── amp-rules-expert/
│   ├── amp-event-finder/
│   ├── amp-concession-redirect/
│   ├── amp-escalation-handler/
│   └── amp-onboarding-coordinator/
├── n8n-workflows/           # N8N workflow JSON exports
├── scripts/                 # Deployment & utility scripts
├── source-docs/             # Original AMP documentation
├── tests/                   # Test emails & expected responses
└── metrics/                 # Dashboard templates & reports
```

---

## The 8 Skills

| Skill | Purpose |
|-------|---------|
| **Lead Qualifier** | Classifies incoming emails by intent and priority |
| **Karting Advisor** | Answers questions about rental karting, pricing, requirements |
| **Membership Explorer** | Explains membership tiers, benefits, and ROI |
| **Rules Expert** | Provides accurate info on track rules, safety, noise limits |
| **Event Finder** | Helps customers find races, track days, and social events |
| **Concession Redirect** | Directs non-member track rental inquiries appropriately |
| **Escalation Handler** | Manages complex issues that need human intervention |
| **Onboarding Coordinator** | Guides new members through orientation process |

---

## Skill Routing Flow

When a customer inquiry comes in, the **Lead Qualifier** analyzes it and routes to the appropriate skill:

```mermaid
flowchart TB
    subgraph INPUT["Customer Inquiry"]
        A[("Email / Chat / Web Form")]
    end

    subgraph QUALIFIER["Traffic Controller"]
        B["amp-lead-qualifier<br/>Classify Intent & Priority"]
    end

    A --> B

    subgraph SKILLS["Specialized Skills"]
        direction TB

        subgraph PREMIUM["Premium Memberships"]
            C["amp-main-track-advisor<br/>Cars & Motorcycles<br/>$25K-$100K"]
            D["amp-karting-advisor<br/>Race Karts - Own<br/>$3,500+"]
        end

        subgraph CASUAL["No Membership Required"]
            E["amp-concession-karting-advisor<br/>Rental Karts<br/>$39.99/session"]
        end

        subgraph SUPPORT["Support Skills"]
            F["amp-membership-explorer<br/>Compare Options"]
            G["amp-event-finder<br/>Calendar & Events"]
            H["amp-rules-expert<br/>Safety & Policies"]
            I["amp-onboarding-coordinator<br/>New Member Help"]
        end
    end

    subgraph ESCALATE["Human Handoff"]
        J["amp-escalation-handler<br/>Safety / Legal / Complaints"]
        K[("Human Team<br/>Shawn / Eli / Jessica / Info")]
    end

    B -->|"road_course"| C
    B -->|"race_karting"| D
    B -->|"concession_karting"| E
    B -->|"membership_comparison"| F
    B -->|"events"| G
    B -->|"rules"| H
    B -->|"onboarding"| I
    B -->|"escalation"| J

    J --> K

    E -.->|"wants serious racing"| D
    E -.->|"child under 12"| D
    F -.->|"cars/motos"| C
    F -.->|"own kart"| D
    F -.->|"rental karts"| E

    C -.->|"pricing/availability"| K
    D -.->|"schools/lessons"| K
    E -.->|"group events"| K

    style A fill:#2c3e50,stroke:#f39c12,color:#fff
    style B fill:#9b59b6,stroke:#8e44ad,color:#fff
    style C fill:#e74c3c,stroke:#c0392b,color:#fff
    style D fill:#3498db,stroke:#2980b9,color:#fff
    style E fill:#2ecc71,stroke:#27ae60,color:#fff
    style F fill:#f39c12,stroke:#d35400,color:#fff
    style G fill:#1abc9c,stroke:#16a085,color:#fff
    style H fill:#e67e22,stroke:#d35400,color:#fff
    style I fill:#9b59b6,stroke:#8e44ad,color:#fff
    style J fill:#c0392b,stroke:#922b21,color:#fff
    style K fill:#34495e,stroke:#2c3e50,color:#fff
```

### Intent Detection Keywords

```mermaid
flowchart LR
    subgraph KEYWORDS["Customer Says..."]
        direction TB
        K1["Porsche, GT3, motorcycle,<br/>track day, 2-mile circuit"]
        K2["Own kart, LO206, TaG,<br/>Kid Kart, competitive"]
        K3["Birthday party, rental,<br/>group event, league"]
        K4["Which membership?<br/>Confused, comparing"]
        K5["Calendar, schedule,<br/>what's happening"]
        K6["Helmet, safety gear,<br/>noise limit, flags"]
        K7["Just joined, first visit,<br/>new member"]
        K8["Refund, complaint,<br/>lawyer, ANGRY!!!"]
    end

    subgraph ROUTES["Routes To..."]
        direction TB
        R1["amp-main-track-advisor"]
        R2["amp-karting-advisor"]
        R3["amp-concession-karting-advisor"]
        R4["amp-membership-explorer"]
        R5["amp-event-finder"]
        R6["amp-rules-expert"]
        R7["amp-onboarding-coordinator"]
        R8["amp-escalation-handler"]
    end

    K1 --> R1
    K2 --> R2
    K3 --> R3
    K4 --> R4
    K5 --> R5
    K6 --> R6
    K7 --> R7
    K8 --> R8

    style K1 fill:#e74c3c,color:#fff
    style K2 fill:#3498db,color:#fff
    style K3 fill:#2ecc71,color:#fff
    style K4 fill:#f39c12,color:#fff
    style K5 fill:#1abc9c,color:#fff
    style K6 fill:#e67e22,color:#fff
    style K7 fill:#9b59b6,color:#fff
    style K8 fill:#c0392b,color:#fff
    style R1 fill:#e74c3c,color:#fff
    style R2 fill:#3498db,color:#fff
    style R3 fill:#2ecc71,color:#fff
    style R4 fill:#f39c12,color:#fff
    style R5 fill:#1abc9c,color:#fff
    style R6 fill:#e67e22,color:#fff
    style R7 fill:#9b59b6,color:#fff
    style R8 fill:#c0392b,color:#fff
```

### Escalation Flow

```mermaid
flowchart TB
    subgraph TRIGGERS["Escalation Triggers"]
        direction LR
        T1["Safety<br/>Injury, Accident"]
        T2["Legal<br/>Lawyer, Lawsuit"]
        T3["Financial<br/>Refund, Billing"]
        T4["Sentiment<br/>ALL CAPS, Angry"]
        T5["VIP/Media<br/>Reporter, Influencer"]
    end

    subgraph HANDLER["amp-escalation-handler"]
        H1["Acknowledge concern"]
        H2["Summarize for human"]
        H3["Set expectations"]
        H4["Route to contact"]
    end

    subgraph HUMANS["Human Team"]
        direction LR
        P1["Shawn<br/>Membership"]
        P2["Eli<br/>Karting"]
        P3["Jessica<br/>Events"]
        P4["Info<br/>General"]
    end

    T1 --> H1
    T2 --> H1
    T3 --> H1
    T4 --> H1
    T5 --> H1

    H1 --> H2 --> H3 --> H4

    H4 --> P1
    H4 --> P2
    H4 --> P3
    H4 --> P4

    style T1 fill:#c0392b,color:#fff
    style T2 fill:#8e44ad,color:#fff
    style T3 fill:#d35400,color:#fff
    style T4 fill:#c0392b,color:#fff
    style T5 fill:#2980b9,color:#fff
    style H1 fill:#34495e,color:#fff
    style H2 fill:#34495e,color:#fff
    style H3 fill:#34495e,color:#fff
    style H4 fill:#34495e,color:#fff
    style P1 fill:#27ae60,color:#fff
    style P2 fill:#27ae60,color:#fff
    style P3 fill:#27ae60,color:#fff
    style P4 fill:#27ae60,color:#fff
```

### Human Contact Reference

| Contact | Email | Handles |
|---------|-------|---------|
| **Shawn** | shawn@atlantamotorsportspark.com | Membership inquiries |
| **Eli** | eli@ampkartracing.com | Karting schools & lessons |
| **Jessica** | jessica@atlantamotorsportspark.com | Group events & track rentals |
| **Info** | info@atlantamotorsportspark.com | General & complaints |

---

## Environment Variables

See `.env.example` for all required API keys and configuration.

---

## Security Notes

- **Never commit `.env` files** - they contain API secrets
- All API keys should be stored in environment variables
- This repository is private - do not make public without security review

---

## Documentation

- [Architecture Overview](docs/ARCHITECTURE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Skill Development Guide](docs/SKILL_DEVELOPMENT_GUIDE.md)
- [N8N Setup Instructions](docs/N8N_SETUP.md)
- [Claude Code Integration Guide](docs/CLAUDE_CODE_INTEGRATION.md) - Making skills work for developer AI

---

## Support

For questions about this system, contact the AMP Implementation Team.
