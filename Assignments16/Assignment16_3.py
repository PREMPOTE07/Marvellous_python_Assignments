import os

def main():
    print("Enter the file you want to create: ")
    
    FileName = input()
    
    fobj = open(FileName,"r")
    data = fobj.read()
    Wcount = 0
    for word in data.split():
        Wcount = Wcount + 1
        
    print("Words in given file is: ",Wcount)
    
    Ccount = 0
    for char in data:
        Ccount = Ccount + 1
    print("Characters in given file: ",Ccount)
    
    Lcount = 0
    for line in data.split("\n"):
        Lcount = Lcount + 1
    print("No of lines in given file: ",Lcount)

if __name__ == "__main__":
    main()