#!/usr/bin/python3 
import os
import hashlib

DIR = []

def get_file_md5(file_name):
    m = hashlib.md5()
    with open (file_name, 'rb') as fobj:
        while True:
            data = fobj.read() # 4096 is what???
            if not data:
                break
            m.update(data)
    return m.hexdigest()
    # file_md5= hashlib.md5(data).hexdigest()

if __name__=="__main__":
    step=1
    rm = 1

    PATH = os.getcwd()
    for root,dirs,files in os.walk(PATH): # /mnt/c/Users/15517/Desktop/bojack hourseman2
        for file in files:
            DIR.append(os.path.join(root,file)) # get the file path

    SET = set()

    for i in DIR:
        temp = get_file_md5(i)
        print(str(step)+ ' ' + temp + '\n')
        step += 1
        if temp in SET:
            os.remove(i)
            rm += 1
            continue
        SET.add(temp)

    print('Total ' + str(step-1) + ' files, and already rm '+ str(rm-1) +' files .\nWish you have a good day :-)')