import streamlit as st
from pages.base_class.page import GeneralPage
from streamlit_authenticator.views.authentication_view import Authenticate

class LogoutPage(GeneralPage):
    def page_structure(self):
        authenticator: Authenticate = st.session_state["authenticator"]
        if st.session_state["authentication_status"]:
            authenticator.logout()