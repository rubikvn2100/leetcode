class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_arr = [[0] * m for _ in range(n)]
        for i in range(n):
            dp_arr[i][0] = 1
            
        for j in range(m):
            dp_arr[0][j] = 1
            
        for i in range(1, n):
            for j in range(1, m):
                dp_arr[i][j] = dp_arr[i - 1][j] + dp_arr[i][j - 1]
                
        return dp_arr[n - 1][m - 1]