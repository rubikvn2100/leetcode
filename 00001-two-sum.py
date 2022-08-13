/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    hashmap = {};
    for(let i = 0; i < nums.length; i++)
    {
        if(hashmap[target - nums[i]] !== undefined)
            return [hashmap[target - nums[i]], i];
        hashmap[nums[i]] = i;
    }
    
    return null;
};