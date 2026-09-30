import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
        .stApp { background: #f5f7f3 !important; }
        [data-testid="stMainBlockContainer"] { max-width: 1120px; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
        .stApp { background: #f5f7f3 !important; }
        [data-testid="stMainBlockContainer"] { max-width: 1180px; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

        :root {
            --cv-ink: #1a2b3a;
            --cv-muted: #708078;
            --cv-paper: #f5f7f3;
            --cv-white: #ffffff;
            --cv-line: #e3e9e2;
            --cv-green: #286b57;
            --cv-green-dark: #205744;
            --cv-lime: #c7ef81;
            --cv-soft: #eaf3ed;
            --cv-gold: #f3c875;
        }

        #MainMenu, footer, header { visibility: hidden; }
        .stApp { color: var(--cv-ink); }
        [data-testid="stMainBlockContainer"] {
            padding: 1.6rem 2rem 2rem !important;
        }
        h1, h2, h3, h4 {
            color: var(--cv-ink) !important;
            font-family: 'Manrope', sans-serif !important;
            letter-spacing: -0.035em;
        }
        h1 { font-size: clamp(2rem, 4vw, 2.8rem) !important; line-height: 1.12 !important; }
        h2 { font-size: 1.45rem !important; line-height: 1.25 !important; }
        h3 { font-size: 1.1rem !important; }
        p, label, li, .stMarkdown, [data-testid="stCaptionContainer"] {
            font-family: 'DM Sans', sans-serif;
        }
        p { color: var(--cv-muted); }
        [data-testid="stDivider"] { border-color: var(--cv-line) !important; }

        .stButton > button {
            min-height: 2.7rem;
            padding: 0.55rem 1rem;
            border-radius: 0.7rem !important;
            border: 1px solid var(--cv-green) !important;
            background: var(--cv-green) !important;
            color: #fff !important;
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 700 !important;
            box-shadow: 0 2px 5px #1a49320f;
            transition: background .16s ease, transform .16s ease, box-shadow .16s ease;
        }
        .stButton > button:hover {
            background: var(--cv-green-dark) !important;
            border-color: var(--cv-green-dark) !important;
            transform: translateY(-1px);
            box-shadow: 0 5px 13px #1a49321c;
        }
        .stButton > button:focus { box-shadow: 0 0 0 3px #286b5730 !important; }
        .stButton > button[kind="secondary"] {
            background: #fff !important;
            color: var(--cv-green) !important;
            border-color: var(--cv-line) !important;
        }
        .stButton > button[kind="secondary"]:hover {
            background: var(--cv-soft) !important;
            border-color: #b8d2c2 !important;
        }
        .stButton > button[kind="tertiary"] {
            background: #f5f7f3 !important;
            color: #53645b !important;
            border-color: var(--cv-line) !important;
            box-shadow: none;
        }

        input, textarea, [data-baseweb="select"] > div {
            border-radius: 0.65rem !important;
        }
        [data-baseweb="input"] > div, [data-baseweb="textarea"] > div,
        [data-baseweb="select"] > div {
            border-color: #dbe3dc !important;
            background: #fff !important;
        }
        [data-baseweb="input"]:focus-within > div,
        [data-baseweb="textarea"]:focus-within > div,
        [data-baseweb="select"] > div:focus-within {
            border-color: var(--cv-green) !important;
            box-shadow: 0 0 0 2px #286b571c !important;
        }
        [data-testid="stFileUploader"], [data-testid="stCameraInput"],
        [data-testid="stAudioInput"] {
            background: #fff;
            border: 1px solid var(--cv-line);
            border-radius: 0.9rem;
            padding: 0.75rem;
        }
        [data-testid="stDataFrame"], [data-testid="stTable"] {
            border: 1px solid var(--cv-line);
            border-radius: 0.85rem;
            overflow: hidden;
            background: #fff;
        }
        [data-testid="stAlert"] { border-radius: 0.8rem; }
        [data-testid="stMetric"] {
            background: #fff;
            padding: 1rem 1.1rem;
            border: 1px solid var(--cv-line);
            border-radius: 0.9rem;
        }
        [data-testid="stDialog"] > div > div {
            border-radius: 1.1rem;
            border: 1px solid var(--cv-line);
        }
        [data-testid="stDialog"] h2 { color: var(--cv-ink) !important; }

        @media (max-width: 700px) {
            [data-testid="stMainBlockContainer"] { padding: 1rem 1rem 1.5rem !important; }
            h1 { font-size: 2rem !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
