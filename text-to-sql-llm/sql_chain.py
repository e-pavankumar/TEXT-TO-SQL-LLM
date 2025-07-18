import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyBLOBwp5dxWSoaltiXf3fC1cfZ4FsefHyo"))

# ✅ Use the flash model for more free usage
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def ask_question(nl_query):
    prompt = f"""
Convert the following natural language question into a valid SQL query 
for a table named 'employees':
{nl_query}

Only return SQL. No explanation.
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error from Gemini: {e}"
