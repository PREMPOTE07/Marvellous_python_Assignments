import sys
import schedule
import time
import Module

    
def main():
    
    border = "-" * 66
    print(border)
    print("-------------------- Marvellous Automation -----------------------")
    print(border, "\n")
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This application is used to display running process in log file and save in given directory")                 
            print("This is the directory automation script")
            
        elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
            print("Use the given script as")
            print("Assignment22.py DeleteDirName scheduletime recieverMail")
            
    elif(len(sys.argv) == 4):
        print("Mail sending...")
        DeleteFilesDirName = sys.argv[1]
        scheduleTime = int(sys.argv[2])
        ToEmail = sys.argv[3]
        
        schedule.every(scheduleTime).minutes.do(Module.DuplicateFilesLogEmail,DeleteFilesDirName,ToEmail)
        
        while True:
            schedule.run_pending()
            time.sleep(1)
          
            
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