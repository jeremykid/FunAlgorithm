# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        if root == None:
            return False
        elif root.right == None and root.left == None :
            return sum == root.val
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val) 
