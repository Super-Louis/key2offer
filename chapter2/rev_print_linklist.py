# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: rev_print_linklist.py
# Python  : python3.6
# Time    : 18-9-24 14:50

"""
题目六：从尾到头打印链表
输入一个链表的头节点，从尾到头反过来打印每个节点的值
"""

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def rev_print(ll):
    stack = list()
    while ll:
        node = ll
        stack.append(node)
        ll = ll.next
    while stack:
        node = stack.pop()
        print(node.val)

def rev_print_recur(ll):
    if not ll:
        return
    rev_print_recur(ll.next) # 先print next，再print current，实现逆序
    print(ll.val)

if __name__ == '__main__':
    ll = Node(1, Node(2, Node(3, Node(4))))
    rev_print_recur(ll)
