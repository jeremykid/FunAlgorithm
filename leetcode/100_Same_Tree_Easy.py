# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':        
        if p == None and q == None:
            return True
        elif (p == None and q != None) or (q == None and p != None):
            return False
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)  
        else:
            return False
