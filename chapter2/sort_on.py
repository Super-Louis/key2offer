# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: sort_on.py
# Python  : python3.6
# Time    : 18-9-28 00:31

"""
实现一个排序算法，要求时间效率为O(N)
"""

def sort_on(ages):
    # 排序O(N)
    # 已知年龄上限（且上限较小，远小于待排序数组长度）
    # 另外采用一个计数数组
    # 将年龄作为下标，计数作为该年龄出现的次数
    # 根据有序的下标实现原数组的排序
    if len(ages) <= 1:
        return ages
    age_count = [0 for _ in range(100)] # 假设年龄为0~99岁
    for age in ages:
        age_count[age] += 1
    sorted_ages = []
    for i, count in enumerate(age_count):
        if count > 0:
            sorted_ages += [i] * count
    return sorted_ages

if __name__ == '__main__':
    print(sort_on([3,2,11,2,3,44,5,11]))
