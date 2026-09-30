import streamlit as st


def _brand(size="normal"):
    st.markdown(
        f"""
        <div class="cv-brand cv-brand-{size}">
            <span class="cv-brand-mark">CV</span>
            <span class="cv-brand-name">ClassVision</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def header_home():
    st.markdown(
        """
        <style>
        .cv-brand { display:flex; align-items:center; gap:11px; color:#1a2b3a; }
        .cv-brand-mark {
            display:grid; place-items:center; width:42px; height:42px;
            border-radius:14px; background:#286b57; color:#c7ef81;
            font:800 14px 'Manrope',sans-serif; letter-spacing:-.04em;
        }
        .cv-brand-name { font:800 20px 'Manrope',sans-serif; letter-spacing:-.04em; }
        .cv-brand-large { justify-content:center; flex-direction:column; gap:14px; padding:12px 0 22px; }
        .cv-brand-large .cv-brand-mark { width:68px; height:68px; border-radius:22px; font-size:21px; }
        .cv-brand-large .cv-brand-name { font-size:33px; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    _brand("large")


def header_dashboard():
    st.markdown(
        """
        <style>
        .cv-brand { display:flex; align-items:center; gap:11px; color:#1a2b3a; }
        .cv-brand-mark {
            display:grid; place-items:center; width:42px; height:42px;
            border-radius:14px; background:#286b57; color:#c7ef81;
            font:800 14px 'Manrope',sans-serif; letter-spacing:-.04em;
        }
        .cv-brand-name { font:800 20px 'Manrope',sans-serif; letter-spacing:-.04em; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    _brand()
