# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: tree_depth.py
# Python  : python3.6
# Time    : 19-1-30 11:26

# 面试题55：二叉树的深度
"""
题目一：二叉树的深度
输入一颗二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）
形成树的一条路径，最长路径的长度为树的深度
"""
def tree_depth(tree):
    if not tree:
        return 0
    left = tree_depth(tree.left)
    right = tree_depth(tree.right)
    return max(left, right) + 1

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
题目二：平衡二叉树
输入一颗二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左、右子树的深度相差不超过1，
那么它就是一颗平衡二叉树
"""
def is_balanced(tree):
    if not tree:
        return True
    left_depth = tree_depth(tree.left)
    right_depth = tree_depth(tree.right)
    if abs(left_depth - right_depth) > 1:
        return False
    return is_balanced(tree.left) and is_balanced(tree.right)

def is_balanced2(tree):
    # 采用后序遍历，左-右-中
    # 避免重复判断节点深度
    if not tree:
        return True, 0
    left_result, left_depth = is_balanced2(tree.left)
    if not left_result:
        return False, 0
    right_result, right_depth = is_balanced2(tree.right)
    if not right_result:
        return False, 0
    diff = abs(left_depth - right_depth)
    if diff <= 1:
        return True, max(left_depth, right_depth) + 1
    return False, 0




if __name__ == '__main__':
    tree = TreeNode(5, TreeNode(3, TreeNode(2),TreeNode(5, TreeNode(7,TreeNode(8)), TreeNode(8))), TreeNode(7, TreeNode(6), TreeNode(8)))
    tree2 = TreeNode(1)
    print(tree_depth(tree2))
    print(is_balanced2(tree))

