import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def Minmaxscaling():
    data = {
        'Name': ['Amit','Sagar','Pooja'],
        'Math': [85,90,78],
        'Science':[92,88,80],
        'English': [75,85,82]
    }

    df = pd.DataFrame(data)

    scaler = MinMaxScaler()

    df['Math'] = scaler.fit_transform(df[['Math']])
        
    print(df)


def main():
    Minmaxscaling()
    
if __name__ == "__main__":
    main()