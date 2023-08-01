import os
import shutil

curDir = os.getcwd()

fileTypes = []

files = os.listdir(os.getcwd())
files.remove('cleanDownload.py')
for elm in files:
    fileSplit = os.path.splitext(elm)
    if fileSplit[1] not in fileTypes: fileTypes.append(fileSplit[1])
    src = curDir + '/' + elm
    dest = curDir + '/' + (fileSplit[1])[1:]
    if (fileSplit[1])[1:] not in os.listdir(os.getcwd()): os.mkdir(dest, 0o666)
    print(src)
    print(dest, '\n\n')
    shutil.move(src, dest)
