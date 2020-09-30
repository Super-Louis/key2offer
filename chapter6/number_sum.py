# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: number_sum.py
# Python  : python3.6
# Time    : 19-1-31 10:36

# 面试题57：和为s的数字
"""
题目一：和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，
使得他们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
"""
def find_sum(l, t):
    if not l:
        return None
    left = 0
    right = len(l) - 1
    while left < right:
        if l[left] + l[right] == t:
            return l[left], l[right]
        elif l[left] + l[right] > t:
            right -= 1
        else:
            left += 1
    return None

"""
题目二：和为s的连续正数序列
输入一个正数s，打印出所有和为s的连续正数序列
（至少包含两个数）。例如，输入15，由于1+2+3+4+5=4+5=7+8=15，
所以打印出3个连续序列1~5,4~6和7~8
"""
def find_sum2(t):
    if t <= 2:
        return []
    l, r = 1, 2
    sum = 3
    res = []
    while l < int((1+t)/2):
        if sum == t:
            res.append((l, r))
            r += 1
            sum += r
        elif sum < t:
            r += 1
            sum += r
        else:
            sum -= l
            l += 1
    return res

if __name__ == '__main__':
    print(find_sum([1,2,3],6))
    print(find_sum2(6))
