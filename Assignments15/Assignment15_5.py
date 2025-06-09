import os
import sys
def main():
    count = 0
    if(len(sys.argv) == 2):
        FileName = sys.argv[1]
        str = input("Enter the string you wnat to search: ")
        ret = os.path.exists(FileName)
    
        if(ret == True):
            print("File exits")
            
            fobj = open(FileName,"r")
            data = fobj.read()
            
            for word in data.split():
                if word == str:
                    count = count + 1
             
            print("Frequncy of word",str,"is: ",count)        
            fobj.close()
     
        else:
            print("File Not exits")
    else:
        print("Enter at least two sys argument")

if __name__ == "__main__":
    main()