import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to make predictions
def predict_disease(features):
    features_array = np.array([features])
    prediction = model.predict(features_array)
    return prediction[0]

# Streamlit app layout
st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")

st.markdown("""
    <style>
        /* General Styles */
        body {
             background: linear-gradient(135deg, #a1c4fd, #c2e9fb);
             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        h1 {
            text-align: center;
            color: #D32F2F;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        label {
            font-weight: 600;
            margin-top: 1rem;
            display: block;
            color: #333333;
        }
         select, .stNumberInput, .stSelectbox {
            width: 100% !important;
            padding: 0.5rem;
            margin-top: 5px;
            border-radius: 8px;
            border: 1.5px solid #ddd;
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }
         

        # input:focus, select:focus {
        #     border-color: #D32F2F !important;
        #     outline: none !important;
        #     box-shadow: 0 0 8px 0 #D32F2F70;
        # }
        button {
            background-color: #D32F2F;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 1.1rem;
            border-radius: 10px;
            cursor: pointer;
            width: 100%;
            margin-top: 1.5rem;
            transition: background-color 0.3s ease;
            font-weight: 700;
        }
        button:hover {
            background-color: #B71C1C;
        }
        .result {
            margin-top: 1.5rem;
            padding: 1rem;
            border-radius: 12px;
            font-weight: 700;
            font-size: 1.2rem;
            text-align: center;
        }
        .success {
            background-color: #C8E6C9;
            color: #2E7D32;
        }
        .error {
            background-color: #FFCDD2;
            color: #C62828;
        }
        /* Responsive */
        @media (max-width: 280px) {
            .main {
                padding: 1rem 1.5rem 2rem 1.5rem;
                margin: 20px 10px;
            }
            h1 {
                font-size: 1.8rem;
            }
            button {
                font-size: 1rem;
            }
        }
        
        /* Animation */
  
        
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown("<h1>❤️ Heart Disease Prediction ❤️</h1>", unsafe_allow_html=True)
st.write("Please enter your health details below:")

# Input fields arranged responsively
age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox(
    "Chest Pain Type (cp)", options=[0,1,2,3],
    format_func=lambda x: {0:"Typical Angina",1:"Atypical Angina",2:"Non-anginal Pain",3:"Asymptomatic"}[x]
)
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=0, value=120, step=1)
chol = st.number_input("Serum Cholesterol (chol)", min_value=0, value=200, step=1)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0,1], format_func=lambda x: "False" if x==0 else "True")
restecg = st.selectbox(
    "Resting ECG results (restecg)", options=[0,1,2],
    format_func=lambda x: {0:"Normal",1:"ST-T Wave abnormality",2:"Left ventricular hypertrophy"}[x]
)
thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=0, value=150, step=1)
exang = st.selectbox("Exercise Induced Angina (exang)", options=[0,1], format_func=lambda x: "No" if x==0 else "Yes")
oldpeak = st.number_input("ST Depression Induced (oldpeak)", min_value=0.0, max_value=10.0, format="%.1f", value=1.0, step=0.1)
slope = st.selectbox(
    "Slope of Peak Exercise ST segment (slope)", options=[0,1,2],
    format_func=lambda x: {0:"Upsloping",1:"Flat",2:"Downsloping"}[x]
)
ca = st.selectbox("Number of Major Vessels Colored (ca)", options=[0,1,2,3,4])
thal = st.selectbox(
    "Thalassemia (thal)", options=[1,2,3],
    format_func=lambda x: {1:"Normal",2:"Fixed Defect",3:"Reversible Defect"}[x]
)

if st.button("Predict"):
    feature_list = [
        age, sex, cp, trestbps, chol, fbs, restecg, thalach,
        exang, oldpeak, slope, ca, thal
    ]
    try:
        result = predict_disease(feature_list)
        if result == 1:
            st.markdown('<div class="result success">The model predicts that you have heart disease.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result success">The model predicts that you do NOT have heart disease.</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="result error">Error: {str(e)}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)




 