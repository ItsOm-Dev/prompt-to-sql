# Prompt-to-SQL Assistant (Powered by Mistral via Ollama)

## What It Does
Takes natural language questions and converts them into SQL queries using Mistral LLM, then runs them on a local SQLite database.It translates natural language prompts into executable SQL queries using the Mistral large language model via Ollama. The tool then executes these queries on a local SQLite database and displays the results in real time.
This project demonstrates how to integrate local LLMs with traditional databases, making it a fully offline, privacy-respecting data query assistant.

## Installing Ollama and Mistral (Local LLM Setup)

This project uses the [Ollama](https://ollama.com) framework to run large language models like Mistral locally on your machine.

### Step 1: Download and Install Ollama

Visit the official Ollama website:

[https://ollama.com/download](https://ollama.com/download)

Choose the version for your operating system (Windows, macOS, or Linux) and follow the installation instructions.

### Step 2: Verify Installation

After installation, open a terminal and run:

```bash
ollama --version


## How to Run

1. Start Ollama and pull model:
```bash
ollama run mistral
```

2. Setup DB:
```bash
python setup_db.py
```

3. Start App:
```bash
python app.py
```

##  Example
**Input:** "show data/info"  
**Output SQL:** `SELECT * FROM users;`

## Tech Stack
- Python
- SQLite
- Ollama (Mistral model)

## Future Features
- Desktop UI using tkinter
- Web UI with Flask,django(for scaling)
- Export results to CSV
- Use AI to explain SQL queries
