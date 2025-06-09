import schedule
import time
import datetime

def Display():
    print("Do Coding..!")

def main():
    schedule.every(30).minute.do(Display)
    
    print("Application waiting .....")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()