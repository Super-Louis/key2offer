# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: sum_path.py
# Python  : python3.6
# Time    : 19-1-14 10:03

"""
面试题34：二叉树中和为某一值的路径
题目：输入一颗二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
"""

class TreeNode():
    def __init__(self, val, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

def findpath(root, target):
    if not root:
        return None
    paths = []
    current_path = [] # current_path
    sums = 0 # current_sum
    find_path_in_tree(root, target, paths, current_path, sums)
    return paths

def find_path_in_tree(root, target, paths, current_path, sums):
    if root:
        sums += root.val
        current_path.append(root.val) # 每次进入find_path_in_tree增加一个节点
        if sums > target:
            return

        if not (root.lchild or root.rchild): # 叶节点
            if sums == target: # 和等于target
                # current_path在后面会发生变化，所以应该用切片！！！
                paths.append(current_path[:])
            else: # 和小于target
                return
        else: # 非叶节点
            # if root.lchild:
            find_path_in_tree(root.lchild, target, paths, current_path, sums)
            # 每次退出find_path_in_tree，current_path相应的要删除一个子节点
            # sums为局部变量，因此不用改变，current_path进入子节点后会发生变化
            current_path.pop()
            # if root.rchild:
            find_path_in_tree(root.rchild, target, paths, current_path, sums)
            # current_path.pop()

if __name__ == '__main__':
    tree = TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(2, TreeNode(5), TreeNode(2, TreeNode(3))))
    print(findpath(tree, 9))