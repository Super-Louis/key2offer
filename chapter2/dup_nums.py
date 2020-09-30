# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: dup_nums.py
# Python  : python3.6
# Time    : 18-9-22 23:54

"""
题目一：找出数组中的重复元素
在一个长度为n的数组里的所有数字都在0~n-1的范围内。
数组中的某些数字是重复的，但不知道有几个重复数字，
也不知道每个数字重复了几次。请找出数组中任意一个重复数字
"""

def dum(nums):
    """
    nums为[0, n-1]范围内的数字组成的数组（n为数组长度）
    输出nums中的重复数字
    方法1：考虑到数字的范围，进行排序 O(n)
    方法2：不考虑数字范围，直接排序后判重 O(nlogn)
    方法3：另外定义一个字典，计数 O(n),O(n)
    :param nums:
    :return:
    """
    dums = set()
    if not nums: # 边界条件，时刻判断是否为空！！！
        return []
    for i in range(len(nums)):
        while i != nums[i]:
            if nums[i] == nums[nums[i]]:
                dums.add(nums[i])
                break
            else:
                index = nums[i] # 不能直接用nums[i]，因为nums[i]会发生变化
                nums[i], nums[index] = nums[index], nums[i]
    return list(dums)

def dumnums2(nums):
    """
    nums为1~n范围内的整数数组，长度为n+1，找出nums中的重复元素；
    要求不改变原数组，且空间复杂度为1，时间复杂度小于N2
    :param nums:
    :return:
    """
    low = 1
    high = len(nums) - 1
    while low < high: # 不要等于
        count = 0
        middle = int(1/2*(low+high))
        for n in nums:
            if n <= middle:
                count += 1
        if count > middle:
            high = middle
        else:
            low = middle + 1
    return low
if __name__ == "__main__":
    # print(dum([1,0]))
    print(dumnums2([1,1,3,2,4]))
