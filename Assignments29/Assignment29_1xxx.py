import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.preprocessing import StandardScaler


def Diabetise(Dataset):
    Line = "-" * 108

    df = pd.read_csv(Dataset)
    
    # First five rows
    print(Line)
    print(df.head())
    print(Line)
    
    # column info
    print("Columns in dataset are: ")
    print(df.columns)
    print(Line)
    
    #show null values count of each column
    print("Null Values in columns: ")
    print(Line)
    print(df.isnull().sum())
    print(Line)
    
    #Basic Staticstics using describe() method
    print("Statistics of Diabetise Dataset: ")
    print(Line)
    print(df.describe())
    print(Line)
    
    # histogram of target variable for checking ouliers
    # sns.pairplot(df,hue='Outcome')
    # plt.ylabel("value")
    # plt.title("Distribution of Target Variable using pairplot")
    # plt.show()
    
    #handling missing and zero values
    df.fillna(df.mean(numeric_only=True) , inplace=True)
    
    x = df.drop(columns=['Outcome']) # Features
    y = df['Outcome'] # Labels
    
    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)
    
    x_train , x_test , y_train , y_test = train_test_split(x_scale,y,test_size=0.2,random_state=42)
    
    model  = LogisticRegression()
    
    model.fit(x_train,y_train)
    
    y_pred = model.predict(x_test)
    
    Accuracy = accuracy_score(y_pred,y_test)
    
    print("Accuracy using LogisticRegression: ",Accuracy * 100)
    print(Line)
    
    
    
def main():
    Diabetise("diabetes.csv")    

if __name__  == "__main__":
    main()