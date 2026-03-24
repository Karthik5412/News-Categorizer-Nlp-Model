import streamlit as st 
import joblib
import pandas as pd
from transformers import Preprocessing
import requests
from newspaper import Article
from bs4 import BeautifulSoup
import cloudscraper 

pipeline = joblib.load('Pipeline.plk')
le = joblib.load('Encoder.plk')

st.set_page_config(page_title='Today news', page_icon='📰', layout='wide')



    
    


st.title('Todays News')

url = "https://www.hindustantimes.com/"






