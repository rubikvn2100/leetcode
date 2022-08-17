# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        globalVar = {"aggregateSum": 0}
        def reverseInOrderTraversal(root: Optional[TreeNode]) -> None:
            if not root:
                return
            
            if root.right:
                reverseInOrderTraversal(root.right)
            
            root.val += globalVar["aggregateSum"]
            globalVar["aggregateSum"] = root.val
            
            if root.left:
                reverseInOrderTraversal(root.left)
                
        reverseInOrderTraversal(root)
        return root
        