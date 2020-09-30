# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: fib.py
# Python  : python3.6
# Time    : 19-1-3 23:25

def fib(n):
    # time: n的指数
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib_dp(n):
    # time: O(N)
    if n <= 0:
        return 0
    if n == 1:
        return 1
    fib_list = [0] * (n+1)
    fib_list[0] = 0
    fib_list[1] = 1
    for i in range(2, n+1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[n]
if __name__ == '__main__':
    print(fib(6))
    print(fib_dp(6))
