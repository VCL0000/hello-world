from DataStructure import Stack
from DataStructure import Queue
from DataStructure import BinaryTree
from DataStructure import LinkList
from DataStructure import QuickSort
from DataStructure import SelectionSort
from DataStructure import BubbleSort
from DataStructure import BinarySearch

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
lls.Insert(node2)
lls.Insert(node3)
lls.Print()
print("--------")

array = [8, 7, 6, 5, 9, 3, 1]
print(array)
QuickSort.quick_sort(array, 0, len(array) - 1)
print(array)

print("--------")
arr = [4, 3, 1, 9, 5, 2]
print(arr)
SelectionSort.selection_sort(arr)
print(arr)
print("--------")

arr = [3, 5, 6, 8, 7, 9, 1]
print(arr)
BubbleSort.BubbleSort(arr)
print(arr)
print("--------")

arr = [1, 2, 3, 5, 7, 8]
index = BinarySearch.BinarySearch(arr, 4)
print(index)
