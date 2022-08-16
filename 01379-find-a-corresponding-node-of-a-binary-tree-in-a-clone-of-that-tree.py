# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original: 
            return None
        
        if original == target:
            return cloned
        
        lst_resutl = self.getTargetCopy(original.left , cloned.left , target)
        if lst_resutl is not None:
            return lst_resutl
        
        rst_resutl = self.getTargetCopy(original.right, cloned.right, target)
        if rst_resutl is not None:
            return rst_resutl
  
        return None
