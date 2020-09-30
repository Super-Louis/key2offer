# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: shaizi.py
# Python  : python3.6
# Time    : 19-2-23 22:03

"""
面试题60：n个骰子的点数
题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。
输入n，打印出s的所有可能的值出现的概率。
"""

def print_prob(n):
    if not n:
        return
    probs = [0] * (5*n+1)
    total = 6 ** n
    i = 0
    sum = 0
    get_freq(n, probs, i, sum)
    print('value', 'count', 'prob')
    total_prob = 0
    for i, c in enumerate(probs):
        prob = c/total
        total_prob += prob
        print(i+n, c, prob)
    print('total prob', total_prob)

def get_freq(n, probs, i, sum):

    if i == n:
        probs[sum-n] += 1
        return
    for j in range(1, 7):
        get_freq(n, probs, i+1, sum+j)

if __name__ == '__main__':
    print_prob(3)
