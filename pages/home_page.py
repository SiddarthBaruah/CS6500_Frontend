import streamlit as st
from pages.base_class.page import GeneralPage
from pages.assets.certificate import show_certificate
from cryptography import x509

class HomePage(GeneralPage):
    def page_structure(self):
        self.certificate :x509.Certificate= st.session_state["user_certificate"]
        show_certificate(self.certificate)
        st.write(st.session_state["user_private_key"])
        innn=  st.chat_input()
        if innn:
            st.write(innn)