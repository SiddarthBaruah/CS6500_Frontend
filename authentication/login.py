import streamlit as st
from pages.base_class.page import GeneralPage
from utilities.digital_certificates.get_certificate import get_certificate
from utilities.digital_certificates.get_private_key import get_private_key
from streamlit_authenticator.views.authentication_view import Authenticate

class LoginPage(GeneralPage):
    def page_structure(self):
        authenticator: Authenticate = st.session_state["authenticator"]
        try:
            authenticator.login(key='login_form')
            if st.session_state["authentication_status"]:
                st.session_state["user_certificate"] = get_certificate(username=st.session_state['username'])
                st.session_state["user_private_key"] = get_private_key(username=st.session_state['username'])
                st.rerun()
        except Exception as e:
            st.error(e)