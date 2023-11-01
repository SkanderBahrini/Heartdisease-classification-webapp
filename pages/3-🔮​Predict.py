import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(

    page_title='Prediction ',
    page_icon='🔮'
   
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
    '<h1 style="text-align: center;"> 🔮Predict Heart Diseases</h1>',
    unsafe_allow_html=True
)

st.sidebar.success("Let's predict")
st.header('Does the patient have heart disease? :heart:')

st.subheader('Upload your model:')

file = st.file_uploader('Upload file here', type=['joblib'])

if file is not None:
   
   st.success('File uploaded successfully !')



st.subheader('Patient Age:')
Age = st.slider('Select patient Age:', 1, 100)

st.subheader('Patient Sex')
Sex = st.radio('Select patient sex:', options=['Male', 'Female'])
Sex = 'M' if Sex == 'Male' else 'F'

st.subheader('Patient Chest Pain Type')
ChestPainType = st.radio('Select Chest Pain Type:', options=[
                         'TA', 'ATA', 'NAP', 'ASY'])

st.subheader('Patient Resting Blood Pressure')
RestingBP = st.slider('Select Resting blood pressure [mm Hg]:', 100, 200)

st.subheader('Patient Cholesterol')
Cholesterol = st.slider('Select Cholesterol [mm/dl]:', 50, 500)

st.subheader('Patient Fasting Blood Sugar [mg/dl]')
FastingBS = st.radio('Select fasting blood sugar:', options=[
                     'Greater than 120mg/dl', 'Less than 120 mg/dl'])
FastingBS = 1 if FastingBS == 'Greater than 120mg/dl' else 0

st.header('Patient Resting Electrocardiogram Result')
RestingECG = st.radio('Select patient resting electrocardiogram:', options=[
                      'Normal', 'ST', 'LVH'])

st.header('Patient Maximum Heart Rate')
MaxHR = st.slider('Select patient maximum heart rate:', 60, 202)

st.header('Does the patient suffer from exercise angina?')
ExerciseAngina = st.radio('Select:', options=['Yes', 'No'])
ExerciseAngina = 'Y' if ExerciseAngina == 'Yes' else 'N'

st.subheader('Select patient Oldpeak')
Oldpeak = st.slider('Select patient old peak', 1.0, 5.0, step=0.1)

st.subheader('Select patient ST_Slope')
ST_Slope = st.radio('Select option', options=['Up', 'Flat', 'Down'])

columns = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol',
           'FastingBS', 'RestingECG', 'MaxHR', 'ExerciceAngina', 'Oldpeak', 'ST_Slope']




def input():
    data = {
        'Age': [Age],
        'Sex': [Sex],
        'ChestPainType': [ChestPainType],
        'RestingBP': [RestingBP],
        'Cholesterol': [Cholesterol],
        'FastingBS': [FastingBS],
        'RestingECG': [RestingECG],
        'MaxHR': [MaxHR],
        'ExerciseAngina': [ExerciseAngina],
        'Oldpeak': [Oldpeak],
        'ST_Slope': [ST_Slope]
    }

  
    df = pd.DataFrame(data=data, index=[0])
    return df

user_input = input()

df = pd.read_csv('heart.csv')

df = df.drop(columns=['HeartDisease'])

df = pd.concat([user_input, df], axis=0)


encode = ['Sex', 'ChestPainType','RestingECG','ExerciseAngina','ST_Slope']

for col in encode:

    dummy = pd.get_dummies(df[col] , prefix=col)

    df = pd.concat([df, dummy], axis=1)

    del df[col]

df = df[:1]




if st.button('Predict'):
  
  model = joblib.load(file)
  pred = model.predict(df)
  if pred == 1:
     
     st.error('Patient suffer from heart diseases')
  else :
     
     st.success('Patient is healthy ')










