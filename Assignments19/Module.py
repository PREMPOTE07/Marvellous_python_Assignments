import os

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
    
        
   