import os
import streamlit as st
from dotenv import load_dotenv
from pages.navigation import  get_nav_menu

load_dotenv()

def app():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = None
    get_nav_menu().run_menu()

if __name__ == "__main__":
    app()