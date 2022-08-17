class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        
        freq_dict_s1     = {char: 0 for char in s1 + s2}
        freq_dict_sub_s2 = {char: 0 for char in s1 + s2}
        for i in range(n):
            freq_dict_s1[s1[i]]     += 1
            freq_dict_sub_s2[s2[i]] += 1
                
        freq_diff_counter = 0
        for char in freq_dict_s1.keys():
            if freq_dict_s1[char] != freq_dict_sub_s2[char]:
                freq_diff_counter += 1
        
        if freq_diff_counter == 0:
            return True
                
        k = n
        while k < m:
            remove_char = s2[k - n]
            if freq_dict_s1[remove_char] == freq_dict_sub_s2[remove_char]:
                freq_diff_counter += 1
                
            freq_dict_sub_s2[remove_char] -= 1
            if freq_dict_s1[remove_char] == freq_dict_sub_s2[remove_char]:
                freq_diff_counter -= 1
                
            add_char = s2[k]
            if freq_dict_s1[add_char] == freq_dict_sub_s2[add_char]:
                freq_diff_counter += 1
                
            freq_dict_sub_s2[add_char] += 1
            if freq_dict_s1[add_char] == freq_dict_sub_s2[add_char]:
                freq_diff_counter -= 1
                             
            if freq_diff_counter == 0:
                return True 
            k += 1
                             
        return False