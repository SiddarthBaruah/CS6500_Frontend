import streamlit as st
from utilities.initialization.state_initialization import initialize_session_state
from utilities.initialization.page_initialization import start_app
from utilities.initialization.apply_global_style import apply_global_style

apply_global_style()
initialize_session_state()

main_canva: st._DeltaGenerator= st.empty()

start_app(main_canva)