
Marvellous Automation - Duplicate File Remover with Email Alert
---------------------------------------------------------------

Description:
----------------
This Python automation script scans a given directory, detects and deletes duplicate files,
and sends an automated email log report to a specified email address at scheduled intervals.

Features:
------------
- Scans the directory recursively to find duplicate files using MD5 checksum.
- Deletes all duplicates while retaining one copy of each.
- Generates a detailed log file with file paths and total count.
- Automatically emails the log to the provided email address.
- Supports scheduling using the `schedule` module.
- Handles errors gracefully and logs all results.

 How It Works:
-----------------
1. Run the script with:
   python Assignment22.py <TargetDirectory> <ScheduleTimeInMinutes> <ReceiverEmail>

2. The script:
   - Validates the input path
   - Searches for duplicate files
   - Deletes duplicates
   - Writes a .log file into a subfolder named MarvellousLog
   - Sends the .log file as an email attachment

3. The process repeats at every scheduled interval using the schedule module.

Command Line Usage:
-----------------------
python Assignment22.py <DirectoryPath> <ScheduleTimeInMinutes> <ReceiverEmail>

Example:
python Assignment22.py D:\MyData 5 myemail@example.com

Optional Flags:
- --h or --H : Display help message
- --u or --U : Display usage instructions

Output:
----------
- .log files saved in: TargetDirectory/MarvellousLog/
- Log includes:
  - Timestamp
  - List of duplicate files
  - Total files scanned and deleted
- Email includes:
  - Summary report
  - Log file as attachment

Email Configuration:
------------------------
- Uses Gmail SMTP (smtp.gmail.com) with starttls().
- Generate an App Password in Gmail for secure authentication.
- Update the following in your code:
  my_Email = "your_email@gmail.com"
  my_password = "your_app_password"

Module Requirements:
------------------------
- schedule
- smtplib
- email.message
- hashlib
- psutil (optional)
- os, time, datetime, sys

