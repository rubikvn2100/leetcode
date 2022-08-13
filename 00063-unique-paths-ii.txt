class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid   )
        m = len(obstacleGrid[0])
        dp_arr = [[0] * m for _ in range(n)]
            
        dp_arr[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 0:
                    dp_arr[i][j] += dp_arr[i - 1][j    ] if i > 0 else 0
                    dp_arr[i][j] += dp_arr[i    ][j - 1] if j > 0 else 0
        
        return dp_arr[n - 1][m - 1]