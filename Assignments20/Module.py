import os
import hashlib
import time
import psutil
import smtplib
from email.message import EmailMessage
import datetime
# This Fuction is used for Display All files with given extension only in given directory
def DisplayFiles(DirName,exe):
    for FolderNames , SubFolderNames , FileNames in os.walk(DirName):
        count = 0
        for fname in FileNames:
            l = len(fname)
            if fname[l-1] == exe[3] and fname[l-2] == exe[2] and fname[l-3] == exe[1] and fname[l-4] == exe[0]:
                print(fname)
                count += 1
    if count == 0:
        print("Files not found")
    else:
        print("Display files sucessfully")
        
        

# This Funciton is used for replace file extensions
def replaceExtension(DirName,exe1,exe2):
    for FolderNames , SubFolderNames , FileNames in os.walk(DirName):
        for fname in FileNames:
            l = len(fname)
            # strings are immutable very in python imp for me
            if fname[l-1] == exe1[3] and fname[l-2] == exe1[2] and fname[l-3] == exe1[1] and fname[l-4] == exe1[0]:
                newName = f"{fname[0:-4]}{exe2}"
                old_path = os.path.join(FolderNames,fname)
                new_path = os.path.join(FolderNames,newName)
                os.replace(old_path,new_path)
    print("Replace Extensions successfully")
            
            
            
# This Function is used for copy all files from one directory to directory           
def copyFiles(src ,dst):
    # make destination directory
    if not os.path.exists(dst):
      os.mkdir(dst) # this function used for create directory
      
    # check destination directory is a abosulute path is not make it
    flag = os.path.isabs(dst)
    if(flag == False):
        dst = os.path.abspath(dst)
    
    for FolderNames , SubFolderNames , FilesNames in os.walk(src):
        for fname in FilesNames:
            src_path = os.path.join(src,fname)
            dst_path = os.path.join(dst,fname)
            isCopied = False
            if os.path.isfile(src_path):
                sobj = open(src_path,"rb") # binary mode supports evey file (e.g pdf , img ,txt)
                sdata = sobj.read()
                dobj = open(dst_path,"wb")
                dobj.write(sdata)
                isCopied = True
    if isCopied == True:            
        print(f"All files copied from {src} to {dst} directory successfully")
    else:
        print("Files not copied")
        
        
            
# This Function is used for copy all files with given extension only from one directory to directory           
def copyFilesExe(src ,dst,exe):
    # make destination directory
    if not os.path.exists(dst):
      os.mkdir(dst) # this function used for create directory
      
    # check destination directory is a abosulute path is not make it
    flag = os.path.isabs(dst)
    if(flag == False):
        dst = os.path.abspath(dst)
    
    for FolderNames , SubFolderNames , FilesNames in os.walk(src):
        for fname in FilesNames:
            if fname[-4:] == exe:
                src_path = os.path.join(src,fname)
                dst_path = os.path.join(dst,fname)
                isCopied = False
                if os.path.isfile(src_path):
                    sobj = open(src_path,"rb") # binary mode supports evey file (e.g pdf , img ,txt)
                    sdata = sobj.read()
                    dobj = open(dst_path,"wb")
                    dobj.write(sdata)
                    isCopied = True
    if isCopied == True:            
        print(f"All files copied from {src} to {dst} directory \n with extension {exe}successfully")
    else:
        print("Files not copied")        
    
        
# this function is used for cal checksum
   
def CalculateChecksum(path,BlockSize = 1024):
    fobj = open(path,"rb")
    
    hobj = hashlib.md5() 
    
    buffer = fobj.read(BlockSize) 
    
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)
        
    fobj.close()
    
    return hobj.hexdigest()
    
    
 # this funciton is used to display duplicates files in log file created at run time if not exits
 
def DisplayDuplicates(MyDict, DirName):
    import os
    import time

    # Ensure the directory exists
    if not os.path.exists(DirName):
        os.makedirs(DirName)  # creates directory if not exist

    timestamp = time.ctime().replace(" ", "").replace(":", "_")
    FName = f"DuplicatesFiles_{timestamp}_Log.log"
    FilePath = os.path.join(DirName, FName)

    with open(FilePath, "w") as fobj:
        border = "-" * 80
        fobj.write(border)
        fobj.write(f"\n Duplicates files at time {time.ctime()}\n")
        fobj.write(border + "\n")

        Result = list(filter(lambda x: len(x) > 1, MyDict.values()))
        DuplCount = 0
        SCcount = 0
        for value in Result:
            SCcount += 1
            for subvalue in value[1:]:
                DuplCount += 1
                fobj.write(f"{subvalue}\n")

        fobj.write(border + "\n")
        fobj.write(f"\n Value of Total Files  Scanned is: {SCcount}")
        fobj.write(f"Value of Duplicates Files is: {DuplCount}")
        fobj.write("\n" + border)

    return FilePath

    

        
       
   
   
# This funciton is used for find duplicates in directory

def FindDuplicates(DirectoryName):
    
    flag = os.path.isabs(DirectoryName)
    
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)
        
    flag = os.path.exists(DirectoryName)
    
    if(flag == False):
        print("The path is invalid")
        exit()
        
    flag = os.path.isdir(DirectoryName)
    
    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
    
    Duplicate = {}
    
    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):

        for fname in FileNames:
            filePath = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(filePath)
            
            if checksum in Duplicate:
                Duplicate[checksum].append(filePath)
            else:
                Duplicate[checksum] = [filePath]
    
    return Duplicate

# this function is used to delete duplicates files

def DeleteDuplicate(path="Marvellous"):
    MyDict = FindDuplicates(path)
    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    SCcount = 0  # total duplicate files found
    Delcnt = 0   # total deleted files

    for value in Result:
        SCcount += len(value)
        for subvalue in value[1:]:  # skip the first (keep one copy)
            try:
                os.remove(subvalue)
                Delcnt += 1
                # print("Deleted file:", subvalue)
            except Exception as e:
                print("Error deleting", subvalue, ":", e)

    return [SCcount, Delcnt]

    
    

 # this function is used for cal checksum of all files in folder
   
def CalChecksumOfAllFilesInFolder(DirectoryName , BlockSize = 1024):
    timestamp = time.ctime()
    flag = os.path.isabs(DirectoryName)
    
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)
        
    flag = os.path.exists(DirectoryName)
    
    if(flag == False):
        print("The path is invalid")
        exit()
        
    flag = os.path.isdir(DirectoryName)
    
    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
    
    for FolderNames , SubFolderNames , FileNames in os.walk(DirectoryName):
        for file in FileNames:
            filePath = os.path.join(DirectoryName,file)
            
            checksum = CalculateChecksum(filePath)
            
            print(f"ChekSum of file {file} is: {checksum}")
            
            
# this function is used for display running processes 

def ProcInfo():
    listProcess = []
    
    try:
        for proc in psutil.process_iter():
            info = proc.as_dict(attrs=['pid','name','username'])
            listProcess.append(info)   
    except Exception as e:
        print(e)
    
    
    return listProcess

# this funciton is used for display running process in log file with given folder name as an argument

def DisplayRunProcessInLog(dirName):
    
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")

    FileName = f"ProcessLog{timestamp}.log"
    FileName = os.path.join(dirName,FileName)
    fobj = open(FileName,"w")
    border = "-" * 80
    fobj.write(border +"\n")
    fobj.write("---------------------------------Marvellous Automation-----------------------------------")
    fobj.write("\n"+border +"\n")
     
    Arr = ProcInfo()
    
    for value in Arr:
        fobj.write(str(value) +"\n")
    
    
    fobj.write(f"\nfile is created at {time.ctime()}\n")
    fobj.write("\n"+border +"\n")
    
    return FileName


# this funciton is used for sent email with log file have running processes

def EmailSentWithProcessLog(dirName , toEmail):
    my_Email = "type your email"
    my_password = "email app password"
    mail_content = EmailMessage()
    
    mail_content['subject'] =""
    mail_content['from'] = my_Email
    mail_content['to'] = toEmail
    
    mail_content.set_content(f"This is the log file of Running Process in my pc creates ar {datetime.datetime.now()}")
    
    # create a folder for save process log files and write running processes content
    FileName = DisplayRunProcessInLog(dirName)
    
    # send created log file to given email
    ProcesslogFile = open(FileName,"rb")
    mail_content.add_attachment(ProcesslogFile.read() ,maintype ="Application" , subtype ="log", filename = FileName)
    
    # make and start connection for sending
    try:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_Email , password=my_password)
        
        connection.send_message(mail_content)
        connection.close()
    except Exception as e:
        print(e)
    
    ProcesslogFile.close()
    
    
# this function is used for sending main contains information of duplicate file at given schedule time

def DuplicateFilesLogEmail(dirName , toEmail):
    print("Mail sending...")
    
    LogDirectory = "MarvellousLog"
    
    if not os.path.exists(LogDirectory):
        os.mkdir(LogDirectory)
    
    LogDirectory = os.path.join(dirName,LogDirectory)
    
    myDict = FindDuplicates(dirName)
    
    FileName = DisplayDuplicates(myDict,LogDirectory)        
    count = DeleteDuplicate(dirName)
    
     #email logic
    my_Email = "type your email"
    my_password = "email app password"
    mail_content = EmailMessage()
    
    mail_content['subject'] =""
    mail_content['from'] = my_Email
    mail_content['to'] = toEmail
    
    mail_content.set_content(f" Starting Time of Scanning {datetime.datetime.now()} \n Total Files Scannes : {count[0]}\n Total deleted Duplicates Files : {count[1]}\n")
    
    
    # send created log file to given email
    DuplicateLog = open(FileName,"rb")
    mail_content.add_attachment(DuplicateLog.read() ,maintype ="Application" , subtype ="log", filename = FileName)
    
    # make and start connection for sending
    try:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_Email , password=my_password)
        
        connection.send_message(mail_content)
        connection.close()
    except Exception as e:
        print(e)
    
    DuplicateLog.close()
