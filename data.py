from bs4 import BeautifulSoup
import cloudscraper 
import pandas as pd
import re 
from urllib.parse import urljoin

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
    try :
        response = scraper.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        content = soup.find('div', class_='artContent')
        
        clean_text = content.get_text(separator=' ', strip=True)
        
        text = clean_text[:3000]
        img_links = set()
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                absolute_url = urljoin(url, src)
                img_links.add(absolute_url)
        
        headline = soup.find('h1').get_text(separator=' ', strip= True)
        
        
        image = []
        for img in img_links:
            if '.jpg' in img or '.jpeg' in img:
                image.append(img)
        
        
        data = {
            'Headline' : str(headline),
            'Content' : str(text),
            'Image' : image[0],
            'Url' : url
        }
        
        return data
    
    except Exception:
        data = {
            'Headline' : '---',
            'Content' : '---',
            'Image' : '---',
            'Url' : '---'
        }
        return data 

url = "https://www.hindustantimes.com/"

url_links = article_links(url)





rows = []
for i in range (len(url_links)) :
    data = (UserDefinedData(url_links[i]))
    
    rows.append(data)
    
print(len(rows))
    
df = pd.DataFrame(rows)
df.to_csv('today_news.csv', index=False)

print(df)
    
