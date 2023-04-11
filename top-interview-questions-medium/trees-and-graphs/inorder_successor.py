#!/usr/bin/python3

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def insert(self, node: TreeNode, data: int):
        if node is None:
            return TreeNode(data)
        else:
            if data <= node.data:
                temp = self.insert(node.left, data)
                node.left = temp

class Solution:
    def inOrderSuccessor(self, root: Optional[TreeNode], p: TreeNode):
        succ = None

        while root:
            if root.val > p.val:
                succ = root
                root = root.left
            else:
                root = root.right
        
        return succ


root = TreeNode(20)
root