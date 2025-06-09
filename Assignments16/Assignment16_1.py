import os

def main():
    print("Enter the file you want to create: ")
    
    FileName = input()
    
    fobj = open(FileName,"w")
    print("Enter 5 students name data")
    Data = input()
    fobj.write(Data)
    
    fobj = open(FileName,"r")
    data = fobj.read()
    print("Data of students: ",data)
    

if __name__ == "__main__":
    main()