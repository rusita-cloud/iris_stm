import streamlit as st
import joblib
import os
import numpy as np

def run_ml_app():
    st.title('Logistic Regression')
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Input cm for Classification.')
        
        sepal_lenght = st.select_slider('Sepal Length',
                                        options = np.arange(1, 11))
        sepal_width = st.select_slider('Sepal Width',
                                       options = np.arange(1, 11))
        petal_lenght = st.select_slider('Petal Length',
                                        options = np.arange(1, 11))
        petal_width = st.select_slider('Petal Width',
                                       options = np.arange(1, 11))
        
        sample = [sepal_lenght, sepal_width, petal_lenght, petal_width]
        st.write(sample)
        
    with col2:
        st.subheader('Results')
        new_df = np.array(sample).reshape(1, -1)
        
        model = joblib.load('model/model_iris_lr.pkl')
        
        prediction = model.predict(new_df)
        pred_prob = model.predict_proba(new_df)
        st.write(prediction)
        st.write(pred_prob)
        
        