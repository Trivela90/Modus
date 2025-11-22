import os
import streamlit as st
from dotenv import load_dotenv
from pages.navigation import  get_nav_menu

load_dotenv()

def app():
    st.markdown("""
        <style>
        [data-testid="stImage"] {
            background: transparent !important;
            padding: 0 !important;
            border-radius: 0 !important;
            box-shadow: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = True
    get_nav_menu().run_menu()

if __name__ == "__main__":
    app()