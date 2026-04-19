from openai import OpenAI
import streamlit as st

st.title("EduGenie 🤖")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

user_input = st.text_input("Ask your question:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": user_input}]
    )

    st.write(response.choices[0].message.content)
