# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: linklist.py
# Python  : python3.6
# Time    : 18-9-24 11:21

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def append_node(node, val):
    """在尾部添加"""
    # todo: 处理node为空/None的情况, 返回linklist? 定义linklist的头指针？
    pre = node
    current = node
    while current:
        pre = current
        current = current.next
    pre.next = Node(val)

def delete_node(node, val):
    # todo: 处理node为空/None/只有一个元素的情况, 返回linklist? 定义linklist的头指针？
    pre = node
    current = node.next
    while current:
        if current.val == val:
            pre.next = current.next
            break
        else:
            pre = current
            current = current.next


def print_ll(ll):
    while ll:
        print(ll.val)
        ll = ll.next
if __name__ == '__main__':
    ll = Node(3, Node(1, Node(2)))
    append_node(ll, 4)
    print_ll(ll)
    delete_node(ll, 1)
    print_ll(ll)