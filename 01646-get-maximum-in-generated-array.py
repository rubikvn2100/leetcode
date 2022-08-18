class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        nums    = [0] * (n + 1) 
        nums[1] = 1
        max_val = 1
        for i in range(2, n + 1):
            half_i = i >> 1
            if i & 1 == 1:
                nums[i] = nums[half_i] + nums[half_i + 1]
            else:
                nums[i] = nums[half_i]
            max_val = max(max_val, nums[i])
            
        return max_val