import random
import pandas as pd


lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})



def one_hot(df, name):
    for i in df[name].unique():
        df[i] = (df[name] == i).astype(int) 
    df.drop(name, axis=1, inplace=True)
    return df

print(one_hot(data, 'whoAmI'))