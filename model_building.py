# STEP-1
#Create a new Python file

import pandas as pd

# Load the dataset
data = pd.read_csv("heart.csv")

# Show first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# Show basic info
print("\nBasic Info:")
print(data.info())

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

#   STEP - 2
#Build and Train the Machine Learning Model

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Split features and target
X = data.drop('target', axis=1)  # Input columns
y = data['target']               # Output column

# Step 2: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Model training
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Step 4: Predict on test data
y_pred = model.predict(X_test)

# Step 5: Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)

#  STEP - 3
#Save the Trained Model

import joblib

# Save the model to a file
joblib.dump(model, 'heart_disease_model.pkl')
print("Model saved as heart_disease_model.pkl")
