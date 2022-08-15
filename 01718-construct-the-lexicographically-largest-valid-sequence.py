class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        len_result_array = 2 * n - 1
        result_array     = [None] * len_result_array
        is_used = [False] * (n + 1)
    
        def DFS(k: int):
            if k == len_result_array:
                return result_array
            
            def next_empty_spot(k: int) -> int:
                k += 1
                while k < len_result_array:
                    if result_array[k] is None:
                        break
                    k += 1 
                return k

            for i in range(2, min(n + 1, len_result_array - k ))[::-1]:
                if not is_used[i] and not result_array[k + i]:
                    result_array[k    ] = i
                    result_array[k + i] = i        
                    is_used[i] = True

                    result = DFS(next_empty_spot(k))
                    if result:
                        return result

                    result_array[k    ] = None
                    result_array[k + i] = None
                    is_used[i] = False

                    
            if not is_used[1]:
                result_array[k] = 1
                is_used[1] = True

                result = DFS(next_empty_spot(k))
                if result:
                    return result

                result_array[k] = None
                is_used[1] = False
                
            return False
                    
        
        return DFS(0)