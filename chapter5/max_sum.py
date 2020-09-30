# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: max_sum.py
# Python  : python3.6
# Time    : 19-1-21 20:06

"""
面试题42：连续子数组的最大和
题目：输入一个整型数组，数组里有正数也有负数。
数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。要求时间复杂度为O(N)
"""

def max_sum(l):
    if not l:
        return None
    ms = l[0]
    cs = l[0]
    for i in range(1, len(l)):
        # 先判断是否小于等于0，为0时先将当前和设为0，再加当前值
        # 接着判断当前值与历史最大值
        if cs <= 0:
            cs = 0
        cs += l[i]
        if cs >= ms:
            ms = cs

    return ms

if __name__ == '__main__':
    print(max_sum([1,2,3]))
