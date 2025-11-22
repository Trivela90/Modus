import streamlit as st
from datetime import datetime  # <- you can remove this if unused

class Nav_Menu:
    def __init__(self):
        self.menu_options = self._init_menu_options()
        self.pages = self._init_pages(self.menu_options)

    def _init_menu_options(self):
        menu_options = {}
        # Análise
        menu_options['chat'] = st.Page(
            "pages/page_chatbot.py",
            title="Chatbot",
            icon=":material/chat:",
            default=True
        )
        menu_options['dashboard'] = st.Page(
            "pages/page_dashboard.py",
            title="Dashboard",
            icon=":material/bar_chart_4_bars:"
        )
        return menu_options

    def _init_pages(self, page):
        pages = {
            "Modus": [page["chat"], page["dashboard"]],
        }
        return pages

    def run_menu(self):
        if not st.session_state['logged_in']:
            menu_pages = {"Auth": [st.Page("pages/page_auth.py", title="Logout", icon=":material/logout:", default=True)]}
            pg = st.navigation(menu_pages, position="sidebar",expanded=False)
        else:
            pg = st.navigation(self.pages, position="sidebar")
            if st.sidebar.button("Logout", icon=":material/logout:"):
                st.session_state["logged_in"] = False
                st.rerun()
        pg.run()

def get_nav_menu():
    """Streamlit-safe singleton: one instance per session, across reruns."""
    if 'nav_menu_singleton' not in st.session_state:
        st.session_state['nav_menu_singleton'] = Nav_Menu()
    return st.session_state['nav_menu_singleton']
