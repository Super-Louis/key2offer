# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: child_tree.py
# Python  : python3.6
# Time    : 18-10-8 22:19

"""
题目二十六：树的子结构
输入两颗二叉树，判断B是不是A的子结构
"""

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.lchild = left
        self.rchild = right

def is_child(tree1, tree2):
    """
    步骤一：先找到tree1中等于tree2根节点的节点
    步骤二：判断子树是否相等
    :param tree1:
    :param tree2:
    :return:
    """
    result = False
    if not (tree1 and tree2):
        return False
    if tree1.val == tree2.val:
        result = hassametree(tree1, tree2)
    if not result:
        result = is_child(tree1.lchild, tree2)
    if not result:
        result = is_child(tree1.rchild, tree2)
    return result

def hassametree(tree1, tree2):
    if not tree2:
        return True
    if not tree1:
        return False
    if not tree1.val == tree2.val:
        return False
    return hassametree(tree1.lchild, tree2.lchild) and \
           hassametree(tree1.rchild, tree2.rchild)

if __name__ == '__main__':
    tree1 = TreeNode(8, TreeNode(8, TreeNode(9), TreeNode(2, TreeNode(4), TreeNode(7))), TreeNode(7))
    tree2 = TreeNode(8, TreeNode(9), TreeNode(3))
    print(is_child(tree1, tree2))
