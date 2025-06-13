import os
import sys

def CopyFileContent(exitsFile,copyFile):
    eobj = open(exitsFile,"r")
    exitsFileData = eobj.read()
    
    cobj = open(copyFile,"w")
    cobj.write(exitsFileData)
    
    # print(f"Data on Exits file {exitsFile}: \n",exitsFileData)
    
    # cobj = open(copyFile,"r")
    # copyFileData = cobj.read()
    # print(f"Copied File data {copyFile}: \n",copyFileData)
 

def main():
    border = "-" * 66
    print(border)
    print("-------------------- Marvellous Automation -----------------------")
    print(border)
    
    if(len(sys.argv) == 3):
        if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This application is used to perform copy content from one file to another")                 
            print("This is the automation script")
        elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
            print("Use the given script as")
            print("ScriptName.py exitsfilename copyfilename")
        else:
            exitsFile = sys.argv[1]
            copyFile = sys.argv[2]
            CopyFileContent(exitsFile,copyFile)
            print(f"Copy data from {exitsFile} to {copyFile} sucessfully")
            
            
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