##### ----- Imports ----- #####
import os, sys
import shutil
import re

##### ----- Initialize ----- #####
input = sys.argv[1]

source = os.getcwd() + "/Ny sagsmappe"
destination = os.getcwd() + '/' + input

''' Copies 'ny sagsmappe' '''
def copy(src, dest):
    shutil.copytree(src, dest)

copy(source, destination)

##### ----- Variables ----- #####
os.chdir(destination)
curDir = os.getcwd()
    
##### ----- Function ----- #####
'''Extract casenumber '''
def extract(inp):
    case = re.search(r'\d\d\d\d\d', inp)
    return case[0]

''' Renames the 'XXXXX' part of all folders/files in closest subdirectories '''
def changeFolder(li, inp):
    if len(li) == 0: return None
    fileLst = li
    
    curFile = os.path.splitext(fileLst[0])
    if curFile[1] == '':
        os.chdir(fileLst[0])
        for elm in os.listdir(os.getcwd()):
            elm_redacted = elm.replace("XXXXX", extract(inp))
            os.rename(elm, elm_redacted)
        fileLst.pop(0)
        os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
        changeFolder(fileLst, inp)
    else:
        fileLst.pop(0)
        changeFolder(fileLst, inp)

''' Renames all files in directory and subdirectories '''
def changeFile(inp):
    for subdir, dirs, files in os.walk(curDir):
        for file in files:
            file_redacted = file.replace("XXXXX", extract(inp))
            os.chdir(subdir)
            os.rename(file, file_redacted)

##### ----- Calls ----- #####
changeFolder(os.listdir(destination), input)
changeFile(input)