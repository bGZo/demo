#!/usr/bin/python3 
import os
import shutil
import time

PATH = os.getcwd()
g = os.walk(PATH) 
LIST = []

step=0

for root,dirs,files in g:
    for file in files:
        LIST.append(os.path.join(root,file)) 


newDir = str(time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))) # new dir

os.mkdir(newDir)
newDir = PATH + newDir 

for i in LIST:
    try:
        shutil.move(i, newDir)
    except:
        os.rename(i, str(step)+i) # name is repeat, so rename it!
        step += 1

if step != 0:
    print('Tatal rename ' + str(step) + '.')
else: 
    print('All works down well.')