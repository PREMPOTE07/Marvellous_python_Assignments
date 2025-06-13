import sys
import os
import Module 
                
def main():
    border = "-" * 79
    print(border)
    print("-------------------- Marvellous Automation -----------------------")
    print(border)
    
    try:
    
        if(len(sys.argv) == 2):
            if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
                print("This application is used to copy files with given extension only")                 
                print("This is the automation script")
            elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
                print("Use the given script as")
                print("ScriptName.py DirectoryName1 DirectoryName2 .exe")
            else:
                ("invalid flags")
                
        elif(len(sys.argv) == 4):
            DirectoryName1 = sys.argv[1]
            DirectoryName2 = sys.argv[2]
            Extension = sys.argv[3]
            flag = os.path.isabs(DirectoryName1)
    
            if(flag == False):
                DirectoryName1 = os.path.abspath(DirectoryName1)
                
            flag = os.path.exists(DirectoryName1)
            
            if(flag == False):
                print("The path is invalid")
                exit()
                
            flag = os.path.isdir(DirectoryName1)
            
            if(flag == False):
                print("Path is valid but the target is not a directory")
                exit()
                        
            Module.copyFilesExe(DirectoryName1,DirectoryName2,Extension) 
            
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