import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_background_dashboard
def home_screen():
    style_base_layout()
    style_background_dashboard()
    header_home()
    

    col1,col2=st.columns(2)

    with col1:
        if st.button('Teacher_Portal'):
            st.session_state['login_type']='teacher'

    with col2:
        if st.button('student_portal'):
            st.session_state['login_type']='student'