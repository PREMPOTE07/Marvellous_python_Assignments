import os
def main():
    print("Enter the file name :")
    
    FileName = input()
    
    ret = os.path.exists(FileName)
    
    if(ret == True):
        print("File exits")
    else:
        print("File Not exits")

if __name__ == "__main__":
    main()