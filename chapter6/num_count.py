# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: num_count.py
# Python  : python3.6
# Time    : 19-1-28 20:43

"""
面试题53：在排序数组中查找数字
统计一个数字在排序数组中出现的次数。例如，输入排序数组
{1,2,3,3,3,3,4,5}和数字3，由于3在这个数组中出现了4次，
因此输出4
"""

def num_count(nums, target):
    """
    利用二分查找，时间复杂度为O(logn)
    如果直接遍历，时间复杂度为O(n)
    """
    if not nums:
        return 0
    low = 0
    high = len(nums) - 1
    first = 0
    found = False
    while low <= high:
        middle = int(1/2*(low+high))
        if nums[middle] == target:
            if middle == 0 or nums[middle-1] != target:
                first = middle
                found = True
                break
            else:
                high = middle - 1
        elif nums[middle] > target:
            high = middle - 1
        else:
            low = middle + 1

    low = 0
    high = len(nums) - 1
    last = 0
    while low <= high:
        middle = int(1 / 2 * (low + high))
        if nums[middle] == target:
            if middle == len(nums) - 1 or nums[middle + 1] != target:
                last = middle
                found = True
                break
            else:
                low = middle + 1
        elif nums[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    if not found: # 不存在！
        return 0
    return last - first + 1

"""
题目二：0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，
并且每个数字都在范围0～n-1之内。在范围0～n-1内的
n个数字中有且只有一个数字不在该数组中，请找出这个数字
"""

def find_miss_num(nums):
    if not nums:
        return None
    low, high = 0, len(nums) - 1
    first = 0
    while low <= high:
        middle = int(1/2*(low+high))
        if middle != nums[middle]:
            if middle == 0 or middle - 1 == nums[middle-1]: # 注意有可能第一个就不等于
                first = middle
                break
            else:
                high = middle - 1
        else:
            low = middle + 1
    if low > high: # 数组中不存在不等于的情况，只有可能是最大值缺失
        return low
    return first

"""
题目三：数组中数值和下标相等的元素
假设一个单调递增的数组里的每个元素都是整数并且是唯一的。
请编程实现一个函数，找出数组中任意一个数值等于其下标的元素。
例如，在数组{-3,1,1,3,5}中，数字3和它的下标相等
"""
def find_index(l):
    if not l:
        return None
    left = 0
    right = len(l) - 1
    while left <= right:
        middle = int(1/2*(left+right))
        if middle == l[middle]:
            return middle
        elif middle < l[middle]:
            right -= 1
        else:
            left += 1
    return None

if __name__ == '__main__':
    print(num_count([1], 2))
    print(find_miss_num([0,1,2]))
    print(find_index([-3,-1,1,2,4]))


