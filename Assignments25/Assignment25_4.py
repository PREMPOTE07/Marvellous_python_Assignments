import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


def OneHotEncoding():
    data = {
    'Department': ["HR","IT","Finance","HR","IT"]
    }
   
    df = pd.DataFrame(data)
    OH = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    
    encoded =  OH.fit_transform(df[['Department']])
    
    encoded_df = pd.DataFrame(encoded,columns=OH.get_feature_names_out(['Department']))
    df = pd.concat([df,encoded_df],axis=1)
    print(df)
    
    
def main():
    OneHotEncoding()

if __name__ == "__main__":
    main()





