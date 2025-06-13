# Prompt-to-SQL Assistant (Powered by Mistral via Ollama)

## What It Does
Takes natural language questions and converts them into SQL queries using Mistral LLM, then runs them on a local SQLite database.

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
**Input:** "Show all users who signed up in the last 7 days"  
**Output SQL:** `SELECT * FROM users WHERE signup_date >= DATE('now', '-7 day');`

## Tech Stack
- Python
- SQLite
- Ollama (Mistral model)

## Future Features
- Web UI with Flask
- Export results to CSV
- Use AI to explain SQL queries
