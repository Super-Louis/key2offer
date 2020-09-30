# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: clockwise_matrix.py
# Python  : python3.6
# Time    : 18-10-10 22:18

"""
题目二十九：顺时针打印
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
"""
def print_clockwise(matrix):
    # 1. 确定循环的条件(每次循环的初始坐标start,start)
    # 2. 确定打印每一步的条件
    if not matrix:
        return
    rows = len(matrix)
    columns = len(matrix[0])
    start = 0
    while columns > 2*start and rows > 2*start:
        print_circle(matrix, start, rows, columns)
        start += 1

def print_circle(matrix, start, rows, columns):
    endX = rows - start - 1
    endY = columns - start -1
    for i in range(start, endY+1):
        print(matrix[start][i])

    if endX > start:
        for i in range(start+1, endX+1):
            print(matrix[i][endY])

    if endX > start and endY > start:
        for i in range(endY-1, start-1, -1):
            print(matrix[endX][i])

    if endX >= start + 2 and endY > start:
        for i in range(endX-1, start, -1):
            print(matrix[i][start])

if __name__ == '__main__':
    print_clockwise([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
