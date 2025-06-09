import schedule
import time
import datetime

def Display():
    print("Namaskar...")
    print(datetime.datetime.now())

def main():
    schedule.every().day.at("09:00").do(Display)
    
    print("Application waiting .....")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()