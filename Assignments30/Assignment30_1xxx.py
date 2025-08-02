import pandas as pd 
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder , StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import sklearn.metrics as metrics

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
    
    #3)Split the data
    x_train , x_test , y_train , y_test =  train_test_split(x_scale,y,test_size=0.2 , random_state=42)
    
    #4)By using Logistic regression
    model = LogisticRegression()
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    Accuracy = metrics.accuracy_score(y_test,y_pred)
    #Accuracy of algorithm
    print(Line)
    print("Accuracy using LogisticRegression: ",Accuracy*100)
    print(Line)
    #Confusion Matrix
    cm = metrics.confusion_matrix(y_test,y_pred)
    print("Confusion Matrix: ",cm)
    print(Line)
    #classification report
    print("Classification report: ")
    print(metrics.classification_report(y_test,y_pred,target_names=['no','yes']))
    print(Line)
    #ROC_AUC score
    print("ROC_AUC Score is: ",metrics.roc_auc_score(y_test,y_pred))
    print(Line)
    
    #Visualize confusion matrix and roc score
    plt.figure(figsize=(8,5))
    sns.heatmap(cm,annot=True,cmap='coolwarm')
    plt.title("confusion matrix visualization")
    plt.xlabel("Predicted value")
    plt.ylabel("Actual value")
    plt.show()
    
    #calcualte fpr , tpr , thresholds
    fpr , tpr, thresholds = metrics.roc_curve(y_test,y_pred)
    plt.figure(figsize=(8,7))
    plt.plot(fpr,tpr,color='red',label = "Roc Curve")
    plt.plot([0,1],[0,1],color='blue',linestyle = "--")
    plt.xlabel("False Positive rate (FPR)")
    plt.ylabel("True Positive Rate(TPR)")
    plt.legend()
    plt.grid(True)
    plt.show()

    
    
def main():
    BankFull("bank-full.csv")

if __name__ == "__main__":
    main()