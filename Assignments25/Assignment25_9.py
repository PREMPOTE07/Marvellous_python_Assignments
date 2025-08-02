import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def ReplaceFail():
    data = {
    'Marks': [45,67,88,32,76]
    }
   
    df = pd.DataFrame(data)
    
    print(df)
    
    df = df.where(df['Marks'] > 50 , 'Fail')
    
    print(df)
    
    
def main():
    ReplaceFail()

if __name__ == "__main__":
    main()





