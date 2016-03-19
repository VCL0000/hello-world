class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self, node):
        self.head = node
        self.head.next = None  # 指针
        self.tail = self.head  # 初始化的时候表尾和表头是重合的

    def add(self, node):
        self.tail.next = node
        self.tail = self.tail.next

    def view(self):
        node = self.head
        linkstr = ''
        while node is not None:
            if node.next is not None:
                linkstr = linkstr + str(node.data) + "-->"
            else:
                linkstr += str(node.data)
            node = node.next
        print(linkstr)
