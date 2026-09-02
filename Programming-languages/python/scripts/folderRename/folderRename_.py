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

##### ----- Functions ----- #####
'''Extract casenumber '''
def extract(inp):
    case = re.search(r'\d\d\d\d\d', inp)
    return case[0]

''' Renames all files in directory and subdirectories '''
def changeFile(inp):
    for subdir, dirs, files in os.walk(curDir):
        for file in files:
            file_redacted = file.replace("XXXXX", extract(inp))
            os.chdir(subdir)
            os.rename(file, file_redacted)

def changeDir(inp):
    for subdir, dirs, files in os.walk(curDir):
        for dir in dirs:
            print(dir)
            dir_redacted = dir.replace("XXXXX", extract(inp))
            print(dir_redacted)
            os.chdir(subdir)
            os.rename(dir, dir_redacted)

##### ----- Calls ----- #####
changeFile(input)
changeDir(input)