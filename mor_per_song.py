from janome.tokenizer import Tokenizer
import pandas as pd
import re
import os
from googletrans import Translator

if not os.path.exists("single_ja_text"):
    os.makedirs("single_ja_text")

if not os.path.exists("single_en_text"):
    os.makedirs("single_en_text")

df_all = pd.read_csv('list_album.csv', encoding='cp932')

list_album = list(set(df_all['title']))
t = Tokenizer()
translator = Translator()

lyrics_album = []

for i in list_album:
    u = i
    if('/' in i):
        u = i.replace('/','-')
    text_file_ja = 'single_ja_text/' + str(u) + '_ja.txt'
    text_file_en = 'single_en_text/' + str(u) + '_en.txt'
    k = []
    all_k = ''
    #exec(f'text_{i} = list_{i}.txt')
    for row in df_all.itertuples():
        if(row[2] == i):
            k.append(row[4])
            #df_all = df_all.drop(row.Index)
    for s in k:
        results = []
        results_en = []

        tokens = t.tokenize(s)
        r = []
        for tok in tokens:
            if tok.base_form == '*': 
                word = tok.surface 
            else:
                word = tok.base_form 

            ps = tok.part_of_speech 

            hinshi = ps.split(',')[0] 

            if hinshi in ['名詞', '形容詞', '動詞', '副詞']: 
                r.append(word)

        '''
        r_en = []
        for src in r:
            dst = translator.translate(src, src='ja', dest='en')
            r_en.append(dst.text)
        print(r_en)
        
        rl_en = (''.join(r_en)).strip()
        results_en.append(rl_en)
        result_en = [i.replace('\u3000','') for i in results_en]

        with open(text_file_en, 'a', encoding='utf-8') as fp:
            fp.write("\n".join(result_en))
        '''

        rl = (' '.join(r)).strip()
        results.append(rl)
        result_ja = [i.replace('\u3000','') for i in results]
        
        with open(text_file_ja, 'a', encoding='utf-8') as fp:
            fp.write("\n".join(result_ja))
        
        