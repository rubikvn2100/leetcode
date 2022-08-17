class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        q, p = 0, len(people) - 1
        
        boat_counter = 0
        while q <= p:
            boat_counter += 1
            if people[q] + people[p] <= limit:
                q += 1
            p -= 1
        
        return boat_counter