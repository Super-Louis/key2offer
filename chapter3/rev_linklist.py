# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: rev_linklist.py
# Python  : python3.6
# Time    : 18-10-3 17:13

"""
题目二十四：反转链表
定义一个函数，输入一个链表的头节点，
反转该链表并输出翻转后链表的头节点
"""

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def rev(ll):
    if not ll:
        return None
    pre = None
    cur = ll
    next = ll.next
    while next:
        cur.next = pre
        pre = cur
        cur = next
        next = next.next
    return cur

def print_ll(ll):
    while ll:
        print(ll.val)
        ll = ll.next

if __name__ == '__main__':
    ll = Node(1, Node(2, Node(3)))
    rl = rev(ll)
    print_ll(rl)