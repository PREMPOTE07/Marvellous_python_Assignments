import schedule
import time
import datetime

def Print():
    print("Current time is: ",datetime.datetime.now())
    print("Jay Ganesh")

def main():
    schedule.every(2).seconds.do(Print)
    
    print("Application waiting .....")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()