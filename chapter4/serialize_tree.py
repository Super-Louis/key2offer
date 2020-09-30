# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: serialize_tree.py
# Python  : python3.6
# Time    : 19-1-15 12:25

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(tree, result):
    if not tree:
        result.append('$')
        return
    result.append(tree.val)
    serialize(tree.left, result)
    serialize(tree.right, result)
    return result

def deserialize(result):
    if len(result) <= 0:
        return None
    root = None
    val = result.pop(0) # 第一个为根节点，左右节点都在根节点后面
    if val != '$':
        root = Node(val)
        root.left = deserialize(result)
        root.right = deserialize(result)
    return root

def printt(tree):
    if tree:
        print(tree.val)
        printt(tree.left)
        printt(tree.right)

if __name__ == '__main__':
    tree = Node(1, Node(2, Node(4)), Node(3, Node(5), Node(6)))
    result = []
    serialize(tree, result)
    print(result)
    tree = deserialize(result)
    printt(tree)
