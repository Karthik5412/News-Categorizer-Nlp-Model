import streamlit as st 
import joblib
import pandas as pd
from transformers import Preprocessing
import requests

api_key = '04b51110e62d2ee68a1d58b2834fc9ed'

url = f'https://gnews.io/api/v4/top-headlines?category=general&lang=en&country=in&max=10&apikey={api_key}'

st.set_page_config(page_title='Today news', page_icon='📰', layout='wide')

pipeline = joblib.load('Pipeline.plk')
le = joblib.load('Encoder.plk')

st.title('Todays News')

# headline = st.text_input('Enter Headline')
# content = st.text_area('Enter Content')


# data = {
#     'Headline' : [headline],
#     'Content' : [content]
# }

data = requests.get(url).json()


articles = data.get('articles', [])
filtered_news = [
    {
        "Headline": a['title'], 
        "link": a['url'], 
        "Content" : a['content'] + ' ' + a['description'],
        "source": a['source']['name']
    } 
    for a in articles
]

df = pd.DataFrame(filtered_news)

# btn = st.button('Predict')


pred = pipeline.predict(df[['Headline', 'Content']])
    
df['pred'] = le.inverse_transform(pred)

st.dataframe(df)