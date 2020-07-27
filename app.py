# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import streamlit as st
import pickle

from PIL import Image


pickle_in=open("random_forest_regression_model.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_Price(Present_Price,Kms_Driven,Owner,no_of_year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual):
    prediction=classifier.predict([[Present_Price,Kms_Driven,Owner,no_of_year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
    print(prediction)
    return prediction

def main():
    st.write("""
            # CAR PRICE PREDICTION
              Using **Streamlit** By **Sufiyan Ghori**
             """)
    image = Image.open('cars.jpg')
    st.image(image, use_column_width=True)
    html_temp = """
    <div style="background-color:SeaGreen;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Present_price=st.number_input(('Present Price'), min_value=0.0, max_value=36.0,key=0)
    Kms_Driven=st.number_input(('Kms_Driven'),min_value=500, max_value=500000,key=1)
    Owner=st.selectbox('Owner',('0', '1', '3'))
    Year=st.number_input(('Year'),min_value=2003, max_value=2020,key=2)
    no_of_years=2020-Year
    Fuel=st.selectbox('Fuel',('Petrol', 'Diesel', 'CNG'))
    if(Fuel=='Petrol'):
        Fuel_Type_Diesel=0
        Fuel_Type_Petrol=1
    elif(Fuel=='Diesel'):
        Fuel_Type_Diesel=1
        Fuel_Type_Petrol=0
    else:
        Fuel_Type_Diesel=0
        Fuel_Type_Petrol=0
    Seller_Type=st.selectbox('Seller_Type',('Individual', 'Dealer'))
    if(Seller_Type=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0
    Transmission=st.selectbox('Transmission',('Manual', 'Automatic'))
    if(Transmission=='Manual'):
        Transmission_Manual=1
    else:
        Transmission_Manual=0
    result=""
    if st.button('predict'):
        result=predict_Price(Present_price,Kms_Driven,Owner,no_of_years,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual)
        st.success("The output is {}".format(result))


if __name__=='__main__':
    main()
    
    
