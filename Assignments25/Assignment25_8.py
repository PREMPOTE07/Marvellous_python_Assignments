import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def ReplaceEmptyValues():
    data = {
    'Marks': [85,np.nan,90,np.nan,95]
    }
   
    df = pd.DataFrame(data)
    
    print(df)
    
    df.fillna(df.mean(numeric_only=True),inplace=True)
    
    print(df)
    
    
def main():
    ReplaceEmptyValues()

if __name__ == "__main__":
    main()





