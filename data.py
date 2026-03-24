from newspaper import Article
from bs4 import BeautifulSoup
import cloudscraper 
import pandas as pd
import re 

scraper = cloudscraper.create_scraper(
    browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False}
    )

def article_links(url) : 
    
    try :
        response = scraper.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            all_links = soup.find_all('a', href=True)
            links = set()
            
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
                
            return list(links)
        
    except Exception as e:
        return f"Error: {e}"


def UserDefinedData(url) :
    
    response = scraper.get(url)
    
    article = Article(url)
    
    article.html = response.text
    article.download_state = 2
    article.parse()
    
    
    data = {
        'Headline' : article.title,
        'Content' : article.text,
        'Image' : article.top_image
    }
    
    return data

url = "https://www.hindustantimes.com/"

url_links = article_links(url)

data = {}
for i in range (len(url_links)) :
    data[i] = article_links(url_links[i])
    


for value in data.items() :
    print(value)
    