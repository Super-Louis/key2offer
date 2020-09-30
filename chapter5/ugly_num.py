# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: ugly_num.py
# Python  : python3.6
# Time    : 19-1-24 21:51

"""
面试题49：丑数
题目：我们把只包含因子2，3和5的数称为丑数。
求按从小到大的顺序的第1500个丑数。例如，6,8
都是丑数，但14不是，因为它包含因子7.
习惯上我们把1当做第一个丑数
"""

def ugly_num(n):
    if not n:
        return None
    nums = [1]
    i2=i3=i5=0
    for _ in range(1, n):
        last = nums[-1]
        while 2*nums[i2] <= last:
            i2 += 1
        num2 = 2*nums[i2]
        while 3*nums[i3] <= last:
            i3 += 1
        num3 = 3*nums[i3]
        while 5*nums[i5] <= last:
            i5 += 1
        num5 = 5*nums[i5]
        num = min(num2,num3,num5)
        nums.append(num)
    return nums[-1]

if __name__ == '__main__':
    print(ugly_num(1500000))
