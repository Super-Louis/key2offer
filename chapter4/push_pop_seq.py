# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: push_pop_seq.py
# Python  : python3.6
# Time    : 18-10-11 00:17

"""
面试题三十一：栈的压入，弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否为该栈的弹出顺序，
假设压入栈的所有数字均不相等
"""

class Stack():
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def top(self):
        assert len(self.items) > 0
        return self.items[-1]

    def isempty(self):
        return len(self.items) == 0

def is_in_order(push_seq, pop_seq):

    if len(push_seq) != len(pop_seq):
        return False
    new_stack = Stack()
    j = 0
    for i in pop_seq:
        if new_stack.isempty() or new_stack.top() != i:
            found = False
            for jj in range(j, len(push_seq)):
                if push_seq[jj] != i:
                    new_stack.push(push_seq[jj])
                else:
                    found = True
                    j = jj + 1
                    break
            if not found:
                return False
        else:
            new_stack.pop()
    return True

def ispushandpop(l1, l2):
    temp = []
    for i in l2:
        while not temp or temp[-1] != i:
            if not l1:
                return False
            temp.append(l1[0])
            del l1[0]
        temp.pop()
    return temp == []

def is_inorder(l1, l2):
    new_stack = []
    i = 0 # 表示l1中当前待插入的位置
    for j in l2:
        # 只要new_stack最后一个元素不等于当前l2中的元素
        # 或new_stack为空，则一直插入
        while not new_stack or new_stack[-1] != j:
            if i >= len(l1): # 如果待插入位置大于等于了l1长度则为false
                return False
            new_stack.append(l1[i])
            i += 1
        new_stack.pop() # new_stack最后一个元素不等于当前l2中的元素，将其pop掉
    return new_stack == [] # 当最终了new_stack抵消了之后，返回True

if __name__ == '__main__':
    print(is_in_order([1,2,3,4,5],[4,3,6,2,1]))
    print(ispushandpop([1,2,3,4,5],[4,3,6,2,1]))