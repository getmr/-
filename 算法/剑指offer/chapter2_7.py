# 重构二叉树
"""
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
示例
            3
           /  \
        9       20
               /   \
            15       7
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(preorder: List[int], inorder: List[int]):
    inorder_dict = {v: k for k, v in enumerate(inorder)}
    def f(a, b, len_arr):
        if len_arr < 1:
            return None
        root = TreeNode(preorder[a])
        root_value = preorder[a]  # root节点值
        inorder_root_index = inorder_dict[root]  # root节点在中序遍历的索引
        left_len = root_value - b  # 左子树的长度
        root.left = f(a+1, b, left_len)
        root.right = f(a + 1 + left_len, inorder_root_index+1, len_arr - left_len - 1)
    return f(0, 0, len(preorder))
        
