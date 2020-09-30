# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: loop_entrance.py
# Python  : python3.6
# Time    : 18-10-3 16:08

"""
题目二十三：链表中环的入口节点
如果一个链表中包含环，如何找到环的入口节点？
"""

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# todo：链表中存在多个环？
def loop_len(ll):
    i, j = ll, ll
    has_loop = False
    while i and i.next:
        i = i.next.next
        j = j.next
        if i == j:
            has_loop = True
            break
    if not has_loop: # 处理链表中无环的情况
        return None
    count = 1
    val = j.val
    while j.next.val != val:
        j = j.next
        count += 1
    return count

def get_entrance(ll):
    loop_length = loop_len(ll)
    i, j = ll, ll
    for _ in range(loop_length):
        i = i.next
    while i != j:
        i = i.next
        j =j.next
    return i

