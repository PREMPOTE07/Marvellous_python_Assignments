import os
def main():
    
    
    print("Enter the file name that you want to check it exits or not in current directory: ")
    
    FileName = input()
    
    ret = os.path.exists(FileName)
    
    if(ret == True):
        print("File exits in current directory")
    else:
        print("File does not exits in current directory")

if __name__ =="__main__":
    main()
    