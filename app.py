import streamlit as st 
import joblib
import pandas as pd
from transformers import Preprocessing
import requests



st.set_page_config(page_title='Today news', page_icon='📰', layout='wide')

pipeline = joblib.load('Pipeline.plk')
le = joblib.load('Encoder.plk')

st.title('Todays News')

headline = st.text_input('Enter Headline')
content = st.text_area('Enter Content')

data = {
    'Headline' : [headline],
    'Content' : [content]
}

df = pd.DataFrame(data)

btn = st.button('Predict')

if btn :
    pred = pipeline.predict(df)
    
    st.success(le.inverse_transform(pred))