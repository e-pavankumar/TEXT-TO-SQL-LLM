# app.py
import streamlit as st
from sql_chain import ask_question

st.title("🧠 Text-to-SQL Generator using GPT")

query = st.text_input("Ask a question about the database:")

if st.button("Generate SQL & Run"):
    with st.spinner("Generating & Executing SQL..."):
        try:
            result = ask_question(query)
            st.success("Result:")
            st.write(result)
        except Exception as e:
            st.error(f"Error: {e}")
