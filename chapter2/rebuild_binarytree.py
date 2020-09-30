# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: rebuild_binarytree.py
# Python  : python3.6
# Time    : 18-9-24 15:43

"""
题目七：重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
"""

class TreeNode():
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

def rebuild(l_p, l_m):
    if not (l_p and l_m):
        return None
    root = l_p[0]
    tree = TreeNode(root)
    left_len = l_m.index(root)
    tree.lchild = rebuild(l_p[1:1+left_len], l_m[:left_len])
    tree.rchild = rebuild(l_p[1+left_len:], l_m[1+left_len:])
    return tree

def print_tree(tree):
    if not tree:
        return
    print(tree.data)
    print_tree(tree.lchild)
    print_tree(tree.rchild)

if __name__ == '__main__':
    l_p = [1,2,4,7,3,5,6,8]
    l_m = [4,7,2,1,5,3,8,6]
    T = rebuild(l_p, l_m)
    print_tree(T)