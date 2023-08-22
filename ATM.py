import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("trainedmodel.sav","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def atmcash(Bank,ATMID,DT,MaxCapacity,TotalTxn,year,month,dayofweek,day,is_month_start,is_month_end):
   
    prediction=classifier.predict([[Bank,ATMID,DT,MaxCapacity,TotalTxn,year,month,dayofweek,day,is_month_start,is_month_end]])
    print(prediction)
    return prediction



def main():
    st.title(" ..")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">ATM Cash Withdrawl Prediction Application </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Bank = st.text_input("Bank"," ")
    ATMID = st.text_input("ATMID"," ")
    DT = st.text_input("DT"," ")
    MaxCapacity = st.text_input("MaxCapacity"," ")
    TotalTxn = st.text_input("Total Transaction"," ")
    year = st.text_input("Year"," ")
    month = st.text_input("Month"," ")
    dayofweek = st.text_input("Dayofweek"," ")
    day = st.text_input("Day"," ")
    is_month_start = st.text_input("Month Start"," ")
    is_month_end = st.text_input("Month End"," ")
    
    result=""
    
    if st.button("Predict"):
        result=atmcash(Bank,ATMID,DT,MaxCapacity,TotalTxn,year,month,dayofweek,day,is_month_start,is_month_end)
    st.success('Predicted ATM Cash Dispense for the given input is  - {}'.format(result))
    
    
    
	


if __name__=='__main__':
    main()
    
    
    