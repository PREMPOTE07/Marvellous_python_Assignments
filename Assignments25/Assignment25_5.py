import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def TrainTestSplit():
    data = {
    'Age':[22,25,47,52,46,56],
    'Purchased': [0,1,1,0,1,0]
    }
   
    df = pd.DataFrame(data)
    
    x= df[['Age']]
    y= df['Purchased']
    
    x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    
    model  = LogisticRegression()
    
    model.fit(x_train , y_train)
    
    y_pred = model.predict(x_test)
    
    Accuracy = accuracy_score(y_pred,y_test)
    
    print("Accurcy: ",Accuracy * 100)
    
    
    
    
def main():
    TrainTestSplit()

if __name__ == "__main__":
    main()





