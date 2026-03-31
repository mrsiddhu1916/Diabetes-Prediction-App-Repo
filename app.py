import os
import requests
import streamlit as st
from dotenv import load_dotenv
#load content into .env file to env variables

load_dotenv()

#enter yout API url

API_URL=os.getenv("API_URL")

#set page configurations

st.set_page_config(
    page_title="DIabetes Prediction App",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Prediction App")
st.write("Enter Patient details and click **predict**")

st.subheader("Patient Details")

col1,col2=st.columns(2)

with col1:
    Pregnancies=st.number_input("Pregnancies",0,10,2)
    Glucose=st.number_input("Glucose",0,400,120)
    BloodPressure=st.number_input("Blood Pressure",0,200,70)
    SkinThickness=st.number_input("Skin Thickness",0,100,25)

with col2:
    Insulin=st.number_input("Insulin",0,900,80)
    BMI=st.number_input("BMI",0.0,70.0,28.5)
    DiabetesPedigreeFunction=st.number_input("Diabetes Pedigree Function",0.0,3.0,0.45)
    Age=st.number_input("Age",1,100,35)
    
if st.button("🔍predict", use_container_width=True):
    input_data={
        "Pregnancies":Pregnancies,
        "Glucose":Glucose,
        "BloodPressure":BloodPressure,
        "SkinThickness":SkinThickness,
        "Insulin":Insulin,
        "BMI":BMI,
        "DiabetesPedigreeFunction":DiabetesPedigreeFunction,
        "Age":Age
    }

    response=requests.post(API_URL, json=input_data)
    response_dictionary=response.json()
    prediction=response_dictionary["prediction"]
    st.divider()

    if prediction==1:
        st.error("⚠️ Model Prediction: Diabetes")
        st.error("Sorry to say ! the model predicts that the patient has diabetes)")
        st.error("Please consult a healthcare professional for further evaluation and management.")
    else:
        st.success("✅ Model Prediction: No Diabetes")
        st.success("Great news! The model predicts that the patient does not have diabetes.")
        st.success("However, it's important to maintain a healthy lifestyle and consult a healthcare professional for regular check-ups.")
        