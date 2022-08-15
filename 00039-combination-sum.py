class Solution
    def combinationSum(self, candidates List[int], target int) - List[List[int]]
        n = len(candidates)
        candidates.sort()
        temp_holder = [None]  (int(target  candidates[0]) + 1)
        
        result_lists = []
        def DFS(k int, remaining_sum int)
            if remaining_sum == 0
                result_lists.append([candidates[temp_holder[i]] for i in range(k)])
                
            lower_bound = 0 if k == 0 else temp_holder[k - 1]
            for i in range(lower_bound, n)
                if candidates[i] = remaining_sum
                    temp_holder[k] = i
                    DFS(k + 1, remaining_sum - candidates[i])
                else
                    break
                    
        DFS(0, target)
        return result_lists
                    
            