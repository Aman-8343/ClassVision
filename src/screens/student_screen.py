import streamlit as st

from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np

from src.pipelines.face_pipeline import predict_attendance
from src.database.db import get_all_students

def student_screen():
    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header('Login using FaceID', text_alignment='center')
    st.space()
    st.space()

    photo_source=st.camera_input("Position your face in the center")
    if photo_source:
        img=np.array(Image.open(photo_source))
        with st.spinner("Scanning Image..."):
            detected,all_ids,num_faces=predict_attendance()

            if num_faces==0:
                st.warning('NO Face Found')
            elif num_faces>1:
                st.warning("Multiple face Found")
            else:
                if detected:
                    student_id=list(detected.keys())[0]
                    all_students=get_all_students()
                    student=next((s for s in all_students if s['student_id']==student_id), None)

                    if student:
                        st.session_state.is_logged_in=True
                        st.session_state.user_role='student'
                        st.session_state.student_data=student
                        st.toast(f"Welcome Back {student['name']}")
                        time.sleep(1)
                        st.rerun()
                else:
                    continue


    footer_dashboard()