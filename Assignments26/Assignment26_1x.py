# play predictor dataset
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def PlayPredictor(Dataset):
    # read the data
    df = pd.read_csv(Dataset)
    
    # Encoding to features and target in given datset
    le = LabelEncoder()
    
    df['Whether'] = le.fit_transform(df['Whether'])
    df['Temperature'] = le.fit_transform(df['Temperature'])
    df['Play'] = le.fit_transform(df['Play'])
    
    print(df)
    
    # training and testing
    
    x = df.drop(columns=['Play'])
    y = df['Play']
    
    scaler = StandardScaler()
    
    x_scale = scaler.fit_transform(x)
    
    # select algorithm
    model = KNeighborsClassifier(n_neighbors=3)
    
    #Training
    x_train , x_test , y_train , y_test = train_test_split(x_scale,y,test_size=0.2, random_state=42)
        
    #Testing
    model.fit(x_train,y_train)
    
    y_pred = model.predict(x_test)
    
    #calculate accuracy
    Accuracy = accuracy_score(y_pred,y_test)
    
    print("Accuracy: ",Accuracy * 100)  # 66.66
     

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()