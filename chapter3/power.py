# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: power.py
# Python  : python3.6
# Time    : 18-10-2 16:16

"""
题目十六：数值的整数次方
实现函数power, 求base的n次方
"""

def power(base, exp):
    # 代码完整性
    if base == 0 and exp < 0:
        raise RuntimeError
    if base == 0 and exp >= 0:
        return 0
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp == -1:
        return 1.0/base
    # 包含exp取负值的情况
    if exp % 2 == 0:
        result = power(base, exp/2)
        return result * result
    else:
        result = power(base, (exp-1)/2)
        return result * result * base

if __name__ == '__main__':
    print(power(-2, 3))