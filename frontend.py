import streamlit as st
from backend import call_llm

st.title("Prompt Playground")

prompt_type = st.selectbox(
    "Select Prompt Type",
    ["Zero-shot", "One-shot", "Few-shot"]
)

user_input = st.text_area("Enter your task")

if st.button("Generate"):
    if user_input.strip():
        response = call_llm(user_input, prompt_type)
        st.write(response)
    else:
        st.warning("Please enter some text")
