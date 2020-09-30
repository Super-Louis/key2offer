# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: half_num.py
# Python  : python3.6
# Time    : 19-1-18 00:10

"""
面试题39：数组中出现次数超过一半的数
题目：数组中有一个数字出现的次数超过数组长度的一半，
请找出这个数字。例如，输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}.
由于数字2在数组中出现了5次，超过数组长度一半，因此输出2
"""

def find_half(l):
    """
    利用快速排序中的partition函数
    时间复杂度为O(N)??
    :param l:
    :return:
    """
    if not l:
        return None
    li = 0
    ri = len(l) - 1
    middle = int(1/2*(ri+1))
    i = partition(l, li, ri)
    while i != middle:
        if i < middle:
            i = partition(l, i+1, ri)
        else:
            i = partition(l, li, i-1)
    return l[i]

def partition(l, li, ri):
    if li >= ri:
        return None
    base = li
    while li < ri:
        # 先right, 后left！！！
        while l[ri] >= l[base] and li < ri:
            ri -= 1
        while l[li] <= l[base] and li < ri:
            li += 1
        l[li], l[ri] = l[ri], l[li]
    l[base], l[li] = l[li], l[base]
    return li

if __name__ == '__main__':
    l = [1,2,2,3,3,3,3,2,3]
    print(find_half(l))
