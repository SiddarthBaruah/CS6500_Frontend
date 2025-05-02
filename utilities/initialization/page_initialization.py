import streamlit as st
from authentication.log_out import LogoutPage
from authentication.login import LoginPage
from authentication.register import RegisterUserPage
from pages.home_page import HomePage
from streamlit_option_menu import option_menu

def start_app(current_page: st._DeltaGenerator):
    with st.sidebar:
        if st.session_state["authentication_status"]:
            page_selected =option_menu(
                "Subpages",                              # menu title
                [
                    "HomePage",
                    "LogOut"
                ],
                icons=[                                # pick any from Bootstrap Icons
                    "house",
                    "Logout"
                ],
                menu_icon="list",                      # the title icon
                default_index=0,
                orientation="vertical",
                styles={                               # fully control font-size, spacing, colors
                    "container": {"padding": "0!important"},
                    "icon": {"font-size": "20px"},     
                    "nav-link": {
                        "font-size": "18px",           # ← bump up text here
                        "text-align": "left",
                        "padding": "8px 16px",
                    },
                    "nav-link-selected": {
                        "background-color": "#0f4c75",
                        "color": "white",
                    }
                }
            )
        else:
            page_selected =option_menu(
                "Subpages",                              # menu title
                [
                    "LogIn", "Register"
                ],
                icons=[                                # pick any from Bootstrap Icons
                    "Person", "App Registration"
                ],
                menu_icon="list",                      # the title icon
                default_index=0,
                orientation="vertical",
                styles={                               # fully control font-size, spacing, colors
                    "container": {"padding": "0!important"},
                    "icon": {"font-size": "20px"},     
                    "nav-link": {
                        "font-size": "18px",           # ← bump up text here
                        "text-align": "left",
                        "padding": "8px 16px",
                    },
                    "nav-link-selected": {
                        "background-color": "#0f4c75",
                        "color": "white",
                    }
                }
            )
    
    if st.session_state["prev"]!= page_selected:
            st.session_state["prev"]= page_selected
            current_page.empty()
            st.rerun() 

    st.session_state["current_page"]= page_selected
    if page_selected == "HomePage":
        homepage= HomePage(name="HomePage")        
        with current_page.container():
            homepage.render()
    elif page_selected == "LogOut":
        logout= LogoutPage(name="LogOut")
        with current_page.container():
            logout.render()
    elif page_selected == "LogIn":
        LogIn= LoginPage(name="LogIn")
        with current_page.container():
            LogIn.render()
    elif page_selected == "Register":
        register = RegisterUserPage(name="Register")
        with current_page.container():
            register.render()






