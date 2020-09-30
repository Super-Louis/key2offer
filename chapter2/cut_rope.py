# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: cut_rope.py
# Python  : python3.6
# Time    : 18-9-30 00:03

"""
题目十四：剪绳子
给你一根长度为n的绳子，请把绳子剪成m段；
每段绳子的长度为k0,k1,k2,...km
请问K0*K1*K2...*Km的最大值为多少
"""
def cut_rope(n):
    # 这几种情况下不剪是最大的，因此要单独返回
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    f_n = [0 for _ in range(n+1)]
    f_n[0] = 0
    f_n[1] = 1
    f_n[2] = 2
    f_n[3] = 3
    for i in range(4, n+1): # 从长度为0的绳子到长度为n的绳子
        max = 0
        for j in range(1, int(i/2)+1): # 对于长度为i的绳子，任意切割点
            product = f_n[j] * f_n[i-j]
            if product > max:
                max = product
        f_n[i] = max
    return f_n[n]

if __name__ == '__main__':
    print(cut_rope(8))