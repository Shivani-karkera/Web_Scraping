
get_ipython().system('pip3 install requests')


get_ipython().system('pip install bs4')


get_ipython().system('pip install urllib3')
get_ipython().system('pip install html5lib')

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import sqlite3
import pandas as pd
import time


def to_get_images():
    linki=[]
    page= requests.get("https://news.google.com/search?q=nri&hl=en-IN&gl=NI&ceid=IN%3Aen")
    #with requests.Session() as c:
    soups= BeautifulSoup(page.content,'html5lib')
    #print(soups.prettify())
    
    images = soups.find_all('img')
    for linki in images:
        d.append(linki['srcset'].split("1x,")[1].split("2x")[0])
    return (d)

while(True):
    
    conn = sqlite3.connect('my_database.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE google_news')
    cur.execute('CREATE TABLE google_news(News_Link VARCHAR, News_Title CHAR, Short_Description CHAR, Featured_Image VARCHAR, Published_Time VARCHAR)')
    url = "https://www.google.com/search?q=nri&source=lmns&tbm=nws&bih=657&biw=1366&rlz=1C1CHBF_enIN919IN919&hl=en&sa=X&ved=2ahUKEwiW4-3dosjyAhVEUnwKHeKKCwQQ_AUoAXoECAEQAQ"
    req= Request(url, headers={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    with requests.Session() as c:
        soup= BeautifulSoup(webpage,'html5lib')
            #print(soup.prettify())
    count=0   
    for item in soup.find_all('div', attrs={'class': 'ZINbbc xpd O9g5cc uUPGi'}):
        raw_link=(item.find('a',href=True)['href'])
        link=raw_link.split("/url?q=")[1].split('&sa=U&')[0]
            #print(item)
        title=(item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
            #print('Link: '+link)
            #print('Title: '+title)
        Summary=(item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())
        Published_Time= Summary.split("·")[0]
        des=Summary.split("·")[1]
            #print('Summary: '+des)
        d=[]
        to_get_images()
            #print('Image URl: '+d[count] )
        count+=1
            #print('Time: '+Published_Time)
        cur.execute('''''''INSERT INTO google_news VALUES(?,?,?,?,?)''''''',(link,title,des,d[count], Published_Time))
    conn.commit()
    #print('done')
    cur.execute('SELECT * FROM google_news')
    df= pd.read_sql_query('SELECT * FROM google_news', conn)
    print(df)
    conn.close()
    time.sleep(3600)





    



