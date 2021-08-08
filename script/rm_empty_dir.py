#!/usr/bin/python3
import os

LIST = []

PATH = os.getcwd()

for root,dirs,files in os.walk(PATH):
        for dir in dirs:
            LIST.append(os.path.join(root,dir))

for i in LIST:
     if not os.listdir(i):
         os.rmdir(i)
# if dir is empty, then rm it!