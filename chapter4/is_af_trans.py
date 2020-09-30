# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: is_af_trans.py
# Python  : python3.6
# Time    : 19-1-11 23:51

"""
题目33：二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同
"""

def is_result(l):
    # 后序遍历根节点在最后
    # 前面小于根节点的为左节点
    # 剩下的理论上都为右节点，即大于根节点
    # 不满足该条件的不是后序遍历
    # todo：边界条件是否正确？？
    if len(l) <= 1:
        return True
    root = l[-1]
    found_larger = False
    for i in range(len(l)-1):
        if l[i] > root:
            found_larger = True
            break
    # 没有比root大的i要加1
    i = i if found_larger else i + 1
    low = l[:i]
    gre = l[i:len(l)-1]
    for g in gre:
        if g < root:
            return False
    return is_result(low) and is_result(gre)

if __name__ == '__main__':
    # print(jiou([2]))
    print(is_result([1,2,3]))
