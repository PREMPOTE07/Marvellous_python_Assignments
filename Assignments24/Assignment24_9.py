import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

data = {
    'Name': ['Amit','Sagar','Pooja'],
    'Math': [85,90,78],
    'Science':[92,88,80],
    'English': [75,85,82]
}

df = pd.DataFrame(data)
    
df['Total'] = df['Math'] + df['Science'] + df['English']

df['Gender'] = ['Male','Male','Female']

encode = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

df['Gender'] = encode.fit_transform(df[['Gender']])

df['Status'] = np.where(df['Total'] >= 250 , 'Pass' , 'Fail')


df.rename(columns={'Math' : 'Mathematics'},inplace=True)

print(df)





