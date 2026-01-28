# AMP Customer Service Skill Tester

A simple chat interface for AMP employees to test the AI customer service skills before public release.

## Quick Start (Local)

```bash
# 1. Navigate to tester directory
cd tester

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up secrets
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit secrets.toml with your API key and password

# 4. Run the app
streamlit run app.py
```

The app will open at http://localhost:8501

## Deploying to Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select this repo, branch `main`, and file `tester/app.py`
5. In "Advanced settings", add your secrets:
   ```
   ANTHROPIC_API_KEY = "sk-ant-api03-..."
   APP_PASSWORD = "your-team-password"
   ```
6. Click "Deploy"

Your team can then access it at `https://[your-app-name].streamlit.app`

## How It Works

1. Loads all skill files from `../skills/*/SKILL.md` and their knowledge files
2. Injects them into the first message to Claude
3. Claude identifies intent and uses the appropriate skill
4. Shows which skill is being used in each response

## Testing Tips

Try these types of questions:
- "How much does rental karting cost?" (concession-karting-advisor)
- "I want to bring my own kart to race" (karting-advisor)
- "What memberships do you have?" (membership-explorer)
- "I want to drive my Porsche on the track" (main-track-advisor)
- "I WANT A REFUND THIS IS RIDICULOUS" (escalation-handler)
- "When is the next track day?" (event-finder)
- "What helmet do I need?" (rules-expert)
- "I just joined, what do I do now?" (onboarding-coordinator)
