import streamlit as st

from home import show_home
from dashbord import show_dashboard

st.set_page_config(
    page_title="AI Network IDS",
    page_icon="🛡️",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "dashboard"

if st.session_state.page == "home":
    show_home()

elif st.session_state.page == "dashboard":
    show_dashboard()