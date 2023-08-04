import os, sys
import shutil
import schedule
import time

folderLst = ['Pictures', 'Text', 'MicrosoftDocuments', 'Compressed', 'Data', 'Executable', 'Programming', 'Other']
Pictures = ['jpeg', 'png', 'gif', 'tiff', 'tif', 'psd', 'eps', 'ai', 'indd', 'raw', 'bmp', 'jpg', 'svg', 'webp']
Text = ['pdf', 'txt']
MicrosoftDocuments = ['doc', 'docx', 'rtf', 'xls', 'xlsx', 'ppt', 'pptx', 'xps']
Compressed = ['7z', 'arj', 'deb', 'pkg', 'rar', 'rpm', 'tar.gz', 'z', 'zip']
Data = ['csv', 'dat', 'db', 'dbf', 'log', 'mdb', 'sav', 'sql', 'tar', 'xml']
Executable = ['apk', 'bat', 'bin', 'cgi', 'pl', 'exe', 'gadget', 'jar', 'msi', 'wsf']
Programming  = ['c', 'cgi', 'class', 'cpp', 'cs', 'h', 'java', 'php', 'py', 'sh', 'swift', 'vb', 'fsx', 'fs', 'fsi', 'fsproj', 'ipynb']

path_ = 'C:/Users/alx/Documents/GitHub/code/python/el-abc/cleanDownload'

def categorize(inp):
    if inp in Pictures: return 'Pictures'
    if inp in Text: return 'Text'
    if inp in MicrosoftDocuments: return 'MicrosoftDocuments'
    if inp in Compressed: return 'Compressed'
    if inp in Data: return 'Data'
    if inp in Executable: return 'Executable'
    if inp in Programming: return 'Programming'
    return 'Other'

def cleanFolder():
    fileTypes = [] #List of all distinct file types in dir 
    files = os.listdir(path_) #List of all files in dir
    files.remove('cleanDownload.py')
    files.remove('cleanDownload_.py')
    print(1, files)
    for elm in files:
        print('Element in question: ', elm, '\n\n\n')
        foldername = ''
        if (os.path.splitext(elm))[1] != '': #Check if folder
            print('(after if) elm = ', elm, os.path.splitext(elm))
            fileSplit = os.path.splitext(elm)
            filetype = (fileSplit[1])[1:] #Filetype minus .
            if fileSplit[1] not in fileTypes: fileTypes.append(fileSplit[1]) #Get distinct
            print(2, fileSplit[1])
            foldername = categorize(filetype)
        else:
            if elm not in folderLst:
                print(3, elm) 
                foldername = 'Folder'
        if foldername != '':
            print(4, 'foldername = ', foldername)
            src = path_ + '/' + elm
            dest = path_ + '/' + foldername 
            if foldername not in os.listdir(path_): os.mkdir(dest, 0o666)
            # if os.path.exists(dest):
            #     shutil.rmtree(dest)
            shutil.move(src, dest)

cleanFolder() #Run startup
schedule.every().hour.do(cleanFolder)

''' Keeps the script running '''
while True:
    schedule.run_pending()
    time.sleep(1)