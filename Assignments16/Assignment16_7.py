import os
def main():
    print("Enter the file you want display marks of student above 75: ")
    FileName = input()
    
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        data = fobj.read()
        
        for line in data.split("\n"):
            
            parts = line.split()
            
            if(len(parts) == 2):
                name = parts[0]
                marks = parts[1]
                if int(marks) >= 75:
                  print("Name:",name,"Marks:",marks)
                    
if __name__ == "__main__":
    main()