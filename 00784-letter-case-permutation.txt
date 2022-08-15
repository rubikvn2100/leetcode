class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        str_arr = [c.lower() for c in s]
        
        result_lists = ["".join(str_arr)]
        while True:
            i = 0
            while i < n:
                if str_arr[i].islower():
                    str_arr[i] = str_arr[i].upper()
                    break
                else:
                    str_arr[i] = str_arr[i].lower()
                i += 1
            if i == n:
                break
            result_lists.append("".join(str_arr))
                
        return result_lists