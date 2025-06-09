import os

def main():
    print("Enter the file you for enters numbers on new line: ")
    FileName = input()
    
    fobj = open(FileName,"w")
    print("Enter 10 numbers: ")
    for i in range(10):
        data = int(input())
        fobj.write(str(data) + "\n")
        
        
    fobj = open(FileName,"r")
    data = fobj.read()
    print("Numbers are: ",data)

if __name__ == "__main__":
    main()