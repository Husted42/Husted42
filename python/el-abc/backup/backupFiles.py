import os, sys
import shutil
import schedule
import time

src = 'C:/Users/alx/Documents/GitHub/code/python/el-abc/files/test01'
des = 'C:/Users/alx/Documents/GitHub/code/python/el-abc/backup/folder'

''' deletes existing folder and replace by a new one '''
def backup():
    if os.path.exists(des):
        shutil.rmtree(des)
    shutil.copytree(src, des)

schedule.every(10).seconds.do(backup)
schedule.every().thursday.do(backup)

''' Keeps the script running '''
while True:
    schedule.run_pending()
    time.sleep(1)