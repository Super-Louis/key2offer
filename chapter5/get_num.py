# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: get_num.py
# Python  : python3.6
# Time    : 19-1-21 22:12

"""
面试题44：数字序列中某一位的数字
题目：数字以012345678910...的格式序列化到一个字符序列中。
在这个序列中，第5位（从0开始计数）是5.第13位是1，第19位是4，
等等。请写一个函数，求任意第n位对应的数字
"""

def get_num(n):
    pre = 0
    count = 0
    for i in range(n+1):
        pre = count
        count += len(str(i))
        if count > n:
            break
    extra = n - pre
    return str(i)[extra]

if __name__ == '__main__':
    print(get_num(0))
