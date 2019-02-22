# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        return self.hasPathSum(root, sum, sum, 0)

    def hasPathSum(self, root: 'TreeNode', sum: 'int', originalSum: 'int', dirty: 'int'):
        if root == None:
            return 0
        elif root.right == None and root.left == None :
            return int(sum == root.val)
        else:
            result = int(sum == root.val) + self.hasPathSum(root.left, sum - root.val, originalSum, 1) + self.hasPathSum(root.right, sum - root.val, originalSum, 1)
            if (not dirty):
                result = result + self.hasPathSum(root.left, originalSum, originalSum, 0) + self.hasPathSum(root.right, originalSum, originalSum, 0) 
            return result
