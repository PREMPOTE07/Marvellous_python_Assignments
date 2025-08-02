import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def LabelEncoding():
    data = {
    'City': ["Pune","Mumbai","Delhi","Pune","Delhi"]
    }
   
    df = pd.DataFrame(data)
    le = LabelEncoder()
    
    df['City'] = le.fit_transform(df['City'])
    print(df)
    
    
    
def main():
    LabelEncoding()

if __name__ == "__main__":
    main()





