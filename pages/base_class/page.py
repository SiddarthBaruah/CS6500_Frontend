import streamlit as st

class GeneralPage:
    def __init__(self,name):
        self.name = name
    
    def page_structure(self):
        raise NotImplementedError
    
    def render(self):
        if st.session_state["current_page"]== self.name:
            st.title(self.name)
            self.page_structure()