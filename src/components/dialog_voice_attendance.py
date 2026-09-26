import streamlit as st

def voice_attendance_dialog(selected_subject_id):
    st.write('Record audio of students saying I am present. Then AI will recognize the students')


    audio_data = None

    audio_data = st.audio_input("Record classroom audio")