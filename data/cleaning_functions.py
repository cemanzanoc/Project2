# functions 

import pandas as pd

def replace_age(df):
    
    bins = [0,30,40,50,70,100]
    labels = ['Z generation', 'millennials', 'X generation', 'boomers', '70+']
    df['generation'] = pd.cut(df['clnt_age'], bins = bins, labels = labels, right = False, include_lowest=True)
    
    return df