import pandas as pd
import streamlit as st
import pickle

model = pickle.load(open("model.pkl","rb"))

st.title("Hart Attack Model to Predict [Yes or Not]")
st.header("Enter Your Medical Report to Predict Yes or Not")

age = st.slider("Enter Your Age ",0,100,18)
gender = st.selectbox("Enter Your Gender Male[1], Female[0]",[0,1])
hart_rate = st.number_input("Enter Your Hart Rate")
systolic_blood_pressure = st.number_input("Enter Your Systolic Blood Pressure")
diastolic_blood_pressuret = st.number_input("Enter Your Diastolic Blood Pressuret")
blood_suger = st.number_input("Enter Your Blood Suger")
ckmb = st.number_input("Enter Your CK-MB")
troponin = st.number_input("Enter Your Troponin")

data = [[age,gender,hart_rate,systolic_blood_pressure,diastolic_blood_pressuret,blood_suger,ckmb,troponin]]

if st.button("Prediction"):
    pediction = model.predict(data)
    st.success(f"This is your Right now status {pediction}")

