import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

def initialize_session_state():


    #session states
    if "authentication_status" not in st.session_state:
        st.session_state["authentication_status"] = None
    if "user_certificate" not in st.session_state:
        st.session_state["user_certificate"]= None
    if "user_private_key" not in st.session_state:
        st.session_state["user_private_key"]= None
    if "authenticator" not in st.session_state:   
        with open('config.yaml') as file:
            st.session_state['config']= config = yaml.load(file, Loader=SafeLoader)
        st.session_state["authenticator"] = stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days']
        )
    if "prev" not in st.session_state:
        st.session_state["prev"]= None




