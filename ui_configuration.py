import streamlit as st
def render_configuration():
    st.title("⚙️ Configuration Panel")
    st.slider("Confidence Threshold", 0.0, 1.0, 0.75)
    st.selectbox("LLM Backend", ["gpt-4o-mini", "gemini-2.5-pro", "llama3 (local)"])
    if st.button("Save"): st.success("Saved for next run!")