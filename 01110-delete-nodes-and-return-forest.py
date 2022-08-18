# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = []
        to_delete_set = set(to_delete)
        def helper(root: Optional[TreeNode], has_parent: bool) -> bool:
            if not root:
                return False
            
            if root.val in to_delete_set:
                if root.left:  helper(root.left , False)
                if root.right: helper(root.right, False)
                to_delete_set.remove(root.val)
                return False
            
            if not has_parent: 
                forest.append(root)
            
            if not helper(root.left , True): root.left  = None
            if not helper(root.right, True): root.right = None
            
            return True
        
        helper(root, False)
        return forest
            