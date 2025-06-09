import os

def main():
    print("Enter the file you for enters numbers on new line: ")
    FileName = input()
    
        
        
    fobj = open(FileName,"r")
    data = fobj.read()
    for line in data.split("\n"):
        count = 0
        for word in line.split():
            count += 1
        if count > 6:
            print(line)
        

if __name__ == "__main__":
    main()