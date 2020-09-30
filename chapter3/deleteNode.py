# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: deleteNode.py
# Python  : python3.6
# Time    : 18-10-2 16:47

"""
题目十八：删除链表的节点
在O(1)时间内删除链表节点，给定单向链表的头指针和一个节点的指针，
定义一个函数在O(1)时间内删除该节点
"""

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def delete_node(linklist, Node):
    # 已知链表头指针及某一节点指针，删除该节点
    # 算法1：顺序遍历，直到找到要删除的节点，将该节点前一节点指向待删除节点的下一节点，事件复杂度为O(N)
    # 算法2：将待删除节点的下一节点的值赋予待删除节点，将下一节点删除（将待删除节点指向下一节点的下一节点）
    # 特殊情况：a.链表只有一个节点; b.待删除节点为末尾节点
    # 假设：该节点一定在链表中
    if linklist.next == None and linklist.val == Node.val:
        return None
    if Node.next != None:
        Node.val = Node.next.val
        Node.next = Node.next.next
    else:
        # 遍历到尾部，然后删除该节点
        pre = linklist
        current = pre.next
        while current:
            if current.val == Node.val:
                pre.next = current.next
                break
            else:
                pre = current
                current = current.next

    return linklist

def delete_node2(ll, node):
    if node.next != None:
        node.val = node.next.val
        node.next = node.next.next
    else:
        if ll.next == None:
            return None
        else:
            pre = None
            cur = ll
            while cur.next:
                pre = cur
                cur = cur.next
            pre.next = None
    return ll

def print_l(ll):
    while ll:
        print(ll.val)
        ll = ll.next

if __name__ == '__main__':
    ll = Node(1,Node(2, Node(3)))
    ll = delete_node2(ll, ll.next.next)
    print_l(ll)
