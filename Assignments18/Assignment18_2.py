import os
def main():
    print("Enter the file name that you want to display content : ")
    
    FileName = input()
    
    ret = os.path.exists(FileName)
    
    if(ret == True):
        print(f"{FileName} is exits in current directory")
        Fobj = open(FileName,'r')
        
        data = Fobj.read()
        
        print(f"Contents on {FileName}:\n",data)
    else:
        print("File does not exits in current directory")

if __name__ =="__main__":
    main()
    