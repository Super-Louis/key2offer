# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: rev_array.py
# Python  : python3.6
# Time    : 19-2-28 19:40

"""
面试题11：旋转数组的最小数字
题目：把一个数组最开始的若干个元素搬到数组的末尾，
称之为数组的旋转。输入一个递增序列的数组的一个旋转，
输出旋转数组的最小元素。例如，数组{3,4,5,1,2}为
{1,2,3,4,5}的一个旋转，该数组的最小值为1
"""

def rev_array(l):
    if not l:
        return None
    if len(l) == 1:
        return l[0]
    low = 0
    high = len(l)-1
    while low < high:
        if l[low] < l[high]:
            return l[low]
        middle = int(1/2*(low+high))
        if l[middle] == l[low] == l[high]:
            min_ = find_min(l, low, high)
            return min_
        elif l[middle] >= l[low]:
            low = middle + 1
        elif l[middle] <= l[high]:
            high = middle
    return l[low]

def find_min(l, low, high):
    min_ = l[low]
    for i in l[low:high+1]:
        if l[i] < min_:
            min_ = l[i]
    return min_

if __name__ == '__main__':
    print(rev_array([1,0,1,1,1]))