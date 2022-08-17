# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        if not root.left and not root.right:
            return f'''{root.val}'''
        
        lst_result = self.tree2str(root.left )
        rst_result = self.tree2str(root.right)
        if root.left and root.right:
            return f'''{root.val}({lst_result})({rst_result})'''
        
        if lst_result is "":
            return f'''{root.val}()({rst_result})'''    
        
        return f'''{root.val}({lst_result})'''