# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameStructure(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if (not root and subRoot) or (root and not subRoot):
                return False
            if not root and not subRoot:
                return True
            if root.val != subRoot.val:
                return False
            
            if not isSameStructure(root.left, subRoot.left):
                return False 
            if not isSameStructure(root.right, subRoot.right):
                return False

            return True 
        
        if isSameStructure(root, subRoot):
            return True 
        
        if not root:
            return False
        if self.isSubtree(root.left, subRoot):
            return True        
        if self.isSubtree(root.right , subRoot):
            return True
        
        return False