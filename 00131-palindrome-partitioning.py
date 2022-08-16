class Solution
    def partition(self, s str) - List[List[str]]
        n = len(s)
        def isPalindrome(s str) - bool
            for i in range(len(s)  1)
                if s[i] != s[len(s) - 1 - i]
                    return False
            return True
        
        palindrome_dict = {i[] for i in range(n)}
        for i in range(n)
            for j in range(i + 1, n + 1)
                if isPalindrome(s[ij])
                    palindrome_dict[i].append(j)
                    
        def DFS(k int, lst List[str]) - List[List[str]]
            if k == n
                return [[sub_str for sub_str in lst]]
            
            result_lst = []
            for j in palindrome_dict[k]
                lst.append(s[kj])
                result_lst += DFS(j, lst)
                lst.pop()
                
            return result_lst
        
        return DFS(0, [])
            
                