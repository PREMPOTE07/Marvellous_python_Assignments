import os

def main():
    print("Enter the file you want to read and display data: ")
    
    FileName = input()
    
    fobj = open(FileName,"r")
    data = fobj.read()
    print("Data of students: ",data)
    

if __name__ == "__main__":
    main()