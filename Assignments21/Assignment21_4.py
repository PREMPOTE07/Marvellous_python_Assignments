import sys
from Module import EmailSentWithProcessLog
    
def main():
    border = "-" * 66
    print(border)
    print("-------------------- Marvellous Automation -----------------------")
    print(border, "\n")
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This application is used to display running process in log file and save in given directory and sent to given email")                 
            print("This is the directory automation script")
            
        elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
            print("Use the given script as")
            print("DirectoryCheckSum.py DirectoryName senderEmail")
            
    elif(len(sys.argv) == 3):
            DirectoryName = sys.argv[1]
            TOEmail = sys.argv[2]
            EmailSentWithProcessLog(DirectoryName,TOEmail)
            
    else:
            print("Invalid number of command line arguments")
            print("Use the given flags as: ")
            print("--h: used to display the help")
            print("--u: used to display the usage")    

    print(border, "\n")
    print("-----------------Thank You for using our script-------------------")
    print("-------------------- Marvellous Automation -----------------------")
    print(border)

if __name__ =="__main__":
    main()