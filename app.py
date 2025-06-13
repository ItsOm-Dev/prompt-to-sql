import sqlite3
from mistral_interface import ask_mistral
import re
def get_schema_description():
    return """
Table: users
Columns:
- id (INTEGER)
- name (TEXT)
- email (TEXT)
- signup_date (DATE)
"""
import re

def make_case_insensitive(sql):
    """
    Add COLLATE NOCASE to string comparisons in WHERE clause.
    """
    def replacer(match):
        return f"{match.group(1)} = {match.group(2)} COLLATE NOCASE"

    # Only process UPDATE, DELETE, or SELECT
    if sql.strip().lower().startswith(("update", "delete", "select")):
        # Match patterns like name = 'alice'
        sql = re.sub(r"(\w+)\s*=\s*('[^']+')", replacer, sql, flags=re.IGNORECASE)
    return sql



def run_query(query):
    conn = sqlite3.connect("db/sample.db")
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        if sql.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            print("\nRESULTS:")
            print(columns)            
            for row in rows:
                print(row)
        else:
            conn.commit()
            print("Query executed successfully.")

        # cursor.execute(query)
        # rows = cursor.fetchall()
        # columns = [desc[0] for desc in cursor.description]
        # print("\nRESULTS:")
        # print(columns)
        # for row in rows:
        #     print(row)
    except Exception as e:
        print("Error running query:", e)
    finally:
        conn.close()



if __name__ == "__main__":
    while(True):
        print("Prompt-to-SQL Assistant using Mistral\n")
        question = input("Enter your query: ")
        if(question=="b"):
            break
        schema = get_schema_description()
        sql = ask_mistral(question, schema)
        sql = make_case_insensitive(sql)
        print("\nModified generated SQL:\n", sql)
        run_query(sql)
