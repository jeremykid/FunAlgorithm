# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = float('-inf')
        self.diff = float('inf')
        self.inorder(root)
        return self.diff
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.diff = min(self.diff,abs(node.val - self.prev))
            self.prev = node.val
            self.inorder(node.right)