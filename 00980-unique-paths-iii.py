class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid   ) 
        m = len(grid[0])
        visited = [[True if grid[i][j] == -1 else False for j in range(m)] for i in range(n)]
        
        startX, startY = None, None
        num_nonObstacle = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    startX, startY = i, j
                num_nonObstacle += 1 if grid[i][j] != -1 else 0

        def helper(x: int, y: int, step: int) -> int:
            if not(0 <= x and x < n and 0 <= y and y < m):
                return 0
            
            if visited[x][y]:
                return 0
            
            if grid[x][y] == 2:
                return 1 if step == num_nonObstacle else 0

            visited[x][y] = True
            total  = helper(x + 1, y    , step + 1)
            total += helper(x - 1, y    , step + 1)
            total += helper(x    , y + 1, step + 1)
            total += helper(x    , y - 1, step + 1)
            visited[x][y] = False
            
            return total
            

                    
        return helper(startX, startY, 1)