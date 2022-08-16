# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return [10**9, -10**9, 10**9]
            
            lst_min, lst_max, lst_min_diff = helper(root.left )
            rst_min, rst_max, rst_min_diff = helper(root.right)
            
            min_val  = min(lst_min, root.val)
            max_val  = max(rst_max, root.val)
            min_diff = min(lst_min_diff, rst_min_diff, root.val - lst_max, rst_min - root.val)
            
            return [min_val, max_val, min_diff]
        
        _, _, min_diff = helper(root)
        return min_diff
        