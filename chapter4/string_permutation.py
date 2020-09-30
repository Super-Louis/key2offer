# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: string_permutation.py
# Python  : python3.6
# Time    : 19-1-16 11:28

"""
面试题38：字符串的排列
题目：输入一个字符串，打印出该字符串中字符的所有排列。
例如，输入字符串abc，则打印出由字符a/b/c所能排列出来
的所有字符串abc, acb...
"""

def permute(string):
    i = 0
    result = []
    sl = list(string)
    if not string:
        return []
    def permutation(sl, i):
        if len(sl) == i:
            result.append(''.join(sl))
            return
        for j in range(i, len(sl)):
            temp = sl[:]
            # 每次将第一个字符分别与后续字符交换
            temp[i], temp[j] = temp[j], temp[i]
            permutation(temp, i+1)
    permutation(sl, i)
    return result

if __name__ == '__main__':
    print(permute('cfg'))

