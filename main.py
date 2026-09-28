from ollama import chat
import streamlit as st

st.title("My AI Bot: Synora")
name = "Priya"
st.write(f"Hello, {name}! Welcome to Synora, your AI assistant.")
question = st.text_input("Ask me anything:")
if st.button("Ask"):
    response = chat(model="gemma3:1b", messages=[
        {
            "role": "system",
            "content": "You are a friendly tutor. You explain concepts in a simple way and provide examples when necessary. You are patient and encouraging."
        },
        {
            "role": "user",
            "content": question
        }

    ])
    answer = response.message.content
    st.write(f"AI: {answer}")

#dropdown
# options = ["C++", "Java", "Python"]
# choice = st.selectbox("Select your favorite programming language:", options)
# st.write(f"You selected: {choice}")
