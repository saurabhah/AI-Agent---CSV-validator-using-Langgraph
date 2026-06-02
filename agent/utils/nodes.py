import pandas as pd
from utils.db_connection import get_schema
from utils.connect_llm import get_llm

def load_csv_node(state):
    """Node to load CSV data from a given file path and store it in the state."""

    df = pd.read_csv(state["file_path"])

    state["csv_rows"] = df.to_dict(orient="records")

    return state


def schema_node(state):
    """Node to fetch the database schema for a given table and store it in the state."""
    schema = get_schema(state["db_table"])
    state["db_schema"] = schema
    return state


def validation_node(state):
    """Node to validate CSV rows against the database schema using an LLM."""
    errors = []
    print("Validating rows...")
    schema = state["db_schema"]
    csv_rows = state["csv_rows"]
    llm = get_llm()
    prompt = prompt = f"""You are a data validation expert.

You are given a PostgreSQL table schema and rows from a CSV file.
Compare every CSV row against the schema and identify ALL issues.

## DB Table Schema
{schema}


## CSV Rows to validate
{csv_rows}

## Instructions
Return a JSON array of ONLY the rows that have issues.
Each item must follow this exact structure:
[
  {{
    "row_index": <int>,
    "row_data": {{<original row dict>}},
    "issues": ["<issue description>", ...]
  }}
]

Check every row for:
1. NULL or missing value in a NOT NULL column
2. Wrong data type (e.g. text in an integer column)
3. Invalid email format (must contain @ and .)


Return ONLY the raw JSON array. No markdown, no explanation, no code fences.
If all rows are valid return an empty dict: {}
"""

    response = llm.invoke(prompt)
    return response.content