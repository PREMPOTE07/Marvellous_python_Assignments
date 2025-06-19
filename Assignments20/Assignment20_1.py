import sys
import os
from Module import CalChecksumOfAllFilesInFolder
import time

def main():
    DirectoryName = sys.argv[1]
    border = "-" * 66
    print(border)
    print("-------------------- Marvellous Automation -----------------------")
    print(border, "\n")
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This application is used to display checksum of all files inside folder")                 
            print("This is the directory automation script")
            
        elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
            print("Use the given script as")
            print("DirectoryCheckSum.py NameOfDirectory")
            print("Please Provide valid absolute path")
            
        else:
            try:
                CalChecksumOfAllFilesInFolder(DirectoryName)
            except Exception as e:
                print(e)
            
    else:
            print("Invalid number of command line arguments")
            print("Use the given flags as: ")
            print("--h: used to display the help")
            print("--u: used to display the usage")    
    
    print(border, "\n")    
    print(f"\nTime of created this ouput log file {time.ctime()}\n")
    print(border, "\n")

    print(border, "\n")
    print("-----------------Thank You for using our script-------------------")
    print("-------------------- Marvellous Automation -----------------------")
    print(border)
    
                

if __name__ == "__main__":
    main()