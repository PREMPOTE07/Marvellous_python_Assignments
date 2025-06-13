import os
import sys

def CalFrequency(FileName,s):
    Fobj = open(FileName,"r")
    FileData = Fobj.read()
    
    freq = 0
    
    for word in FileData.split():
        if word == s:
           freq += 1
        
    print(f"{s} is happen in {freq} times")
        
 

def main():
    border = "-" * 66
    print(border)
    print("-------------------- Marvellous Automation -----------------------")
    print(border)
    
    if(len(sys.argv) == 3):
        if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This application is used to calculate freq of given word in given file")                 
            print("This is the automation script")
        elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
            print("Use the given script as")
            print("ScriptName.py FileName word/string")
        else:
            FileName = sys.argv[1]
            str = sys.argv[2]
            CalFrequency(FileName,str)
            
            
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