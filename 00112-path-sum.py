# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        stack = [(root, root.val)]
        while stack:
            p, currentSum = stack.pop()
            
            if p.left == p.right and currentSum == targetSum:
                return True
            
            if p.left:
                stack.append((p.left, currentSum + p.left.val))
                
            if p.right:
                stack.append((p.right, currentSum + p.right.val))
                
        return False
        
        
        
        