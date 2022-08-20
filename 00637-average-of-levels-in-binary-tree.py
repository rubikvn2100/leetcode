# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        class LevelData:
            def __init__(self, level = 0):
                self.sum = 0
                self.count = 0
                self.level = level
                
        max_level = 0
        statistic = []
        def helper(root: Optional[TreeNode], level: int) -> None:
            if not root:
                return
            
            if level > len(statistic) - 1:
                statistic.append(LevelData(level))
                
            statistic[level].sum   += root.val
            statistic[level].count += 1
            
            if root.left:
                helper(root.left, level + 1)
            
            if root.right:
                helper(root.right, level + 1)
                
        helper(root, 0)
        return [stat.sum / stat.count for stat in statistic]