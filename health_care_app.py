import streamlit as st
from utilities.initialization.state_initialization import initialize_session_state
from utilities.initialization.page_initialization import start_app

initialize_session_state()

main_canva: st._DeltaGenerator= st.empty()

start_app(main_canva)