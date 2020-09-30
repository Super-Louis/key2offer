# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: max_profit.py
# Python  : python3.6
# Time    : 19-2-23 22:46

"""
面试题63：股票的最大利润
题目：假设把某股票的价格按照时间先后顺序存储在数组中，
请问买卖该股票一次可能获得的最大利润是多少？
例如，一只股票在某些时间节点的价格为{9,11,8,5,7,12,16,14}.
如果我们在价格为5时买入，在价格为16时卖出，则能收获最大利润11
"""

def max_profit(nums):
    if not nums:
        return 0
    max_ = 0
    min_ = nums[0]
    for i in range(1, len(nums)):
        max_ = max(max_, nums[i]-min_)
        min_ = min(min_, nums[i])
    return max_

if __name__ == '__main__':
    # print_prob(3)
    print(max_profit([9,11,8,5,7,12,16,14]))

