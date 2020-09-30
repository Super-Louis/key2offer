# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: first_common_node.py
# Python  : python3.6
# Time    : 19-1-27 11:59

"""
面试题52：两个链表的第一个公共节点
题目：输入两个链表，找出他们的第一个公共节点。
"""
"""
链表有公共节点，则从公共节点开始，后面的节点都是相同的
因此可以用栈存储节点，然后从后遍历，直至第一个不同节点出现
或者将两个链表长度移至相同，然后开始同时遍历，直至出现第一个相同节点
"""
class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def first_common_node(l1, l2):
    s1 = []
    s2 = []
    n = None
    while l1:
        s1.append(l1)
        l1 = l1.next
    while l2:
        s2.append(l2)
        l2 = l2.next
    min_len = min(len(s1), len(s2))
    found = False
    for i in range(-1, -min_len-1, -1):
        if s1[i].val != s2[i].val:
            found = True
            break
    # 三种情况，都不同，都相同，有不同有相同
    if i != -1 and found:
        n = s1[i+1]
    if not found:
        n = s2[i]
    return n

def first_common_node2(l1, l2):
    lens1 = get_lens(l1)
    lens2 = get_lens(l2)
    if lens1 > lens2:
        while lens1 > lens2:
            l1 = l1.next
            lens1 -= 1
    if lens2 > lens1:
        while lens2 > lens1:
            l2 = l2.next
    while l1 and l2 and l1.val != l2.val:
        l1 = l1.next
        l2 = l2.next
    if not l1:
        return None
    return l1


def get_lens(l):
    lens = 0
    while l:
        lens += 1
        l = l.next
    return lens

if __name__ == '__main__':
    l1 = Node(2, Node(3, Node(4)))
    l2 = Node(2, Node(3, Node(4)))
    print(first_common_node(l1, l2))
    print(first_common_node2(l1, l2))
