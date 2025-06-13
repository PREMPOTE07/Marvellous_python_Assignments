import os
import sys

def isSameContent(F1,F2):
    F1obj = open(F1,"r")
    File1Data = F1obj.read()
    
    F2obj = open(F2,"r")
    File2Data = F2obj.read()
    
    if File1Data == File2Data:
        print("Sucess")
    else:
        print("Failure")
 

def main():
    border = "-" * 66
    print(border)
    print("-------------------- Marvellous Automation -----------------------")
    print(border)
    
    if(len(sys.argv) == 3):
        if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This application is used to perform both file content same or not")                 
            print("This is the automation script")
        elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
            print("Use the given script as")
            print("ScriptName.py FileName1 FileName2")
        else:
            FileName1 = sys.argv[1]
            FileName2 = sys.argv[2]
            isSameContent(FileName1,FileName2)
            
            
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