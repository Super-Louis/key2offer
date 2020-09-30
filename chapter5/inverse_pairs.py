# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: inverse_pairs.py
# Python  : python3.6
# Time    : 19-1-27 09:57

"""
面试题51：数组中的逆序对
题目：在数组中的两个数字，如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。输入一个数组，求出这个数组中
的逆序对的总数。例如，在数组{7,5,6,4}中，一共存在5个
逆序对：（7,6），（7,5），（7,4），（6,4），（5,4）
"""
def inverse_pairs(l):
    if len(l) <= 1:
        return 0, l
    lens = len(l)
    m = int(1/2*lens)
    left_count, left = inverse_pairs(l[:m])
    right_count, right = inverse_pairs(l[m:])
    merge_count, merged = merge(left, right)
    return left_count + right_count + merge_count, merged

def merge(left, right):
    merged = []
    count = 0
    i, j = 0, 0
    # left, right均为升序排列
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(right[j])
            j += 1
            # 若li > rj，则l中剩余元素都大于rj
            # 因为此时j已经加了1，因此l后面的元素将不会再与j进行比较
            count += len(left) - i
        else:
            merged.append(left[i])
            i += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return count, merged

if __name__ == '__main__':
    print(inverse_pairs([7,5,6,6]))
