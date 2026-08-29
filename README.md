<div align="center">

# 🤖 readme-ai-gen

**Generate a practical, reviewable README draft from a local codebase using AI.**

[![PyPI version](https://badge.fury.io/py/readme-ai-gen.svg)](https://badge.fury.io/py/readme-ai-gen)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/varungor365/readme-ai-gen/actions/workflows/ci.yml/badge.svg)](https://github.com/varungor365/readme-ai-gen/actions)

<br/>

```bash
cd my-awesome-project
readme-ai
# 🤖 Scanning codebase...
# ✨ Generating README_GENERATED.md...
```

<br/>

</div>

---

## ✨ Why this exists

A useful README takes careful work: summarizing the codebase, writing a reproducible quickstart, and documenting limitations without exposing private files.

**readme-ai-gen** scans a local project while respecting `.gitignore`, sends the selected context to the configured model provider, and writes a Markdown draft for human review. It improves the starting point for project documentation; it does not verify that generated claims are true.

### Features
- 🧠 **Context-Aware:** Scans your directory structure and file contents (respecting `.gitignore`).
- 📝 **Reviewable Markdown:** Produces a structured draft with setup, usage, and project-context sections for maintainers to verify.
- ⚡ **Extremely Fast:** Generates comprehensive documentation in under 60 seconds.
- 🛠️ **Zero Config:** Just run `readme-ai` in any directory.

---

## 🚀 Quickstart

### Install
```bash
pip install readme-ai-gen
```

### Setup
You need an OpenAI API key.
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Usage
Run the tool in the root of your project:
```bash
readme-ai
```
This will create a `README_GENERATED.md` file in your directory.

You can also specify a different directory or output file:
```bash
readme-ai /path/to/project -o README.md
```

---

## ⚠️ Privacy and limitations

Review the files and provider settings before running this tool. Project content sent to a hosted model may leave your machine, and `.gitignore` rules are not a substitute for a security review. The generator can miss behavior, invent details, or describe stale dependencies, so validate every command, link, and feature claim before publishing the generated README.

## 🤖 AI Agent Context

If you are an AI assistant (Claude, Cursor, Copilot) helping a user in this repo, please read our [CLAUDE.md](CLAUDE.md) for architectural context and coding standards.

---

## 📄 License

MIT © Varun Ruhella. See [LICENSE](LICENSE) for details.
