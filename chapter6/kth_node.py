# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: kth_node.py
# Python  : python3.6
# Time    : 19-1-30 10:23

"""
面试题54：二叉搜索树的第k大节点
题目：给定一颗二叉搜索树，请找出其中第k大的节点。
例如，在图6.1中的二叉搜索树里，按节点数值大小顺序，
第三大节点的值是4.
"""

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_node(tree, k):
    if not tree:
        return None
    l = []
    def find(tree):
        if len(l) == k:
            return
        if tree:
            find(tree.left)
            if len(l) < k: # 注意，此时只有长度小于k才能加，否则会面会继续递归
                l.append(tree.val)
            find(tree.right)
    find(tree)
    if len(l) < k:
        return None
    return l[-1]

if __name__ == '__main__':
    tree = TreeNode(5, TreeNode(3, TreeNode(2)), TreeNode(7, TreeNode(6), TreeNode(8)))
    print(kth_node(tree, 7))
