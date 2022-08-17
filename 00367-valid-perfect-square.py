class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num
        while lo <= hi:
            mid     = (lo + hi) >> 1
            mid_sqr = mid ** 2
            if mid_sqr == num:
                return True
            elif mid_sqr < num:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return False