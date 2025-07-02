import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('heart_disease_model.pkl')

st.title("💓 Heart Disease Prediction App")

# Create input fields
age = st.number_input('Age', 18, 100, 25)
sex = st.selectbox('Sex (1 = Male, 0 = Female)', [1, 0])
cp = st.selectbox('Chest Pain Type (0-3)', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure (mm Hg)', 80, 200, 120)
chol = st.number_input('Serum Cholesterol (mg/dl)', 100, 600, 200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)', [1, 0])
restecg = st.selectbox('Resting ECG (0-2)', [0, 1, 2])
thalach = st.number_input('Max Heart Rate Achieved', 60, 250, 150)
exang = st.selectbox('Exercise Induced Angina (1 = Yes, 0 = No)', [1, 0])
oldpeak = st.number_input('ST Depression Induced by Exercise', 0.0, 6.0, 1.0, step=0.1)
slope = st.selectbox('Slope of Peak Exercise ST Segment (0-2)', [0, 1, 2])
ca = st.selectbox('Major Vessels Colored by Fluoroscopy (0-4)', [0, 1, 2, 3, 4])
thal = st.selectbox('Thal (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)', [1, 2, 3])

# When button is clicked
if st.button('Predict'):
    input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg,
                                 thalach, exang, oldpeak, slope, ca, thal]],
                               columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                                        'restecg', 'thalach', 'exang', 'oldpeak',
                                        'slope', 'ca', 'thal'])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("❌ High chance of heart disease!")
    else:
        st.success("✅ Low chance of heart disease.")
