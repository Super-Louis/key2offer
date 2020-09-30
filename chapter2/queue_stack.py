# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: queue_stack.py
# Python  : python3.6
# Time    : 18-9-24 18:06

"""
题目九：
用两个栈实现队列
用两个队列实现栈
"""

class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Stack():
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class StackQueue():
    # stack to queue
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        # 始终入队到stack1
        self.stack1.push(data)

    def dequeue(self):
        if not (self.stack1 or self.stack2):
            raise IndexError
        elif self.stack2.size():
            return self.stack2.pop() # 始终从stack2出队
        else:
            while self.stack1.size():
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()


class QueueStack():
    # queue to stack
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, data):
        self.queue1.enqueue(data)

    def pop(self):
        # 直至某队列中只剩最后一个元素后才pop
        if self.queue1.size() == 1: # 先判断queue1，因为始终向queue1中插入
            return self.queue1.dequeue()
        elif self.queue2.size() == 1:
            return self.queue2.dequeue()
        elif self.queue1.size():
            while self.queue1.size() != 1:
                self.queue2.enqueue(self.queue1.dequeue())
            return self.queue1.dequeue()
        else:
            while self.queue2.size() != 1:
                self.queue1.enqueue(self.queue2.dequeue())
            return self.queue2.dequeue()

if __name__ == '__main__':
    qs = StackQueue()
    qs.enqueue(1)
    qs.enqueue(2)
    qs.enqueue(3)
    print(qs.dequeue())
    print(qs.dequeue())
    qs.enqueue(4)
    qs.enqueue(5)
    print(qs.dequeue())
    print(qs.dequeue())


