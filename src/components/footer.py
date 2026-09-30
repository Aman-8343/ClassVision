import streamlit as st


def _footer():
    st.markdown(
        """
        <div class="cv-footer"><span>Made for focused classrooms</span><span>CLASSVISION &nbsp;·&nbsp; ATTENDANCE, SIMPLIFIED</span></div>
        <style>
        .cv-footer { margin-top:2.25rem; padding:1rem .25rem 0; border-top:1px solid #e3e9e2; display:flex; justify-content:space-between; gap:1rem; color:#829087; font:11px 'DM Sans',sans-serif; }
        @media(max-width:600px){.cv-footer{flex-direction:column;align-items:center;}}
        </style>
        """,
        unsafe_allow_html=True,
    )


def footer_home():
    _footer()


def footer_dashboard():
    _footer()
