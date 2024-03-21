""""
序列化二叉树
题目：请实现两个函数，分别用来序列化和反序列化二叉树
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def serialize(self, root):
        if not root:
            return "$"
        else:
            return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
    
    def deserialize(self, data: str):
        """
        从字符串重建二叉树
        """
        def deserialize_core():
            val = next(vals)
            if val == "$":
                return None
            root = TreeNode(int(val))
            root.left = deserialize_core()
            root.right = deserialize_core()
            return root
        vals = iter(data.split(","))
        return deserialize_core()
    

if __name__ == "__main__":
    # 初始化一个二叉树
    tree = TreeNode(8)
    tree.left = TreeNode(6)
    tree.right = TreeNode(10)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(7)
    tree.right.left = TreeNode(9)
    tree.right.right = TreeNode(11)
    solution = Solution()
    s = solution.serialize(tree)
    print(s)
    # Expected output: 8,6,5,$,$,7,$,$,10,9,$,$,11,$,$
    tree = solution.deserialize(s)
    print(tree)
    # Expected output: <__main__.TreeNode object at 0x7f9b4a0a5f10>
    print(tree.val)
    # Expected output: 8
    print(tree.left.val)
    # Expected output: 6
    print(tree.right.val)
    # Expected output: 10
    print(tree.left.left.val)
    # Expected output: 5
    print(tree.left.right.val)
    # Expected output: 7
    print(tree.right.left.val)
    # Expected output: 9
    print(tree.right.right.val)
    # Expected output: 11
    print(tree.left.left.left)
    # Expected output: None
    print(tree.left.left.right)
    # Expected output: None
    print(tree.left.right.left)
    # Expected output: None
    print(tree.left.right.right)
    # Expected output: None
    print(tree.right.left.left)
    # Expected output: None
    print(tree.right.left.right)
    # Expected output: None
    print(tree.right.right.left)
    # Expected output: None
    print(tree.right.right.right)
    # Expected output: None
    s = solution.serialize(None)
    print(s)
    # Expected output: $
    tree = solution.deserialize(s)
    print(tree)
    # Expected output: None
    s = solution.serialize(TreeNode(1))
    print(s)
    # Expected output: 1,$,$
    tree = solution.deserialize(s)
    print(tree)
    # Expected output: <__main__.TreeNode object at 0x7f9b4a0a5f10>
    print(tree.val)
    # Expected output: 1
    print(tree.left)
    # Expected output: None
    print(tree.right)
    # Expected output: None