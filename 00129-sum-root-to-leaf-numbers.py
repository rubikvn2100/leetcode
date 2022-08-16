# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode], createdNum: int) -> int:
            if not root:
                return 0
            
            newCreatedNum = createdNum * 10 + root.val
            if not root.left and not root.right:
                return newCreatedNum
            
            return helper(root.left, newCreatedNum) + helper(root.right, newCreatedNum)
        
        return helper(root, 0)