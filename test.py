import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


loan_approv_loaded_model = pickle.load(open("loan_prediction.sav", "rb"))

with st.sidebar:
    predictions = ['Loan Approval']
    selected = option_menu("Multiple Prediction", predictions, default_index=0)

    
if(selected == 'Loan Approval'):
    def prediction(input):
        input_as_numpy_array = np.asarray(input)
        input_reshaped = input_as_numpy_array.reshape(1,-1)
        prediction = loan_approv_loaded_model.predict(input_reshaped)
        if (prediction[0] == 0):
            return 'The loan is not approved'
        else:
            return 'The loan is approved'
        
    def main():
        st.title("Loan Prediction Model")
        
        col1, col2 = st.columns(2)
        
        with col1:
            Gender = st.text_input("Gender (0: Male, 1: Female)", "0")
            Married = st.text_input("Married (0: No, 1: Yes)", "1")
            Dependents = st.text_input("Dependents (0, 1, 2, or 3+)", "1")
            Education = st.text_input("Education (0: Graduate, 1: Not Graduate)", "1")
            Self_Employed = st.text_input("Self_Employed (0: No, 1: Yes)", "0")
            ApplicantIncome = st.text_input("ApplicantIncome", "4583")
        with col2 : 
            CoapplicantIncome = st.text_input("CoapplicantIncome", "1500.0")
            LoanAmount = st.text_input("LoanAmount", "128.0")
            Loan_Amount_Term = st.text_input("Loan_Amount_Term", "360.0")
            Credit_History = st.text_input("Credit_History (0 or 1)", "1.0")
            Property_Area = st.text_input("Property_Area (Rural : 0,Semiurban : 1,Urban : 2)", "0")

        if st.button("Predict"):
            try:
                input_data = [
                    float(Gender),
                    float(Married),
                    float(Dependents),
                    float(Education),
                    float(Self_Employed),
                    float(ApplicantIncome),
                    float(CoapplicantIncome),
                    float(LoanAmount),
                    float(Loan_Amount_Term),
                    float(Credit_History),
                    float(Property_Area)
                ]
                result = prediction(input_data)
                st.success(result)
            
            except ValueError:
                st.error("Please enter valid numerical values for all inputs.")

    if __name__ == '__main__':
        main()