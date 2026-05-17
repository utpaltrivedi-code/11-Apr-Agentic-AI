import streamlit as st
import pandas as pd
from utils.db_setup import get_session, Ticket

def render_dashboard():
    st.title("📊 Dashboard Overview")
    session = get_session()
    tickets = session.query(Ticket).all()
    session.close()
    
    if not tickets:
        st.info("No tickets found. Run `python main.py` first.")
        return
        
    df = pd.DataFrame([{"ID": t.id, "Category": t.category, "Priority": t.priority, "Title": t.title, "Status": t.status} for t in tickets])
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Tickets", len(df))
    col2.metric("Critical", len(df[df["Priority"] == "Critical"]))
    col3.metric("Bugs", len(df[df["Category"] == "Bug"]))
    col4.metric("Features", len(df[df["Category"] == "Feature Request"]))
    
    st.dataframe(df, use_container_width=True)