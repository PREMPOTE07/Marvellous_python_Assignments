import pandas as pd
import numpy as np



def RenameDictionaryValues():
    data = {
    'Grade':['A+','B','A','C','B+']
    }
   
    for i in range(len(data['Grade'])):
        if data['Grade'][i] == 'A+':
            data['Grade'][i] ='Excellent'
        elif data['Grade'][i] == 'A':
            data['Grade'][i]='Very Good'
        elif data['Grade'][i] == 'B+':
            data['Grade'][i]= 'Good'
        elif data['Grade'][i] == 'B':
            data['Grade'][i] = 'Average'
        else:
            data['Grade'][i]='Poor'
    
    print(data)
            
    
    
    
    
def main():
    RenameDictionaryValues()

if __name__ == "__main__":
    main()





