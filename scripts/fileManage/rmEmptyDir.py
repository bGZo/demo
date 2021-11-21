#!/usr/bin/python3
import os

localDir = []
PATH = os.getcwd()
for root,dirs,files in os.walk(PATH):
        for dir in dirs:
            localDir.append(os.path.join(root,dir))

for i in localDir:
     if not os.localDirdir(i):
         os.rmdir(i)
# if dir is empty, then rm it!