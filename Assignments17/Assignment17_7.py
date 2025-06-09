import schedule
import time
import datetime
import os
import shutil

Source_File = "original_data.txt"
Backup_File = "backup_data.txt"
Log_File = "backup_log.txt"
def BackupFile():
    
    if os.path.exists(Source_File):
        shutil.copy(Source_File,Backup_File)
        log_time = f"{datetime.datetime.now()}: Backup Sucessfule\n"
    
    else:
        log_time = "File not found"
        
    log = open(Log_File,"a")
    log.write(log_time)
    
def main():
     
    schedule.every().hour.do(BackupFile)
    
    print("Backup running....")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()