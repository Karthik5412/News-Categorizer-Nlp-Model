import streamlit as st 
import joblib
import pandas as pd
from transformers import Preprocessing
from datetime import  date
pipeline = joblib.load('Pipeline.plk')
le = joblib.load('Encoder.plk')

df = pd.read_csv('today_news.csv')

df = df[df['Headline'] != '---'].reset_index()

st.set_page_config(page_title='Today news', page_icon='📰', layout='wide')

st.title('Todays News  🗞️', text_alignment= 'center')
st.subheader(date.today(), text_alignment= 'right')

pred = pipeline.predict(df[['Headline','Content']])
df['Category'] = le.inverse_transform(pred)

df['Category'] = df['Category'].astype(str).str.capitalize()

categories = sorted(list(set(item for item in df['Category'])))

n = 3
tabs = st.tabs(categories)

for idx, val in enumerate(categories) :
    with tabs[idx] :
        
        data = df[df['Category'] == val].reset_index(drop=True)
        
        num_rows = (len(data) + n - 1) // n
        for row_idx in range(num_rows):
            cols = st.columns(n)
            
            for col_idx in range(n) :
                data_idx = row_idx * n + col_idx
        
                if data_idx < len(data) :
                    row = data.iloc[data_idx]
                    
                    with cols[col_idx] :
                        with st.container(border= True) :
                            st.image(row['Image'], use_container_width= True)
                            st.subheader(row['Headline'])
                            with st.expander('Article') :
                                st.write(row['Content'])
        










