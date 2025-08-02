import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score , mean_squared_error , r2_score


def AdvertisingDF(Dataset):
    Line = "-" * 79
    #step1: read and load the data
    df = pd.read_csv(Dataset)
    
    # step2: clean , prepare and manipulate data
    df = df.drop(columns=['Unnamed: 0'],inplace=True) # remove unwanted column
    print(Line)
    print(df.head()) # first five rows
    print(Line)

    print("Missing values: ",df.isnull().sum()) # print missing values if available
    print(Line)

    
    # step3: train and test data
    x = df.drop(columns=['sales'])
    y = df['sales']
    
    x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    
    model = LinearRegression()
    
    model.fit(x_train,y_train)
    
    y_pred = model.predict(x_test)
    
    #display predicted and actual values
    results = pd.DataFrame({"Actual values: ": y_test,"Predicted values: ": y_pred})
    print(Line)
    print(results.head())
    print(Line)

    MSE = mean_squared_error(y_pred,y_test)
    
    RMSE = np.sqrt(MSE)
    
    r2 = r2_score(y_pred,y_test)
    print("Mean Square error is: ",MSE)
    print("Root Mean Square error is: ",RMSE)
    print("R Square value: ",r2)
    print(Line)
    
    print("Model Coefficient are: ")
    for col , coef in zip(x.columns,model.coef_):
        print(f"{col} : {coef}")
        
    print("Y Intercept is ",model.intercept_)
    print(Line)

    

def main():
    AdvertisingDF("Advertising.csv")

if __name__ == "__main__":
    main()