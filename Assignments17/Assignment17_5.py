import schedule
import time
import datetime

def InsertTime():
    FileName= "Marvellous.txt"
    Fobj = open(FileName,"a")
    Fobj.write(str(datetime.datetime.now()) + "\n") # use append mode for not create new same file
def main():
     
    
    schedule.every(5).minutes.do(InsertTime)
    
    print("Application waiting .....")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()