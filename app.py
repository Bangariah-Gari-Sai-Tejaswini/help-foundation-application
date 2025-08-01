
import streamlit as st
import numpy as np
import pandas as pd
import joblib 

# dirst lets load instances we created

with open('scaler.joblib','rb') as file:
    scale = joblib.load(file)
    
with open('pca_final.joblib','rb') as file:
    pca = joblib.load(file)
    
with open('kmeans_final.joblib','rb') as file:
    model = joblib.load(file)
    

def prediction(input_list):
    scaled_input = scale.transform([input_list])
    pca_input = pca.transform(saled_input)
    output = mode.predict(pca_input)[0]
    
    if output == 0 :
        return "developing"
    
    elif output == 1:
        return "developed"
    
    else: 
        return "underdeveloped"
    
def main():
    st.title("Help NGO Foundation")
    st.subheader("This application willl give status of country based on socio-economic & health factors")
    
    gdp = st.text_input('Enter the GDP for population of country')
    inc = st.text_input('Enter per capita income of a country')
    imp = st.text_input('Enter the imports in terms of % of GDP')
    exp = st.text_input('Enter the exports in terms of % of GDP')
    inf = st.text_input("Enter the inflation rate in a country(%)")
    hel = st.text_input("Enter the health expenditure in terms of % of GDP")
    ch_m = st.text_input("Enter the no of deaths per 1000 births for <5 years")
    fer = st.text_input("Enter the avg children born o a woman in a country")
    lf = st.text_input("Enter the avg life expectancy in a country")
    
    in_data = [ch_m,exp,hel,imp,inc,inf,lf,fer,gdp]
    
    if st.button('Predict'):
        response = prediction(in_data)
        st.success(response)
        
if __name__ == '__main__':
    main()
