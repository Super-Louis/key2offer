# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: symmetry_tree.py
# Python  : python3.6
# Time    : 18-10-8 23:55

"""
题目二十八：对称的二叉树
"""
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.lchild = left
        self.rchild = right

def is_symmetric(tree):
    list1 = []
    list2 = []
    pre_travels(tree, list1)
    print('\n')
    pre_travels_rev(tree, list2)
    return list1 == list2

def pre_travels(tree, list):
    if tree:
        print(tree.val, end=' ')
        list.append(tree.val)
        pre_travels(tree.lchild, list)
        pre_travels(tree.rchild, list)
    else:
        print(None, end=' ')
        list.append(None)

def pre_travels_rev(tree, list):
    if tree:
        print(tree.val, end=' ')
        list.append(tree.val)
        pre_travels_rev(tree.rchild, list)
        pre_travels_rev(tree.lchild, list)
    else:
        print(None, end=' ')
        list.append(None)

if __name__ == '__main__':
    tree = None
    print(is_symmetric(tree))