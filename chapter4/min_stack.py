# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: min_stack.py
# Python  : python3.6
# Time    : 18-10-10 23:39

"""
面试题三十：包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小值
的min函数。在该栈中，调用min/push及pop的时间复杂度均为O(1)
"""

class MinStack():
    def __init__(self):
        self.items = []
        self.mins = [] # 辅助栈，用于存放最小值

    def push(self, item):
        if not self.mins or item < self.mins[-1]:
            self.mins.append(item)
        else:
            self.mins.append(self.mins[-1])
        self.items.append(item)

    def pop(self):
        self.mins.pop()
        return self.items.pop()

    def min(self):
        assert len(self.mins) > 1
        return self.mins[-1]

if __name__ == '__main__':
    ms = MinStack()
    ms.push(2)
    ms.push(3)
    ms.push(1)
    ms.push(4)
    print(ms.min())
    ms.pop()
    print(ms.min())
    ms.pop()
    print(ms.min())
