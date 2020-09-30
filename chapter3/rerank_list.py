# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: rerank_list.py
# Python  : python3.6
# Time    : 18-10-2 18:26

"""
题目二十一：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分
"""
def rerank_list(li):
    l = 0
    r = len(li) - 1
    while l < r:
        while li[l] % 2 == 1 and l < r:
            l += 1
        while li[r] % 2 == 0 and l < r:
            r -= 1
        li[l], li[r] = li[r], li[l]

    return li

if __name__ == '__main__':
    print(rerank_list([2,4,6,8,3]))