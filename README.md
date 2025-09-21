Gemini SQL Assistant 
Project Overview

This repository contains a small SQLite + Streamlit app that converts natural-language questions into SQLite SQL queries (via the Gemini API), runs them against a local SQLite database, and optionally explains the generated SQL. It’s a lightweight demo / utility for working with an example database (ipl_csk_players.db) and experimenting with LLM-assisted SQL generation.

Files in this repo (what’s included)

app.py — Streamlit web UI.

Accepts an English question, calls the Gemini model to generate SQL, executes the SQL against the SQLite DB, shows results, and can ask Gemini to explain the SQL.

sql.py — Database setup script.

Creates the ipl_csk_players table and inserts sample records.

app.env / .env — (example) environment file containing GEMINI_API_KEY. Do not commit real keys to public repos.

Modules & Sub-Modules (mapped to code)
1. UI (Streamlit)

Landing + input box for English questions.

Suggestions/examples expander.

Buttons to generate & run SQL.

Sections to show: generated SQL, query result (pandas dataframe), and an expandable SQL explanation.

2. LLM Integration

get_gemini_sql(question, prompt) — uses google.generativeai to transform English question → SQL.

explain_sql_query(query) — optional Gemini-powered explanation of the SQL.

3. Database

read_sql_query(sql, db) — runs the SQL against SQLite and returns rows + column names.

sql.py — creates ipl_csk_players with columns:

players_name (varchar)

players_role (varchar)

players_age (int)

players_salary (float)

Sample entries inserted by sql.py (e.g., Ruturaj Gaikwad, MS Dhoni, etc.)

Tech Stack

Python 3.8+

Streamlit (UI)

SQLite (local DB)

google.generativeai (Gemini API client)

python-dotenv (load .env)

pandas (display results)

Features

Translate plain-English questions into valid SQLite queries (via Gemini).

Execute those queries on a local SQLite DB.

Display results as an interactive table (pandas / Streamlit).

Ask the LLM for a step-by-step explanation of the generated SQL.

Example queries provided in the UI.

Install required packages

streamlit 

pandas 

python-dotenv 

google-generativeai


Open the URL printed by Streamlit (usually http://localhost:8501).

Example Questions to Try (shown in the UI)

List all players.

Show only Batsmen.

Who earns more than 300000?

Count of Allrounder?

Who has the highest salary?

Average salary by players_role?

Security / Best Practices

Add the following to .gitignore:

.env
app.env
ipl_csk_players.db
__pycache__/
