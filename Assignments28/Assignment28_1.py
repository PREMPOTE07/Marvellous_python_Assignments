import pandas as pd
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


def winePredictor(Dataset):
    Line = "-" * 79
    #step1: read and load the dataset
    df = pd.read_csv(Dataset)
    
    print(Line)
    print(df.head())
    print(Line)
    
    print("Missing values: ",df.isnull().sum()) # print missing values if available
    print(Line)
    
    #step2: clean , prepare and manupulate data
    
    #Step3: Training and testing dataset
    x = df.drop(columns=['Class'])
    y = df['Class']
    
    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)
    
    x_train , x_test , y_train , y_test = train_test_split(x_scale,y , test_size=0.2 , random_state=42)
    
    Accuracy_Scores = []
    KRange =  range(1,21)
    
        
    for k in KRange:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)
        Accuracy = accuracy_score(y_test , y_pred)
        Accuracy_Scores.append(Accuracy)
    
    
    best_k = KRange[Accuracy_Scores.index(max(Accuracy_Scores))]
    print("Best value of k is: ",best_k)
    print(Line)
    
    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    Accuracy = accuracy_score(y_test , y_pred)
    
    print("Final best accuacy is : ",Accuracy * 100)
    print(Line)
 

def main():
    winePredictor("WinePredictor.csv")    

if __name__  == "__main__":
    main()