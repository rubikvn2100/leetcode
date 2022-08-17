class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] ** 2
            
        min_idx = nums.index(min(nums))
        result= [nums[min_idx]]
        
        p = min_idx + 1
        q = min_idx - 1
        while q >= 0 or p < n:
            if q == -1:
                result.append(nums[p])
                p += 1
                continue 
            
            if p == n:
                result.append(nums[q])
                q -= 1
                continue
               
            if nums[p] < nums[q]:
                result.append(nums[p])
                p += 1
            else:
                result.append(nums[q])
                q -= 1
               
        return result
               
              
        