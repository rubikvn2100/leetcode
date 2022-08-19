class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq_dict = {num: 0 for num in arr2}
        arr = []
        
        for num in arr1:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                arr.append(num)
                
        result_arr = []
        for num in arr2:
            result_arr += [num] * freq_dict[num]
        
        arr.sort()
        result_arr += arr
        
        return result_arr