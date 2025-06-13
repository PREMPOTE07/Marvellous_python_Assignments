import sys
import os
import Module # importing module
                
def main():
    border = "-" * 79
    print(border)
    print("-------------------- Marvellous Automation -----------------------")
    print(border)
    
    try:
    
        if(len(sys.argv) == 2):
            if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
                print("This application is used to replace file extension")                 
                print("This is the automation script")
            elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
                print("Use the given script as")
                print("ScriptName.py DirectoryName firstext secondext")
            else:
                ("invalid flags")
                
        elif(len(sys.argv) == 4):
            DirectoryName = sys.argv[1]
            extension1 = sys.argv[2].lower()
            extension2 = sys.argv[3].lower()
            
            flag = os.path.isabs(DirectoryName)
    
            if(flag == False):
                DirectoryName = os.path.abspath(DirectoryName)
                
            flag = os.path.exists(DirectoryName)
            
            if(flag == False):
                print("The path is invalid")
                exit()
                
            flag = os.path.isdir(DirectoryName)
            
            if(flag == False):
                print("Path is valid but the target is not a directory")
                exit()
                
          
            Module.replaceExtension(DirectoryName,extension1 ,extension2) # from module 
            
           
            
        else:
                print("Invalid number of command line arguments")
                print("Use the given flags as: ")
                print("--h: used to display the help")
                print("--u: used to display the usage") 
                
    except Exception as e:
        print(e) 
            
    
    print(border)
    print("-----------------Thank You for using our script-------------------")
    print("-------------------- Marvellous Automation -----------------------")
    print(border)

if __name__ == "__main__":
    main()