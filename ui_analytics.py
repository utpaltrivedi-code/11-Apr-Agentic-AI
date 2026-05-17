import streamlit as st
import pandas as pd
from utils.db_setup import get_session, Ticket

def render_analytics():
    st.title("📈 Analytics")
    session = get_session()
    tickets = session.query(Ticket).all()
    session.close()
    if not tickets: return st.warning("No data.")
    
    df = pd.DataFrame([{"Category": t.category, "Priority": t.priority} for t in tickets])
    c1, c2 = st.columns(2)
    with c1: st.bar_chart(df["Category"].value_counts())
    with c2: st.bar_chart(df["Priority"].value_counts())