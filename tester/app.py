"""
AMP Customer Service Skill Tester
---------------------------------
A simple Streamlit app for AMP employees to test the AI customer service skills.

This app:
- Loads all skills from the ../skills directory
- Provides a chat interface to test customer inquiries
- Uses Claude API to generate responses
- Shows which skill handled the inquiry

To run locally:
    streamlit run app.py

To deploy to Streamlit Cloud:
    1. Push to GitHub
    2. Connect repo at share.streamlit.io
    3. Add secrets in Streamlit Cloud dashboard
"""

import streamlit as st
import anthropic
from pathlib import Path
import os

# Page config
st.set_page_config(
    page_title="AMP Customer Service Tester",
    page_icon="🏎️",
    layout="centered"
)

# Simple password protection
def check_password():
    """Returns True if the user has entered the correct password."""

    def password_entered():
        """Check if password is correct."""
        if st.session_state["password"] == st.secrets.get("APP_PASSWORD", "amptest2024"):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Enter team password:",
            type="password",
            key="password",
            on_change=password_entered
        )
        st.caption("Ask your team lead for the password")
        return False

    if not st.session_state["password_correct"]:
        st.text_input(
            "Enter team password:",
            type="password",
            key="password",
            on_change=password_entered
        )
        st.error("Incorrect password")
        return False

    return True


def load_skills():
    """Load all SKILL.md files and their knowledge files from the skills directory."""

    skills_dir = Path(__file__).parent.parent / "skills"
    skills_content = []

    # Get all skill directories (excluding README.md)
    skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir() and d.name.startswith("amp-")]

    for skill_dir in sorted(skill_dirs):
        skill_name = skill_dir.name
        skill_file = skill_dir / "SKILL.md"

        if skill_file.exists():
            skill_text = skill_file.read_text()

            # Also load knowledge files
            knowledge_dir = skill_dir / "knowledge"
            knowledge_content = []

            if knowledge_dir.exists():
                for knowledge_file in sorted(knowledge_dir.glob("*.md")):
                    knowledge_name = knowledge_file.stem
                    knowledge_text = knowledge_file.read_text()
                    knowledge_content.append(f"<knowledge name=\"{knowledge_name}\">\n{knowledge_text}\n</knowledge>")

            # Combine skill and knowledge
            full_skill = skill_text
            if knowledge_content:
                full_skill += "\n\n## Supporting Knowledge\n" + "\n\n".join(knowledge_content)

            skills_content.append(f'<skill name="{skill_name}">\n{full_skill}\n</skill>')

    return "\n\n".join(skills_content)


def get_system_prompt():
    """Return the system prompt for the AI assistant."""
    return """You are AMP's customer service AI assistant. You help customers with inquiries about Atlanta Motorsports Park.

Your personality:
- Friendly, professional, and knowledgeable about motorsports
- Enthusiastic about racing but not pushy
- Clear and concise in your responses
- Always prioritize safety

Your process:
1. First, identify the customer's intent using the amp-lead-qualifier skill
2. Route to the appropriate specialized skill
3. Provide accurate information based on that skill's knowledge
4. If you need to escalate to a human, use the amp-escalation-handler guidelines

Always start your response by briefly noting which skill you're using in italics, like:
*Using amp-karting-advisor*

Then provide your response to the customer.

If multiple skills apply, mention all of them.

IMPORTANT: If you don't know something or the customer's question is outside your knowledge, say so and offer to connect them with a human team member."""


def main():
    st.title("🏎️ AMP Customer Service Tester")
    st.caption("Test the AI skills before they go live")

    # Check password
    if not check_password():
        return

    # Load skills (cached)
    @st.cache_data
    def get_skills():
        return load_skills()

    skills = get_skills()

    # Sidebar with info
    with st.sidebar:
        st.header("About")
        st.write("This app lets you test AMP's customer service AI by pretending to be a customer.")

        st.header("How to Test")
        st.write("""
        1. Type a customer question below
        2. See how the AI responds
        3. Note which skill it uses
        4. Try edge cases and tricky questions!
        """)

        st.header("Skills Loaded")
        skill_names = [
            "amp-lead-qualifier",
            "amp-main-track-advisor",
            "amp-karting-advisor",
            "amp-concession-karting-advisor",
            "amp-membership-explorer",
            "amp-event-finder",
            "amp-rules-expert",
            "amp-onboarding-coordinator",
            "amp-escalation-handler"
        ]
        for name in skill_names:
            st.write(f"• {name}")

        st.divider()
        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Type a customer question..."):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Prepare the full prompt with skills
        if len(st.session_state.messages) == 1:
            # First message - include skills
            full_user_message = f"""<skills>
{skills}
</skills>

<customer_inquiry>
{prompt}
</customer_inquiry>

Using the skills above, identify the customer's intent and respond appropriately."""
        else:
            # Subsequent messages - just the question
            full_user_message = f"""<customer_inquiry>
{prompt}
</customer_inquiry>

Continue helping this customer using the skills provided earlier."""

        # Build messages for API
        api_messages = []
        for i, msg in enumerate(st.session_state.messages):
            if msg["role"] == "user":
                if i == 0:
                    # First user message gets skills injected
                    api_messages.append({
                        "role": "user",
                        "content": f"""<skills>
{skills}
</skills>

<customer_inquiry>
{msg["content"]}
</customer_inquiry>

Using the skills above, identify the customer's intent and respond appropriately."""
                    })
                else:
                    api_messages.append({
                        "role": "user",
                        "content": f"""<customer_inquiry>
{msg["content"]}
</customer_inquiry>

Continue helping this customer."""
                    })
            else:
                api_messages.append(msg)

        # Get Claude response
        try:
            api_key = st.secrets.get("ANTHROPIC_API_KEY", os.environ.get("ANTHROPIC_API_KEY"))
            if not api_key:
                st.error("No API key found. Please set ANTHROPIC_API_KEY in secrets.")
                return

            client = anthropic.Anthropic(api_key=api_key)

            with st.chat_message("assistant"):
                # Stream the response
                with st.spinner("Thinking..."):
                    response = client.messages.create(
                        model="claude-sonnet-4-5-20250929",
                        max_tokens=1024,
                        system=get_system_prompt(),
                        messages=api_messages
                    )

                assistant_message = response.content[0].text
                st.markdown(assistant_message)

            # Add assistant message to history
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})

        except anthropic.APIError as e:
            st.error(f"API Error: {e}")
        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
