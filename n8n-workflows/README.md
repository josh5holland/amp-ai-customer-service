# N8N Workflows - AMP AI Customer Service

## What This Folder Contains

N8N workflow files for automating customer service tasks at Atlanta Motorsports Park. These workflows connect to external systems (Gmail, Claude API) to help staff respond to inquiries more efficiently.

---

## Corporate Karting Email Assistant

**File:** `corporate-karting-assistant.json`

### What It Does

1. Monitors Jessica's Gmail inbox for new emails
2. Uses Claude AI to detect if the email is about a group/corporate karting event
3. If yes, generates a templated response with calculated pricing
4. Creates a Gmail draft for Jessica to review and send

### Architecture

```
┌──────────────────┐     ┌─────────────────┐     ┌──────────────────┐
│  Jessica's       │────▶│  N8N Cloud      │────▶│  Claude API      │
│  Gmail Inbox     │     │  Workflow       │     │  (Sonnet)        │
└──────────────────┘     └─────────────────┘     └──────────────────┘
                                │
                                ▼
                         ┌──────────────────┐
                         │  Gmail Draft     │
                         │  (for review)    │
                         └──────────────────┘
```

### Setup Instructions

#### Step 1: Set Up Gmail Credential in N8N

1. In N8N Cloud, go to **Settings > Credentials**
2. Click **Add Credential**
3. Search for **Gmail OAuth2**
4. Click **Sign in with Google** and connect Jessica's account
5. Grant these permissions:
   - Read emails
   - Create drafts
   - Send emails (optional, for future use)
6. **Copy the credential ID** from the URL (looks like: `abc123...`)
7. Save the credential

#### Step 2: Set Up Anthropic API Credential

1. In N8N, go to **Settings > Credentials**
2. Click **Add Credential**
3. Search for **Header Auth**
4. Configure:
   - **Name:** `Anthropic API`
   - **Name (header):** `x-api-key`
   - **Value:** Your Anthropic API key (starts with `sk-ant-api03-...`)
5. **Copy the credential ID** from the URL
6. Save the credential

#### Step 3: Import the Workflow

1. In N8N, create a **New Workflow**
2. Click the **...** menu in the top right
3. Select **Import from File**
4. Upload `corporate-karting-assistant.json`
5. The workflow will appear with all nodes

#### Step 4: Update Credential References

After importing, you need to update the placeholder credential IDs:

1. **Gmail Trigger node:**
   - Click the node
   - Under Credentials, select your Gmail credential

2. **Filter Internal Emails node:**
   - No changes needed

3. **Intent Classifier (Claude) node:**
   - Click the node
   - Under Credentials, select your Header Auth (Anthropic API) credential

4. **Response Generator (Claude) node:**
   - Click the node
   - Under Credentials, select your Header Auth (Anthropic API) credential

5. **Create Gmail Draft node:**
   - Click the node
   - Under Credentials, select your Gmail credential

6. **Slack Notification node (optional):**
   - This node is disabled by default
   - To enable: click the node, then toggle "Active" on
   - You'll need to add a Slack credential
   - Update the channel name if not `#sales-notifications`

#### Step 5: Test the Workflow

1. Click **Execute Workflow** to run manually
2. Send a test email to Jessica's inbox:
   ```
   Subject: Corporate event for 15 people
   Body: Hi, I'm interested in booking a corporate team event for 15 people on a Saturday. Can you send me pricing?
   ```
3. The workflow should:
   - Detect it as a group event (confidence 80%+)
   - Generate the full template with weekend pricing ($4,617)
   - Create a draft in Jessica's Gmail

4. Check Jessica's Gmail Drafts folder - the response should be there

#### Step 6: Activate the Workflow

1. Once testing passes, click **Active** toggle (top right)
2. The workflow will now run automatically when new emails arrive

---

## Test Cases

Use these to verify the workflow is working correctly:

| Send This Email | Expected Result |
|-----------------|-----------------|
| "Corporate event for 15 people on Saturday" | Draft with weekend pricing ($4,617) |
| "Birthday party for 8 kids on Thursday" | Draft with weekday pricing (~$2,014) |
| "What are your hours?" | Skipped (not a group event) |
| "I want to race my Porsche on the track" | Skipped (not karting) |
| "Group event but haven't decided details yet" | Draft asking for day + guest count |

---

## Pricing Reference

The workflow uses this pricing logic (from `skills/amp-concession-karting-advisor/knowledge/group-event-template.md`):

### Weekend (Friday/Saturday/Sunday)
- **Base:** $4,200 (covers up to 20 guests)
- **Over 20 guests:** Add $209 per additional person
- **Award Ceremony:** $75
- **Tax:** 8%

### Weekday (Wednesday/Thursday)
- **Base:** $1,790 (covers up to 10 guests)
- **Over 10 guests:** Add $179 per additional person
- **Award Ceremony:** $75
- **Tax:** 8%

### Closed Days
- Monday and Tuesday - AMP is closed for group events

### Example Calculations

| Scenario | Calculation | Total |
|----------|-------------|-------|
| Weekend, 15 guests | $4,200 + $75 = $4,275 × 1.08 | **$4,617** |
| Weekend, 25 guests | ($4,200 + 5×$209) + $75 = $5,320 × 1.08 | **$5,745.60** |
| Weekday, 8 guests | $1,790 + $75 = $1,865 × 1.08 | **$2,014.20** |
| Weekday, 15 guests | ($1,790 + 5×$179) + $75 = $2,760 × 1.08 | **$2,980.80** |

---

## Cost Estimate

| Component | Cost |
|-----------|------|
| Intent Classifier call | ~$0.001 per email |
| Response generation | ~$0.01 per draft |
| N8N Cloud | Free tier covers this volume |
| **Per group event email** | **~$0.01** |

At typical volumes (50-100 group inquiries/month), expect ~$1-2/month in API costs.

---

## Troubleshooting

### Workflow Not Triggering

1. Check that the workflow is **Active** (toggle in top right)
2. Verify Gmail credential has proper permissions
3. Check N8N's Executions tab for errors

### Wrong Classification

If emails are being incorrectly classified:
1. Check the **Parse Classification** node output
2. Adjust the confidence threshold in **Is Group Event?** node (currently 70%)
3. Review the classification prompt in **Intent Classifier** node

### Pricing Errors

If pricing calculations are wrong:
1. Review the system prompt in **Response Generator** node
2. Compare against `skills/amp-concession-karting-advisor/knowledge/group-event-template.md`
3. Verify the customer's day of week and guest count

### Draft Not Created

1. Check Gmail credential permissions
2. Verify the **Prepare Draft** node output has valid data
3. Check N8N's Executions tab for the specific error

---

## Security Notes

- **API keys** are stored securely in N8N's credential system (never in workflow JSON)
- **Gmail OAuth** uses Google's secure authentication
- **Email content** is sent to Claude API - review Anthropic's data policies
- **Drafts only** - no emails are sent automatically, Jessica always reviews first

---

## Support

- **N8N Issues:** Check N8N's documentation at docs.n8n.io
- **Workflow Logic:** Update the skill files in `skills/amp-concession-karting-advisor/`
- **Pricing Updates:** Edit `skills/amp-concession-karting-advisor/knowledge/group-event-template.md` AND update the system prompt in the workflow
