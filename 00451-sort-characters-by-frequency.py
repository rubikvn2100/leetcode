class Solution:
    def frequencySort(self, s: str) -> str:
        freq_dict = {}
        for char in s:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char]  = 1
                
        freq_list = [(char, freq) for char, freq in freq_dict.items()]
        freq_list.sort(reverse = True, key = lambda x: x[1])
        
        result_str = ""
        for char, freq in freq_list:
            result_str += char * freq
            
        return result_str