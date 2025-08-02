import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


def TrainTestSplitData():
    data = {
    'Age': [25,30,45,35,22],
     'Salary': [50000,60000,80000,65000,45000],
     'Purchased': [1,0,1,0,1]
    
    }
   
    df = pd.DataFrame(data)
    
    model = LogisticRegression()
    
    x = df.drop(columns=['Purchased'])
    
    y = df['Purchased']
    
    scaler = StandardScaler()
    
    x_scale = scaler.fit_transform(x)
    
    x_train, x_test , y_train , y_test = train_test_split(x_scale,y,test_size=0.2,random_state=42)
    
    model.fit(x_train,y_train)
    
    y_pred = model.predict(x_test)
    
    Accuracy = accuracy_score(y_test,y_pred)
    
    print("Accuracy: ",Accuracy * 100)
    
    
def main():
    TrainTestSplitData()

if __name__ == "__main__":
    main()





