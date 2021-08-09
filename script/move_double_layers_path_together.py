#!/usr/bin/python3 
import os
import shutil
import time

PATH = os.getcwd()
g = os.walk(PATH) #os.walk(r'/mnt/c/Users/15517/Pictures/pic')

# if you write latter.
#
# 1. i am run wsl2, so `C:\Users\15517\Pictures\pic` is not suitting me.
#    should use the mount path, such as `/mnt/c/Users/15517/Pictures/pic`
#
# 2.  char `r` before path is important, or will result
#     (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: 
#     truncated \UXXXXXXXX escape [duplicate] <generator object walk at 0x7f067f9a9820>
#
#     so Just put r before your normal string it converts normal string to raw string:
#     And could put other char like 
#     - u/U: unicode String [defult]
#     - r/R: raw String
#     - b: bytes String
#     or pandas.read_csv("C:/Users/DeePak/Desktop/myac.csv")
#     or pandas.read_csv("C:\\Users\\DeePak\\Desktop\\myac.csv")
#     refer to: 
#         - https://medium.com/@zuokun.ouyang/python-%E5%AD%97%E7%AC%A6%E4%B8
#         %B2%E5%89%8D%E9%9D%A2%E5%8A%A0-u-r-b-%E7%9A%84%E5%90%AB%E4%B9%89-1a93e35de13
#         - https://stackoverflow.com/questions/37400974/
#         unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca

LIST = []

# walk in list:
# - for i in list:
# - for i in range(len(list)):
# - for i, val in enumerate(list):
# - for i, val in enumerate(list, 2):
# - refer to
#     - https://www.cnblogs.com/pizitai/p/6398276.html

step=0

for root,dirs,files in g:
    for file in files:
        LIST.append(os.path.join(root,file)) 


# for root,dirs,files in os.walk(r"D:\test"):
#     for file in files:
#         print(root) # 获取文件所属目录
#         print(os.path.join(root,file))# 获取文件路径

# for root,dirs,files in os.walk(r"D:\test"):
#     for dir in dirs:
#         print(dir) #获取目录的名称
#         print(os.path.join(root,dir)) #获取目录的路径

# # 递归获取该目录下所有的文件名称和目录名称
# def get_file_path(root_path,file_list,dir_list):
#     dir_or_files = os.listdir(root_path)
#     for dir_file in dir_or_files:
#         dir_file_path = os.path.join(root_path,dir_file)
#         if os.path.isdir(dir_file_path): # 判断 文件/路径
#             dir_list.append(dir_file_path)
#             get_file_path(dir_file_path,file_list,dir_list)
#         else:
#             file_list.append(dir_file_path)

# walk all file, so the method is like
#     os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
    
# top − Each directory rooted at directory, yields 3-tuples, i.e.(dirpath, dirnames, filenames)
# topdown − If optional argument topdown is True or not specified, 
# directories are scanned from top-down. If topdown is set to False, directories are scanned from bottom-up.
# onerror − This can show error to continue with the walk, or raise the exception to abort the walk.
# followlinks − This visits directories pointed to by symlinks, if set to true.

# refer to:
# - https://www.tutorialspoint.com/python/os_walk.htm
# - https://blog.csdn.net/sinat_29957455/article/details/82778306

newDir = str(time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))) # new dir

# too fast can not to do well???
# - time
#     - %y 两位数的年份表示（00-99）
#     - %Y 四位数的年份表示（000-9999）
#     - %m 月份（01-12）
#     - %d 月内中的一天（0-31）
#     - %H 24小时制小时数（0-23）
#     - %I 12小时制小时数（01-12） 
#     - %M 分钟数（00=59）
#     - %S 秒（00-59）
#     - %a 本地简化星期名称
#     - %A 本地完整星期名称
#     - %b 本地简化的月份名称
#     - %B 本地完整的月份名称
#     - %c 本地相应的日期表示和时间表示
#     - %j 年内的一天（001-366）
#     - %p 本地A.M.或P.M.的等价符
#     - %U 一年中的星期数（00-53）星期天为星期的开始
#     - %w 星期（0-6），星期天为星期的开始
#     - %W 一年中的星期数（00-53）星期一为星期的开始
#     - %x 本地相应的日期表示
#     - %X 本地相应的时间表示
#     - %Z 当前时区的名称
#     - %% %号本身
# - string & int
#     - str(12)10进制string
#     - hex(12)16进制string
#     - int('12', 16)
#     - int('12',(10))
# - refer
#     - https://www.cnblogs.com/kerwinC/p/5760811.html

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