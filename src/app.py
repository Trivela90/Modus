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

    # pasta onde está o app.py -> src/
    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"             # src/data
    model_path = data_dir / "model.json"     # src/data/model.json

    # Carrega user_data só se ainda não estiver na sessão
    if "user_data" not in st.session_state:
        try:
            st.session_state["user_data"] = json.loads(
                model_path.read_text(encoding="utf-8")
            )
        except FileNotFoundError:
            st.warning(f"Arquivo não encontrado: {model_path}. Usando lista vazia.")
            st.session_state["user_data"] = []

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = True

    get_nav_menu().run_menu()

if __name__ == "__main__":
    app()