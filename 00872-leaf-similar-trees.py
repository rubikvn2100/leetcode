# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def extractLeaves(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return []
            
            if not root.left and not root.right:
                return [root.val]
            
            lst_leaves = extractLeaves(root.left ) if root.left  else []
            rst_leaves = extractLeaves(root.right) if root.right else []
        
            return lst_leaves + rst_leaves
        
        leaves1 = extractLeaves(root1)
        leaves2 = extractLeaves(root2)
        
        if len(leaves1) != len(leaves2):
            return False 
        
        return leaves1 == leaves2