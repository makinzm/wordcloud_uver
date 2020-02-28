import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import types

list_df = pd.DataFrame(columns=['title','release','lyrics'])

base_url = 'https://www.uta-net.com'
url = 'https://www.uta-net.com/search/?Aselect=1&Keyword=UVER&Bselect=3&x=0&y=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
links = soup.find_all('td', class_='side td1')
for link in links:
    a = base_url + (link.a.get('href'))
    response = requests.get(a)
    soup = BeautifulSoup(response.text, 'lxml')
    song_title = soup.find('h2', class_='prev_pad')
    if(song_title is None):
        song_title = soup.find('div', class_='title').text
        song_title = song_title.strip()
    else:
        song_title = song_title.string
        song_title = song_title.replace('<h2 class="prev_pad">','')
        song_title = song_title.replace('</h2>','')
    if 'ver.' in song_title or  'TV' in song_title or  'version' in song_title:
        pass
    else:
        song_release = soup.find('div', id='view_amazon').text[5:15]
        song_release = song_release.replace('-','')
        song_release = int(song_release)
        song_lyrics = soup.find('div', itemprop='lyrics')
        song_lyrics = song_lyrics.text
        song_lyrics = song_lyrics.replace('\n','')
        time.sleep(0.5)
        tmp_se = pd.DataFrame([song_title, song_release, song_lyrics], index=list_df.columns).T

        list_df = list_df.append(tmp_se)
print(list_df)

list_df.to_csv('list.csv', mode = 'a', encoding='cp932')