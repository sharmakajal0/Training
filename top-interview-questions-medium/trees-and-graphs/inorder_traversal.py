#!/usr/bin/python3

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        self.inorder(root, ret)
        return ret


    def inorder(self, root: Optional[TreeNode], ret):
        if root:
            self.inorder(root.left)
            ret.append(root.val)
            self.inorder(root.right)