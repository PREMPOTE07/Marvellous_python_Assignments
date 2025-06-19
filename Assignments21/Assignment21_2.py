import sys
from Module import ProcInfo

def main():
    ProcessName = sys.argv[1]
    border = "-" * 66
    print(border)
    print("-------------------- Marvellous Automation -----------------------")
    print(border, "\n")
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This application is used to display running process which is given as a argument")                 
            print("This is the directory automation script")
            
        elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
            print("Use the given script as")
            print("DirectoryCheckSum.py ProcessName")
            
        else:
            Arr = ProcInfo()
            isRunning = False
            for value in Arr:
                if value['name'] == ProcessName:
                    isRunning = True
            if isRunning == True:
                print(f"{value} Process is running")
            
            else:
                print("There is no such process running")
                    
            
              
            
    else:
            print("Invalid number of command line arguments")
            print("Use the given flags as: ")
            print("--h: used to display the help")
            print("--u: used to display the usage")    

    print(border, "\n")
    print("-----------------Thank You for using our script-------------------")
    print("-------------------- Marvellous Automation -----------------------")
    print(border)


if __name__ == "__main__":
    main()