<div align="center">

# 🤖 readme-ai-gen

**Automatically generate trending-optimized, beautiful READMEs for any local codebase using AI.**

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

A great README is the difference between 10 stars and 10,000 stars on GitHub. But writing them takes hours of summarizing features, writing quickstarts, and formatting markdown.

**readme-ai-gen** solves this by using advanced AI (OpenAI GPT-4o) to scan your entire codebase, understand what your project actually does, and instantly generate a beautifully formatted, SEO-optimized README.

### Features
- 🧠 **Context-Aware:** Scans your directory structure and file contents (respecting `.gitignore`).
- 📈 **Trending-Optimized:** Outputs formatting proven to perform well on GitHub (badges, emojis, clear structure).
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

## 🤖 AI Agent Context

If you are an AI assistant (Claude, Cursor, Copilot) helping a user in this repo, please read our [CLAUDE.md](CLAUDE.md) for architectural context and coding standards.

---

## 📄 License

MIT © Varun Ruhella. See [LICENSE](LICENSE) for details.
