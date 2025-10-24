import streamlit as st
import pandas as pd
import joblib

# Load model and expected feature columns
model = joblib.load("churn_model.pkl")
model_features = joblib.load("model_features.pkl")  # list of columns used during training

# Streamlit app setup
st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊", layout="centered")
st.title("📊 Customer Churn Prediction App")
st.write("Enter the customer details below to predict if they are likely to churn.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Has Partner", ["Yes", "No"])
dependents = st.selectbox("Has Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=12)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)

# Convert inputs into DataFrame
input_data = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone_service],
    "InternetService": [internet_service],
    "Contract": [contract],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})

# One-hot encode and align columns
input_encoded = pd.get_dummies(input_data)
input_encoded = input_encoded.reindex(columns=model_features, fill_value=0)

# Predict churn
if st.button("🔍 Predict Churn"):
    prediction = model.predict(input_encoded)[0]
    probability = model.predict_proba(input_encoded)[0][1]

    if prediction == 1:
        st.error(f"⚠️ This customer is likely to CHURN. (Probability: {probability:.2f})")
    else:
        st.success(f"✅ This customer is NOT likely to churn. (Probability: {probability:.2f})")

st.markdown("---")
st.caption("Built by Abhinay using Streamlit")