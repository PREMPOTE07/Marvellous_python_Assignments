import pandas as pd 
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder , StandardScaler

def BankFull(Dataset):
    Line = "-" * 79
    
    #1)load and read the dataset
    df = pd.read_csv(Dataset,sep=';',quotechar='"')
    
    # Display basic stats
    print(df.head()) # fist five rows
    print(Line)
    print("Shape of dataset: ",df.shape)
    print(Line)
    print("Information of Dataset Columns: ")
    print(df.info())
    print(Line)
    print(df.isnull().sum()) # any missing values for each column
    print(Line)
    print("values of target variable: ")
    print(df['y'].value_counts())
    print(Line)
    print(df.describe())
    print(Line)
    
    #visualize the target column
    # plt.hist(df['y'],bins=2,color='skyblue',edgecolor='black')
    # plt.title("Visualization of Target column (y)")
    # plt.xlabel("subscriber")
    # plt.ylabel("Frequency")
    # plt.show()
    
    #2)Preprocess the data
    #LabelEncoding
    columns = ['job','marital','education','default','housing','loan','contact','month','poutcome','y']
    for c in columns:
        le = LabelEncoder()
        df[c] = le.fit_transform(df[c])
        
    # print(df.head())
    #Scale numeric features
    scaler = StandardScaler()
    x = df.drop(columns=['y'])
    y = df['y']
    x_scale  = scaler.fit_transform(x)
    
        
    
    
def main():
    BankFull("bank-full.csv")

if __name__ == "__main__":
    main()