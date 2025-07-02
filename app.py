import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import pandas as pd
import joblib
import json  # For parsing Streamlit secrets

# ✅ Function to log data to Google Sheet with auto-header
def log_to_sheet(data):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # 🔐 Load credentials from Streamlit secrets
    creds_dict = json.loads(st.secrets["gcp_service_account"]["json"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

    client = gspread.authorize(creds)
    sheet = client.open("heart_user_data").sheet1  # ✅ Ensure this sheet exists and is shared

    # ✅ Add header row only once if the sheet is empty
    existing_data = sheet.get_all_values()
    if len(existing_data) == 0:
        headers = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                   'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'prediction']
        sheet.append_row(headers)

    # ✅ Add user data
    sheet.append_row(data)

# ✅ Load the trained model
model = joblib.load('heart_disease_model.pkl')

# ✅ Streamlit App Title
st.title("💓 Heart Disease Prediction App")

# ✅ Input Fields
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

# ✅ Predict Button
if st.button('Predict'):
    # Prepare input for model
    input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg,
                                 thalach, exang, oldpeak, slope, ca, thal]],
                               columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                                        'restecg', 'thalach', 'exang', 'oldpeak',
                                        'slope', 'ca', 'thal'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Show result
    if prediction == 1:
        st.error("❌ High chance of heart disease!")
    else:
        st.success("✅ Low chance of heart disease.")

    # ✅ Store in Google Sheet
    log_to_sheet([age, sex, cp, trestbps, chol, fbs, restecg,
                  thalach, exang, oldpeak, slope, ca, thal, int(prediction)])
