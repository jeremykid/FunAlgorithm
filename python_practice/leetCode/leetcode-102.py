# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root == None:
            return result
        parentNodes = [root];
        
        while (len(parentNodes) > 0):
            levelVals = []
            nextParentNodes = []
            for i in parentNodes:

                levelVals.append(i.val)

                if (i.left != None):
                    nextParentNodes.append(i.left)

                if (i.right != None):
                    nextParentNodes.append(i.right)

            
            result.append(levelVals)
            parentNodes = nextParentNodes
        return result

