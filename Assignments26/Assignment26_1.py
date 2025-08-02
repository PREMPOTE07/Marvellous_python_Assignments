# play predictor dataset
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder

def PlayPredictor(Dataset):
    # read the data
    df = pd.read_csv(Dataset)
    
    # Encoding to features and target in given datset
    le = LabelEncoder()
    
    df['Whether'] = le.fit_transform(df['Whether'])
    df['Temperature'] = le.fit_transform(df['Temperature'])
    df['Play'] = le.fit_transform(df['Play'])
    
    print(df)
    

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()