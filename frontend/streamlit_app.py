import streamlit as st
import cv2

st.title("AI Virtual Assistant")
run = st.checkbox('Run Camera')

if run:
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        st.image(frame, channels="BGR")
    cap.release()