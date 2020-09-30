# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: max_value.py
# Python  : python3.6
# Time    : 19-1-23 11:53

"""
面试题47：礼物的最大价值
题目：在一个m*n的棋盘的每一格都放有一个礼物，
每个礼物都有一定的价值（价值大于0）。你可以从
棋盘的左上角开始拿格子里的礼物，并每次向右或者
向下移动一格，直到到达棋盘的右下角。给定一个棋盘
及其上面的礼物，请计算你最多能拿到多少价值的礼物
"""

def max_value(M):
    """
    递归公式：value[i][j] = max(value[i-1][j],value[i][j-1]) + m[i][j]
    :param M:
    :return:
    """
    if not M:
        return 0
    r = len(M)
    c = len(M[0])
    value = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                value[i][j] = M[i][j]
            elif i == 0:
                value[i][j] = value[i][j-1] + M[i][j]
            elif j == 0:
                value[i][j] = value[i-1][j] + M[i][j]
            else:
                value[i][j] = max(value[i][j-1], value[i-1][j]) + M[i][j]
    return value[r-1][c-1]

if __name__ == '__main__':
    M = [[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]
    print(max_value(M))
