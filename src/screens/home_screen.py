import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():


    header_home()
    style_background_home()
    style_base_layout()


    st.markdown(
        """
        <div class="cv-home-intro">
            <span class="cv-eyebrow">✦ &nbsp; SMARTER CLASSROOMS START HERE</span>
            <h1>More teaching.<br><span>Less roll call.</span></h1>
            <p>Simple, secure attendance for every classroom. Check in with face or voice, and keep every class organized in one place.</p>
        </div>
        <style>
        .cv-home-intro { text-align:center; max-width:700px; margin:0 auto 2rem; }
        .cv-eyebrow { display:inline-block; padding:7px 12px; background:#e8f2e9; color:#286b57; border-radius:30px; font:700 11px 'DM Sans',sans-serif; letter-spacing:.05em; }
        .cv-home-intro h1 { margin:17px 0 10px; font-size:clamp(2.5rem,5vw,3.7rem)!important; }
        .cv-home-intro h1 span { color:#286b57; }
        .cv-home-intro p { max-width:530px; margin:0 auto; line-height:1.7; }
        [data-testid="stVerticalBlockBorderWrapper"] { background:#fff; border-color:#e3e9e2; border-radius:16px; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            st.header("I'm a student")
            st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
            st.caption("Check in and keep track of your attendance.")
            if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
                st.session_state['login_type']='student'
                st.rerun()

    with col2:
        with st.container(border=True):
            st.header("I'm a teacher")
            st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
            st.caption("Manage classes and take attendance in moments.")
            if st.button('Teacher Portal', type='secondary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
                st.session_state['login_type']='teacher'
                st.rerun()


    st.divider()
    footer_home()
