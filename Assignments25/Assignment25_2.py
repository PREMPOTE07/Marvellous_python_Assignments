import pandas as pd
import numpy as np


def ConvertDataTypeOfColumn():
    data = {
    'Name': ["A","B","C"],
    'Age': [21.0 , 22.0, 23.0]
    }
   
    df = pd.DataFrame(data)
    
    print("DataType of Age is: ",df['Age'].dtypes)
    print()
    df['Age'] = df['Age'].astype(int)
    print(df)
    
    
def main():
    ConvertDataTypeOfColumn()

if __name__ == "__main__":
    main()





