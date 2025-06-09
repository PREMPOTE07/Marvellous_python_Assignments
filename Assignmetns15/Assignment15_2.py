import os
def main():
    print("Enter the file name that you want to read:")
    
    FileName = input()
    
    ret = os.path.exists(FileName)
    
    if(ret == True):
        print("File exits")
        
        fobj = open(FileName,"r")
        
        data = fobj.read()
        
        print("Data in file: ",data[1])
        
        fobj.close()
    else:
        print("File Not exits")

if __name__ == "__main__":
    main()