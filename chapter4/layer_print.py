# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: layer_print.py
# Python  : python3.6
# Time    : 19-1-11 22:45

"""
分行从上到下打印二叉树
"""

class Node:
    def __init__(self, val, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

def layer_print(tree):
    if not tree:
        return None
    queue = [tree]
    to_be_print = 1
    next_layers = 0
    while queue:
        node = queue[0]
        print(node.val, end=' ')
        del queue[0]
        to_be_print -= 1
        if node.lchild:
            queue.append(node.lchild)
            next_layers += 1
        if node.rchild:
            queue.append(node.rchild)
            next_layers += 1
        if to_be_print == 0:
            print('\n')
            to_be_print = next_layers
            next_layers = 0

def layer_travelsal(l):
    if not l:
        return []
    res = [[l.val]]
    queues = [l]
    while queues:
        queues_ = []
        for n in queues:
            if n.lchild:
                queues_.append(n.lchild)
            if n.rchild:
                queues_.append(n.rchild)
        queues = queues_
        if queues:
            res.append([q.val for q in queues])
    return res

            
if __name__ == '__main__':
    tree = Node(8, Node(8, Node(9), Node(2)), Node(7, Node(3), Node(4)))
    layer_print(tree)
    print(layer_travelsal(tree))