# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 15:37:56 2025

@author: HONNAPPA M S
"""
import pickle
import streamlit as st
import numpy as np

# load the saved model

load_model=pickle.load(open('C:/Users/HONNAPPA M S/Desktop/Loan Status Prediction/trained_model1.sav','rb'))

# create function for prediction
def prediction_function(input):
    
    # chaning the input_data  to numpy array
    input_data_asarray=np.asarray(input)

   # reshape the array as we are predictive for one instance
    input_data_reshape=input_data_asarray.reshape(1,-1)

    predict=load_model.predict(input_data_reshape)
    print(predict)

    if predict[0]==0:
        return 'Not Approval'
    else:
        return 'Loan Approval'

def main():
    
    # creating title
    st.title('Loan Status Prediction Using ML')
    
    
   # loan_dataset.replace({'Gender':{'Male':0,'Female':1}},inplace=True)
#loan_dataset.replace({'Education':{'Graduate':0,'Not Graduate':1}},inplace=True)
#loan_dataset.replace({'Property_Area':{'Semiurban':0,'Urban':1,'Rural':2}},inplace=True)
#loan_dataset.replace({'Married':{'Yes':0,'No':1}},inplace=True)
#loan_dataset.replace({'Self_Employed':{'No':0,'Yes':1}},inplace=True)


#Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
      # 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       #'Loan_Amount_Term', 'Credit_History', 'Property_Area'],
    
    
    #getting the input from user
    
    col1,col2=st.columns(2)
    with col1:
        Gender=st.text_input('If you are Male Please Enter "1" OtherWise "0"')
    with col2:
        
        Married=st.text_input('If you are Married Enter Please Enter "0",Otherwise "1"')
        
    with col1:
        Dependents=st.text_input('If you are Dependent Please Enter "1" Otherwise "0"')
    with col2:
        Education=st.text_input('If you are Graduate Please Enter "0" Otherwise "1"')
    with col1:
        Self_Employed=st.text_input('If you are Self_Employed Please Enter "1" Otherwise "0"')
    with col2:
        ApplicantIncome=st.text_input('Enter Youre Income')
    with col1:
        CoapplicantIncome=st.text_input('Enter the Coapplicant Income')
    with col2:
        LoanAmount=st.text_input('Enter the Loan Amount')
    with col1:
        Loan_Amount_Term=st.text_input('Enter the Loan Amount Term')
    with col2:
        Credit_History=st.text_input('Enter the Credit History')
    with col1:
        Property_Area=st.text_input('If you are in Semiurban Enter "0",Urban Enter "1",Otherwise "2" ')
        
    
    # code for prediction
    diagnosis=''
    
    # create the button for prediction
    if st.button('Loan Status Result'):
        diagnosis=prediction_function([Gender, Married, Dependents, Education, Self_Employed,
                  ApplicantIncome, CoapplicantIncome, LoanAmount,Loan_Amount_Term, Credit_History, Property_Area])
    st.success(diagnosis)
    
if __name__=='__main__':
    main()

