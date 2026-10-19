
import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    /* Retro-inspired tourism dashboard */

    :root {
        --cream: #FAF1D5;
        --paper: #FFF9E9;
        --orange: #F4511E;
        --green: #35833B;
        --blue: #328CB9;
        --yellow: #F5B83D;
        --red: #E51D2A;
        --text: #42392F;
        --border: #E8D7AF;
    }

    /* App background */
    .stApp,
    [data-testid="stAppViewContainer"] {
        background-color: var(--cream);
        color: var(--text);
    }

    /* Main content spacing */
    .block-container {
        max-width: 1300px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #F6E9C8;
        border-right: 1px solid var(--border);
    }

    /* Headings */
    h1, h2, h3 {
        font-family: 'Arial', sans-serif;
        letter-spacing: -0.035em;
    }

    h1 {
        color: var(--orange) !important;
        font-size: clamp(2.2rem, 4vw, 3.6rem) !important;
        font-weight: 800 !important;
    }

    h2 {
        color: var(--green) !important;
        font-weight: 750 !important;
    }

    h3 {
        color: var(--orange) !important;
        font-weight: 700 !important;
    }

    /* Body text */
    p, li, label {
        color: var(--text);
    }

    /* Primary buttons */
    .stButton > button[kind="primary"] {
        background-color: var(--orange);
        color: white;
        border: 1px solid var(--orange);
        border-radius: 5px;
        font-weight: 700;
        padding: 0.55rem 1.4rem;
    }

    .stButton > button[kind="primary"]:hover {
        background-color: #D94314;
        border-color: #D94314;
        color: white;
    }

    /* Secondary buttons */
    .stButton > button[kind="secondary"] {
        background-color: var(--paper);
        border: 1px solid var(--orange);
        color: var(--orange);
        border-radius: 5px;
        font-weight: 650;
    }

    .stButton > button[kind="secondary"]:hover {
        background-color: #FCE4C8;
        border-color: var(--orange);
        color: var(--orange);
    }

    /* Tables */
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border);
        border-radius: 6px;
        overflow: hidden;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background-color: var(--paper);
        padding: 1rem;
        border: 1px solid var(--border);
        border-radius: 6px;
    }

    [data-testid="stMetricValue"] {
        color: var(--green);
        font-weight: 750;
    }

    /* Dividers */
    hr {
        border-color: var(--orange);
        opacity: 0.35;
    }

    /* Content containers */
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        border-color: var(--border);
    }

    /* Input fields */
    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input {
        background-color: var(--paper);
        color: var(--text);
        border-radius: 5px;
    }

    /* Sliders */
    [data-testid="stSlider"] {
        accent-color: var(--orange);
    }

    /* Links */
    a {
        color: var(--orange);
    }

    a:hover {
        color: var(--green);
    }

    /* Hide broken navigation icon text */
    [data-testid="stSidebar"] [data-testid="stSidebarNav"] .material-symbols-rounded {
        display: none !important;
    }

    /* Hide sidebar navigation icon elements */
    [data-testid="stSidebarNav"] [data-testid="stIconMaterial"] {
        display: none !important;
    }

    /* Hide the sidebar collapse control's broken icon */
    [data-testid="stSidebarCollapseButton"] .material-symbols-rounded,
    [data-testid="stSidebarCollapseButton"] [data-testid="stIconMaterial"] {
        display: none !important;
    }

    </style>
    """, unsafe_allow_html=True)
