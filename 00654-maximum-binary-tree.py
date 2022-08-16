# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None
        
        max_val = max(nums)
        max_idx = nums.index(max_val)

                
        print(nums, max_val, max_idx)
                
        lst = None if max_idx == 0     else self.constructMaximumBinaryTree(nums[0:max_idx]    )
        rst = None if max_idx == n - 1 else self.constructMaximumBinaryTree(nums[max_idx + 1:n])
        
        return TreeNode(max_val, lst, rst)
        