import schedule
import time
import datetime

def Display():
    print("Current time is: ",datetime.datetime.now())

def main():
    schedule.every(1).minute.do(Display)
    
    print("Application waiting .....")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()