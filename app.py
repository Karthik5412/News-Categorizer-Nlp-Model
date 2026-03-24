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


def article_links(url) :
    scraper = cloudscraper.create_scraper(
    browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False}
    )
    
    links = set()
    
    try :
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup.get(response.text, 'html.parse')
            
            all_links = soup.find_all('a', href = True)
            
            for link in all_links :
                href = link['href']
                
                if href.endswith('.html') and '/static-pages/' not in href:
                    if href.startswith('/'):
                        full_url = f"https://www.hindustantimes.com{href}"
                elif href.startswith('https://www.hindustantimes.com'):
                    full_url = href
                else:
                    continue
                
                links.add(full_url)
                
            return links
        
    except Exception as e:
        st.success(f"Error: {e}")


def DataFrame(url) :
    
    article = Article(url)
    
    article.download()
    article.parse()
    
    article.download('punckt')
    
    article.nlp()


st.title('Todays News')

url = "https://www.hindustantimes.com/"






