# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        current_level = [root]
        result_lists  = [[root.val]]
        while True:
            next_level = []
            for p in current_level:
                if p.left:
                    next_level.append(p.left)
                if p.right:
                    next_level.append(p.right)
                    
            if len(next_level) == 0:
                break
            else:
                result_lists.append([p.val for p in next_level])
                current_level = next_level
            
        return result_lists
            
                    
        