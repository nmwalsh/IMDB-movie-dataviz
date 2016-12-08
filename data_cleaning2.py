#!/usr/bin/env python3
import pandas as pd

#df = pd.read_csv('movie_metadata.csv')
df = pd.read_csv(input('Name of data: '))
#attributes = list(pd)

#enumerates categorical variable column based on key-value pairs in input dictionary
def var_encoder(col, val_dict):
    col_encoded= pd.Series(col,copy=True)
    for key, value in val_dict.items():
        col_encoded.replace(key, value, inplace = True)
    return col_encoded

RATING_DICT={'Passed': 1,
             'Approved': 1,
             'TV-G': 2,
             'TV-Y': 2,
             'TV-Y7': 2,
             'G': 2,
             'GP': 3,
             'TV-PG': 3,
             'PG': 3,
             'TV-14': 4,
             'PG-13': 4,
             'M': 5,
             'TV-MA': 5,
             'R': 5,
             'Not Rated': 6,
             'Unrated': 6,
             'X': 6,
             'NC-17': 6
            }

COLOR_DICT={' Black and White': 0,
            'Color': 1,
            }

df['content_rating'] = var_encoder(df['content_rating'],RATING_DICT)
df['color'] = var_encoder(df['color'],COLOR_DICT)


df = df[df.duration > 60]
del df['movie_imdb_link']

df.to_csv('cleaned_data.csv',index=False)





