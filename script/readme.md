Maybe every in python is simple. But not easy! See my [gist](./notes.ipynby) about it.

Here are exercise file.

```python
#Python 可以同一行显示多条语句，方法是用分号 ; 分开，如：
help(print)
a = 8
b = 3
print(a)
print(b)
print(a, b)
c = a // b  # 表示整除
d = a / b  # 表示保留小数的除法
print(c, "&", d)
e = 8
f = 3
print(e**f)  # 表示e的f次方
if (e == f):
    print("true")
else:
    print('false')
if e is not f:  # 两种效果等效-> is (not) & ==,!=
    print('true')
else:
    print('false')

print(a and b)
ai = [1, 2, 3, 4, 5, 6]
bi = ai * 2  # 重复序列
ai += bi  # 连接序列
print(bi, '&', ai)
#  字符串
stri = 'son of bitch!'
print('\\\'\"\b\000\n\v\t\r\f\012\x0a')
print('over\n')
print(stri[-2:-1])
if ('f ' in stri):
    print("stri, Yes!!!")
for i in range(5,10):
    print(i)
for a in range(10):
    print(a**10)
print(10**10)
# #####################formay######################
# I decide to sell my soul to this dirty world beacause there're no thing is perfect, also everything about me. Maybe it would be a sigh in the end but damn right, haha.
print("{}" "{}".format("Hello", "World"))
print("{1} + {0} + {1}".format("hello", "world"))
print("Hello:{name}".format(name='lufenghua'))
print("pd={:.2f}".format(3.1415926))
print("{:0>5d}".format(10))
print("{value:#x}".format(value=25))  # HEX
# ######################list########################
l = list()
p = list(l)
pi = []
li = [1001, 211, 388, 404]
x = input()  # 输入字符串
# ###调用第三方库import sys sys.stdin（）; address: https://blog.csdn.net/shuwenting/article/details/79711869
l.append(x)
print(l)
l.insert(1, 3)
l.remove(3)
print(l)
l.pop()
print(l)
li.sort()
print(li)
# #####################range##########################
# r=range(10)
# r=range(5,15)
# r=range(0,10,2)
r = range(100, 10, -2)
lii = list(range(100, 150, 5))
print(lii)
# ####################dict############################
# 键值对集合
# d = dict
# d = {}
# d = dict(one=1, two=2, three=3)
d = {'one': 1, 'two': 2, 'three': 3}
l2 = list(d)
l2 = list(d.values())
print(d)
print(l2)
# ##################Tuple Set#########################
t = (1, 2)
# t=tuple(1,2,3,3,4,5)
# 一个不可变的列表 函数多返回值,dict的键
s = {1, 2, 3}
sa = set(s)
sa.add(4)
saa0 = s & sa
print(saa0)
saa1 = s | sa
print(saa1)
saa2 = sa - s
print(saa2)
# #######################异常##########################
try:
    i=int('a')
except Exception as e:
    print(e)
import errno
import os


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

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



```
