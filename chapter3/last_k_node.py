# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: last_k_node.py
# Python  : python3.6
# Time    : 18-10-2 22:11

"""
题目二十二：链表中倒数第k个节点
输入一个链表，输出该链表中倒数第K个节点
"""
class LinkNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def last_k_node(linklist, k):
    """
    双指针
    特殊情况处理，增强代码鲁棒性
    1.linklist为空；2.k为0 ；3.linklist长度小于k
    :param linklist:
    :return:
    """
    if not linklist:
        return None
    if k == 0:
        return None
    i, j = 1, 1
    node = linklist
    while i < k and node: # 当第一个指针到第k个节点时，第二个指针开始运动
        i += 1
        node = node.next
    if not node:
        return None
    current = linklist
    while node.next: # 当第一个指针到达最后一个节点（非None）时第二个指针停止
        node = node.next
        current = current.next
    return current.val

def middle_node(linklist):
    """
    双指针
    输出链表中间节点
    1.linklist为空；2.k为0
    :param linklist:
    :return:
    """
    if not linklist:
        return None
    first, second = linklist, linklist
    while second and second.next: # 当第一个指针到第k个节点时，第二个指针开始运动
        second = second.next.next
        first = first.next
    return first.val

if __name__ == '__main__':
    ll = LinkNode(1, LinkNode(2, LinkNode(3)))
    print(middle_node(ll))

