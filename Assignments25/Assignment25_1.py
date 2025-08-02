import pandas as pd
import numpy as np


def DetectOutliers():
    data = {
    'Salary': [25000,27000,29000,31000,50000,100000]
    }
   
    df = pd.DataFrame(data)
    salary = df["Salary"]
    
    # First step find first and third quartile
    Q1 = salary.quantile(0.25)
    Q3 = salary.quantile(0.75)
    
    # second step find IQR = Q2 - Q1
    IQR = Q3 - Q1
    
    # Third step find outliers boundries
    lowerBound= Q1 - 1.5 * IQR
    UpperBound= Q3 + 1.5 * IQR
    
    #Find outliers
    Outliers = salary[(salary < lowerBound) | (salary > UpperBound)]
    
    print("First Qurtile: ",Q1)
    print("Third Qurtile: ",Q3)
    print("IQR: ",IQR)
    print("LOwer bound: ",lowerBound)
    print("Upper bound: ",UpperBound)
    print("ounliers: ",Outliers.to_list())
    
    
def main():
    DetectOutliers()

if __name__ == "__main__":
    main()





