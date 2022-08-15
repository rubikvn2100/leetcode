class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        arrive = [d / s for d, s in zip(dist, speed)]
        arrive.sort()
        
        maxKill = 0
        for i in range(n):
            if arrive[i] > i:
                maxKill = i + 1
            else:
                break
                
        return maxKill