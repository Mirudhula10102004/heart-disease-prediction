# 💓 Heart Disease Prediction App

This is a Machine Learning web app that predicts the likelihood of heart disease based on user input.

## 💻 Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

## 🔧 Features
- Logistic Regression Model trained on the UCI Heart Disease dataset
- User input through Streamlit UI
- Real-time prediction
- Deployed using Streamlit Community Cloud

## 🚀 How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py

## Google Sheets Integration Setup

This app logs user inputs to a Google Sheet using the Google Sheets API.

### Setup Steps:

1. Create a Google Cloud project.
2. Enable **Google Sheets API** and **Google Drive API**.
3. Create credentials and download the `credentials.json` file.
4. Place the `credentials.json` file in the project root folder.
5. Share your Google Sheet with the client email in your `credentials.json` (service account email).

---

**Important:**  
Do NOT upload your `credentials.json` file to GitHub for security reasons.
