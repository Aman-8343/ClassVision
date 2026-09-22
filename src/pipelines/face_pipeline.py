import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st
from src.database.db import get_all_students

# face Image -> face detector(dlib) -> shape predictor(sp) (Landmarks) -> resnet(facerecog)(embedding(128D)) -> SVC -> student id

@st.cache_resource  ## loads the model only once
def load_dlib_models():
    detector=dlib.get_frontal_face_detector()

    sp=dlib.shape_predictor(face_recognition_models.pose_predictor_model_location())

    facerec=dlib.face_recognition_model_v1(face_recognition_models.face_recognition_model_location())

    return detector,sp,facerec