import os
import sys
def main():
    if(len(sys.argv) == 3):
        FileName = sys.argv[1]
        exitFile = sys.argv[2]
        ret = os.path.exists(exitFile)
    
        if(ret == True):
            print("File exits")
            
            fobj = open(exitFile,"r")
            data1 = fobj.read()
                        
            f2obj = open(FileName,"r")
            data2 = f2obj.read()
            
        
            if data1 != data2:           # comapare data in both files
                print("Failure")
            else:
                print("Sucess")
            
            fobj.close()
            f2obj.close()
        else:
            print("File Not exits")
    else:
        print("Enter at least two sys argument")
        print("New file_name Exiting file_name")

if __name__ == "__main__":
    main()