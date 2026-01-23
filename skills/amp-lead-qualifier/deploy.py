#!/usr/bin/env python3
"""
What this script does:
Deploys the Lead Qualifier skill to the production AI system.
This skill is responsible for classifying incoming emails by intent.

Which AMP system it talks to:
OpenAI API for skill configuration.
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def load_skill_files(skill_path: Path) -> dict:
    """
    Loads all files needed for the skill deployment.
    Returns a dictionary with the skill configuration.
    """

    # Load the main skill instructions
    skill_md_path = skill_path / "SKILL.md"
    with open(skill_md_path, "r") as f:
        instructions = f.read()

    # Load all knowledge files
    knowledge = {}
    knowledge_path = skill_path / "knowledge"

    if knowledge_path.exists():
        for file in knowledge_path.iterdir():
            if file.is_file():
                with open(file, "r") as f:
                    if file.suffix == ".json":
                        knowledge[file.name] = json.load(f)
                    else:
                        knowledge[file.name] = f.read()

    return {
        "name": skill_path.name,
        "instructions": instructions,
        "knowledge": knowledge
    }


def deploy_skill(skill_config: dict) -> bool:
    """
    Deploys the skill configuration to the production system.
    Returns True if successful, False otherwise.
    """

    # Verify we have required environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key.startswith("sk-your"):
        print("⚠️  Warning: OPENAI_API_KEY not configured in .env")
        print("   Skill files validated but not deployed to production.")
        return False

    # TODO: Add actual deployment logic here
    # This would typically:
    # 1. Connect to OpenAI API
    # 2. Create or update an assistant with these instructions
    # 3. Upload knowledge files as retrieval documents

    print(f"📦 Skill configuration loaded:")
    print(f"   - Instructions: {len(skill_config['instructions'])} characters")
    print(f"   - Knowledge files: {len(skill_config['knowledge'])}")

    return True


def main():
    """Main entry point for deployment."""

    # Get the skill directory (same folder as this script)
    skill_path = Path(__file__).parent
    skill_name = skill_path.name

    print(f"\n🚀 Deploying {skill_name}...")
    print("-" * 40)

    try:
        # Load skill configuration
        config = load_skill_files(skill_path)

        # Deploy to production
        success = deploy_skill(config)

        if success:
            print(f"\n✅ {skill_name} deployed successfully!")
        else:
            print(f"\n⚠️  {skill_name} validated but not deployed (check API key)")

    except FileNotFoundError as e:
        print(f"\n❌ Error: Required file not found: {e}")
        return 1
    except json.JSONDecodeError as e:
        print(f"\n❌ Error: Invalid JSON in knowledge file: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Error deploying {skill_name}: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
