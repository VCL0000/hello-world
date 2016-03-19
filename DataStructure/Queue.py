# 先进先出 后进后出
from logging import exception


class Queue():
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.head = -1
        self.tail = -1

    def enQueue(self, content):
        if self.isFull():
            raise exception("Queue is Full")
        else:
            self.tail += 1
            self.queue.append(content)

    def outQueue(self):
        if self.isEmpty():
            raise exception("Queue is Empty")
        else:
            self.head += 1
            return self.queue[self.tail]


    def isFull(self):
        if self.head - self.tail + 1 == self.size:  # 注1
            return True
        else:
            return False

    def isEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False
"""
注1
i = -1
1 - i
    0
"""
