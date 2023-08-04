import os, sys
import shutil
import schedule
import time

path_ = os.getcwd()

def cleanFolder():
    print('cleaning')
    fileTypes = []
    files = os.listdir(os.getcwd())
    print(files)
    files.remove('cleanDownload.py')
    for elm in files:
        if (os.path.splitext(elm))[1] != '':
            fileSplit = os.path.splitext(elm)
            if fileSplit[1] not in fileTypes: fileTypes.append(fileSplit[1])
            src = path_ + '/' + elm
            dest = path_ + '/' + (fileSplit[1])[1:]
            print(src, dest)
            print((fileSplit[1])[1:])
            if (fileSplit[1])[1:] not in os.listdir(os.getcwd()): os.mkdir(dest, 0o666)
            print(src)
            print(dest, '\n\n')
            shutil.move(src, dest)

cleanFolder() #Run startup
schedule.every().hour.do(cleanFolder)

''' Keeps the script running '''
while True:
    schedule.run_pending()
    time.sleep(1)