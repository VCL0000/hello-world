# 先进后出 后进先出

# stack.pop()  #取出数据   从最后取
from logging import exception


class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def push(self, content):
        if self.isFull():
            raise exception("Stack is Full")
        else:
            self.stack.append(content)
            self.top += 1

    def out(self):
        if self.isEmpty():
            raise exception("Stack is Empty")
        else:
            self.top -= 1
            return self.stack.pop()

    def isFull(self):
        if self.top == self.size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False


class Queue(object):
    pass
