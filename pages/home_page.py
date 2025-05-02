import streamlit as st
from pages.base_class.page import GeneralPage

class HomePage(GeneralPage):
    def page_structure(self):
        st.write(st.session_state["user_certificate"])
        st.write(st.session_state["user_private_key"])
        innn=  st.chat_input()
        if innn:
            st.write(innn)