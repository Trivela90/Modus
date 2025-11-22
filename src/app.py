import os
import streamlit as st
from dotenv import load_dotenv
from pages.navigation import  get_nav_menu
from pathlib import Path
import json

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
    
    data = Path("data")  # diretório data/

    if 'user_data' not in st.session_state:
        st.session_state['user_data'] = json.loads((data / "model.json").read_text(encoding="utf-8"))
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = True
    st.session_state['user_data'] = json.loads((data / "model.json").read_text(encoding="utf-8"))
    get_nav_menu().run_menu()

if __name__ == "__main__":
    app()