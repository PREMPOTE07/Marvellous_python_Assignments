import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.preprocessing import StandardScaler


def Diabetise(Dataset):
    Line = "-" * 108
    #step1: read and load the dataset
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
    sns.pairplot(df,hue='Outcome')
    plt.ylabel("value")
    plt.title("Distribution of Target Variable using pairplot")
    plt.show()
    
def main():
    Diabetise("diabetes.csv")    

if __name__  == "__main__":
    main()