from janome.tokenizer import Tokenizer
import pandas as pd
import re
import os
from googletrans import Translator

if not os.path.exists("ja_text"):
    os.makedirs("ja_text")

if not os.path.exists("en_text"):
    os.makedirs("en_text")

df_all = pd.read_csv('list_album.csv', encoding='cp932')

list_album = list(set(df_all['album']))
t = Tokenizer()
translator = Translator()

lyrics_album = []

for i in list_album:
    text_file_ja = 'ja_text/' + str(i) + '_ja.txt'
    text_file_en = 'en_text/' + str(i) + '_en.txt'
    k = []
    all_k = ''
    #exec(f'text_{i} = list_{i}.txt')
    for row in df_all.itertuples():
        if(row[5] == i):
            k.append(row[4])
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
        
        