import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def MinMaxScaling():
    data = {
    'Age' : [18,22,25,30,35]
    }
   
    df = pd.DataFrame(data)
    
    scaler = MinMaxScaler()
    
    df['Age'] = scaler.fit_transform(df[['Age']])
    
    print(df)
    
            
    
    

def main():
    MinMaxScaling()

if __name__ == "__main__":
    main()





