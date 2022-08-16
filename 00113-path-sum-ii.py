# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        if not root.left and not root.right:
            if root.val == targetSum:
                return [[root.val]]
            else:
                return []
            
        lst_result = self.pathSum(root.left,  targetSum - root.val)            
        rst_result = self.pathSum(root.right, targetSum - root.val)
        
        return [[root.val] + lst for lst in lst_result + rst_result]
        