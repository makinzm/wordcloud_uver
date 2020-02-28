import csv
import pandas as pd

df = pd.read_csv('list.csv',encoding='cp932')

df['album'] = ''

df = df.drop(columns='Unnamed: 0')

for i,row in enumerate(df.itertuples()):
    if(row.release <= 20060215):
        df.at[i, 'album'] = 'Timeless'
    elif(row.release <= 20070221):
        df.at[i, 'album'] = 'BURGRIGHT'
    elif(row.release <= 20080116):
        df.at[i, 'album'] = 'PROGLUTION'
    elif(row.release <= 20090218):
        df.at[i, 'album'] = 'AwakEVE'
    elif(row.release <= 20100414):
        df.at[i, 'album'] = 'LAST'
    elif(row.release <= 20110611):
        df.at[i, 'album'] = 'LIFE 6 SENSE'
    elif(row.release <= 20121128):
        df.at[i, 'album'] = 'THE ONE'
    elif(row.release <= 20140702):
        df.at[i, 'album'] = '0 CHOIR'
    elif(row.release <= 20170802):
        df.at[i, 'album'] = 'TYCOON'
    elif(row.release <= 20191204):
        df.at[i, 'album'] = 'UNSER'
    else:
        df.at[i, 'album'] = 'XXX'
    ##この条件も本当は書きたくない
    #https://ja.wikipedia.org/wiki/UVERworld#アルバム

df = df.sort_values('release',ascending = True)
df = df.reset_index(drop=True)
df.to_csv('list_album.csv', mode = 'a', encoding = 'cp932')