import os
from dotenv import load_dotenv
from pages.navigation import  get_nav_menu
load_dotenv()

def app():
    get_nav_menu().run_menu()
    
if __name__ == "__main__":
    app()