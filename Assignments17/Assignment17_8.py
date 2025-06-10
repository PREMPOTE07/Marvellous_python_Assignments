import schedule
import time
import datetime


def check_email():
    
   print("Cheking email ....")
   
   fname = open("Email Updates.log","a")
   
   fname.write(f"check email at {str(datetime.datetime.now())} \n")
   
   fname.close()
    
def main():
     
    schedule.every(10).seconds.do(check_email)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()
