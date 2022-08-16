# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def constructSegmentTree(start: int, end: int) -> Optional[TreeNode]:
            # Each node val will contain:
            # 1/ Start index of the segment
            # 2/ Ending index of the segment
            # 3/ Max value in the sement
            if start > end:
                return None 
            
            if start == end:
                return TreeNode([start, start, nums[start], start])

            mid = (start + end) >> 1 
            lst = constructSegmentTree(start  , mid)
            rst = constructSegmentTree(mid + 1, end)            
            
            _, _, max_val, max_idx = lst.val
            if max_val < rst.val[2]:
                _, _, max_val, max_idx = rst.val
            
            return TreeNode([start, end, max_val, max_idx], lst, rst)
        
        def findMax(root: Optional[TreeNode], start: int, end: int) -> List[int]:
            if not root:
                return [-10**9, None]
            
            segment_start, segment_end, segment_max_val, segment_max_idx = root.val
            if segment_end < start or end < segment_start:
                return [-10**9, None]
            
            if start <= segment_start and segment_end <= end:
                return [segment_max_val, segment_max_idx]
            
            lst_max_val, lst_max_idx = findMax(root.left , start, end)
            rst_max_val, rst_max_idx = findMax(root.right, start, end)
            if lst_max_val > rst_max_val:
                return [lst_max_val, lst_max_idx]
            else:
                return [rst_max_val, rst_max_idx]
        
        maxSegmentTree = constructSegmentTree(0, len(nums) - 1)
        def helper(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            
            if start == end:
                return TreeNode(nums[start], None, None)
                
            max_val, max_idx = findMax(maxSegmentTree, start, end)
            
            lst = None if max_idx == start else helper(start      , max_idx - 1)
            rst = None if max_idx == end   else helper(max_idx + 1, end        )
            
            return TreeNode(max_val, lst, rst)
        
        return helper(0, len(nums) - 1)
            
        