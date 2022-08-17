# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def longestPath(head: Optional[ListNode], root: Optional[TreeNode]) -> int:
            if not head and not root:
                return 0
            
            if head:
                head.val = [head.val, longestPath(head.next, None) + 1]
                return head.val[1]
                            
            if root:
                lst_result = longestPath(None, root.left )
                rst_result = longestPath(None, root.right)
                root.val = [root.val, max(lst_result, rst_result) + 1]
                return root.val[1]
                       
        def helper(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
            def hasPathFromRoot(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
                if not head:
                    return True

                if not root:
                    return False

                if head.val[0] != root.val[0]:
                    return False

                if head.val[1] > root.val[1]:
                    print("stop")
                    return False

                return hasPathFromRoot(head.next, root.left) or hasPathFromRoot(head.next, root.right)

            if not root:
                return False

            if hasPathFromRoot(head, root):
                return True
            
            return helper(head, root.left) or helper(head, root.right)
            
        longestPath(head, None)
        longestPath(None, root)
        return helper(head, root)