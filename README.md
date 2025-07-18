# 🧠 Text-to-SQL Generator using Gemini LLM

A full-stack AI-powered tool that converts natural language questions into SQL queries using Google’s Gemini API and displays the results in a Streamlit interface.

---

## 🔍 Demo

Ask questions like:
  Who are the employees in the HR department?
List all employees with a salary greater than 50,000

⚙️ Features
🔁 Converts natural language to SQL using Gemini 1.5 Flash

🧠 Uses prompt engineering for structured SQL output

📊 Live interaction with a SQLite database

⚡ Clean, responsive UI using Streamlit

🔐 Secure API key storage with .env


🧠 Tech Stack

Layer	Technology
Frontend UI	Streamlit
Backend Logic	Python (sql_chain.py)
LLM	Gemini 1.5 Flash via google.generativeai
Database	SQLite (local)
Secrets Mgmt	python-dotenv + .env
