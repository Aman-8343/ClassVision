import streamlit as st

def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #5867f2 !important;
            }
        </style>
    """, unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
        <style>
            #MainMenu,footer,header{
            visibility:hidden
            }
        </style>
    """, unsafe_allow_html=True)