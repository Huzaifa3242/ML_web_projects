import streamlit as st
import pandas as pd
import joblib

# Load the model using joblib
model = joblib.load('pipeline_model.pkl')
st.title("Loan Predictor System")

st.markdown("""
Enter your details below to check your loan eligibility.
""")

# User input form
with st.form("Loan Prediction Form"):
    gender = st.selectbox("Gender", ['Male', 'Female'])
    married = st.selectbox("Married", ['Yes', 'No'])
    dependents = st.selectbox("Dependents", ['0', '1', '2', '3+'])
    education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
    self_employed = st.selectbox("Self Employed", ['Yes', 'No'])
    applicant_income = st.number_input("Applicant Income", min_value=0,step=1)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0,step=1)
    loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0,step=1)
    loan_term = st.number_input("Loan Amount Term (in days)", value=360,step=1)
    credit_history = st.selectbox("Credit History", [1.0, 0.0])
    property_area = st.selectbox("Property Area", ['Urban', 'Semiurban', 'Rural'])

    # Submit button
    submitted = st.form_submit_button("Predict Loan Approval")

    if submitted:
        # Create a DataFrame with user input
        user_input = pd.DataFrame([{
            'Gender': gender,
            'Married': married,
            'Dependents': dependents,
            'Education': education,
            'Self_Employed': self_employed,
            'ApplicantIncome': applicant_income,
            'CoapplicantIncome': coapplicant_income,
            'LoanAmount': loan_amount,
            'Loan_Amount_Term': loan_term,
            'Credit_History': credit_history,
            'Property_Area': property_area
        }])

        # Show the input data
        st.subheader("User Input Data")
        st.write(user_input)

        # Make prediction
        prediction = model.predict(user_input)

        # Show result
        st.subheader("Prediction Result")
        if prediction[0] == 1:
            st.success("Loan Approved ✅")
        else:
            st.error("Loan Rejected ❌")
