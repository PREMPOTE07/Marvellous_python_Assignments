import os

def main():
    print("Enter the first file : ")
    FileName1 = input()
    print("Enter the second file which want to copy: ")
    FileName2 = input()
        
        
    fobj1 = open(FileName1,"w")
    data = input()
    fobj1.write(data)
    
    fobj1 = open(FileName1,"r")
    F1data = fobj1.read()
    
    fobj2 = open(FileName2,"w")
    fobj2.write(F1data)
    
    fobj2 = open(FileName2,"r")
    F2data = fobj2.read()
    
    print("File1 data: ",F1data)
    print("File2 data: ",F2data)
        

if __name__ == "__main__":
    main()