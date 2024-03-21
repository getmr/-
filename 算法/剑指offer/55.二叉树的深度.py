"""
二叉树的深度
题目：输入一棵二叉树的根节点，求该树的深度
解题思路：跟节点的深度等于左右子树的大的加一，所以可以使用递归的方式
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tree_depth(root: TreeNode):
    if root is None:
        return 0
    n_left = tree_depth(root.left)
    n_right = tree_depth(root.right)

    return (n_left + 1) if n_left > n_right else n_right + 1


if __name__ == "__main__":
    tree_node = TreeNode(1)
    tree_node.left = TreeNode(2)
    tree_node.left.left = TreeNode(4)
    tree_node.left.right = TreeNode(5)
    tree_node.left.right.left = TreeNode(7)

    tree_node.right = TreeNode(3)
    tree_node.right.right = TreeNode(6)

    print(tree_depth(tree_node))