class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        MAX_INT = 10 ** 9
        adj_lists = {u: [] for u in range(1, n + 1)}
        for u, v, time in times:
            adj_lists[u].append((v, time))
            
        arrived_time    = [MAX_INT] * (n + 1)
        arrived_time[k] = 0

        locked = [False] * (n + 1)
        
        candidates = set([k])
        while candidates:
            min_val = MAX_INT
            u       = None
            for candidate in candidates:
                if arrived_time[candidate] < min_val:
                    min_val = arrived_time[candidate]
                    u       = candidate
            
            locked[u] = True
            candidates.remove(u)    
            for v, time in adj_lists[u]:
                if not locked[v]:
                    if arrived_time[v] == MAX_INT:
                        candidates.add(v)
                        arrived_time[v] =     arrived_time[u] + time
                    else:
                        arrived_time[v] = min(arrived_time[u] + time, arrived_time[v])
                
        result = max(arrived_time[1:])
        return -1 if result == MAX_INT else result