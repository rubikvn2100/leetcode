# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        seq = []
        def inOrderTraversal(root: TreeNode) -> None:
            if root.left:
                inOrderTraversal(root.left)
            
            seq.append(root.val)
            
            if root.right:
                inOrderTraversal(root.right)
                
        inOrderTraversal(root)
        result_root = TreeNode(seq[0])
        p = result_root
        for val in seq[1:]:
            p.right = TreeNode(val)
            p = p.right
            
        return result_root
                
        