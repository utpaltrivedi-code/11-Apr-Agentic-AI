import streamlit as st
from ui.dashboard import render_dashboard
from ui.analytics import render_analytics
from ui.manual_override import render_manual_override
from ui.configuration import render_configuration

st.set_page_config(page_title="TaskFlow Pro AI Feedback", layout="wide")

def main():
    st.sidebar.title("🤖 TaskFlow Pro AI")
    page = st.sidebar.radio("Navigation", ["Dashboard Overview", "Analytics & Metrics", "Manual Override", "Configuration Panel"])
    
    if page == "Dashboard Overview": render_dashboard()
    elif page == "Analytics & Metrics": render_analytics()
    elif page == "Manual Override": render_manual_override()
    elif page == "Configuration Panel": render_configuration()

if __name__ == "__main__": main()