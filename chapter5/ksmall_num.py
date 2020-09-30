# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: ksmall_num.py
# Python  : python3.6
# Time    : 19-1-18 10:41

"""
面试题40：最小的K个数
题目：输入n个整数，找出其中最小的K个数。
例如，输入4,5,1,6,2,7,3,8这8个数字，
则最小的4个数字是1\2\3\4
"""

def find_ksmall(l, k):
    if not l or len(l) < k:
        return None
    le = 0
    ri = len(l) - 1
    i = partition(l, le, ri)
    while i != k-1:
        if i > k-1:
            i = partition(l, le, i-1)
        else:
            i = partition(l, i+1, ri)
    return l[:k]

def partition(l, le, ri):
    if le >= ri:
        return None
    base = le
    while le < ri:
        while l[ri] >= l[base] and le < ri:
            ri -= 1
        while l[le] <= l[base] and le < ri:
            le += 1
        l[le], l[ri] = l[ri], l[le]
    l[base], l[le] = l[le], l[base]
    return le

def ksmall2(l, k):
    # 利用python中的最小堆来实现
    # python中heapq实现了最小堆
    # heap[0]永远是最小数
    if len(l) < k:
        return None
    import heapq
    a = []
    for i in l:
        i = -i
        if len(a) < k:
            heapq.heappush(a, i)
        else:
            # heappushpop先插入，然后删除最小的数
            # 由于都取了-，所以相当于删除最大数
            # 不能用heapqreplace(item, a)
            # 不能用heapqreplace，其相当于先heappop删掉最小数
            # 再heappush插入item
            heapq.heappushpop(a, i)
    return [-i for i in a]



if __name__ == '__main__':
    print(find_ksmall([4,5,1,6,2,7,3,8], 4))
    print(find_ksmall([4,-5,1,6,2,7,3,8], 4))