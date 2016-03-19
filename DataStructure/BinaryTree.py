class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):  # 初始化为None 不传参数为None
        self.left = left
        self.right = right
        self.data = data


class BinaryTree:
    def __init__(self, data=None):
        self.data = data

    def isEmpty(self):
        if self.data is None:
            return True
        else:
            return False

    """前序遍历 root left right"""

    def preOrder(self, node):
        if node is None:
            return
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)

    """中序遍历 left root right"""

    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data)
        self.inOrder(node.right)

    """后序遍历  left right root"""

    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data)
