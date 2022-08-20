# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        class LevelData:
            def __init__(self, initMaxVal, level = 0):
                self.max = initMaxVal
                self.level = 0
                
        statistic = []
        def helper(root: Optional[TreeNode], level: int) -> None:
            if not root:
                return
            
            if level > len(statistic) - 1:
                statistic.append(LevelData(root.val, level))
            else:
                statistic[level].max = max(statistic[level].max, root.val)
            
            if root.left:  helper(root.left , level + 1)
            if root.right: helper(root.right, level + 1)
                
            return 
        
        helper(root, 0)
        return [stat.max for stat in statistic]
        