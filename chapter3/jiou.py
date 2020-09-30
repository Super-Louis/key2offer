# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: jiou.py
# Python  : python3.6
# Time    : 19-1-11 21:38

"""
面试题21：调整数组顺序使奇数位于偶数前面
"""

def jiou(l):
    if not l:
        return None
    start = 0
    end = len(l) - 1
    while start < end:
        while l[start] % 2 == 1 and start < end:
            start += 1
        while l[end] % 2 == 0 and start < end:
            end -= 1
        l[start], l[end] = l[end], l[start]
    return l

if __name__ == '__main__':
    print(jiou([1,2,5,6]))