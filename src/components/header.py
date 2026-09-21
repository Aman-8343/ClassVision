import streamlit as st

def header_home():
    logo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQT9DJverBiwBhROsiQsneJ4ch13XFESHIQRZVmIs_-w&s=10"
    st.markdown(f"""
            <div>
                <img src='{logo_url}', height=100px; />
            </div>

            """,unsafe_allow_html=True)