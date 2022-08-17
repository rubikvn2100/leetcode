class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        
        weight_freq = [[people[0], 1]]
        for weight in people[1:]:
            if weight_freq[-1][0] == weight:
                weight_freq[-1][1] += 1
            else:
                weight_freq.append([weight, 1])
        
        p_start = 0
        p_end   = len(weight_freq) - 1
        
        boat_counter = 0
        while p_start < p_end:
            total_weight = weight_freq[p_start][0] + weight_freq[p_end][0]
            if total_weight > limit:
                boat_counter += weight_freq[p_end][1]
                weight_freq[p_end][1] = 0
                p_end -= 1
            else: 
                amount = min(weight_freq[p_start][1], weight_freq[p_end][1])
                boat_counter += amount
                
                weight_freq[p_start][1] -= amount
                if weight_freq[p_start][1] == 0:
                    p_start += 1
                    
                weight_freq[p_end][1] -= amount
                if weight_freq[p_end][1] == 0:
                    p_end -= 1
           
        if p_start == p_end:
            if limit >= 2 * weight_freq[p_start][0]:
                boat_counter += weight_freq[p_start][1] >> 1
                boat_counter += weight_freq[p_start][1]  % 2
            else:
                boat_counter += weight_freq[p_start][1] 
            
        return boat_counter