import subprocess

def ask_mistral(question, schema_description):
    prompt = f"""
You are a helpful assistant that translates natural language questions into SQL queries.

Given the question: "{question}"
And the database schema: {schema_description}

Generate an SQL query only. Do not explain or add any extra text.
"""
    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
          encoding='utf-8',  # Explicitly decode output as UTF-8
        errors='replace' 
    )
    return result.stdout.strip()
