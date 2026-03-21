import streamlit as st 
import joblib
import pandas as pd
from transformers import Preprocessing
import requests
from newspaper import Article

st.set_page_config(page_title='Today news', page_icon='📰', layout='wide')

def paper(url) :
    article = Article(url)
    
    article.download()
    article.parse()
    
    data = {
        "title": article.title,
        "text": article.text,        
        "top_image": article.top_image, 
        "images": article.images,    
        "date": article.publish_date
    }
    
    return data

bbc = 'https://www.bbc.com/news/world/asia/india'

api_key = '04b51110e62d2ee68a1d58b2834fc9ed'

url = f'https://gnews.io/api/v4/top-headlines?category=general&lang=en&country=in&max=10&apikey={api_key}'


pipeline = joblib.load('Pipeline.plk')
le = joblib.load('Encoder.plk')

st.title('Todays News')

# headline = st.text_input('Enter Headline')
# content = st.text_area('Enter Content')


news_data = paper(url)
print(f"Title: {news_data['title']}")
print(f"Top Photo: {news_data['top_image']}")

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