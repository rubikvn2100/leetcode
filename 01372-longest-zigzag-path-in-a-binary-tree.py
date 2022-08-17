# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode], longestTrack: int, fromLeft: bool) -> int:
            if not root:
                return longestTrack - 1
            
            if fromLeft:
                lst_result = helper(root.left , longestTrack + 1, False)
                rst_result = helper(root.right,                1, True )
            else:            
                lst_result = helper(root.left ,                1, False )
                rst_result = helper(root.right, longestTrack + 1, True)
                
            return max(lst_result, rst_result)
        
        lst_result = helper(root.left , 1, False)
        rst_result = helper(root.right, 1, True )
        return max(lst_result, rst_result)
        