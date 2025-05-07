import streamlit as st

def apply_global_style():
    st.markdown(
        """
        <style>
        /* Global Styles */
        .main {
            background-color: #0e1117;
            color: #ffffff;
        }
        
        /* Card Styles */
        .card {
            background-color: #1a1b1e;
            border-radius: 15px;
            box-shadow: 0 8px 32px 0 rgba(0, 255, 0, 0.1);
            padding: 25px;
            transition: all 0.3s ease;
            margin-bottom: 25px;
            border: 1px solid rgba(0, 255, 0, 0.1);
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px 0 rgba(0, 255, 0, 0.2);
        }
        
        /* Button Styles */
        .stButton > button {
            width: 100%;
            background-color: #1a1b1e;
            color: #00ff00 !important;
            border: 2px solid rgba(0, 255, 0, 0.2);
            padding: 3px;
            border-radius: 10px;
            margin: 2px 0;
            transition: all 0.3s ease;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .stButton > button:hover {
            background-color: rgba(0, 255, 0, 0.1);
            border-color: #00ff00;
            box-shadow: 0 0 20px rgba(0, 255, 0, 0.2);
            transform: scale(1.02);
        }
        
        .stButton > button:active {
            transform: scale(0.98);
        }
        
        /* Status Message Styles */
        .status-message {
            padding: 15px;
            border-radius: 10px;
            margin: 15px 0;
            background-color: #1a1b1e;
            border: 1px solid rgba(0, 255, 0, 0.2);
            backdrop-filter: blur(10px);
        }
        
        /* Title Styles */
        h1 {
            color: #00ff00;
            text-align: center;
            margin-bottom: 30px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        /* Last Command Card Styles */
        .last-command-card {
            background: linear-gradient(145deg, #1a1b1e, #0e1117);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 30px;
            border: 1px solid rgba(0, 255, 0, 0.2);
        }
        
        .last-command-title {
            color: #00ff00;
            font-size: 1.2em;
            margin-bottom: 10px;
            font-weight: 500;
        }
        
        .last-command-value {
            color: #ffffff;
            font-size: 1.1em;
            opacity: 0.9;
        }

        /* Container Styles */
        .stContainer {
            background-color: #1a1b1e;
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            border: 1px solid rgba(0, 255, 0, 0.1);
        }

        /* Sidebar Styles */
        .sidebar .sidebar-content {
            background-color: #1a1b1e;
        }

        /* Text Input Styles */
        .stTextInput > div > div {
            background-color: #1a1b1e;
            color: #ffffff;
            border-radius: 10px;
            border: 1px solid rgba(0, 255, 0, 0.2);
        }

        .stTextInput > div > div:hover {
            border-color: #00ff00;
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.1);
        }

        /* Selectbox Styles */
        .stSelectbox > div > div {
            background-color: #1a1b1e;
            color: #ffffff;
            border-radius: 10px;
            border: 1px solid rgba(0, 255, 0, 0.2);
        }

        .stSelectbox > div > div:hover {
            border-color: #00ff00;
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )