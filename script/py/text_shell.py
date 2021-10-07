# coding=utf-8
# import os
# import shutil
# address: https://www.cnblogs.com/iois/p/7258686.html
# address: https://www.jianshu.com/p/aad05356ca3f
# address: https://www.cnblogs.com/jhao/p/7243043.html
# address: https://blog.csdn.net/d1240673769/article/details/82802521
# address: https://zhuanlan.zhihu.com/p/56909212
# address: https://blog.csdn.net/LZGS_4/article/details/50371030
# runoop: https://www.runoob.com/python/os-file-methods.html
############################## text ######################################
# string = os.getcwd()
# string1 = os.path.basename(string)
# string2 = os.path.abspath(string)
# print(string)
# print(string1)
# print(string2)
# print("Hello world")
# sum = 0
# i = 0
# for i in range(0, 5):
#     sum += 1 
# print(sum)
# path_111 = os.getcwd()
# print(path_111)
# if os.path.isdir(path_111):
#     print("it's a directory")
# elif os.path.isfile(path_111):
#     print("it's a normal file")
# else:
#     print("it's a special file(socket,FIFO,device file)")
############################## over ######################################
# def digv(Selfpath):
#     if os.path.isfile(Selfpath):
#         file_pwd = Selfpath
#         return file_pwd
#     else:
#         rootdir = os.getcwd()
#         list = os.listdir(rootdir)
#         for ii in range(0, len(list)):
#             path_1 = os.path.join(rootdir, list[ii])
#             digv(path_1)
#             print(path_1)
# rdir = os.getcwd()
# list = os.listdir(rdir)
# # os.makedirs(fpath)
# for j in range(0, len(list)):
#     path_temp = os.path.join(rdir, list[j])
#     path_mv = digv(path_temp)
#     if os.path.isdir(path_mv):
#         print("it's a directory")
#     elif os.path.isfile(path_mv):
#         print("it's a normal file")
#     else:
#         print("it's a special file(socket,FIFO,device file)")
# RecursionError: maximum recursion depth exceeded while calling a Python object


# def isDigit(ch):
#     return re.search()


# ch = "1"
# print(int(isDigit(ch)))


