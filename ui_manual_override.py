import streamlit as st
from utils.db_setup import get_session, Ticket

def render_manual_override():
    st.title("✍️ Manual Override")
    session = get_session()
    tickets = session.query(Ticket).all()
    if not tickets: return st.info("No tickets to review.")
    
    t_dict = {f"[{t.priority}] {t.title}": t for t in tickets}
    selected = st.selectbox("Select ticket", list(t_dict.keys()))
    t = t_dict[selected]
    
    with st.form("edit"):
        new_title = st.text_input("Title", t.title)
        new_status = st.selectbox("Status", ["open", "approved", "rejected"], index=0)
        if st.form_submit_button("Save"):
            t.title, t.status = new_title, new_status
            session.commit()
            st.success("Updated!")
    session.close()