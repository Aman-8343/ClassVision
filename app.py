import streamlit as st

def main():
    name=st.text_input("enter the name")
    st.header("TItle")
    if st.button('displaly the nane' ,type="primary", key='btn1'):
        print('hii ', name)
    st.button('display ', type='secondary',key='btn2')
    st.markdown("""
        <h1>dfld</h1>
    """,unsafe_allow_html=True)
main()