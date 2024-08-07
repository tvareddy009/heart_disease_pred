import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.title('heart disease prediction')
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://wallpapercave.com/wp/wp2386870.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
pipe=pickle.load(open('lr.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
age = st.text_input('Give the age')
sex = st.text_input('Sex')
cp = st.text_input('CP')
trestbps = st.text_input('Trestbps')
chol = st.text_input('Chol')
fbs = st.text_input('FBS')
restecg = st.text_input('Restecg')
thalach = st.text_input('Thalach')
exang = st.text_input('Exang')
oldpeak = st.text_input('Oldpeak')
slope = st.text_input('Slope')
ca = st.text_input('CA')
thal = st.text_input('Thal')

def make_prediction():
    input = {
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    }
    query=pd.DataFrame(input)
    input=query.values
    prediction=pipe.predict(input)
    st.write(prediction)

if st.button('Make prediction'):
    make_prediction()