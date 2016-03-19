from DataStructure import Stack
from DataStructure import Queue
from DataStructure import BinaryTree
from DataStructure import LinkList

ss = Stack.Stack(10)
ss.push(ss)
ss.push(55)
print(ss.out())
print(ss.out())
print(ss.isEmpty())

bb = Queue.Queue(2)
bb.enQueue(66)
bb.enQueue(77)
print(bb.outQueue())
print(bb.outQueue())
print(bb.isEmpty())
print("--------")

ll = BinaryTree.BinaryTreeNode(2, None, None)
rr = BinaryTree.BinaryTreeNode(3, None, None)
node = BinaryTree.BinaryTreeNode(1, ll, rr)
tree = BinaryTree.BinaryTree(node)
tree.preOrder(tree.data)
print("------")
tree.inOrder(tree.data)

print("--------")
node1 = LinkList.Node(7)
node2 = LinkList.Node("hello")
node3 = LinkList.Node(8899)
lls = LinkList.LinkList(node1)
lls.add(node2)
lls.add(node3)
lls.view()