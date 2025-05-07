
import streamlit as st
from pages.base_class.page import GeneralPage
from utilities.digital_certificates.generate_certificate import generate_and_register_certificate
from streamlit_authenticator.views.authentication_view import Authenticate
from utilities.digital_certificates.get_all_users import get_all_users
import yaml

class RegisterUserPage(GeneralPage):
    def page_structure(self):
        authenticator: Authenticate = st.session_state["authenticator"]
        try:
            email_of_registered_user, \
            username_of_registered_user, \
            name_of_registered_user =  authenticator.register_user(captcha=False)
            if email_of_registered_user:
                st.success('User registered successfully')
                user_key, user_cert, transactionHash= generate_and_register_certificate(user_name=username_of_registered_user)
                st.write(transactionHash)
                with open('config.yaml', 'w', encoding='utf-8') as file:
                    yaml.dump(st.session_state['config'], file, default_flow_style=False)
                st.session_state["all_users"]= get_all_users()
        except Exception as e:
            st.error(e)
