#! /usr/bin/python3
# references:
# https://docs.python.org/zh-cn/3/howto/argparse.html
# https://docs.python.org/zh-cn/3/library/argparse.html#nargs
import argparse

# ArgumentParser 对象包含将命令行解析成 Python 数据类型所需的全部信息
parser = argparse.ArgumentParser(description='Process some integers.')

# add_argument: 给一个 ArgumentParser 添加程序参数信息
# 指定 ArgumentParser 如何获取命令行字符串并将其转换为对象
# 这些信息在 parse_args() 调用时被存储和使用
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('-s','--sum', dest='accumulate', 
                    action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
# FIXME: 调用参数的名称不可以改, 比如我希望可以支持下面的命令 
# python3 ./main.py 3 2 1 4 -s=max 如何实现呢???
# 在添加 action='store', nargs='?' 等参数后又会报错
# TypeError: 'str' object is not callable
# 似乎无法识别调用的函数, max被识别为了str, 无法调用


args = parser.parse_args()
# 此时, 返回一个具有 integers 和 accumulate 两个属性的对象
# 选项会以 - 前缀识别，剩下的参数则会被假定为位置参数:

print(args)
# Namespace(accumulate=<built-in function max>, integers=[3, 2, 1, 4])

print(args.accumulate(args.integers))
