from wordcloud import WordCloud
import os
import glob

if not os.path.exists("ja_wordcloud"):
    os.makedirs("ja_wordcloud")

files = glob.glob("./ja_text/*")
fpath = '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc'
stop_words = ['する','そう','られる','ない','なる','こと','する','いる','てる','よう','くれる','いる','ため','れる','the','lo','It','La','la','Wow','Yo','よう']
stop_words += ['せる','ゆく','もう','もの','それ','どう','これ']
stop_words += ['No',]
stop_words += ['EverybodyWow', 'WowYo']

for file in files:
    name = os.path.basename(file)[:-7]
    text = open(file, encoding='utf-8').read()
    wordcloud = WordCloud(background_color='white',font_path=fpath, width=800, height=600, stopwords=set(stop_words)).generate(text)
    wordcloud.to_file('./ja_wordcloud/wordcloud_ja_'+name+'_.png')