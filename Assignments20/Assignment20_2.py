import os
import sys
import time
import hashlib 
from Module import CalculateChecksum
from Module import DisplayDuplicates
from Module import FindDuplicates

def main():
    border = "-" * 66
    print(border)
    print("-------------------- Marvellous Automation -----------------------")
    print(border)
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This application is used to perform directory cleaning")                 
            print("This is the directory automation script")
            
        elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
            print("Use the given script as")
            print("ScriptName.py NameOfDirectory")
            print("Please Provide valid absolute path")
            
        else:
            try:
                DirName =sys.argv[1]
                result = FindDuplicates(DirName)
                DisplayDuplicates(result,DirName)
            except Exception as e:
                print(e)
            
    else:
            print("Invalid number of command line arguments")
            print("Use the given flags as: ")
            print("--h: used to display the help")
            print("--u: used to display the usage")    
            
    
    print(border)
    print("-----------------Thank You for using our script-------------------")
    print("-------------------- Marvellous Automation -----------------------")
    print(border)
    
if __name__ =="__main__":
    main()