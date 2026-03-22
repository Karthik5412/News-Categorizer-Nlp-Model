import streamlit as st 
import joblib
import pandas as pd
from transformers import Preprocessing
import requests
from pygooglenews import GoogleNews

st.set_page_config(page_title='Today news', page_icon='📰', layout='wide')

def data_api(url) :
    data = []

    gn = GoogleNews(country = "IN")

    search = gn.search('entertainment')
    data = {}

    # for item in search['entries'] :
    #     data = {
    #         'Headline' :,
            
    #     }





pipeline = joblib.load('Pipeline.plk')
le = joblib.load('Encoder.plk')

st.title('Todays News')


gn = GoogleNews(country = "IN")

search = gn.search('entertainment')

for item in search['entries'] :
    
    st.json(item)
    st.success('End')









pred = pipeline.predict(df[['Headline', 'Content']])
    
df['pred'] = le.inverse_transform(pred)

st.dataframe(df)