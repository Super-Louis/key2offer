# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: matrix_path.py
# Python  : python3.6
# Time    : 18-9-28 23:28

"""
题目十二：矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径
"""

def matrix_path(matrix, m, n, str):
    # 矩阵中的路径，判断矩阵中是否存在字符串的路径
    # 采用回溯法, 递归求解
    """
    :param matrix: 矩阵
    :param m: 矩阵行数
    :param n: 矩阵列数
    :param str: 字符串
    :return: True/False
    """
    for i in range(m):
        for j in range(n):
            has_entered = [[False for _ in range(n)] for _ in range(m)]
            path_len = 0
            if has_path_core(matrix, i, j, str, m, n, has_entered, path_len):
                return True
    return False

def has_path_core(matrix, i, j, str, m, n, has_entered, path_len):
    if path_len == len(str): # base_line, 所有的字符均有对应路径节点
        return True
    has_path = False # has_path初始值为false, 不满足下一条件则直接为False
    if i in range(m) and j in range(n) and \
            matrix[i][j] == str[path_len] and has_entered[i][j] == False: # 满足条件时要进行递归
        path_len += 1
        has_entered[i][j] = True
        has_path = has_path_core(matrix, i-1, j, str, m, n, has_entered, path_len) or \
                   has_path_core(matrix, i+1, j, str, m, n, has_entered, path_len) or \
                   has_path_core(matrix, i, j-1, str, m, n, has_entered, path_len) or \
                   has_path_core(matrix, i, j+1, str, m, n, has_entered, path_len)
        if not has_path: # 该节点所有相邻节点均不能形成路径，则该节点无效，将对应entered置为false
            has_entered[i][j] = False
    return has_path

# --------------------------------------------------------------------------------------
def robot_path(m, n, k):
    # todo: 递归超过最大深度，采用栈实现
    # 机器人的运动范围查找
    """
    :param m: 矩阵行数
    :param n: 矩阵列数
    :param k: 阈值，行数及列数的书位置和应小于等于k
    :return: count
    """
    if m <= 0 or n <= 0 or k <= 0:
        return 0
    visited = [[False for _ in range(n)] for _ in range(m)]
    count = count_core(m, n, 0, 0, k, visited)
    return count

def count_core(m, n, i, j, k, visited):
    count = 0
    if check(m, n, i, j, k, visited):
        visited[i][j] = True
        count = 1 + count_core(m, n, i-1, j, k, visited) + \
                count_core(m, n, i+1, j, k, visited) + \
                count_core(m, n, i, j-1, k, visited) + \
                count_core(m, n, i, j+1, k, visited)
    return count

def check(m, n, i, j, k, visited):
    if i in range(m) and j in range(n) and not visited[i][j] and get_sum(i) + get_sum(j) <= k:
        return True
    return False

def get_sum(i):
    sum = 0
    while i:
        sum += i % 10
        i = i / 10
    return sum


if __name__ == '__main__':
    # print(matrix_path([["1","2","1"],["3","4","5"],["4","5","6"]], 3, 3, '451'))
    print(robot_path(36, 36, 20))