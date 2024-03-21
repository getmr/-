"""
二叉树转换成双向链表
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        self.pLastNodeInList = None
        self.ConvertNode(pRootOfTree)
        pHeadOfList = self.pLastNodeInList
        while pHeadOfList and pHeadOfList.left:
            pHeadOfList = pHeadOfList.left
        return pHeadOfList

    def ConvertNode(self, pNode):
        if not pNode:
            return
        pCurrent = pNode
        if pCurrent.left:
            self.ConvertNode(pCurrent.left)
        pCurrent.left = self.pLastNodeInList
        if self.pLastNodeInList:
            self.pLastNodeInList.right = pCurrent
        self.pLastNodeInList = pCurrent
        if pCurrent.right:
            self.ConvertNode(pCurrent.right)