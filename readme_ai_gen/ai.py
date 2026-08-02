import os

from openai import OpenAI


def generate_readme(context: str, project_name: str) -> str:
    """Sends the codebase context to OpenAI to generate a trending-optimized README."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")
        
    client = OpenAI(api_key=api_key)
    
    system_prompt = """You are an expert open-source maintainer and technical writer. 
Your task is to write a highly-engaging, SEO-optimized README.md for a GitHub repository.
You will be provided with the project name and the codebase context (directory structure + file contents).

Your README MUST include:
1. A centered header with an emoji, the project name, and a punchy 1-sentence tagline.
2. Placeholder for GitHub badges (e.g. License, CI, Version).
3. A "✨ Why this exists" section explaining the value proposition.
4. A "🚀 Quickstart" section with clear installation and usage instructions.
5. A "📖 Features" list.
6. A "🤖 AI Agent Context" section explaining how AI tools should interact with this repo.

Write the README directly in Markdown. Do not include markdown block backticks (```markdown) around the entire output. Just output the raw markdown text. Make it look beautiful and professional."""

    user_prompt = f"Project Name: {project_name}\n\nCodebase Context:\n{context}"
    
    response = client.chat.completions.create(
        model="gpt-4o", # Using GPT-4o for better reasoning over large codebases
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )
    
    return response.choices[0].message.content.strip()
