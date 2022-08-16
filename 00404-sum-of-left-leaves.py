# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode], isLeftChild: bool) -> int:
            if not root:
                return 0
            
            if not root.left and not root.right:
                return root.val if isLeftChild else 0
            
            return helper(root.left, True) + helper(root.right, False)
        
        return helper(root, False)
                
            