# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        return self.recPathSum(root, sum, [], [])

    def recPathSum(self, root: 'TreeNode', sum: 'int', result, globalResult):
        
        if root == None:
            return []
        elif root.right == None and root.left == None :
            if sum == root.val:
                result.append(root.val)
                globalResult.append(result)
            return globalResult
        else:
            leftResult = list(result)
            leftResult.append(root.val) 
            rightResult = list(result)
            rightResult.append(root.val) 
            self.recPathSum(root.left, sum - root.val, leftResult, globalResult) 
            self.recPathSum(root.right, sum - root.val, rightResult, globalResult) 
            return globalResult
