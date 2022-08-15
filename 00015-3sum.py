class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        location_dict = {}
        for i, num in enumerate(nums):
            location_dict[num] = i
            
        triplet_set = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                inv_sum = -(nums[i] + nums[j])
                if inv_sum in location_dict and location_dict[inv_sum] > j:
                    triplet_set.add((nums[i], nums[j], inv_sum))
                    
        return [list(triplet) for triplet in triplet_set]        