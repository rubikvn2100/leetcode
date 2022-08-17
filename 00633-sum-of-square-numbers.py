class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        half_c = c >> 1
        a     = 0
        a_sqr = a ** 2
        b     = int(sqrt(c - a_sqr))
        b_sqr = b ** 2
        while a <= b:
            while a_sqr + b_sqr > c:
                b    -= 1
                b_sqr = b** 2
              
            if a_sqr + b_sqr == c:
                return True
    
            a    += 1
            a_sqr = a ** 2
              
            if a_sqr + b_sqr == c:
                return True
            
        return False
            
        