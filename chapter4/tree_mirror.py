# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: tree_mirror.py
# Python  : python3.6
# Time    : 18-10-8 23:10

"""
题目二十七：二叉树的镜像
请完成一个函数，输入一颗二叉树，该函数输出他的镜像
"""
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.lchild = left
        self.rchild = right

def mirror_tree(tree):
    # 画图，将镜像过程画出来
    if not tree:
        return None
    left = tree.lchild
    right = tree.rchild
    tree.lchild = right
    tree.rchild = left
    mirror_tree(tree.lchild)
    mirror_tree(tree.rchild)
    return tree

def print_tree(tree):
    if tree:
        print(tree.val, end=' ')
        print_tree(tree.lchild)
        print_tree(tree.rchild)

if __name__ == '__main__':
    tree = TreeNode(8, TreeNode(8, TreeNode(9), TreeNode(2, TreeNode(4), TreeNode(7))), TreeNode(7))
    print_tree(tree)
    mtree = mirror_tree(tree)
    print('\n')
    print_tree(mtree)