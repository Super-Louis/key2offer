# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: tree2ll.py
# Python  : python3.6
# Time    : 19-1-15 10:53

"""
面试题36：二叉搜索树与双向链表
题目：输入一颗二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。
"""

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Convert():
    def __init__(self):
        self.lh = None
        self.lt = None

    def convert(self, tree):
        if not tree:
            return None
        self.convert(tree.left)
        if not self.lh: # left-most-node
            # lh, lt引用同一个对象
            # lt的变化会同时影响tree及lh的变化
            self.lh = tree
            self.lt = tree
        else: # root node
            # 此时lt表示上一节点，tree表示当前节点
            # lt.right设置为当前节点
            self.lt.right = tree
            temp = self.lt
            # tree.left = self.lt
            # lt更新为当前节点
            # lt.left设置为上一节点
            self.lt = tree
            self.lt.left = temp
        self.convert(tree.right)
        return self.lh

def printll(ll):
    while ll and ll.right:
        print(ll.val)
        ll = ll.right
    while ll and ll.left:
        print(ll.val)
        ll = ll.left
    print(ll.val)
if __name__ == '__main__':
    tree = Node(10, Node(6, Node(4), Node(8)), Node(14, Node(12), Node(16)))
    ll = Convert().convert(tree)
    printll(ll)


