import os
def main():
    print("Enter file name want to remove blank lines: ")
    
    FileName = input()
    
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        data = fobj.readlines()
        
        fobj = open(FileName,"w")
    
        for line in data:
            if line.strip():
                fobj.write(line)
        fobj.close()

if __name__ =="__main__":
    main()