"""
题目：从上到下打印二叉树
题：不分行从上到下打印二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
例如：输入下图的二叉树
    8
    / \
    6  10
    / \ / \
    5 7 9 11
则依次打印出8, 6, 10, 5, 7, 9, 11。
"""
from queue import Queue
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def level_order(self, start):
        if start is None:
            return
        queue = Queue()
        queue.put(start)
        while not queue.empty():
            node = queue.get()
            print(node.value, end=" ")
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
 

if __name__ == "__main__":
    # 初始化一个二叉树
    tree = BinaryTree(8)
    tree.root.left = Node(6)
    tree.root.right = Node(10)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(7)
    tree.root.right.left = Node(9)
    tree.root.right.right = Node(11)
    tree.level_order(tree.root)
    # Expected output: 8 6 10 5 7 9 11