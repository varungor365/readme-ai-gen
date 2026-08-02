# readme-ai-gen - AI Agent Guidelines

## Context
This CLI tool scans a local codebase (respecting `.gitignore`) and uses OpenAI's GPT-4o API to generate a highly-optimized `README.md`.

## Architecture
- `scanner.py`: Handles directory traversal and file reading. It limits the context size to avoid blowing up LLM token limits and ignores binary/heavy files.
- `ai.py`: Wraps the OpenAI API call.
- `cli.py`: The `rich` CLI interface.

## Rules for Agents
- Keep the UI lightweight and beautiful using `rich`.
- Ensure tests in `tests/test_readme_ai_gen.py` are updated if `scanner.py` or `ai.py` logic changes.
- Always mock the `OpenAI` client in tests.
