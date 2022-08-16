class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        current_set = {i for i in range(1, 10)}
        for _ in range(n - 1):
            new_set = set()
            for num in current_set:
                last_digit = num % 10
                
                new_digit = last_digit + k
                if new_digit <= 9:
                    new_set.add(num * 10 + new_digit)
                    
                new_digit = last_digit - k
                if new_digit >= 0:
                    new_set.add(num * 10 + new_digit)
                    
            current_set = new_set
            
        return current_set
            
                
        