#procInfo.py
from Module import ProcInfo
    
    
def main():
    border = "-" * 80
    print(border)
    print("--------------------------Marvellous Automation Script--------------------------")
    print(border)
    
    Arr = ProcInfo()
    
    for value in Arr:
        print(f"Name : {value['name']}  PID: {value['pid']}" )
    
    border = "-" * 80
    print(border)
    print("---------------------------Thanks For Using Script-----------------------------")
    print(border)

if __name__ =="__main__":
    main()