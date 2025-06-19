import sys
import time
from Module import DisplayDuplicates
from Module import FindDuplicates
from Module import DeleteDuplicate

def main():
    border = "-" * 66
    print(border)
    print("-------------------- Marvellous Automation -----------------------")
    print(border)
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This application is used to display duplicate files in log.txt and delete those files also display execution time")                 
            print("This is the directory automation script")
            
        elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
            print("Use the given script as")
            print("ScriptName.py NameOfDirectory")
            print("Please Provide valid absolute path")
            
        else:
            try:
                DirName = sys.argv[1]
                result = FindDuplicates(DirName)
                DisplayDuplicates(result,DirName)
                start_time = time.time()
                DeleteDuplicate(result)
                end_time = time.time()
                print("Execution time of deleting file is : ", end_time - start_time)
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