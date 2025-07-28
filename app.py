import streamlit as st
import numpy as np
import joblib

st.title("Telco Churn Prediction App")

model = joblib.load("churn_model.pkl")

st.header("📋 Customer Info")
st.markdown("Enter customer details to predict whether they are likely to churn.")

# inputs
tenure = st.slider("Tenure (in months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 1500.0)
gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen?", ["No", "Yes"])
partner = st.selectbox("Has a partner?", ["No", "Yes"])
dependents = st.selectbox("Has dependents?", ["No", "Yes"])
phone_service = st.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
device_protection = st.selectbox(
    "Device Protection", ["No", "Yes", "No internet service"]
)
tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
streaming_movies = st.selectbox(
    "Streaming Movies", ["No", "Yes", "No internet service"]
)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing?", ["No", "Yes"])
payment_method = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check",
    ],
)


def encode_input():
    return np.array(
        [
            [
                tenure,
                monthly,
                total,
                1 if gender == "Male" else 0,
                1 if senior == "Yes" else 0,
                1 if partner == "Yes" else 0,
                1 if dependents == "Yes" else 0,
                1 if phone_service == "Yes" else 0,
                1 if multiple_lines == "No phone service" else 0,
                1 if multiple_lines == "Yes" else 0,
                1 if internet_service == "Fiber optic" else 0,
                1 if internet_service == "No" else 0,
                1 if online_security == "No internet service" else 0,
                1 if online_security == "Yes" else 0,
                1 if online_backup == "No internet service" else 0,
                1 if online_backup == "Yes" else 0,
                1 if device_protection == "No internet service" else 0,
                1 if device_protection == "Yes" else 0,
                1 if tech_support == "No internet service" else 0,
                1 if tech_support == "Yes" else 0,
                1 if streaming_tv == "No internet service" else 0,
                1 if streaming_tv == "Yes" else 0,
                1 if streaming_movies == "No internet service" else 0,
                1 if streaming_movies == "Yes" else 0,
                1 if contract == "One year" else 0,
                1 if contract == "Two year" else 0,
                1 if paperless == "Yes" else 0,
                1 if payment_method == "Credit card (automatic)" else 0,
                1 if payment_method == "Electronic check" else 0,
                1 if payment_method == "Mailed check" else 0,
            ]
        ]
    )


if st.button("Predict Churn"):
    input_data = encode_input()
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Likely to Churn (probability = {prob:.2f})")
    else:
        st.success(f"✅ Likely to Stay (probability = {prob:.2f})")
