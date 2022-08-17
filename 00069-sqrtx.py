class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        while lo <= hi:
            if lo + 1 == hi:
                return hi if hi * hi == x else lo
            
            mid     = (lo + hi) >> 1
            mid_sqr = mid * mid
            if mid_sqr == x:
                return mid
            elif mid_sqr < x:
                lo = mid
            else:
                hi = mid
            